# -*- coding: utf-8 -*-

import pyaudio
import viVoicecloud as vv
from sjtu.audio import findDevice
import re

device_in = findDevice("ac108","input")
Sample_channels = 1  
Sample_rate = 16000  
Sample_width = 2         
time_seconds = 0.5
p = pyaudio.PyAudio()
stream = p.open(
            rate=Sample_rate,
            format=p.get_format_from_width(Sample_width),
            channels=Sample_channels,
            input=True,
            input_device_index=device_in,
            start=False)

vv.Login()
ASR=vv.asr()

while True:
    try:
        import pyaudio
        import viVoicecloud as vv
        from sjtu.audio import findDevice

        device_in = findDevice("ac108","input")
        Sample_channels = 1  
        Sample_rate = 16000  
        Sample_width = 2         
        time_seconds = 0.5  #录音片段的时长，建议设为0.2-0.5秒

        p = pyaudio.PyAudio()
        stream = p.open(
                    rate=Sample_rate,
                    format=p.get_format_from_width(Sample_width),
                    channels=Sample_channels,
                    input=True,
                    input_device_index=device_in,
                    start = False)

        ASR=vv.asr()#实例化
        ASR.SessionBegin(language='Chinese')#开始语音识别
        stream.start_stream()
        print ('***Listening...')

        #录音并上传到讯飞，当判定一句话已经结束时，status返回3
        status=0
        while status!=3:
            frames=stream.read(int(Sample_rate*time_seconds))
            ret,status,recStatus=ASR.AudioWrite(frames)
        stream.stop_stream()
        print ('---GetResult...')
            
        text1=ASR.GetResult()#获取结果
        ASR.SessionEnd()#结束语音识别
        print (text1)
        temp=re.match("[盘潘判盼攀畔磐叛泮槃][盐眼演烟延岩燕严研]",text1)
        if temp!=None:
            break 
    except Exception as e:
        print(e)
        print('stopped')
        vv.Logout()
        stream.close()
        break

temp=re.match("[\u4E00-\u9FA5]*音乐",text1)

