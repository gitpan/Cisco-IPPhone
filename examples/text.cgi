#!/usr/bin/perl

use Cisco::IPPhone;

$mytext = new Cisco::IPPhone;

$mytext->Text( { Title => "My Title", Prompt => "My Prompt", 
                           Text => "My Text" });
$mytext->AddSoftKeyItem( { Name => "Update", URL => "SoftKey:Update", 
                           Position => "1" });
$mytext->AddSoftKeyItem( { Name => "Exit", URL => "SoftKey:Exit", 
                           Position => "2" });

print $mytext->Content;

__END__
