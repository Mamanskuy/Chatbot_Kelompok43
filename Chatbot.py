import random

# Fungsi untuk menghasilkan respon acak
def generate_response(user_input):
    greetings = ["hai", "halo", "hi", "hello", "selamat pagi", "selamat siang", "selamat sore", "selamat malam"]
    goodbyes = ["byee", "goodbye", "sampai jumpa", "dada", "see you", "hingga nanti"]
    thanks = ["terima kasih", "thanks", "makasih", "sukron", "trimakasih"]
    # Jika input pengguna adalah salam
    if user_input.lower() in greetings:
        responses = ["Hai! Ada yang bisa saya bantu?", "Selamat datang! Ada yang bisa saya bantu?"]
        return random.choice(responses)
    # Jika input pengguna adalah permintaan untuk keluar
    elif user_input.lower() in goodbyes:
        responses = ["Terima kasih telah menggunakan chatbot ini. Sampai jumpa!", "Hingga jumpa lagi!"]
        return random.choice(responses)
    # Jika input pengguna adalah ucapan terima kasih
    elif user_input.lower() in thanks:
        responses = ["Sama-sama! Ada lagi yang bisa saya bantu?", "Tidak masalah. Ada lagi yang bisa saya bantu?"]
        return random.choice(responses)
    # Jika input pengguna tidak dikenali
    else:
        responses = [
            "Maaf, saya tidak mengerti. Bisa dijelaskan lagi?",
            "Hmm, saya kurang paham. Ada yang bisa saya bantu?",
            "Silakan sampaikan masalah Anda."
        ]
        return random.choice(responses)

# Method untuk meminta input dari pengguna dan menghasilkan respon
def chat():
    print("Halo! Selamat datang di chatbot sederhana ini.")
    print("Silakan sampaikan pertanyaan atau masalah Anda.")
    while True:
        user_input = input("Anda: ")
        if user_input.lower() in ["keluar", "exit"]:
            print("Chatbot: " + generate_response(user_input))
            break
        elif user_input == "":
            continue
        else:
            print("Chatbot: " + generate_response(user_input))
            
# Memanggil method chat untuk memulai chatbot
chat()
