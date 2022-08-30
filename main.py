#1차 목표 
# 셀레니움을 이용하여 네이버 리뷰 수집
# to do: 주소 중복 검사 필요

import sys    
import os     

import pandas as pd    
import numpy as np     

from bs4 import BeautifulSoup     
from selenium import webdriver    
from selenium.webdriver.common.keys import Keys

import time                      
import math

import pandas as pd

#path는 각자 컴퓨터에 맞게 변경 필요
path_driver = "E:\python\data_collect\data_ml_pr\chromedriver.exe"
path_data = r'E:\python\anireview_blog_pr\data_a.xlsx'
data_pd = pd.read_excel(path_data)
adress = data_pd['소재지지번주소'].values.tolist()
name = data_pd['사업장명'].values.tolist()

driver = webdriver.Chrome(path_driver)

#경기도 동물병원 현황 엑셀 불러오기 및 판다스 변환

# 한사이클 순서

# 화면1
# 네이버 지도 검색창
# 경기도 동물병원현황 엑셀 소재지 지번주소 검색
# 이주소의 장소 더보기 클릭

driver.get("https://map.naver.com")
time.sleep(2)

search_input = driver.find_element_by_xpath("/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div[1]/div/input")
search_input.send_keys(adress[10] + Keys.ENTER)

time.sleep(2)
try:
    viewmore = driver.find_element_by_class_name("link_more").click()
    time.sleep(2)
except:
    print("eror1: no place in the adress")


# 화면2
# 동물병원 텍스트 찾기
# try => 링크 클릭
# except => error code => pass

try:
    keyword = "동물병원"  
    # foo 변수를 가진 요소를 찾으려면
    hospital = driver.find_element_by_xpath("//div[.='" + keyword + "']")
    for i in range(2):
        hospital = hospital.find_element_by_xpath('..')
    time.sleep(3)
except:
    print("error2: no animal hospital in the place")



# 화면3(true)
# 이용 시간 + 전화번호 추출
# 리뷰 여부 확인
# try
# 방문자 리뷰 더보기 클릭
# except
# error code => pass

driver.close()

# 화면4(true)
# 리뷰추출 ~ 더보기 클릭(더보기 클릭 없을 때까지 반복)


#음...

