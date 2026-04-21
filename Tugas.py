import tkinter as tk
from tkinter import messagebox

gejala_db = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Airliur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Beratbadan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh dimulut",
    "G29": "Benjolan dileher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam",
}

penyakit_db = {
    "Tonsilitis": {
        "gejala": ["G37", "G12", "G5", "G27", "G6", "G21"],
        "solusi": (
            "- Istirahat yang cukup dan perbanyak minum air hangat\n"
            "- Kumur air garam hangat untuk meredakan nyeri tenggorokan\n"
            "- Konsumsi obat pereda nyeri seperti paracetamol\n"
            "- Jika disebabkan bakteri, dokter akan meresepkan antibiotik\n"
            "- Pada kasus berulang, dokter mungkin menyarankan tonsilektomi"
        )
    },
    "Sinusitis Maksilaris": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
        "solusi": (
            "- Gunakan dekongestan untuk melegakan hidung tersumbat\n"
            "- Lakukan irigasi hidung dengan larutan garam (NaCl)\n"
            "- Kompres hangat di area wajah untuk mengurangi nyeri\n"
            "- Konsumsi antibiotik sesuai resep dokter\n"
            "- Hindari paparan debu dan alergen"
        )
    },
    "Sinusitis Frontalis": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
        "solusi": (
            "- Gunakan semprotan hidung saline untuk membersihkan sinus\n"
            "- Konsumsi dekongestan dan antihistamin sesuai anjuran dokter\n"
            "- Kompres hangat di area dahi untuk meredakan nyeri\n"
            "- Istirahat cukup dan perbanyak minum air putih\n"
            "- Jika kronis, konsultasikan ke dokter THT untuk tindakan lebih lanjut"
        )
    },
    "Sinusitis Edmoidalis": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
        "solusi": (
            "- Lakukan irigasi hidung secara rutin\n"
            "- Gunakan kortikosteroid nasal untuk mengurangi peradangan\n"
            "- Konsumsi antibiotik jika infeksi bakteri\n"
            "- Hindari merokok dan paparan polusi udara\n"
            "- Periksakan ke dokter THT jika gejala berlangsung lebih dari 12 minggu"
        )
    },
    "Sinusitis Sfenoidalis": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
        "solusi": (
            "- Segera konsultasi ke dokter THT karena lokasi sinus yang dalam\n"
            "- Gunakan antibiotik spektrum luas sesuai resep dokter\n"
            "- Lakukan CT-Scan untuk diagnosis yang lebih akurat\n"
            "- Hindari menundukkan kepala terlalu lama\n"
            "- Pada kasus berat, mungkin diperlukan tindakan operasi endoskopi"
        )
    },
    "Abses Peritonsiler": {
        "gejala": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
        "solusi": (
            "- Segera periksa ke dokter THT untuk drainase abses\n"
            "- Konsumsi antibiotik dosis tinggi sesuai resep dokter\n"
            "- Gunakan obat pereda nyeri dan antiinflamasi\n"
            "- Kumur dengan larutan antiseptik\n"
            "- Konsumsi makanan lunak dan perbanyak minum air"
        )
    },
    "Faringitis": {
        "gejala": ["G37", "G5", "G6", "G7", "G15"],
        "solusi": (
            "- Perbanyak minum air hangat dan istirahat\n"
            "- Kumur air garam hangat 3-4 kali sehari\n"
            "- Konsumsi lozenges (permen pelega tenggorokan)\n"
            "- Jika disebabkan bakteri Streptococcus, konsumsi antibiotik\n"
            "- Hindari makanan pedas dan minuman dingin"
        )
    },
    "Kanker Laring": {
        "gejala": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
        "solusi": (
            "- Segera konsultasi ke dokter spesialis onkologi THT\n"
            "- Lakukan biopsi untuk konfirmasi diagnosis\n"
            "- Pengobatan meliputi radioterapi, kemoterapi, atau operasi\n"
            "- Berhenti merokok dan konsumsi alkohol\n"
            "- Lakukan kontrol rutin sesuai jadwal dokter"
        )
    },
    "Deviasi Septum": {
        "gejala": ["G37", "G17", "G20", "G8", "G18", "G25"],
        "solusi": (
            "- Gunakan dekongestan untuk melegakan hidung\n"
            "- Gunakan semprotan steroid hidung\n"
            "- Hindari alergen yang memperburuk gejala\n"
            "- Pada kasus berat, lakukan operasi septoplasti\n"
            "- Konsultasikan ke dokter THT untuk evaluasi"
        )
    },
    "Laringitis": {
        "gejala": ["G37", "G5", "G15", "G16", "G32"],
        "solusi": (
            "- Istirahatkan suara, hindari berbicara terlalu keras\n"
            "- Perbanyak minum air hangat\n"
            "- Gunakan pelembab udara (humidifier)\n"
            "- Hindari merokok dan paparan asap\n"
            "- Jika berlangsung lebih dari 2 minggu, periksa ke dokter"
        )
    },
    "Kanker Leher & Kepala": {
        "gejala": ["G5", "G22", "G8", "G28", "G3", "G11"],
        "solusi": (
            "- Segera rujuk ke dokter spesialis onkologi\n"
            "- Lakukan pemeriksaan CT-Scan/MRI dan biopsi\n"
            "- Pengobatan sesuai stadium: operasi, radioterapi, kemoterapi\n"
            "- Jaga pola makan sehat dan nutrisi yang cukup\n"
            "- Lakukan follow-up rutin pasca pengobatan"
        )
    },
    "Otitis Media Akut": {
        "gejala": ["G37", "G20", "G35", "G31"],
        "solusi": (
            "- Konsumsi antibiotik sesuai resep dokter\n"
            "- Gunakan obat tetes telinga antiinflamasi\n"
            "- Kompres hangat di area telinga yang sakit\n"
            "- Jangan memasukkan benda apapun ke dalam telinga\n"
            "- Kontrol ulang ke dokter jika gejala tidak membaik dalam 3 hari"
        )
    },
    "Contact Ulcers": {
        "gejala": ["G5", "G2"],
        "solusi": (
            "- Istirahatkan suara secara total selama beberapa hari\n"
            "- Hindari berbisik karena justru menegangkan pita suara\n"
            "- Lakukan terapi suara dengan speech therapist\n"
            "- Hindari makanan asam dan pedas\n"
            "- Konsultasi ke dokter THT untuk pemeriksaan laringoskopi"
        )
    },
    "Abses Parafaringeal": {
        "gejala": ["G5", "G16"],
        "solusi": (
            "- Segera periksa ke dokter karena bisa mengancam jiwa\n"
            "- Diperlukan drainase abses melalui pembedahan\n"
            "- Konsumsi antibiotik intravena di rumah sakit\n"
            "- Pastikan jalan napas tetap aman\n"
            "- Rawat inap mungkin diperlukan untuk pemantauan"
        )
    },
    "Barotitis Media": {
        "gejala": ["G12", "G20"],
        "solusi": (
            "- Lakukan manuver Valsava untuk menyeimbangkan tekanan telinga\n"
            "- Kunyah permen karet atau menelan saat perubahan tekanan\n"
            "- Gunakan dekongestan sebelum naik pesawat atau menyelam\n"
            "- Hindari menyelam atau terbang saat pilek\n"
            "- Jika gejala berat, konsultasi ke dokter THT"
        )
    },
    "Kanker Nasofaring": {
        "gejala": ["G17", "G8"],
        "solusi": (
            "- Segera rujuk ke dokter spesialis onkologi THT\n"
            "- Lakukan biopsi nasofaring untuk konfirmasi\n"
            "- Pengobatan utama: radioterapi, dapat dikombinasi kemoterapi\n"
            "- Periksakan diri jika ada riwayat keluarga\n"
            "- Kontrol rutin setelah pengobatan selesai"
        )
    },
    "Kanker Tonsil": {
        "gejala": ["G6", "G29"],
        "solusi": (
            "- Segera periksakan ke dokter spesialis onkologi\n"
            "- Lakukan biopsi untuk menentukan jenis dan stadium\n"
            "- Pengobatan: operasi, radioterapi, atau kemoterapi\n"
            "- Berhenti merokok dan konsumsi alkohol\n"
            "- Lakukan pemeriksaan HPV terkait"
        )
    },
    "Neuronitis Vestibularis": {
        "gejala": ["G35", "G24"],
        "solusi": (
            "- Istirahat total saat serangan vertigo akut\n"
            "- Konsumsi obat antimual dan antivertigo\n"
            "- Lakukan rehabilitasi vestibular dengan fisioterapi\n"
            "- Hindari gerakan kepala yang mendadak\n"
            "- Gejala biasanya membaik dalam beberapa minggu"
        )
    },
    "Meniere": {
        "gejala": ["G20", "G35", "G14", "G4"],
        "solusi": (
            "- Kurangi konsumsi garam untuk mengurangi retensi cairan\n"
            "- Konsumsi obat diuretik sesuai resep dokter\n"
            "- Hindari kafein, alkohol, dan makanan tinggi garam\n"
            "- Lakukan terapi rehabilitasi vestibular\n"
            "- Pada kasus berat, mungkin diperlukan tindakan operasi"
        )
    },
    "Tumor Syaraf Pendengaran": {
        "gejala": ["G12", "G34", "G23"],
        "solusi": (
            "- Lakukan MRI untuk mendeteksi ukuran dan lokasi tumor\n"
            "- Pilihan pengobatan: observasi, radioterapi, atau operasi\n"
            "- Konsultasi ke dokter bedah saraf dan THT\n"
            "- Lakukan audiometri berkala untuk memantau pendengaran\n"
            "- Pertimbangkan alat bantu dengar jika pendengaran menurun"
        )
    },
    "Kanker Leher Metastatik": {
        "gejala": ["G29"],
        "solusi": (
            "- Segera lakukan biopsi benjolan di leher\n"
            "- Cari sumber kanker primer dengan pemeriksaan lengkap\n"
            "- Lakukan CT-Scan, PET-Scan untuk menentukan stadium\n"
            "- Pengobatan sesuai jenis kanker: operasi, kemo, radioterapi\n"
            "- Konsultasi ke tim onkologi multidisiplin"
        )
    },
    "Osteosklerosis": {
        "gejala": ["G34", "G9"],
        "solusi": (
            "- Konsultasi ke dokter THT untuk pemeriksaan audiometri\n"
            "- Pertimbangkan penggunaan alat bantu dengar\n"
            "- Pada kasus tertentu, operasi stapedektomi bisa dilakukan\n"
            "- Suplemen fluorida mungkin diresepkan dokter\n"
            "- Kontrol rutin untuk memantau perkembangan pendengaran"
        )
    },
    "Vertigo Postular": {
        "gejala": ["G24"],
        "solusi": (
            "- Lakukan manuver Epley untuk reposisi kristal telinga dalam\n"
            "- Hindari perubahan posisi kepala yang mendadak\n"
            "- Lakukan latihan Brandt-Daroff di rumah\n"
            "- Konsumsi obat antivertigo saat serangan\n"
            "- Konsultasi ke dokter THT untuk terapi vestibular"
        )
    },
}

