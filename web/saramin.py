import requests
from bs4 import BeautifulSoup

def search_saramin(keyword):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    jobs = []
    url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchword={keyword}"
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 사람인 공고 리스트 태그
    item_list = soup.select(".item_recruit")
    
    for item in item_list:
        try:
            company = item.select_one(".corp_name a").text.strip()
            title = item.select_one(".job_tit a").text.strip()
            href = "https://www.saramin.co.kr" + item.select_one(".job_tit a").get("href")
            location = item.select_one(".job_condition span").text.strip()

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "href": href
            })
        except:
            continue
            
    return jobs