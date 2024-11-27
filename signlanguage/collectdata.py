
import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/a")),
             'b': len(os.listdir(directory+"/aa")),
             'c': len(os.listdir(directory+"/i")),
             'd': len(os.listdir(directory+"/u")),
             'e': len(os.listdir(directory+"/ru")),
             'f': len(os.listdir(directory+"/e")),
             'g': len(os.listdir(directory+"/ai")),
             'h': len(os.listdir(directory+"/o")),
             'i': len(os.listdir(directory+"/ou")),
             'j': len(os.listdir(directory+"/ka")),
             'k': len(os.listdir(directory+"/kha")),
             'l': len(os.listdir(directory+"/ga")),
             'm': len(os.listdir(directory+"/gha")),
             'n': len(os.listdir(directory+"/cha")),
             'o': len(os.listdir(directory+"/chha")),
             'p': len(os.listdir(directory+"/ja")),
             '-': len(os.listdir(directory+"/jha")),
             'r': len(os.listdir(directory+"/ta")),
             's': len(os.listdir(directory+"/tha")),
             't': len(os.listdir(directory+"/da")),
             'u': len(os.listdir(directory+"/dha")),
             'v': len(os.listdir(directory+"/ta1")),
             'w': len(os.listdir(directory+"/tha1")),
             'x': len(os.listdir(directory+"/da1")),
             'y': len(os.listdir(directory+"/dha1")),
             'z': len(os.listdir(directory+"/pa")),
             '.': len(os.listdir(directory+"/pha")),
             '/': len(os.listdir(directory+"/ba")),
             '1': len(os.listdir(directory+"/bha")),
             '2': len(os.listdir(directory+"/ma")),
             '3': len(os.listdir(directory+"/jya")),
             '4': len(os.listdir(directory+"/ra")),
             '5': len(os.listdir(directory+"/la")),
             '6': len(os.listdir(directory+"/wa")),
             '7': len(os.listdir(directory+"/sha")),
             '8': len(os.listdir(directory+"/sha1")),
             '9': len(os.listdir(directory+"/sa")),
             '0': len(os.listdir(directory+"/ha")),
             ';': len(os.listdir(directory+"/ya")),
             '`': len(os.listdir(directory+"/la1"))
             }
    cv2.putText(frame, "a : "+str(count['a']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "aa : "+str(count['b']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "i : "+str(count['c']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "u : "+str(count['d']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ru : "+str(count['e']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "e : "+str(count['f']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ai : "+str(count['g']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "o : "+str(count['h']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ou : "+str(count['i']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ka : "+str(count['j']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "kha : "+str(count['k']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ga : "+str(count['l']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "gha : "+str(count['m']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "cha : "+str(count['n']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "chha : "+str(count['o']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ja : "+str(count['p']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "jha : "+str(count['-']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ta : "+str(count['r']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "tha : "+str(count['s']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "da : "+str(count['t']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "dha : "+str(count['u']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ta1 : "+str(count['v']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "tha1 : "+str(count['w']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "da1 : "+str(count['x']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "dha1 : "+str(count['y']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "pa : "+str(count['z']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "pha : "+str(count['.']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ba : "+str(count['/']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "bha : "+str(count['1']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ma : "+str(count['2']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "jya : "+str(count['3']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ra : "+str(count['4']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "la : "+str(count['5']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "wa : "+str(count['6']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "sha : "+str(count['7']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "sha : "+str(count['8']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "sa : "+str(count['9']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ha : "+str(count['0']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ya : "+str(count[';']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "la1 : "+str(count['`']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "ra : "+str(count['z']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('q'):  # Add this line
        break  # Exit the loop when 'q' is pressed
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'a/'+str(count['a'])+'.png',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'aa/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'i/'+str(count['c'])+'.png',frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'u/'+str(count['d'])+'.png',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'ru/'+str(count['e'])+'.png',frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'e/'+str(count['f'])+'.png',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'ai/'+str(count['g'])+'.png',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'o/'+str(count['h'])+'.png',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'ou/'+str(count['i'])+'.png',frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory+'ka/'+str(count['j'])+'.png',frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'kha/'+str(count['k'])+'.png',frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'ga/'+str(count['l'])+'.png',frame)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'gha/'+str(count['m'])+'.png',frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'cha/'+str(count['n'])+'.png',frame)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'chha/'+str(count['o'])+'.png',frame)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'ja/'+str(count['p'])+'.png',frame)
    if interrupt & 0xFF == ord('-'):
        cv2.imwrite(directory+'jha/'+str(count['-'])+'.png',frame)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory+'ta/'+str(count['r'])+'.png',frame)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'tha/'+str(count['s'])+'.png',frame)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'da/'+str(count['t'])+'.png',frame)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'dha/'+str(count['u'])+'.png',frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'ta1/'+str(count['v'])+'.png',frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'tha1/'+str(count['w'])+'.png',frame)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'da1/'+str(count['x'])+'.png',frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'dha1/'+str(count['y'])+'.png',frame)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory+'pa/'+str(count['z'])+'.png',frame)
    if interrupt & 0xFF == ord('.'):
        cv2.imwrite(directory+'pha/'+str(count['.'])+'.png',frame)
    if interrupt & 0xFF == ord('/'):
        cv2.imwrite(directory+'ba/'+str(count['/'])+'.png',frame)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'bha/'+str(count['1'])+'.png',frame)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'ma/'+str(count['2'])+'.png',frame)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'jya/'+str(count['3'])+'.png',frame)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'ra/'+str(count['4'])+'.png',frame)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'la/'+str(count['5'])+'.png',frame)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'wa/'+str(count['6'])+'.png',frame)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'sha/'+str(count['7'])+'.png',frame)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'sha1/'+str(count['8'])+'.png',frame)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'sa/'+str(count['9'])+'.png',frame)
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'ha/'+str(count['0'])+'.png',frame)
    if interrupt & 0xFF == ord(';'):
        cv2.imwrite(directory+'ya/'+str(count[';'])+'.png',frame)
    if interrupt & 0xFF == ord('`'):
        cv2.imwrite(directory+'la1/'+str(count['`'])+'.png',frame)
    


cap.release()
cv2.destroyAllWindows()