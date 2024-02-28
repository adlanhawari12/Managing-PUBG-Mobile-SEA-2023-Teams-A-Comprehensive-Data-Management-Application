# PROJECT CRETAE READ UPLOAD DELETE DATA PUBG MOBILE SEA 2023


team1 = {
    "Nama" : "Bigetron E-Sport", 
    "Negara" : "indonesia", 
    "Dropzone" : "Mylta",   
    "Roaster": 7
    }
team2 = {
    "Nama" : "Secret E-SPort", 
    "Negara" : "Malaysia", 
    "Dropzone": "Hospital", 
    "Roaster": 6 
    }
team3 = {
    "Nama" : "Faze clan", 
    "Negara": "Thailand",
    "Dropzone" : "Yesnaya", 
    "Roaster" : 6
    }
team4 = {
    "Nama" : "Box Gaming", 
    "Negara" : "Vietnam",
    "Dropzone" : "Zharki",  
    "Roaster" : 5
    }

team5 = {
    "Nama" : "Yoodo", 
    "Negara" : "Malaysia",
    "Dropzone" : "Pochinki",  
    "Roaster" : 4
}
team6 = {
    "Nama" : "Vampire", 
    "Negara" : "Thailand",
    "Dropzone" : "Farm",  
    "Roaster" : 5
} 
team7 = {
    "Nama" : "Pigmy Esport", 
    "Negara" : "Indonesia",
    "Dropzone" : "Zharki",  
    "Roaster" : 5
}

team8 = {
    "Nama" : "Boom Esport", 
    "Negara" : "indonesia",
    "Dropzone" : "School",  
    "Roaster" : 6
}   

team9 = {
    "Nama" : "Xerxia", 
    "Negara" : "Thailand",
    "Dropzone" : "Zharki",  
    "Roaster" : 5
}

listTeam = {
    "team1" : team1,
    "team2" : team2,
    "team3" : team3,
    "team4" : team4,
    "team5" : team5,
    "team6" : team6,
    "team7" : team7,
    "team8" : team8,
    "team9" : team9,
}

list_juara = {}

def team_pmsl_2023() :
    print('\t ======Team PUBG MOBILE SEA(SOUTH EAST ASIA) 2023======\t')
    print(68*'-')
    print(f"{'Index':<8} {'| Nama':<20} {'|Negara':<15} {'|Dropzone':<15} {'|Roaster':<15}")
    print(68*'-')
    for team in listTeam.keys() : 
        Index = team
        Nama = listTeam[team]["Nama"]
        Negara = listTeam[team]["Negara"]
        Dropzone = listTeam[team]["Dropzone"]
        Roaster = listTeam[team]["Roaster"]
        print(f"{Index:<8} {Nama:<20} {Negara:<15} {Dropzone:<15} {Roaster:<15}")

## Menu 1 ---> Menampilkan team
def daftar_team() :
    while True:

        print("""  
                Apa  yang sedang anda cari?

            ======== Menu Report data ========
            1. Report Seluruh data PMSL SEA 2023
            2. Report data tertentu PMSL SEA 2023
            3. Kembali ke menu utama""")
        print("")
        menu_read = input("Silahkan masukkan sub menu pilihan anda [1 - 3] : ")
        if menu_read == '1' :
            team_pmsl_2023()
            daftar_team()

        elif menu_read == '2' :
            while True:
                team_pmsl_2023()
                FindTeam = input('Silahkan masukkan kode index team yang ingin dicari : ')
                if FindTeam in listTeam.keys() :
                    print('Hasil Pencarian Nama team berdasarkan Index')
                    print(68*'-')
                    print(f"{'Index':<8} {'| Nama Team':<20} {'| Negara':<15} {'| Dropzone':<15} {'| Roaster':<15}")
                    print(68*'-')
                    Index = FindTeam
                    Nama = listTeam[FindTeam]["Nama"]
                    Negara = listTeam[FindTeam]["Negara"]
                    Dropzone = listTeam[FindTeam]["Dropzone"]
                    Roaster = listTeam[FindTeam]["Roaster"]
                    print(f"{Index:<8} {Nama:<20} {Negara:<15} {Dropzone:<15} {Roaster:<15}")
                    print("")
                    FindMore = input('Apakah ada lagi team yang ingin anda cari(YES/NO): ').upper()
                    if FindMore == 'NO' :
                        menuUtama()
                    elif FindMore == 'YES' :
                        continue
                else :
                    print('Index TEAM PMSL SEA 2023 yang anda masukkan tidak ada di dalam daftar')
                    continue
        elif menu_read == '3':
            menuUtama()
                
        else:
            print("Menu yang anda masukkan harus dalam range [1 - 3]")
            continue

