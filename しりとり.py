import os, json, random
directory = os.path.dirname(os.path.realpath(__file__))

f = open(os.path.join(directory,"json_words.txt"), "r")
j = json.loads(f.read())
f.close()

used_words = []

lang = {
   "Type PLAY, HELP or QUIT": "「PLAY」「HELP」または「QUIT」を入力",
   "play": "play",
   "I lose! GG": "やられた！すごいね！",
   "Kana:　　　":  "ひらがな： ",
   "Kanji:　 　":  "漢字：　　 ",
   "Definition:": "意味：　　 ",
   "quit": "quit",
   "I win. GG!": "やった！君も頑張ったね！",
   "You can't end with that": "「ん」で終わる言葉は、使えません。",
   "You can't do that": "これは出来ません。",
   "You already used that": "既に使いました。",
   "help": "help",
   "SHIRITORI「しりとり」is a Japanese word-guessing game.": "しりとりは言葉を考えるゲームです。",
   "Take turns by mentioning words (in hiragana) that start with the last letter of the previous word.": "自分の番に、相手が言った言葉の最後のひらがなで始まる言葉を考えます。",
   "You can't use the same word twice, and you can't end with ん": "同じ言葉は二回使えません。「ん」で終わる言葉は、使えません。",
   "Have fun!": "楽しんで！",
   "Bye! Play later :D": "またね！",
}
e = True

def gett(word):
    if e: return word
    else: return lang[word]

small = ["ゃ","ゅ","ょ","っ"]

shiritori = '''
   ______ _________  ______________  ___  ____
  / __/ // /  _/ _ \/  _/_  __/ __ \/ _ \/  _/
 _\ \/ _  // // , _// /  / / / /_/ / , _// /  
/___/_//_/___/_/|_/___/ /_/  \____/_/|_/___/  
'''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def random_word():
    c = random.choice(j)
    return {"kana":c['kana'],"kanji":c['kanji'],"def":c['def']}

def random_word_with_kana(kana):
    viable = []
    for i in range(len(j)):
        c = j[i]
        if c['kana'][0] == kana and c['kana'] not in used_words:
            viable.append(c)
    if len(viable) == 0: return "./lose"
    else:
        c = random.choice(viable)
        used_words.append(c['kana']) 
        return {"kana":c['kana'],"kanji":c['kanji'],"def":c['def']}

r = random_word_with_kana("あ")

def intro():
    os.system('clear')

    print(shiritori)
    print(gett("Type PLAY, HELP or QUIT"))

os.system('clear')

print("Type 'en' for English")
print("日本語にするには、「JA」を入力してください。")
while True:
    inp = input("\n> ")
    if inp.lower().strip()=="en":
        e = True
        break
    elif inp.lower().strip()=="ja":
        e = False
        break

intro()

while True:

    inp = input("\n> ").lower().strip()

    if inp == gett("play"):

        while True:
            if r == "./lose":
                intro()
                print(bcolors.OKGREEN+gett("I lose! GG")+bcolors.ENDC) 
                break

            os.system('clear')

            print(bcolors.OKBLUE+gett("Kana:　　　")+bcolors.ENDC,r['kana'])
            if(r['kanji']!="./none"): print(bcolors.OKBLUE+gett("Kanji:　 　")+bcolors.ENDC,r['kanji'])
            print(bcolors.OKBLUE+gett("Definition:")+bcolors.ENDC,r['def'])

            ll = r['kana'][-1]
            if ll in small: ll = r['kana'][-2]

            while True:
                i = input("\n> ")
                if i == gett("quit"):
                    intro()
                    print(bcolors.FAIL+gett("I win. GG!")+bcolors.ENDC)
                    break

                if i[-1] == "ん": print(bcolors.FAIL+gett("You can't end with that")+bcolors.ENDC)
                elif i[0] != ll: print(bcolors.FAIL+gett("You can't do that")+bcolors.ENDC)
                else:
                    if i not in used_words: break
                    else: print(bcolors.FAIL+gett("You already used that")+bcolors.ENDC)

            if i == gett("quit"): break
                
            ll = i[-1]
            if ll in small: ll = i[-2]

            used_words.append(i)

            r = random_word_with_kana(ll)

    elif inp == gett("help"):
        print(gett("SHIRITORI「しりとり」is a Japanese word-guessing game."))
        print(gett("Take turns by mentioning words (in hiragana) that start with the last letter of the previous word."))
        print(gett("You can't use the same word twice, and you can't end with ん"))
        print(gett("Have fun!"))

    elif inp == gett("quit"):
        os.system('clear')
        print(gett("Bye! Play later :D"))
        quit()