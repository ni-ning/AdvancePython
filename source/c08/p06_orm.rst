===============================
8.6 通过元素实现ORM
===============================

首先明确需求

.. code-block:: py

    # 简单定义
    class User:
        name = CharFiled(db_column="", max_length=32)
        age = IntFiled(db_column="", min_value=0, max_value=100)
        class Meta:
            db_table = 'user'

    # ORM
    user = User()
    user.name = 'linda'
    user.age = 18
    user.save()


迷你版 ORM

.. code-block:: py

    from collections import OrderedDict


    class Field:
        pass


    class IntField(Field):
        def __init__(self, db_column, min_value=0, max_value=100):
            self.db_column = db_column
            self.min_value = min_value
            self.max_value = max_value
            self._value = None

        def __get__(self, instance, owner):
            return self._value

        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise TypeError('need int value')
            if value < self.min_value or value > self.max_value:
                raise ValueError('need [%s, %s] value' % (self.min_value, self.max_value))
            self._value = value


    class CharField(Field):
        def __init__(self, db_column, max_length=32):
            self.db_column = db_column
            self.max_length = max_length
            self._value = None

        def __get__(self, instance, owner):
            return self._value

        def __set__(self, instance, value):
            if not isinstance(value, str):
                raise TypeError('need str value')
            if len(value) > self.max_length:
                raise ValueError('len need lower than %s' % self.max_length)
            self._value = value


    # 元类注入一系列属性
    class MetaClass(type):
        def __new__(cls, name, bases, attrs, **kw):
            # BaseModel 也会调用 Metaclass，但没有定义 name，age 等属性，可特殊判断
            if name == 'BaseModel':
                return super().__new__(cls, name, bases, attrs, **kw)

            fields = {}
            for key, value in attrs.items():
                if isinstance(value, Field):
                    fields[key] = value

            attrs_meta = attrs.get('Meta', None)
            _meta = {}
            db_table = name.lower()
            if attrs_meta is not None:
                table = getattr(attrs_meta, 'db_table', None)
                if not table:
                    db_table = table

            _meta['db_table'] = db_table
            attrs['_meta'] = _meta
            attrs['fields'] = fields
            if attrs.get('Meta'):
                del attrs['Meta']
            return super().__new__(cls, name, bases, attrs, **kw)


    class BaseModel(metaclass=MetaClass):
        def __init__(self, **kw):
            for key, value in kw.items():
                setattr(self, key, value)
            super().__init__()

        def save(self):
            fields = OrderedDict(self.fields)
            fields_str = ", ".join([value.db_column for value in fields.values()])
            values_str = ', '.join([str(getattr(self, field)) if not isinstance(value, CharField)
                                    else "'%s'" % str(getattr(self, field))
                                    for field, value in fields.items()])
            sql = "insert into %s (%s) values (%s)" % (self._meta['db_table'], fields_str, values_str)
            print(sql)
            # insert into user (name1, age) values ('linda', 20)


    # 自定义类时写少量属性，元类帮助我们注入很多通用属性
    class User(BaseModel):
        name = CharField('name1', max_length=16)
        age = IntField('age', min_value=0, max_value=100)

        class Meta:
            db_table = 'user'


    if __name__ == '__main__':
        user = User(name='linda')
        user.age = 20
        user.save()
