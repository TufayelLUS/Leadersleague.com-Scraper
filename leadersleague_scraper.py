import requests
import csv
import os


countries = {
    "BR": "bresil",
    "PE": "perou",
    "CO": "colombia",
    "IT": "italie",
    "ES": "espagne",
    "DE": "allemagne",
    "CH": "suisse",
    "CL": "chile",
    "BE": "belgique",
    "LU": "luxembourg",
    "PT": "portugal",
    "MX": "mexico",
    "FR": "france",
    "EC": "ecuador",
    "AR": "argentina",
    "AC": None,
    "AF": None,
    "CA": "canada",
    "BO": "bolivia",
    "UY": "uruguay",
    "GB": "royaume-uni",
    "US": "etats-unis",
    "CN": "chine"
}


def saveData(dataset):
    with open('leads.csv', mode='a+', encoding='utf-8-sig', newline='') as csvFile:
        fieldnames = [
            "Email", "First Name", "Last Name", "Full Name", "Job Position", "Company Name", "Company URL", "Region", "Category", "LeadersLeague Link"
        ]
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames,
                                delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if os.stat('leads.csv').st_size == 0:
            writer.writeheader()
        writer.writerow({
            "Email": dataset[0],
            "First Name": dataset[1],
            "Last Name": dataset[2],
            "Full Name": dataset[3],
            "Job Position": dataset[4],
            "Company Name": dataset[5],
            "Company URL": dataset[6],
            "Region": dataset[7],
            "Category": dataset[8],
            "LeadersLeague Link": dataset[9]
        })


def getCategory(subtopic):
    link = f'https://api.leadersleague.com/subtopic/{subtopic}'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(link, headers=headers).json()
    except:
        print("Failed to open {}".format(link))
        return ""
    contents = resp.get('contents', [])
    for content in contents:
        if content.get('lang', '') == 'fr_FR':
            return content.get('title', '')
    return ""


def getState(state):
    link = f'https://api.leadersleague.com/state/{state}'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(link, headers=headers).json()
    except:
        print("Failed to open {}".format(link))
        return ""
    contents = resp.get('contents', [])
    for content in contents:
        if content.get('lang', '') == 'fr_FR':
            return content.get('name', '')
    return ""


def getProfession(profession):
    link = f'https://api.leadersleague.com/profession/{profession}'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(link, headers=headers).json()
    except:
        print("Failed to open {}".format(link))
        return ""
    contents = resp.get('contents', [])
    for content in contents:
        if content.get('lang', '') == 'fr_FR':
            return content.get('title', '')
    return ""


def getPersonSingleDetail(person_slug, company_name, company_url, parent_link, region, category, job_only=False):
    link = f'https://api.leadersleague.com/people/{person_slug}/aggregate'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    try:
        people = requests.get(link, headers=headers).json()
    except:
        print("Failed to open {}".format(link))
        return
    first_name = people.get('firstname', '')
    last_name = people.get('lastname', '')
    full_name = first_name + ' ' + last_name
    try:
        job_position = people.get('jobs').get('job')
    except:
        job_position = ''
    if job_only:
        return job_position
    email = people.get('email', '')
    profile_link = "https://www.leadersleague.com/fr/peoples/" + \
        people.get('slug')
    print("Person Full Name: {}".format(full_name))
    print("Person Profile Link: {}".format(profile_link))
    print("Person Job Position: {}".format(job_position))
    print("Person Email: {}".format(email))
    print("Company Name: {}".format(company_name))
    print("Company URL: {}".format(company_url))
    print("Region: {}".format(region))
    dataset = [email, first_name, last_name, full_name,
               job_position, company_name, company_url, region, category, parent_link]
    saveData(dataset)


