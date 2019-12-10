===============================
6.2 dict的常用方法
===============================

借助编辑器，如 PyCharm 实时查看源码

.. code-block:: py

    d = {
        'linda': {'company': 'Yahoo'},
        'catherine': {'company': 'Google'}
    }

    # 清空
    # d.clear()

    # 浅拷贝
    new_dict = d.copy()
    # 深拷贝
    import copy
    new_dict_deep = copy.deepcopy(d)

    new_dict['linda']['company'] = 'Ali'
    print(d)
    print(new_dict)
    print(new_dict_deep)

    dd = dict.fromkeys(['key1', 'key2'], 'default')
    dd.get('key', None)
    dd.keys(), dd.values(), dd.items()

    # 获取key的value, 没有时更新为默认值
    print(dd.setdefault('key', 'value'))
    dd.update({'name': 'linda'})
    print(dd)
