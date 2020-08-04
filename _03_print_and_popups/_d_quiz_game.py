from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    questions = ['What is 12^2?', 'What is 2^6', 'What is the capitol of New Jersey',
                 'What is the capitol of Kentucky']
    answers = ['144', '64', 'trenton', 'frankfort']
    for q, a in zip(questions, answers):
        ans = simpledialog.askstring(None, q)
        if ans.lower() == a:
            score+=1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo('Score', 'Your score was ' + str(score) + '/4')
    # Run the window's .mainloop() method
    window.mainloop()