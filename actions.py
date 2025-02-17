from SimplerLLM.tools.rapid_api import RapidAPIClient

def get_seo_page_report(url :str):
    api_url = "https://seo-analyzer3.p.rapidapi.com/seo-audit-basic"
    api_params = {
        'url': url,
    }
    api_client = RapidAPIClient(api_key="28fa374bb3mshcee546e09fac28ep11043bjsn1d6e5b460873") 
    response = api_client.call_api(api_url, method='GET', params=api_params)
    return response