#1 SHA512_BruteForce  
Brute force 방식으로 hash 값(앞 3byte: 000) 찾기  
-> for문으로 통해 0 - 2^24-1 까지 탐색  

#2 HMAC_Integrity  
- [2.a] HMAC 생성  
  - 1. 사용자로부터 key 입력 받기  
  - 2. txt 파일 내용 읽기  
  - 3. key + message -> HMAC 생성  
  - 4. 새로운 txt 파일(H.txt)에 (원문 메세지 + HMAC) 저장  

- [2.b] HMAC 계산 -> 무결성 확인   
  - 1. 사용자로부터 key 입력 받기  
  - 2. H.txt 파일에서 (원문 메세지 + HMAC) 읽기  
  - 3. key로 메세지 HMAC 계산하기  
  - 4. 읽은 HMAC과 계산한 HMAC 비교 -> 같으면 "OK", 다르면 "NOK"  
