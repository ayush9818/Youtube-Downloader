from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pytube import YouTube

SAVE_PATH = './'

def download_video(link, video_name):
    yt = YouTube(link)
    try:
        yt.streams.filter(progressive = True,
        file_extension = "mp4").first().download(output_path = SAVE_PATH,
        filename = video_name)
    except:
        print("Some Error!")
    print('Task Completed!')


def parse_link(driver,url_name):
    driver.get(f'https://www.youtube.com/results?search_query={url_name}')
    content = driver.page_source.encode("utf-8").strip()
    soup = BeautifulSoup(content,'lxml')
    titles = soup.findAll('a',id='video-title')
    views = soup.findAll('span',class_='style-scope ytd-video-meta-block')
    video_urls = soup.findAll('a',id='video-title')
    i = 0
    j = 0
    index_to_url = {}
    for title in titles:
        try:
            print("\n{}\t{}\t{}\t{}\thttps:\\youtube.com{}".format(j,title.text[2:],views[i].text,views[i+1].text,video_urls[j].get('href')))

            index_to_url[j] = {}
            index_to_url[j]['link'] = 'https:\\youtube.com{}'.format(video_urls[j].get('href'))
            index_to_url[j]['video_name'] = title.text[2:]

            i+=2
            j+=1
        except:
            continue
    return index_to_url




def main():

    video_name = input("Enter Video to download :\n>")

    options = Options()
    options.binary_location = '/usr/bin/brave-browser'
    options.add_experimental_option("detach", True)
    driver_path = '/usr/bin/chromedriver'
    driver = webdriver.Chrome(options = options, executable_path = driver_path)



    url_name = "+".join(video_name.split(' '))

    index_to_url = parse_link(driver,url_name)
    download_index = int(input("Enter Video number :\n>"))

    download_video(index_to_url[download_index]['link'],index_to_url[download_index]['video_name'])


if __name__ == "__main__":
    main()
