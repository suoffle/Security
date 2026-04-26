#1 Ping of Death
- hping3를 이용해 크기가 큰 ICMP 패킷을 만들어 전송하고, 이를 wireshark를 통해 확인.
- local 환경에서 실습
- sudo hping3 --icmp --rand-source [Host IP] -d 65000
  - source ip는 분산 공격 트래픽처럼 설정하기 위해 rand-source 사용.
  - 데이터 패킷은 65,000 bytes의 큰 값을 설정하여 framgentation 되도록 설정.

### Wireshark 확인 결과
  - 동일한 패킷 길이 반복(1402 bytes): Fragmentation에 의해 여러 조각으로 ICMP DATA가 분할되어 전송되는 것을 확인할 수 있었다.
    ```
    1. Frame Length: 1402 Bytes
    2. Ethernet Header: 14 bytes
    3. IP Total Length: 1388 bytes
    4. IP Header Length: 20 bytes
    5. ICMP Header: 8 bytes
    6. Data: 65000 bytes
    => Ethernet Header(14) + IP Header(20) + ICMP Header(8) + ICMP Data(1360) = 1402 bytes
    ```
  - 65000 bytes에 8bytes가 추가된 것은 ICMP Header인 것으로 판단된다.










  
