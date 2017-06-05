#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: xyj
@license: MIT License
@contact: xieyingjun@vip.qq.com
@Created on 2017/5/25

微信发送信息测试用例

"""
import requests
import time
from src.weixin_secret import appid, secret  # 导入自己保存的appid和secret

def get_access_token(appid, secret):
    """ 获取access_token

    接口调用请求说明
    https请求方式: GET
    https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET

    :param appid:第三方用户唯一凭证
    :param secret:第三方用户唯一凭证密钥，即appsecret
    """
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(appid,
                                                                                                           secret)
    result = requests.get(url).json()
    print(result)
    return result['access_token']


def get_all_private_template(ACCESS_TOKEN):
    """ 获取获取模板列表

        接口调用请求说明
        http请求方式: POST
        https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=ACCESS_TOKEN

        :param ACCESS_TOKEN:获取到的凭证
    """
    url = "https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=" + ACCESS_TOKEN
    print(url)
    result = requests.get(url).json()
    print(result)


def send_template(ACCESS_TOKEN, touser, template_id, data=None):
    """ 发送模板消息

        接口调用请求说明
        http请求方式: POST
        https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=ACCESS_TOKEN

        :param ACCESS_TOKEN:获取到的凭证
        :param touser:接收者openid
        :param template_id:模板ID
        :param data:模板数据

    """
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + ACCESS_TOKEN
    d = {"touser": touser, "template_id": template_id, "data": data}
    print(data)
    result = requests.post(url, json=d)
    print(result.text)


def get_meun(ACCESS_TOKEN):
    """ 自定义菜单查询接口

        接口调用请求说明
        http请求方式：GET
        https://api.weixin.qq.com/cgi-bin/menu/get?access_token=ACCESS_TOKEN

        :param ACCESS_TOKEN:获取到的凭证
    """
    url = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=" + ACCESS_TOKEN
    result = requests.get(url).json()
    print(result.text)


def del_meun(ACCESS_TOKEN):
    """ 自定义菜单删除接口

        接口调用请求说明
        http请求方式：GET
        https://api.weixin.qq.com/cgi-bin/menu/get?access_token=ACCESS_TOKEN

        :param ACCESS_TOKEN:获取到的凭证
    """
    url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=" + ACCESS_TOKEN
    result = requests.get(url).json()
    print(result)


def create_meun(ACCESS_TOKEN):
    """ 自定义菜单创建接口

        接口调用请求说明
        http请求方式：POST
        https://api.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN

        :param ACCESS_TOKEN:获取到的凭证

    """
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + ACCESS_TOKEN



if __name__ == '__main__':
    appid = appid
    secret = secret
    access_token = get_access_token(appid, secret)  # 获取access_token
    # get_all_private_template(access_token)  # 获取获取模板列表

    # send_template(access_token, 'ogx99jtzGPY0QSgGzeqe_RoPjHew', 'M9AsgY7lklW3WJhBGGR_oIVhmhib-IVpkhoKimKI0jI',
    #               {'card': {"value": '123456789'},
    #                'jtime': {"value": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))},
    #                'line': {"value": '139线'},
    #                'bus_id':{"value": '1013924'},
    #                'tf': {"value": "2.00元", "color": "#173177"}})  # 发送模板消息

    get_meun(access_token)
    del_meun(access_token)
