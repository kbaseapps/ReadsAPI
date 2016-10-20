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
    GIT_COMMIT_HASH = "09829ff8394fe0c4355ed7edd71ad12ee2f73e04"
    
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

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": workspace_name + '/' + name}],
                                                      "includeMetadata": 0,
                                                      "ignoreErrors": 0})[0][0]
            #print "get_id objid "+str(returnVal)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)

        #END get_id

        # At some point might do deeper type checking...
        if not isinstance(returnVal, int):
            raise ValueError('Method get_id return value ' +
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
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": workspace_name + '/' + str(objid)}],
                                                      "includeMetadata": 0,
                                                      "ignoreErrors": 0})[0][1]
            #print "get_name name "+returnVal
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)

        #END get_name

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_name return value ' +
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
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": objref}]})[0][2]
            #,"includeMetadata": 0,
            #"ignoreErrors": 0

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

    def get_sequencing_tech(self, ctx, params):
        """
        Returns the platform for a Reads object
        :param params: instance of type "ReadsParams" (ReadsAPI parameters
           string id - id of object string name - name of object string
           workspace_name - name of workspace) -> structure: parameter "id"
           of String, parameter "name" of String, parameter "workspace_name"
           of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_sequencing_tech

        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        workspace_name = params['workspace_name']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objid = params['id']

        #print "get_platform objid " + str(objid)

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:

            objref = workspace_name + '/' + str(objid)
            #print "get_platform "+objref

            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_objects([{"ref": objref}])[0]
            #_mock.get_objects([{'ref': '10/1'}, {'ref': '10/2'}])

            #print "get_platform returnVal "+str(returnVal)

            if returnVal is not None:
                if returnVal['data']['sequencing_tech'] is not None:
                    returnVal = returnVal['data']['sequencing_tech']

                    #print "get_platform platform "+str(returnVal)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)


        #END get_sequencing_tech

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_sequencing_tech return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def single_genome(self, ctx, params):
        """
        Returns the single_genome flag for a Reads object
        :param params: instance of type "ReadsParams" (ReadsAPI parameters
           string id - id of object string name - name of object string
           workspace_name - name of workspace) -> structure: parameter "id"
           of String, parameter "name" of String, parameter "workspace_name"
           of String
        :returns: instance of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN single_genome

        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        workspace_name = params['workspace_name']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        objid = params['id']

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:

            objref = workspace_name + '/' + str(objid)

            # Note that results from the workspace are returned in a list
            returnVal = wsClient.get_objects([{'ref': objref}])[0]

            #print "returnVal "+str(returnVal)

            if returnVal is not None:
                if returnVal['data']['single_genome'] is not None:
                    returnVal = returnVal['data']['single_genome']

                    #print "single_genome issingle "+str(returnVal)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)


        #END single_genome

        # At some point might do deeper type checking...
        if not isinstance(returnVal, int):
            raise ValueError('Method single_genome return value ' +
                             'returnVal is not type int as required.')
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
           of workspace string type - type of object string sequencing_tech -
           technological platform used to generate data in this object int
           single_genome - float insert_size_mean - float insert_size_std_dev
           - int read_orientation_outward - @metadata ws id as id @metadata
           ws name as name @metadata ws workspace_name as workspace_name
           @metadata ws type as type @optional sequencing_tech single_genome
           insert_size_mean insert_size_std_dev read_orientation_outward) ->
           structure: parameter "id" of String, parameter "name" of String,
           parameter "workspace_name" of String, parameter "type" of String,
           parameter "sequencing_tech" of String, parameter "single_genome"
           of Long, parameter "insert_size_mean" of Double, parameter
           "insert_size_std_dev" of Double, parameter
           "read_orientation_outward" of Long
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
            returnVal = wsClient.get_objects([{'ref': objref}])[0]

            info['id'] = returnVal['info'][0]#['id']
            info['name'] = returnVal['info'][1]#['name']
            info['workspace_name'] = workspace_name
            info['type'] = returnVal['info'][2]#['type']

            if returnVal['data']['sequencing_tech'] is not None:
                info['platform'] = returnVal['data']['sequencing_tech']
            else:
                info['platform'] = ""

            if returnVal['data']['single_genome'] is not None:
                info['single_genome'] = returnVal['data']['single_genome']
            else:
                info['single_genome'] = ""

            if returnVal['data']['insert_size_mean'] is not None:
                info['insert_size_mean'] = returnVal['data']['insert_size_mean']
            else:
                info['insert_size_mean'] = ""

            if returnVal['data']['insert_size_std_dev'] is not None:
                info['insert_size_std_dev'] = returnVal['data']['insert_size_std_dev']
            else:
                info['insert_size_std_dev'] = ""

            if 'read_orientation_outward' in returnVal['data']:
                if returnVal['data']['read_orientation_outward'] is not None:
                    info['read_orientation_outward'] = returnVal['data']['read_orientation_outward']
                else:
                    info['read_orientation_outward'] = ""
            else:
                info['read_orientation_outward'] = ""


            #print "is_single_genome issingle "+str(returnVal)
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
           name of workspace string type - type of object string
           sequencing_tech - technological platform used to generate data in
           this object int single_genome - string strain - string source -
           int read_count - int read_size - float gc_content - float
           read_length_mean - float read_length_stdev - float phred_type -
           int number_of_duplicates - float qual_min - float qual_max - float
           qual_mean - float qual_stdev - float base_percentages - float
           duplicate_perc - int interleaved - float insert_size_mean - float
           insert_size_std_dev - int read_orientation_outward -
           mapping<string, float> base_percentages - @metadata ws id as id
           @metadata ws name as name @metadata ws workspace_name as
           workspace_name @metadata ws type as type @optional gc_content
           source strain read_count read_size single_genome @optional
           read_length_mean read_length_stdev phred_type @optional
           number_of_duplicates qual_min qual_max @optional qual_mean
           qual_stdev base_percentages @optional insert_size_mean
           insert_size_std_dev interleaved @optional
           read_orientation_outward) -> structure: parameter "id" of String,
           parameter "name" of String, parameter "workspace_name" of String,
           parameter "type" of String, parameter "sequencing_tech" of String,
           parameter "single_genome" of Long, parameter "strain" of String,
           parameter "source" of String, parameter "read_count" of Long,
           parameter "read_size" of Long, parameter "gc_content" of Double,
           parameter "read_length_mean" of Double, parameter
           "read_length_stdev" of Double, parameter "phred_type" of Double,
           parameter "number_of_duplicates" of Long, parameter "qual_min" of
           Double, parameter "qual_max" of Double, parameter "qual_mean" of
           Double, parameter "qual_stdev" of Double, parameter
           "duplicate_perc" of Double, parameter "interleaved" of Long,
           parameter "insert_size_mean" of Double, parameter
           "insert_size_std_dev" of Double, parameter
           "read_orientation_outward" of Long, parameter "base_percentages"
           of mapping from String to Double
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
            returnVal = wsClient.get_objects([{'ref': objref}])[0]

            print "get_reads_info_all "+ returnVal

            info['id'] = returnVal['info'][0]  #['id']
            info['name'] = returnVal['info'][1]  #['name']
            info['workspace_name'] = workspace_name
            info['type'] = returnVal['info'][2]  #['type']

            if returnVal['data']['sequencing_tech'] is not None:
                info['platform'] = returnVal['data']['sequencing_tech']
            else:
                info['platform'] = ""

            if returnVal['data']['single_genome'] is not None:
                info['single_genome'] = returnVal['data']['single_genome']
            else:
                info['single_genome'] = ""


            if returnVal['data']['strain'] is not None:
                info['strain'] = returnVal['data']['strain']
            else:
                info['strain'] = ""

            if returnVal['data']['source'] is not None:
                info['source'] = returnVal['data']['source']
            else:
                info['source'] = ""

            if returnVal['data']['read_count'] is not None:
                info['read_count'] = returnVal['data']['read_count']
            else:
                info['read_count'] = ""

            if returnVal['data']['read_size'] is not None:
                info['read_size'] = returnVal['data']['read_size']
            else:
                info['read_size'] = ""

            if returnVal['data']['gc_content'] is not None:
                info['gc_content'] = returnVal['data']['gc_content']
            else:
                info['gc_content'] = ""

            if returnVal['data']['read_length_mean'] is not None:
                info['read_length_mean'] = returnVal['data']['read_length_mean']
            else:
                info['read_length_mean'] = ""

            if returnVal['data']['read_length_stdev'] is not None:
                info['read_length_stdev'] = returnVal['data']['read_length_stdev']
            else:
                info['read_length_stdev'] = ""

            if returnVal['data']['phred_type'] is not None:
                info['phred_type'] = returnVal['data']['phred_type']
            else:
                info['phred_type'] = ""

            if returnVal['data']['number_of_duplicates'] is not None:
                info['number_of_duplicates'] = returnVal['data']['number_of_duplicates']
            else:
                info['number_of_duplicates'] = ""

            if returnVal['data']['qual_min'] is not None:
                info['qual_min'] = returnVal['data']['qual_min']
            else:
                info['qual_min'] = ""

            if returnVal['data']['qual_max'] is not None:
                info['qual_max'] = returnVal['data']['qual_max']
            else:
                info['qual_max'] = ""

            if returnVal['data']['qual_mean'] is not None:
                info['qual_mean'] = returnVal['data']['qual_mean']
            else:
                info['qual_mean'] = ""

            if returnVal['data']['qual_stdev'] is not None:
                info['qual_stdev'] = returnVal['data']['qual_stdev']
            else:
                info['qual_stdev'] = ""

            if returnVal['data']['duplicate_perc'] is not None:
                info['duplicate_perc'] = returnVal['data']['duplicate_perc']
            else:
                info['duplicate_perc'] = ""

            if returnVal['data']['base_percentages'] is not None:
                info['base_percentages'] = returnVal['data']['base_percentages']
            else:
                info['base_percentages'] = ""



            if returnVal['data']['insert_size_mean'] is not None:
                info['insert_size_mean'] = returnVal['data']['insert_size_mean']
            else:
                info['insert_size_mean'] = ""

            if returnVal['data']['insert_size_std_dev'] is not None:
                info['insert_size_std_dev'] = returnVal['data']['insert_size_std_dev']
            else:
                info['insert_size_std_dev'] = ""

            if 'read_orientation_outward' in returnVal['data']:
                if returnVal['data']['read_orientation'] is not None:
                    info['read_orientation_outward'] = returnVal['data']['read_orientation_outward']
                else:
                    info['read_orientation_outward'] = ""
            else:
                info['read_orientation_outward'] = ""


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
