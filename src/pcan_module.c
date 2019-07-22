/*
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
*/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>   // exit
#include <signal.h>
#include <string.h>
#include <stdlib.h>   // strtoul
#include <fcntl.h>    // O_RDWR
#include <unistd.h>

#include <libpcan.h>
#include <ctype.h>

HANDLE h;
char driver_info[64] = "\0";

int open_can(char *dev){
	// open CAN port
	//const char *szDevNode = DEFAULT_NODE;
	// O_NONBLOCK - non blocking read 
	// O_RDWR - blocking read - function returns only if there is something in the buffer to read
	h = LINUX_CAN_Open(dev, O_RDWR | O_NONBLOCK);
	
	if (!h) {
		//printf("PCan::Open: can't open %s\n", dev);
		return -1;
	}
	
	// clear status
	CAN_Status(h);
	
	return 0;
}

int close_can(){
	CAN_Close(h);
}

int get_version_info(){
	
	errno = CAN_VersionInfo(h, driver_info);
	if(!errno){
		
		return 0;
	}else{
		//printf("Error getting the version info\n"); 
		return -1;
	}
	
}

int configure_can(){
	
  // init to a user defined bit rate
	errno = CAN_Init(h, CAN_BAUD_1M, CAN_INIT_TYPE_ST); 
	if (errno) {
		printf("CAN_Init() failed\n");
		return -1;
	}

	return 0;
}


int send_can_msg(const int num_elements, int *data){
	TPCANMsg tpcmsg;
    tpcmsg.ID = data[0];	// ID in data[0]
    tpcmsg.LEN = data[1];      //Message size in data[1]
    tpcmsg.MSGTYPE = MSGTYPE_STANDARD;
    int i = 0;
    
    for(i = 0; i < 8; i++){
		tpcmsg.DATA[i] = data[i+2];
	}
    
    //printf("send_can_msg: ID = %x, LEN = %x, TYPE = %d, DATA = %x %x %x %x %x %x %x %x \n", tpcmsg.ID, tpcmsg.LEN, tpcmsg.MSGTYPE, tpcmsg.DATA[0], tpcmsg.DATA[1], tpcmsg.DATA[2], tpcmsg.DATA[3], tpcmsg.DATA[4], tpcmsg.DATA[5], tpcmsg.DATA[6], tpcmsg.DATA[7] );
    
	CAN_Write( h, &tpcmsg );
	int iRet = CAN_Status(h);
	if(iRet < 0){
		// 
		int err = nGetLastError();
		printf("send_can_msg: error in CAN_Write() errno=%d iRet=%d nGetLastError=%d\n", errno, iRet, err );
		return -1;
	}

	return 0;
}

int * read_can_msg(){
	int i= 0, j = 0;
	TPCANRdMsg tpcmsg;
	int last_err = 0;
	
	static int output[10];
	output[0] = 0;	//ret
	output[1] = 0;	//ID
	
	int ret = 0;
	
	int iRet = LINUX_CAN_Read(h, &tpcmsg);
	
    if (iRet == CAN_ERR_OK){
        if (tpcmsg.Msg.MSGTYPE == MSGTYPE_STANDARD) {
			// MSG
			for(i = 2, j = 0; i < 10; i++, j++){
				output[i] = tpcmsg.Msg.DATA[j]; 
			}
			output[1] = tpcmsg.Msg.ID;
        	output[0] = 0;
        	return output;
		}else {		
			output[0] = 1;
			return output;
		}
	}else if(tpcmsg.Msg.MSGTYPE == MSGTYPE_STATUS){  
		if (iRet < 0) {
			last_err = nGetLastError();
			printf("PCan::Read: error in LINUX_CAN_Read() - MSGTYPE_STATUS - err=%d", last_err);
			
			output[0] = -1;    
			return output;            
		}
		if (iRet & CAN_ERR_QRCVEMPTY){
			output[0] = 1;
			return output;
		}
	}

	// Este caso no esta claro : last_err da 11, iRet -1 y son tramas de longitud 4, todo a 0
	//  id=1, len=4, data[ 0 0 0 0 0 0 0 0 ]
	if (iRet & CAN_ERR_QRCVEMPTY) {
		output[0] = 1;
		return output;
	}

	last_err = nGetLastError();
	// this ret values appeared in late library version but it doesn't mean error
	if(iRet != 11)
		printf("PCan::Read: error in LINUX_CAN_Read, iRet=%d  err=%d", iRet, last_err);      
	// ERROR
	
	output[0] = -1;	//ret
	
	return output;
}


int main(){
	int ret = open_can("/dev/pcan32");
	int ID = 0x602;
	//unsigned char data[8];
	int data[10];
	unsigned char *data2;// = 8*malloc(unsigned char);
	int *ret_data; 
	
	data[0] = 0x602;
	data[1] = 0x4;
	data[2] = 0x05;
	data[3] = 0x06;
	data[4] = data[5] = data[6] = data[7] = data[8] = data[9] = 0;
	
	if(ret >= 0){
		printf("CAN opened!\n");
		get_version_info();
		printf("Can info = %s!\n", driver_info);
		printf("Configuring = %d\n", configure_can());
		//printf("Sending data = %d\n", send_can_msg(ID, data));
		//printf("Sending data = %d\n", send_can_msg(9, data));
		ret_data = read_can_msg();
		//printf("Reading data = %d\n", ret_data[0]);
		//unsigned char c = 1;
		//data2 = read_can_msg(&ID);
		//printf("Reading data = %d\n", read_can_msg(&ID, data));
		//printf("ID = %d, data=%d%d%d%d%d%d%d%d\n", ID, data[0],data[1],data[2],data[3],data[4], data[5],data[6],data[7]);
		//printf("ID = %d, data=%d%d%d%d%d%d%d%d\n", ID, data2[0],data2[1],data2[2],data2[3],data2[4], data2[5],data2[6],data2[7]);
		//printf("ID = %d, data=%s\n", ID);
		//printf("ID = %d, data=%d\n", ID, c);
		
		
		sleep(2);
		close_can();
	}
	
	return 0;
	
}


