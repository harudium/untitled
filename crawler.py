from urllib.request import urlopen

import bs4
# import csv
from collections import defaultdict

d = defaultdict(dict)

html = urlopen("file:///Users/kyongjin/Downloads/nds-standard-2.5.4-rc2-html-docu/content/nds.common.flexattr.valuecodes/AttributeTypeCode_ENUM.html")

bsObject = bs4.BeautifulSoup(html, "html.parser")

itemobj = bsObject.find("dl").find_all("dt", {"class":"memberItem"})
tdobj = (bsObject.find("dl").find_all("td"))

attlist = []
alist= []
clist = []
glist = []
rlist = []

i = 0
initlist = 1
# popped = 0

def sumitems(itemlist):
    klist = []
    popped = 0

    for citem in itemlist:
        if citem == "|":
            popped = popped + 1
            break
        klist.append(citem)
        popped = popped + 1
    for tmp in range(0, popped):
        itemlist.pop(0)
    return klist

def poplist(itemlist):
    global popped

    popped = 0

# extracts only for attribute codes
for attribitem in itemobj:
    attribstr = str(attribitem.string)
    attribstr = attribstr.replace(":", "")
    attlist.append(attribstr)

# extracts annotations such as category, group role, features
# group role is only a single value per an attribute code, but
# categories and features could be assigned more than a single
# value per an attribute code. tricky.

for annoitem in tdobj:
    annotstr = str(annoitem.string)

    if "Category" in annotstr:
        if initlist == 1 :
            # print("#")
            # print(attlist[i])
            if i != 0 :
                rlist.append("|")
            i = i + 1
            initlist = 0
        # print(annotstr)
        clist.append(annotstr)
    if "GroupRole" in annotstr:
        initlist = 1
        clist.append("|")
        annotstr = annotstr.replace("GroupRole.", "")
        glist.append(annotstr)
        # print(annotstr)
    if "ReferenceType" in annotstr:
        # print(annotstr)
        rlist.append(annotstr)
    if "AnnotationIndicatedFeature" in annotstr:
        # print(annotstr)
        rlist.append(annotstr)

# put extracted items into data structure for further search process
i = 0
for aitem in attlist:
    d[aitem][glist[i]] = sumitems(clist) + sumitems(rlist)
    i = i + 1
    # poplist(clist)

foo = []
for k in d:
    if "PRIMARY" in d[k]:
        foo = d[k].get("PRIMARY")
        for c in foo:
            if "ROUTING" in c:
                print(k, '\n', foo)
                break;
#print(d["SPEED_LIMIT"])
# with open('./some.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.