if temp!=None:
    print("进入播放音乐模式")
    #!/usr/bin/python3
    # -*- coding: utf-8 -*-

    import viVoicecloud as vv  #导入模块

    t = vv.tts() #实例化

    t.say(text="你要英文还是中文？",voice="xiaofeng")
    while True:
        # -*- coding: utf-8 -*-
        import pyaudio
        import viVoicecloud as vv
        from sjtu.audio import findDevice

        device_in = findDevice("ac108","input")
        Sample_channels = 1  
        Sample_rate = 16000  
        Sample_width = 2         
        time_seconds = 0.5  #录音片段的时长，建议设为0.2-0.5秒

        p = pyaudio.PyAudio()
        stream = p.open(
                    rate=Sample_rate,
                    format=p.get_format_from_width(Sample_width),
                    channels=Sample_channels,
                    input=True,
                    input_device_index=device_in,
                    start = False)

        ASR=vv.asr()#实例化
        ASR.SessionBegin(language='Chinese')#开始语音识别
        stream.start_stream()
        print ('***Listening...')

        #录音并上传到讯飞，当判定一句话已经结束时，status返回3
        status=0
        while status!=3:
            frames=stream.read(int(Sample_rate*time_seconds))
            ret,status,recStatus=ASR.AudioWrite(frames)
        stream.stop_stream()
        print ('---GetResult...')
            
        lang=ASR.GetResult()#获取结果
        ASR.SessionEnd()#结束语音识别
        print (lang)
        temp=re.match("[\u4E00-\u9FA5]*[英|中]",lang)
        if temp!= False:
            break

    # -*- coding: utf-8 -*-
    temp=re.match("[\u4E00-\u9FA5]*英文",lang)
    if temp!=None:
        # -*- coding: utf-8 -*-
        import pyaudio
        import viVoicecloud as vv
        from sjtu.audio import findDevice



        device_in = findDevice("ac108","input")
        Sample_channels = 1  
        Sample_rate = 16000  
        Sample_width = 2         
        time_seconds = 0.5  #录音片段的时长，建议设为0.2-0.5秒

        p = pyaudio.PyAudio()
        stream = p.open(
                    rate=Sample_rate,
                    format=p.get_format_from_width(Sample_width),
                    channels=Sample_channels,
                    input=True,
                    input_device_index=device_in,
                    start = False)

        ASR=vv.asr()#实例化
        ASR.SessionBegin(language='English')#开始语音识别
        stream.start_stream()
        print ('***Listening...')

        #录音并上传到讯飞，当判定一句话已经结束时，status返回3
        status=0
        while status!=3:
            frames=stream.read(int(Sample_rate*time_seconds))
            ret,status,recStatus=ASR.AudioWrite(frames)
        stream.stop_stream()
        print ('---GetResult...')
            
        enmu=ASR.GetResult()#获取结果
        ASR.SessionEnd()#结束语音识别
        print (enmu)
        
        enmu=enmu.strip(".")

        #!/usr/bin/python3
        # -*- coding: utf-8 -*-

        #第一步：检索歌曲
        import urllib
        import urllib.request

        url = "http://tingapi.ting.baidu.com/v1/restserver/ting?"
        url += "from=webapp_music"
        url += "&method=baidu.ting.search.catalogSug"
        url += "&format=json"

        keywords = enmu
        keywords_encoded = urllib.parse.quote(keywords) #转成urlcode编码
        print(keywords_encoded)

        url += "&query="+keywords_encoded

        ref = urllib.request.urlopen(url)

        result = ref.read()
        print (result)


        #第二步：获取链接

        import json
        dict1 = json.loads(str(result,encoding='utf-8'))
        #print(dict1)
        songid = dict1["song"][0]["songid"]

        url2 = "http://music.taihe.com/data/music/fmlink?"
        url2 += "songIds="+songid

        ref2 = urllib.request.urlopen(url2)
        result2 = ref2.read()
        #print (result2)

        dict2 = json.loads(str(result2,encoding='utf-8'))
        #print(dict2)
        songLink = dict2["data"]["songList"][0]["songLink"]
        #print(songLink)

        #第三步：下载或播放

        #urllib.request.urlretrieve(songLink,"myMusic.mp3")  #下载

        import vlc
        p = vlc.MediaPlayer(songLink)
        p.play()                                            #直接播放

        import time
        time.sleep(2)

        while p.is_playing():                        #每隔0.5秒循环一次，直到音乐播放结束
            time.sleep(0.5)       

    temp=re.matchtemp=re.match("[\u4E00-\u9FA5]*中文",lang)
    if temp!=None:

        # -*- coding: utf-8 -*-
        import pyaudio
        import viVoicecloud as vv
        from sjtu.audio import findDevice

        device_in = findDevice("ac108","input")
        Sample_channels = 1  
        Sample_rate = 16000  
        Sample_width = 2         
        time_seconds = 0.5  #录音片段的时长，建议设为0.2-0.5秒

        p = pyaudio.PyAudio()
        stream = p.open(
                    rate=Sample_rate,
                    format=p.get_format_from_width(Sample_width),
                    channels=Sample_channels,
                    input=True,
                    input_device_index=device_in,
                    start = False)


        ASR=vv.asr()#实例化
        ASR.SessionBegin(language='Chinese')#开始语音识别
        stream.start_stream()
        print ('***Listening...')

        #录音并上传到讯飞，当判定一句话已经结束时，status返回3
        status=0
        while status!=3:
            frames=stream.read(int(Sample_rate*time_seconds))
            ret,status,recStatus=ASR.AudioWrite(frames)
        stream.stop_stream()
        print ('---GetResult...')
            
        enmu=ASR.GetResult()#获取结果
        ASR.SessionEnd()#结束语音识别
        print (enmu)
        enmu=enmu.strip("。")
        #!/usr/bin/python3
        # -*- coding: utf-8 -*-

        #第一步：检索歌曲
        import urllib
        import urllib.request

        url = "http://tingapi.ting.baidu.com/v1/restserver/ting?"
        url += "from=webapp_music"
        url += "&method=baidu.ting.search.catalogSug"
        url += "&format=json"

        keywords = enmu
        keywords_encoded = urllib.parse.quote(keywords) #转成urlcode编码
        print(keywords_encoded)

        url += "&query="+keywords_encoded

        ref = urllib.request.urlopen(url)

        result = ref.read()
        print (result)


        #第二步：获取链接

        import json
        dict1 = json.loads(str(result,encoding='utf-8'))
        #print(dict1)
        songid = dict1["song"][0]["songid"]

        url2 = "http://music.taihe.com/data/music/fmlink?"
        url2 += "songIds="+songid

        ref2 = urllib.request.urlopen(url2)
        result2 = ref2.read()
        #print (result2)

        dict2 = json.loads(str(result2,encoding='utf-8'))
        #print(dict2)
        songLink = dict2["data"]["songList"][0]["songLink"]
        #print(songLink)

        #第三步：下载或播放

        #urllib.request.urlretrieve(songLink,"myMusic.mp3")  #下载

        import vlc
        p = vlc.MediaPlayer(songLink)
        p.play()                                            #直接播放

        import time
        time.sleep(2)

        while p.is_playing():                        #每隔0.5秒循环一次，直到音乐播放结束
            time.sleep(0.5)       