## Menu 2 ---> Menambah team
def tambahTeam() :
    while True :
        print("")
        print("""  
        ====== Menambah data PMSL SEA 2023 =======
        
            1. Tambah data team pmsl 2023
            2. Kembali ke menu utama
            """)
        menu_tambah = input("Silahkan pilih sub menu tambah team [1 - 2] :")
        if menu_tambah == '1' :
            while True :
                team_pmsl_2023()
                print('Menambah Team')
                for team in listTeam.keys() :
                    Index = team
                teamTemplate = {
                    "Nama" : "namateam",
                    "Negara" : "negara",
                    "Dropzone" : "dropzone",
                    "Roaster" : 0
                    }
                teamBaru = dict.fromkeys(teamTemplate.keys())
                indexBaru = input("Silahkan masukkan indexs team baru yang ingin ditambah :")
                if indexBaru in listTeam.keys():
                    print('Index team PMSL SEA yang anda tambahkan sudah terdaftar')
                    continue
                
                teamBaru["Nama"] = input("silahkan masukkan nama team : ").capitalize()
                teamBaru["Negara"] = input("silahkan masukkan negara asal team :").capitalize()
                teamBaru["Dropzone"] = input("Silahkan masukkan nama  daerah Dropzone yang akan digunakan :").capitalize()
                teamBaru["Roaster"] = int(input("silahkan masukkan jumlah roaster team :"))
                saveData = input("Simpan data team PMSL SEA terbaru (YES/NO) : ").upper()
                if saveData == 'NO' :
                    print('Data team PMSL SEA terbaru batal tersimpan')
                    break
                elif saveData == 'YES' :
                    listTeam.update({indexBaru : teamBaru})
                    team_pmsl_2023()
                    print('\n')
                    tambahLagi = input("""Data team baru PMSL SEA terbaru sudah tersimpan, Apakah anda mau menambahkan Team yang lain? (YES/NO) : """).upper()
                    if tambahLagi == 'YES' :
                        continue
                    elif tambahLagi == 'NO' :
                         break
        elif menu_tambah == '2':
            menuUtama()
        
        else :
            print("Menu yang anda masukkan harus dalam range [1 - 2]")
            continue

## Menu 3 ---> Mengubah team
def updateTeam():
    while True:
        print("")
        print("""
            ====== Mengupdate data PMSL SEA 2023 =======
        
            1. Update data team pmsl 2023
            2. Kembali ke menu utama
            """)
        menu_update = input("Silahkan pilih sub menu tambah team [1 - 2] :")
        if menu_update == '1' :
            print('Update Team PMSL SEA 2')
            team_pmsl_2023()
            while True :
                updateTeam = input("Silahkan masukkan kode Index Team PMSL 2023 yang akan di update : ")
                if updateTeam not in listTeam:
                    print("Index TEAM PMSL yang anda masukkan tidak terdaftar ")
                print(68*'-')
                print(f"{'Index' :<8} {'| Nama' :<20} {'| Negara' :15} {'| Dropzone' :<15} {'| Roaster' :<15}")
                print(68*'-')
                Index = updateTeam 
                Nama = listTeam[updateTeam]["Nama"]
                Negara = listTeam[updateTeam]["Negara"]
                Dropzone = listTeam[updateTeam]["Dropzone"]
                Roaster = listTeam[updateTeam]["Roaster"]
                print(f"{Index:<8} {Nama:<20} {Negara:<15} {Dropzone:<15} {Roaster:<15}")
                break
            updateTerbaru = input('Silahkan masukkan kolom data yang ingin di update:').capitalize()
            listTeam[updateTeam][updateTerbaru] = input('Silahkan masukkan update data terbaru : ').capitalize()
            print(f"Data Team PMSL SEA dengan index : {updateTeam} berhasil di update")
            team_pmsl_2023()
            

        elif menu_update == '2':
            menuUtama()

        else :
            print("Menu yang anda masukkan harus dalam range [1 - 2]")
            continue

