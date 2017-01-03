from django.shortcuts import render
import psycopg2,traceback
from django.http import HttpResponse
from django.shortcuts import render_to_response
url =''
insert =''
"""
try:
   conn = psycopg2.connect("dbname = 'malicious_urls' user = 'postgres' host = 'localhost' password= 'password' ")
   print "Hifdnvfdlj"
except:
   print "Unable to connect to the database" 
# Create your views here.
cur = conn.cursor()
"""
def crawl(request):
                conn = psycopg2.connect("dbname = 'malicious_urls' user = 'postgres' host = 'localhost' password = 'password' ")
                cur = conn.cursor() 
# Create your views here.	
		cur.execute("SELECT * FROM malicious_websites")		
		malicious_websites = cur.fetchall()		
		malicious_urls = dict()
		i=0
		for item in malicious_websites:
			malicious_urls.update({i:item})
			i=i+1
                print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                #return HttpResponse(table)		  
		return render(request,"index.html",{'urls' : malicious_websites })
		
def entry(request):
	if request.method =='POST': 
		url = request.POST.get('textfield',None)
		html = ("<H1>url added:" + url + "</H1>")
                site=str(url)
                print  type(url)
                print type(site)
		try:
                   insert = "INSERT INTO malicious_websites (domain) VALUES ('" + site + "')"
                   print insert
		   dbinsert(insert)
                   print "$%%$$$$$$$$$$$$$$$$$$$$$$$$$$"
		except:
			print url
			print(traceback.format_exc())
			print("Unable to insert into the database")
		return HttpResponse(html)
	else:
		   return render(request,'form.html')
	      
def dbinsert(url):
       try:
          conn = psycopg2.connect("dbname = 'malicious_urls' user = 'postgres' host = 'localhost' password= 'password' ")
       except:
          print "Unable to connect to the database"
        
       cur = conn.cursor()
       cur.execute(url)
       conn.commit()
def main(request):
       try:
          conn = psycopg2.connect("dbname = 'malicious_urls' user = 'postgres' host = 'localhost' password='password' ")
       except:
          print "Unable to connect to the database"
       return render(request,"main.html")
