from tkinter import *
from jap_data import temp_data
from scrollframe import VerticalScrolledFrame

class JapEngFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self._initialize()

    def _initialize(self):
        self.master.title('Japanese-English Dictionary')
        self.pack(fill=BOTH, expand=1)

        self._search_string = StringVar()
        searchFrame = Frame(self)

        # Search TextBox
        search_input_frame = Frame(
                            searchFrame,
                            bg='gray25',
                            padx=2,
                            pady=2,
                        )

        search_input  = Entry(
                            search_input_frame,
                            textvariable=self._search_string,
                            relief=FLAT,
                            bd=3,
                            font='Helvetica 10',
                            width=50
                        )

        search_input.pack(fill=BOTH, expand=1)

        # Search Button
        search_button = Button(
                            searchFrame, 
                            text='SEARCH',
                            command=self._search_dictionary,
                            borderwidth=2,
                            padx=5,
                            pady=2,
                            bg='gray25',
                            fg='white',
                            font='Helvetica 8 bold'
                        )

        # Result Container
        result_cont = VerticalScrolledFrame(
                        self,
                    )

        # search_input_frame.pack()
        # search_button.pack()
        searchFrame.pack(fill=BOTH, expand=1)

        # Layout
        search_input_frame.grid(
                        column=0,
                        row=0,
                        padx=5,
                        pady=10,
                        sticky=(E, W)
                    )
        search_button.grid(
                        column=1,
                        row=0,
                        padx=2,
                        pady=10
                    )
        # result_cont.grid(
                        # column=0,
                        # row=1,
                        # padx=2,
                        # pady=5,
                        # columnspan=2,
                        # sticky=(N, E, S, W)
                    # )

        self._result_cont = result_cont
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

    def _search_dictionary(self):
        # TODO Orjan, Rap: tatawagin tong function pag pinindot ung search button
        # nasa 'self._search_string' na variable ung ni-type sa input box
        self._test();
        pass

    def _test(self):
        for i in range(len(temp_data)):
            self._add_entry(temp_data[i], i)

    def _add_entry(self, entry, index):
        kana  = entry.get('kana')
        kanji = entry.get('kanji', '')
        defs  = entry.get('definitions')

        entryFrame = Frame(self._result_cont.interior)
        entryFrame.grid(column=0, row=index, sticky=W, pady=10)
        entryFrame.columnconfigure(0, weight=0)
        entryFrame.columnconfigure(1, weight=1)
        defFrame   = Frame(entryFrame)
        defFrame.grid(column=0, row=1, columnspan=2, sticky=W, padx=10, pady=5)
        kanaLabel  = Label(entryFrame, text=kana, font='MS-Gothic 12 bold', fg='blue4')
        kanaLabel.grid(column=0, row=0)

        if kanji != '':
            kanjiLabel = Label(entryFrame, text=f'【 {kanji} 】', font='MS-Gothic 12 bold', fg='brown4')
            kanjiLabel.grid(column=1, row=0, sticky=W)

        for i in range(len(defs)):
            data = defs[i]
            form = data.get('form', '')
            definition = data.get('definition')
            numLabel = Label(defFrame, text=f'{i+1}.', fg='steelblue3', font='Helvetica 10')
            numLabel.grid(column=0, row=i, sticky=W)

            if len(form) != 0:
                text = f' ('
                for j in range(len(form)):
                    if j == len(form) - 1:
                        text += form[j]
                    else:
                        text += f'{form[j]}, '
                text += f') {definition}'
            else:
                text = f' {definition}'

            defLabel  = Label(defFrame, text=text, font='Helvetica 10')
            defLabel.grid(column=1, row=i, sticky=(W))

        defFrame.columnconfigure(0, weight=0)
        defFrame.columnconfigure(1, weight=0)
        self._result_cont.pack()

        pass