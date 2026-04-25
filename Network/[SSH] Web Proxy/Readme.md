- Putty SSH Tunnel을 이용한 Web Proxy  
- 브라우저 <-> SSH Client(putty) <-> AWS(SSH 서버) <-> 웹사이트  

</br>

[실행 순서]
1. AWS 인스턴스 생성  
   -> key pair 생성(.ppk)  
   -> 서버 IP 주소 획득  
   
2. Putty SSH tunnel 설정  
   -> AWS 서버 IP 주소를 Host로 저장  
   -> Auth: key pair로 공개키 인증  
   -> SSH Tunnel을 위해 root-framework 설치  
   -> forwarded port는 5000으로 설정  
   
3. SSH 재접속  
   -> 터널링 적용된 상태로 SSH 연결  
 
4. 브라우저 proxy 설정  
   -> 인터넷 속성 -> 연결 -> LAN 설정  
   -> 프록시 서버: localhost / port: 5000  
   
5. 브라우저로 웹사이트 접속  
   -> 브라우저 접속 시 트래픽이 SSH Tunnel을 통해 AWS 서버를 거침.  
   -> 네이버 'ip 주소 확인' 페이지에서 AWS 서버 IP 확인 가능.  
