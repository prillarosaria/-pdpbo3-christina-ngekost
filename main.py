from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog

root = Tk()
root.title("Tugas Praktikum 3 DPBO Python")
val_nama = StringVar()
val_alamat = StringVar()
value_radio = StringVar()
val = StringVar()

def lihat():
    top = Toplevel()
    top.title("Lihat Data Diri")

    d_frame = LabelFrame(top, text="Data Diri", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    nama = Label(d_frame, text="Nama : " + val_nama.get(), anchor="w").grid(row=0, column=0, sticky="w")
    alamat = Label(d_frame, text="Alamat : " + val_alamat.get(), anchor="w").grid(row=1, column=0, sticky="w")
    jk = Label(d_frame, text="Jenis Kelamin : " + value_radio.get(), anchor="w").grid(row=2, column=0, sticky="w")
    kendaraan = Label(d_frame, text="Apakah Anda memiliki Kendaraan? : " + val.get(), anchor="w").grid(row=4, column=0, sticky="w")


def about():
    tentang = Toplevel()
    tentang.title("Tentang Aplikasi")

    d_frame = LabelFrame(tentang, text="Tentang Aplikasi", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    abt1 = Label(d_frame, text="versi 1.0", anchor="w").grid(row=0, column=0, sticky="w")
    abt2 = Label(d_frame, text="creator : Christina Prilla Rosaria Ardyanti", anchor="w").grid(row=1, column=0, sticky="w")
    abt1 = Label(d_frame, text="nim     : 1900575", anchor="w").grid(row=2, column=0, sticky="w")
    abt1 = Label(d_frame, text="kelas   : Ilmu Komputer C1", anchor="w").grid(row=3, column=0, sticky="w")


def field():
    isi = Toplevel()
    isi.title("Isi Data Diri")

    frame2 = LabelFrame(isi, text="Masukkan Data Dirimu", padx=10, pady=10)
    frame2.pack(padx=10, pady=10)

    label = Label(frame2, text="Nama", font=("Helvetica", 10)).pack()
    nama = Entry(frame2, textvariable=val_nama).pack()
    spasi = Label(frame2, text="", font=("Arial", 10)).pack()

    label = Label(frame2, text="Alamat", font=("Helvetica", 10)).pack()
    alamat = Entry(frame2, textvariable=val_alamat).pack()
    spasi = Label(frame2, text="", font=("Arial", 10)).pack()

    label = Label(frame2, text="Jenis Kelamin", font=("Helvetica", 10)).pack()
    radio_laki = Radiobutton(frame2, text="Laki-Laki", value="Laki-Laki", variable=value_radio).pack()
    radio_perempuan = Radiobutton(frame2, text="Perempuan", value="Perempuan", variable=value_radio).pack()
    spasi = Label(frame2, text="", font=("Arial", 10)).pack()

    cb = Checkbutton(frame2, text="Apakah Anda memiliki kendaraan?", variable=val, onvalue="Ya", offvalue="Tidak").pack()
    spasi = Label(frame2, text="", font=("Arial", 10)).pack()

    b_kirim = Button(frame2, text="Kirim").pack()

def hapus():
    val_nama.set("")
    val_alamat.set("")
    value_radio.set("")
    val.set("")

def keluar():
    msg = messagebox.askyesno("Keluar Aplikasi", "Apakah Anda Yakin?", icon='warning')
    if msg == "yes":
        root.destroy()
    else:
        msg2 = messagebox.showinfo('Kembali ke Aplikasi','Anda akan Kembali ke Aplikasi')

frame = LabelFrame(root, text="Selamat Datang!", padx=10, pady=10)
frame.pack(padx=10, pady=10)

namaApp = Label(frame, text="NGEKOST#", font=("Arial", 25)).grid(row=1, column=0, sticky="w")
desc = Label(frame, text="Aplikasi untuk berkenalan dengan teman kost terdekat", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w")

spasi = Label(frame, text="", font=("Arial", 25)).grid(row=3, column=0, sticky="w")
b_isi = Button(frame, text="Daftarkan Akun", command=field)
b_isi.grid(row=4, column=0)

b_lihat = Button(frame, text="Lihat Data Diri", command=lihat)
b_lihat.grid(row=5, column=0)

b_hapus = Button(frame, text="Hapus Data Diri", command=hapus)
b_hapus.grid(row=6, column=0)

b_about = Button(frame, text="Tentang", command=about)
b_about.grid(row=7, column=0)

spasi = Label(frame, text="", font=("Arial", 25)).grid(row=8, column=0, sticky="w")
b_exit = Button(frame, text="Exit", command=keluar)
b_exit.grid(row=9, column=0)



root.mainloop()
