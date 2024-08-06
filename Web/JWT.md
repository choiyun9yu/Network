# Json Web Token

## 1. What is JWT?
- JWT 는 웹 표준(RFC 7519)으로 정외든 토큰 기반 인증 방식이다.
- JWT 는 사용자 인증 정보를 안전하게 전송하고 저장할 수 있는 방법을 제공한다.

## 2. JWT 의 구조
![img.png](../.img/wimg_5.png)  

    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

### 2-1. Header
- 토큰 유형과 사용된 암호화 알고리즘(HS256, RS256 등)이 포함된다.

      {
          "alg": "HS256",
          "typ": "JWT"
      }

### 2-2. Payload
- 토큰에 포함된 데이터를 저장한다. 
- 여기에는 사용자 ID, 이름, 이메일 과 같은 사용자 정보가 포함될 수 있다.

      {
          "sub": "1234567890"
          "name": "John Doe"
          "iat": 1516239022
      }
    - 데이터 각각의 Key 를 claim 이라고 한다.
    - claim 은 사용자가 원하는 Key 와 Value 로 구성할 수 있다.
    - claim 에는 3가지 종류가 있다. (registered, public, private)

#### registered claim: 등록된 클레임
- 컴팩트하게 3글자로 정의하며, 필수는 아니나 사용이 권장된다.
- iss(issuer), exp(expiration time), sub(subject), aud(audience) 등이 있다.
- [그 외 종류](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1)

#### public claim: 공개 클레임
- 사용자가 자유롭게 정의할 수 있다.
- 단, 충돌을 방지하려면 IANA JSON 웹 토큰 레지스트리에 정의돼 있거나,  
  충돌이 방지된 네임스페이스를 포함하는 URI 로 정의해야 한다.
- URI 로 정의하는 경우
  
      {"http(s)://specific.uri/@unique_recommended_namespace/additional_path": true}
- [IANA JSON Web Token Registries](https://www.iana.org/assignments/jwt/jwt.xhtml)

#### private claim: 비공개 클레임
- 등록된 또는 공개 클레임이 아닌 클레임이며, 정보를 공유하기 위해 만들어진 커스터마이징된 클레임이다.

#### precautions: 주의사항
- Payload 는 서명된 파트가 아니다.
- 단순 Base64 인코딩이 된 파트이며, 이는 누구나 디코딩하여 데이터 열람이 가능하다.
- password 같은 결정적인 요소들은 Payload 에 담기면 안된다.

### 2-3. Signature
- Header 와 Payload 를 합친 문자열에 비밀키로 서명한 값이다. 
- 서버에서만 알고 있는 비밀키로 생성되므로 토큰의 무결성을 보장한다.

      HMACSHA256(
        base64UrlEncode(header) + "." +
        base64UrlEncode(playload),
        secret
      )
- 위와 같이 Base64 인코딩된 Header"."Payload 그리고 secret 이 필요하다.

## 3. JWT 의 작동 원리 
1. 사용자 인증: 사용자가 로그인 요청을 보낸다.
2. 인증 성공: 서버가 사용자를 인증하고 JWT 를 생성한다.
3. JWT 생성: 서버는 사용자 정보를 JSON 형식으로 만들고, 이를 암호화하여 JWT 를 생성한다.
4. 클라이언트에 전송: 서버는 JWT 를 클라이언트에 전송한다.
5. 클라이언트 저장: 클라이언트는 JWT 를 로컬 스토리지 또는 쿠키에 저장한다.
6. 인증 요청: 클라이언트가 서버에 인증이 필요한 요청을 보낸다.
7. JWT 검증: 서버는 클라이언트가 보낸 JWT 를 검증한다.
8. 인증 성공: JWT 가 유효하면 서버는 요청을 처리한다.

## 4. JWT 의 특징
### 4-1. 장점
- 자체 포함적(Self-contained): JWT 에는 필요한 모든 정보가 포함되어 있어 별도의 데이터베이스 조회 없이 인증이 가능하다. 
- 무상태(Stateless): 서버에 세션 정보를 저장하지 않고 클라이언트가 JWT 를 가지고 있어 상태 정보를 관리한다.
- 확장성: 다양한 클레임을 추가할 수 있어 사용 사례에 맞게 토큰을 확장할 수 있다.
- 보안성: JWT 는 디지털 서명으로 토큰의 무결성을 보장한다. 또한 암호화를 통해 전송 중 데이터 유출을 방지할 수 있다.

### 4-2. 단점 
- 토큰의 크기: JWT 는 다른 인증 메커니즘에 비해 토큰의 크기가 크다.
- 토큰의 유효 기간: JWT 의 유효 기간을 설정해야 하며, 이 기간이 만료되면 토큰을 재발급해야 한다.


## 5.  JWT 사용 사례
- 인증: 사용자 인증 및 권한 부여에 사용된다.
- API 인증: API 요청에 대한 인증에 사용된다.
- 단일 로그인: 여러 서비스에 대한 단일 로그인에 사용된다.