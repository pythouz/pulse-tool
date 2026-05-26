import yt_dlp
import sys
import os

def run_download_tool(url):
    # المجلد المخصص للتحميل داخل الحاوية
    save_path = "/home/pulseuser"
    
    # رسالة تعريفية للـ Debug للتأكد أن هذا هو الملف الجديد
    print(f"--- [PULSE-DEBUG] النسخة الجديدة تعمل الآن (main.py) ---", flush=True)
    print(f"--- [PulseEngine] بدء معالجة الرابط: {url} ---", flush=True)

    # خيارات التحميل
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'quiet': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # التأكد المحاسبي من وجود الملفات
        files = os.listdir(save_path)
        print(f"--- [PulseEngine] تم التحميل بنجاح. المحتويات الحالية: {files} ---", flush=True)
        
    except Exception as e:
        print(f"--- [PulseEngine] خطأ أثناء التشغيل: {str(e)} ---", flush=True)

if __name__ == "__main__":
    # استلام الرابط من الـ Arguments المرسلة من النظام
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        run_download_tool(video_url)
    else:
        print("--- [PulseEngine] خطأ: لم يتم استلام رابط الفيديو. ---", flush=True)
