/*
A KBase module: ReadsAPI
*/

module ReadsAPI {


    /* ReadsAPI parameters

       string id - id of object
       string name - name of object
       string workspace_name - name of workspace

    */
    typedef structure {
        string id;
        string name;
        string workspace_name;
    } ReadsParams;


    /*
        Returns the object id for a Reads object
    */
    funcdef get_id(ReadsParams params) returns (int) authentication required;

    /*
        Returns the object id for a Reads object
    */
    funcdef get_id_by_ref(string workspace_object_ref) returns (int) authentication required;

    /*
        Returns the object name for a Reads object
    */
    funcdef get_name(ReadsParams params) returns (string) authentication required;

    /*
        Returns the object name for a Reads object
    */
    funcdef get_name_by_ref(string workspace_object_ref) returns (string) authentication required;

    /*
        Returns the object type for a Reads object
    */
    funcdef get_type(ReadsParams params) returns (string) authentication required;

    /*
        Returns the object type for a Reads object
    */
    funcdef get_type_by_ref(string workspace_object_ref) returns (string) authentication required;


    /* Reads info

       string id - id of object
       string name - name of object
       string workspace_name - name of workspace
       string workspace_type - type of object
       string sequencing_tech - technological platform used to generate data in this object
       int single_genome -
       float insert_size_mean -
       float insert_size_std_dev -
       int read_orientation_outward -

       @optional sequencing_tech single_genome insert_size_mean insert_size_std_dev read_orientation_outward

    */
    typedef structure {
        string id;
        string name;
        string workspace_name;
        string workspace_type;
        string sequencing_tech;
        int single_genome;
        float insert_size_mean;
        float insert_size_std_dev;
        int read_orientation_outward;
    } ReadsInfo;


    /*
        Returns info about this Reads object.
    */
	funcdef get_reads_info(ReadsParams params) returns(ReadsInfo info) authentication required;


    /* Reads info all

       string id - id of object
       string name - name of object
       string workspace_name - name of workspace
       string workspace_type - type of object
       string sequencing_tech - technological platform used to generate data in this object
       int single_genome -

       string strain -
       string source -

       int read_count -
       int read_size -
       float gc_content -
       float read_length_mean -
       float read_length_stdev -
       float phred_type -
       int number_of_duplicates -
       float qual_min -
       float qual_max -
       float qual_mean -
       float qual_stdev -
       float base_percentages -
       float duplicate_perc -

       int interleaved -
       float insert_size_mean -
       float insert_size_std_dev -
       int read_orientation_outward -

       mapping<string, float> base_percentages -

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

        int read_count;
        int read_size;
        float gc_content;
        float read_length_mean;
        float read_length_stdev;
        float phred_type;
        int number_of_duplicates;
        float qual_min;
        float qual_max;
        float qual_mean;
        float qual_stdev;
        float duplicate_perc;

        int interleaved;
        float insert_size_mean;
        float insert_size_std_dev;
        int read_orientation_outward;

        mapping<string, float> base_percentages;
    } ReadsInfoAll;


    /*
        Returns all info about this Reads object.
    */
    funcdef get_reads_info_all(ReadsParams params) returns(ReadsInfoAll info) authentication required;
};
