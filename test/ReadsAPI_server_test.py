# -*- coding: utf-8 -*-
import unittest
import os
import json
import time
import requests

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
        readssetparams = {}
        readssetparams['workspace_name'] = 'marcin:1475008857456'
        readssetparams['name'] = 'test_SRR400615_1000'
        
        result = self.getImpl().get_id(self.getContext(),readssetparams)
        print('RESULT test_get_id_ok:')
        pprint(result)

    
    def test_get_name_ok(self):
        readssetparams = {}
        readssetparams['workspace_name'] = 'marcin:1475008857456'
        readssetparams['name'] = 'test_SRR400615_1000'
        
        objid = self.getImpl().get_id(self.getContext(),readssetparams)
        
        readssetparams['id'] = objid[0]

        result = self.getImpl().get_name(self.getContext(),readssetparams)
        print('RESULT test_get_name_ok:')
        pprint(result)

        #self.assertEqual(ret[0]['n_contigs_remaining'], 2)


    def test_get_sequencing_tech_ok(self):
        readssetparams = {}
        readssetparams['workspace_name'] = 'marcin:1475008857456'
        readssetparams['name'] = 'test_SRR400615_1000'

        objid = self.getImpl().get_id(self.getContext(), readssetparams)

        readssetparams['id'] = objid[0]

        result = self.getImpl().get_sequencing_tech(self.getContext(), readssetparams)
        print('RESULT test_get_platform_ok:')
        pprint(result)

    def test_single_genome_ok(self):
        readssetparams = {}
        readssetparams['workspace_name'] = 'marcin:1475008857456'
        readssetparams['name'] = 'test_SRR400615_1000'

        objid = self.getImpl().get_id(self.getContext(), readssetparams)

        readssetparams['id'] = objid[0]

        result = self.getImpl().single_genome(self.getContext(), readssetparams)
        print('RESULT test_single_genome_ok:')
        pprint(result)

    def test_get_type_ok(self):
        readssetparams = {}

        readssetparams['workspace_name'] = 'marcin:1475008857456'
        readssetparams['name'] = 'test_SRR400615_1000'

        objid = self.getImpl().get_id(self.getContext(), readssetparams)

        readssetparams['id'] = objid[0]

        result = self.getImpl().get_type(self.getContext(), readssetparams)
        print('RESULT test_get_type_ok:')
        pprint(result)


    def test_get_reads_info_ok(self):
        readssetparams = {}

        readssetparams['workspace_name'] = 'marcin:1475008857456'
        readssetparams['name'] = 'ERR000916'

        objid = self.getImpl().get_id(self.getContext(), readssetparams)

        readssetparams['id'] = objid[0]

        result = self.getImpl().get_reads_info(self.getContext(), readssetparams)
        print('RESULT test_get_reads_info_ok:')
        pprint(result)

    def test_get_reads_info_all_ok(self):
        readssetparams = {}

        readssetparams['workspace_name'] = 'kbasetest:1477429140721'
        readssetparams['name'] = 'test_paired_reads_eautils'

        objid = self.getImpl().get_id(self.getContext(), readssetparams)

        readssetparams['id'] = objid[0]

        result = self.getImpl().get_reads_info_all(self.getContext(), readssetparams)
        print('RESULT test_get_reads_info_all_ok:')
        pprint(result)


            #def test_get_reads_info_all_ok(self):
    #    readssetparams = {}

    #    readssetparams['workspace_name'] = 'marcin:1475008857456'
    #    readssetparams['name'] = 'ERR000916'

    #    objid = self.getImpl().get_id(self.getContext(), readssetparams)

    #    readssetparams['id'] = objid[0]

    #    result = self.getImpl().get_reads_info_all(self.getContext(), readssetparams)
    #    print('RESULT test_get_reads_info_ok:')
    #    pprint(result)