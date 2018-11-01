from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("file:///C:/nds-standard-2.5.1-html-docu/content/nds.common.flexattr.valuecodes/AttributeTypeCode_ENUM.html")

bsObject = BeautifulSoup(html, "html.parser")

itemobj = bsObject.find("dl").find_all("dt", {"class":"memberItem"})
tdobj = (bsObject.find("dl").find_all("td"))
attlist = []

for attribitem in itemobj:
    attribstr = str(attribitem.string)
    attlist.append(attribstr)

#
i = 0
initlist = 1
worth = 0
primary = 0

for annoitem in tdobj:
    annotstr = str(annoitem.string)

    if "Category.ROUTING" in annotstr:
        worth = 1
    if "Category.GUIDANCE" in annotstr:
        worth = 1
    if "GroupRole.PRIMARY" in annotstr:
        primary = 1
    elif "GroupRole.SECONDARY" in annotstr:
        primary = 2
    if "ReferenceType.ROUTING" in annotstr:
        worth = 1

    if worth == 1 and primary == 1:
        if "Category" in annotstr:
            if initlist == 1 :
                print("-----------------------------------------------")
                print(attlist[i])
                i = i + 1
                initlist = 0
            print(annotstr)
        if "GroupRole" in annotstr:
            initlist = 1
            print(annotstr)
        if "ReferenceType" in annotstr:
            print(annotstr)





