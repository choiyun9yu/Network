# WebSocket

## 1. 웹 소켓 개요
### 1-1. 웹 소켓
웹 소켓은 컴퓨터 네트워킹 프로토콜 중 하나이다. 이 프로토콜은 클라이언트와 서버 간에 실시간 양방향 통신을 가능하게 하고, 이를 통해 실시간 웹 애플리케이션을 구축하는 데 사용된다. 예를 들어 실시간 채팅, 주식 시장 실시간 데이터 스트리밍, 협업 도구, 게임 등 클라이언트와 서버간 실시간 통신이 중요한 경우, 많은 사용자들이 동시에 연결되어 있는 경우 효율적으로 데이터를 전송할 수 있다.

### 1-2. HTTP와 다른점
기존 HTTP는 단방향 통신이다. 클라이언트에서 서버로 Request를 보내면 서버는 클라이언트로 Response를 보내는 방식으로 동작한다. 또한, HTTP는 기본적으로 무상태(Stateless)이므로 상태를 저장하지 않는다. 하지만 웹 소켓은 양방향 통신으로 연결이 이루어지면 클라이언트가 요청하지 않아도 데이터가 저절로 서버로부터 올 수 있다. HTTP처럼 별도의 요청을 보내지 않아도 데이터를 수신할 수 있는 것이다.

### 1-3. 웹 소켓 프로토콜
웹 소켓 프로토콜은 HTTP와는 별개로 동작한다. 웹 소캣을 사용하기 위해서는 먼저 HTTP를 통한 업그레이드 과정이 필요하다. 클라이언트는 서버에 웹 소켓을 연결하고, 서버가 이를 수락하여 양측은 웹 소캣을 통한 통신을 할 수 있게 된다. 웹 소켓 프로토콜은 실시간 양방향 데이터 전송에 특화되어 있으며, 헤더 크기가 작고 메시지 전송에 대한 최소한의 오버헤드를 가지고 있다. 



## 2. 웹 소켓 통신
### 2-1. 웹 소켓 연결 및 해제
클라이언트는 서버에 웹 소켓 연결을 요청하기 위해 HTTP를 사용한다. 클라이언트가 특정 헤더와 함께 HTTP 요청을 전송하면, 서버는 해당 요청을 수락하여 웹 소켓 통신을 위한 연결을 설정한다. 웹 소켓 연결은 일반적으로 사용자 인증과정, 세션 관리 등을 포함한다. 웹 소켓 연결은 클라잉너트 브라우저에서 실행되며, 사용자가 페이지를 나가거나 연결이 끊어질 때까지 유지된다.

### 2-2. 메시지 전송 및 수신
클라이언트와 서버는 연결된 웹 소켓을 통해 메시지를 전송하고 수신할 수 있다. 클라이언트가 서버로 메시지를 전송하면, 서버는 해당 메시지를 수신하고 필요한 처리를 수행한다. 마찬가지로 서버가 클라이언트로 메시지를 전송하면, 클라이언트는 해당 메시지를 수신하고 필요한 동작을 수생한다. 

### 2-3. 이벤트 처리
웹 소켓은 이벤트 기반 통신을 지원한다. 클라이언트와 서버는 특정 이벤트(예: 메시지 수신, 연결 해제 등)가 발생할 때 해당 이벤트를 처리하는 콜백 함수를 등록할 수 있다. 이벤트 처리 함수는 해당 이벤트가 발생했을 때 실행되며, 특정 동작을 수행하는 데 사용될 수 있다. 이벤트 처리를 통해 클라이언트와 서버는 실시간 통신에 필요한 기능을 구현할 수 있다.


## 3. 웹 소켓 구현
### 3-1. 웹 소켓 확장
웹 소켓은 기본적인 양방향 통신 기능을 제공하지만, 확장 기능을 추가하여 더 다양한 기능을 구현할 수 있다. 예를 들어 채팅방, 실시간 알림, 게임 등 다양한 기능을 웹소켓을 통해 구현할 수 있다.

### 3-2. 클라이언트 구현 방법
웹 소켓은 서버와 클라이언트 간의 실시간 통신을 지원하기 때문에 클라이언트 구현도 중요한 부분이다. 웹 소켓 클라이언트를 구현하는 방법은 크게 2가지가 있다.  

