wordpress-tag-importer
======================

A tool to import tags into WordPress using Scrapy (http://scrapy.org/) and WP-CLI (http://wp-cli.org/).

This project has some hardcoded paths and xpath selectors, but should be easily modified for other projects.  It was originally developed to import tags from Squarespace.  The official Squarespace exporter did not include tag information.  Use this tool to import the posts into WordPress: https://github.com/gfreeau/squarespace-to-wordpress-plugin.

Usage
-----

    $ scrapy crawl northstar

This generates a file called items.jl that contains a list of post titles and associated tags.

Get a list of the post ids and associated titles:

    $ php ~/wp-cli.phar post list --fields=ID,post_title --format=json > ~/post_ids.json

Then run this script to associate the posts with the new tag information and update the posts in the new WordPress installation.

    $ python update_tags.py

