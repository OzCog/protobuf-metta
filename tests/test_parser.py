# Test ProtobufParser.parser.  Must be run from the repository root
# directory.

# Import simple_pb2, obtained by running
#
# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. simple.proto
import simple_pb2

# Import protobuf-metta
from protobuf_metta import parser

# Test ProtobufParser.description_to_metta
def test_description_to_metta():
    # Parse simple.proto and dump the result in metta_desc
    proto_parser = parser.ProtobufParser(simple_pb2.DESCRIPTOR)
    metta_desc = proto_parser.description_to_metta().rstrip()

    # Load simple.metta and compare it to metta_desc
    with open('tests/simple.metta', 'r') as file:
        data = file.read().rstrip()
        assert metta_desc == data
