package ReadsAPI::ReadsAPIClient;

use JSON::RPC::Client;
use POSIX;
use strict;
use Data::Dumper;
use URI;
use Bio::KBase::Exceptions;
my $get_time = sub { time, 0 };
eval {
    require Time::HiRes;
    $get_time = sub { Time::HiRes::gettimeofday() };
};

use Bio::KBase::AuthToken;

# Client version should match Impl version
# This is a Semantic Version number,
# http://semver.org
our $VERSION = "0.1.0";

=head1 NAME

ReadsAPI::ReadsAPIClient

=head1 DESCRIPTION


A KBase module: ReadsAPI


=cut

sub new
{
    my($class, $url, @args) = @_;
    

    my $self = {
	client => ReadsAPI::ReadsAPIClient::RpcClient->new,
	url => $url,
	headers => [],
    };

    chomp($self->{hostname} = `hostname`);
    $self->{hostname} ||= 'unknown-host';

    #
    # Set up for propagating KBRPC_TAG and KBRPC_METADATA environment variables through
    # to invoked services. If these values are not set, we create a new tag
    # and a metadata field with basic information about the invoking script.
    #
    if ($ENV{KBRPC_TAG})
    {
	$self->{kbrpc_tag} = $ENV{KBRPC_TAG};
    }
    else
    {
	my ($t, $us) = &$get_time();
	$us = sprintf("%06d", $us);
	my $ts = strftime("%Y-%m-%dT%H:%M:%S.${us}Z", gmtime $t);
	$self->{kbrpc_tag} = "C:$0:$self->{hostname}:$$:$ts";
    }
    push(@{$self->{headers}}, 'Kbrpc-Tag', $self->{kbrpc_tag});

    if ($ENV{KBRPC_METADATA})
    {
	$self->{kbrpc_metadata} = $ENV{KBRPC_METADATA};
	push(@{$self->{headers}}, 'Kbrpc-Metadata', $self->{kbrpc_metadata});
    }

    if ($ENV{KBRPC_ERROR_DEST})
    {
	$self->{kbrpc_error_dest} = $ENV{KBRPC_ERROR_DEST};
	push(@{$self->{headers}}, 'Kbrpc-Errordest', $self->{kbrpc_error_dest});
    }

    #
    # This module requires authentication.
    #
    # We create an auth token, passing through the arguments that we were (hopefully) given.

    {
	my %arg_hash2 = @args;
	if (exists $arg_hash2{"token"}) {
	    $self->{token} = $arg_hash2{"token"};
	} elsif (exists $arg_hash2{"user_id"}) {
	    my $token = Bio::KBase::AuthToken->new(@args);
	    if (!$token->error_message) {
	        $self->{token} = $token->token;
	    }
	}
	
	if (exists $self->{token})
	{
	    $self->{client}->{token} = $self->{token};
	}
    }

    my $ua = $self->{client}->ua;	 
    my $timeout = $ENV{CDMI_TIMEOUT} || (30 * 60);	 
    $ua->timeout($timeout);
    bless $self, $class;
    #    $self->_validate_version();
    return $self;
}




=head2 get_reads_info_all_formatted

  $info = $obj->get_reads_info_all_formatted($params)

=over 4

=item Parameter and return types

=begin html

<pre>
$params is a ReadsAPI.ReadsParams
$info is a ReadsAPI.ReadsInfoAll
ReadsParams is a reference to a hash where the following keys are defined:
	id has a value which is a string
	name has a value which is a string
	workspace_name has a value which is a string
	workspace_id has a value which is a string
	workspace_obj_ref has a value which is a string
ReadsInfoAll is a reference to a hash where the following keys are defined:
	id has a value which is a string
	Name has a value which is a string
	workspace_name has a value which is a string
	Type has a value which is a string
	Platform has a value which is a string
	Single_Genome has a value which is a string
	Strain has a value which is a string
	Source has a value which is a string
	Number_of_Reads has a value which is a string
	Total_Number_of_Bases has a value which is a string
	GC_Percentage has a value which is a string
	Mean_Read_Length has a value which is a string
	Read_Length_Std_Dev has a value which is a string
	Phred_Type has a value which is a string
	Number_of_Duplicate_Reads has a value which is a string
	Quality_Score_Min_Max has a value which is a string
	Quality_Score_Mean_Std_Dev has a value which is a string
	Insert_Size_Mean has a value which is a string
	Insert_Size_Std_Dev has a value which is a string
	Outward_Read_Orientation has a value which is a string
	Base_Percentages has a value which is a string

