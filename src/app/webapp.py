# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 15:47

from app import create_app

application = create_app()

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)
