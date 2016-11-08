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

       string id - id of object
       string name - name of object
       string workspace_name - name of workspace
       string workspace_type - type of object
       string sequencing_tech - technological platform used to generate data in this object
       int single_genome -

       string strain -
       string source -

       string read_count -
       string read_size -
       string gc_content -
       string read_length_mean -
       string read_length_stdev -
       string phred_type -
       string number_of_duplicates -
       string qual_min -
       string qual_max -
       string qual_mean -
       string qual_stdev -
       string base_percentages -
       string duplicate_perc -

       string interleaved -
       string insert_size_mean -
       string insert_size_std_dev -
       string read_orientation_outward -

       mapping<string, string> base_percentages -

       @optional gc_content source strain read_count read_size single_genome
       @optional read_length_mean read_length_stdev phred_type
       @optional number_of_duplicates qual_min qual_max
       @optional qual_mean qual_stdev base_percentages
       @optional insert_size_mean insert_size_std_dev interleaved
       @optional read_orientation_outward

	*/
    typedef structure {
        string id;
        string name;
        string workspace_name;
        string workspace_type;
        string sequencing_tech;
        int single_genome;

        string strain;
        string source;

        string read_count;
        string read_size;
        string gc_content;
        string read_length_mean;
        string read_length_stdev;
        string phred_type;
        string number_of_duplicates;
        string qual_min;
        string qual_max;
        string qual_mean;
        string qual_stdev;
        string duplicate_perc;

        string interleaved;
        string insert_size_mean;
        string insert_size_std_dev;
        string read_orientation_outward;

        mapping<string, string> base_percentages;
    } ReadsInfoAll;


    /*
        Returns all info about this Reads object.
    */
    funcdef get_reads_info_all(ReadsParams params) returns(ReadsInfoAll info) authentication required;

    /*
        Returns all info about this Reads object.
    */
    funcdef get_reads_info_all_by_ref(ReadsParams params) returns(ReadsInfoAll info) authentication required;
};