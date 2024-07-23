# Port Fowarding

### 내부에서 개방 포트 번호 확인
// 모든 활성 포트 조회
% netstat -an | grep LISTEN

// 특정 포트 확인
% sudo netstat -lnup | grep :[포트번호]

// 모든 TCP 포트 조회
% netstat -anvp tcp | awk 'NR<3 || /LISTEN/'

// 모든 UDP 포트 조회
% netstat -anvp udp

### 외부에서 개방 여부 확인
  % telnet [IP 주소] [포트 번호]
  % nc -zv [IP 주소] [포트 번호]

<hr>

# U+

## 1. 포트 개방

### 1-1. 포트 번호
- Well Registered Port: 0 ~ 1023 
- Registered Port: 1024 ~ 49151
- Dynamic Port: 449152 ~ 65535

### 1-2. ssh 포트 번호 변경
  % sudo vim /etc/ssh/sshd_config
    #Port 22 -> Port 원하는 번호
  % /etc/init.d/ssh restart

### 1-3. 컴퓨터에 고정 ip 할당 
[reference](https://github.com/choiyun9yu/OperatingSystem/blob/main/Linux/Installation.md)

## 2. 공유기별 관리자 페이지

### 2-1. U+
- 주소: 192.168.219.1
- LGU_0000 [ Click ]
- 비번: 공유기 뒷면 관리자 비밀번호
- 네트워크 설정 Tap [ Click ]
- NAT 설정 [ Click ]
######
- 네트워크 설정 [ Click ] 
- 유선 네트워크 설정 [ Click ]
- 인터넷 연결 방법 고정 ip [ Click ]

### 2-2. KT

### 2-3. SKT

### 2-4. IPTIME

### 2-5. tp-link
