from pytube import YouTube
import os

def download_audio(url, output_path='.'):
    """
    ดาวน์โหลดเฉพาะเสียงจากวิดีโอ YouTube และเปลี่ยนชื่อเป็น .mp3.
    
    :param url: URL ของวิดีโอ YouTube
    :param output_path: พาธที่จะบันทึกไฟล์ (ค่าเริ่มต้นคือโฟลเดอร์ปัจจุบัน)
    """
    try:
        # สร้างออบเจกต์ YouTube
        yt = YouTube(https://www.youtube.com/watch?v=g3F-nzc0Vdc&list=RDg3F-nzc0Vdc&start_radio=1)
        
        # กรองและเลือกเฉพาะสตรีมเสียงที่มีบิตเรตสูงสุด
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        
        if not audio_stream:
            print("❌ ไม่พบสตรีมเสียงที่เหมาะสม")
            return
            
        print(f"กำลังดาวน์โหลดเสียง: {yt.title} (บิตเรต: {audio_stream.abr})")

        # ดาวน์โหลดไฟล์เสียง
        out_file = audio_stream.download(output_path=output_path)
        
        # เปลี่ยนชื่อไฟล์ให้เป็น .mp3
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        
        # ตรวจสอบว่าไฟล์เดิมมีอยู่หรือไม่ก่อนเปลี่ยนชื่อ
        if os.path.exists(out_file):
            os.rename(out_file, new_file)
            print(f"✅ ดาวน์โหลดเสียงสำเร็จและเปลี่ยนชื่อเป็น: {os.path.basename(new_file)}")
        else:
            print("❌ เกิดข้อผิดพลาดในการบันทึกไฟล์")

    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการดาวน์โหลด: {e}")

# --- การใช้งาน ---
youtube_url = input("กรุณาป้อน URL ของวิดีโอ YouTube: ")
download_audio(youtube_url)