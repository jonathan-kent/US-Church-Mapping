import config
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


baptist = ["Alliance of Baptists","American Baptist","American Baptist Association","Baptist","Baptist (Missionary)","Baptist Bible Fellowship International","Baptist General Conference","Baptist- Independent","Conservative Baptist Association of America","Converge Worldwide (Baptist General Conference)","Cooperative Baptist Fellowship","Fellowship of Evangelical Baptist Churches in Canada","General Association of General Baptists","General Association of Regular Baptist","National Association of Free Will Baptists","National Baptist Convention of America","National Baptist Convention, USA","National Missionary Baptist Convention of America","North American Baptist Conference in Canada","Progressive National Baptist Convention","Southern Baptist Convention","United Baptist Convention of the Atlantic Province", "Full Gospel Baptist Church Fellowship"]
methodist = ["African Methodist Episcopal","African Methodist Episcopal Zion","Christian Methodist Episcopal (CME)","Free Methodist Church of North America","Methodist","United Methodist"]
presbyterian = ["Cumberland Presbyterian Church","Presbyterian","Presbyterian Church in America","Presbyterian Church in Canada"]
orthodox = ["Antiochian Orthodox Christian Archdiocese","Coptic Orthodox","Greek Orthodox","Greek Orthodox Metropolis of Toronto (Canada)","Orthodox","Orthodox Church in America","Romanian Orthodox Episcopate","Ukrainian Orthodox","Ukrainian Orthodox Church of Canada", "Armenian Apostolic Church"]
episcopal = ["Anglican", "Anglican Church of Canada", "Episcopal"]
catholic = ["Catholic", "Roman Catholic"]
lutheran = ["American Association of Lutheran","Association of Free Lutheran Congregations","Evangelical Lutheran in America","Lutheran","Lutheran Church of Missouri Synod","Wisconsin Evangelical Lutheran Synod"]
reformed = ["Reformed", "Christain Reformed Church in North America", "Evangelical Presbyterian"]
calvinist = ["Calvinist", "Netherlands Reformed Congregations"]
pentecostal = ["Apostolic Church of Pentecost of Canada", "Assemblies of God", "Church of God", "Church of God (Cleveland, TN)", "Church of God (Pentecostal)", "Church of God in Christ", "Church of God of Prophecy", "Church of Our Lord Jesus Christ of the Apostolic Faith", "Congregational Holiness", "Elim Fellowship", "Fellowship of Christian Assemblies", "Foursquare Gospel", "Full Gospel", "International Pentecostal Holiness", "Open Bible", "Pentecostal", "Pentecostal Assemblies of Canada", "Pentecostal Assemblies of the World", "Pentecostal Church of God", "United Pentecostal Church", "United Pentecostal Church International", "Apostolic", "The Christian Congregation"]
adventist = ["General Conference Church of God (Seventh Day)", "Seventh Day Adventist"]
mennonite = ["Council of Mennonite Brethren Churches", "General Council of Mennonites", "Mennonite"]
messianic = ["Messianic Judaism"]
amish = ["Old Order Amish Church"]
quaker = ["Quaker"]
denominations = [baptist, methodist, presbyterian, orthodox, episcopal,\
                 catholic, lutheran, reformed, calvinist, pentecostal,\
                 adventist, mennonite, messianic, amish, quaker]
denom_names = ["Baptist", "Methodist", "Presbyterian", "Orthodox", "Episcopal",\
               "Catholic", "Lutheran", "Reformed", "Calvinist", "Pentecostal",\
               "Adventist", "Mennonite", "Messianic Jewish", "Amish", "Quaker",\
               "Protestant"]


class church_logger:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        #add chrome webdriver file path
        self.driver = webdriver.Chrome(config.driver_path,chrome_options=chrome_options)
        self.driver.get("https://www.churchfinder.com/christian-churches-united-states")
        sleep(1)

    def get_cities(self, state):
        self.driver.get("https://www.churchfinder.com/churches/"+state)
        i = 1
        more_cities = True
        while more_cities == True:
            try:
                for j in range(1,6):
                    self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div/div/div/div/div/div/article/div/div[2]/div/div/div/table/tbody/tr["+str(i)+"]/td["+str(j)+"]/div/span/a").click()
                    sleep(2)
                    self.get_churches(state)
                    self.driver.get("https://www.churchfinder.com/churches/"+state)
                i = i + 1
            except Exception as e:
                more_cities = False
                print(e)

    def get_churches(self, state):
        more_pages = True
        page = 0
        while more_pages == True:
            divs = extra_divs(page)
            arrow = 5
            if page > 0:
                arrow = 7
            last = False
            i = 1
            while last == False:
                try:
                    address = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div/div/div/div/div/article/div/div[1]/div/div[3]"+divs+"div[2]/div["+str(i)+"]/div[3]/div/div").text
                    denomination = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div/div/div/div/div/article/div/div[1]/div/div[3]"+divs+"div[2]/div["+str(i)+"]/div[4]").text
                    denom = "Protestant"
                    for index, d in enumerate(denominations):
                        if denomination in d:
                            denom = denom_names[index]
                            break
                    file = open(state+".txt", "a")
                    file.writelines(address+";"+denom+"\n")
                    file.close()
                    i = i + 1
                except Exception as e:
                    print("end of page")
                    last = True

            try:
                self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div/div/div/div/div/article/div/div[1]/div/div[3]"+divs+"div[3]/ul/li["+str(arrow)+"]/a").click()
                page = page + 1
                sleep(3)
            except Exception as e:
                more_pages = False
                print("no more pages")


def extra_divs(num):
    divs = ""
    for i in range(num):
        divs = divs+"/div"
    return divs + "/"

church_logger = church_logger()
church_logger.get_cities("ma")
