#1 AES 암호화/복호화  
- 암호 종류: AES(대칭키 암호)    
- Mode: CFB  
- Key: 암호화, 복호화 시 동일하게 사용  
- IV: 암호화, 복호화 시 동일하게 사용  

#2 TXT 파일 복호화
- 암호 종류: AES
- Mode: CBC
- 파일 구조: filesize(4) + Encrypted.txt

#3 TXT 파일 복호화
- 암호 종류: AES
- Mode: CTR
- 파일 구조: filesize(4) + Encrypted.txt
