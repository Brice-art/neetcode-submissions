class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            size = len(s)
            if size < 10:
                encoded_str += f'#th{size}{s}'
            elif size < 100:
                encoded_str += f'#h{size}{s}'
            else:
                encoded_str += f'#{size}{s}'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        while i < len(s):
            if s[i] == '#':
                if s[i+1] == 't':
                    length = int(s[i+3])
                elif s[i+1] == 'h':
                    length = int(s[i+2:i+4])
                else:
                    length = int(s[i+1:i+4])
                decoded_strs.append(s[i+4:length+i+4])
                i += length + 4


        return decoded_strs
