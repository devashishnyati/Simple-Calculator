import grpc
from concurrent import futures
import time


# import generated classes
import calculator_pb2
import calculator_pb2_grpc

# create a class to define the server function 'AddCalculator' derived from 
# generated class service 'calculator_pb2_grpc.AddServicer'
class AddServicer(calculator_pb2_grpc.AddServicer):

    # the request and response are of the data type 
    # calculator_pb2.NumberRequest and calculator_pb2.NumberReply respectively
    def AddCalculator(self, request, context):
        return calculator_pb2.NumberReply(value = request.value1 + request.value2)

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function 'add_AddServicer_to_server'
# to add the defined class to the server
calculator_pb2_grpc.add_AddServicer_to_server(
        AddServicer(), server)


# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()


# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)