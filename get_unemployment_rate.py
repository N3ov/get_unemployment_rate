import requests
from bs4 import BeautifulSoup
import sys

def main():
    start = sys.argv[1]
    end = sys.argv[2]
    print('起始民國與月份: %s' % (start))
    print('結束民國與月份: %s' % (end))

    # url = 'https://statdb.mol.gov.tw/statis/jspProxy.aspx?sys=220&ym=6701&ymt=10802&funid=q02072'
    url = 'https://statdb.mol.gov.tw/statis/jspProxy.aspx?sys=220&ym={0}&ymt={1}&funid=q02072'.format(start,end)
    # urls = ['https://www.stat.gov.tw/lp.asp?CtNode=519&CtUnit=1818&BaseDSD=29&nowPage={}' .format(str(i)) for i in range(1,9)]
    response = requests.get(url)
    doc = BeautifulSoup(response.text, 'html.parser')
    # print(url)
    # print(doc)
    pod = doc.select('tr>td.stymon.stydata')
    # print(len(pod))

    rate = []
    count = 0
    for result in pod:
        # print(result.get_text())
        rate.append(result.get_text())
        count += 1
    print(rate)
    print('總計月份數: ',count)
        # unemp = result.select_one('td[class="stymon stydata"]')
        # print(unemp)
        # match = re.compile(r'(\d+(\.\d+)?)', unemp)


        # print(match)





if __name__ == "__main__" :
    main()


