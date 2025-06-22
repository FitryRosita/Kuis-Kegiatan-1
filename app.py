import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Kuis Kegiatan 1", page_icon="🌷")

# Background cokelat muda
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f4f2;
    }
    </style>
""", unsafe_allow_html=True)

# Judul dan Caption
st.title("🎮 Kuis Interaktif - Kegiatan 1")
st.caption("Topik: Titik Sampel, Ruang Sampel, Percobaan, dan Kejadian (Etnomatematika - Permainan Cublak-cublak Suweng)")

# =====================
# Petunjuk pengerjaan
with st.expander("📌 Petunjuk Pengerjaan", expanded=True):
    st.markdown("""
    - Masukkan nama kamu terlebih dahulu.
    - Jawab soal pilihan ganda terlebih dahulu (no. 1–5).
    - Lanjutkan ke soal uraian (no. 6–7).
    - Tekan tombol untuk mengirim jawaban dan melihat pembahasan.
    """)

# =====================
# Session nama
if "nama_dikunci" not in st.session_state:
    st.session_state.nama_dikunci = False

# Input nama
if not st.session_state.nama_dikunci:
    nama = st.text_input("Masukkan nama kamu:")
    if nama:
        if st.button("Mulai Kuis"):
            st.session_state.nama = nama
            st.session_state.nama_dikunci = True

# =====================
else:
    st.success(f"Halo, {st.session_state.nama}! Silakan mengerjakan kuis di bawah ini. Semangat ya 🎯")

    # ========== SOAL PILIHAN GANDA ==========
    st.header("📝 Soal Pilihan Ganda")

    soal_pilgan = [
        {
            "soal": "1. Ruang sampel dari permainan Cublak-Cublak Suweng dengan pemain Fahri (penebak), Gilang, Hana, dan Laila, adalah...",
            "opsi": ["A. {Gilang, Fahri, Hana}",
                     "B. {Hana, Laila, Fahri}",
                     "C. {Gilang, Hana, Laila}",
                     "D. {Gilang, Fahri, Hana, Laila}"],
            "jawaban": "C"
        },
        {
            "soal": "2. Banyaknya anggota ruang sampel dalam permainan Cublak-Cublak Suweng dengan 8 pemain adalah...",
            "opsi": ["A. 8", "B. 7", "C. 6", "D. 9"],
            "jawaban": "B"
        },
        {
            "soal": "3. Dalam permainan dengan 5 pemain, jika kejadian A adalah 'suweng ada di tangan pemain perempuan' dan terdapat 2 pemain perempuan (Sari dan Tini), maka A = ...",
            "opsi": ["A. {Sari}", "B. {Tini}", "C. {Sari, Tini}", "D. {Sari, Tini, penebak}"],
            "jawaban": "C"
        },
        {
            "soal": "4. Seorang siswa melempar sebuah dadu bermata enam sekali. Ruang sampel dari percobaan ini adalah...",
            "opsi": ["A. 1", "B. {1, 2, 3, 4, 5, 6}", "C. Angka genap", "D. Salah satu dari {1, 2, 3}"],
            "jawaban": "B"
        },
        {
            "soal": "5. Seorang guru membuat permainan undian sederhana di kelas. Ia memasukkan 4 bola berwarna merah, 3 biru, dan 2 kuning ke dalam kotak. Setiap siswa mengambil satu bola secara acak tanpa melihat. Manakah kejadian yang paling mungkin terjadi?",
            "opsi": ["A. kejadian terambilnya bola merah ", "B. kejadian terambilnya bola biru", "C. kejadian terambilnya bola kuning", "D. kejadian terambilnya bola putih"],
            "jawaban": "A"
        }
    ]

    jawaban_pg = []
    skor = 0

    for i, soal in enumerate(soal_pilgan):
        st.markdown(f"**{soal['soal']}**")
        pilihan = st.radio("Pilih jawaban:", soal["opsi"], key=f"pg_{i}")
        jawaban_pg.append(pilihan[0])

    if st.button("📨 Kirim Jawaban Pilihan Ganda"):
        st.subheader("📊 Hasil Jawaban Pilihan Ganda")
        for i, user_jawab in enumerate(jawaban_pg):
            kunci = soal_pilgan[i]["jawaban"]
            if user_jawab == kunci:
                st.success(f"Soal {i+1}: ✅ Benar (Jawaban: {kunci})")
                skor += 1
            else:
                st.error(f"Soal {i+1}: ❌ Salah. Jawaban yang benar: {kunci}")

        st.session_state.skor_pg = skor

        st.markdown("---")
        st.subheader("🎓 Ringkasan Skor Pilihan Ganda")
        st.markdown(f"""
            <div style='background-color:#fff8e1; padding: 16px; border-radius: 10px; text-align: left;'>
                <h4 style='color:#4e342e;'> Nama: <b>{st.session_state.nama}</b></h4>
                <h5 style='color:#4e342e;'> Jawaban Benar: <b>{skor} dari {len(soal_pilgan)} soal</b></h5>
                <h3 style='color:#d84315;'>🎉 Nilai: <b>{int(skor/len(soal_pilgan)*100)}/100</b></h3>
            </div>
        """, unsafe_allow_html=True)

    # ========== SOAL URAIAN ==========
    st.header("📝 Soal Uraian")

    soal6 = """**6.** Pada percobaan pelemparan tiga koin sekaligus:
