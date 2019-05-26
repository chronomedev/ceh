import re
from selenium import webdriver
from bs4 import BeautifulSoup
# import urllib




# Fungsi untuk ambil list variabel input dari tag html (ambil atribut name)
def fetchListInput(hasil_soup):
    print(hasil_soup.prettify())
    tampung_variabel_elemen = []
    tampung_tag = hasil_soup.find_all('input')
    print(tampung_tag)

    index = 0;
    print("panjang array_TAG:::::{}".format(len(tampung_tag)))
    while(index < len(tampung_tag)):
        # if tampung_tag[index].get('type') == 'password' or tampung_tag[index].get('type') == 'text':
        if tampung_tag[index].get('type') == 'password':
            print(tampung_tag[index].get('name'))
            tampung_variabel_elemen.append(tampung_tag[index-1].get('name'))
            tampung_variabel_elemen.append(tampung_tag[index].get('name'))
            break;
        

        index = index + 1

    # print("PANJANG CLEANSING::::{}".format(len(tampung_variabel_elemen)))
    # print("--------------------------")
    print(tampung_variabel_elemen)
    return tampung_variabel_elemen


# driver fetch HTML document HTML
def fetchHTMLdoc(link_request):
    browser = webdriver.Firefox()
    browser.get(link_request)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    html_soup = BeautifulSoup(innerHTML, 'html.parser')
    #browser.quit()
    return html_soup



# fungsi untuk ambil action submit dari form
def getFormAction(soup_html):
    tag_form = soup_html.find_all("form")
    if tag_form[0].get('action') == "" or tag_form[0].get('action') == None:
        print('kosong bos')
        return None
    else:
        print("ada bos")
        print(tag_form[0].get('action'))
        return tag_form[0].get('action')


    #print(ekstrak_html.form['action'])

  




###################yang di comment buat debugging aja

# input1 = raw_input("Ambil halaman web: ")

# getFormAction(input1)