</pre>

=end html

=begin text

$params is a ReadsAPI.ReadsParams
$info is a ReadsAPI.ReadsInfoAll
ReadsParams is a reference to a hash where the following keys are defined:
	id has a value which is a string
	name has a value which is a string
	workspace_name has a value which is a string
	workspace_id has a value which is a string
	workspace_obj_ref has a value which is a string
ReadsInfoAll is a reference to a hash where the following keys are defined:
	id has a value which is a string
	Name has a value which is a string
	workspace_name has a value which is a string
	Type has a value which is a string
	Platform has a value which is a string
	Single_Genome has a value which is a string
	Strain has a value which is a string
	Source has a value which is a string
	Number_of_Reads has a value which is a string
	Total_Number_of_Bases has a value which is a string
	GC_Percentage has a value which is a string
	Mean_Read_Length has a value which is a string
	Read_Length_Std_Dev has a value which is a string
	Phred_Type has a value which is a string
	Number_of_Duplicate_Reads has a value which is a string
	Quality_Score_Min_Max has a value which is a string
	Quality_Score_Mean_Std_Dev has a value which is a string
	Insert_Size_Mean has a value which is a string
	Insert_Size_Std_Dev has a value which is a string
	Outward_Read_Orientation has a value which is a string
	Base_Percentages has a value which is a string


=end text

=item Description

Returns all info about this Reads object.

=back

=cut

 sub get_reads_info_all_formatted
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function get_reads_info_all_formatted (received $n, expecting 1)");
    }
    {
	my($params) = @args;

	my @_bad_arguments;
        (ref($params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"params\" (value was \"$params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to get_reads_info_all_formatted:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'get_reads_info_all_formatted');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "ReadsAPI.get_reads_info_all_formatted",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'get_reads_info_all_formatted',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method get_reads_info_all_formatted",
					    status_line => $self->{client}->status_line,
					    method_name => 'get_reads_info_all_formatted',
				       );
    }
}
 
  
sub status
{
    my($self, @args) = @_;
    if ((my $n = @args) != 0) {
        Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
                                   "Invalid argument count for function status (received $n, expecting 0)");
    }
    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
        method => "ReadsAPI.status",
        params => \@args,
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
                           code => $result->content->{error}->{code},
                           method_name => 'status',
                           data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
                          );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method status",
                        status_line => $self->{client}->status_line,
                        method_name => 'status',
                       );
    }
}
   

