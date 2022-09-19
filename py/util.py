"""
@Description: TODO

@Author: weizongtang

@Create: 2020-07-30 23:57
"""
import datetime
import decimal
import re
import time

from flask import json
import sys

path = sys.path[0]


class Util():

    def mybatis_log_to_sql(self, value):
        """
        mybatis日志转sql
        :param arr:
        :return:
        """
        preparing = None
        parameters = None
        for text in value.split('\n'):
            text = text.split('==>')[-1]
            preparing = text if text.__contains__('Preparing') else preparing
            parameters = text if text.__contains__('Parameters') else parameters

        preparing = preparing.replace('Preparing:', '').replace('%', '%%').replace('?', '%s')
        value_arr = []
        for value in parameters.replace('Parameters:', '').split(','):
            tmp_value = re.findall('(.*?)\(.*?\)', value)
            value_ = tmp_value[0] if tmp_value.__len__() > 0 else value
            value_ = value_.replace(' ', '')
            if value.__contains__('String'):
                value_ = "\'%s\'" % value_
            elif value.__contains__('Timestamp'):
                value_ = "date_format(\'%s\',\'%%Y-%%m-%%d %%H:%%i:%%s\')" % value_
            value_arr.append(value_)

        return preparing % tuple(value_arr)

    def get_layui_width(self, value):
        """
        layui获取宽度
        :param value:
        :return:
        """
        sum = 25
        for text in value.split('\n'):
            widths = re.findall("width: \'(.*?)\'", text)
            if len(widths) > 0 and not text.__contains__('hide'):
                sum += int(widths[0])
        return self.return_data(sum)

    def get_search_layui_value(self, value):
        """
        获取layui搜索id
        :param value:
        :return:
        """
        arrs = []
        template = '%s: $("#%s").val(),'
        for dom in value.split('\n'):
            vaules = re.findall('id=\"(.*?)\"', dom)
            if vaules and len(vaules) > 0:
                arrs.append(template % (vaules[0], vaules[0]))
        return '\n'.join(arrs)

    def auto_fields_json(self, value):
        """
        json生成对象
        :param value:
        :return:
        """
        loads = json.loads(value) if type(json.loads(value)) == dict else json.loads(value)[0]
        keys = loads.keys()
        arr = []
        for key in keys:
            text = ''
            if type(loads[key]) is dict:
                key__keys = loads[key].keys()
                text += ('private Res%s %s;' % (key[0].upper() + key[1:], key))
                text += ('@Data\npublic class Res%s{' % (key[0].upper() + key[1:]))
                for key__key in key__keys:
                    clo_name = self.auto_to_upper(key__key)
                    text += ('\tprivate String %s;' % clo_name)
                text += ('}')
            else:
                field_type = 'String'
                if isinstance(loads[key], int):
                    field_type = 'Integer'
                elif isinstance(loads[key], float):
                    field_type = 'BigDecimal'
                text += ('private %s %s;' % (field_type, key))
            arr.append(text)
        return '\n'.join(arr)

    def document_to_class(self, data):
        """
        文档转class或map
        :param data:
        :return:
        """
        values = data['value'].split('\n')
        className = data['className']
        columnName = int(data['columnName'])
        classType = data['classType']
        document_util = self.document_util()
        if not classType or classType.__eq__('class'):
            className = className[0].upper() + className[1:]
            remark = data['remark']
            return document_util.document_to_class_defalut(className, columnName, remark, values)
        elif not classType or classType.__eq__('req'):
            className = className[0].upper() + className[1:]
            return document_util.document_to_class_req(className, columnName, values)
        else:
            return document_util.document_to_class_map(columnName, values)

    class document_util:
        def document_to_class_req(self, className, columnName, values):
            """
            生成req赋值
            :param columnName:
            :param values:
            :return:
            """
            className += 'Req'
            template = '%s req = new %s();\n' % (className, className)
            for value in values:
                cls = value.split('\t')
                columnName_ = cls[columnName]
                get_columnName_ = columnName_[0].upper() + columnName_[1:]
                template += 'req.set%s("");\n' % self.auto_to_upper(get_columnName_)
            return template

        def document_to_class_map(self, columnName, values):
            """
            文档转map
            :param className:
            :param columnName:
            :param remark:
            :param values:
            :return:
            """
            template = 'ConcurrentHashMap<String,String> map = new ConcurrentHashMap<>();\n'
            for value in values:
                cls = value.split('\t')
                columnName_ = cls[columnName]
                get_columnName_ = columnName_[0].upper() + columnName_[1:]
                template += '%s\n' % 'map.put("%s",%s());' % (columnName_, 'req.get%s' % get_columnName_)
            return template

        def document_to_class_defalut(self, className, columnName, remark, values):
            """
            文档转class
            :param className:
            :param columnName:
            :param remark:
            :param values:
            :return:
            """
            template = self.read_template('template/doc_to_entiry.java')
            template = template.replace('${className}', className)
            template = template.replace('${time}', self.get_time())
            columnName_template = re.findall('<columnName>([\s\S]*?)</columnName>', template)[0]
            columnName_str = []
            for value in values:
                cls = value.split('\t')
                columnName_ = self.auto_to_upper(cls[columnName])
                if remark.__contains__(':'):
                    remark_ = ','.join(cls[int(remark.replace(':', '')):])
                else:
                    remark_ = ','.join(cls[int(remark):])
                columnName_str.append(
                    columnName_template.replace('${remark}', remark_).replace('${columnName}', columnName_))
            return template.replace(columnName_template, '\n'.join(columnName_str)).replace('<columnName>', '').replace(
                '</columnName>', '')

    def read_template(self, filename):
        """
        读取模板
        :param filename:
        :return:
        """
        with open('%s/%s' % (path, filename), 'r') as f:
            return f.read()

    def return_data(self, data):
        """
        返回数据
        :param data:
        :return:
        """
        return json.dumps(data).replace('"', '')

    def get_time(self, rule="%Y-%m-%d %H:%M:%S"):
        """
        获取当前时间
        :param rule:
        :return:
        """
        return time.strftime(rule, time.localtime())

    def auto_to_upper(selt, value):
        """
        字段自动转大写
        :param value:
        :return:
        """
        values = value.split('_')
        restr = ''
        for i, val in enumerate(values):
            if i > 0:
                restr += val.capitalize()
            else:
                restr += val
        return restr

    def base64_decode(self, value):
        print(value)


if __name__ == '__main__':
    a = '{"cvv":"582","signature":"8702A2EB2E0C4D8857D4E63A97ACED04","traceno":"1290898903641751552","validDate":"0823","mobile":"15086183703","cardType":"2","cardno":"6225768673480347","trueName":"%CE%A4%D7%DA%CC%C3","certno":"522726199704252318","settleAccountno":"6217007200070360253","merchno":"886130242250001","settleMobile":"15086183703","interType":"2"}'
    print(a.encode('GB2312').decode('GB2312'))