## Menu 4 ---> Menghapus team
def DeleteTeam() :
    while True :
        print("")
        print("""
            
            ====== Menghapus data PMSL SEA 2023 =======
        
            1. Menghapus data team pmsl 2023
            2. Kembali ke menu utama
            """)
        menu_delete = input("Silahkan pilih sub menu tambah team [1 - 2] :")
        if menu_delete == '1' :
            while True :
                print("")
                team_pmsl_2023()
                print("")
                del_team = input("Silahkan masukkan index Team PMSL SEA yang akan di hapus: ")
                print("")
                if del_team not in listTeam :
                    print("Index yang anda masukkan tidak terdaftar di dalam team PMSL SEA ")
                    continue
                else :
                    break
            while True :
                deleteNotif = input("Apakah anda yakin untuk menghapus TEAM PMSL SEA? (YES/NO) : ")
                if deleteNotif == 'NO' or deleteNotif == 'no' :
                    print(f"TEAM PMSL SEA dengan index : {del_team} tidak berhasil terhapus")
                    break
                elif deleteNotif == 'YES' or deleteNotif == 'yes':
                    listTeam.pop(del_team)
                    print(f"\nTEAM PMSL SEA dengan index : {del_team} berhasil terhapus")
                    team_pmsl_2023()
                    break
                else:
                    break
        elif menu_delete == '2':
            menuUtama()
        
        else :
            print("Menu yang anda masukkan harus dalam range [1 - 2]")

