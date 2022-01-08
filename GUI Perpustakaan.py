from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

root =Tk()

conn = sqlite3.connect("Perpustakaan.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("DROP TABLE IF EXISTS LIBRARY")
    query = """
    CREATE TABLE LIBRARY(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        JUDUL TEXT NOT NULL,
        KATEGORI TEXT NOT NULL,
        NOMOR_RAK TEXT NOT NULL,
        PENULIS TEXT,
        PENERBIT TEXT,
        TAHUN TEXT,
        STOK INT
    )
    """
    cursor.execute(query)
    conn.commit()

def isfirst(table_name):
    query = ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(table_name)
    cursor.execute(query)
    conn.commit()
    if cursor.fetchone()[0]==1 :
        return False
    else :
        return True

def select_all():
    query ="SELECT ID,JUDUL,KATEGORI,NOMOR_RAK,PENULIS,PENERBIT,TAHUN,STOK FROM LIBRARY"
    cursor.execute(query)
    rows= cursor.fetchall()
    update_trv(rows)

def update_trv(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def update_people():
    if messagebox.askyesno("Harap Konfirmasi lagi","Apakah Anda Ingin Mempebarui Data Ini?"):
        query ="""
        UPDATE LIBRARY
        SET JUDUL=:JUDUL,KATEGORI=:KATEGORI,NOMOR_RAK=:NOMOR_RAK,PENULIS=:PENULIS,PENERBIT=:PENERBIT,TAHUN=:TAHUN,STOK=:STOK WHERE ID=:ID
        """
        params={
            'ID':v_id.get(),
            'JUDUL':v_judul.get(),
            'KATEGORI':v_kategori.get(),
            'NOMOR_RAK':v_no_rak.get(),
            'PENULIS':v_penulis.get(),
            'PENERBIT':v_penerbit.get(),
            'TAHUN':v_tahun_terbit.get(),
            'STOK':v_jumlah_stok.get()
        }
        cursor.execute(query,params)
        conn.commit()
        clear()
        clear_filed()
        select_all()
    else :
        return True

def add_new():
    query = """
    INSERT INTO LIBRARY
    (JUDUL,KATEGORI,NOMOR_RAK,PENULIS,PENERBIT,TAHUN,STOK)
    VALUES(:JUDUL, :KATEGORI, :NOMOR_RAK, :PENULIS, :PENERBIT, :TAHUN, :STOK)"""
    params={
        'JUDUL':v_judul.get(),
        'KATEGORI':v_kategori.get(),
        'NOMOR_RAK':v_no_rak.get(),
        'PENULIS':v_penulis.get(),
        'PENERBIT':v_penerbit.get(),
        'TAHUN':v_tahun_terbit.get(),
        'STOK':v_jumlah_stok.get()
    }
    cursor.execute(query,params)
    conn.commit()
    clear_filed()

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(rowid)
    v_id.set(item['values'][0])
    v_judul.set(item['values'][1])
    v_kategori.set(item['values'][2])
    v_no_rak.set("00"+str(item['values'][3]))
    v_penulis.set(item['values'][4])
    v_penerbit.set(item['values'][5])
    v_tahun_terbit.set(item['values'][6])
    v_jumlah_stok.set(item['values'][7])

def clear_filed():
    judul_field.delete(0,'end')
    penulis_field.delete(0,'end')
    penerbit_field.delete(0,'end')
    tahun_field.delete(0,'end')
    Kategori_field.set('')
    no_rak_field.set('')
    jumlah_stok_field.delete(0,'end')

def search():
    q2 = q.get()
    query = """
    SELECT ID,JUDUL,KATEGORI,NOMOR_RAK,PENULIS,PENERBIT,TAHUN,STOK FROM LIBRARY WHERE JUDUL LIKE {} OR NOMOR_RAK LIKE {}
    """.format("'%"+q2+"%'","'%"+q2+"%'")
    cursor.execute(query)
    conn.commit()
    rows = cursor.fetchall()
    update_trv(rows)


def clear():
    ent.delete(0, 'end')
    clear_filed()
    select_all()

    
def delete_book():
    id= v_id.get()
    if(messagebox.askyesno("Konfirmasi Hapus","Apakah Anda Serius Ingin Menghapus Data Ini?")):
        query = "DELETE FROM LIBRARY WHERE ID = {}".format(id)
        cursor.execute(query)
        conn.commit()
        clear_filed()
        select_all()
    else :
        return True


wrapper1=LabelFrame(root, text="Daftar Buku")
wrapper2=LabelFrame(root, text="Pencarian")
wrapper3=LabelFrame(root, text="Data Buku")

wrapper1.pack(fill="both",expand="yes",padx=20,pady=10)
wrapper2.pack(fill="both",padx=20,pady=10)
wrapper3.pack(fill="both",padx=20,pady=10)

v_id = IntVar()
v_judul = StringVar()
v_kategori =StringVar()
v_no_rak = StringVar()
v_penulis = StringVar()
v_penerbit = StringVar()
v_tahun_terbit = StringVar()
v_jumlah_stok = IntVar()

judul = Label(wrapper3, text="Judul")
judul_field = Entry(wrapper3, textvariable=v_judul)
judul.grid(row=0,column=0,sticky="w",pady=4)
judul_field.grid(row=0,column=1,columnspan=2,sticky="w",pady=4,padx=10)

Kategori = Label(wrapper3,text="Kategori")
Kategori_field = ttk.Combobox(wrapper3,width=18,textvariable=v_kategori)
Kategori_field['values']=(
                    '000 - Umum',
                    '100 - Filsafat',
                    '200 - Teknologi',
                    '300 - Agama',
                    '400 - Budaya',
                    '500 - Sosial',
                    '600 - Psikologi',
                    '700 - Sains dan Matematika',
                    '800 - Sejarah dan Geografi',
                    '900 - Bahasa Asing'
                )
Kategori.grid(row=1,column=0,sticky="w",pady=4)
Kategori_field.grid(row=1,column=1,columnspan=2,sticky="W",pady=4,padx=10)

no_rak =Label(wrapper3,text ="Nomor Rak")
no_rak_field = ttk.Combobox(wrapper3,width=18,textvariable=v_no_rak)
no_rak_field['values']=('001,002,003,004,005')
no_rak.grid(row=2,column=0,sticky="w",pady=4)
no_rak_field.grid(row=2,column=1,columnspan=2,sticky="W",pady=4,padx=10)

penulis =Label(wrapper3,text ="Penulis")
penulis_field = Entry(wrapper3,textvariable=v_penulis)
penulis.grid(row=3,column=0,sticky="w",pady=4)
penulis_field.grid(row=3,column=1,columnspan=2,sticky="W",pady=4,padx=10)

penerbit =Label(wrapper3,text ="Penerbit")
penerbit_field = Entry(wrapper3,textvariable=v_penerbit)
penerbit.grid(row=0,column=3,sticky="w",pady=4,padx=10)
penerbit_field.grid(row=0,column=4,columnspan=2,sticky="W",pady=4)

tahun_terbit =Label(wrapper3,text ="Tahun Penerbit")
tahun_field = Entry(wrapper3,textvariable=v_tahun_terbit)
tahun_terbit.grid(row=1,column=3,sticky="w",pady=4,padx=10)
tahun_field.grid(row=1,column=4,columnspan=2,sticky="W",pady=4)

jumlah_stok =Label(wrapper3,text ="Jumlah Stok")
jumlah_stok_field = Entry(wrapper3,textvariable=v_jumlah_stok)
jumlah_stok.grid(row=2,column=3,sticky="w",pady=4,padx=10)
jumlah_stok_field.grid(row=2,column=4,columnspan=2,sticky="W",pady=4)

frame_btn = Frame(wrapper3)
up_btn = Button(frame_btn,text="Update",command=update_people,fg="blue")
add_btn = Button(frame_btn,text="Tambah Baru",command=add_new,fg="green")
delete_btn = Button(frame_btn,text="Hapus",command=delete_book,fg="red")

frame_btn.grid(row=4,column=0,columnspan=5,sticky=W,pady=10)
add_btn.pack(side=LEFT,padx=5)
up_btn.pack(side=LEFT,padx=5)
delete_btn.pack(side=LEFT,padx=5)

q= StringVar()
lbl = Label(wrapper2,text="Search")
lbl.pack(side=LEFT,padx=10,pady=15)
ent = Entry(wrapper2,textvariable=q)
ent.pack(side=LEFT,padx=6,pady=15)
btn = Button(wrapper2,text="Search",command=search,fg="blue")
btn.pack(side=LEFT,padx=6,pady=15)
cbtn = Button(wrapper2,text="Clear",command=clear,fg="red")
cbtn.pack(side=LEFT,padx=6,pady=15)

trv = ttk.Treeview(wrapper1,column=(0,1,2,3,4,5,6,7),show="headings",height=6)
style = ttk.Style()
style.theme_use("clam")
trv.pack(side=RIGHT)
trv.place(x=0,y=0)

trv.heading(0,text = "Id")
trv.heading(1,text = "Judul")
trv.heading(2,text = "Kategori")
trv.heading(3,text = "Nomor Rak")
trv.heading(4,text = "Penulis")
trv.heading(5,text = "Penerbit")
trv.heading(6,text = "Tahun Terbit")
trv.heading(7,text = "Jumlah Stok")

trv.column(0,stretch=NO,minwidth=0,width=0)
trv.column(1,width=90,minwidth=130,anchor=CENTER)
trv.column(2,width=90,minwidth=130,anchor=CENTER)
trv.column(3,width=90,minwidth=130,anchor=CENTER)
trv.column(4,width=90,minwidth=130,anchor=CENTER)
trv.column(5,width=90,minwidth=130,anchor=CENTER)
trv.column(6,width=90,minwidth=130,anchor=CENTER)
trv.column(7,width=90,minwidth=130,anchor=CENTER)

trv.bind('<Double 1>',getrow)

yscorllbar = Scrollbar(wrapper1,orient="vertical",command=trv.yview)
yscorllbar.pack(side=RIGHT,fill="y") 
xscorllbar = Scrollbar(wrapper1,orient="horizontal",command=trv.xview)
xscorllbar.pack(side=BOTTOM,fill="x") 

trv.configure(yscrollcommand=yscorllbar.set,xscrollcommand=xscorllbar.set)

if __name__ =='__main__':
    root.title("Aplikasi Perpustakaan")
    root.geometry("700x500")
    root.resizable(FALSE,FALSE)
    if(isfirst("LIBRARY")):
        create_table()
    else:
        select_all()
    root.mainloop()