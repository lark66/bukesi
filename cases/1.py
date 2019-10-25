import ddt
import unittest, requests
from BeautifulReport import BeautifulReport


@ddt.ddt
class MyCase_login(unittest.TestCase):

    @ddt.file_data('ceshi.yaml')
    @ddt.unpack
    def test_run(self, **kwargs):
        method = kwargs.get('method')
        detail =kwargs.get('detail','用户密码进行登录')
        self._testMethodName =detail
        url = "http://192.168.0.185:7700/auth/signin_form"
        data = kwargs.get('data')
        header = kwargs.get('header', {})
        is_json = kwargs.get('is_json', 0)
        cookie = kwargs.get('cookie', {})
        check = kwargs.get('check',{})
        if method == 'POST':
            if is_json:
                res = requests.post(url, json=data, headers=header,
                                  cookies=cookie).text

            else:
                res = requests.post(url, data=data, headers=header,
                                  cookies=cookie).text
        elif method =="GET" :
            res = requests.get(url, params=data, headers=header,
                             cookies=cookie).text


        for c in check:
            self.assertIn(c,res)
            self.assertEqual(c,str(res.status_code))
