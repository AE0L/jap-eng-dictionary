from tkinter import *
from tkinter.ttk import Style
from jap_data import dict_data
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

        # COMPONENTS
        search_cont    = Frame(self)
        result_wrapper = Frame(self)
        result_cont    = VerticalScrolledFrame(result_wrapper)

        search_cont.grid(column=0, row=0, sticky=(W, E), padx=5, pady=5)
        result_wrapper.grid(column=0, row=1, sticky=(S, N, W, E), pady=5)
        result_cont.pack(fill=BOTH, expand=1, padx=5)

        search_input_wrapper = Frame(search_cont,
                                borderwidth=2, 
                                background='dimgray')
        search_input         = Entry(search_input_wrapper,
                                textvariable=self._search_string,
                                borderwidth=3,
                                relief='flat',
                                font='Helvetica 14')
        search_button        = Button(search_cont,
                                command=self.shounenJumpuSearch,
                                text='Search',
                                font='Helvetica 13 bold',
                                activebackground='gray10',
                                activeforeground='white')

        search_input_wrapper.grid(column=0, row=0, sticky=(E,W))
        search_input.pack(fill=BOTH, expand=1)
        search_button.grid(column=1, row=0, sticky=(E), padx=5, ipadx=7.5)

        self._result_cont = result_cont

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self._result_cont.columnconfigure(0, weight=1)
        search_cont.columnconfigure(0, weight=1)
        search_cont.columnconfigure(1, weight=0)



    def square_root(number, number_iters = 500):
        a = float(number)
        for r in range(number_iters):
            number = 0.5 * (number + a / number)
        return number

    def shounenJumpuSearch (dict_data):    
        self._clear_result()
        search_string = self._search_string.get()
        def _search_dictionary(search,self1):
          
            a = len(search_string)
            b = 0
            x = 0
            y = 0
            for i in range(len(dict_data)):
                b = len(dict_data[i]['romaji'])
                x = 0
                for x in range(b):
                    y = 0
                    for y in range(a):
                        try:
                            if dict_data[i]['romaji'][x + y] != search_string[y]:
                                break
                        except:
                            break
                        y = y + 1
                    if y == a:
                        self1._add_entry(dict_data[i], i)

            for i in range(len(dict_data)):
                b = len(dict_data[i]['definition'])
                x = 0
                for x in range(b):
                    y = 0
                    for y in range(a):
                        try:
                            if dict_data[i]['definition'][x + y] != search_string[y]:
                                break
                        except:
                            break
                            y = y + 1
                    if y == a:
                        self1._add_entry(dict_data[i], i)

        length = len(dict_data[i]['romaji'])
        jump = int(square_root(length))
        left, right = 0, 0
        while length > left & search >= dict_data[left]:
            right = min(length - 1, left + jump)
            if dict_data[left] <=    search and dict_data[right] >= search:
                break
            left += jump;
        if left >= length or dict_data[left] > search:
            return -1
        right = min(length - 1, right)
        w = left
        while w <= right and dict_data[w] <= search:
            if dict_data[w] == search:
                return w
            w += 1
        return -1






    def _add_entry(self, entry, index):
        kana       = entry.get('kana')
        romaji     = entry.get('romaji')
        kanji      = entry.get('kanji')
        definition = entry.get('definition')
        entry_cont = Frame(self._result_cont.interior,
                            highlightbackground='dimgray',
                            highlightthickness=1)

        self._result_cont.interior.columnconfigure(0, weight=1)

        kanji_label      = Label(entry_cont,
                            text=kanji,
                            font='MS-Gothic 12 bold')
        romaji_label     = Label(entry_cont,
                            text=romaji,
                            font='Helvetica 8')
        kana_label       = Label(entry_cont,
                            text=f'【{kana}】',
                            font='MS-Gothic 12 bold')
        definition_label = Label(entry_cont,
                            text=definition,
                            font='Arial 12')

        kanji_label.grid(column=0,
                            row=1,
                            padx=(10, 0))
        kana_label.grid(column=1,
                            row=1,
                            padx=(0,10),
                            sticky=W)
        romaji_label.grid(column=1,
                            row=0,
                            sticky=W,
                            padx=(20, 0))
        definition_label.grid(column=0,
                            row=3,
                            columnspan=2,
                            sticky=W,
                            padx=10,
                            pady=10)
        entry_cont.grid(row=index,
                            sticky=(W,E),
                            pady=10)

        entry_cont.columnconfigure(0, weight=0)
        entry_cont.columnconfigure(1, weight=1)

        self._result_cont.pack()

        pass

    def _clear_result(self):
        self._result_cont.destroy()
        
        result_wrapper = Frame(self)
        self._result_cont = result_cont = VerticalScrolledFrame(result_wrapper)

        result_wrapper.grid(column=0, row=1, sticky=(S, N, W, E), pady=5)
        result_cont.pack(fill=BOTH, expand=1, padx=5)
