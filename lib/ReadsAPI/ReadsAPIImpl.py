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
    GIT_COMMIT_HASH = "459a5bddb68641fd434b3670bceec773f5b55749"
    
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
        :param params: instance of type "ReadsParams" -> structure: parameter
           "id" of String, parameter "name" of String, parameter
           "workspace_name" of String
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
            # Note that results from the workspace are returned in a list, and the actual data is saved
            # in the 'data' key.  So to get the ContigSet data, we get the first element of the list, and
            # look at the 'data' field.
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": workspace_name+'/'+name}],
                "includeMetadata": 0,
                "ignoreErrors": 0})[0][0]
            print "objid "+str(returnVal)
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
        :param params: instance of type "ReadsParams" -> structure: parameter
           "id" of String, parameter "name" of String, parameter
           "workspace_name" of String
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
            # Note that results from the workspace are returned in a list, and the actual data is saved
            # in the 'data' key.  So to get the ContigSet data, we get the first element of the list, and
            # look at the 'data' field.
                    
            print "ref"+ workspace_name+'/'+str(objid)
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": workspace_name+'/'+str(objid[0])}],
                "includeMetadata": 0,
                "ignoreErrors": 0})[0][1]
            print "name "+returnVal
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
        :param params: instance of type "ReadsParams" -> structure: parameter
           "id" of String, parameter "name" of String, parameter
           "workspace_name" of String
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

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token) 
        try: 
            # Note that results from the workspace are returned in a list, and the actual data is saved
            # in the 'data' key.  So to get the ContigSet data, we get the first element of the list, and
            # look at the 'data' field.
            returnVal = wsClient.get_object_info_new({"objects": [{"ref": workspace_name+'/'+objid}],
                "includeMetadata": 0,
                "ignoreErrors": 0})[0][2]
            print "objtype "+returnVal
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

    def get_platform(self, ctx, params):
        """
        Returns the platform for a Reads object
        :param params: instance of type "ReadsParams" -> structure: parameter
           "id" of String, parameter "name" of String, parameter
           "workspace_name" of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_platform

        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        workspace_name = params['workspace_name']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        contigset_id = params['id']

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token) 
        try: 
            # Note that results from the workspace are returned in a list, and the actual data is saved
            # in the 'data' key.  So to get the ContigSet data, we get the first element of the list, and
            # look at the 'data' field.
            returnVal = wsClient.get_type([{'ref': workspace_name+'/'+id}])[0]['sequencing_tech']
            print "platform "+returnVal
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)

        #END get_platform

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method get_platform return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]

    def is_single_genome(self, ctx, params):
        """
        Returns the object name for a Reads object
        :param params: instance of type "ReadsParams" -> structure: parameter
           "id" of String, parameter "name" of String, parameter
           "workspace_name" of String
        :returns: instance of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN is_single_genome

        if 'workspace_name' not in params:
            raise ValueError('Parameter workspace_name is not set in input arguments')
        workspace_name = params['workspace_name']
        if 'id' not in params:
            raise ValueError('Parameter id is not set in input arguments')
        contigset_id = params['id']

        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token) 
        try: 
            # Note that results from the workspace are returned in a list, and the actual data is saved
            # in the 'data' key.  So to get the ContigSet data, we get the first element of the list, and
            # look at the 'data' field.
            returnVal = wsClient.returnVal([{'ref': workspace_name+'/'+id}])[0]['single_genome']
            print "issingle "+issingle
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)

        #END is_single_genome

        # At some point might do deeper type checking...
        if not isinstance(returnVal, int):
            raise ValueError('Method is_single_genome return value ' +
                             'returnVal is not type int as required.')
        # return the results
        return [returnVal]

    def get_insert_size_mean(self, ctx, params):
        """
        Returns the object name for a Reads object
        :param params: instance of type "ReadsParams" -> structure: parameter
           "id" of String, parameter "name" of String, parameter
           "workspace_name" of String
        :returns: instance of Double
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_insert_size_mean
        #END get_insert_size_mean

        # At some point might do deeper type checking...
        if not isinstance(returnVal, float):
            raise ValueError('Method get_insert_size_mean return value ' +
                             'returnVal is not type float as required.')
        # return the results
        return [returnVal]

    def get_insert_size_std_dev(self, ctx, params):
        """
        Returns the object name for a Reads object
        :param params: instance of type "ReadsParams" -> structure: parameter
           "id" of String, parameter "name" of String, parameter
           "workspace_name" of String
        :returns: instance of Double
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_insert_size_std_dev
        #END get_insert_size_std_dev

        # At some point might do deeper type checking...
        if not isinstance(returnVal, float):
            raise ValueError('Method get_insert_size_std_dev return value ' +
                             'returnVal is not type float as required.')
        # return the results
        return [returnVal]

    def get_read_orientation_outward(self, ctx, params):
        """
        Returns the object name for a Reads object
        :param params: instance of type "ReadsParams" -> structure: parameter
           "id" of String, parameter "name" of String, parameter
           "workspace_name" of String
        :returns: instance of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_read_orientation_outward
        #END get_read_orientation_outward

        # At some point might do deeper type checking...
        if not isinstance(returnVal, int):
            raise ValueError('Method get_read_orientation_outward return value ' +
                             'returnVal is not type int as required.')
        # return the results
        return [returnVal]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
