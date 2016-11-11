/*
A KBase module: ReadsAPI
*/

module ReadsAPI {


    /* ReadsAPI parameters

       string id - id of object
       string name - name of object
       string workspace_name - name of workspace
       string workspace_id - id of workspace
       string string workspace_obj_ref - workspace object ref

    */
    typedef structure {
        string id;
        string name;
        string workspace_name;
        string workspace_id;

        string workspace_obj_ref;
    } ReadsParams;


    /* Reads info all

        string id
        string Name;
        string workspace_name
        string Type
        string Platform
        string Single_Genome

        string Strain
        string Source

        string Number_of_Reads
        string Total_Number_of_Bases
        string GC_Percentage
        string Mean_Read_Length
        string Read_Length_Std_Dev
        string Phred_Type
        string Number_of_Duplicate_Reads - number of duplicate and (%)
        string Quality_Score - quality min and max X/ Y
        string Quality_Score_Mean_Std_Dev - mean (st dev)

        string Insert_Size_Mean
        string Insert_Size_Std_Dev
        string Outward_Read_Orientation

        string Base_Percentages - A (%), C(%), G (%), T (%), N (%)

        @optional Single_Genome Strain Source Number_of_Reads Total_Number_of_Bases GC_Percentage
        @optional Mean_Read_Length Read_Length_Std_Dev Phred_Type Number_of_Duplicate_Reads
        @optional Quality_Score Quality_Score_Mean_Std_Dev
        @optional Insert_Size_Mean Insert_Size_Std_Dev Outward_Read_Orientation Base_Percentages
	*/
    typedef structure {
        string id;
        string Name;
        string workspace_name;
        string Type;
        string Platform;
        string Single_Genome ;

        string Strain;
        string Source;

        string Number_of_Reads;
        string Total_Number_of_Bases;
        string GC_Percentage;
        string Mean_Read_Length;
        string Read_Length_Std_Dev;
        string Phred_Type;
        string Number_of_Duplicate_Reads;
        string Quality_Score;
        string Quality_Score_Mean_Std_Dev;

        string Insert_Size_Mean;
        string Insert_Size_Std_Dev;
        string Outward_Read_Orientation;

        string Base_Percentages;
    } ReadsInfoAll;


    /*
        Returns all info about this Reads object.
    */
    funcdef get_reads_info_all(ReadsParams params) returns(ReadsInfoAll info) authentication required;

};