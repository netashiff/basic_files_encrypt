__author__ = 'DELL'
__author__ = 'Neta'
import operator

frequency_d_s = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y',
                 'b', 'v', 'k', 'x', 'j', 'q', 'z']
frequency_c = [',', '.', '-',  '"', '_', ')', '(', ';', '0', '1', '=', '2', ':', '/', '*', '!', '?', '$', '3', '5',
               '>', '{', '}', '4', '9', '[', ']', '8', '6', '7', '\\', '+', '|', '&', '<', '%', '@', '#', '^', '`', '~']


class kisar_vis():

    def __init__(self, text):
        self.text = text.lower()

    def organize_dics(self, lowecase_letter):
        #organize the frquency of the letter to list from dictionary
        #return the list
        sorted_x = sorted(lowecase_letter.items(), key=operator.itemgetter(1))
        letter = []
        i = len(sorted_x) - 1
        while i >= 0:
            letter.append(sorted_x[i][0])
            i -= 1
        print letter
        return letter

    def coded_ceasar(self, organize_d, frequency_d, text):
        #encypsion ceasar1
        organize_l = organize_d[0]
        organize_si = organize_d[1]
        if len(organize_d) > 0:
            key = ord(frequency_d[0])-ord(organize_d[0])
            newtext = ""
            for i in text:
                cheng = ord(i) + key
                newtext += str(chr(cheng))
            print "coded 1" + newtext
            return newtext

    def coded_vinser(self, organize_d, frequency_d, text):
        #encypsion
        organize_l = organize_d[0]
        organize_si = organize_d[1]
        newtext = ""
        for i in text:
            if i in organize_l:
                #check if it is letter
                num_l = [u for u, x in enumerate(organize_l) if x == i]
                num_l = num_l[0]
                #find the place of the letter in list
                key = ord(i) - ord(frequency_d[num_l])
                cheng = ord(i) + key
                print key
                newtext += str(chr(cheng))
            elif i in organize_l:
                #if it isn't a letter
                #key =
                cheng = ord(i) + key
                print key
                newtext += str(chr(cheng))
        print "decode 2 : " + newtext
        return newtext

    def decode_ceasare(self, organuize_d, frequency_d, text):
        #change just checking the first letter
        organuize_l = organuize_d[0]
        organuize_si = organuize_d[1]
        if len(organuize_d) > 0:
            key = ord(organuize_l[0]) - ord(frequency_d[0])
            newtext = ""
            for i in text:
                cheng = ord(i) - key
                print i
                print cheng
                newtext += str(chr(cheng))
            print key
            print "decode 1 : " + newtext
        else:
            newtext = ""
        return newtext

    def decode_vinser(self, organize_d, frequency_d, text):
        #change just checking the frequency in the english languish and changh about every letter
        #return the decode text
        organize_l = organize_d[0]
        organize_si = organize_d[1]
        newtext = ""
        for i in text:
            if i in organize_l:
                #check if it is letter
                num_l = [u for u, x in enumerate(organize_l) if x == i]
                num_l = num_l[0]
                #find the place of the letter in list
                key = ord(i) - ord(frequency_d[num_l])
                cheng = ord(i) - key
                print key
                newtext += str(chr(cheng))
            elif i in organize_l:#if it isn't a letter
               # key =
                cheng = ord(i) - key
                print key
                newtext += str(chr(cheng))
        print "decode 2 : " + newtext
        return newtext

    def reconize(self):
        #sorter the letters in the text file
        lowercase_letter = {'a': 0,
                            'b': 0,
                            'c': 0,
                            'd': 0,
                            'e': 0,
                            'f': 0,
                            'g': 0,
                            'h': 0,
                            'i': 0,
                            'j': 0,
                            'k': 0,
                            'l': 0,
                            'm': 0,
                            'n': 0,
                            'o': 0,
                            'p': 0,
                            'q': 0,
                            'r': 0,
                            's': 0,
                            't': 0,
                            'u': 0,
                            'v': 0,
                            'w': 0,
                            'x': 0,
                            'y': 0,
                            'z': 0,
                            }
        non_letters = {',': 0,
                       '.': 0,
                       '-': 0,
                       '"': 0,
                       '_': 0,
                       ')': 0,
                       '(': 0,
                       ';': 0,
                       '0': 0,
                       '1': 0,
                       '=': 0,
                       '2': 0,
                       ':': 0,
                       '/': 0,
                       '*': 0,
                       '!': 0,
                       '?': 0,
                       '$': 0,
                       '3': 0,
                       '5': 0,
                       '>': 0,
                       '{': 0,
                       '}': 0,
                       '4': 0,
                       '9': 0,
                       '[': 0,
                       ']': 0,
                       '8': 0,
                       '6': 0,
                       '7': 0,
                       '\\': 0,
                       '+': 0,
                       '|': 0,
                       '&': 0,
                       '<': 0,
                       '%': 0,
                       '@': 0,
                       '#': 0,
                       '^': 0,
                       '`': 0,
                       '~': 0
            }
        print self.text
        for i in self.text:
            if i in lowercase_letter:
                lowercase_letter[i] = lowercase_letter.get(i) + 1
            else:
                if i in non_letters:
                    non_letters[i] = non_letters.get(i) + 1
                else:
                    non_letters[i] = 1
        print non_letters
        return self.organize_dics(lowercase_letter), self.organize_dics(non_letters)
