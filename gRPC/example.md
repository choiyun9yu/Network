# Example

- 각 언어에는 gRPC 의 클라이언트 및 서버용 라이브러리가 있어 다른 언어로 작성된 클라이언트와 서버가 서로 통신할 수 있다.
- 이렇게 gRPC 는 서로 다른 언어 간에 효율적인 통신을 지원한다.

#### 서버
- 서버는 클라이언트의 요청을 받아들이고 처리한다.
- 일반적으로 서비스의 구현이 위치하며, 클라이언트 요청에 대한 응답을 생성한다.
- 서버는 서비스를 호스팅하고, 클라이언트로부터의 요청을 받아들이고 이에 따른 작업을 수행한다.

#### 클라이언트
- 클라이언트는 서버에 요청을 보내고 응답을 받는다.
- 일반적으로 클라이언트는 서비스의 사용자 또는 소비자이다.
- 클라이언트는 서버에 요청을 보내고, 서버의 응답을 받아 필요에 따라 처리한다.

#### 양방향 통신
- 양방향 통신에서는 클라이언트와 서버 모두 요청을 보내고 응답을 받을 수 있다.
- 이런 양방향 통신은 스트리밍 RPC 를 통해 제공된다.

<br>

## 1. C# -> Python

### 1-1. .proto 파일 작성 

    syntax = "proto3";  // 프로토 버퍼 버전 3 지정  

    package greet;      // 메시지와 서비스가 속하는 패키지 지정
    
    // GreetRequest 메시지 정의 
    message GreetRequest {
      string name = 1;  // name 필드 정의 필드 번호는 1 
    }
    
    // GreetResponse 메시지 정의 
    message GreetResponse {
      string message = 1; // message 필드 정의 필드 번호는 1 
    }
    
    // Greet 서비스 정의 
    service Greeter {
      // SayHello 메소드 정의 
        // GreetReqeust 메시지를 입력으로 받고 GreetResponse 메시지를 반환 
      rpc SayHello (GreetRequest) returns (GreetResponse);
    }

- 클라이언트는 SayHello 메소드를 호출하여 서버에 GreetRequest 메시지를 보낸다.
- 서버는 GreetResponse 메시지를 만들어 클라이언트에게 반환한다.

### 1-2. 프로토 버퍼 컴파일 

    // 라이브러리 설치 
    % pip install grpcio-tools

- grpcio-tools 는 프로토콜 버퍼 컴파일러와 서비스 정의 protoc 에서 서버 및 클라이언트 코드를 생성하기 위한 특수 플러그인이 포함되어 있다.  
  (grpcio-tools 를 설치하면 자동으로 protoc-gen-grpc 가 설치된다.)
- 즉, .proto 확장자로 작성한 파일을 컴파일 해주는 역할을 한다.


    // 프로토 버퍼 컴파일 명령 
    % protoc --proto_path=. greet.proto --csharp_out=. --python_out=.

- protoc: 프로토 버퍼 컴파일러
- proto_path=.: .proto 파일이 있는 경로 지정 
- greet.proto: 컴파일할 프로토 버퍼 파일 이름
- csharp_out=.: C# 코드 출력 경로 지정 
  - greet_pb.cs: C# 클라이언트 코드 
- python_out=.: Python 코드 출력 경로 지정
  - greet_pb2.py: Pthon 서버 코드 
- grpc_out=.: Python gRPC 서버 코드 출력 경로 지정
  - greet_pb2_grpc.py: Python 서버 코드 (gRPC 서버 코드 생성에 필요)

### 1-3. Python gRPC Server

    // 프로젝트 생성
    % poetry init grpc
    
    // 가상환경 쉘 실행 
    % poetry shell
    
    // grpc 라이브러리 추가 
    % poetry add grpcio grpcio-tools

######
    // run.py
    import grpc

    from greet_pb2 import GreetRequest, GreetResponse
    from greet_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server
    
    class Greeter(GreeterServicer):
      def SayHello(self, request, context):
      return GreetResponse(message="안녕하세요, " + request.name + "!")
    
    def serve():
      server =grpc.Server()
      add_GreeterServicer_to_server(Greeter(), server)
      server.add_insecure_port('[::]:50051')
      server.start()
      server.wait_for_termination()
    
    if __name__ == '__main__':
    serve()

### 1-4. CSharp gRPC Client
- [dotnet-grpc](https://github.com/grpc/grpc-dotnet?tab=readme-ov-file) 사용 권장
- [microsoft docs](https://learn.microsoft.com/ko-kr/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-8.0&tabs=visual-studio)


    // GrpcGreeter 폴더에 새 gRPC 서비스 만들기 
    % dotnet new grpc -o GrpcGreeter

    // 윈도우에서 실행 (리눅스에서 동작하지 않음)
    % dotnet dev-certs https --trust

