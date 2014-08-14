# Software License Agreement (BSD License)
#
# Copyright (c) 2014, Robotnik Automation SLL
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Robotnik Automation SSL nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


from ctypes import *
from pcan_python import pcan_module

#///////////////////////////////////////////////////////////
# Type definitions
#///////////////////////////////////////////////////////////

TPCANHandle            = c_ubyte  # Represents a PCAN hardware channel handle
TPCANStatus            = int      # Represents a PCAN status/error code
TPCANParameter         = c_ubyte  # Represents a PCAN parameter to be read or set
TPCANDevice            = c_ubyte  # Represents a PCAN device
TPCANMessageType       = c_ubyte  # Represents the type of a PCAN message
TPCANType              = c_ubyte  # Represents the type of PCAN hardware to be initialized
TPCANMode              = c_ubyte  # Represents a PCAN filter mode
TPCANBaudrate          = c_ushort # Represents a PCAN Baud rate register value

#///////////////////////////////////////////////////////////
# Value definitions
#///////////////////////////////////////////////////////////

# Currently defined and supported PCAN channels
#
PCAN_NONEBUS             = TPCANHandle(0x00)  # Undefined/default value for a PCAN bus

PCAN_ISABUS1             = TPCANHandle(0x21)  # PCAN-ISA interface, channel 1
PCAN_ISABUS2             = TPCANHandle(0x22)  # PCAN-ISA interface, channel 2
PCAN_ISABUS3             = TPCANHandle(0x23)  # PCAN-ISA interface, channel 3
PCAN_ISABUS4             = TPCANHandle(0x24)  # PCAN-ISA interface, channel 4
PCAN_ISABUS5             = TPCANHandle(0x25)  # PCAN-ISA interface, channel 5
PCAN_ISABUS6             = TPCANHandle(0x26)  # PCAN-ISA interface, channel 6
PCAN_ISABUS7             = TPCANHandle(0x27)  # PCAN-ISA interface, channel 7
PCAN_ISABUS8             = TPCANHandle(0x28)  # PCAN-ISA interface, channel 8

PCAN_DNGBUS1             = TPCANHandle(0x31)  # PCAN-Dongle/LPT interface, channel 1

PCAN_PCIBUS1             = TPCANHandle(0x41)  # PCAN-PCI interface, channel 1
PCAN_PCIBUS2             = TPCANHandle(0x42)  # PCAN-PCI interface, channel 2
PCAN_PCIBUS3             = TPCANHandle(0x43)  # PCAN-PCI interface, channel 3
PCAN_PCIBUS4             = TPCANHandle(0x44)  # PCAN-PCI interface, channel 4
PCAN_PCIBUS5             = TPCANHandle(0x45)  # PCAN-PCI interface, channel 5
PCAN_PCIBUS6	         = TPCANHandle(0x46)  # PCAN-PCI interface, channel 6
PCAN_PCIBUS7	         = TPCANHandle(0x47)  # PCAN-PCI interface, channel 7
PCAN_PCIBUS8	         = TPCANHandle(0x48)  # PCAN-PCI interface, channel 8

PCAN_USBBUS1             = TPCANHandle(0x51)  # PCAN-USB interface, channel 1
PCAN_USBBUS2             = TPCANHandle(0x52)  # PCAN-USB interface, channel 2
PCAN_USBBUS3             = TPCANHandle(0x53)  # PCAN-USB interface, channel 3
PCAN_USBBUS4             = TPCANHandle(0x54)  # PCAN-USB interface, channel 4
PCAN_USBBUS5             = TPCANHandle(0x55)  # PCAN-USB interface, channel 5
PCAN_USBBUS6             = TPCANHandle(0x56)  # PCAN-USB interface, channel 6
PCAN_USBBUS7             = TPCANHandle(0x57)  # PCAN-USB interface, channel 7
PCAN_USBBUS8             = TPCANHandle(0x58)  # PCAN-USB interface, channel 8

PCAN_PCCBUS1             = TPCANHandle(0x61)  # PCAN-PC Card interface, channel 1
PCAN_PCCBUS2             = TPCANHandle(0x62)  # PCAN-PC Card interface, channel 2

