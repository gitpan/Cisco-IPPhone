#!/usr/bin/perl

# Must use authentication when POSTING an object to an IP PHone.
# User should be a user in the global directory associated with the phone
# This script uses the LWP package

use Cisco::IPPhone;
use LWP;
$ua = LWP::UserAgent->new;
$myexecute = new Cisco::IPPhone;
$mytext = new Cisco::IPPhone;

$SERVER = "192.168.250.16";

## Build Execute Object
# One Execute Object can take up to 3 Execute Items
$myexecute->Execute;
$myexecute->AddExecuteItem( { ExecuteItem => "http://$SERVER/cgi-bin/directory.cgi" });
my @xml = $myexecute->Content;
foreach $line (@xml) {
  $xml = "$xml$line";
}

# $xml = '<CiscoIPPhoneExecute> <ExecuteItem URL="http://192.168.250.16/cgi-bin/directory.cgi" /> </CiscoIPPhoneExecute>';
$xml = "&lt;CiscoIPPhoneExecute&gt; &lt;ExecuteItem URL=&quot;http://192.168.250.16/cgi-bin/directory.cgi&quot;/&gt; &lt;/CiscoIPPhoneExecute&gt;";

# Create XML Form parameter containing XML execute object
$ipphone = $ENV{REMOTE_ADDR}; # Phone making the request

# Get IP Address of phone making request and build URL to POST
$url = "CGI/Execute"; # URL on phone to accept execute XML object
$completeurl = "http:\/\/$ipphone\/$url";

# Send POST to Phone URL with XML variable set with Execute Object
my $request = HTTP::Request->new(POST => "$completeurl");

# $request->authorization_basic('user', 'password');
$request->content_type('form-data');
$request->content("XML=$xml");

# Capture response and display to phone
my $response = $ua->request($request);

if ($response->is_success) {
  $lines = $response->content;
  $mytext->Text( { Title => "My Title", Prompt => "My Prompt", 
                             Text => "Response: $lines" });
  $mytext->AddSoftKeyItem( { Name => "Update", URL => "SoftKey:Update", 
                           Position => "1" });
  $mytext->AddSoftKeyItem( { Name => "Exit", URL => "SoftKey:Exit", 
                           Position => "2" });
  print $mytext->Content;
} else {
  # Capture error if phone returns an error
  $lines = $response->status_line;
  # $lines = $response->error_as_HTML;
  $mytext->Text( { Title => "My Title", Prompt => "My Prompt", 
                             Text => "Error: $completeurl\n$lines" });
  $mytext->AddSoftKeyItem( { Name => "Update", URL => "SoftKey:Update", 
                           Position => "1" });
  $mytext->AddSoftKeyItem( { Name => "Exit", URL => "SoftKey:Exit", 
                           Position => "2" });
  print $mytext->Content;
}


__END__

