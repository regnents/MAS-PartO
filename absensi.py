# Copyright of Rafael Sean Putra

import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# Preparing necessary variable
daftar_hasil =[]
checker = []

def second_counter(waktu):
    h, m, s = waktu.split(":")
    detik = (((int(h) * 60) + int(m)) * 60) + int(s)
    return detik

def sheet_editor():
    global daftar_hasil
    global checker
    scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]

    file_name = "client_key.json"
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
    client = gspread.authorize(creds)

    sheet_presensi = client.open("Presensi Peserta SPARTA 2019 v2")
    chosen_work = sheet_presensi.worksheet("Presensi")

    # Finding the column that need to be edited
    temp_cell_number = chosen_work.find(day)
    col_number = temp_cell_number.col
    temp_row_number = temp_cell_number.row + 1
    cell_data = chosen_work.cell(temp_row_number,col_number).value
    while cell_data != sesi:
        col_number += 1
        cell_data = chosen_work.cell(temp_row_number,col_number).value

    # Finding the row and edit the cell in the exact row and col
    start_time = time.time()
    for i in range (len(daftar_hasil)):
        if (checker[i] != 1):
            pass
        else:
            temp_nim = re.search("16519\d\d\d",daftar_hasil[i]).group(0)
            nim = temp_nim[-3:]
            kel = re.search("\d\d ",daftar_hasil[i]).group(0)
            kel = re.sub(" ","",kel)
            nim_cell = chosen_work.findall(nim)
            while (len(nim_cell) > 1):
                j = 0
                while j < len(nim_cell):
                    if (nim_cell[j].col != 1):
                        nim_cell.remove(nim_cell[j])
                    else:
                        j += 1
            if (len(nim_cell) == 0):
                print(nim + " gak ada di sheet presensi")
                checker[i] = -1
            else:
                row_number = nim_cell[0].row
                kel_cell_value =  chosen_work.cell(row_number,3).value
                if (int(kel_cell_value) != int(kel)):
                    print(nim + " ada tapi kelompoknya salah")
                    checker[i] = -1
                else:
                    chosen_work.update_cell(row_number,col_number,"1")
        if (i % 10 == 0):
            time.sleep(10 - ((time.time() - start_time) % 10))
            start_time = time.time()




# MAIN PROGRAM
# Open the zoom chat file
file_chat = input("Masukkan nama file chat ZOOM (Pastikan file berada di folder file-chat dan jangan lupa extensi .txt nya): ")
file_chat = "file-chat/" + file_chat
daftar_teks = open(file_chat,"r",encoding='utf-8')

# Getting all the data (day, sesi, waktu absensi)
day = "Day " + str(int(input("Day ke berapa? ")))
sesi = "Sesi " + str(int(input("Sesi ke berapa? ")))
print("\nMasukkan waktu awal dan akhir absensi (format JJ:MM:DD):")
waktu_awal = input("Waktu awal: ")
waktu_akhir = input("Waktu akhir: ")


detik_awal = second_counter(waktu_awal)
detik_akhir = second_counter(waktu_akhir)

# Moving the file into array of string
i = 0        
for line in daftar_teks:
    if (re.search("From .* \:",line)):
        daftar_hasil.append(line)
        i += 1
    else:
        daftar_hasil[i-1] = daftar_hasil[i-1] + line

daftar_teks.close()

# Filtering the chat 1: Removing chat outside the time range
i = 0
while i < len(daftar_hasil):
    temp = daftar_hasil[i]
    waktu_teks = temp[:8]
    detik_teks = second_counter(waktu_teks)
    if (detik_awal > detik_teks) or (detik_akhir < detik_teks):
        daftar_hasil.remove(temp)
    else:
        i += 1

# Filtering the chat 2: Removing not Private Chat and Private Chat not received by user
i = 0
while i < len(daftar_hasil):
    temp = daftar_hasil[i]
    if not re.search("\(Privately\)",temp):
        daftar_hasil.remove(temp)
    else:
        if not re.search("From( )*\d\d ",temp):
            daftar_hasil.remove(temp)
        else:
            i += 1

# Cleaning the chat
for i in range (len(daftar_hasil)):
    temp = daftar_hasil[i]
    temp = re.sub("From( )*","",temp)
    temp = re.sub("to.*\(Privately\) ","",temp)
    daftar_hasil[i] = re.sub("\n"," ",temp)

# Check if chat is about presence or not
for i in range (len(daftar_hasil)):
    temp_kel = re.findall(" \d\d ",daftar_hasil[i])
    temp_nim = re.findall("16519\d\d\d",daftar_hasil[i])
    if (len(temp_kel) != 2) and (len(temp_nim) != 2):
        checker.append(0)
    elif (temp_kel[0] != temp_kel[1]) and (temp_nim[0] != temp_nim[1]):
        checker.append(0)
        print("Presensi dan username berbeda untuk username " + temp_kel[0] + " " + temp_nim[0])
    else:
        checker.append(1)

# Open and edit the spreadsheet
done = 0
while not done:
    try:
        sheet_editor()
        done = 1
    except Exception as err:
        print(format(err))
        time.sleep(5)
        
# Writing the result in a txt file
nama_file = "hasil-absensi/absensi " + day + " " + sesi +".txt"
with open(nama_file,"w",encoding="utf-8") as f:
    for i in range (len(daftar_hasil)):
        if checker[i] == 1:
            f.write("SUKSES       ")
        elif checker[i] == 0:
            f.write("SALAH FORMAT ")
        elif checker[i] == -1:
            f.write("GAGAL ABSEN  ")
        f.write(daftar_hasil[i])
        f.write("\n")

