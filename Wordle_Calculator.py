import tkinter as tk
import json

#TODO: make a clause that doesnt allow the use to enter nothing for those 2 boxes
    
def get_words():
    wrd = entry1.get()
    letters1 = entry2.get()
    positions = entry3.get()
    letters2 = entry4.get()
    
    if letters1 != "0":
        for i in range(len(positions)):
            knownLetters.append(letters1[i])
            num = int(positions[i])-1
            word[num] = letters1[i]
    if letters2 != "0":
        for i in letters2:
            knownLetters.append(i)
        
    for letter in wrd:
        if letter not in letters1 and letter not in letters2:
            not_in_word.append(letter)
            if letter in alphabet:
                alphabet.remove(letter)
    
    listbox = tk.Listbox(root, height=5)
    listbox.pack()
    label = tk.Label(root, text="Choose a word and start back from step 1")
    label.pack()
    for keys in dic:
        if len(keys) == 5:
            if letters1 == "0" and letters2 == "0":
                cnt3 = 0
                for i in range(5):
                    if keys[i] not in not_in_word:
                        cnt3 = cnt3 + 1
                        if cnt3 == 5: 
                            listbox.insert(tk.END, keys)
                            entry1.delete(0, tk.END)
                            entry2.delete(0, tk.END)
                            entry3.delete(0, tk.END)
                            entry4.delete(0, tk.END)
            else:
                if word == ["0", "1", "2", "3", "4"]:
                    cnt2 = 0
                    for i in range(5):
                        if keys[i] not in not_in_word:
                            cnt2 = cnt2 + 1
                            if cnt2 == 5:
                                ugh2 = 0
                                for j in knownLetters:
                                    if j in keys:
                                        ugh2 = ugh2 + 1
                                        if ugh2 == len(knownLetters):
                                            if letters2 != "0":
                                                for l in letters2:
                                                    if keys.index(l) != wrd.index(l):
                                                        listbox.insert(tk.END, keys)
                                                        entry1.delete(0, tk.END)
                                                        entry2.delete(0, tk.END)
                                                        entry3.delete(0, tk.END)
                                                        entry4.delete(0, tk.END)
                                            else:
                                                listbox.insert(tk.END, keys)
                                                entry1.delete(0, tk.END)
                                                entry2.delete(0, tk.END)
                                                entry3.delete(0, tk.END)
                                                entry4.delete(0, tk.END)

                if word != ["0", "1", "2", "3", "4"]:
                    cnt = 0
                    for i in range(5):
                        if word[i] == "0" or word[i] == "1" or word[i] == "2" or word[i] == "3" or word[i] == "4" or keys[i] == word[i]:
                            if keys[i] not in not_in_word:
                                cnt = cnt + 1
                                if cnt == 5:
                                    ugh = 0
                                    for j in knownLetters:
                                        if j in keys:
                                            ugh = ugh + 1
                                            if ugh == len(knownLetters):
                                                if letters2 != "0":
                                                    for l in letters2:
                                                        if keys.index(l) != wrd.index(l):
                                                            listbox.insert(tk.END, keys)
                                                            entry1.delete(0, tk.END)
                                                            entry2.delete(0, tk.END)
                                                            entry3.delete(0, tk.END)
                                                            entry4.delete(0, tk.END)
                                                else:
                                                    listbox.insert(tk.END, keys)
                                                    entry1.delete(0, tk.END)
                                                    entry2.delete(0, tk.END)
                                                    entry3.delete(0, tk.END)
                                                    entry4.delete(0, tk.END)

root = tk.Tk()
root.title("Wordle Calculator")
root.geometry("500x750")

with open('5_letter_words.json', 'r') as f:
    dic = json.load(f)

#create lists
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
not_in_word = []
word = ["0", "1", "2", "3", "4"]
knownLetters = []

# Create entry widgets for user input
label1 = tk.Label(root, text="Enter word below")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
label2 = tk.Label(root, text="Enter letters in the correct position (if none, enter 0)")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
label3 = tk.Label(root, text="If you entered anything above, enter the position of the correct letters (ex. 125)")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()
label4 = tk.Label(root, text="Enter valid letters in the wrong position if any (if none, enter 0)")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

calcButton = tk.Button(root, text="Calculate", command=get_words)
calcButton.pack()


# Start the event loop
root.mainloop()