먼저 Javascript 라이브러리를 사용하여 클라이언트를 구현할 수 있다. 예를 들어, WebSocket API를 사용하여 클라이언트를 구현할 수 있으며,  Socket.IO, SockJS 등의 라이브러리를 사용하여 더 다양한 기능을 구현할 수 있다.  

다음으로 웹 소켓 클라이언트를 네이트브 앱에 포함시킬 수 있다. 안드로이드나 IOS 앱에서 웹 소켓 클라이언트를 사용하여 실시간 통신을 구현할 수 있다. 네이티브 앱에서 웹 소켓 클라이언트를 사용하는 방법은 플랫폼에 따라 다를 수 있으므로 해당 플랫폼의 문서를 참고해야 한다.

#### 네이티브 앱
네이티브 앱은 특정 플랫폼이나 운영체제를 위해 개발된 소프트웨어 어플리케이션을 말한다. 네이티브 앱은 해당 플랫폼의 언어와 도구를 사용하여 개발되며, 일반적으로 iOS나 Android와 같은 특정 운영체제에서만 실행된다.

### 3-3. 서버 구현 방법과 웹 소켓 개념 정리
웹 소켓 서버를 구현하기 위한 방법도 여러가지가 있다. 일반적으로는 프로그래밍 언어와 프레임워크를 사용하여 웹 소켓 서버를 구현할 수 있다. 예를 들어, Node.js에서는 ws, Socket.IO, SockJS 등의 라이브러리를 사용하여 웹 소켓 서버를 구현할 수 있다. Java에서는 Spring Framework의 Spring Websocket 모듈을 사용하여 웹 소켓 서버를 구현할 수 있다. 또한 Python에서는 Flask-SocketIO, Django Channels 등의 라이브러리를 사용하여 구현할 수 있다.

웹 소켓 개념을 간략하게 정의하자면, 웹 소켓은 HTML5에서 지원하는 프로토콜로, 양방향 통신을 위해 사용된다. 기존의 HTTP 요청/응답 모델과 달리, 웹 소켓은 클라이언트와 서버 간의 지속적인 연결을 유지하며 데이터를 주고 받는다. 이를 통해 실시간 통신을 구현할 수 있으며, 채팅 애플리케이션, 주식 시세 알림, 게임 등 다양한 영역에서 사용된다.

[ref](https://infokyeon.com/websocket-%ED%95%9C%EB%B0%A9%EC%97%90-%EC%A0%95%EB%A6%AC/)

## 4. 웹 소켓 동작
![image](https://github.com/choiyun9yu/Network/assets/110392046/f3ee5ae9-db00-4ab8-a2c3-0d5f7ec87067)

웹 소켓은 HTTP 포트 80, HTTPS 포트 443 위에서 동작한다. 웹 소켓은 TCP연결 처럼 핸드셰이크를 이용해 연결을 맺는다. 이때 HTTP 업그레이드 헤더를 사용하여 HTTP 프로토콜에서 웹 소켓 프로토콜(WS)로 변경된다.
(최초 접속 시 HTTP 프로토콜을 이용해 핸드셰이킹하는 것이다.)

이후 연결이 맺어지면 어느 한쪽이 연결을 끊지 않는 이상 영구적인 동일한 채널이 맺어진다. 이때 데이터를 암호화하기 위해 WSS 프로토콜 등을 이용할 수도 있다.

### Web Socket과 Socket.io의 차이
#### Web Socket
HTTP 5 표준의 일부로 실시간으로 상효작용하는 웹 서비스를 만드는 표준 기술이다.

#### Socket.io
다양한 방식의 실시간 웹 기술을 손쉽게 사용할 수 있는 모듈(WebSocket, FlashSocket, AJAX Long Polling, IFrame, JsonP, Polling 등), JavaScript를 이용하여 브라우저 종류에 상관없이 실시간 웹을 구현할 수 있도록 한 기술이다. WebSocket을 지원하지 않는 브라우저에서도 메시지를 일관된 모듈로 보낼 수 있다.
