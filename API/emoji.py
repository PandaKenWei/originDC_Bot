import random

# 假設你有一個表情數據庫，每種類型的表情都存放在一個list中

cute_list = ['(｡･∀･)ﾉﾞ','(⁠◍⁠•⁠ᴗ⁠•⁠◍⁠)','(。’▽’。)♡','✧⁠◝⁠(⁠⁰⁠▿⁠⁰⁠)⁠◜⁠✧','⁽⁠⁽⁠ଘ⁠(⁠ ⁠ˊ⁠ᵕ⁠ˋ⁠ ⁠)⁠ଓ⁠⁾⁠⁾','(⁠づ⁠￣⁠ ⁠³⁠￣⁠)⁠づ','╰⁠(⁠⸝⁠⸝⁠⸝⁠´⁠꒳⁠`⁠⸝⁠⸝⁠⸝⁠)⁠╯','(⁠*⁠ﾉ⁠・⁠ω⁠・⁠)⁠ﾉ⁠♫','(๑´ㅁ`)','(๑´ㅂ`๑)','(⁠◍⁠•⁠ᴗ⁠•⁠◍⁠)⁠❤',
             '(。•ω•。)ノ♡','✧⁠⁠(⁠>⁠o⁠<⁠)⁠ﾉ⁠✧','(✪ω✪)',"(〃'▽'〃)",'(ᗒᗨᗕ)/'," ෆ(  ˶'ᵕ'˶)ෆ  ̖́-"]

angry_list = ['(๑•̀ㅁ•́ฅ)','(๑`^´๑)','๛ก(ｰ̀ωｰ́ก)','(⁠ ⁠≧⁠Д⁠≦⁠)','(。・`ω´・)','ε٩(๑> ₃ <)۶з','٩(๑`^´๑)۶','( ˘•ω•˘ )','(－－〆)','(︶^︶)']

vert_angry_list = ['(⁠┛⁠◉⁠Д⁠◉⁠)⁠┛⁠彡⁠┻⁠━⁠┻','(⁠ﾉ⁠≧⁠∇⁠≦⁠)⁠ﾉ⁠ ⁠ﾐ⁠ ⁠┻⁠━⁠┻','ʕ⁠ノ⁠•⁠ᴥ⁠•⁠ʔ⁠ノ⁠ ⁠︵⁠ ⁠┻⁠━⁠┻','┻⁠━⁠┻⁠ミ⁠＼⁠(⁠≧⁠ﾛ⁠≦⁠＼⁠)']

gogo_list = ['(๑•̀ㅂ•́)و','(⁠~⁠￣⁠³⁠￣⁠)⁠~','٩(ˊᗜˋ*)و','(σ′▽‵)′▽‵)σ','─=≡Σ((( つ•̀ω•́)つ','(๑•̀ㅂ•́)و✧','']

funny_list = ['(´ｰ∀ｰ`)','(◐‿◑)','(°◕ ∀ ◕°)','(„ಡωಡ„）','(⁠●⁠´⁠⌓⁠`⁠●⁠)','(⁠ ⁠˶⁠ ⁠❛⁠ ⁠ꁞ⁠ ⁠❛⁠ ⁠˶⁠ ⁠)','♆(◍` ˘ ´◍)↝','(ﾉ)`ω´(ヾ)','ᕙ⁠(⁠＠⁠°⁠▽⁠°⁠＠⁠)⁠ᕗ'] 

sad_list = ['(இωஇ )','(,,•́ . •̀,,)','(._.)','(๑•́ ₃ •̀๑)']

emoji_database = {
    "cute": cute_list,  
    "angry": angry_list,
    "vert_angry" :vert_angry_list,
    "gogo" :gogo_list,
    "funny" : funny_list,
    "sad" : sad_list
}

def get_emoji(category):
    
    emoji = random.choice(emoji_database[category])
    
    return emoji
