import qrcode 


student_id = input("학번을 입력하세요: ")
name = input("이름을 입력하세요: ")
major = input("전공을 입력하세요: ")

qr_data =  (student_id,name,major)
qr_img = qrcode.make(qr_data)

save_path='qr_data.png'
qr_img.save(save_path)

