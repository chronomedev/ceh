import ambiltag


#####TEMPAT CORAT CORET AMBIL LIBRARY FUNGSI SECARA PISAH-PISAH

html_ekstrak = ambiltag.fetchHTMLdoc("http:192.168.136.128/ceh/coba_site.html")

ambiltag.getFormAction(html_ekstrak)