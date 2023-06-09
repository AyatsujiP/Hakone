# importing required librarys
import PySimpleGUI as sg
import subprocess
import copy
import fenparser
import showpng
import io


bc_alice_blue = '#f0f8ff'
light_color_square = '#b0c4de'
dark_color_square = '#4682b4'
focused_square = '#f0e6ac'
version = "v0.02"
files = ["a","b","c","d","e","f","g","h"]
timeout_sec = 6000

pieces_ret = showpng.return_pngs()
png_wk = pieces_ret[0]
png_wq = pieces_ret[1]
png_wr = pieces_ret[2]
png_wb = pieces_ret[3]
png_wn = pieces_ret[4]
png_wp = pieces_ret[5]
png_bk = pieces_ret[6]
png_bq = pieces_ret[7]
png_br = pieces_ret[8]
png_bb = pieces_ret[9]
png_bn = pieces_ret[10]
png_bp = pieces_ret[11]

with open("pictures/empty.png",mode="rb") as f:
    png_emf = f.read()
    png_em = io.BytesIO(png_emf)

pieces_img = {"bk": png_bk.getvalue(),"wk": png_wk.getvalue(), "bq": png_bq.getvalue(),"wq":png_wq.getvalue(),
    "br":png_br.getvalue(),"wr":png_wr.getvalue(),"bb":png_bb.getvalue(),"wb":png_wb.getvalue(),
    "bn": png_bn.getvalue(),"wn":png_wn.getvalue(),"bp":png_bp.getvalue(),"wp":png_wp.getvalue(),"em":png_em.getvalue()}

