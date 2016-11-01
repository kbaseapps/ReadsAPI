# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statments should live
import sys
import traceback
import uuid
from pprint import pprint, pformat
from biokbase.workspace.client import Workspace as workspaceService
#END_HEADER


class ReadsAPI:
    '''
    Module Name:
    ReadsAPI

    Module Description:
    A KBase module: ReadsAPI
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/kbaseapps/ReadsAPI"
    GIT_COMMIT_HASH = "7fe1726d8fcaada4d8ffee5ededc08510c9dd00b"
    
    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    workspaceURL = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        #END_CONSTRUCTOR
        pass
    

    def get_id(self, ctx, params):
        """
        Returns the object id for a Reads object
        :param params: instance of type "ReadsParams" (ReadsAPI parameters
           string id - id of object string name - name of object string
           workspace_name - name of workspace) -> structure: parameter "id"
           of String, parameter "name" of String, parameter "workspace_name"
           of String
        :returns: instance of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_id

        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        workspace_name = params['workspace_name']
        if 'name' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        name = params['name']

        ref = workspace_name + '/' + name

        try:
            # Note that results from the workspace are returned in a list
            returnVal = self.get_id_by_ref(ctx, ref)[0]
            #print "get_id objid "+str(returnVal)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error:\n' + orig_error)

        #END get_id

        # At some point might do deeper type checking...
        if not isinstance(returnVal, int):
            raise ValueError('Method get_id return value ' +
                             'returnVal is not type int as required.')
        # return the results
        return [returnVal]

    def get_id_by_ref(self, ctx, workspace_object_ref):
        """
        Returns the object id for a Reads object
        :param workspace_object_ref: instance of String
        :returns: instance of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_id_by_ref

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": workspace_object_ref}],
                                                      "includeMetadata": 0,
                                                      "ignoreErrors": 0})[0][0]
            #print "get_id objid "+str(returnVal)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error:\n' + orig_error)

        #END get_id_by_ref

        # At some point might do deeper type checking...
        if not isinstance(returnVal, int):
            raise ValueError('Method get_id_by_ref return value ' +
                             'returnVal is not type int as required.')
        # return the results
        return [returnVal]

    def get_name(self, ctx, params):
        """
        Returns the object name for a Reads object
        :param params: instance of type "ReadsParams" (ReadsAPI parameters
           string id - id of object string name - name of object string
           workspace_name - name of workspace) -> structure: parameter "id"
           of String, parameter "name" of String, parameter "workspace_name"
           of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_name

        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        workspace_name = params['workspace_name']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objid = params['id']

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            #Note that results from the workspace are returned in a list
            #print "get_name ref"+ workspace_name+'/'+str(objid)

            ref = workspace_name + '/' + str(objid)

            returnVal = self.get_name_by_ref(ctx, ref)[0]
            #print "get_name name "+returnVal
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error:\n' + orig_error)

        #END get_name

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_name return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_name_by_ref(self, ctx, workspace_object_ref):
        """
        Returns the object name for a Reads object
        :param workspace_object_ref: instance of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_name_by_ref

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            #Note that results from the workspace are returned in a list
            #print "get_name ref"+ workspace_name+'/'+str(objid)
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": workspace_object_ref}],
                                                      "includeMetadata": 0,
                                                      "ignoreErrors": 0})[0][1]
            #print "get_name name "+returnVal
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)

        #END get_name_by_ref

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_name_by_ref return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_type(self, ctx, params):
        """
        Returns the object type for a Reads object
        :param params: instance of type "ReadsParams" (ReadsAPI parameters
           string id - id of object string name - name of object string
           workspace_name - name of workspace) -> structure: parameter "id"
           of String, parameter "name" of String, parameter "workspace_name"
           of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_type

        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        workspace_name = params['workspace_name']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objid = params['id']

        #print "get_type objid "+str(objid)
        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            objref = workspace_name + '/' + str(objid)
            #print "get_type "+objref
            # Note that results from the workspace are returned in a list
            returnVal = self.get_type_by_ref(ctx, objref)[0]

            #print "get_type objtype "+returnVal
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)

        #END get_type

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_type return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_type_by_ref(self, ctx, workspace_object_ref):
        """
        Returns the object type for a Reads object
        :param workspace_object_ref: instance of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_type_by_ref

        #print "get_type objid "+str(objid)
        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            #print "get_type "+objref
            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": workspace_object_ref}]})[0][2]
            #,"includeMetadata": 0,
            #"ignoreErrors": 0

            #print "get_type objtype "+returnVal
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)

        #END get_type_by_ref

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_type_by_ref return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def get_reads_info(self, ctx, params):
        """
        Returns info about this Reads object.
        :param params: instance of type "ReadsParams" (ReadsAPI parameters
           string id - id of object string name - name of object string
           workspace_name - name of workspace) -> structure: parameter "id"
           of String, parameter "name" of String, parameter "workspace_name"
           of String
        :returns: instance of type "ReadsInfo" (Reads info string id - id of
           object string name - name of object string workspace_name - name
           of workspace string workspace_type - type of object string
           sequencing_tech - technological platform used to generate data in
           this object string single_genome - string insert_size_mean -
           string insert_size_std_dev - string read_orientation_outward -
           @optional sequencing_tech single_genome insert_size_mean
           insert_size_std_dev read_orientation_outward) -> structure:
           parameter "id" of String, parameter "name" of String, parameter
           "workspace_name" of String, parameter "workspace_type" of String,
           parameter "sequencing_tech" of String, parameter "single_genome"
           of String, parameter "insert_size_mean" of String, parameter
           "insert_size_std_dev" of String, parameter
           "read_orientation_outward" of String
        """
        # ctx is the context object
        # return variables are: info
        #BEGIN get_reads_info

        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        workspace_name = params['workspace_name']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objid = params['id']

        token = ctx['token']

        info = dict()
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:

            objref = workspace_name + '/' + str(objid)

            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_objects2({'objects': [{'ref': objref}]})['data'][0]

            #print returnVal

            ###required
            info['id'] = returnVal['info'][0]#['id']
            info['name'] = returnVal['info'][1]#['name']
            info['workspace_name'] = workspace_name
            info['workspace_type'] = returnVal['info'][2]#['type']

            fields = ['single_genome', 'insert_size_mean', 'insert_size_std_dev',
                      'insert_size_std_dev','read_orientation_outward']
            for field in fields:
                if field in returnVal['data']:
                    info[field] = returnVal['data'][field]
                else:
                    info[field] = ""

            ###special cases
            if 'sequencing_tech' in returnVal['data'] and returnVal['data']['sequencing_tech'] is not None:
                info['platform'] = returnVal['data']['sequencing_tech']
            else:
                info['platform'] = ""

        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)


        #END get_reads_info

        # At some point might do deeper type checking...
        if not isinstance(info, dict):
            raise ValueError('Method get_reads_info return value ' +
                             'info is not type dict as required.')
        # return the results
        return [info]

    def get_reads_info_all(self, ctx, params):
        """
        Returns all info about this Reads object.
        :param params: instance of type "ReadsParams" (ReadsAPI parameters
           string id - id of object string name - name of object string
           workspace_name - name of workspace) -> structure: parameter "id"
           of String, parameter "name" of String, parameter "workspace_name"
           of String
        :returns: instance of type "ReadsInfoAll" (Reads info all string id -
           id of object string name - name of object string workspace_name -
           name of workspace string workspace_type - type of object string
           sequencing_tech - technological platform used to generate data in
           this object int single_genome - string strain - string source -
           string read_count - string read_size - string gc_content - string
           read_length_mean - string read_length_stdev - string phred_type -
           string number_of_duplicates - string qual_min - string qual_max -
           string qual_mean - string qual_stdev - string base_percentages -
           string duplicate_perc - string interleaved - string
           insert_size_mean - string insert_size_std_dev - string
           read_orientation_outward - mapping<string, string>
           base_percentages - @optional gc_content source strain read_count
           read_size single_genome @optional read_length_mean
           read_length_stdev phred_type @optional number_of_duplicates
           qual_min qual_max @optional qual_mean qual_stdev base_percentages
           @optional insert_size_mean insert_size_std_dev interleaved
           @optional read_orientation_outward) -> structure: parameter "id"
           of String, parameter "name" of String, parameter "workspace_name"
           of String, parameter "workspace_type" of String, parameter
           "sequencing_tech" of String, parameter "single_genome" of Long,
           parameter "strain" of String, parameter "source" of String,
           parameter "read_count" of String, parameter "read_size" of String,
           parameter "gc_content" of String, parameter "read_length_mean" of
           String, parameter "read_length_stdev" of String, parameter
           "phred_type" of String, parameter "number_of_duplicates" of
           String, parameter "qual_min" of String, parameter "qual_max" of
           String, parameter "qual_mean" of String, parameter "qual_stdev" of
           String, parameter "duplicate_perc" of String, parameter
           "interleaved" of String, parameter "insert_size_mean" of String,
           parameter "insert_size_std_dev" of String, parameter
           "read_orientation_outward" of String, parameter "base_percentages"
           of mapping from String to String
        """
        # ctx is the context object
        # return variables are: info
        #BEGIN get_reads_info_all

        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        workspace_name = params['workspace_name']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objid = params['id']

        token = ctx['token']

        info = dict()
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:

            objref = workspace_name + '/' + str(objid)

            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_objects2({'objects': [{'ref': objref}]})['data'][0]

            #print "get_reads_info_all "+ str(returnVal)

            info['id'] = returnVal['info'][0]  #['id']
            info['name'] = returnVal['info'][1]  #['name']
            info['workspace_name'] = workspace_name
            info['workspace_type'] = returnVal['info'][2]  #['type']

###PLACEHOLDERS strain and source currently not specified in example data
            #if returnVal['data']['strain'] is not None:
            #    info['strain'] = returnVal['data']['strain']
            #else:
            #    info['strain'] = ""
            info['strain'] = ""

            #if returnVal['data']['source'] is not None:
            #    info['source'] = returnVal['data']['source']
            #else:
            #    info['source'] = ""
            info['source'] = ""

            fields = ['sequencing_tech', 'single_genome', 'read_count', 'read_size',
                      'gc_content', 'read_length_mean', 'read_length_stdev', 'phred_type',
                      'number_of_duplicates', 'qual_min', 'qual_max', 'qual_mean',
                      'qual_stdev', 'base_percentages',
                      'insert_size_mean', 'insert_size_std_dev', 'insert_size_std_dev', 'read_orientation_outward']


            for field in fields:
                if field in returnVal['data']:
                    info[field] = returnVal['data'][field]
                else:
                    info[field] = ""

            ###special cases
            if 'sequencing_tech' in returnVal['data'] and returnVal['data']['sequencing_tech'] is not None:
                info['platform'] = returnVal['data']['sequencing_tech']
            else:
                info['platform'] = ""

            if 'number_of_duplicates' in returnVal['data'] and returnVal['data']['number_of_duplicates'] is not None \
                    and 'read_count' in returnVal['data'] \
                    and returnVal['data']['read_count'] is not None:
                info['duplicate_perc'] = returnVal['data']['number_of_duplicates'] / info['read_count']
            else:
                info['duplicate_perc'] = ""


                #print "is_single_genome issingle "+str(returnVal)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)


        #END get_reads_info_all

        # At some point might do deeper type checking...
        if not isinstance(info, dict):
            raise ValueError('Method get_reads_info_all return value ' +
                             'info is not type dict as required.')
        # return the results
        return [info]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION,
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
