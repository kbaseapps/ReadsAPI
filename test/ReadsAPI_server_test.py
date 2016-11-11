# -*- coding: utf-8 -*-
import unittest
import os
import json
import time
import requests
import string
import random

from os import environ

try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint

from biokbase.workspace.client import Workspace as workspaceService
from ReadsAPI.ReadsAPIImpl import ReadsAPI
from ReadsAPI.ReadsAPIServer import MethodContext


class ReadsAPITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        user_id = requests.post(
            'https://kbase.us/services/authorization/Sessions/Login',
            data='token={}&fields=user_id'.format(token)).json()['user_id']
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'ReadsAPI',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('ReadsAPI'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = ReadsAPI(cls.cfg)
    
    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')
    
    def getWsClient(self):
        return self.__class__.wsClient
    
    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_ReadsAPI_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})
        self.__class__.wsName = wsName
        return wsName
    
    def getImpl(self):
        return self.__class__.serviceImpl
    
    def getContext(self):
        return self.__class__.ctx
    
    # NOTE: According to Python unittest naming rules test method names should start from 'test'.
    
    def test_get_id_ok(self):
        ws_obj_names = self.load_test_data_ok()
        
        readssetparams = {}
        
        readssetparams['workspace_id'] = ws_obj_names[0]  #'marcin:1475008857456'
        readssetparams['name'] = ws_obj_names[3]  #'ERR000916'
        
        result = self.getImpl().get_id(self.getContext(), readssetparams)
        print('RESULT test_get_id_ok:')
        pprint(result)
        
        self.assertEqual(result, [1])
    
    def test_get_name_ok(self):
        ws_obj_names = self.load_test_data_ok()
        
        readssetparams = {}
        
        readssetparams['workspace_id'] = ws_obj_names[0]  #'marcin:1475008857456'
        readssetparams['id'] = ws_obj_names[1]  #'ERR000916'
        
        #objid = self.getImpl().get_id(self.getContext(),readssetparams)
        #readssetparams['id'] = objid[0]
        
        result = self.getImpl().get_name(self.getContext(), readssetparams)
        print('RESULT test_get_name_ok:')
        pprint(result)
        
        self.assertEqual(result, [u'test_paired_reads_eautils'])
    
    def test_get_type_ok(self):
        ws_obj_names = self.load_test_data_ok()
        
        readssetparams = {}
        
        readssetparams['workspace_id'] = ws_obj_names[0]  #'marcin:1475008857456'
        readssetparams['id'] = ws_obj_names[1]  #'ERR000916'
        
        #objid = self.getImpl().get_id(self.getContext(), readssetparams)
        #readssetparams['id'] = objid[0]
        
        result = self.getImpl().get_type(self.getContext(), readssetparams)
        print('RESULT test_get_type_ok:')
        pprint(result)
        
        self.assertEqual(result, [u'KBaseFile.PairedEndLibrary-2.2'])
    
    def create_random_string(self):
        N = 20
        return ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
    
    def load_test_data_ok(self):
        
        test_file = "test_paired_reads_eautils.json"
        with open("../test_data/" + test_file) as json_file:
            data = json.load(json_file)
        
        #print(json.dumps(data, sort_keys=True, indent=2))
        
        token = environ.get('KB_AUTH_TOKEN', None)
        
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('ReadsAPI'):
            cfg[nameval[0]] = nameval[1]
        wsURL = cfg['workspace-url']
        
        wsClient = workspaceService(wsURL, token=token)
        
        test_ws_name = self.create_random_string()
        test_obj_name = 'test_paired_reads_eautils'
        
        try:
            ret = wsClient.create_workspace({'workspace': test_ws_name})
        except Exception as inst:
            print "ERROR"
            print(type(inst))
            print(inst.args)
            print(inst)
        
        summary_provenance = [{
            "description": "Saving object " + test_obj_name + " to WS"
        }]
        
        summary_save_info = wsClient.save_objects({"workspace": test_ws_name,
                                                   "objects": [{"type": "KBaseFile.PairedEndLibrary",
                                                                "data": data,
                                                                "name": test_obj_name,
                                                                "hidden": 0,
                                                                "provenance": summary_provenance}]})
        print "SAVED NEW OBJECT"
        
        ret = [summary_save_info[0][6], summary_save_info[0][0], summary_save_info[0][7], summary_save_info[0][1]]
        print ret
        
        return ret
    
    def load_test_data_empty(self):
        
        test_file = "test_paired_reads_eautils_empty.json"
        with open("../test_data/" + test_file) as json_file:
            data = json.load(json_file)
        
        #print(json.dumps(data, sort_keys=True, indent=2))
        
        token = environ.get('KB_AUTH_TOKEN', None)
        
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('ReadsAPI'):
            cfg[nameval[0]] = nameval[1]
        wsURL = cfg['workspace-url']
        
        wsClient = workspaceService(wsURL, token=token)
        
        test_ws_name = self.create_random_string()
        test_obj_name = 'test_paired_reads_eautils'
        
        try:
            ret = wsClient.create_workspace({'workspace': test_ws_name})
        except Exception as inst:
            #print "ERROR"
            #print(type(inst))
            #print(inst.args)
            #print(inst)
            pass
        
        summary_provenance = [{
            "description": "Saving object " + test_obj_name + " to WS"
        }]
        
        summary_save_info = wsClient.save_objects({"workspace": test_ws_name,
                                                   "objects": [{"type": "KBaseFile.PairedEndLibrary",
                                                                "data": data,
                                                                "name": test_obj_name,
                                                                "hidden": 0,
                                                                "provenance": summary_provenance}]})
        print "SAVED NEW MINIMAL OBJECT"
        print "summary_save_info " + str(summary_save_info)
        
        ret = [summary_save_info[0][6], summary_save_info[0][0], summary_save_info[0][7], summary_save_info[0][1]]
        print ret
        
        return ret
    
    def test_get_reads_info_all_ok(self):
        
        ws_obj_names = self.load_test_data_ok()
        
        readssetparams = {}
        
        readssetparams['workspace_id'] = ws_obj_names[0]  #'kbasetest:1477429140721'
        readssetparams['id'] = ws_obj_names[1]  #'test_paired_reads_eautils'
        
        #objid = self.getImpl().get_id(self.getContext(), readssetparams)
        #readssetparams['id'] = objid[0]
        
        result = self.getImpl().get_reads_info_all_formatted(self.getContext(), readssetparams)
        print('RESULT test_get_reads_info_all_ok:')
        pprint(result)
                
        testresult = [{'Insert_Size_Std_Dev': 'Not Specified', 'Phred_Type': '33', 'Number_of_Duplicate_Reads': '792(0%)',
                       'Name': u'test_paired_reads_eautils', 'Strain': 'Not Specified', 'GC_Percentage': '67.93%',
                       'Type': 'Paired End', 'Read_Length_Std_Dev': '0.0', 'Insert_Size_Mean': 'Not Specified',
                       'Quality_Score_Mean_Std_Dev': '43.05(10.54)', 'Mean_Read_Length': '100.0',
                       'Quality_Score_Min_Max': '10.0/51.0', 'Total_Number_of_Bases': 'Not Specified',
                       'Source': 'Not Specified', 'Base_Percentages': 'A(16.07%), C(33.95%), G(33.97%), T(16.0%), N(0.0%)',
                       'Single_Genome': 'Yes', 'Platform': u'seqtech-pr1', 'workspace_name':u'' + str(ws_obj_names[2]),
                       'Number_of_Reads': '25,000', 'id': 1, 'Outward_Read_Orientation': 'No'}]
        
        self.assertEqual(sorted(result), sorted(testresult))
    
    def test_get_reads_info_all_minimal_ok(self):
        
        ws_obj_names = self.load_test_data_empty()
        
        readssetparams = {}
        
        readssetparams['workspace_id'] = ws_obj_names[0]  #'kbasetest:1477429140721'
        readssetparams['id'] = ws_obj_names[1]  #'test_paired_reads_eautils'
        
        #objid = self.getImpl().get_id(self.getContext(), readssetparams)
        #readssetparams['id'] = objid[0]
        
        result = self.getImpl().get_reads_info_all_formatted(self.getContext(), readssetparams)
        print('RESULT test_get_reads_info_all_minimal:')
        pprint(result)
        
        testresult = [{'Insert_Size_Std_Dev': 'Not Specified', 'Phred_Type': 'Not Specified',
                       'Number_of_Duplicate_Reads': 'Not Specified', 'Name': u'test_paired_reads_eautils',
                       'Strain': 'Not Specified', 'GC_Percentage': 'Not Specified', 'Type': 'Paired End',
                       'Read_Length_Std_Dev': 'Not Specified', 'Insert_Size_Mean': 'Not Specified',
                       'Quality_Score_Mean_Std_Dev': 'Not Specified', 'Mean_Read_Length': 'Not Specified',
                       'Quality_Score_Min_Max': 'Not Specified', 'Total_Number_of_Bases': 'Not Specified',
                       'Source': 'Not Specified', 'Base_Percentages': 'Not Specified', 'Single_Genome': 'Not Specified',
                       'Platform': u'seqtech-pr1', 'workspace_name': u'' + str(ws_obj_names[2]),
                       'Number_of_Reads': 'Not Specified', 'id': 1, 'Outward_Read_Orientation': 'Not Specified'}]
        
        self.assertEqual(sorted(result), sorted(testresult))
    
    def test_get_reads_info_all_minimal_by_ref_ok(self):
        
        ws_obj_names = self.load_test_data_empty()
        
        objref = str(ws_obj_names[0]) + "/" + str(ws_obj_names[1])
        
        params = {}
        params['workspace_obj_ref'] = objref
        
        result = self.getImpl().get_reads_info_all_formatted(self.getContext(), params)
        print('RESULT test_get_reads_info_all_minimal:')
        pprint(result)
        
        testresult = [{'Insert_Size_Std_Dev': 'Not Specified', 'Phred_Type': 'Not Specified',
                        'Number_of_Duplicate_Reads': 'Not Specified', 'Name': u'test_paired_reads_eautils',
                        'Strain': 'Not Specified', 'GC_Percentage': 'Not Specified', 'Type': 'Paired End',
                        'Read_Length_Std_Dev': 'Not Specified', 'Insert_Size_Mean': 'Not Specified',
                        'Quality_Score_Mean_Std_Dev': 'Not Specified', 'Mean_Read_Length': 'Not Specified',
                        'Quality_Score_Min_Max': 'Not Specified', 'Total_Number_of_Bases': 'Not Specified',
                        'Source': 'Not Specified', 'Base_Percentages': 'Not Specified', 'Single_Genome': 'Not Specified',
                        'Platform': u'seqtech-pr1', 'workspace_name': u'' + str(ws_obj_names[2]),
                        'Number_of_Reads': 'Not Specified', 'id': 1, 'Outward_Read_Orientation': 'Not Specified'}]
        self.assertEqual(sorted(result), sorted(testresult))
