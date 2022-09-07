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

import csv 

from difflib import SequenceMatcher

#path는 각자 컴퓨터에 맞게 변경 필요
path_driver = "naver_review_crawling\chromedriver.exe"
# path_data = r'naver_review_crawling\excel_data\data_renew.xlsx'
# data_pd = pd.read_excel(path_data)
# address = data_pd['주소이름'].values.tolist()
# name = data_pd['사업장명'].values.tolist()

driver = webdriver.Chrome(path_driver)

#경기도 동물병원 현황 엑셀 불러오기 및 판다스 변환

# 한사이클 순서

# 화면1
# 네이버 지도 검색창
# 경기도 동물병원현황 엑셀 소재지 지번주소 검색
# 이주소의 장소 더보기 클릭
# hole_data = []
# count_progress = 0
# start_index = 0

    
# name_roop = name[count_progress+start_index]
# print(name_roop)
driver.get("https://map.naver.com")
time.sleep(4)
search_input = driver.find_element_by_xpath("/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div[1]/div/input")
# search_input.send_keys(address_roop + Keys.ENTER)
search_input.send_keys("경기도 가평군 청평면 청평리 438-23번지 경기동물병원 경기동물병원" + Keys.ENTER)
time.sleep(2)
for i in range(10):
    try:
        driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div/div[3]/a[2]').click()
    except:
        break
try:
    viewmore = driver.find_element_by_class_name("link_more").click()
    time.sleep(2)
except:
    # print("eror1: no place in the address")
    pass

# 화면2
# 페이지 넘기면서 동물병원 텍스트 찾기
# try => 링크 클릭
# except => error code => pass

#to do: 건물에 있는 영업점의수가 많을때

# a = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-address/entry-address-detail-place/div[2]/div/div/div/div[2]/div[1]')
# for i in range(2):
#     a = a.find_element_by_xpath('..')
# a.click()
# time.sleep(3)
keyword = "경기동물병원"
hospital = driver.find_elements_by_xpath("//div[.='" + keyword + "']")
for i in hospital:
    for j in range(2):
        i = i.find_element_by_xpath('..')
        print("1")
    try:
        i.click()
        time.sleep(3)
    except:
        pass
# hospital_exist = 0
# while(1):
#     try:
        
#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#         hospital_name = soup.find_all(class_ = 'search_title')
#         hospital_name = [hospital_n.get_text() for hospital_n in hospital_name]
#         soup= 0
#         name_exist = 0
#         for i in hospital_name:
#             i_r = i.replace(" ","")
#             name_roop_r = name_roop.replace(" ","")

#             print(i_r)
#             print(name_roop_r)

#             try:
#                 c = i_r.replace("동물병원", "")
#             except:
#                 c = i_r
#             try:
#                 d = name_roop_r.replace("동물병원","")
#             except:
#                 d = name_roop_r
            
#             ratio = SequenceMatcher(None, c, d).ratio()
            
#             if ratio >= 0.5:
#                 name_exist = 1
#                 print("잇다고!!!!!!!11")
#                 keyword = i 
#                 hospital = driver.find_element_by_xpath("//strong[.='" + keyword + "']")
#                 print(hospital.text, "+++++++++=")
#                 break

#         if name_exist == 1:   
#             for i in range(3):
#                 hospital = hospital.find_element_by_xpath('..')
#                 print(hospital)
#             hospital.click()
#             time.sleep(3)
            
#             hospital_exist = 1
#             break
#     except:
#         # print("case: this page doesn't contain hospital name")
#         pass
#     try:
#         next_button = driver.find_element_by_class_name("btn_next")
#         next_button.click()

#         next_button = 0
#         time.sleep(2)
#     except:
#         # print("alert: page finish")
#         # print("error2: no hospital in the place")
#         break
#     try:
#         next_button = driver.find_element_by_class_name("btn_next")
#         enabled_false = next_button.is_enabled()
#         if enabled_false == False:
#             # print("error: no hospital in the place")
#             break
#     except:
#         pass
# time.sleep(2)
