#!/usr/bin/perl

use Cisco::IPPhone;

$myimage = new Cisco::IPPhone;

$data = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1F001000001F00FF0F40FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF010001000001401F00F4FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF01FF011FF001F401F4FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1FF01F00401F000F40FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF01FF0100F4010104F4FFFFFFFFFFFFFFFFFFFFFFFFFFFF41FFFF1FF01FF0011F104040FFF1F4FFFFFFFFFFFFFFFFFFFFFF1144FF1F00100000F0000F0F404F04FFFFFFFFFFFFFFFFFFFFFFFF14FFFF01000100F00FF0F000F40FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1F';

# Create Menu Object
$myimage->Image( { Title => "IBM Image", Prompt => "View the image",
                 LocationX => "-1", LocationY => "-1", Width => "53",
                 Height => "23", Depth => "2", Data => "$data" });

# Add SoftKeyItems to Menu Object
$myimage->AddSoftKeyItem({ Name => "Select", URL => "SoftKey:Select", 
                          Position => "1" });
$myimage->AddSoftKeyItem({ Name => "Exit", URL => "SoftKey:Exit", 
                          Position => "2" });

# Print the Menu Object to the Phone
print $myimage->Content;

__END__
~;
