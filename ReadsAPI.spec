/*
A KBase module: ReadsAPI
*/

module ReadsAPI {


    typedef structure {
        string id;
        string name;'
        string workspace_name;
    } ReadsParams;

    /*
        Returns the object name for a Reads object
    */
    funcdef get_name(ReadsParams params) returns (String) authentication required;

    /*
        Returns the object type for a Reads object
    */
    funcdef get_type(ReadsParams params) returns (String) authentication required;

    /*
        Returns the platform for a Reads object
    */
    funcdef get_platform(ReadsParams params) returns (String) authentication required;

    /*
        Returns the object name for a Reads object
    */
    funcdef is_single_genome(ReadsParams params) returns (Boolean) authentication required;

    /*
        Returns the object name for a Reads object
    */
    funcdef get_insert_size_mean(ReadsParams params) returns (Float) authentication required;

    /*
        Returns the object name for a Reads object
    */
    funcdef get_insert_size_std_dev(ReadsParams params) returns (Float) authentication required;

    /*
        Returns the object name for a Reads object
    */
    funcdef get_read_orientation_outward(ReadsParams params) returns (Boolean) authentication required;

};
