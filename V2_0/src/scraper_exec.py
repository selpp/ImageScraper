# scraper_exec.py

# Dependencies
import argparse
from DataBase.mysql_db import MySqlSession
from Modules.flickr_scraper import FlickrScraper

# Logo
logo = '        __\n'
logo +='       :##;__\n'           
logo +='     @@@@@@@@,__\n'        
logo +="   '@@`     @@@__\n"       
logo +="  '@;  @+    `@@__\n"      
logo +=' `@; +@       `@;__\n'     
logo +=' @@ +@         +@__\n'     
logo +=' @` @           @,__\n'    
logo +=':@ @            @@__\n'    
logo +='+@ +            #@__\n'    
logo +='#@              #@__           TIDMARSH IMAGE SCRAPER V2.0\n'    
logo +=';@              @@__\n'    
logo +=' @              @;__\n'    
logo +=' @@            :@__\n'     
logo +=' ,@`           @#__\n'     
logo +='  @@`         @@__\n'      
logo +='   @@+      :@@@.__\n'     
logo +='    ;@@@##@@@# ,@@__\n'    
logo +='      ,@@@@;    @@@__\n'   
logo +='                 @@@__\n'  
logo +='                  @@@__\n' 
logo +='                   @@#__\n'
logo +='                    #__\n' 


def main(search, label, table):
	print(logo)

	database = MySqlSession('APIKeys/MySqlConfig.json', table)

	flickr_scraper = FlickrScraper(500, 'APIKeys/FlickrAPIConfig.json')
	flickr_scraper.scrap_images(search, database, label)

	database.disconnect()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Scrap images url from web services and add them into a Mysql database")
	parser.add_argument("-s","--search", help = "The search terms you want to look for to find images")
	parser.add_argument("-l","--label", help = "The label of the class theese images should belong to")
	parser.add_argument("-t","--table", help = "The database table in which you want to add images")
	args = parser.parse_args()

	search = args.search
	label = int(args.label)
	table = args.table

	if (search is None) or (search == '') or (label is None) or (label < 0) or (table is None) or (table == ''):
		print('[Main] Look at your args. If you do not know how to use this program call --help ...')
		exit(2)

	main(search, label, table)