def hitung_relevansi_gejala(gejala_ya, gejala_tidak):
    penyakit_mungkin = get_penyakit_mungkin(gejala_ya, gejala_tidak)
    skor = {}
    sudah_dijawab = gejala_ya | gejala_tidak

    for penyakit in penyakit_mungkin:
        for g in penyakit_db[penyakit]["gejala"]:
            if g not in sudah_dijawab:
                if g not in skor:
                    skor[g] = 0
                skor[g] += 1

    return skor


def get_penyakit_mungkin(gejala_ya, gejala_tidak):
    mungkin = []
    for penyakit, data in penyakit_db.items():
        gejala_penyakit = set(data["gejala"])
        cocok_ya = gejala_ya & gejala_penyakit
        sisa = gejala_penyakit - gejala_tidak
        if len(sisa) > 0 and (len(cocok_ya) > 0 or len(gejala_ya) == 0):
            mungkin.append(penyakit)
    return mungkin


def proses_diagnosa(gejala_dipilih):
    hasil = []

    for penyakit, data in penyakit_db.items():
        gejala_penyakit = set(data["gejala"])
        cocok = set(gejala_dipilih) & gejala_penyakit

        if cocok:
            persen = (len(cocok) / len(gejala_penyakit)) * 100
            hasil.append({
                "nama": penyakit,
                "persen": persen,
                "cocok": cocok,
                "total_gejala": len(gejala_penyakit),
                "solusi": data["solusi"]
            })

    hasil.sort(key=lambda x: x["persen"], reverse=True)
    return hasil


