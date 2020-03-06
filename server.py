# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 17:33

from app.webapp import application

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)
