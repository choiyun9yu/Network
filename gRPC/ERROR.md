# gRPC ERROR 

## 1. Type Error

> descriptor 'SerializeToString' for 'google._upb._message.Message' objects doesn't apply to a 'NoneType' obejct
> ERROR:grpc._common:Exception serializing message!
  
  [원인] gRPC 서버에서 클라이언트에게 비워진 메소드라도 반환하지 않은 경우 
####
  [해법] 괄호 안에 아무것도 안넣더라도 반환하면 괜찮음
