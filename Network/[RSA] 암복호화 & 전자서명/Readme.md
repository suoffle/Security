#1 RSA 암복호화  
- [a-1] RSA 키 생성(PEM)  
  ```
  1. 공개키 / 개인키 생성 및 저장  
  2. 개인키: Alice_private.pem  
  3. 공개키: Alice_public.pem
  ```
- [a-2] 암호화
  ```
  1. 공개키 읽기    
  2. '1.txt' 파일 공개키로 암호화 -> 'enc.txt'로 저장
  ```
- [a-3] 복호화  
  ```
  1. passphrase 입력 받기  
  2. 개인키 읽기  
  3. enc.txt에서 암호문 읽기  
  4. RSA OAEP 방식으로 복호화 -> 원문 출력  
  ```
#2 RSA 전자서명 및 무결성 확인  
- [b-1] 전자서명 생성  
  ```
  1. key: RSA 2048bit 키 쌍 생성  
  2. key에서 공개키를 추출해 DER 형식으로 저장 -> public.der  
  3. '1.txt' 파일 내용 읽기  
  4. 읽은 파일 SHA 해시 생성  
  5. RSA PKCS1_PSS 방식으로 해시값에 전자서명 생성  
  6. (원문 메세지 + base64 encoding 전자서명) 저장 -> 'sig.txt'
  ```
- [b-2] 전자서명 무결성 확인
  ```
  1. public.der에서 공개키 추출  
  2. '1.txt' 원문 파일 내용 읽기  
  3. 'sig.txt'에서 내용과 서명 읽기 및 분리  
  4. 서명 decoding(base64)  
  5. 원문 파일 내용(1.txt) SHA 해시값 생성  
  6. 공개키로 RSA PSS 서명 검증
  ```
