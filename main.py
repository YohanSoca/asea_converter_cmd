import binascii
import time
#
# import serial
#
# ser = serial.Serial(
#     port= 'COM5',
#     baudrate= 19200,
#
#     parity=serial.PARITY_NONE,
#
#     stopbits=serial.STOPBITS_ONE,
#
#     bytesize=serial.EIGHTBITS,
#     timeout= 2
# )
#
#
#
# print("connected to: " + ser.portstr, "Please wait" )
# print('COM5 is now Open!')
# ser.flushInput()
# ser.flushOutput()
#
# ser.write(':SHORe:ON'.encode())

# ID = None
# FC = None
# ADDR = None
# OFFSET = None
# CRC = None
#
# def calc_crc(data):
#     crc = 0xFFFF
#     for pos in data:
#         crc ^= pos
#         for i in range(8):
#             if ((crc & 1) != 0):
#                 crc >>= 1
#                 crc ^= 0xA001
#             else:
#                 crc >>= 1
#     return crc
#
# def write_to_ser():
#
#     try:
#         # 01 03 0001 0001 d5ca
#         ser_frame = bytearray()
#         ser_frame.append(2)
#         ser_frame.append(3)
#         ser_frame.append(2)
#         ser_frame.append(1)
#         ser_frame.append(255)
#
#
#         data1 = bytearray.fromhex('02030201ff')
#         crc = calc_crc(data1)
#         local_crc = str("%04X" % (crc))[2:] + str("%04X" % (crc))[:2]
#         print(str("%04X" % (crc)))
#
#         ser_frame.append(189)
#         ser_frame.append(148)
#         # ser_frame.append(int(str(str("%04X" % (crc))[2:]), 16))
#         # ser_frame.append(int(str(str("%04X" % (crc))[:2]), 16))
#         print(ser_frame)
#
#         while True:
#             ser.write(ser_frame)
#             time.sleep(0.1)
#             print('writting')
#
#
#         print('write succeed')
#     except:
#             print('fail tp write')
#     time.sleep(0.5)
#
# print('trying to read')
# while True:
#     buffer = []
#     while len(buffer) < 8:
#         data = binascii.hexlify(ser.readline(1))
#         if data != b'':
#             buffer.append(data.decode('ascii'))
#     print(buffer)
#     # test = buffer
#     # data = data.decode('ascii')
#     # ID = ' '.join(str(e) for e in buffer[:1])
#     # FC = ' '.join(str(e) for e in buffer[1:2])
#     # ADDR = '00 10'
#     # OFFSET = ' '.join(str(e) for e in buffer[4:6])
#     # CRC = ' '.join(str(e) for e in buffer[6:8])
#     # cracked = f"{data[0:4]}0020{data[8:]}"
#     #
#     # tmp = ''.join(str(e) for e in buffer[:4])
#     # tmp = tmp + '0010'
#     # data1 = bytearray.fromhex(tmp)
#     # crc = calc_crc(data1)
#     # local_crc = str("%04X" % (crc))[2:] + str("%04X" % (crc))[:2]
#     # CRC = local_crc
#     # print(str("%04X" % (crc))[2:] + str("%04X" % (crc))[:2])
#     # print("%04X" % (crc))
#     #
#     # print(f"Id: {ID}, FC: {FC}, Addreess: {ADDR}, Offset: {OFFSET}, CRC: {CRC}")
#     # temp = int(f"0x{ID}", 16)


import serial

port = "COM5"
baud = 19200

ser = serial.Serial(port, baud, timeout=1)
# open the serial port
if ser.isOpen():
    print(ser.name + ' is open...')

while True:
    # cmd = raw_input("Enter command or 'exit':")
    # for Python 2
    cmd = input("Enter command or 'exit':")
    # for Python 3
    if cmd == 'exit':
        ser.close()
        exit()
    else:
        ser.write(cmd.encode('ascii') + '\r\n'.encode())
        out = ser.read()
        print('Receiving...' + out.decode('ascii'))


