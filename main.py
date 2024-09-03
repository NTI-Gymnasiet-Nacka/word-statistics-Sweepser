# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)


def read_from_file(path: str): #https://www.geeksforgeeks.org/python-program-to-count-words-in-text-file/

    with open(path, "r" ,encoding="utf-8") as f: 
        data=f.read()
        words=data.split()
        return words

        
def most_frequent(words): #https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    
    counter=0
    num=words[0]
    for i in words:
        curr_frequency = words.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num

 

def word_length(words):
    total_length=sum(len(word)for word in words)
    return total_length/len(words)

def main():

    words=read_from_file("en_resa_genom_svenska_skogen.txt")
    
    number_of_words=len(words)
    print(f'{number_of_words}')

    most_common_word=most_frequent(words)
    print(f'{most_common_word}')

    average_length=word_length(words)
    print(f'{average_length}')


    
if __name__ == "__main__":
    main()