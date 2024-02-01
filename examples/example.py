import example_pb2
from protobuf_metta import parser

proto_parser = parser.ProtobufParser(example_pb2.DESCRIPTOR,
                                     prefix="simple",
                                     curried=True)
metta_desc = proto_parser.description_to_metta()
print(metta_desc)
