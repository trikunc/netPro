# Variabel global untuk menyimpan data ip_address

router_list = []

# fungsi untuk menampilkan semua data
def show_data():
    if len(router_list) == 0:
        print ("BELUM ADA DATA")
    else:
        # for indeks in range(len(ip_address)):
        #     print ("[{}] {}".format(indeks, ip_address[indeks]))

        # ["192.168.1.1","192.168.1.2","192.168.1.3"]
        for index in range(len(router_list)):
            print(f"[{index}] {router_list[index]['ip']} ({router_list[index]['user']}/{router_list[index]['password']})")

# fungsi untuk menambah data
def insert_data():
    ip_address_baru = input("IP Address: ")
    user_baru = input("Username: ")
    pass_baru = input("Password: ")
    router_list.append({
        'ip': ip_address_baru,
        'user': user_baru,
        'password':pass_baru
    })

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID IP_Address: "))
    if(indeks >= len(router_list)):
        print ("ID salah")
    else:
        ip_baru = input("IP Address baru: ")
        user_baru = input("Username: ")
        pass_baru = input("Password: ")
        router_list[indeks]['ip'] = ip_baru
        router_list[indeks]['user'] = user_baru
        router_list[indeks]['password'] = pass_baru


# ["192.168.1.1","192.168.1.2","192.168.1.3"], len=3


# fungsi untuk menhapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID IP Address: "))
    if(indeks >= len(router_list)):
        print ("ID salah")
    else:
        router_list.remove(router_list[indeks])

# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[1] Show IP Address")
    print ("[2] Insert IP Address")
    print ("[3] Edit IP Address")
    print ("[4] Delete IP Address")
    print ("[5] Exit")
    
    menu = int(input("PILIH MENU> "))
    print ("\n")

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print ("Salah pilih!")


while True:
    show_menu()
