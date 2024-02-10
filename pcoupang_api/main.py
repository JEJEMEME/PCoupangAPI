import hmac
import hashlib
import requests
from time import gmtime, strftime

class PCoupangAPI:
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        self.domain = "https://api-gateway.coupang.com"
        self.urls = {
            "goldbox": "/v2/providers/affiliate_open_api/apis/openapi/v1/products/goldbox",
            "deeplink": "/v2/providers/affiliate_open_api/apis/openapi/v1/deeplink",
            "bestcategories": "/v2/providers/affiliate_open_api/apis/openapi/products/bestcategories/{category_id}",
            "coupangPL": "/v2/providers/affiliate_open_api/apis/openapi/products/coupangPL",
            "search": "/v2/providers/affiliate_open_api/apis/openapi/products/search",
            "reco": "/v2/providers/affiliate_open_api/apis/openapi/products/reco",
            "coupangPLBrand": "/v2/providers/affiliate_open_api/apis/openapi/products/coupangPL/{brandId}"
        }

    def generate_hmac(self, method, url):
        path, *query = url.split("?")
        datetime_gmt = strftime('%y%m%d', gmtime()) + 'T' + strftime('%H%M%S', gmtime()) + 'Z'
        message = datetime_gmt + method + path + (query[0] if query else "")

        signature = hmac.new(bytes(self.secret_key, "utf-8"),
                             message.encode("utf-8"),
                             hashlib.sha256).hexdigest()

        return f"CEA algorithm=HmacSHA256, access-key={self.access_key}, signed-date={datetime_gmt}, signature={signature}"

    def request(self, method, url_key_or_url, params=None, data=None, path_params=None):
        if url_key_or_url in self.urls:
            base_url = self.urls[url_key_or_url]
            if path_params:
                base_url = base_url.format(**path_params)
        else:
            base_url = url_key_or_url  # 직접 제공된 URL 사용
        
        query_string = '&'.join([f"{key}={value}" for key, value in (params or {}).items()])
        full_url = f"{self.domain}{base_url}?{query_string}" if query_string else f"{self.domain}{base_url}"
        
        authorization = self.generate_hmac(method, full_url.replace(self.domain, ''))
        headers = {"Authorization": authorization, "Content-Type": "application/json"}

        if method.upper() == "GET":
            response = requests.get(full_url, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(full_url, headers=headers, json=data)
        elif method.upper() == "PUT":
            response = requests.put(full_url, headers=headers, json=data)
        elif method.upper() == "DELETE":
            response = requests.delete(full_url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        return response.json()

    def get_goldbox_offers(self, params):
        return self.request("GET", "goldbox", params=params)

    def create_deeplink(self, coupang_urls, sub_id=None):
        data = {"coupangUrls": coupang_urls}
        if sub_id:
            data["subId"] = sub_id
        return self.request("POST", "deeplink", data=data)

    def get_best_category_products(self, category_id, limit=20, sub_id=None, image_size=None):
        params = {
            "limit": limit
        }
        if sub_id:
            params["subId"] = sub_id
        if image_size:
            params["imageSize"] = image_size

        path_params = {"category_id": category_id}
        
        return self.request("GET", "bestcategories", params=params, path_params=path_params)

    def get_recommended_products(self, deviceId, sub_id=None, image_size=None):
        params = {
            "deviceId": deviceId,
            "subId": sub_id if sub_id else "",
            "imageSize": image_size if image_size else ""
        }
        return self.request("GET", "reco", params=params)

    def search_products(self, keyword, limit=10, sub_id=None, image_size=None, srpLinkOnly=False):
        params = {
            "keyword": keyword,
            "limit": limit,
            "subId": sub_id if sub_id else "",
            "imageSize": image_size if image_size else "",
            "srpLinkOnly": srpLinkOnly
        }
        return self.request("GET", "search", params=params)

    def get_coupang_pl_products(self, limit=20, sub_id=None, image_size=None):
        params = {
            "limit": limit,
            "subId": sub_id if sub_id else "",
            "imageSize": image_size if image_size else ""
        }
        return self.request("GET", "coupangPL", params=params)
    
    def get_coupang_pl_brand_products(self, brand_id, limit=20, sub_id=None, image_size=None):
        params = {
            "limit": limit,
            "subId": sub_id if sub_id else "",
            "imageSize": image_size if image_size else ""
        }
        path_params = {"brandId": brand_id}
        return self.request("GET", "coupangPLBrand", params=params, path_params=path_params)