# Represent the PCAN error and status codes 
#
PCAN_ERROR_OK            = TPCANStatus(0x00000)  # No error 
PCAN_ERROR_XMTFULL       = TPCANStatus(0x00001)  # Transmit buffer in CAN controller is full
PCAN_ERROR_OVERRUN       = TPCANStatus(0x00002)  # CAN controller was read too late
PCAN_ERROR_BUSLIGHT      = TPCANStatus(0x00004)  # Bus error: an error counter reached the 'light' limit
PCAN_ERROR_BUSHEAVY      = TPCANStatus(0x00008)  # Bus error: an error counter reached the 'heavy' limit
PCAN_ERROR_BUSOFF        = TPCANStatus(0x00010)  # Bus error: the CAN controller is in bus-off state
PCAN_ERROR_ANYBUSERR     = TPCANStatus(PCAN_ERROR_BUSLIGHT | PCAN_ERROR_BUSHEAVY | PCAN_ERROR_BUSOFF) # Mask for all bus errors
PCAN_ERROR_QRCVEMPTY     = TPCANStatus(0x00020)  # Receive queue is empty
PCAN_ERROR_QOVERRUN      = TPCANStatus(0x00040)  # Receive queue was read too late
PCAN_ERROR_QXMTFULL      = TPCANStatus(0x00080)  # Transmit queue is full
PCAN_ERROR_REGTEST       = TPCANStatus(0x00100)  # Test of the CAN controller hardware registers failed (no hardware found)
PCAN_ERROR_NODRIVER      = TPCANStatus(0x00200)  # Driver not loaded
PCAN_ERROR_HWINUSE       = TPCANStatus(0x00400)  # Hardware already in use by a Net
PCAN_ERROR_NETINUSE      = TPCANStatus(0x00800)  # A Client is already connected to the Net
PCAN_ERROR_ILLHW         = TPCANStatus(0x01400)  # Hardware handle is invalid
PCAN_ERROR_ILLNET        = TPCANStatus(0x01800)  # Net handle is invalid
PCAN_ERROR_ILLCLIENT     = TPCANStatus(0x01C00)  # Client handle is invalid
PCAN_ERROR_ILLHANDLE     = TPCANStatus(PCAN_ERROR_ILLHW | PCAN_ERROR_ILLNET | PCAN_ERROR_ILLCLIENT) # Mask for all handle errors
PCAN_ERROR_RESOURCE      = TPCANStatus(0x02000)  # Resource (FIFO, Client, timeout) cannot be created
PCAN_ERROR_ILLPARAMTYPE  = TPCANStatus(0x04000)  # Invalid parameter
PCAN_ERROR_ILLPARAMVAL   = TPCANStatus(0x08000)  # Invalid parameter value
PCAN_ERROR_UNKNOWN       = TPCANStatus(0x10000)  # Unknow error
PCAN_ERROR_ILLDATA       = TPCANStatus(0x20000)  # Invalid data, function, or action
PCAN_ERROR_INITIALIZE    = TPCANStatus(0x40000)  # Channel is not initialized

# PCAN devices
#
PCAN_NONE                = TPCANDevice(0x00)  # Undefined, unknown or not selected PCAN device value
PCAN_PEAKCAN             = TPCANDevice(0x01)  # PCAN Non-Plug&Play devices. NOT USED WITHIN PCAN-Basic API
PCAN_ISA                 = TPCANDevice(0x02)  # PCAN-ISA, PCAN-PC/104, and PCAN-PC/104-Plus
PCAN_DNG                 = TPCANDevice(0x03)  # PCAN-Dongle
PCAN_PCI                 = TPCANDevice(0x04)  # PCAN-PCI, PCAN-cPCI, PCAN-miniPCI, and PCAN-PCI Express
PCAN_USB                 = TPCANDevice(0x05)  # PCAN-USB and PCAN-USB Pro
PCAN_PCC                 = TPCANDevice(0x06)  # PCAN-PC Card

