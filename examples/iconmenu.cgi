#!/usr/bin/perl

use Cisco::IPPhone;

$myiconmenu = new Cisco::IPPhone;

$data = "0C3F0F030C3F0C303F3F";

# Create Icon Menu
$myiconmenu->IconMenu( { Title => "My Title", 
                   Prompt => "My Prompt" });

$myiconmenu->AddMenuItem({ Name => "Item 2", 
                       URL => "http://www.mydomain.com" });

# Index is the numeric index of the icon to be displayed
# Up to 10 instances of iconitem can be displayed
$myiconmenu->AddIconItem ({ Index => "1", 
                            Width => "5",
                            Height => "5", 
                            Depth => "2", 
                            Data => "$data" });

print $myiconmenu->Content;
