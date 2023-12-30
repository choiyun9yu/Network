# U+

## 1. 관리자 페이지 접속
- 주소: 192.168.219.1
- LGU_0000 [ Click ]
- 비번: 공유기 뒷면 관리자 비밀번호

## 2. 네트워크 설정
- 네트워크 설정 Tap [ Click ]
- NAT 설정 [ Click ]
  - Well Registered Port: 0 ~ 1023 
  - Registered Port: 1024 ~ 49151
  - Dynamic Port: 449152 ~ 65535

## 3. ssh 포트 번호 변경
  % sudo vim /etc/ssh/sshd_config
    #Port 22 -> Port 원하는 번호
  % /etc/init.d/ssh restart


# KT



# SKT
