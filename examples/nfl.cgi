#!/usr/bin/perl

# Mark Palmer markpalmer@us.ibm.com

use Cisco::IPPhone;
use LWP;
use CGI;

$ua = LWP::UserAgent->new;
$mytext = new Cisco::IPPhone;
$error = new Cisco::IPPhone;
$query = new CGI;

my $host = "www.nfl.com";
my $url = "scores";
$completeurl = "http:\/\/$host\/$url";

my $request = HTTP::Request->new(GET => $completeurl);
my $response = $ua->request($request);

if ($response->is_success) {
 # It was successful, so parse the form

 $results = $response->content;

 @lines = split ('\n', $results);
$counter = 0;
$team = '';
$score = -1;
foreach $line (@lines) {
  $team = $1 if ($line =~ /\/teams\/news\/(\S+)"/);
  $score = $1 if ($line =~ /finalscore">(\d+)</);
  if ($line =~ /"columnrow".*>(.*)<\/t.>/) {
    $timeleft = $1;
    $timeleft =~ s/&nbsp//g;
  }
  if ($score >= 0) {
    $counter++;
    $text .= "$team : $score ";
    if ($counter % 2 == 0) {
      $text .= "$timeleft\n";
      $timeleft = '';
    }
    $team = '';
    $score = -1;
  }
}

$mytext->Text( { Title => "NFL Scores from nfl.com", Prompt => "Go Packers", 
          Text => "$text" });
$mytext->AddSoftKeyItem( { Name => "Update", URL => "SoftKey:Update", 
                           Position => "1" });
$mytext->AddSoftKeyItem( { Name => "Exit", URL => "SoftKey:Exit", 
                           Position => "2" });
print $mytext->Content ({ Refresh=>"60" });
} else {
  $mytext->Text( { Title => "NFL Scores from nfl.com", Prompt => "Go Packers", 
                           Text => "Unable to access $completeurl" });
  $mytext->AddSoftKeyItem( { Name => "Update", URL => "SoftKey:Update", 
                           Position => "1" });
  $mytext->AddSoftKeyItem( { Name => "Exit", URL => "SoftKey:Exit", 
                           Position => "2" });
  print $mytext->Content;
}

__END__
