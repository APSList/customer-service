import grpc
from concurrent import futures
from generated import customer_pb2_grpc
from services import CustomerService
from grpc_reflection.v1alpha import reflection

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    customer_pb2_grpc.add_CustomerServiceServicer_to_server(CustomerService(), server)

    SERVICE_NAMES = (
        customer_pb2_grpc.CustomerServiceServicer.__name__,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051 with reflection")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
