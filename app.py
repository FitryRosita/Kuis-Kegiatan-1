import streamlit as st

# Konfigurasi tampilan
st.set_page_config(page_title="🎮 Kuis Peluang - Cublak-Cublak Suweng", page_icon="🎮")

# Background cokelat muda
st.markdown("""
    <style>
    .stApp {
        background-color: #f5e8dc;
    }
    </style>
""", unsafe_allow_html=True)

# Judul & Caption
st.title("🎮 Kuis Interaktif Peluang - Cublak-Cublak Suweng")
st.caption("Materi: Ruang Sampel, Kejadian, dan Peluang (PG + Uraian + Pembahasan)")

# Session kontrol
if "nama_dikunci" not in st.session_state:
    st.session_state.nama_dikunci = False

# Input Nama
if not st.session_state.nama_dikunci:
    nama = st.text_input("Masukkan nama kamu:")
    if nama:
        if st.button("Mulai Kuis"):
            st.session_state.nama = nama
            st.session_state.nama_dikunci = True
else:
    st.success(f"Halo, {st.session_state.nama}! Yuk, kita mulai kuis interaktifnya 🎮")

    # =====================
    # Soal Pilihan Ganda
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

    for idx, soal in enumerate(soal_pilgan):
        st.write(soal["soal"])
        pilihan = st.radio("Pilih jawaban:", soal["opsi"], key=f"pg_{idx}")
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
                <h5 style='color:#2e7d32;'>✅ Jawaban Benar: <b>{skor} dari {len(soal_pilgan)} soal</b></h5>
                <h3 style='color:#d84315;'>🎉 Nilai: <b>{int(skor/len(soal_pilgan)*100)}/100</b></h3>
            </div>
        """, unsafe_allow_html=True)

    # =====================
    # Soal Uraian + Pembahasan
    st.header("📘 Soal Uraian")

    soal_uraian = [
        {
            "soal": "6. (Uraian) Pada percobaan pelemparan tiga koin sekaligus:\n a. Tentukan ruang sampel dan banyaknya elemen ruang sampel\n b. Tentukan kejadian A yaitu muncul paling sedikit dua angka",
            "pembahasan": "a. Ruang sampel S = {AAA, AAG, AGA, AGG, GAA, GGA, GAG, GGG}, jadi n(S) = 8\nb. A = {AAA, AAG, AGA, GAA}, karena ini kejadian muncul minimal dua angka. Jadi n(A) = 4"
        },
        {
            "soal": "7. (Uraian) Pada percobaan melambungkan dua buah dadu secara bersamaan:\n a. Tentukan ruang sampel dan banyaknya elemen ruang sampel\n b. Tentukan kejadian A yaitu muncul angka-angka yang berjumlah 9",
            "pembahasan": "a. Ruang sampel pelemparan dua dadu = 36 kombinasi, jadi n(S) = 36\nb. A = {(3,6), (4,5), (5,4), (6,3)}, karena jumlahnya 9. Jadi n(A) = 4"
        }
    ]

    for idx, soal in enumerate(soal_uraian):
        st.markdown(f"**{soal['soal']}**")
        st.text_area("Jawaban kamu:", key=f"uraian_{idx}")
        if st.button(f"💡 Tampilkan Pembahasan Soal {idx+6}"):
            st.info(f"🔍 **Pembahasan Soal {idx+6}:**\n\n{soal['pembahasan']}")