# PCAN parameters
#
PCAN_DEVICE_NUMBER       = TPCANParameter(0x01)  # PCAN-USB device number parameter
PCAN_5VOLTS_POWER        = TPCANParameter(0x02)  # PCAN-PC Card 5-Volt power parameter
PCAN_RECEIVE_EVENT       = TPCANParameter(0x03)  # PCAN receive event handler parameter
PCAN_MESSAGE_FILTER      = TPCANParameter(0x04)  # PCAN message filter parameter
PCAN_API_VERSION         = TPCANParameter(0x05)  # PCAN-Basic API version parameter
PCAN_CHANNEL_VERSION     = TPCANParameter(0x06)  # PCAN device channel version parameter
PCAN_BUSOFF_AUTORESET    = TPCANParameter(0x07)  # PCAN Reset-On-Busoff parameter
PCAN_LISTEN_ONLY         = TPCANParameter(0x08)  # PCAN Listen-Only parameter
PCAN_LOG_LOCATION        = TPCANParameter(0x09)  # Directory path for trace files
PCAN_LOG_STATUS          = TPCANParameter(0x0A)  # Debug-Trace activation status
PCAN_LOG_CONFIGURE       = TPCANParameter(0x0B)  # Configuration of the debugged information (LOG_FUNCTION_***)
PCAN_LOG_TEXT            = TPCANParameter(0x0C)  # Custom insertion of text into the log file
PCAN_CHANNEL_CONDITION   = TPCANParameter(0x0D)  # Availability status of a PCAN-Channel
PCAN_HARDWARE_NAME       = TPCANParameter(0x0E)  # PCAN hardware name parameter
PCAN_RECEIVE_STATUS      = TPCANParameter(0x0F)  # Message reception status of a PCAN-Channel
PCAN_CONTROLLER_NUMBER   = TPCANParameter(0x010) # CAN-Controller number of a PCAN-Channel

# PCAN parameter values
#
PCAN_PARAMETER_OFF       = int(0x00)  # The PCAN parameter is not set (inactive)
PCAN_PARAMETER_ON        = int(0x01)  # The PCAN parameter is set (active)
PCAN_FILTER_CLOSE        = int(0x00)  # The PCAN filter is closed. No messages will be received
PCAN_FILTER_OPEN         = int(0x01)  # The PCAN filter is fully opened. All messages will be received
PCAN_FILTER_CUSTOM       = int(0x02)  # The PCAN filter is custom configured. Only registered messages will be received
PCAN_CHANNEL_UNAVAILABLE = int(0x00)  # The PCAN-Channel handle is illegal, or its associated hadware is not available
PCAN_CHANNEL_AVAILABLE   = int(0x01)  # The PCAN-Channel handle is available to be connected (Plug&Play Hardware: it means futhermore that the hardware is plugged-in)
PCAN_CHANNEL_OCCUPIED    = int(0x02)  # The PCAN-Channel handle is valid, and is already being used

LOG_FUNCTION_DEFAULT     = int(0x00)   # Logs system exceptions / errors
LOG_FUNCTION_ENTRY       = int(0x01)   # Logs the entries to the PCAN-Basic API functions 
LOG_FUNCTION_PARAMETERS  = int(0x02)   # Logs the parameters passed to the PCAN-Basic API functions 
LOG_FUNCTION_LEAVE       = int(0x04)   # Logs the exits from the PCAN-Basic API functions 
LOG_FUNCTION_WRITE       = int(0x08)   # Logs the CAN messages passed to the CAN_Write function
LOG_FUNCTION_READ        = int(0x10)   # Logs the CAN messages received within the CAN_Read function
LOG_FUNCTION_ALL         = int(0xFFFF) # Logs all possible information within the PCAN-Basic API functions

# PCAN message types
#
PCAN_MESSAGE_STANDARD    = TPCANMessageType(0x00)  # The PCAN message is a CAN Standard Frame (11-bit identifier)
PCAN_MESSAGE_RTR         = TPCANMessageType(0x01)  # The PCAN message is a CAN Remote-Transfer-Request Frame
PCAN_MESSAGE_EXTENDED    = TPCANMessageType(0x02)  # The PCAN message is a CAN Extended Frame (29-bit identifier)
PCAN_MESSAGE_STATUS      = TPCANMessageType(0x80)  # The PCAN message represents a PCAN status message

# Frame Type / Initialization Mode
#
PCAN_MODE_STANDARD       = PCAN_MESSAGE_STANDARD  
PCAN_MODE_EXTENDED       = PCAN_MESSAGE_EXTENDED  

