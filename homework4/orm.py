import pymysql


class Field:
    def __init__(self, type_, required=False, default=None):
        self.type_ = type_
        self.required = required
        self.default = default

    def validate(self, value):
        if value is None:
            if not self.required:
                return None
            else:
                raise ValueError('НЕ определено обязательное поле')
        return self.type_(value)


class IntegerField(Field):
    def __init__(self, required=False, default=None):
        super().__init__(int, required, default)


class CharField(Field):
    def __init__(self, required=False, default=None):
        super().__init__(str, required, default)


class BooleanField(Field):
    def __init__(self, required=False, default=None):
        super().__init__(bool, required, default)


class ModelMeta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'Model':
            return super().__new__(mcs, name, bases, namespace)

        meta = namespace.get('Meta')
        if meta is None:
            raise ValueError('meta is none')
        if not hasattr(meta, 'table_name'):
            raise ValueError('table_name is empty')

        fields = {k: v for k, v in namespace.items()
                  if isinstance(v, Field)}

        # mro = super().__new__(mcs, name, bases, namespace).mro()
        # for cls in mro:
        #     for k, v in cls.__dict__.items():
        #         if isinstance(v, Field) and k not in fields:
        #             fields[k] = v

        namespace['_fields'] = fields
        namespace['_table_name'] = meta.table_name
        return super().__new__(mcs, name, bases, namespace)


class Manager:

    def __get__(self, instance, owner):
        self.model_cls = owner
        return self

    @staticmethod
    def execute_query(query):
        connection = pymysql.connect(host='127.0.0.1', port=3306,
                                     user='root', password='pass',
                                     db='deeppython', charset='utf8')
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        res = cursor.fetchall()
        return res

    def create(self, **kwargs):
        table_name = self.model_cls.Meta.table_name

        cols = ', '.join(kwargs.keys())
        values = ', '.join(list(map(lambda x: '\'' + str(x) + '\'', kwargs.values())))
        query = f"INSERT INTO {table_name} ({cols}) values ({values})"
        self.execute_query(query)

    def all(self):
        table_name = self.model_cls.Meta.table_name
        query = f"SELECT * FROM {table_name}"
        return self.execute_query(query)

    def get(self, id):
        table_name = self.model_cls.Meta.table_name
        query = f"SELECT * FROM {table_name} where id={id}"
        return self.execute_query(query)

    def update(self, **kwargs):  # на всех ???
        table_name = self.model_cls.Meta.table_name
        fields = ', '.join([f'{k}=\'{v}\'' for k, v in kwargs.items()])
        query = f"UPDATE {table_name} set {fields}"
        self.execute_query(query)

    def delete(self, id=None):
        table_name = self.model_cls.Meta.table_name
        if id is not None:
            query = f"DELETE FROM {table_name} where id={id}"
        else:
            query = f"DELETE FROM {table_name}"
        self.execute_query(query)

    def save(self):
        pass


class Model(metaclass=ModelMeta):
    class Meta:
        table_name = ''

    def __init__(self, *_, **kwargs):
        for field_name, field in self._fields.items():
            value = field.validate(kwargs.get(field_name))
            setattr(self, field_name, value)

    objects = Manager()

class Human(Model):
    id = IntegerField()
    name = CharField(required=True)
    surname = CharField()

    class Meta:
        table_name = 'human'


# Human.objects.create(name='Gennady', surname='Kandaurov')
