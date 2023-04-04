import random

class Chatbot:
    def _init_(self):
        self.sapaan = ["hai", "halo", "hi", "hello", "selamat pagi", "selamat siang", "selamat sore", "selamat malam"]
        self.Exit = ["byee", "goodbye", "sampai jumpa", "dada", "see you", "sampai nanti"]
        self.Trims = ["terima kasih", "thanks", "makasih", "sukron", "terima kasih", "Suwun"]
    
    def generate_response(self, user_input):
        if user_input.lower() in self.sapaan:
            responses = ["Hai! Ada yang bisa saya bantu?", "Selamat datang! Ada yang bisa saya bantu?"]
            return random.choice(responses)
        elif user_input.lower() in self.Exit:
            responses = ["Terima kasih telah menggunakan chatbot ini. Sampai jumpa!", "Sampai jumpa lagi!"]
            return random.choice(responses)
        elif user_input.lower() in self.Trims:
            responses = ["Sama-sama! Ada lagi yang bisa saya bantu?", "Tidak masalah. Ada lagi yang bisa saya bantu?"]
            return random.choice(responses)
        else:
            responses = [
                "Maaf, saya tidak mengerti. Bisa dijelaskan lagi?",
                "Hmm, saya kurang paham. Ada yang bisa saya bantu?",
                "Silakan sampaikan masalah Anda."
            ]
            return random.choice(responses)

    def start_chat(self):
        print("Halo! Selamat datang di chatbot sederhana ini.")
        print("Silakan sampaikan pertanyaan atau masalah Anda.")
        while True:
            user_input = input("Anda: ")
            if user_input.lower() in self.Exit:
                print("Chatbot: " + self.generate_response(user_input))
                break
            elif user_input == "":
                continue
            else:
                print("Chatbot: " + self.generate_response(user_input))

chatbot = Chatbot()
chatbot.start_chat()