def getPersonList(company_uuid, company_slug, company_name, company_url, parent_link, region, category):
    link = f"https://api.leadersleague.com/company-page/{company_slug}/aggregate?page=1&perpage=500&companyUuid={
        company_uuid}&country=france-1&expertise=gestion-de-patrimoine"
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(link, headers=headers).json()
    except:
        print("Failed to open {}".format(link))
        return []
    for people in resp.get('peoples', []):
        first_name = people.get('firstName', '')
        last_name = people.get('lastName', '')
        full_name = first_name + ' ' + last_name
        job_position = getPersonSingleDetail(people.get(
            'slug'), company_name, company_url, parent_link, region, category, job_only=True)
        email = people.get('email', '')
        profile_link = "https://www.leadersleague.com/fr/peoples/" + \
            people.get('slug')
        print("Person Full Name: {}".format(full_name))
        print("Person Profile Link: {}".format(profile_link))
        print("Person Job Position: {}".format(job_position))
        print("Person Email: {}".format(email))
        print("Company Name: {}".format(company_name))
        print("Company URL: {}".format(company_url))
        print("Region: {}".format(region))
        print("Company UUID: {}".format(company_uuid))
        dataset = [email, first_name, last_name, full_name,
                   job_position, company_name, company_url, region, category, parent_link]
        saveData(dataset)


def getCompanyWebsite(company_uuid):
    link = f'https://api.leadersleague.com/firm/{company_uuid}/aggregate'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(link, headers=headers).json()
    except:
        print("Failed to open {}".format(link))
        return None
    return resp.get('websiteUrl')


def listCompanies(link, parent_link):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(link, headers=headers).json()
    except:
        print("Failed to open {}".format(link))
        return
    state = resp.get('states')
    if state:
        state = getState(state)
    if not state:
        try:
            region = resp.get('countries')
            region_matched = countries.get(region, region)
            if region_matched is None:
                region = region.title()
            else:
                region = region_matched.title()
        except:
            region = resp.get('countries')
    else:
        region = state
    print("Region: {}".format(region))
    category = resp.get('subtopics', "")
    profession = resp.get('professions')
    if category:
        category = getCategory(category)
    if not category:
        category = getProfession(profession)
    print("Category: {}".format(category))
    companies = resp.get('companies', [])
    companies = sorted(companies, key=lambda x: (
        x['level'], x['sublevel'], x['position']))
    for company in companies:
        company_name = company.get('name')
        print("Company: {}".format(company_name))
        company_uuid = company.get('uuid')
        company_slug = company.get('slug')
        company_url = getCompanyWebsite(company_uuid)
        if not company.get('isCompanyPage'):
            peoples = company.get('peoples', [])
            for people in peoples:
                people_uuid = people.get('uuid')
                if people_uuid is None:
                    continue
                try:
                    getPersonSingleDetail(
                        people_uuid, company_name, company_url, parent_link, region, category)
                except:
                    print("Error getting person data for person uuid {}".format(
                        people_uuid))
        else:
            try:
                getPersonList(company_uuid, company_slug, company_name,
                              company_url, parent_link, region, category)
            except:
                print("Error getting person list for company {}".format(company_name))


def getCompanyWebsite(company_slug):
    link = f'https://api.leadersleague.com/firm/{company_slug}/aggregate'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(link, headers=headers).json()
    except:
        print("Failed to open {}".format(link))
        return ''
    return resp.get('websiteUrl')


if __name__ == "__main__":
    links = open('links.txt', mode='r', encoding='utf-8').read().split('\n')
    for parent_link in links:
        if parent_link == "":
            continue
        print("Checking link {}".format(parent_link))
        converted_link = parent_link.split('/')
        if converted_link[-1] == "":
            converted_link = converted_link[:-2]
        else:
            converted_link = converted_link[-1]
        api_link = f"https://api.leadersleague.com/ranking/n9F4oEK34Rc-0/content/{
            converted_link}/aggregate"
        try:
            listCompanies(api_link, parent_link)
        except:
            print("An exception occured while processing company listing, log is below")
            import traceback
            traceback.print_exc()
