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
        
        result = self.getImpl().get_reads_info_all(self.getContext(), readssetparams)
        print('RESULT test_get_reads_info_all_ok:')
        pprint(result)
        
        testresult = [
            {'read_count': '25000', 'total_bases': '', 'insert_size_mean': 'None', 'qual_min': '10.0', 'strain': '',
             'duplicate_perc': 0, 'number_of_duplicates': '792',
             'base_percentages': "{u'A': 16.0727, u'C': 33.9538, u'T': 16.0, u'G': 33.9735, u'N': 0.0}",
             'qual_max': '51.0', 'platform': u'seqtech-pr1', 'id': 1, 'source': '', 'single_genome': '1',
             'qual_stdev': '10.545', 'read_orientation_outward': '0', 'phred_type': '33', 'read_length_stdev': '0.0',
             'read_size': '2500000', 'qual_mean': '43.0493', 'read_length_mean': '100.0', 'insert_size_std_dev': 'None',
             'name': u'test_paired_reads_eautils', 'workspace_name': u'' + str(ws_obj_names[2]), 'gc_content': '0.679273',
             'workspace_type': u'KBaseFile.PairedEndLibrary-2.2'}]
        
        self.assertEqual(sorted(result), sorted(testresult))
    
    def test_get_reads_info_all_minimal_ok(self):
        
        ws_obj_names = self.load_test_data_empty()
        
        readssetparams = {}
        
        readssetparams['workspace_id'] = ws_obj_names[0]  #'kbasetest:1477429140721'
        readssetparams['id'] = ws_obj_names[1]  #'test_paired_reads_eautils'
        
        #objid = self.getImpl().get_id(self.getContext(), readssetparams)
        #readssetparams['id'] = objid[0]
        
        result = self.getImpl().get_reads_info_all(self.getContext(), readssetparams)
        print('RESULT test_get_reads_info_all_minimal:')
        pprint(result)
        
        testresult = [{'read_count': '', 'total_bases': '', 'insert_size_mean': '', 'qual_min': '', 'strain': '',
                       'duplicate_perc': '', 'number_of_duplicates': '', 'base_percentages': '', 'qual_max': '',
                       'platform': u'seqtech-pr1', 'id': 1, 'source': '', 'single_genome': '', 'qual_stdev': '',
                       'read_orientation_outward': '', 'phred_type': '', 'read_length_stdev': '', 'read_size': '',
                       'qual_mean': '', 'read_length_mean': '', 'insert_size_std_dev': '',
                       'name': u'test_paired_reads_eautils', 'workspace_name': u'' + str(ws_obj_names[2]),
                       'gc_content': '', 'workspace_type': u'KBaseFile.PairedEndLibrary-2.2'}]
        
        self.assertEqual(sorted(result), sorted(testresult))
    
    def test_get_reads_info_all_minimal_by_ref_ok(self):
        
        ws_obj_names = self.load_test_data_empty()
        
        objref = str(ws_obj_names[0]) + "/" + str(ws_obj_names[1])
        
        params = {}
        params['workspace_obj_ref'] = objref
        
        result = self.getImpl().get_reads_info_all(self.getContext(), params)
        print('RESULT test_get_reads_info_all_minimal:')
        pprint(result)
        
        testresult = [{'read_count': '', 'total_bases': '', 'insert_size_mean': '', 'qual_min': '', 'strain': '',
                       'duplicate_perc': '', 'number_of_duplicates': '', 'base_percentages': '', 'qual_max': '',
                       'platform': u'seqtech-pr1', 'id': 1, 'source': '', 'single_genome': '', 'qual_stdev': '',
                       'read_orientation_outward': '', 'phred_type': '', 'read_length_stdev': '', 'read_size': '',
                       'qual_mean': '', 'read_length_mean': '', 'insert_size_std_dev': '',
                       'name': u'test_paired_reads_eautils', 'workspace_name': u'' + str(ws_obj_names[2]),
                       'gc_content': '', 'workspace_type': u'KBaseFile.PairedEndLibrary-2.2'}]
        
        self.assertEqual(sorted(result), sorted(testresult))
