from tkinter import *


def main():
    root = Tk()

    def quit_me():  # define quit behavior
        print('quit')
        root.quit()
        root.destroy()

    def openStartPage():  # Opens Start Page
        gameTitleStart.destroy()
        startBTN.destroy()
        instructsBTN.destroy()
        quitBTN.destroy()

        tempInstructionsTitle = Label(root, text="Start Page Placeholder", font='Helvetica 25 bold')
        tempInstructionsTitle.place(relx='.5', rely='.07', anchor=CENTER)

    def openInstructionsPage():  # Opens Instructions Page
        gameTitleStart.destroy()
        startBTN.destroy()
        instructsBTN.destroy()
        quitBTN.destroy()

        tempInstructionsTitle = Label(root, text="Instructions Page Placeholder", font='Helvetica 25 bold')
        tempInstructionsTitle.place(relx='.5', rely='.07', anchor=CENTER)

    root.protocol("WM_DELETE_WINDOW", quit_me)
    root.title("CS2450-Ethics-Game")  # this is a simple placeholder until we get a real title
    root.geometry('900x700')  # Window screen size which can be changed
    root.iconbitmap('./images/PlaceholderIcon.ico')  # Placeholder for a simple window icon
    root.config(bg='#75cdff')  # Set the default color of the window

    gameTitleStart = Label(root, text="CS305G Game Title Placeholder", font='Helvetica 25 bold')
    gameTitleStart.place(relx='.5', rely='.07', anchor=CENTER)

    startBTN = Button(root, text='START', command=lambda: openStartPage(), height=2,
                      width=8, font='Helvetica 25 bold')
    startBTN.place(relx='.5', rely='.25', anchor=CENTER)

    instructsBTN = Button(root, text='Instructions', command=lambda: openInstructionsPage(), height=2,
                          width=12, font='Helvetica 25 bold')
    instructsBTN.place(relx='.5', rely='.5', anchor=CENTER)

    quitBTN = Button(root, text='Quit', command=lambda: quit_me(), height=2,
                     width=8, font='Helvetica 25 bold')
    quitBTN.place(relx='.5', rely='.75', anchor=CENTER)

    root.mainloop()


if __name__ == '__main__':
    main()
