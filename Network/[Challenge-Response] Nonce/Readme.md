HMAC 기반 Challenge-Response (Server-Client 구조)  
- Client가 Server에 id를 전송한 뒤 Server로부터 nonce 값을 받고, 이후 (비밀번호 + nonce)로 HMAC 생성.  
- Server는 저장된 사용자 정보와 생성한 nonce로 HMAC을 계산하여 비교 및 인증.
- 사용자 인증과 메세지 무결성 확인  
  
#1 Server.py   
  ```
  1. 사용자 정보는 딕셔너리 타입으로 미리 저장
  2. TCP 소켓 생성 및 클라이언트 연결
  3. 클라이언트로부터 uid 수신 -> JSON 형식으로 전달된 ID 읽기
  4. nonce 생성(8byte 랜덤값) -> base64 encoding 후 Client에 전송
  5. Client로부터 HMAC 수신 -> base64 decoding
  6. 저장해 둔 비밀번호와 nonce로 HMAC 생성(재계산)
  7. 인증 검증(Client의 HMAC과 계산한 HMAC이 동일한지 확인) 
  ```
#2 Client.py
  ```
  1. 소켓 생성 및 Server에 연결 요청
  2. 사용자의 ID를 입력 받고 Server에 전송(JSON 타입)
  3. Server로부터 nonce 수신(JSON 형식 -> base64 decoding)
  4. 비밀번호를 입력 받고 encoding
  5. (비밀번호 + nonce) HMAC 생성
  6. 계산한 HMAC encoding 후 Server에 전송(JSON 형식)

  ```
