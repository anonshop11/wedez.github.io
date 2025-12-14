const audio = document.getElementById('background-music');

// ตั้งค่าระดับเสียง
audio.volume = 0.2; 

// ฟังก์ชันที่พยายามเล่นเพลง
function attemptAutoplay() {
    audio.play().catch(error => {
        // หากเล่นไม่ได้ ให้รอการโต้ตอบจากผู้ใช้
        console.log("Autoplay ถูกบล็อก: รอการคลิก/สัมผัสครั้งแรกจากผู้ใช้...");
    });
    // เมื่อพยายามเล่นแล้ว ให้ลบ Event Listener ออกเพื่อไม่ให้ทำงานซ้ำ
    document.removeEventListener('click', attemptAutoplay);
    document.removeEventListener('touchstart', attemptAutoplay);
}

// 1. ลองพยายามเล่นทันทีเมื่อหน้าเว็บโหลด
attemptAutoplay(); 

// 2. หากยังไม่เล่น: ดักจับการโต้ตอบแรกของผู้ใช้ (คลิก หรือ สัมผัส)
document.addEventListener('click', attemptAutoplay);
document.addEventListener('touchstart', attemptAutoplay);