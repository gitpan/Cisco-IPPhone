#!/usr/bin/perl

# Mark Palmer markpalmer@us.ibm.com

# Use a browser to run this CGI
use Cisco::IPPhone;

$myexecute = new Cisco::IPPhone;

$IPPHONE = "192.168.250.7";
$SERVER = "192.168.250.17";
$URL = "http://$SERVER/cgi-bin/menu.cgi"; # push this URL to the phone

print "Content-Type: text/html\n\n<HTML><BODY>\n";
print "<FORM action=\"http://$IPPHONE/CGI/Execute\" Method=\"POST\">\n";
print "<TEXTAREA NAME=\"XML\" Rows=\"5\" Cols=\"60\">\n";

$myexecute->Execute;
$myexecute->AddExecuteItem({ ExecuteItem=>$URL });
print $myexecute->Content_Noheader;

print "</TEXTAREA><BR><input type=submit value=POST></FORM></BODY></HTML>\n";

