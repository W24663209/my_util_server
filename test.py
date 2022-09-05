import json

if __name__ == '__main__':
    with open('static/1.txt', 'r') as f:
        columns = {}
        for text in f:
            if not text.__eq__('\n'):
                classes = text.split('\t')
                columns[classes[0]] = (classes[0], classes[3].split('.')[-1], classes[3])
        with open('template/column.json', 'w') as a:
            a.write(json.dumps(columns))