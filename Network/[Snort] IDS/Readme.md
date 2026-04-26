### 실습 목표
- Snort를 이용해 네트워크 트래픽을 감시하고 등록된 룰 검사
- FTP 트래픽 중 21번 포트로 들어오는 패킷 중 "lsa" 문자열이 포함된 경우를 탐지
- snort 실행 과정: snort.conf -> 룰이 적혀있는 파일들을 호출 -> 룰 실행

### 실습 과정
  ```
  1. /etc/snort/snort.conf 파일에 $RULE_PATH/local.rules 파일 추가(include)
  2. /etc/snort/rules/local.rules 파일에 FTP 탐지 룰 등록
    - $ alert tcp any any -> any 21 (msg:"FTP"; content:"lsa"; sid:1000003;)
  3. vsftpd(ftp 데몬) 설치 및 실행.
  4. 윈도우에서 ftp로 연결 후 "lsa" 입력
  5. Snort가 해당 접속의 패킷에서 "lsa" 탐지 -> alert 출력
  ```
