# PCoupangAPI Python 패키지

PCoupangAPI 패키지는 쿠팡 Affiliate API와 상호작용하기 위한 Python 인터페이스입니다. 
골드박스 오퍼 검색, 딥링크 생성, 베스트 카테고리 제품 조회 등 다양한 엔드포인트로의 HTTP 요청을 간소화합니다.
래핑된 API외에도 request를 통해 full url을 제공하면 해당 url을 기반으로 요청을 처리할 수 있습니다

## 특징

- 골드박스 오퍼 검색
- 쿠팡 제품을 위한 딥링크 생성
- 카테고리별 베스트셀러 제품 조회
- 추천 제품 가져오기
- 키워드로 제품 검색
- 쿠팡 PL(Private Label) 제품 및 브랜드 접근

## 설치

pip를 사용하여 PCoupangAPI 패키지를 쉽게 설치할 수 있습니다:

```
pip install PCoupangAPI
```

## 시작하기

PCoupangAPI 패키지를 사용하려면 유효한 쿠팡 Access Key와 Secret Key가 필요합니다. 시작하는 방법은 다음과 같습니다:

```python
from PCoupangAPI import PCoupangAPI

# 쿠팡 Access Key와 Secret Key로 초기화
api = PCoupangAPI(access_key='YOUR_ACCESS_KEY', secret_key='YOUR_SECRET_KEY')

# 예시: 골드박스 오퍼 가져오기
goldbox_offers = api.get_goldbox_offers(params={"limit": 10})
print(goldbox_offers)
```

## 문서

### 초기화

```python
api = PCoupangAPI(access_key, secret_key)
```

- `access_key`: 쿠팡 API 액세스 키.
- `secret_key`: 쿠팡 API 시크릿 키.

### 메소드

- `get_goldbox_offers(params)`: 골드박스 오퍼를 검색합니다.
- `create_deeplink(coupang_urls, sub_id=None)`: 쿠팡 제품에 대한 딥링크를 생성합니다.
- `get_best_category_products(category_id, limit=20, sub_id=None, image_size=None)`: 카테고리별 베스트셀러 제품을 조회합니다.
- `get_recommended_products(deviceId, sub_id=None, image_size=None)`: 추천 제품을 가져옵니다.
- `search_products(keyword, limit=10, sub_id=None, image_size=None, srpLinkOnly=False)`: 키워드로 제품을 검색합니다.
- `get_coupang_pl_products(limit=20, sub_id=None, image_size=None)`: 쿠팡 PL 제품에 접근합니다.
- `get_coupang_pl_brand_products(brand_id, limit=20, sub_id=None, image_size=None)`: 특정 쿠팡 PL 브랜드의 제품을 조회합니다.

### 인증

패키지는 제공된 Access Key와 Secret Key를 사용하여 HMAC-SHA256으로 각 요청을 자동으로 인증합니다.

## 기여

기여를 환영합니다! 제안이 있거나 버그를 발견하셨다면 풀 리퀘스트를 보내거나 이슈를 생성해 주세요.

## 라이센스

이 프로젝트는 MIT 라이센스에 따라 라이센스가 부여됩니다.
