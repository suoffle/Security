Root CA, 중간 CA, 사용자 인증서를 생성하고, 인증서 체인을 확인.

- Root CA 생성
  ```
  1. Root CA 개인키 생성
  2. Self Sign -> Root CA 인증서 생성
  ```
- 중간 CA 생성
  ```
  1. 중간 CA 개인키 생성
  2. 중간 CA 인증서 발급 요청
  3. Root CA로 중간 CA 인증서 서명
  ```
- 사용자 인증서 생성
  ```
  1. 사용자 개인키 생성
  2. 사용자 인증서 발급 요청
  3. 중간 CA로 사용자 인증서 서명
  ```
- 인증서 체인 검증
  ```
  1. Root CA 인증서 '/usr/local/share/ca-certificates'에 추가
  2. sudo update-ca-certificates로 실제 시스템이 신뢰하는 인증서로 등록
  3. 'openssl verify -show_chain -untrusted'로 인증서 체인 확인
  ```
