import time 
import mace


class AtCommand:
    def __init__():
        self.device = mace.get_context()
            
    def mipi_cmd(mode, die_info, port, usid, addr, data=None):
        """
        mode: 'r' for read, 'w' for write
        die_info: number or DEC number
        port: HEX number or DEC number
        usid: HEX number or DEC number
        addr: HEX number or DEC number
        data: HEX number or DEC number if mode is 'w'
        """
        if mode == 'r':
            self.device_send_at_command(f'"AT+EGCMD=1, \"read_mipi_cw\", \"{die_info}\", {port}, \"{usid}\", \"{addr}\""')
        if mode == 'w':
            self.device_send_at_command(f'"AT+EGCMD=1, \"write_mipi_cw\", \"{die_info}\", {port}, \"{usid}\", \"{addr}\", \"{data}\""')			
    
    def bsi_cmd(mode, cw, data=None):
        """
        mode: 'r' or 'w'
        cw: HEX number or DEC number
        data: HEX number or DEC number if mode is 'w'
        """
        if mode == 'r':
            self.device_send_at_command(f'"AT+EGCMD=1, \"read_bsi_cw\", {cw}"')
        if mode == 'w':
            self.device_send_at_command(f'"AT+EGCMD=1, \"write_bsi_cw\", {cw}, \"{data}\""')			
            
    def reg_cmd(mode, addr, data=None):
        """
        mode: 'r' or 'w'
        addr: HEX number or DEC number
        data: HEX number or DEC number if mode is 'w'
        """
        if mode == 'r':
            self.device_send_at_command(f'"AT+EGCMD=1, \"read_reg\", \"{addr}\""')
        if mode == 'w':
            self.device_send_at_command(f'"AT+EGCMD=1, \"write_reg\", \"{addr}\", \"{data}\""')

    
def main():
    pass
    
    
if __name__ == "__main__":
    main()