# Baud rate codes = BTR0/BTR1 register values for the CAN controller.
# You can define your own Baud rate with the BTROBTR1 register.
# Take a look at www.peak-system.com for our free software "BAUDTOOL" 
# to calculate the BTROBTR1 register for every baudrate and sample point.
#
PCAN_BAUD_1M             = TPCANBaudrate(0x0014) #   1 MBit/s
PCAN_BAUD_800K           = TPCANBaudrate(0x0016) # 800 kBit/s
PCAN_BAUD_500K           = TPCANBaudrate(0x001C) # 500 kBit/s
PCAN_BAUD_250K           = TPCANBaudrate(0x011C) # 250 kBit/s
PCAN_BAUD_125K           = TPCANBaudrate(0x031C) # 125 kBit/s
PCAN_BAUD_100K           = TPCANBaudrate(0x432F) # 100 kBit/s
PCAN_BAUD_95K            = TPCANBaudrate(0xC34E) #  95,238 kBit/s
PCAN_BAUD_83K            = TPCANBaudrate(0x4B14) #  83,333 kBit/s
PCAN_BAUD_50K            = TPCANBaudrate(0x472F) #  50 kBit/s
PCAN_BAUD_47K            = TPCANBaudrate(0x1414) #  47,619 kBit/s
PCAN_BAUD_33K            = TPCANBaudrate(0x1D14) #  33,333 kBit/s
PCAN_BAUD_20K            = TPCANBaudrate(0x532F) #  20 kBit/s
PCAN_BAUD_10K            = TPCANBaudrate(0x672F) #  10 kBit/s
PCAN_BAUD_5K             = TPCANBaudrate(0x7F7F) #   5 kBit/s

# Supported No-Plug-And-Play Hardware types
#
PCAN_TYPE_ISA            = TPCANType(0x01)  # PCAN-ISA 82C200
PCAN_TYPE_ISA_SJA        = TPCANType(0x09)  # PCAN-ISA SJA1000
PCAN_TYPE_ISA_PHYTEC     = TPCANType(0x04)  # PHYTEC ISA 
PCAN_TYPE_DNG            = TPCANType(0x02)  # PCAN-Dongle 82C200
PCAN_TYPE_DNG_EPP        = TPCANType(0x03)  # PCAN-Dongle EPP 82C200
PCAN_TYPE_DNG_SJA        = TPCANType(0x05)  # PCAN-Dongle SJA1000
PCAN_TYPE_DNG_SJA_EPP    = TPCANType(0x06)  # PCAN-Dongle EPP SJA1000
N_ERROR_INITIALIZE    = TPCANStatus(0x40000)  # Channel is not initialized


# Represents a PCAN message
#
class TPCANMsg (Structure):
    """
    Represents a PCAN message
    """
    _fields_ = [ ("ID",      c_ulong),          # 11/29-bit message identifier
                 ("MSGTYPE", TPCANMessageType), # Type of the message
                 ("LEN",     c_ubyte),          # Data Length Code of the message (0..8)
                 ("DATA",    c_ubyte * 8) ]     # Data of the message (DATA[0]..DATA[7])


# Represents a timestamp of a received PCAN message
# Total Microseconds = micros + 1000 * millis + 0xFFFFFFFF * 1000 * millis_overflow
#
class TPCANTimestamp (Structure):
    """
    Represents a timestamp of a received PCAN message
    Total Microseconds = micros + 1000 * millis + 0xFFFFFFFF * 1000 * millis_overflow
    """
    _fields_ = [ ("millis", c_ulong),           # Base-value: milliseconds: 0.. 2^32-1
                 ("millis_overflow", c_ushort), # Roll-arounds of millis
                 ("micros", c_ushort) ]         # Microseconds: 0..999

#///////////////////////////////////////////////////////////
# PCAN-Basic API function declarations
#///////////////////////////////////////////////////////////

