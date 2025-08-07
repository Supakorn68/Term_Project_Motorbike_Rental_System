def sort_words_in_sentence(sentence):
    # แยกประโยคออกเป็นคำๆ
    words = sentence.split()
    
    # เรียงลำดับคำตามตัวอักษร โดยไม่คำนึงถึงตัวพิมพ์เล็ก-ใหญ่
    words.sort(key=str.lower)
    
    # นำคำที่เรียงแล้วมารวมกันเป็นประโยค โดยคั่นด้วยช่องว่าง
    sorted_sentence = ' '.join(words)
    
    # ส่งคืนประโยคที่เรียงแล้ว
    return sorted_sentence

# ตัวอย่างการใช้งาน
sentence = "This is a man world"
sorted_result = sort_words_in_sentence(sentence)

# ผลลัพธ์ที่คาดหวังคือ 'a is man This world'
print("Sorted sentence:", sorted_result)