temp=re.matchtemp=re.match("[\u4E00-\u9FA5]*聊天",text1)
if temp!=None:
    time_seconds = 0.5
    p = pyaudio.PyAudio()
    stream = p.open(
                rate=Sample_rate,
                format=p.get_format_from_width(Sample_width),
                channels=Sample_channels,
                input=True,
                input_device_index=device_in,
                start=False)

    ASR=vv.asr()

    while True:
        try:
            ASR.SessionBegin(language='Chinese')
            stream.start_stream()
            print ('***Listening...')
            status=0
            while status!=3:
                frames=stream.read(int(Sample_rate*time_seconds),exception_on_overflow = False)
                ret,status,recStatus=ASR.AudioWrite(frames)
       
            stream.stop_stream()
            print ('---GetResult...')
            qa=ASR.GetResult()
            ASR.SessionEnd()
            print (qa)
            import viVoicecloud as vv
            from sjtu.answer import aiui_answer,my_answer
            t = vv.tts()  
            q = qa
            if q=="exit":
                break
            else: 
                if not my_answer(q,t):
                    aiui_answer(q,vv,t)
            
            
        except Exception as e:
            print(e)
            print('stopped')
            vv.Logout()
            stream.close()
            break

temp=re.match("[\u4E00-\u9FA5]*[转|赚|转|砖|篆]",text1)
if temp!=None:
    print("进入语音转换")
    # -*- coding: utf-8 -*-

    import pyaudio
    import viVoicecloud as vv
    from sjtu.audio import findDevice

    device_in = findDevice("ac108","input")
    Sample_channels = 1  
    Sample_rate = 16000  
    Sample_width = 2         
    time_seconds = 0.5
    p = pyaudio.PyAudio()
    stream = p.open(
                rate=Sample_rate,
                format=p.get_format_from_width(Sample_width),
                channels=Sample_channels,
                input=True,
                input_device_index=device_in,
                start=False)

    ASR=vv.asr()

    while True:
        try:
            ASR.SessionBegin(language='Chinese')
            stream.start_stream()
            print ('***Listening...')
            status=0
            while status!=3:
                frames=stream.read(int(Sample_rate*time_seconds),exception_on_overflow = False)
                ret,status,recStatus=ASR.AudioWrite(frames)
       
            stream.stop_stream()
            print ('---GetResult...')
            words=ASR.GetResult()
            ASR.SessionEnd()
            print (words)
            
        except Exception as e:
            print(e)
            print('stopped')
            vv.Logout()
            stream.close()
            p.terminate()
            break
