import urllib
import re
from bs4 import BeautifulSoup



# Fungsi untuk ambil list variabel input dari tag html (ambil atribut name)
def fetchListInput(alamat_website):
    html_doc = urllib.urlopen(alamat_website)
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.prettify())
    print("\n")
   
    tampung_variabel_elemen = []
    tampung_tag = soup.find_all('input')
    print(tampung_tag)
    index = 0;

    print("panjang array_TAG:::::{}".format(len(tampung_tag)))
    while(index < len(tampung_tag)):
        tampung_variabel_elemen.append(tampung_tag[index].get('name'))
        index = index + 1


    return tampung_variabel_elemen



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


# html_doc = urllib.urlopen("http://192.168.43.83/ceh/coba_site.html")
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print("\n")
# for z in soup.find_all('input'):
#     print(z.get('name'))


# tampung = soup.find_all('input')
# print(tampung[0])