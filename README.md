# anireview_blog_pr
애니리뷰_블로그_프로젝트

## naver_data crawling

### 완료 작업 <br/>
1. 경기도 동물병원 리스트 엑셀 > pd > roop( 네이버 지도 검색 > 병원 이름 / 전화번호 / 운영 시간 / 리뷰 / 별점 추출).append > list > pd > pickle<br/>
2. pickle data에서 review만 뽑아내서 flatten 시킨후 엑셀 파일로 변환 ml_raw_data 생성<br/>
### To Do<br/>
1. 한 건물에 동물병원 두개일 경우에 대한 알고리즘 수정 필요 (clear)<br/>
2. 동물병원 이름 일치율 알고리즘으로 검색 (문자열 일치도 0.5 이상이면 맞다고 처리) (clear)<br/>
3. 속도개선 필요 (clear)<br/>

### Recognized Error<br/>
non

## Review_data_classification ML

### 완료작업 <br/>
1. 수집한 네이버 리뷰 데이터를 라벨링하여 문장을 tokenized 및 전처리
2. BERT 모델을 이용하여 라벨링(0: 부정 / 1: 긍정) 학습(테스트셋 정확도: 0.98)
3. 학습된 모델 파라미터를 pt파일로 저장

### To Do <br/>
1. 단어 자체로 긍정 부정 판별은 잘하지만 '안' '아니'와 같은 부정형이 단어앞에 올 경우를 인식 잘 못함.

### Recognized Error <br/>
non
