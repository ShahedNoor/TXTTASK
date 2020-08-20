banner = """
\033[0;31m
████████╗██╗  ██╗████████╗████████╗ █████╗ ███████╗██╗  ██╗
╚══██╔══╝╚██╗██╔╝╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
   ██║    ╚███╔╝    ██║      ██║   ███████║███████╗█████╔╝ 
   ██║    ██╔██╗    ██║      ██║   ██╔══██║╚════██║██╔═██╗ 
   ██║   ██╔╝ ██╗   ██║      ██║   ██║  ██║███████║██║  ██╗
   ╚═╝   ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
\033[32;1m
Author		: r1d3x0r
Tools Name	: TXTTASK
Version		: 1.0                                                  
"""
print(banner)
numberoftexts = int(input("Number Of Texts: "))
text = input("Enter Your Text: ")
counter = 1
while counter <= numberoftexts:
 print(text)
 counter = counter + 1
