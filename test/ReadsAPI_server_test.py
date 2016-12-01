# -*- coding: utf-8 -*-
import unittest
import os
import json
import time
import requests
import string
import random
import shutil

from os import environ

try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint

from biokbase.workspace.client import Workspace as workspaceService
from ReadsAPI.ReadsAPIImpl import ReadsAPI
from ReadsAPI.ReadsAPIServer import MethodContext
from ReadsUtils.ReadsUtilsClient import ReadsUtils

from DataFileUtil.baseclient import ServerError as DFUError
from DataFileUtil.DataFileUtilClient import DataFileUtil

class ReadsAPITest(unittest.TestCase):
    

        
    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        user_id = requests.post(
            'https://kbase.us/services/authorization/Sessions/Login',
            data='token={}&fields=user_id'.format(token)).json()['user_id']
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        
        cls.token = environ.get('KB_AUTH_TOKEN', None)
        
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
        
        cls.scratch = cls.cfg['scratch']

        cls.dfu = DataFileUtil(os.environ['SDK_CALLBACK_URL'], token=cls.token)
        
        shutil.rmtree(cls.scratch)
        os.mkdir(cls.scratch)

        cls.testobjref = []
        cls.testobjdata = []
        cls.testwsname = []
        cls.testwsname2 = []

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            print('Deleting workspace 1 ' + cls.wsName)
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace 1 was deleted '+cls.wsName)

        if hasattr(cls, 'testwsname'):
            try:
                print('Deleting workspace 2 ' + cls.testwsname[0])
                cls.wsClient.delete_workspace({'workspace': cls.testwsname[0]})
                print('Test workspace 2 was deleted ' + cls.testwsname[0])
            except Exception as e:
                print e
                
        if hasattr(cls, 'testwsname2'):
            try:
                print('Deleting workspace 3 ' + cls.testwsname2[0])
                cls.wsClient.delete_workspace({'workspace': cls.testwsname2[0]})
                print('Test workspace 3 was deleted ' + cls.testwsname2[0])
            except Exception as e:
                print e

        if hasattr(cls, 'testobjdata'):
            try:
                print('Deleting shock data '+str(len(cls.testobjdata)))
                print('Deleting shock data '+str(cls.testobjdata[0]))
                node = cls.testobjdata[0]['data'][0]['lib']['file']['id']
                cls.delete_shock_node(node)
                print('Test shock data was deleted')
            except Exception as e:
                print e

    @classmethod
    def delete_shock_node(cls, node_id):
        header = {'Authorization': 'Oauth {0}'.format(cls.token)}
        requests.delete(cls.shockURL + '/node/' + node_id, headers=header,
                        allow_redirects=True)
        print('Deleted shock node ' + node_id)
        
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
        
        self.upload_reads()
        
        readssetparams = {}
        
        #print "test_get_id_ok"
        #print self.testobjdata[0]['data'][0]['info']
        
        readssetparams['workspace_id'] = self.testobjdata[0]['data'][0]['info'][6]
        readssetparams['name'] =  self.testobjdata[0]['data'][0]['info'][1]
        
        result = self.getImpl().get_id(self.getContext(), readssetparams)
        print('RESULT test_get_id_ok:')
        pprint(result)
        
        self.assertEqual(result, [1])
    
    def test_get_name_ok(self):

        self.upload_reads()
        
        readssetparams = {}
        
        readssetparams['workspace_id'] = self.testobjdata[0]['data'][0]['info'][6]
        readssetparams['id'] = self.testobjdata[0]['data'][0]['info'][0]
        
        result = self.getImpl().get_name(self.getContext(), readssetparams)
        print('RESULT test_get_name_ok:')
        pprint(result)
        
        self.assertEqual(result, [u'filereads1'])
    
    def test_get_type_ok(self):
        self.upload_reads()
        
        readssetparams = {}
        
        readssetparams['workspace_id'] = self.testobjdata[0]['data'][0]['info'][6]
        readssetparams['id'] = self.testobjdata[0]['data'][0]['info'][0]
        
        result = self.getImpl().get_type(self.getContext(), readssetparams)
        print('RESULT test_get_type_ok:')
        pprint(result)
        
        self.assertEqual(result, [u'KBaseFile.SingleEndLibrary-2.2'])

    def test_get_reads_info_all_ok(self):
    
        self.upload_reads()
    
        readssetparams = {}
    
        readssetparams['workspace_id'] = self.testobjdata[0]['data'][0]['info'][6]
        readssetparams['id'] = self.testobjdata[0]['data'][0]['info'][0]
    
        result = self.getImpl().get_reads_info_all_formatted(self.getContext(), readssetparams)
        print('RESULT test_get_reads_info_all_ok:')
        pprint(result)
    
        testresult = [
            {'Insert_Size_Std_Dev': 'Not Specified', 'Phred_Type': '33', 'Number_of_Duplicate_Reads': '0 (0.0%)',
             'Name': u'filereads1', 'Strain': 'Not Specified', 'GC_Percentage': '65.71%', 'Type': 'Single End',
             'Read_Length_Std_Dev': '0.0', 'Insert_Size_Mean': 'Not Specified',
             'Quality_Score_Mean_Std_Dev': '44.68 (8.8)', 'Mean_Read_Length': '100.0',
             'Quality_Score_Min_Max': '10.0/51.0', 'Total_Number_of_Bases': '2,500',
             'Source': 'Not Specified', 'Base_Percentages': 'A(16.34%), C(31.77%), G(33.94%), T(17.94%), N(0.0%)',
             'Single_Genome': 'Yes', 'Platform': u'illumina',
             'workspace_name': u'' + self.testobjdata[0]['data'][0]['info'][7],
             'Number_of_Reads': '25', 'id': 1, 'Outward_Read_Orientation': 'Not Specified'}]
    
        self.assertEqual(sorted(result), sorted(testresult))

    def create_random_string(self):
        N = 20
        return ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
    
    def load_test_data_empty(self):
        
        test_file = "test_paired_reads_eautils_empty.json"
        with open("../test_data/" + test_file) as json_file:
            data = json.load(json_file)
        
        #print(json.dumps(data, sort_keys=True, indent=2))
        
        test_obj_name = 'test_paired_reads_eautils'

        if not self.testwsname2:
            self.testwsname2.append(self.create_random_string())
            
        #try:
        #    self.wsClient.get_workspace_info({'workspace':self.testwsname2[0]})
        #    wsexist = 1
        #except Exception as e:
        #    wsexist = 0
        #print "wsexist "+wsexist
        
        #if wsexist == 0:
        try:
            ret = self.wsClient.create_workspace({'workspace': self.testwsname2[0]})#test_ws_name
            print "created "+str(ret)
        except Exception as e:
            #print "ERROR"
            #print(type(e))
            #print(e.args)
            #print(e)
            pass
    
        summary_provenance = [{
            "description": "Saving object " + test_obj_name + " to WS"
        }]
        
        print "self.testwsname2[0] "+self.testwsname2[0]
        summary_save_info = self.wsClient.save_objects({"workspace": self.testwsname2[0],#test_ws_name,
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
    
    def test_get_reads_info_all_minimal_ok(self):
        
        ws_obj_names = self.load_test_data_empty()
        
        readssetparams = {}
        
        readssetparams['workspace_id'] = ws_obj_names[0]  #'kbasetest:1477429140721'
        readssetparams['id'] =  ws_obj_names[1]  #'test_paired_reads_eautils'
        
        result = self.getImpl().get_reads_info_all_formatted(self.getContext(), readssetparams)
        print('RESULT test_get_reads_info_all_minimal:')
        pprint(result)

        testresult = [{'Insert_Size_Std_Dev': 'Not Specified', 'Phred_Type': 'Not Specified', 'Number_of_Duplicate_Reads': 'Not Specified',
                       'Name': u'test_paired_reads_eautils', 'Strain': 'Not Specified', 'GC_Percentage': 'Not Specified',
                       'Type': 'Paired End', 'Read_Length_Std_Dev': 'Not Specified', 'Insert_Size_Mean': 'Not Specified',
                       'Quality_Score_Mean_Std_Dev': 'Not Specified', 'Mean_Read_Length': 'Not Specified',
                       'Quality_Score_Min_Max': 'Not Specified', 'Total_Number_of_Bases': 'Not Specified',
                       'Source': 'Not Specified', 'Base_Percentages': 'Not Specified', 'Single_Genome': 'Not Specified',
                       'Platform': u'seqtech-pr1', 'workspace_name': u'' + str(ws_obj_names[2]), 'Number_of_Reads': 'Not Specified', 'id': 1,
                       'Outward_Read_Orientation': 'Not Specified'}]
        
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
                       'Platform': u'seqtech-pr1', 'workspace_name':  u'' + str(ws_obj_names[2]),
                       'Number_of_Reads': 'Not Specified', 'id': 1, 'Outward_Read_Orientation': 'Not Specified'}]
        
        self.assertEqual(sorted(result), sorted(testresult))


    def upload_reads(self):
        
        if not self.testobjref:
            print "upload_reads start"
            
            forwardf = 'small.forward_100.fq'
            reversef = 'small.reverse_100.fq'
            ftarget = os.path.join(self.scratch, forwardf)
            print "ftarget "+ftarget
            ret = shutil.copy('../test_data/' + forwardf, ftarget)
            rtarget = os.path.join(self.scratch, reversef)
            print "rtarget " + rtarget
            ret = shutil.copy('../test_data/' + reversef, rtarget)
    
            self.readsUtilClient = ReadsUtils(os.environ['SDK_CALLBACK_URL'])

            if not self.testwsname:
                self.testwsname.append(self.create_random_string())

            print "upload_reads self.testwsname[0] "+self.testwsname[0]
            
            try:
                ret = self.wsClient.create_workspace({'workspace': self.testwsname[0]})  #test_ws_name
            except Exception as e:
                #print "ERROR"
                #print(type(e))
                #print(e.args)
                print(e)
                pass
            
            try:
                print "attempt upload"
                print "ftarget " + ftarget
                ref = self.readsUtilClient.upload_reads(
                    {'fwd_file': ftarget,
                               'reverse_file': rtarget,
                               'sequencing_tech': 'illumina',
                               'wsname': self.testwsname[0],
                               'name': 'filereads1'})
                
                print "test_upload_reads"
                print ref
                #self.testobjref = []
                self.testobjref.append(self.testwsname[0] + '/filereads1')
                #self.testobjdata = []
                self.testobjdata.append(self.dfu.get_objects(
                    {'object_refs': [self.testobjref[0]]}))#['data'][0]
                
                print "self.testobjdata[0]"
                print self.testobjdata[0]

            except Exception as e:
                print e
                pass

            print "self.testobjref[0]"
            print self.testobjref[0]