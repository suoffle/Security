### #1 실습 환경
- OS: VMware-Ubuntu
- Firewall: UFW

### #2 실습 목적
- 방화벽 규칙의 우선순위에 따른 동작 여부 확인
- 백그라운드에서 실시간으로 실행되는 네트워크 트래픽 감시 확인
```
SNORT RULE
[1 처리방법] [2 프로토콜] [3 송신 IP] [4 송신 Port] [5 패킷 방향] [6 수신 IP] [7 수신 Port] [8 옵션]
```
### #3 실습 과정
  ```
  1. ufw reset
  2. ufw enable
  3. ufw deny 21
  4. ufw insert 1 allow ftp
  5. ufw status numbered
  ```
### #4 결과
- ufw deny 21 -> 21번 TCP 포트(FTP 기본 포트)
- 룰 번호가 작을 수록 우선순위가 높다. (위에서 아래 순서로 규칙을 검사한다.)
- IPv4와 IPv6 규칙은 별도로 존재하며, 환경 설정에서 IPv6이 활성화되어 있으면, 하나의 규칙을 추가해도 IPv4/IPv6이 동시에 추가된다.
