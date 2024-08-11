def find_final(desired_course, scrapy=None):

    import requests

    url = 'https://registrar.yale.edu/general-information/final-exams'
    html = requests.get(url).content

    from scrapy import Selector

    num = 2
    sel = Selector(text = html)
    list = sel.xpath('/html/body//table[2]/tbody//tr').extract()

    master_dic = {}
    for item in list[1:]:
        sel2 = Selector(text = item)
        date = sel2.xpath('//td[3]').extract()[0][18:-5]
        course_name = sel2.xpath('//td[1]').extract()[0][36:-5]
        time = sel2.xpath('//td[4]').extract()[0][18:-5]
        location = sel2.xpath('//td[6]').extract()[0][4:-5]
        sub_dic = {'Date': date, 'Time': time, 'Location': location}
        master_dic[course_name] = sub_dic

    if desired_course in master_dic.keys() :
        return('Date: ' + str(master_dic[desired_course]['Date']) + ' Time: ' + str(master_dic[desired_course]['Time']) + ' Location: ' + str(master_dic[desired_course]['Location']))
    else :
        return('Please enter a course name with a valid final.')




