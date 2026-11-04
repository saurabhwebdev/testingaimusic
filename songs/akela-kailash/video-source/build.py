import subprocess, os, sys
S=sys.argv[1]; REPO="/home/user/testingaimusic/songs/akela-kailash"
I=S+"/imgs/"
img={1:"Deity_meditating_on_snowy_peak_967951e8.jpg",2:"Shiva_weeping_with_freezing_tear_9c2f23ee.jpg",
3:"Ganga_flowing_from_Shiva's_hair_1397ce08.jpg",4:"Deity_reaching_through_glowing_f#U2026_ec13e38e.jpg",
5:"Lord_Shiva_carrying_body_cd8ecff0.jpg",6:"Shiva_performing_cosmic_Tandav_d#U2026_c86b93e3.jpg",
7:"Shiva_meditating_and_Parvati_loo#U2026_53cf6791.jpg"}
DUR=258.31; FPS=30
# (image, start, end, zoom direction)
shots=[(1,0,26.5,"in"),(2,26.5,54,"out"),(3,54,68.3,"in"),(4,68.3,95,"out"),(3,95,110.3,"out"),
(5,110.3,136.9,"in"),(1,136.9,166,"out"),(6,166,198.7,"in"),(7,198.7,232.8,"out"),(1,232.8,DUR,"in")]
X=1.0  # crossfade seconds
clips=[]
for k,(n,a,b,d) in enumerate(shots):
    L=b-a+(X if k<len(shots)-1 else 0); fr=int(round(L*FPS)); out=f"c{k}.mp4"; clips.append((out,L))
    z = f"1+0.12*on/{fr}" if d=="in" else f"1.12-0.12*on/{fr}"
    vf=(f"scale=3840:-2,crop=3840:2144,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1920x1080:fps={FPS},"
        "eq=contrast=1.04:saturation=1.05,vignette=PI/5,format=yuv420p")
    if not os.path.exists(out):
        subprocess.run(["ffmpeg","-v","error","-y","-loop","1","-i",I+img[n],"-vf",vf,"-frames:v",str(fr),"-c:v","libx264","-preset","medium","-crf","18",out],check=True)
    print("clip",k,flush=True)
# chain xfades
inp=[];fc=[];off=0;prev="0:v"
for i,(c,L) in enumerate(clips): inp+=["-i",c]
for i in range(1,len(clips)):
    off+=clips[i-1][1]-X
    lab=f"v{i}"; fc.append(f"[{prev}][{i}:v]xfade=transition=fade:duration={X}:offset={off:.3f}[{lab}]"); prev=lab
fc.append(f"[{prev}]fade=t=in:st=0:d=2,fade=t=out:st={DUR-3}:d=3,ass=lyrics.ass:fontsdir={S}/fonts[vout]")
subprocess.run(["ffmpeg","-v","error","-y",*inp,"-i",REPO+"/akela-kailash.mp3","-filter_complex",";".join(fc),
 "-map","[vout]","-map",f"{len(clips)}:a","-c:v","libx264","-preset","slow","-crf","22","-pix_fmt","yuv420p",
 "-c:a","aac","-b:a","256k","-af",f"afade=t=out:st={DUR-3}:d=3","-t",str(DUR),"-movflags","+faststart",S+"/akela-kailash.mp4"],check=True)
print("done")
