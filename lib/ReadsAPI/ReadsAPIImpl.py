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
    GIT_COMMIT_HASH = "372ddebcd5b78b0cb413b43b246ae5f27f056e82"
    
    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    workspaceURL = None
    
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
            returnVal = wsClient.get_object_info_new(
                {"objects": [{"wsid": str(workspace_id), "name": objname}], "includeMetadata": 0, "ignoreErrors": 0})[
                0][0]
        
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
            params['workspace_obj_ref'] = ref
            returnVal = self.get_name_by_ref(ctx, params)[0]
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
            params['workspace_obj_ref'] = objref
            # Note that results from the workspace are returned in a list
            returnVal = self.get_type_by_ref(ctx, params)[0]
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
    
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        #END_CONSTRUCTOR
        pass
    

    def get_reads_info_all_formatted(self, ctx, params):
        """
        Returns all info about this Reads object.
        :param params: instance of type "ReadsParams" (ReadsAPI parameters
           string id - id of object string name - name of object string
           workspace_name - name of workspace string workspace_id - id of
           workspace string string workspace_obj_ref - workspace object ref)
           -> structure: parameter "id" of String, parameter "name" of
           String, parameter "workspace_name" of String, parameter
           "workspace_id" of String, parameter "workspace_obj_ref" of String
        :returns: instance of type "ReadsInfoAll" (Reads info all string id
           string Name; string workspace_name string Type string Platform
           string Single_Genome string Strain string Source string
           Number_of_Reads string Total_Number_of_Bases string GC_Percentage
           string Mean_Read_Length string Read_Length_Std_Dev string
           Phred_Type string Number_of_Duplicate_Reads - number of duplicate
           and (%) string Quality_Score_Min_Max - quality min and max X/ Y
           string Quality_Score_Mean_Std_Dev - mean (st dev) string
           Insert_Size_Mean string Insert_Size_Std_Dev string
           Outward_Read_Orientation string Base_Percentages - A (%), C(%), G
           (%), T (%), N (%) @optional Single_Genome Strain Source
           Number_of_Reads Total_Number_of_Bases GC_Percentage @optional
           Mean_Read_Length Read_Length_Std_Dev Phred_Type
           Number_of_Duplicate_Reads @optional Quality_Score_Min_Max
           Quality_Score_Mean_Std_Dev @optional Insert_Size_Mean
           Insert_Size_Std_Dev Outward_Read_Orientation Base_Percentages) ->
           structure: parameter "id" of String, parameter "Name" of String,
           parameter "workspace_name" of String, parameter "Type" of String,
           parameter "Platform" of String, parameter "Single_Genome" of
           String, parameter "Strain" of String, parameter "Source" of
           String, parameter "Number_of_Reads" of String, parameter
           "Total_Number_of_Bases" of String, parameter "GC_Percentage" of
           String, parameter "Mean_Read_Length" of String, parameter
           "Read_Length_Std_Dev" of String, parameter "Phred_Type" of String,
           parameter "Number_of_Duplicate_Reads" of String, parameter
           "Quality_Score_Min_Max" of String, parameter
           "Quality_Score_Mean_Std_Dev" of String, parameter
           "Insert_Size_Mean" of String, parameter "Insert_Size_Std_Dev" of
           String, parameter "Outward_Read_Orientation" of String, parameter
           "Base_Percentages" of String
        """
        # ctx is the context object
        # return variables are: info
        #BEGIN get_reads_info_all_formatted
        
        if 'workspace_obj_ref' not in params:
            if 'workspace_id' not in params and 'id' not in params:
                raise ValueError(
                    'Parameter workspace_obj_ref and separate other option of ws + object ids not set in input arguments')
            else:
                workspace_obj_ref = str(params['workspace_id']) + "/" + str(params['id'])
        else:
            workspace_obj_ref = params['workspace_obj_ref']
        
        token = ctx['token']
        
        info = dict()
        wsClient = workspaceService(self.workspaceURL, token=token)
        try:
            
            # Note that results from the workspace are returned in a list
            try:
                returnVal = wsClient.get_objects2({'objects': [{'ref': workspace_obj_ref}]})['data'][0]
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                orig_error = ''.join('    ' + line for line in lines)
                raise ValueError('Error from workspace:\n' + orig_error)
            
            info['id'] = returnVal['info'][0]
            
            info['workspace_name'] = returnVal['info'][7]
            
            ###PLACEHOLDERS strain and source currently not specified in example data
            #if returnVal['data']['strain'] is not None:
            #    info['strain'] = returnVal['data']['strain']
            #else:
            #    info['strain'] = ""
            info['Strain'] = "Not Specified"
            
            #if returnVal['data']['source'] is not None:
            #    info['source'] = returnVal['data']['source']
            #else:
            #    info['source'] = ""
            info['Source'] = "Not Specified"
            
            ###Overview tab
            info['Name'] = returnVal['info'][1]
            
            if 'read_count' in returnVal['data']:
                info['Number_of_Reads'] = str("{:,}".format(returnVal['data']['read_count']))
            else:
                info['Number_of_Reads'] = "Not Specified"
            
            if str(returnVal['info'][2]).startswith('KBaseFile.PairedEndLibrary'):
                info['Type'] = 'Paired End'
            elif str(returnVal['info'][2]).startswith('KBaseFile.SingleEndLibrary'):
                info['Type'] = 'Single End'
            
            if 'sequencing_tech' in returnVal['data']:
                info['Platform'] = returnVal['data']['sequencing_tech']
            else:
                info['Platform'] = "Not Specified"
            
            if 'single_genome' in returnVal['data']:
                if returnVal['data']['single_genome'] == 0:
                    info['Single_Genome'] = 'No'
                elif returnVal['data']['single_genome'] == 1:
                    info['Single_Genome'] = 'Yes'
            else:
                info['Single_Genome'] = "Not Specified"
            
            if 'insert_size_mean' in returnVal['data'] and returnVal['data']['insert_size_mean'] is not None:
                #print "insert_size_mean "+returnVal['data']['insert_size_mean']
                #print "insert_size_mean "+round(returnVal['data']['insert_size_mean'], 2)
                info['Insert_Size_Mean'] = str("{:,}".format(round(returnVal['data']['insert_size_mean'], 2)))
            else:
                info['Insert_Size_Mean'] = "Not Specified"
            
            if 'insert_size_std_dev' in returnVal['data'] and returnVal['data']['insert_size_std_dev'] is not None:
                info['Insert_Size_Std_Dev'] = str("{:,}".format(round(returnVal['data']['insert_size_std_dev'], 2)))
            else:
                info['Insert_Size_Std_Dev'] = "Not Specified"
            
            if 'read_orientation_outward' in returnVal['data']:
                if returnVal['data']['read_orientation_outward'] == 0:
                    info['Outward_Read_Orientation'] = 'No'
                elif returnVal['data']['read_orientation_outward'] == 1:
                    info['Outward_Read_Orientation'] = 'Yes'
            else:
                info['Outward_Read_Orientation'] = "Not Specified"
            
            ##Stats
            #Number_of_Reads
            if 'total_bases' in returnVal['data']:
                info['Total_Number_of_Bases'] = str("{:,}".format(returnVal['data']['total_bases']))
            else:
                info['Total_Number_of_Bases'] = "Not Specified"
            
            if 'read_length_mean' in returnVal['data']:
                info['Mean_Read_Length'] = str("{:,}".format(round(returnVal['data']['read_length_mean'], 2)))
            else:
                info['Mean_Read_Length'] = "Not Specified"
            
            if 'read_length_stdev' in returnVal['data']:
                info['Read_Length_Std_Dev'] = str("{:,}".format(round(returnVal['data']['read_length_stdev'], 2)))
            else:
                info['Read_Length_Std_Dev'] = "Not Specified"
            
            if 'number_of_duplicates' in returnVal['data'] and 'read_count' in returnVal['data']:
                info['Number_of_Duplicate_Reads'] = str("{:,}".format(returnVal['data']['number_of_duplicates'])) + \
                                                    " (" + str(
                    round(100.0 * (float(returnVal['data']['number_of_duplicates']) / float(returnVal['data']['read_count'])),2)) + "%)"
            else:
                info['Number_of_Duplicate_Reads'] = "Not Specified"
            
            if 'phred_type' in returnVal['data']:
                info['Phred_Type'] = str(returnVal['data']['phred_type'])
            else:
                info['Phred_Type'] = "Not Specified"
            
            if 'qual_mean' in returnVal['data'] and 'qual_stdev' in returnVal['data']:
                info['Quality_Score_Mean_Std_Dev'] = str(round(returnVal['data']['qual_mean'], 2)) + " (" + str(
                    round(returnVal['data']['qual_stdev'], 2)) + ")"
            else:
                info['Quality_Score_Mean_Std_Dev'] = "Not Specified"
            
            if 'qual_min' in returnVal['data'] and 'qual_max' in returnVal['data']:
                info['Quality_Score_Min_Max'] = str(round(returnVal['data']['qual_min'], 2)) + "/" + str(
                    round(returnVal['data']['qual_max'], 2))
            else:
                info['Quality_Score_Min_Max'] = "Not Specified"
            
            if 'gc_content' in returnVal['data']:
                info['GC_Percentage'] = str(round(100 * returnVal['data']['gc_content'], 2)) + "%"
            else:
                info['GC_Percentage'] = "Not Specified"
            
            if 'base_percentages' in returnVal['data']:
                info['Base_Percentages'] = "A(" + str(round(returnVal['data']['base_percentages']['A'], 2)) + "%), " + \
                                           "C(" + str(round(returnVal['data']['base_percentages']['C'], 2)) + "%), " + \
                                           "G(" + str(round(returnVal['data']['base_percentages']['G'], 2)) + "%), " + \
                                           "T(" + str(round(returnVal['data']['base_percentages']['T'], 2)) + "%), " + \
                                           "N(" + str(round(returnVal['data']['base_percentages']['N'], 2)) + "%)"
            else:
                info['Base_Percentages'] = "Not Specified"
        
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error:\n' + orig_error)
        
        #END get_reads_info_all_formatted

        # At some point might do deeper type checking...
        if not isinstance(info, dict):
            raise ValueError('Method get_reads_info_all_formatted return value ' +
                             'info is not type dict as required.')
        # return the results
        return [info]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION,
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
