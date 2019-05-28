import re
from selenium import webdriver
from bs4 import BeautifulSoup
# import urllib




# Fungsi untuk ambil list variabel input dari tag html (ambil atribut name)
def fetchListInput(hasil_soup):
    #print(hasil_soup.prettify())
    tampung_variabel_elemen = []
    tampung_tag = hasil_soup.find_all('input')
    #print(tampung_tag)

    index = 0;
    #print("panjang array_TAG:::::{}".format(len(tampung_tag)))
    while(index < len(tampung_tag)):
        # if tampung_tag[index].get('type') == 'password' or tampung_tag[index].get('type') == 'text':
        if tampung_tag[index].get('type') == 'password':
            #print(tampung_tag[index].get('name'))
            tampung_variabel_elemen.append(tampung_tag[index-1].get('name'))
            tampung_variabel_elemen.append(tampung_tag[index].get('name'))
            break;
        

        index = index + 1

    # print("PANJANG CLEANSING::::{}".format(len(tampung_variabel_elemen)))
    # print("--------------------------")
    #print(tampung_variabel_elemen)
    return tampung_variabel_elemen


# driver fetch HTML document HTML using Selenium gecko driver
def fetchHTMLdoc(link_request):
    print("> menjalankan webdriver...")
    browser = webdriver.Firefox()
    browser.get(link_request)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    html_soup = BeautifulSoup(innerHTML, 'html.parser')
    browser.quit()
    return html_soup



# fungsi untuk ambil action submit dari form
def getFormAction(soup_html):
    tag_form = soup_html.find_all("form")
    if tag_form[0].get('action') == "" or tag_form[0].get('action') == None:
        #print('kosong bos')
        return None
    else:
        #print("ada bos")
        #print(tag_form[0].get('action'))
        return tag_form[0].get('action')


    #print(ekstrak_html.form['action'])


# fungsi untuk cleansing request URL
def linkCleansing(pecah, form_action_url):
    link_url_force = ""
    indeks_loop = 0
    while(indeks_loop<len(pecah)):
        if indeks_loop == (len(pecah)-1):
		    link_url_force = link_url_force + "/" + form_action_url
        elif indeks_loop == 0 :
		    link_url_force = link_url_force + pecah[indeks_loop] + "//"
        elif pecah[indeks_loop] == "" :
			indeks_loop = indeks_loop + 1
			continue
        else:
		    link_url_force = link_url_force + pecah[indeks_loop] + "/"
		    #print(pecah[indeks_loop])

        indeks_loop = indeks_loop+1

    return link_url_force	    



  




###################yang di comment buat debugging aja
