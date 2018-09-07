import grpc

# import generated classes
import calculator_pb2
import calculator_pb2_grpc

# open gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub
stub = calculator_pb2_grpc.AddStub(channel)

# create the request and get the response
a = 20
b = 10

print('Client side: {} + {}\n'.format(a, b))
print('Goint to server side \n. \n. \n.')
response = stub.AddCalculator(calculator_pb2.NumberRequest(value1 = a,value2 = b))

print('Server side: {}'.format(response.value))