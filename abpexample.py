#ABP Example
from iotloranode import loraNode
#Setup the Node
node = loraNode()
node.set_devAddr("26011FD8")
node.set_networkKey("2E6292746E6905BFF64B6DAA2A983ADF")
node.set_appSessionKey("23C9BC60EBED5998F09E83C4BF70CAA8")
node.join(node.abp)
node.send_string_packet("Hello World")
