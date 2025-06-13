# 🧠 โจทย์: Word Ladder Transformation
# ให้เขียนฟังก์ชัน ladder_length(begin_word, end_word, word_list)
# ที่หาความยาวของการแปลงคำจาก begin_word ไปเป็น end_word โดยเปลี่ยนครั้งละ 1 ตัวอักษร และแต่ละครั้งที่เปลี่ยนต้องเป็นคำที่มีอยู่ใน word_list เท่านั้น

# กฎการแปลง:

# เปลี่ยนได้ครั้งละ 1 ตัวอักษร

# แต่ละคำที่เปลี่ยนต้องอยู่ใน word_list

# ต้องหาทางที่ "สั้นที่สุด" ในการเปลี่ยนจาก begin_word → end_word

# หากไม่สามารถแปลงได้ให้ return 0

from collections import deque

def ladder_length(begin_word, end_word, word_list):
    word_set = set(word_list)  # แปลงเป็น set เพื่อให้ค้นหาคำได้เร็ว
    if end_word not in word_set:
        return 0  # ถ้า end_word ไม่มีใน list ก็ไปไม่ถึงแน่นอน

    queue = deque()
    queue.append((begin_word, 1))  # เริ่มต้นที่ begin_word กับจำนวนก้าว = 1
    visited = set()  # เก็บคำที่เคยไปแล้ว จะได้ไม่วนลูป

    while queue:
        current_word, steps = queue.popleft()

        if current_word == end_word:
            return steps  # ถึงแล้ว ก็ return จำนวนก้าวได้เลย

        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                # ลองเปลี่ยนทีละตัวอักษรในตำแหน่ง i
                next_word = current_word[:i] + c + current_word[i+1:]
                
                # ถ้าเป็นคำที่อยู่ใน word_set และยังไม่เคยไป
                if next_word in word_set and next_word not in visited:
                    queue.append((next_word, steps + 1))  # ใส่เข้าคิวพร้อมบวกขั้น
                    visited.add(next_word)  # กันไม่ให้วนมาอีก

    return 0  # ถ้าหมดคิวแล้วไม่เจอคำปลายทาง ก็ไปไม่ถึง

begin = "hit"
end = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(ladder_length(begin, end, words))
