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
    GIT_COMMIT_HASH = "691dc4e56a6b9400e362df03b32582da1d1a98de"
    
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
        Get the name of a Reads object based on its workspace id
        :param params: instance of type "ReadsParams" -> structure:
           parameter "workspace" of type "workspace_name" (A string
           representing a workspace name.), parameter "id" of type
           "String" (A string representing a Reads object id), parameter "name" of type
           "String" (A string representing a Reads object name), 
        :returns: instance of type "String" -> workspace object name
        """
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
            objid = wsClient.get_name([{'ref': workspace_name+'/'+id}])[0]['name']
            print "objid "+objid
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)
        return [objid]

    def get_name(self, ctx, params):
        """
        Get the name of a Reads object based on its workspace id
        :param params: instance of type "ReadsParams" -> structure:
           parameter "workspace" of type "workspace_name" (A string
           representing a workspace name.), parameter "id" of type
           "String" (A string representing a Reads object id), parameter "name" of type
           "String" (A string representing a Reads object name), 
        :returns: instance of type "String" -> workspace object name
        """
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
            name = wsClient.get_name([{'ref': workspace_name+'/'+id}])[0]['name']
            print "name "+name
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)
        return [name]

    def get_type(self, ctx, params):
        """
        Get the type of a Reads object based on its workspace id
        :param params: instance of type "ReadsParams" -> structure:
           parameter "workspace" of type "workspace_name" (A string
           representing a workspace name.), parameter "id" of type
           "String" (A string representing a Reads object id), parameter "name" of type
           "String" (A string representing a Reads object name), 
        :returns: instance of type "String" -> workspace object type
        """
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
            objtype = wsClient.get_type([{'ref': workspace_name+'/'+id}])[0]['type']
            print "objtype "+objtype
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)
        return [objtype]

    def get_platform(self, ctx, params):
        """
        Get the platform of a Reads object based on its workspace id
        :param params: instance of type "ReadsParams" -> structure:
           parameter "workspace" of type "workspace_name" (A string
           representing a workspace name.), parameter "id" of type
           "String" (A string representing a Reads object id), parameter "name" of type
           "String" (A string representing a Reads object name), 
        :returns: instance of type "String" -> reads platform
        """
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
            platform = wsClient.get_type([{'ref': workspace_name+'/'+id}])[0]['sequencing_tech']
            print "platform "+platform
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)
        return [platform]

    def is_single_genome(self, ctx, params):
        """
        Does the Reads object represent a single genome?
        :param params: instance of type "ReadsParams" -> structure:
           parameter "workspace" of type "workspace_name" (A string
           representing a workspace name.), parameter "id" of type
           "String" (A string representing a Reads object id), parameter "name" of type
           "String" (A string representing a Reads object name), 
        :returns: instance of type "Boolean" -> is single genome
        """
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
            issingle = wsClient.get_type([{'ref': workspace_name+'/'+id}])[0]['single_genome']
            print "issingle "+issingle
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error from workspace:\n' + orig_error)
        return [issingle]

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
