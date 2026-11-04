L=[
(17.0,26.3,"हम्म… हर हर… महादेव…","Hmm… Har Har… Mahadev…"),
(26.4,33.6,"बर्फ़ों पे बैठा है जोगी, आँखों में जलती आग","Barfon pe baitha hai jogi, aankhon mein jalti aag"),
(33.6,40.4,"डमरू भी चुप है अब तो, सोया है सारा राग","Damru bhi chup hai ab toh, soya hai saara raag"),
(40.4,47.6,"भस्म लगी है तन पे, पर मन पे लगी है राख","Bhasm lagi hai tan pe, par man pe lagi hai raakh"),
(47.6,54.0,"सती बिन सूनी-सूनी, कैलाश की हर शाख","Sati bin sooni-sooni, Kailash ki har shaakh"),
(54.0,61.4,"गंगा भी रोती जटा में, चंदा भी है उदास","Ganga bhi roti jata mein, chanda bhi hai udaas"),
(61.4,68.2,"तीनों लोक का स्वामी, आज खड़ा है निराश","Teenon lok ka swami, aaj khada hai niraash"),
(68.3,74.8,"सती… सती… मेरी सती","Sati… Sati… meri Sati"),
(74.9,82.0,"तुझ बिन अधूरा है ये शिव, तू ही मेरी शक्ति","Tujh bin adhoora hai ye Shiv, tu hi meri Shakti"),
(82.0,88.4,"भोले का दिल भी टूटे, रोए ये कैलाश","Bhole ka dil bhi toote, roye ye Kailash"),
(88.5,96.0,"महादेव अकेला है, बस यादें हैं पास","Mahadev akela hai, bas yaadein hain paas"),
(110.3,116.4,"यज्ञ की आग में जलकर, तूने निभाई रीत","Yagya ki aag mein jalkar, tune nibhaai reet"),
(116.4,123.0,"अपमान सहा ना मेरा, ऐसी थी तेरी प्रीत","Apmaan saha na mera, aisi thi teri preet"),
(123.0,130.5,"कंधे पे लेके तुझको, मैं घूमा सारा जहान","Kandhe pe leke tujhko, main ghooma saara jahaan"),
(130.5,136.8,"हर क़दम पे तांडव था, हर साँस में तूफ़ान","Har qadam pe taandav tha, har saans mein toofaan"),
(136.9,143.6,"सती… सती… मेरी सती","Sati… Sati… meri Sati"),
(143.7,150.4,"तुझ बिन अधूरा है ये शिव, तू ही मेरी शक्ति","Tujh bin adhoora hai ye Shiv, tu hi meri Shakti"),
(150.5,157.2,"भोले का दिल भी टूटे, रोए ये कैलाश","Bhole ka dil bhi toote, roye ye Kailash"),
(157.3,166.0,"महादेव अकेला है, बस यादें हैं पास","Mahadev akela hai, bas yaadein hain paas"),
(177.6,185.2,"ना त्रिशूल उठता है, ना नैना खुलते हैं","Na trishool uthta hai, na naina khulte hain"),
(185.3,191.9,"तेरी याद के दीपक, बस भीतर जलते हैं","Teri yaad ke deepak, bas bheetar jalte hain"),
(192.0,198.6,"फिर भी राह तकूँगा, जनम-जनम मैं जोगी","Phir bhi raah takoonga, janam-janam main jogi"),
(198.7,205.4,"लौटेगी तू पार्वती बन, फिर से मेरी होगी","Lautegi tu Parvati ban, phir se meri hogi"),
(205.5,212.3,"सती… सती… मेरी सती","Sati… Sati… meri Sati"),
(212.4,218.7,"तुझ बिन अधूरा है ये शिव, तू ही मेरी शक्ति","Tujh bin adhoora hai ye Shiv, tu hi meri Shakti"),
(218.8,225.6,"भोले का दिल भी टूटे, रोए ये कैलाश","Bhole ka dil bhi toote, roye ye Kailash"),
(225.7,232.7,"महादेव अकेला है, पर बाक़ी है आस","Mahadev akela hai, par baaqi hai aas"),
(232.8,246.7,"हर हर… महादेव…","Har Har… Mahadev…"),
(246.8,253.0,"सती…","Sati…"),
]
def t(s):
    h=int(s//3600);m=int(s%3600//60);x=s%60;return f"{h}:{m:02d}:{x:05.2f}"
def srt(s):
    ms=int(round(s*1000));return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"
hdr="""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hi,Noto Serif Devanagari SemiBold,76,&H00F2F6FF,&H000000FF,&H00140A00,&H96000000,0,0,0,0,100,100,0,0,1,3,3,2,80,80,135,1
Style: En,DejaVu Sans,36,&H00A8D8FF,&H000000FF,&H00140A00,&H96000000,0,1,0,0,100,100,1,0,1,2,2,2,80,80,78,1
Style: Title,Noto Serif Devanagari SemiBold,150,&H00F2F6FF,&H000000FF,&H00140A00,&H96000000,0,0,0,0,100,100,0,0,1,4,5,5,80,80,0,1
Style: Sub,DejaVu Sans,44,&H00A8D8FF,&H000000FF,&H00140A00,&H96000000,0,0,0,0,100,100,6,0,1,2,3,5,80,80,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev=[]
ev.append(f"Dialogue: 0,{t(2.5)},{t(14.5)},Title,,0,0,0,,{{\\fad(1500,1500)\\pos(960,470)}}अकेला कैलाश")
ev.append(f"Dialogue: 0,{t(3.5)},{t(14.5)},Sub,,0,0,0,,{{\\fad(1500,1500)\\pos(960,610)}}AKELA KAILASH  •  SHIV BHAJAN")
for a,b,h,e in L:
    ev.append(f"Dialogue: 0,{t(a)},{t(b)},Hi,,0,0,0,,{{\\fad(400,400)}}{h}")
    ev.append(f"Dialogue: 0,{t(a)},{t(b)},En,,0,0,0,,{{\\fad(400,400)}}{e}")
open("lyrics.ass","w").write(hdr+"\n".join(ev)+"\n")
with open("/home/user/testingaimusic/songs/akela-kailash/akela-kailash.hi.srt","w") as f:
    for i,(a,b,h,e) in enumerate(L,1): f.write(f"{i}\n{srt(a)} --> {srt(b)}\n{h}\n\n")
with open("/home/user/testingaimusic/songs/akela-kailash/akela-kailash.hi-Latn.srt","w") as f:
    for i,(a,b,h,e) in enumerate(L,1): f.write(f"{i}\n{srt(a)} --> {srt(b)}\n{e}\n\n")
