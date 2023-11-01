# SignalR

## 1. SignalR 이란?

Microsoft에서 개발한 실시간 웹 응용 프로그램을 구축하기 위한 라이브러리  
(실시간 웹 기능은 서버측 코드가 클라이언트에 즉시 컨텐츠를 밀어주는 것을 의미)

#### SignalR의 기본 아키텍처

-   **클라이언트**: 웹 브라우저, 모바일 앱 또는 기타 클라이언트 애플리케이션은 SignalR 클라이언트 라이브러리를 사용하여 서버와 통신합니다.

-   **서버**: .NET Core 또는 .NET Framework에서 실행되는 SignalR 서버는 클라이언트와 통신하고 실시간 이벤트를 처리합니다.

-   **전송 프로토콜**: SignalR은 여러 가지 전송 프로토콜을 사용하여 클라이언트와 서버 간의 통신을 처리합니다. 이 중 웹소켓(WebSockets)이 가장 효율적이며 실시간 통신에 적합한 프로토콜입니다.

## 2. 사용하기

#### HubConnectionBuilder

Signal 연결 설정을 돕는 도우미 클래스

-   연결 URL 설정
-   연결 메서드 설정
-   허브 메서드에 대한 클라이언트 콜백 설정
-   연결 옵션 설정
-   연결 빌드

### 2-1. .Net side

    // SignalR 설치
    % dotnet add package Microsoft.AspNetCore.SignalR   

#### Hub/SignalRHub.cs

    using Microsoft.AspNetCore.SignalR;

    namespace project_service.Hubs
    {
        public class SignalRHub : Hub
        {
            public async Task SendMessage(string user, string message)
            {
                await Clients.All.SendAsync("ReceiveMessage", user, message);
            }
        }
    }

#### Startup.cs

    using project_service.Hubs;
    using project_service.Service;
    
    namespace project_service
    {
        public class Startup    
        {
            public Startup(IConfiguration configuration)    
            {                                              
                Configuration = configuration;             
            }
            
            public IConfiguration Configuration { get; }

            public void ConfigureServices(IServiceCollection services)
            {
                .
                .
                .
                services.AddSignalR();  // SignalR 추가
            }

            public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
            {
                .
                .
                .

                // 엔드포인트 매핑, 컨트롤러 엔드 포인트를 애플리케이션에 매핑, API 요청을 처리하고 컨트롤러 액션을 실행하는데 사용
                app.UseEndpoints(endpoints =>
                {
                    endpoints.MapControllers();
                    endpoints.MapHub<DroneHub>("/signalHub");    // SignalHub endpoint 추가
                });
            }
        }   
    }

### 2-2. React side

#### SignalRContainer.jsx

    import React, {useState, useEffect} from 'react'
    import { HubConnectionBuilder } from '@microsoft/signalr';
    
    export const SignalRContext = React.createContext({})
    
    export const SignalRProvider = ({ children }) => {
    const [ connStt, setConnStt ] = useState('init');
    
        useEffect(() => {
            // 1. HubConnectionBuilder를 사용하여 SignalR Hub 연결을 위한 객체 생성
            const connection = new HubConnectionBuilder()
                .withUrl('http://localhost:5000/signalHub') // SignalR Hub의 URL 설정
                .build(); // HubConnection 객체 생성
    
            // 2. SignalR Hub 연결 시작
            connection.start()
                .then(async () => {
                    setConnStt('connected');
                    console.log('SignalR 연결 성공');   // Hub 연결 시작
                })
                .catch(error => {
                    setConnStt('error');
                    console.error('SignalR 연결 실패: ', error);    //
                });
        }, []);
    
        return <>{children}</>
    }
