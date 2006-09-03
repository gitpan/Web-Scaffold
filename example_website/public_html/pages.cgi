#!/usr/bin/perl
#
# pages.cgi.example
# version 1.00, 8-30-06, michael@bizsystems.com
#
use Web::Scaffold;

%specs = (

# directory path for 'html pages', defaults to:
#
	pagedir		=> '../pages',

# font family used throughout the document
#
	face		=> 'VERANDA,ARIAL,HELVETICA,SAN-SERIF',

# background color of the web page
# this can be a web color like 'white' or number '#ffffff'
#
	backcolor	=> 'white',

# Menu specifications
#
	barcolor	=> '#0000CC',
	menudrop	=> '55',	# drop down position
	menuwidth	=> '100px',	# width of menu item
	pagewidth	=> '620px',	# recommended
# meNU font specifications - class='NU'
	menucolor	=> 'gold',
	menuhot		=> 'red',	# mouse over
	menucold	=> 'white',	# page selected
	menustyle	=> 'bold',	# bold, italic
	menusize	=> '13px',	# font points or pixels
	sepcolor	=> 'gold',	# separator color

# Basic link font specifications - class='B'
#
	linkcolor	=> 'blue',
	linkhot		=> 'green',
	linkstyle	=> 'normal',	# bold, italic
	linksize	=> '13px',	# font points or pixels

# Page Text font specifications - class='PT'
#
 	fontcolor	=> 'black',
	fontstyle	=> 'normal',
	fontsize	=> '13px',

# Heading Text specifications - class='HT'
#
	headcolor	=> 'black',
	headstyle	=> 'bold',	# normal, italic
	headsize	=> '16px',
);

=pod

The specifications for menus and pages. Menus can be single link or a series
of drop down menu depending on how you specifiy the page. The page names are
the keys to the hash and are used as the menu-bar link text. All page files
are placed in the 'pages' directory. 

FILE NAME SYNTAX:

Files are named with the 'key' name of the page as the lefthand side and 
a suffix designating the file's purpose as the right hand side. For the 
required page 'Home', they are as follows:

 # [optional] page used if there are not individual pages
 # NOTE: neither a Default page or individual page is required
  Default.meta		# meta text loaded after <title>
  Default.head		# optional additional <head> text
			# that is on every page, end of page
  Default.top		# optional body text that appears
			# on every page before menu-bar
			# i.e. logo, etc...
 # for each individual page
  Home.meta		# meta text loaded after <title>
  Home.head		# optional additional <head> text
  Home.top		# body text that appears before
			# menu-bar. i.e. logo, etc...
  Home.c1		# column 1 content
  Home.c2		# column 2 content
  Home.cn		# column 'n' content

=cut

my $menu = [qw(
	Home
	Schema
	Page-Source
	manpage
)];

my $copyright = 'Copyright 2006, Michael@bizsystems.com';

%pages = (

# REQUIRED page
#
	Home	=> {
	    menu	=> $menu,
# optional title text - if missing, 'heading' text will be used
	    title	=> 'Web::Scaffold, a perl extension for building web sites',

	    heading	=> '&nbsp;&nbsp;&nbsp;&nbsp;A perl extension for building web sites',

# number of columns and column width in pixels
	    column	=> [20, 160, 400],    # two columns

# optional
	    submenu	=> [qw(specs pages)], # drop down menu

# optional trailer bar
	    trailer	=> {

# a named page
#		links	=> [qw(Page5 Page6)],

# optional right hand side text. if there are no links then the
# text will be placed on the left hand side of the trailer bar
		text	=> $copyright,
	    },
	},

	Schema	=> {
	    menu	=> $menu,
	    title	=> 'Web::Scaffold example site schema',
	    heading	=> '&nbsp;&nbsp;Site Schema for this example',
	    column	=> ['50%', '50%'],
	    submenu	=> ['Structure'],
	    trailer	=> {
		links	=> ['Home'],
		text	=> $copyright,
	    },
	},
	Structure	=> {
	    menu	=> $menu,
	    title	=> 'Web::Scaffold page structure',
	    heading	=> '&nbsp;&nbsp;Site schema and page structure',
	    column	=> ['50%', '50%'],
	    trailer	=> {
		links	=> ['Home'],
		text	=> $copyright,
	    },
	},

	'Page-Source'	=> {
	    menu	=> $menu,
	    title	=> 'Web::Scaffold, page source text',
	    heading	=> '&nbsp;&nbsp;&nbsp;&nbsp;View the Page Source text',
	    column	=> [qw( 20 600)],
	    submenu	=> [qw(Default.meta Default.top Home.meta Home.c2 Home.c3 pages.cgi scaffold.js winMenus.js winUtils.js)],
	    trailer	=> {
		links	=> ['Home'],
		text	=> $copyright,
	    },
	},
	manpage		=> {
	    menu	=> $menu,
	    heading	=> 'Web::Scaffold manpage',
	    trailer	=> {
		links	=> ['Home'],
		text	=> $copyright,
	    },
	},
	specs		=> {
	    menu	=> $menu,
	    heading	=> 'Typical specification hash: %specs, (from POD)',
	    column	=> [20, 600],
	    trailer	=> {
		links	=> ['Home'],
		text	=> $copyright,
	    },
	},
	pages		=> {
	    menu	=> $menu,
	    heading	=> 'Typical specification hash: %pages, (from POD)',
	    column	=> [20, 600],
	    trailer	=> {
		links	=> ['Home'],
		text	=> $copyright,
	    },
	},


# and for debug... example
# load this page segment as source in a single window
#            location    => 'path/to/filename',

	'Default.meta'	=> {
# copy prototype page structure from this page. 

	    debug	=> 'Page-Source',
	},
	'Default.top'	=> {
	    debug	=> 'Page-Source',
	},
	'Home.meta'	=> {
	    debug	=> 'Page-Source',
	},
	'Home.c2'	=> {
	    debug	=> 'Page-Source',
	},
	'Home.c3'	=> {
	    debug	=> 'Page-Source',
	},
	'pages.cgi'	=> {
	    debug	=> 'Page-Source',
	    location	=> './pages.cgi',
	},
	'scaffold.js'	=> {
	    debug	=> 'Page-Source',
	    location	=> 'lib/scaffold.js',
	},
	'winUtils.js'	=> {
	    debug	=> 'Page-Source',
	    location	=> 'lib/winUtils.js',
	},
	'winMenus.js'	=> {
	    debug	=> 'Page-Source',
	    location	=> 'lib/winMenus.js',
	},
#
#	... and so on

);

Web::Scaffold::build(\%specs,\%pages);