# PCAN-Basic API class implementation
#
class PCANBasic:
	"""
	  PCAN-Basic API class implementation
	"""      
	def __init__(self, port = '/dev/pcan32'):
		self.initialized = False
		self.can_port = port

	# Initializes a PCAN Channel
	#
	def Initialize(
		self,
		Channel,   
		Btr0Btr1,  
		HwType = 'USB',  
		IOPort = '',
		Interrupt = ''):

		"""
		  Initializes a PCAN Channel

		Parameters:
		  Channel  : A TPCANHandle representing a PCAN Channel
		  Btr0Btr1 : The speed for the communication (BTR0BTR1 code)
		  HwType   : NON PLUG&PLAY: The type of hardware and operation mode
		  IOPort   : NON PLUG&PLAY: The I/O address for the parallel port
		  Interrupt: NON PLUG&PLAY: Interrupt number of the parallel port

		Returns:
		  A TPCANStatus error code
		"""
		if not self.initialized:
			ret = pcan_module.open_can(self.can_port)
			if ret == 0:
				print 'PCANBasic::Initialize: Port %s opened successfully'%(self.can_port)
				
				if pcan_module.configure_can() == 0:
					print 'PCANBasic::Initialize: Port %s configured'%(self.can_port)
					self.initialized = True
				if pcan_module.get_version_info() == 0:
					print 'PCANBasic::Initialize: PCAN version info = %s'%(pcan_module.cvar.driver_info)
				
			else:
				print 'PCANBasic::Initialize: Error openning port %s'%(self.can_port)
				return 0x10000
		
		return 0

	
    #  Uninitializes one or all PCAN Channels initialized by CAN_Initialize
    #
	def Uninitialize(
		self,
		Channel):

		"""
		  Uninitializes one or all PCAN Channels initialized by CAN_Initialize
		  
		Remarks:
		  Giving the TPCANHandle value "PCAN_NONEBUS", uninitialize all initialized channels
		  
		Parameters:
		  Channel  : A TPCANHandle representing a PCAN Channel

		Returns:
		  A TPCANStatus error code
		"""
		if self.initialized:
			ret = pcan_module.close_can()
			if ret == 0:
				print 'PCANBasic::Uninitialize: Port %s closed successfully'%(self.can_port)
				self.initialized = False
			else:
				print 'PCANBasic::Uninitialize: Error closing port %s'%(self.can_port)
				return 0x10000
		
		return 0

	#  Resets the receive and transmit queues of the PCAN Channel
	#
	def Reset(
		self,
		Channel):

		"""
		  Resets the receive and transmit queues of the PCAN Channel
		  
		Remarks:
		  A reset of the CAN controller is not performed
		  
		Parameters:
		  Channel  : A TPCANHandle representing a PCAN Channel

		Returns:
		  A TPCANStatus error code
		"""
		return 0
            
	#  Gets the current status of a PCAN Channel
	#
	def GetStatus(
		self,
		Channel):

		"""
		  Gets the current status of a PCAN Channel
		  
		Parameters:
		  Channel  : A TPCANHandle representing a PCAN Channel
		
		Returns:
		  A TPCANStatus error code
		"""
		return 0

	# Reads a CAN message from the receive queue of a PCAN Channel
	#
	def Read(
		self,
		Channel):

		"""
		  Reads a CAN message from the receive queue of a PCAN Channel

		Remarks:
		  The return value of this method is a 3-touple, where 
		  the first value is the result (TPCANStatus) of the method.
		  The order of the values are:
		  [0]: A TPCANStatus error code
		  [1]: A TPCANMsg structure with the CAN message read
		  [2]: A TPCANTimestamp structure with the time when a message was read
		  
		Parameters:
		  Channel  : A TPCANHandle representing a PCAN Channel
		
		Returns:
		  A touple with three values
		"""

		msg = TPCANMsg()
		timestamp = TPCANTimestamp()
		ret = pcan_module.read_can_msg()
		res = ret[0]
		
		if res == 0:
			msg.ID = ret[1]
			msg.MSGTYPE = PCAN_MESSAGE_STANDARD
			msg.LEN = 0x8
			for i in range(8):
				msg.DATA[i] = ret[i+2]
			
			#print 'Read: ID = %x, msg = %x, %x, %x, %x, %x, %x, %x, %x'%(msg.ID, msg.DATA[0], msg.DATA[1], msg.DATA[2], msg.DATA[3], msg.DATA[4], msg.DATA[5], msg.DATA[6], msg.DATA[7])	
		    
		return TPCANStatus(res),msg,timestamp
          

	# Transmits a CAN message 
	#
	def Write(
		self,
		Channel,
		MessageBuffer):

		"""
		  Transmits a CAN message 
		  
		Parameters:
		  Channel      : A TPCANHandle representing a PCAN Channel
		  MessageBuffer: A TPCANMsg representing the CAN message to be sent
		
		Returns:
		  A TPCANStatus error code
		"""
		
		data = []
		# data[0] -> CAN ID
		# data[1..8] -> MSG.DATA
		data.append(int(MessageBuffer.ID))
		data.append(int(MessageBuffer.LEN))
		
		for i in range(8):
			data.append(int(MessageBuffer.DATA[i]))
		
		#print 'ID = %x, len = %d, type = %x, data %x %x %x %x %x %x %x %x'%(MessageBuffer.ID, MessageBuffer.LEN, MessageBuffer.MSGTYPE, MessageBuffer.DATA[0],MessageBuffer.DATA[1], MessageBuffer.DATA[2], MessageBuffer.DATA[3], MessageBuffer.DATA[4], MessageBuffer.DATA[5], MessageBuffer.DATA[6], MessageBuffer.DATA[7] )
		
		ret = pcan_module.send_can_msg(data)
		if ret == 0:
			return 0
		else:
			print 'PCANBasic::Write: Error writting on bus'
			return TPCANStatus(0x10000)
			
	

	# Configures the reception filter 
	#
	def FilterMessages(
		self,
		Channel,
		FromID,
		ToID,
		Mode):

		"""
		  Configures the reception filter

		Remarks:
		  The message filter will be expanded with every call to this function.
		  If it is desired to reset the filter, please use the 'SetValue' function.
		
		Parameters:
		  Channel : A TPCANHandle representing a PCAN Channel
		  FromID  : A c_ulong value with the lowest CAN ID to be received
		  ToID    : A c_ulong value with the highest CAN ID to be received
		  Mode    : A TPCANMode representing the message type (Standard, 11-bit 
					identifier, or Extended, 29-bit identifier)
		
		Returns:
		  A TPCANStatus error code
		"""
       
		return 0

	# Retrieves a PCAN Channel value 
	#
	def GetValue(
		self,
		Channel,
		Parameter):

		"""
		  Retrieves a PCAN Channel value

		Remarks:
		  Parameters can be present or not according with the kind
		  of Hardware (PCAN Channel) being used. If a parameter is not available,
		  a PCAN_ERROR_ILLPARAMTYPE error will be returned.
		  
		  The return value of this method is a 2-touple, where 
		  the first value is the result (TPCANStatus) of the method and
		  the second one, the asked value 
		  
		Parameters:
		  Channel   : A TPCANHandle representing a PCAN Channel
		  Parameter : The TPCANParameter parameter to get
		
		Returns:
		  A touple with 2 values
		"""        
		return TPCANStatus(0x0),''
                    

	# Returns a descriptive text of a given TPCANStatus
	# error code, in any desired language
	#
	def SetValue(
		self,
		Channel,
		Parameter,
		Buffer):

		"""
		  Returns a descriptive text of a given TPCANStatus error
		  code, in any desired language

		Remarks:
		  Parameters can be present or not according with the kind
		  of Hardware (PCAN Channel) being used. If a parameter is not available,
		  a PCAN_ERROR_ILLPARAMTYPE error will be returned.
		  
		Parameters:
		  Channel      : A TPCANHandle representing a PCAN Channel
		  Parameter    : The TPCANParameter parameter to set
		  Buffer       : Buffer with the value to be set
		  BufferLength : Size in bytes of the buffer
		
		Returns:
		  A TPCANStatus error code
		"""        
		return TPCANStatus(0x0)
		

	def GetErrorText(
		self,
		Error,
		Language = 0):

		"""
		  Configures or sets a PCAN Channel value

		Remarks:

		  The current languages available for translation are:
		  Neutral (0x00), German (0x07), English (0x09), Spanish (0x0A),
		  Italian (0x10) and French (0x0C)          

		  The return value of this method is a 2-touple, where 
		  the first value is the result (TPCANStatus) of the method and
		  the second one, the error text
		  
		Parameters:
		  Error    : A TPCANStatus error code
		  Language : Indicates a 'Primary language ID' (Default is Neutral(0))
		
		Returns:
		  A touple with 2 values
		"""  
		return TPCANStatus(0x0),''
              
































