# -*- coding: utf-8 -*-

# Scrapy settings for northstar project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'northstar'

SPIDER_MODULES = ['northstar.spiders']
NEWSPIDER_MODULE = 'northstar.spiders'
ITEM_PIPELINES = { 'northstar.pipelines.JsonWriterPipeline': 500 }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'northstar (+http://www.yourdomain.com)'
