import math

def literal(trans):
    number = ''
    while True:
        number += trans[1:5]
        x = trans[0]
        trans = trans[5:]
        if x =='0':
            break
    return int(number,2),trans

def packet(trans):
    pversion,ptype,rest = int(trans[:3],2),int(trans[3:6],2),trans[6:]
    versions,result = 0,0
    if ptype == 4:
        result, rest = literal(rest)
    elif ptype != 4:
        x = rest[0]
        rest = rest[1:]
        subpackets = []
        if x == '0':        #next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            subpacked_length = int(rest[:15],2)
            rest = rest[15:]
            estimatedrestlength = len(rest) - subpacked_length
            while len(rest) > estimatedrestlength:
                subpacket, rest = packet(rest)
                subpackets += [subpacket]
        elif x == '1':       #next 11 bits are a number that represents the number of sub-packets immediately contained by this packet
            subpacked_count = int(rest[:11],2)
            rest = rest[11:]
            for _ in range(subpacked_count):
                subpacket, rest = packet(rest)
                subpackets += [subpacket]
        versions = sum([x[0] for x in subpackets])
        if ptype == 0:  
            result = sum([x[2] for x in subpackets])
        elif ptype == 1:
            result = math.prod([x[2] for x in subpackets])
        elif ptype == 2:
            result = min([x[2] for x in subpackets])
        elif ptype ==3:
            result = max([x[2] for x in subpackets])
        elif (ptype ==5 and subpackets[0][2]>subpackets[1][2]) or \
            (ptype ==6 and subpackets[0][2]<subpackets[1][2]) or \
            (ptype ==7 and subpackets[0][2]==subpackets[1][2]):
            result = 1 
    a = (pversion+versions,ptype,result)
    return a, rest

def Main():
    transmission = ''.join(['0'*(6-len(bin(int(x,base=16)))) +str(bin(int(x,base=16)))[2:] for x in open('2021/day16/input.txt').read().strip()])
    packets = packet(transmission)
    print('part1',packets[0][0])
    print('part2',packets[0][2])

if __name__ == '__main__':
    Main()