## Menu 5 ---> Memberi penghargaan team
def penghargaan():
    while True :
        print("")
        print(""" 
        ===== Menu Penghargaan juara PMSL SEA ====
            1. Penghargaan untuk juara PMSL SEA
            2. Kembali ke menu utama
            """)
        
        
        input_juara = input("Silahkan pilih sub menu yang ingin anda jalankan [1 - 2] : ")
        print("")
        if input_juara == '1' :
            team_pmsl_2023()
            while True :
                for item in list_juara.keys():
                    IndexJuara = item
                JuaraTemplate = {
                    "Nama" : "namateam",
                    "Negara" : "negarateam",
                    "Rank" : 0,
                    "Hadiah" : 000000000
                }

                #### untuk Juara 1
                while True:
                    penghargaan1 = dict.fromkeys(JuaraTemplate.keys())
                    print("")
                    IndexJuara1 = input("Silahkan masukkan index team yang juara: ")
                    if IndexJuara1 not in listTeam.keys():
                        print("Tidak ada index team terdaftar pada TEAM PMSL SEA 2023")
                        continue
                    else :
                        break
                penghargaan1['Nama'] = listTeam[IndexJuara1]['Nama']
                penghargaan1['Negara'] = listTeam[IndexJuara1]['Negara']
                while True :
                    print("")
                    penghargaan1['Rank'] = int(input("Silahkan Masukkan rank team juara [1] : "))   
                    if penghargaan1['Rank'] > 1 :
                        print("Rank team harus sama dengan 1 ")
                        continue
                    else :
                        break
                print("")
                penghargaan1_input = int(input("Silahkan masukkan nominal hadiah juara PMSL SEA 2023 : "))
                penghargaan1['Hadiah'] = penghargaan1_input


                ## untuk juara 2
                while True:
                    penghargaan2 = dict.fromkeys(JuaraTemplate.keys())
                    print("")
                    IndexJuara2 = input("Silahkan masukkan index team yang juara [2]: ")
                    if IndexJuara2 not in listTeam.keys():
                        print("Tidak ada index team terdaftar pada TEAM PMSL SEA 2023")
                        continue
                    elif IndexJuara2 == IndexJuara1  :
                        print("Index team sudah terdaftar di list juara, silahkan masukkan index team yang lain")
                    else :
                        break
                penghargaan2['Nama'] = listTeam[IndexJuara2]['Nama']
                penghargaan2['Negara'] = listTeam[IndexJuara2]['Negara']
                while True :
                    print("")
                    penghargaan2['Rank'] = int(input("Silahkan Masukkan rank team juara [2] : "))   
                    if penghargaan2['Rank'] != 2 :
                        print("Rank team harus sama dengan 2")
                        continue
                    else :
                        break

                while True :
                    print("")
                    penghargaan2_input= int(input("Silahkan masukkan nominal hadiah juara 2 PMSL SEA 2023 : "))
                    if penghargaan2_input >= penghargaan1_input :
                        print("silahkan masukkan nilai nominal hadiah kecil dari hadiah juara 1")
                    else :
                        break
                penghargaan2['Hadiah'] = penghargaan2_input

                ### Untuk juara 3
                while True:
                    penghargaan3 = dict.fromkeys(JuaraTemplate.keys())
                    print("")
                    IndexJuara3 = input("Silahkan masukkan index team yang juara [3]: ")
                    if IndexJuara3 not in listTeam.keys():
                        print("Tidak ada index team terdaftar pada TEAM PMSL SEA 2023")
                        continue
                    elif IndexJuara3 == IndexJuara1 :
                        print("Index team sudah terdaftar di list juara, silahkan masukkan index team yang lain")
                    elif IndexJuara3 == IndexJuara2 :
                        print("Index team sudah terdaftar di list juara, silahkan masukkan index team yang lain")
                    else :
                        break
                penghargaan3['Nama'] = listTeam[IndexJuara3]['Nama']
                penghargaan3['Negara'] = listTeam[IndexJuara3]['Negara']
                while True :
                    print("")
                    penghargaan3['Rank'] = int(input("Silahkan Masukkan rank team juara [3] : "))   
                    if penghargaan3['Rank'] != 3 :
                        print(" Rank Team harus sama dengan 3")
                        continue
                    else :
                        break
                print("")
                while True :
                    print("")
                    penghargaan3_input= int(input("Silahkan masukkan nominal hadiah juara 3 PMSL SEA 2023 : "))
                    if penghargaan3_input >= penghargaan1_input :
                        print("silahkan masukkan nilai nominal hadiah kecil dari hadiah juara 1 dan 2")
                    elif penghargaan3_input >= penghargaan2_input :
                        print("silahkan masukkan nilai nominal hadiah kecil dari hadiah juara 1 dan 2")
                    else :
                        break
                penghargaan3['Hadiah'] = penghargaan3_input

                list_juara.update({IndexJuara1 : penghargaan1})
                list_juara.update({IndexJuara2 : penghargaan2})
                list_juara.update({IndexJuara3 : penghargaan3})

                print("")
                print('\t\t===Selamat kepada Juara PMSL SEA 2023=== \n')
                print(f"{'Index' :<8} {'| Nama' :<20} {'| Negara' :15} {'| Rank' :<15} {'| Hadiah' :<15}")
                print(f"{IndexJuara1:<8} {list_juara[IndexJuara1]['Nama']:<20} {list_juara[IndexJuara1]['Negara']:<15} {list_juara[IndexJuara1]['Rank']:<15} {list_juara[IndexJuara1]['Hadiah']:<15}") 
                print(f"{IndexJuara2:<8} {list_juara[IndexJuara2]['Nama']:<20} {list_juara[IndexJuara2]['Negara']:<15} {list_juara[IndexJuara2]['Rank']:<15} {list_juara[IndexJuara2]['Hadiah']:<15}") 
                print(f"{IndexJuara3:<8} {list_juara[IndexJuara3]['Nama']:<20} {list_juara[IndexJuara3]['Negara']:<15} {list_juara[IndexJuara3]['Rank']:<15} {list_juara[IndexJuara3]['Hadiah']:<15}") 
                break

        elif input_juara == '2' :
            menuUtama()  

        else :
            print("Menu yang anda masukkan harus dalam range [1 - 2]")    
            continue 
            
####### PROSES 
def menuUtama() :
    print("")
    print("""
           ================ Menu Utama =================
        == PUBG MOBILE SUPER LEAGUE SEA(SOUTH EAST ASIA) 2023 ==
          
          1. Report data team pubg mobile sea 2023       
          2. Menambahkan data pubg mobile sea 2023      
          3. Mengubah data pubg mobile sea 2023         
          4. Menghapus data pubg mobile sea 2023        
          5. Memberi penghargaan team pubg mobile sea 2023
          6. Exit program
         """)
    InputMenu = int(input("Silahkan pilih menu yang ingin anda jalankan: "))

    if InputMenu == 1 :
        daftar_team()

    elif InputMenu == 2 :
        tambahTeam()
        
    elif InputMenu == 3 :
        updateTeam()

    elif InputMenu == 4 :
        DeleteTeam()

    elif InputMenu == 5 :
        penghargaan()

    elif InputMenu == 6 :
        print("Anda berhasil keluar dari program")
        exit()

menuUtama()