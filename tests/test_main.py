import unittest
from pcoupang_api.main import PCoupangAPI

class TestCoupangAPI(unittest.TestCase):
    def setUp(self):
        self.api = PCoupangAPI("publc key", "secret key")

    def test_get_goldbox_offers(self):
        response = self.api.get_goldbox_offers({'limit': 10})
        self.check_response(response)

    def test_create_deeplink(self):
        response = self.api.create_deeplink(["http://example.com"])
        self.check_response(response)

    def test_get_best_category_products(self):
        response = self.api.get_best_category_products('123', 20)
        self.check_response(response)

    def test_get_recommended_products(self):
        response = self.api.get_recommended_products('device1')
        self.check_response(response)

    def test_search_products(self):
        response = self.api.search_products('keyword')
        self.check_response(response)

    def test_get_coupang_pl_products(self):
        response = self.api.get_coupang_pl_products(20)
        self.check_response(response)

    def test_get_coupang_pl_brand_products(self):
        response = self.api.get_coupang_pl_brand_products('brand1', 20)
        self.check_response(response)

    def check_response(self, response):
        # 'code' 필드가 있고 그 값이 'ERROR'인지 확인
        if "code" in response:
            self.assertNotEqual(response["code"], "ERROR", "API call failed with 'ERROR' code.")
        else:
            # 'code' 필드가 없으면 테스트는 성공으로 간주
            self.assertTrue(True)

# 테스트 실행
if __name__ == '__main__':
    unittest.main()
