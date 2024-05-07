sns = open('1.txt').read().split('\n')
sns2 = {}
sns3 = {}
for text in open('2.txt').read().split('\n'):
    orderNo, sn = text.split('\t')
    sns2[sn] = orderNo
# if sns.__contains__(sn):
# with open('5.txt', 'a') as f:
#     if sns3.keys().__contains__(sn):
#         sns3[sn]=sns3[sn]+1
#     else:
#         sns3[sn] = 0
# f.write('%s\t%s\n' % (orderNo, sn))
#
for sn in sns:
    if sns3.keys().__contains__(sn):
        sns3[sn] = sns3[sn] + 1
    else:
        sns3[sn] = 1
for sn in sns3.keys():
    if sns3[sn]>1:
        print(sn)
print(set(sns).__len__())
print(set(sns2).__len__())
for sn in set(sns) - set(sns2):
    print(sn)