sub version {
    my ($self) = @_;
    my $result = $self->{client}->call($self->{url}, $self->{headers}, {
        method => "ReadsAPI.version",
        params => [],
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(
                error => $result->error_message,
                code => $result->content->{code},
                method_name => 'get_reads_info_all_formatted',
            );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(
            error => "Error invoking method get_reads_info_all_formatted",
            status_line => $self->{client}->status_line,
            method_name => 'get_reads_info_all_formatted',
        );
    }
}

sub _validate_version {
    my ($self) = @_;
    my $svr_version = $self->version();
    my $client_version = $VERSION;
    my ($cMajor, $cMinor) = split(/\./, $client_version);
    my ($sMajor, $sMinor) = split(/\./, $svr_version);
    if ($sMajor != $cMajor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Major version numbers differ.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor < $cMinor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Client minor version greater than Server minor version.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor > $cMinor) {
        warn "New client version available for ReadsAPI::ReadsAPIClient\n";
    }
    if ($sMajor == 0) {
        warn "ReadsAPI::ReadsAPIClient version is $svr_version. API subject to change.\n";
    }
}

=head1 TYPES



=head2 ReadsParams

=over 4



=item Description

ReadsAPI parameters

       string id - id of object
       string name - name of object
       string workspace_name - name of workspace
       string workspace_id - id of workspace
       string string workspace_obj_ref - workspace object ref


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
id has a value which is a string
name has a value which is a string
workspace_name has a value which is a string
workspace_id has a value which is a string
workspace_obj_ref has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
id has a value which is a string
name has a value which is a string
workspace_name has a value which is a string
workspace_id has a value which is a string
workspace_obj_ref has a value which is a string


=end text

=back



=head2 ReadsInfoAll

=over 4



=item Description

Reads info all

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
        string Quality_Score_Min_Max - quality min and max X/ Y
        string Quality_Score_Mean_Std_Dev - mean (st dev)

        string Insert_Size_Mean
        string Insert_Size_Std_Dev
        string Outward_Read_Orientation

        string Base_Percentages - A (%), C(%), G (%), T (%), N (%)

        @optional Single_Genome Strain Source Number_of_Reads Total_Number_of_Bases GC_Percentage
        @optional Mean_Read_Length Read_Length_Std_Dev Phred_Type Number_of_Duplicate_Reads
        @optional Quality_Score_Min_Max Quality_Score_Mean_Std_Dev
        @optional Insert_Size_Mean Insert_Size_Std_Dev Outward_Read_Orientation Base_Percentages


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
id has a value which is a string
Name has a value which is a string
workspace_name has a value which is a string
Type has a value which is a string
Platform has a value which is a string
Single_Genome has a value which is a string
Strain has a value which is a string
Source has a value which is a string
Number_of_Reads has a value which is a string
Total_Number_of_Bases has a value which is a string
GC_Percentage has a value which is a string
Mean_Read_Length has a value which is a string
Read_Length_Std_Dev has a value which is a string
Phred_Type has a value which is a string
Number_of_Duplicate_Reads has a value which is a string
Quality_Score_Min_Max has a value which is a string
Quality_Score_Mean_Std_Dev has a value which is a string
Insert_Size_Mean has a value which is a string
Insert_Size_Std_Dev has a value which is a string
Outward_Read_Orientation has a value which is a string
Base_Percentages has a value which is a string

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
id has a value which is a string
Name has a value which is a string
workspace_name has a value which is a string
Type has a value which is a string
Platform has a value which is a string
Single_Genome has a value which is a string
Strain has a value which is a string
Source has a value which is a string
Number_of_Reads has a value which is a string
Total_Number_of_Bases has a value which is a string
GC_Percentage has a value which is a string
Mean_Read_Length has a value which is a string
Read_Length_Std_Dev has a value which is a string
Phred_Type has a value which is a string
Number_of_Duplicate_Reads has a value which is a string
Quality_Score_Min_Max has a value which is a string
Quality_Score_Mean_Std_Dev has a value which is a string
Insert_Size_Mean has a value which is a string
Insert_Size_Std_Dev has a value which is a string
Outward_Read_Orientation has a value which is a string
Base_Percentages has a value which is a string


=end text

=back



=cut

package ReadsAPI::ReadsAPIClient::RpcClient;
use base 'JSON::RPC::Client';
use POSIX;
use strict;

#
# Override JSON::RPC::Client::call because it doesn't handle error returns properly.
#

sub call {
    my ($self, $uri, $headers, $obj) = @_;
    my $result;


    {
	if ($uri =~ /\?/) {
	    $result = $self->_get($uri);
	}
	else {
	    Carp::croak "not hashref." unless (ref $obj eq 'HASH');
	    $result = $self->_post($uri, $headers, $obj);
	}

    }

    my $service = $obj->{method} =~ /^system\./ if ( $obj );

    $self->status_line($result->status_line);

    if ($result->is_success) {

        return unless($result->content); # notification?

        if ($service) {
            return JSON::RPC::ServiceObject->new($result, $self->json);
        }

        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    elsif ($result->content_type eq 'application/json')
    {
        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    else {
        return;
    }
}


sub _post {
    my ($self, $uri, $headers, $obj) = @_;
    my $json = $self->json;

    $obj->{version} ||= $self->{version} || '1.1';

    if ($obj->{version} eq '1.0') {
        delete $obj->{version};
        if (exists $obj->{id}) {
            $self->id($obj->{id}) if ($obj->{id}); # if undef, it is notification.
        }
        else {
            $obj->{id} = $self->id || ($self->id('JSON::RPC::Client'));
        }
    }
    else {
        # $obj->{id} = $self->id if (defined $self->id);
	# Assign a random number to the id if one hasn't been set
	$obj->{id} = (defined $self->id) ? $self->id : substr(rand(),2);
    }

    my $content = $json->encode($obj);

    $self->ua->post(
        $uri,
        Content_Type   => $self->{content_type},
        Content        => $content,
        Accept         => 'application/json',
	@$headers,
	($self->{token} ? (Authorization => $self->{token}) : ()),
    );
}



1;
