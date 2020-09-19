from googleapiclient.discovery import build
import pprint
from pathlib import Path
import json

api_key = 'xxx' 
cse_id = 'xxx' 

def google_search(service, query_keywords, api_key, cse_id):
    res = service.cse().list(q=query_keywords, cx=cse_id).execute()
    return res

def google_next_page(service, query_keywords, api_key, cse_id, res, page, max_page, url_items):
    next_res = service.cse().list(q=query_keywords, cx=cse_id, num=10, start=res['queries']['nextPage'][0]['startIndex'],).execute()
    for item in next_res['items']:
        url_items.append(item)
    page += 1
    
    if page == max_page:
        return url_items

    return google_next_page(service, query_keywords, api_key, cse_id, next_res, page, max_page, url_items)

if __name__ == "__main__":

    service = build("customsearch","v1", developerKey=api_key)

    # ====== create the dictionary object to save parameters for scrapy ======
    settings_json = {'name':[], 'allowed_domains':[], 'start_urls':[]}
    # create the url and domain list
    urls_list = []
    urls_pdf_list = []
    domains_list = []
    
    # define the key words to query 
    key_words = 'xxx'

    # query the first page
    result = google_search(service = service, query_keywords=key_words, api_key = api_key, cse_id = cse_id)
    # append the result from first page
    url_items = result['items']
    # pprint.pprint(result)

    # go through the top three pages only
    # define the pages to scrap
    max_page = 3
    url_items = google_next_page(service = service, query_keywords=key_words, api_key = api_key, cse_id = cse_id, res = result, page=0, max_page = max_page, url_items = url_items)

    # loop the pages
    # pprint.pprint(url_items)
    for items in url_items:
        # pprint.pprint(item)
        # single item is a dictionary object
        # check whether it is the pdf format or not
        try:
            # pprint.pprint(item)            
            if 'fileFormat' in items.keys():        
                # separate the urls for pdf, then go to pdf parser module than scrapy part
                urls_pdf_list.append(items['link'])
            else:
                urls_list.append(items['link'])
                domains_list.append(items['displayLink'])
        except Exception as e:
            print(e)
            continue

    # pass the values to settings_json
    settings_json['name'] = key_words
    settings_json['allowed_domains'] = domains_list
    settings_json['start_urls'] = urls_list

    # get the current path
    current_path = Path(__file__).parent.absolute()
    # define the output folder for normal links
    result_output = current_path/'output'/'urls'
    # define the output folder for pdf links
    result_pdf_output = current_path/'output'/'pdf_urls'
    # create new folders if the folder does not exist
    for output_folder in [result_output, result_pdf_output]:
        if not output_folder.is_dir():
            output_folder.mkdir (parents=True, exist_ok=True)
    
    # save the pdf result and the settings_json result
    with Path(result_output/'query_result.json').open('w') as fw:
        json.dump(settings_json, fw)
    
    with Path(result_pdf_output/'query_pdf_result.txt').open('w') as pw:
        for url in urls_pdf_list:
            pw.write(url+'\n')
