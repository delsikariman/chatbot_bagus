def get_response(user_text):
    text = user_text.lower().strip()

    if "apa itu ai" in text or text == "ai" or "artificial intelligence" in text:
        return "Artificial Intelligence atau AI adalah teknologi yang membuat komputer mampu meniru sebagian kemampuan berpikir manusia, seperti mengenali pola, belajar dari data, dan mengambil keputusan sederhana."

    elif "machine learning" in text:
        return "Machine Learning adalah cabang AI yang memungkinkan komputer belajar dari data tanpa harus diprogram secara rinci untuk setiap tugas."

    elif "deep learning" in text:
        return "Deep Learning adalah bagian dari Machine Learning yang menggunakan jaringan saraf tiruan bertingkat untuk mempelajari pola yang lebih kompleks."

    elif "nlp" in text or "natural language processing" in text:
        return "Natural Language Processing atau NLP adalah cabang AI yang mempelajari bagaimana komputer memahami, mengolah, dan menghasilkan bahasa manusia."

    elif "computer vision" in text:
        return "Computer Vision adalah cabang AI yang membuat komputer mampu memahami gambar dan video, misalnya untuk deteksi wajah atau pengenalan objek."

    elif "cabang ai" in text or "cabang-cabang ai" in text:
        return "Beberapa cabang AI antara lain Machine Learning, Deep Learning, NLP, Computer Vision, Robotics, dan Expert System."

    elif "contoh ai" in text or "penerapan ai" in text:
        return "Contoh penerapan AI adalah chatbot, rekomendasi film, deteksi wajah, mobil otonom, penerjemah otomatis, dan sistem prediksi."

    elif "halo" in text or "hai" in text:
        return "Halo juga. Silakan ajukan pertanyaan tentang AI dasar."

    else:
        return "Maaf, saya belum memiliki jawaban yang sesuai. Coba tanyakan tentang AI, Machine Learning, Deep Learning, NLP, atau Computer Vision."