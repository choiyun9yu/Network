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