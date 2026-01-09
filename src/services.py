from generated import customer_pb2_grpc, customer_pb2
import grpc
from customer.customer import get_customers, get_customer_by_id, create_customer, delete_customer

class CustomerService(customer_pb2_grpc.CustomerServiceServicer):
    def GetCustomer(self, request, context):
        customer = get_customer_by_id(request.id)
        if not customer:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Customer with id={request.id} not found")
            return customer_pb2.CustomerResponse()

        return customer_pb2.CustomerResponse(
            customer=customer_pb2.Customer(
                id=customer[0],
                full_name=customer[1],
                email=customer[2],
                created_at=str(customer[3])  # convert datetime to string
            )
        )

    def ListCustomers(self, request, context):
        users = get_customers()
        return customer_pb2.ListCustomersResponse(
            customers=[
                customer_pb2.Customer(
                    id=u[0],
                    full_name=u[1],
                    email=u[2],
                    created_at=str(u[3]),
                    organization_id=u[4]
                ) for u in users
            ]
        )

    def CreateCustomer(self, request, context):
        create_customer(request.full_name, request.email, request.organization_id)

        users = get_customers()
        new_user = users[-1]  # simple approach, last inserted
        return customer_pb2.CustomerResponse(
            customer=customer_pb2.Customer(
                id=new_user[0],
                full_name=new_user[1],
                email=new_user[2],
                created_at=str(new_user[3]),
                organization_id=new_user[4]
            )
        )

    def DeleteCustomer(self, request, context):
        success = delete_customer(request.id)
        return customer_pb2.DeleteCustomerResponse(success=success)