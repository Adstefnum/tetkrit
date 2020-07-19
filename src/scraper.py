import requests
from bs4 import BeautifulSoup

site_list = ["https://angel.co/jobs",
			r"https://internshala.com/internships/work-from-home-.net%20development,analytics,android,angular.js%20development,artificial%20intelligence%20(ai),internet%20of%20things%20(iot),ios,mobile%20app%20development,software%20development-jobs/part_time-true/ppo-true",
			"https://www.indeed.com/jobs?q=software+engineer&explvl=entry_level"]

#use threading
for s in site_list:
	page = requests.get(s)
	soup = BeautifulSoup(page.content,"html.parser")
	links = list(soup.find_all('a', href= True))
	#write i['href'] to database