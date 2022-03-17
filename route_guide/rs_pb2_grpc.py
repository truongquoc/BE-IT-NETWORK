# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rs_pb2 as rs__pb2


class RecommendationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetItemRecommended = channel.unary_unary(
                '/Recommendation.Recommendation/GetItemRecommended',
                request_serializer=rs__pb2.UserRequest.SerializeToString,
                response_deserializer=rs__pb2.ItemResponse.FromString,
                )
        self.GetSimilarItem = channel.unary_unary(
                '/Recommendation.Recommendation/GetSimilarItem',
                request_serializer=rs__pb2.ItemRequest.SerializeToString,
                response_deserializer=rs__pb2.ItemResponse.FromString,
                )
        self.TrackChange = channel.unary_unary(
                '/Recommendation.Recommendation/TrackChange',
                request_serializer=rs__pb2.Check.SerializeToString,
                response_deserializer=rs__pb2.Check.FromString,
                )


class RecommendationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetItemRecommended(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSimilarItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrackChange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommendationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetItemRecommended': grpc.unary_unary_rpc_method_handler(
                    servicer.GetItemRecommended,
                    request_deserializer=rs__pb2.UserRequest.FromString,
                    response_serializer=rs__pb2.ItemResponse.SerializeToString,
            ),
            'GetSimilarItem': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSimilarItem,
                    request_deserializer=rs__pb2.ItemRequest.FromString,
                    response_serializer=rs__pb2.ItemResponse.SerializeToString,
            ),
            'TrackChange': grpc.unary_unary_rpc_method_handler(
                    servicer.TrackChange,
                    request_deserializer=rs__pb2.Check.FromString,
                    response_serializer=rs__pb2.Check.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Recommendation.Recommendation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recommendation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetItemRecommended(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Recommendation.Recommendation/GetItemRecommended',
            rs__pb2.UserRequest.SerializeToString,
            rs__pb2.ItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSimilarItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Recommendation.Recommendation/GetSimilarItem',
            rs__pb2.ItemRequest.SerializeToString,
            rs__pb2.ItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrackChange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Recommendation.Recommendation/TrackChange',
            rs__pb2.Check.SerializeToString,
            rs__pb2.Check.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)