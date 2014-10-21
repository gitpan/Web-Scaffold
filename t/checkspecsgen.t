# Before `make install' is performed this script should be runnable with
# `make test'. After `make install' it should work as `perl test.pl'

######################### We start with some black magic to print on failure.
# Change 1..1 below to 1..last_test_to_print .
# (It may become useful if the test is moved to ./t subdirectory.)

BEGIN { $| = 1; print "1..3\n"; }
END {print "not ok 1\n" unless $loaded;}

#use diagnostics;
do './recurse2txt';     # get my Dumper

use Web::Scaffold;
*checkspecs = \&Web::Scaffold::checkspecs;
*stylegen = \&Web::Scaffold::stylegen;

$loaded = 1;
print "ok 1\n";
######################### End of black magic.

# Insert your test code below (better if it prints "ok 13"
# (correspondingly "not ok 13") depending on the success of chunk 13
# of the test code):

$test = 2;

sub ok {
  print "ok $test\n";
  ++$test;
}

if (0) {
umask 027;
foreach my $dir (qw(tmp)) {
  if (-d $dir) {         # clean up previous test runs
    opendir(T,$dir);
    @_ = grep($_ ne '.' && $_ ne '..', readdir(T));
    closedir T;
    foreach(@_) {
      unlink "$dir/$_";
    }
    rmdir $dir or die "COULD NOT REMOVE $dir DIRECTORY\n";
  }
  unlink $dir if -e $dir;       # remove files of this name as well
}

my $dir = './tmp';
mkdir $dir,0755;
} # if 0

sub next_sec {
  my ($then) = @_;
  $then = time unless $then;
  my $now;
# wait for epoch
  do { select(undef,undef,undef,0.1); $now = time }
        while ( $then >= $now );
  $now;
}

sub gotexp {
  my($got,$exp) = @_;
  if ($exp =~ /\D/) {
    print "got: $got\nexp: $exp\nnot "
        unless $got eq $exp;
  } else {
    print "got: $got, exp: $exp\nnot "
        unless $got == $exp;
  }
  &ok;
}

################################################################
################################################################

my @defaults = (
# directory path for 'html pages', defaults to:
#
	pagedir		=> '../pages/',

# directory for 'javascript libriaries', defaults to:
#
	javascript	=> 'lib/',

# font family used throughout the document
#
	face		=> 'VERANDA,ARIAL,HELVETICA,SAN-SERIF',

# background color of the web page
# this can be a web color like 'white' or number '#ffffff'
#
	backcolor	=> 'white',

# Menu specifications
#
	barcolor	=> 'red',
	menudrop	=> '55',	# drop down position
	menuwidth	=> '100px',	# width of menu item
	pagewidth	=> '620px',	# recommended
# menu font specifications
	menucolor	=> 'black',
	menuhot		=> 'yellow',	# mouse over
	menucold	=> 'white',	# page selected
	menustyle	=> 'normal',	# bold, italic
	menusize	=> '13px',	# font points or pixels
	sepcolor	=> 'black',	# separator color

# Page link font specifications
#
	linkcolor	=> 'blue',
	linkhot		=> 'green',
	linkstyle	=> 'normal',	# bold, italic
	linksize	=> '13px',	# font points or pixels

# Page Text font specifications
#
 	fontcolor	=> 'black',
	fontstyle	=> 'normal',
	fontsize	=> '13px',

# Heading font specifications
#
	headcolor	=> 'black',
	headstyle	=> 'bold',	# normal, italic
	headsize	=> '16px',
);

## test 2	check setup of default specs
my $specs = {};
checkspecs($specs);
gotexp(Dumper($specs),Dumper({@defaults}));

# test 3	check style string
my $exp = q|<style type="text/css">
.mhs {
  background-color: red;
}
.dropdown {
  background-color: red;
  padding: 2px;
  border: solid 1px black;
}
#mh {
  position: relative;
  z-index: 50;
}
A.B {
  color: blue;
  background: transparent;
  font-family: VERANDA,ARIAL,HELVETICA,SAN-SERIF;
  font-weight: normal;
  font-size: 13px;
  text-decoration: underline;
}
A.B:hover {
  color: green;
}
A.NU {
  color: black;
  background: transparent;
  font-family: VERANDA,ARIAL,HELVETICA,SAN-SERIF;
  font-weight: normal;
  font-size: 13px;
  text-decoration: none;
}
A.NU:hover {
  color: yellow;
}
A.CP {
  color: white;
  background: transparent;
  font-family: VERANDA,ARIAL,HELVETICA,SAN-SERIF;
  font-weight: normal;
  font-size: 13px;
  text-decoration: none;
}
FONT.NU {
  color: black;
  background: transparent;
  font-family: VERANDA,ARIAL,HELVETICA,SAN-SERIF;
  font-weight: normal;
  font-size: 13px;
}
TD.NU {
  color: black;
  background: transparent;
  font-family: VERANDA,ARIAL,HELVETICA,SAN-SERIF;
  font-weight: normal;
  font-size: 13px;
}
TD.S {
  color: black;
  background: transparent;
  font-family: VERANDA,ARIAL,HELVETICA,SAN-SERIF;
  font-weight: normal;
  font-size: 13px;
}
.PT {
  color: black;
  background: transparent;
  font-family: VERANDA,ARIAL,HELVETICA,SAN-SERIF;
  font-weight: normal;
  font-size: 13px;
}
.HT {
  color: black;
  background: transparent;
  font-family: VERANDA,ARIAL,HELVETICA,SAN-SERIF;
  font-weight: bold;
  font-size: 16px;
}
#L1 {
  position: relative;
}
#menu1 {
  position: absolute;
  z-index: 100;
  visibility: hidden;
  width: 100px;
}
</style>
|;
my $got = stylegen($specs,1);
print "got:\n$got\nexp:\n$exp\nnot "
	unless $got eq $exp;
&ok;
