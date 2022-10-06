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
path_data = r'naver_review_crawling\excel_data\data_renew.xlsx'
data_pd = pd.read_excel(path_data)
address = data_pd['주소이름'].values.tolist()
name = data_pd['사업장명'].values.tolist()

driver = webdriver.Chrome(path_driver)

#경기도 동물병원 현황 엑셀 불러오기 및 판다스 변환

# 한사이클 순서

# 화면1
# 네이버 지도 검색창
# 경기도 동물병원현황 엑셀 소재지 지번주소 검색
# 이주소의 장소 더보기 클릭
hole_data = []
count_progress = 0
start_index = 0
for address_roop in address[start_index:]:
    
    name_roop = name[count_progress+start_index]
    print(name_roop)
    driver.get("https://map.naver.com")
    time.sleep(4)
    search_input = driver.find_element_by_xpath("/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div[1]/div/input")
    search_input.send_keys(address_roop + Keys.ENTER)
    # search_input.send_keys("경기도 고양시 일산서구 주엽동 17번지 문촌마을10단지아파트 A동 106-3호" + Keys.ENTER)
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
    hospital_exist = 0
    while(1):
        try:
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            hospital_name = soup.find_all(class_ = 'search_title')
            hospital_name = [hospital_n.get_text() for hospital_n in hospital_name]
            soup= 0
            name_exist = 0
            for i in hospital_name:
                if '동물병원' not in i:
                    continue
                i_r = i.replace(" ","")
                name_roop_r = name_roop.replace(" ","")

                # print(i_r)
                # print(name_roop_r)

                try:
                    c = i_r.replace("동물병원", "")
                except:
                    c = i_r
                try:
                    d = name_roop_r.replace("동물병원","")
                except:
                    d = name_roop_r
                
                ratio = SequenceMatcher(None, c, d).ratio()
                
                if ratio >= 0.5:
                    name_exist = 1
                    keyword = i 
                    hospital = driver.find_elements_by_xpath("//div[.='" + keyword + "']")
                    break

            for i in hospital:
                for j in range(2):
                    i = i.find_element_by_xpath('..')
                    # print("1")
                try:
                    i.click()
                    time.sleep(3)
                except:
                    pass
                    
            if name_exist == 1:   
                for i in range(3):
                    hospital = hospital.find_element_by_xpath('..')
                    # print(hospital)
                hospital.click()
                time.sleep(3)
                
                hospital_exist = 1
                break
        except:
            # print("case: this page doesn't contain hospital name")
            pass
        try:
            next_button = driver.find_element_by_class_name("btn_next")
            next_button.click()

            next_button = 0
            time.sleep(2)
        except:
            # print("alert: page finish")
            # print("error2: no hospital in the place")
            break
        try:
            next_button = driver.find_element_by_class_name("btn_next")
            enabled_false = next_button.is_enabled()
            if enabled_false == False:
                # print("error: no hospital in the place")
                break
        except:
            pass
    time.sleep(2)

    # 화면3(true)
    # 이용 시간 + 전화번호 추출
    # 리뷰 여부 확인
    # try
    # 방문자 리뷰 더보기 클릭
    # except
    # error code => pass

    time_exist = 1
    try:
        driver.switch_to.frame("entryIframe")
    except:
        # print("error3: iframe switch error")
        time_exist = 0
    try:
        
        time_not_exist = "이용시간을 알려주세요."
        time_n_exist = driver.find_element_by_xpath("//span[.='" + time_not_exist + "']")
        if time_n_exist != None:
            time_exist = 0
            # print(time_exist)
            # print("case: no operationg time")
        
    except:
        # print(time_exist)
        pass

    try:
        phone_number = driver.find_elements_by_class_name('dry01')[0].text 
        # print(phone_number)
    except:
        phone_number = -1
        # print("error4: phone number error")


    try:
        if time_exist == 1:
            driver.find_element_by_class_name('Sg7qM').click()
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            time_text = soup.find_all(class_ = "nNPOq")
            time_text = [tag.get_text() for tag in time_text]
            # print(time_text)
            #soup 초기화 해야 오류 안나는 듯
            soup = 0
            time.sleep(1)
        else:
            time_text = -1
    except:
        print("error: time_exist error")

    try:
        review_exist = driver.find_element_by_xpath("//span[.='" + "리뷰" + "']").find_element_by_xpath('..').click()
        time.sleep(2)
    except:
        # print("case: no review")
        pass





    # 화면4(true)
    # 리뷰추출 ~ 더보기 클릭(더보기 클릭 없을 때까지 반복)

    try:
        review_all = []
        review_grade = []
        while(1):
            try:
                driver.find_element_by_xpath("//a[.='" + "더보기" + "']").click()
                time.sleep(2)
            except:
                # print("case: no more review to expand")
                break
        expand_list = driver.find_elements_by_class_name('xHaT3')
        count = 0
        # print(expand_list)
        for e in expand_list[count:]:
            # print(e.text)
            e.send_keys(Keys.ENTER)
        count = len(expand_list)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        review_list = soup.find_all(class_ = "YeINN")
        for r in review_list:
            t = r.find(class_ = "ZZ4OK")
            # print(t)
            review_all.append(t.get_text())
            try:
                g = r.find(class_ = "sb8UA").find(class_ = "P1zUJ").find("em")
                # print(g)
                review_grade.append(g.get_text())
            except:
                # print("case: no grade")
                review_grade.append(-1)
        soup = 0

        # print(review_all)
        # print(review_grade)
    except:
        review_all = [-1]
        review_grade = [-1]
        # print("case: no review")

    one_roop_data = [name_roop, address_roop, phone_number, time_text, review_all, review_grade ]
    count_progress += 1
    hole_data.append(one_roop_data)
    if (count_progress % 10) == 0:
        print("========================")
        print(f"{count_progress*100/len(address):.1f}%" )
        print("========================")
    if (count_progress % 5) == 0:
        fields = ["Name", "Address", "Phone_num", "Operating_time","Review_txt","Review_grade"]
        df = pd.DataFrame(hole_data, columns= fields)
        df.to_pickle("df.pkl")
        print("df.pkl updated")


#csv에서 pickle로 변경: 3차원 데이터 타입이므로 형태까지 저장 필요 

fields = ["Name", "Address", "Phone_num", "Operating_time","Review_txt","Review_grade"]
df = pd.DataFrame(hole_data, columns= fields)
df.to_pickle("./naver_review_crawling/ml_data/df.pkl")

#끝!

#네이버 리뷰 특징: 별점 낮은 순 보기 기능 x / 안 좋은 리뷰에는 의사 답글이 달려있음 (이런 리뷰들과 답글이 중요 데이터 인듯 향후 의사 답변 데이터 수집도 필요할듯)
#그리고 네이버리뷰는 최근에 별점 기능을 제거함