a. Tentukan ruang sampel dan banyaknya elemen ruang sampel  
b. Tentukan kejadian A yaitu muncul paling sedikit dua angka"""
    st.markdown(soal6)
    jawaban6 = st.text_area("Jawaban kamu untuk soal 6:", key="uraian_6")
    kunci_6 = ["a.", "AAA", "AAG", "AGA", "AGG", "GAA", "GGA", "GAG", "GGG", "n(S)", "n(s)", "8", "delapan", "b.", "B.", "GAA"]

    soal7 = """**7.** Pada percobaan melambungkan dua buah dadu secara bersamaan:
a. Tentukan ruang sampel dan banyaknya elemen ruang sampel  
b. Tentukan kejadian A yaitu muncul angka-angka yang berjumlah 9"""
    st.markdown(soal7)
    jawaban7 = st.text_area("Jawaban kamu untuk soal 7:", key="uraian_7")
    kunci_7 = ["a.", "A.", "b.", "B.", "36", "tiga puluh enam", "(3,6)", "(4,5)", "(5,4)", "(6,3)", "3,6", "4,5", "5,4", "6,3"]

    if st.button("📬 Kirim Jawaban Uraian"):
        skor_uraian = 0
        st.subheader("🔍 Pemeriksaan Jawaban & Pembahasan")

        cocok_6 = [k for k in kunci_6 if k.lower() in jawaban6.lower()]
        st.markdown("**Soal 6:**")
        if len(cocok_6) >= 5:
            st.success(f"✅ Jawaban soal 6 cukup baik. ({len(cocok_6)} kata kunci terdeteksi)")
            skor_uraian += 1
        else:
            st.warning(f"⚠️ Jawaban soal 6 kurang lengkap. ({len(cocok_6)} dari {len(kunci_6)} kata kunci)")
        st.markdown("**Pembahasan:**\n- a. Ruang sampel S = {AAA, AAG, AGA, AGG, GAA, GGA, GAG, GGG}, jadi n(S) = 8\n- b. A = {AAA, AAG, AGA, GAA}, karena ini kejadian muncul minimal dua angka. Jadi n(A) = 4")

        cocok_7 = [k for k in kunci_7 if k.lower() in jawaban7.lower()]
        st.markdown("**Soal 7:**")
        if len(cocok_7) >= 5:
            st.success(f"✅ Jawaban soal 7 cukup baik. ({len(cocok_7)} kata kunci terdeteksi)")
            skor_uraian += 1
        else:
            st.warning(f"⚠️ Jawaban soal 7 kurang lengkap. ({len(cocok_7)} dari {len(kunci_7)} kata kunci)")
        st.markdown("**Pembahasan:**\n- a. Ruang sampel pelemparan dua dadu = 36 kombinasi, jadi n(S) = 36\n- b. A = {(3,6), (4,5), (5,4), (6,3)}, karena jumlahnya 9. Jadi n(A) = 4")

        skor_pg = st.session_state.get("skor_pg", 0)
        total_skor = skor_pg + skor_uraian
        total_soal = len(soal_pilgan) + 2

        st.markdown("---")
        st.subheader("🎓 Ringkasan Total Nilai Kuis")
        st.markdown(f"""
            <div style='background-color:#fff3e0; padding: 16px; border-radius: 10px; text-align: left;'>
                <h4>Nama: <b>{st.session_state.nama}</b></h4>
                <h5>Skor Total Benar: <b>{total_skor} dari {total_soal} soal</b></h5>
                <h3 style='color:#e65100;'>🎉 Nilai Akhir: <b>{int((total_skor / total_soal) * 100)}/100</b></h3>
            </div>
        """, unsafe_allow_html=True)
