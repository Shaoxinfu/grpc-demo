# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import data_pb2 as data__pb2


class modelStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.test_show = channel.unary_unary(
        '/test_example.model/test_show',
        request_serializer=data__pb2.test_Request.SerializeToString,
        response_deserializer=data__pb2.test_Response.FromString,
        )


class modelServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def test_show(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_modelServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'test_show': grpc.unary_unary_rpc_method_handler(
          servicer.test_show,
          request_deserializer=data__pb2.test_Request.FromString,
          response_serializer=data__pb2.test_Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'test_example.model', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))