initial_board = [["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["em","em","em","em","em","em","em","em"],
    ["em","em","em","em","em","em","em","em"],
    ["em","em","em","em","em","em","em","em"],
    ["em","em","em","em","em","em","em","em"],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"]]

image_size_main = (50,50)
main_image_subsample = 1
image_size_add = (40,40)
add_image_subsample = 1

def call_engine(values,engine='stelvio'):
    with open("problems.txt","w") as f:
         f.write("#{}\n{}\n{}\n".format(values["title"],values["forsyth"],int(float(values["mn"])*2)))
    subprocess.run(["{}".format(values["-jdk-"]), "-Xmx{}g".format(values["-mem-"]), "-jar", "engine\\bin\\stelvio11.jar"])



def show_result():
    with open("problems_out.txt") as f:
        ret = f.read()
    return ret



def create_layout():
    layout = []
    col1 = []
    for y in range(8):
        inner = []
        for x in range(8):
            inner.append(sg.Button(button_text='',image_data=pieces_img[initial_board[y][x]],image_size=image_size_main,image_subsample=main_image_subsample,
                          border_width=0, button_color= dark_color_square if ((x + y) % 2) else light_color_square,
                          pad=(0, 0), key='-sq{}{}board{}{}-'.format(files[x],8-y,y,x)))
        
        col1.append(inner.copy())
    col2 = [[sg.Push(),sg.Text('Hakone {}\n GUI wrapper for PG Solving Engine'.format(version))]]
    col2.append([sg.Text("JDK path"),
        sg.Input(default_text="c:\\jdk\\jdk17\\bin\\javaw",key="-jdk-",size=(30,1)),
        sg.Text("Memory (GB)"),
        sg.Input(default_text='8',key="-mem-",size=(5,1))])
    col2.append([sg.Text("Result:")])
    col2.append([sg.Multiline('',size=(60,20),key="-res-")])
    #Board and result layout
    layout.append([sg.Column(col1),sg.Column(col2)])

    inner = []
    
    #Pieces for adding
    inner.append(sg.Button(button_text='',image_data=png_bk.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-bk'))
    inner.append(sg.Button(button_text='',image_data=png_bq.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-bq'))
    inner.append(sg.Button(button_text='',image_data=png_br.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-br'))
    inner.append(sg.Button(button_text='',image_data=png_bb.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-bb'))
    inner.append(sg.Button(button_text='',image_data=png_bn.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-bn'))
    inner.append(sg.Button(button_text='',image_data=png_bp.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-bp'))
    layout.append(inner.copy())

    inner = []
    inner.append(sg.Button(button_text='',image_data=png_wk.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-wk'))
    inner.append(sg.Button(button_text='',image_data=png_wq.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-wq'))
    inner.append(sg.Button(button_text='',image_data=png_wr.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                           border_width=0, button_color= bc_alice_blue,
                           pad=(0, 0), key='-outside-wr'))
    inner.append(sg.Button(button_text='',image_data=png_wb.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-wb'))
    inner.append(sg.Button(button_text='',image_data=png_wn.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-wn'))
    inner.append(sg.Button(button_text='',image_data=png_wp.getvalue(),image_size=image_size_add,image_subsample=add_image_subsample,
                          border_width=0, button_color= bc_alice_blue,
                          pad=(0, 0), key='-outside-wp'))

    layout.append(inner.copy())

    layout.append([sg.Text('Title     '),sg.Input(key='title',size=(102,1))])
    layout.append([sg.Text('Forsyth'),sg.Input(default_text='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',key="forsyth",size=(60,1)),
        sg.Button('load',pad=(10,0)),sg.Text("Move number (e.g. 10.5)"), sg.Input(default_text="0",key="mn",size=(5,1)),sg.Button('clear',pad=(0,0))])

    layout.append([sg.Button('Solve with PG Solving Engine'),sg.Button('Reset')])   

    return layout

def main():
    sg.theme('Lightblue2')
    move_board = copy.deepcopy(initial_board)
    layout = create_layout()
    window = sg.Window('Hakone {}'.format(version), layout)
    #is the departure square is set
    move_from_set = False
    #coordination of the departure square
    move_from_square = None
    #coordination of the arrival square
    move_to_square = None
    #idx of dep.square
    move_from_index = None
    #idx of arrival square
    move_to_index = None
    #is "adding a piece" mode?
    from_outside = False
    add_piece = ""

    #GUI main loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        elif event == 'Solve with PG Solving Engine':
            #call engine and view
            call_engine(values)
            ret = show_result()
            window["-res-"].update(ret)
        #return to the initial status
        elif event == 'Reset':
            move_board = copy.deepcopy(initial_board)
            for y in range(8):
                for x in range(8):
                    window['-sq{}{}board{}{}-'.format(files[x],8-y,y,x)].update(image_data=pieces_img[initial_board[y][x]],image_size=image_size_main,image_subsample=main_image_subsample)
            forsyth = fenparser.read_fen_from_current_position(move_board)
            window["forsyth"].update(forsyth)
            move_from_set = False
            move_from_square = None
            move_to_square = None
            move_from_index = None
            move_to_index = None
            from_outside = False
            add_piece = ""
            window["-res-"].update('')
            window["mn"].update('0')

        elif event == 'clear':
            window["mn"].update('0')
        #fen
        elif event == 'load':
            try:
                move_board = fenparser.load_fen(window["forsyth"].Get())
                move_from_set = False
                move_from_square = None
                move_to_square = None
                move_from_index = None
                move_to_index = None
                from_outside = False
                for y in range(8):
                    for x in range(8):
                        window['-sq{}{}board{}{}-'.format(files[x],8-y,y,x)].update(image_data=pieces_img[move_board[y][x]],image_size=image_size_main,image_subsample=main_image_subsample)
            except:
                sg.PopupOK("invalid forsyth",keep_on_top=True)
                window["forsyth"].update('')
            window["mn"].update('0')

        elif '-outside' in event:
            if move_from_set == False:
                move_from_set = True
                from_outside = True
                add_piece = event[9:11]

                window[event].update('',button_color=focused_square)
                move_from_square = event
            else: 
                if move_from_square == event: #if the piece is clicked twice, the status is reset.

                    from_outside = False
                    move_from_set == False
                    window[move_from_square].update(button_color=bc_alice_blue)
                    move_from_square = event
                else:
                    window[move_from_square].update(button_color=bc_alice_blue)
                    window[event].update(button_color=focused_square)
                    move_from_square = event
                    move_from_set = True
                    from_outside = True
                    add_piece = event[9:11]

        elif "-sq" in event:
            #when clicked
            if move_from_set == False:
                
                move_from_square = event
                move_from_index = event[10:12]
                
                if from_outside == False and move_board[int(move_from_index[0])][int(move_from_index[1])] != "em":
                    window[move_from_square].update('',button_color=focused_square)

                if move_board[int(move_from_index[0])][int(move_from_index[1])] != "em":
                    move_from_set = True

            else: #move_from_set == True 
                #arrival square
                move_to_square = event
                move_to_index = event[10:12]

                #arrival
                if from_outside == False:
                    if not move_board[int(move_from_index[0])][int(move_from_index[1])] == "em":
                        #exchange of pieces
                        tmp = move_board[int(move_from_index[0])][int(move_from_index[1])]
                        move_board[int(move_from_index[0])][int(move_from_index[1])] = "em"
                        move_board[int(move_to_index[0])][int(move_to_index[1])] = tmp
                        window[move_from_square].update(image_data=pieces_img[move_board[int(move_from_index[0])][int(move_from_index[1])]],image_size=image_size_main,image_subsample=main_image_subsample,button_color=dark_color_square if (int(move_from_index[0])+int(move_from_index[1])) % 2 else light_color_square)
                        window[move_to_square].update(image_data=pieces_img[move_board[int(move_to_index[0])][int(move_to_index[1])]],image_size=image_size_main,image_subsample=main_image_subsample)

                        #adding 0.5 to the plycount
                        if not move_from_square == move_to_square:
                            try:
                                window["mn"].update(str(float(window["mn"].Get())+0.5))
                            except ValueError:
                                sg.PopupOK("invalid move number",keep_on_top=True)
                                window["mn"].update('0')
                else: #"adding" mode

                    move_board[int(move_to_index[0])][int(move_to_index[1])] = add_piece
                    window[move_to_square].update(image_data=pieces_img[move_board[int(move_to_index[0])][int(move_to_index[1])]],image_size=image_size_main,image_subsample=main_image_subsample)
                    window[move_from_square].update(button_color=bc_alice_blue)

                #FEN transform
                forsyth = fenparser.read_fen_from_current_position(move_board)
                window["forsyth"].update(forsyth)


                move_from_set = False
                from_outside = False
                add_piece = ""


    window.close()

if __name__ == '__main__':
    main()