temp=re.match("[\u4E00-\u9FA5]*翻译",text1)
if temp!=None:
    print("开始翻译")
    #!/usr/bin/python3
    # -*- coding: utf-8 -*-

    import viVoicecloud as vv  #导入模块

    t = vv.tts() #实例化

    t.say(text="你是要翻译成英文还是翻译成中文",voice="xiaomeng")

    # -*- coding: utf-8 -*-
    import pyaudio
    import viVoicecloud as vv
    from sjtu.audio import findDevice

    device_in = findDevice("ac108","input")
    Sample_channels = 1  
    Sample_rate = 16000  
    Sample_width = 2         
    time_seconds = 0.5  #录音片段的时长，建议设为0.2-0.5秒

    p = pyaudio.PyAudio()
    stream = p.open(
                rate=Sample_rate,
                format=p.get_format_from_width(Sample_width),
                channels=Sample_channels,
                input=True,
                input_device_index=device_in,
                start = False)

    ASR=vv.asr()#实例化
    ASR.SessionBegin(language='Chinese')#开始语音识别
    stream.start_stream()
    print ('***Listening...')

    #录音并上传到讯飞，当判定一句话已经结束时，status返回3
    status=0
    while status!=3:
        frames=stream.read(int(Sample_rate*time_seconds))
        ret,status,recStatus=ASR.AudioWrite(frames)
    stream.stop_stream()
    print ('---GetResult...')
        
    lang1=ASR.GetResult()#获取结果
    ASR.SessionEnd()#结束语音识别
    print (lang1)

    temp=re.matchtemp=re.match("[\u4E00-\u9FA5]*英文",lang1)
    if temp!=None:
        # -*- coding: utf-8 -*-

        import pyaudio
        import viVoicecloud as vv
        from sjtu.audio import findDevice

        device_in = findDevice("ac108","input")
        Sample_channels = 1  
        Sample_rate = 16000  
        Sample_width = 2         
        time_seconds = 0.5
        p = pyaudio.PyAudio()
        stream = p.open(
                    rate=Sample_rate,
                    format=p.get_format_from_width(Sample_width),
                    channels=Sample_channels,
                    input=True,
                    input_device_index=device_in,
                    start=False)

        ASR=vv.asr()

        while True:
            try:
                ASR.SessionBegin(language='Chinese')
                stream.start_stream()
                print ('***Listening...')
                status=0
                while status!=3:
                    frames=stream.read(int(Sample_rate*time_seconds),exception_on_overflow = False)
                    ret,status,recStatus=ASR.AudioWrite(frames)
           
                stream.stop_stream()
                print ('---GetResult...')
                lang2=ASR.GetResult()
                ASR.SessionEnd()
                print (lang2)
                
                import viVoicecloud as vv
                tr = vv.baidu_translate()
                result = tr.translate(lang2,"zh","en")
                print(result)
                t = vv.tts() #实例化
                t.say(text=result,voice="henry")
                
            except Exception as e:
                print(e)
                print('stopped')
                vv.Logout()
                stream.close()
                p.terminate()
                break
        
    temp=re.matchtemp=re.match("[\u4E00-\u9FA5]*中文",lang2)
    if temp!=None:
        # -*- coding: utf-8 -*-

        import pyaudio
        import viVoicecloud as vv
        from sjtu.audio import findDevice

        device_in = findDevice("ac108","input")
        Sample_channels = 1  
        Sample_rate = 16000  
        Sample_width = 2         
        time_seconds = 0.5
        p = pyaudio.PyAudio()
        stream = p.open(
                    rate=Sample_rate,
                    format=p.get_format_from_width(Sample_width),
                    channels=Sample_channels,
                    input=True,
                    input_device_index=device_in,
                    start=False)

        ASR=vv.asr()

        while True:
            try:
                ASR.SessionBegin(language='English')
                stream.start_stream()
                print ('***Listening...')
                status=0
                while status!=3:
                    frames=stream.read(int(Sample_rate*time_seconds),exception_on_overflow = False)
                    ret,status,recStatus=ASR.AudioWrite(frames)
           
                stream.stop_stream()
                print ('---GetResult...')
                lang2=ASR.GetResult()
                ASR.SessionEnd()
                print (lang2)
                
                import viVoicecloud as vv
                tr = vv.baidu_translate()
                result = tr.translate( lang2 ,"en","zh")
                print(result)
                t = vv.tts() #实例化
                t.say(text=result,voice="xiaofeng")
                
            except Exception as e:
                print(e)
                print('stopped')
                vv.Logout()
                stream.close()
                p.terminate()
                break




        
    
       







