#1차 목표 
# 셀레니움을 이용하여 네이버 리뷰 수집


import sys    
import os     

import pandas as pd    
import numpy as np     

from bs4 import BeautifulSoup     
from selenium import webdriver    
from selenium.webdriver.common.keys import Keys

import time                      
import math

#path는 각자 컴퓨터에 맞게 변경 필요
path = "E:\python\data_collect\data_ml_pr\chromedriver.exe"

driver = webdriver.Chrome(path)

# 한사이클 순서

# 화면1
# 네이버 지도 검색창
# 경기도 동물병원현황 엑셀 소재지 지번주소 검색
# 이주소의 장소 더보기 클릭

# 화면2
# 동물병원 텍스트 찾기
# true => 링크 클릭
# false => pass

# 화면3(true)
# 이용 시간 + 전화번호 추출
# 리뷰 여부 확인
# true
# 방문자 리뷰 더보기 클릭
# false
# pass

# 화면4(true)
# 리뷰추출 ~ 더보기 클릭(더보기 클릭 없을 때까지 반복)






