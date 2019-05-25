import urllib
import re
from selenium import webdriver
from bs4 import BeautifulSoup



# Fungsi untuk ambil list variabel input dari tag html (ambil atribut name)
def fetchListInput(link_request):
    hasil_soup = BeautifulSoup(fetchHTMLdoc(link_request), 'html.parser')
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
    #browser.quit()
    return innerHTML



# fungsi untuk ambil action submit dari form
def getFormAction(alamat_website):
    html = urllib.urlopen(alamat_website)
    ekstrak_html = BeautifulSoup(html, "html.parser")
    try:
        print(ekstrak_html.form['action'])

    except:
        print("Form kosong")
        

    #print(ekstrak_html.form['action'])

  




###################yang di comment buat debugging aja

# input1 = raw_input("Ambil halaman web: ")

# getFormAction(input1)