def get_gejala_berikutnya(gejala_ya, gejala_tidak):

    skor = hitung_relevansi_gejala(gejala_ya, gejala_tidak)
    if not skor:
        return None
    return max(skor, key=skor.get)


class AplikasiSistemPakarTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.root.geometry("550x450")
        self.root.resizable(True, True)
        self.gejala_ya = set()
        self.gejala_tidak = set()
        self.gejala_sekarang = None
        self.nomor_pertanyaan = 0

        self.buat_halaman_utama()

    def buat_halaman_utama(self):
        self.bersihkan()

        tk.Label(
            self.root,
            text="Sistem Pakar Diagnosa Penyakit THT",
            font=("Arial", 14, "bold")
        ).pack(pady=(30, 5))

        frame_info = tk.LabelFrame(self.root, text="Informasi", font=("Arial", 10, "bold"),
                                   padx=15, pady=10)
        frame_info.pack(padx=30, pady=20, fill="x")

        tk.Label(
            frame_info,
            text="Sistem ini akan mendiagnosa kemungkinan penyakit THT\n"
                 "berdasarkan gejala-gejala yang Anda alami.\n\n"
                 "Anda akan ditanya beberapa pertanyaan tentang gejala.\n"
                 "Jawab dengan  Ya  atau  Tidak  untuk setiap pertanyaan.",
            font=("Arial", 10), justify="left"
        ).pack()

        tk.Button(
            self.root, text="Mulai Diagnosa", font=("Arial", 12, "bold"),
            width=20, pady=10,
            command=self.mulai_diagnosa
        ).pack(pady=10)

    def mulai_diagnosa(self):
        self.gejala_ya = set()
        self.gejala_tidak = set()
        self.nomor_pertanyaan = 0
        self.tanya_berikutnya()

    def tanya_berikutnya(self):
        penyakit_mungkin = get_penyakit_mungkin(self.gejala_ya, self.gejala_tidak)

        if len(self.gejala_ya) > 0 and len(penyakit_mungkin) == 0:
            self.tampilkan_hasil()
            return

        gejala_next = get_gejala_berikutnya(self.gejala_ya, self.gejala_tidak)

        if gejala_next is None:
            self.tampilkan_hasil()
            return

        self.gejala_sekarang = gejala_next
        self.nomor_pertanyaan += 1
        self.buat_halaman_pertanyaan(gejala_next)

    def buat_halaman_pertanyaan(self, kode_gejala):
        self.bersihkan()
        nama_gejala = gejala_db[kode_gejala]

        frame_top = tk.Frame(self.root)
        frame_top.pack(fill="x", padx=15, pady=(10, 5))

        tk.Label(
            frame_top,
            text=f"Pertanyaan #{self.nomor_pertanyaan}",
            font=("Arial", 10, "bold")
        ).pack(side="left")

        tk.Label(
            frame_top,
            text=f"Ya: {len(self.gejala_ya)}  |  Tidak: {len(self.gejala_tidak)}",
            font=("Arial", 9)
        ).pack(side="right")

        tk.Frame(self.root, height=1, bg="gray").pack(fill="x", padx=15, pady=5)

        if self.gejala_ya:
            frame_riwayat = tk.LabelFrame(self.root, text="Gejala yang dialami",
                                          font=("Arial", 9, "bold"), padx=10, pady=5)
            frame_riwayat.pack(fill="x", padx=15, pady=(5, 10))

            daftar = ", ".join(
                [gejala_db[g] for g in sorted(self.gejala_ya, key=lambda x: int(x[1:]))]
            )
            tk.Label(
                frame_riwayat, text=daftar,
                font=("Arial", 9), wraplength=480, justify="left", anchor="w"
            ).pack(fill="x")

        frame_q = tk.LabelFrame(self.root, text="Pertanyaan", font=("Arial", 10, "bold"),
                                padx=20, pady=15)
        frame_q.pack(padx=20, pady=10, fill="x")

        tk.Label(
            frame_q,
            text="Apakah Anda mengalami gejala berikut?",
            font=("Arial", 10)
        ).pack(pady=(5, 10))

        tk.Label(
            frame_q,
            text=f"{nama_gejala}",
            font=("Arial", 14, "bold")
        ).pack(pady=(0, 5))

        tk.Label(
            frame_q,
            text=f"[Kode: {kode_gejala}]",
            font=("Arial", 9)
        ).pack(pady=(0, 10))

        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=15)

        tk.Button(
            frame_btn, text="Ya", font=("Arial", 11, "bold"),
            width=15, pady=5,
            command=self.jawab_ya
        ).pack(side="left", padx=10)

        tk.Button(
            frame_btn, text="Tidak", font=("Arial", 11, "bold"),
            width=15, pady=5,
            command=self.jawab_tidak
        ).pack(side="left", padx=10)

        frame_bawah = tk.Frame(self.root)
        frame_bawah.pack(side="bottom", fill="x", padx=15, pady=10)

        tk.Button(
            frame_bawah, text="Kembali ke Menu",
            font=("Arial", 9), width=15,
            command=self.buat_halaman_utama
        ).pack(side="left")

        if len(self.gejala_ya) >= 1:
            tk.Button(
                frame_bawah, text="Lihat Hasil Sekarang",
                font=("Arial", 9), width=18,
                command=self.tampilkan_hasil
            ).pack(side="right")

    def jawab_ya(self):
        if self.gejala_sekarang:
            self.gejala_ya.add(self.gejala_sekarang)
        self.tanya_berikutnya()

    def jawab_tidak(self):
        if self.gejala_sekarang:
            self.gejala_tidak.add(self.gejala_sekarang)
        self.tanya_berikutnya()

    def tampilkan_hasil(self):
        self.bersihkan()
        hasil = proses_diagnosa(self.gejala_ya)

        tk.Label(
            self.root, text="Hasil Diagnosa",
            font=("Arial", 14, "bold")
        ).pack(pady=(10, 5))

        tk.Label(
            self.root,
            text=f"Berdasarkan {len(self.gejala_ya)} gejala yang Anda alami",
            font=("Arial", 9)
        ).pack()

        frame_luar = tk.Frame(self.root)
        frame_luar.pack(fill="both", expand=True, padx=15, pady=10)

        scrollbar = tk.Scrollbar(frame_luar)
        scrollbar.pack(side="right", fill="y")

        text_hasil = tk.Text(
            frame_luar, wrap="word", font=("Consolas", 10),
            yscrollcommand=scrollbar.set
        )
        text_hasil.pack(fill="both", expand=True)
        scrollbar.config(command=text_hasil.yview)

        text_hasil.insert("end", "GEJALA YANG DIALAMI:\n")
        for g in sorted(self.gejala_ya, key=lambda x: int(x[1:])):
            text_hasil.insert("end", f"  [{g}] {gejala_db[g]}\n")
        text_hasil.insert("end", "\n")

        if not hasil:
            text_hasil.insert("end", "=" * 48 + "\n")
            text_hasil.insert("end", "Tidak ditemukan penyakit yang cocok\n")
            text_hasil.insert("end", "dengan gejala yang Anda alami.\n\n")
            text_hasil.insert("end", "Saran:\n")
            text_hasil.insert("end", "- Coba ulangi diagnosa dengan gejala berbeda\n")
            text_hasil.insert("end", "- Konsultasikan langsung ke dokter THT\n")
        else:
            for i, item in enumerate(hasil, 1):
                text_hasil.insert("end", "=" * 48 + "\n")
                text_hasil.insert("end", f"Diagnosa #{i}\n")
                text_hasil.insert("end", f"Penyakit   : {item['nama']}\n")
                text_hasil.insert("end", f"Kecocokan  : {item['persen']:.0f}% "
                                  f"({len(item['cocok'])}/{item['total_gejala']} gejala)\n\n")

                text_hasil.insert("end", "Gejala yang cocok:\n")
                for g in item["cocok"]:
                    text_hasil.insert("end", f"  - [{g}] {gejala_db[g]}\n")

                text_hasil.insert("end", "\nSolusi:\n")
                text_hasil.insert("end", f"{item['solusi']}\n\n")

        text_hasil.config(state="disabled")
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=10)

        tk.Button(
            frame_btn, text="Diagnosa Ulang", font=("Arial", 10),
            width=15, command=self.mulai_diagnosa
        ).pack(side="left", padx=5)

        tk.Button(
            frame_btn, text="Menu Utama", font=("Arial", 10),
            width=15, command=self.buat_halaman_utama
        ).pack(side="left", padx=5)

    def bersihkan(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiSistemPakarTHT(root)
    root.mainloop()
