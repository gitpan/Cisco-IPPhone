#!/usr/bin/perl

use Cisco::IPPhone;

$mygraphicmenu = new Cisco::IPPhone;

$data = "0C3F0F030C3F0C303F3F";

# Create Menu Object
$mygraphicmenu->GraphicMenu( { Title => "My Image", 
                   Prompt => "View the image",
                   LocationX => "-1", LocationY => "-1", 
                   Width => "5",
                   Height => "5", 
                   Depth => "2", 
                   Data => "$data" });
print $mygraphicmenu->Content;
