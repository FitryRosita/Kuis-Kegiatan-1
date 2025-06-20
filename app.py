import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="🎮 Kuis Peluang - Cublak-Cublak Suweng", page_icon="🎮")

# Background cokelat muda
st.markdown("""
    <style>
    .stApp { background-color: #ECFAE5; }
    </style>
""", unsafe_allow_html=True)

# Judul
st.title("🎮 Kuis Interaktif Peluang - Cublak-Cublak Suweng")
st.caption("Topik: Ruang Sampel, Kejadian, dan Peluang")

# ==========================
# Petunjuk
with st.expander("📌 Petunjuk Pengerjaan", expanded=True):
    st.markdown("""
    - Masukkan nama kamu terlebih dahulu.
    - Jawab soal pilihan ganda terlebih dahulu (no. 1–5).
    - Lalu jawab soal uraian (no. 6–7).
    - Tekan tombol untuk mengirim jawaban dan melihat pembahasan.
    """)

# ==========================
# Session kontrol
if "nama_dikunci" not in st.session_state:
    st.session_state.nama_dikunci = False

# Input nama
if not st.session_state.nama_dikunci:
    nama = st.text_input("Masukkan nama kamu:")
    if nama:
        if st.button("Mulai Kuis"):
            st.session_state.nama = nama
            st.session_state.nama_dikunci = True

# ==========================
else:
    st.success(f"Halo, {st.session_state.nama}! Selamat mengerjakan kuis berikut. 😊")

    # Soal PG
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
            "soal": "5. Manakah kejadian yang paling mungkin terjadi dalam undian bola merah, biru, kuning (4:3:2)?",
            "opsi": ["A. Bola merah", "B. Bola biru", "C. Bola kuning", "D. Bola putih"],
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

        st.markdown("---")
        st.subheader("🎓 Ringkasan Skor Pilihan Ganda")
        st.markdown(f"""
            <div style='background-color:#fff8e1; padding: 16px; border-radius: 10px; text-align: left;'>
                <h4 style='color:#4e342e;'> Nama: <b>{st.session_state.nama}</b></h4>
                <h5 style='color:#4e342e;'> Jawaban Benar: <b>{skor} dari {len(soal_pilgan)} soal</b></h5>
                <h3 style='color:#d84315;'>🎉 Nilai: <b>{int(skor/len(soal_pilgan)*100)}/100</b></h3>
            </div>
        """, unsafe_allow_html=True)

    # Soal Uraian
    st.header("📘 Soal Uraian")

    soal_uraian = [
        {
            "soal": "6a. Tentukan ruang sampel dan banyaknya elemen ruang sampel dari pelemparan tiga koin sekaligus.",
            "soal2": "6b. Tentukan kejadian A yaitu muncul paling sedikit dua angka.",
            "pembahasan": "a. S = {AAA, AAG, AGA, AGG, GAA, GGA, GAG, GGG}, jadi n(S) = 8\nb. A = {AAA, AAG, AGA, GAA}, jadi n(A) = 4"
        },
        {
            "soal": "7a. Tentukan ruang sampel dan banyaknya elemen ruang sampel dari pelemparan dua dadu.",
            "soal2": "7b. Tentukan kejadian A yaitu muncul angka-angka yang berjumlah 9.",
            "pembahasan": "a. S = 36 pasangan (1,1) sampai (6,6), jadi n(S) = 36\nb. A = {(3,6), (4,5), (5,4), (6,3)}, jadi n(A) = 4"
        }
    ]

    jawaban_uraian = []
    for i, soal in enumerate(soal_uraian):
        st.markdown(f"**{soal['soal']}**")
        st.text_area("Jawaban kamu:", key=f"uraian_{i}_a")
        st.markdown(f"**{soal['soal2']}**")
        st.text_area("Jawaban kamu:", key=f"uraian_{i}_b")

    if st.button("📩 Kirim Jawaban Uraian"):
        st.subheader("🔍 Pembahasan Soal Uraian")
        for i, soal in enumerate(soal_uraian):
            pembahasan_lines = soal["pembahasan"].split("\n")
            st.markdown(f"**Soal {i+6}a - Pembahasan:** {pembahasan_lines[0]}")
            st.markdown(f"**Soal {i+6}b - Pembahasan:** {pembahasan_lines[1]}")
