def main():
 print ('starting')
 with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        #print(file_contents)

        ab = f'{file_contents}'
        words = ab.split()
        count = 0
        for word in words:
            count += 1
        print (count)

        lowered = file_contents.lower()
        #print(lowered)

        letter_count = {'a':0,
                        'b':0,
                        'c':0,
                        'd':0,
                        'e':0,
                        'f':0,
                        'g':0,
                        'h':0,
                        'i':0,
                        'j':0,
                        'k':0,
                        'l':0,
                        'm':0,
                        'n':0,
                        'o':0,
                        'p':0,
                        'r':0,
                        's':0,
                        't':0,
                        'u':0,
                        'w':0,
                        'x':0,
                        'y':0,
                        'z':0}
        
        for letter in lowered:
            if letter in letter_count:
                letter_count[letter] +=1
        print(letter_count)
 
        character_list=[]
        for char, num in letter_count.items():
            character_list.append({'char':char, 'num':num})
        def sort_on(dict):
            return dict['num']
        
        character_list.sort(reverse = True, key=sort_on)
        print('Starting report')
        print(f'{count} words found in the document\n')
        
        for char_dict in character_list:
         print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

        print("--- End report ---")





main()  