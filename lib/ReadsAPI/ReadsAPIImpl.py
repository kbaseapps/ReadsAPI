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
    GIT_COMMIT_HASH = "5cc2184194e7c0e9f3d0baea2e6c0a38234c714e"
    
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
           workspace_name - name of workspace string workspace_id - id of
           workspace) -> structure: parameter "id" of String, parameter
           "name" of String, parameter "workspace_name" of String, parameter
           "workspace_id" of String
        :returns: instance of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_id

        if 'workspace_id' not in params:
            raise ValueError('Parameter workspace_id is not set in input arguments')
        workspace_id = params['workspace_id']
        if 'name' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objname = params['name']

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)

        try:
            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_object_info_new({"objects": [{"wsid": str(workspace_id), "name": objname}], "includeMetadata": 0, "ignoreErrors": 0})[0][0]

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

    def get_id_by_ref(self, ctx, params):
        """
        Returns the object id for a Reads object
        :param params: instance of type "ObjRefParams" (Object reference
           parameter) -> structure: parameter "workspace_obj_ref" of String
        :returns: instance of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_id_by_ref

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": params['workspace_obj_ref']}],
                                                      "includeMetadata": 0,
                                                      "ignoreErrors": 0})[0][0]
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
           workspace_name - name of workspace string workspace_id - id of
           workspace) -> structure: parameter "id" of String, parameter
           "name" of String, parameter "workspace_name" of String, parameter
           "workspace_id" of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_name

        if 'workspace_id' not in params:
            raise ValueError('Parameter workspace_id is not set in input arguments')
        workspace_id = params['workspace_id']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objid = params['id']

        token = ctx['token']
        try:
            #Note that results from the workspace are returned in a list

            ref = str(workspace_id) + '/' + str(objid)

            returnVal = self.get_name_by_ref(ctx, ref)[0]
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

    def get_name_by_ref(self, ctx, params):
        """
        Returns the object name for a Reads object
        :param params: instance of type "ObjRefParams" (Object reference
           parameter) -> structure: parameter "workspace_obj_ref" of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_name_by_ref

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            #Note that results from the workspace are returned in a list
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": params['workspace_obj_ref']}],
                                                      "includeMetadata": 0,
                                                      "ignoreErrors": 0})[0][1]
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
           workspace_name - name of workspace string workspace_id - id of
           workspace) -> structure: parameter "id" of String, parameter
           "name" of String, parameter "workspace_name" of String, parameter
           "workspace_id" of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_type

        if 'workspace_id' not in params:
            raise ValueError('Parameter workspace_id is not set in input arguments')
        workspace_id = params['workspace_id']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objid = params['id']

        try:
            objref = str(workspace_id) + '/' + str(objid)
            # Note that results from the workspace are returned in a list
            returnVal = self.get_type_by_ref(ctx, objref)[0]
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

    def get_type_by_ref(self, ctx, params):
        """
        Returns the object type for a Reads object
        :param params: instance of type "ObjRefParams" (Object reference
           parameter) -> structure: parameter "workspace_obj_ref" of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_type_by_ref

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": params['workspace_obj_ref']}]})[0][2]
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

    def get_reads_info_all(self, ctx, params):
        """
        Returns all info about this Reads object.
        :param params: instance of type "ReadsParams" (ReadsAPI parameters
           string id - id of object string name - name of object string
           workspace_name - name of workspace string workspace_id - id of
           workspace) -> structure: parameter "id" of String, parameter
           "name" of String, parameter "workspace_name" of String, parameter
           "workspace_id" of String
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

        if 'workspace_id' not in params:
            raise ValueError('Parameter workspace_id is not set in input arguments')
        workspace_id = params['workspace_id']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objid = params['id']

        try:

            objref = str(workspace_id) + '/' + str(objid)

            params = {}
            params['workspace_obj_ref'] = objref

            info = self.get_reads_info_all_by_ref(ctx, params)[0]

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

    def get_reads_info_all_by_ref(self, ctx, params):
        """
        Returns all info about this Reads object.
        :param params: instance of type "ObjRefParams" (Object reference
           parameter) -> structure: parameter "workspace_obj_ref" of String
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
        #BEGIN get_reads_info_all_by_ref

        token = ctx['token']

        info = dict()
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:

            print "type params "+str(type(params))
            print "type params " + str(params)
            print "params['workspace_obj_ref']" + params['workspace_obj_ref']

            # Note that results from the workspace are returned in a list
            try:
                returnVal = wsClient.get_objects2({'objects': [{'ref': params['workspace_obj_ref']}]})['data'][0]
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                orig_error = ''.join('    ' + line for line in lines)
                raise ValueError('Error from workspace:\n' + orig_error)

            info['id'] = returnVal['info'][0]
            info['name'] = returnVal['info'][1]
            info['workspace_name'] = returnVal['info'][7]
            info['workspace_type'] = returnVal['info'][2]

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

            fields = ['single_genome', 'read_count', 'read_size',
                      'gc_content', 'read_length_mean', 'read_length_stdev', 'phred_type',
                      'number_of_duplicates', 'qual_min', 'qual_max', 'qual_mean',
                      'qual_stdev', 'base_percentages', 'total_bases',
                      'insert_size_mean', 'insert_size_std_dev', 'insert_size_std_dev', 'read_orientation_outward']

            for field in fields:
                if field in returnVal['data']:
                    info[field] = str(returnVal['data'][field])
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
                info['duplicate_perc'] = int(returnVal['data']['number_of_duplicates']) / int(info['read_count'])
            else:
                info['duplicate_perc'] = ""

        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error:\n' + orig_error)

        #END get_reads_info_all_by_ref

        # At some point might do deeper type checking...
        if not isinstance(info, dict):
            raise ValueError('Method get_reads_info_all_by_ref return value ' +
                             'info is not type dict as required.')
        # return the results
        return [info]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION,
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
