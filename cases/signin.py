import  unittest
import  ddt
import  requests

@ddt.ddt
class Signin(unittest.TestCase):
    @ddt.file_data(r'/Users/aina/PycharmProjects/unt/data/signin.yaml')
    @ddt.unpack
    def test_data(self,**test_data):
        url = test_data.get('url')
        method =test_data.get('method')
        detail =test_data.get('detail','用例描述')
        self._testMethod = detail #获取用例描述
        data =test_data.get('data',{})
        headers =test_data.get('headers',{})
        cookies =test_data.get('cookies',{})
        is_json =test_data.get('is_json',0)
        check =test_data.get('check',{})

        if method == 'post':
            if is_json:
                res = requests.post(url, json=data, headers=header,cookies=cookies)

            else:
                res = requests.post(url, data=data, headers=headers,cookies=cookies)
        elif method == 'get' :
            res = requests.get(url, params=data, headers=headers,cookies=cookies)


        for c in check:
            result =res.json()

            self.assertEqual(c,result["code"],msg='验证code是否正确')