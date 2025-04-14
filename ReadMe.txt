Bu proje, Python kullanarak FTP (File Transfer Protocol) işlemlerini gerçekleştiren bir FTP istemcisi içerir. Bu betik, dosya yükleme, indirme, listeleme, yeniden adlandırma, dizin oluşturma ve silme gibi temel FTP işlemlerini destekler.

Denetim Masası > Programlar > Windows Özelliklerini Aç veya Kapat seçeneği üzerinden Internet Information Services (IIS) bölümünündeki FTP Sunucusu seçeneğini işaretleyip özelliği yükledikten sonra ekran görüntüsündeki gibi bir username ve password ile kullanıcı eklenir.


Daha sonra kod içerisindeki 

host = "localhost"
port = 21
username = "ftpuser"
password = "sifren123"

bilgileri kodun çalıştırılacağı sunucuya göre ve oluşturulan user bilgilerine göre değiştirilerek kod içerisindeki fonksiyonlar bir nesne oluşturularak çağrılır ve çalıştırılır.


Fonksiyonlar

1. setConnection(host, port, username, password)

FTP sunucusuna bağlanır.

2. listRemoteDir()

Uzak FTP sunucusundaki dizin ve dosyaları listeler.

3. listLocalDir(path)

Yerel bilgisayardaki dizin ve dosyaları listeler (mevcut dizin).

4. createDir(dirname)

FTP sunucusunda yeni bir dizin oluşturur.

5. deleteDir(dirname)

FTP sunucusundan belirtilen dizini siler.

6. uploadFile(local_file, remote_file)

Yerel bir dosyayı FTP sunucusuna yükler.

7. downloadFile(remote_file, local_file)

FTP sunucusundan bir dosyayı indirir.

8. renameFile(old_name, new_name)

FTP sunucusunda bir dosyanın adını değiştirir.

9. closeConnection()

FTP bağlantısını kapatır.