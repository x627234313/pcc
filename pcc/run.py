#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sanic import Sanic
from sanic import response

import view


func_dict = {
    'list': view.list,
    'like': view.like,
    'count': view.count,
    'is_like': view.is_like
}


app = Sanic()


@app.route("/pcc", methods=['GET'])
async def test(request):
    try:
        action = request.args['action']
        uid = request.args['action']
    except KeyError:
        result = {
            "error_code": "101",
            "error_message": "未能提供正确的参数, 请检查参数后重新发起请求"
        }
        return response.json(result)
    oid = request.args.get('action', None)
    action = func_dict['action']
    result = action(uid, oid)
    return response.json(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
