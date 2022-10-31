import random
import numpy as np
#Ζητάω τη διάσταση από το χρήστη.Λόγω του ότι θέλουμε τετράγωνο, η διάσταση των γραμμών θα είναι ίση με τη διάσταση
#των στηλων.
rows = cols = int(input("Give the dimension of the array:"))
#Φτιάχνω μέσα από λίστες τον πίνακα με τη διάσταση που του έδωσε ο χρήστης
a = [[[0] for j in range(cols)] for i in range(rows)]
#Φτιάχνω μία λίστα ώστε να βάλω στο τέλος μέσα όλες τις τετράδες που μετρήθηκαν για να βγει ο μέσος όρος
lst=[]
#Επαναλαμβάνω για 100 φορές βάζοντας στον πίνακα που έφτιαξα στις μισές θέσεις 0 και στις άλλες μισές 1
for i in range(0,100):
#Βάζω έναν μετρητή που θα τον χρησιμοποιήσω όταν το i=j ώστε να γεμίζω τις μισές θέσεις του πίνακα με στρογγυλ
#προς τα πάνω με 0 και 1
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            if i < j:
                a[i][j] = 1
            elif i > j:
                a[i][j] = 0
            elif i == j:
#Όταν i=j αν ο μετρητής είναι < από τις μισές στήλες (ακέραιο υπόλοιπο) γεμίζω με 0 και αυξάνω το μετρητή κατά 1
                if cnt < rows // 2:
                    a[i][j] = 0
                    cnt = cnt + 1
#Όταν ο μετρητής ξεπεράσει τις μισές γεμίζω τις υπόλοιπες με 1
                else:
                    a[i][j] = 1
#Μετατρέπω τον πίνακα σε numPy array διότι προσπάθησα να τον τυχαιοποιήσω με randomshuffle αλλά δε γινόταν
#πλήρης τυχαιοποίηση των θέσεων. Βρήκα ότι με αυτόν τον τρόπο οι μονάδες και τα μηδενικά τυχαιοποιούνται πλήρως
    board = np.array(a)
#με το .ravel() επιστρέφει έναν συνεχόμενο επίπεδο πίνακα
    board = board.ravel()
#Τυχαιοποιώ τις μονάδες και τα μηδενικά
    np.random.shuffle(board)
#και κάνω .reshape(rows, cols) ώστε να επιστραφεί ο πίνακας σε γραμμές και στήλες
    board = board.reshape(rows, cols)
#Τυπώνω τον τυχαιοποιημένο πλέον πίνακα
    for i in range(1):
        for row in board:
            print(' '.join([str(elem) for elem in row]))
#Φτιάχνω μετρητές τετράδων, οριζόντιων, κάθετων, διαγώνιων και συνολικών
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
#Ελέγχω για τετράδες οριζόντια και τις τυπώνω
    for C in range(cols - 3):
        for R in range(rows):
            if board[R][C] == 1 and board[R][C + 1] == 1 and board[R][C + 2] == 1 and board[R][C + 3] == 1:
                cnt1 = cnt1 + 1
    print("Horizontally there are", cnt1, "quads")
#Ελέγχω για τετράδες κάθετα και τις τυπώνω
    for C in range(cols):
        for R in range(rows - 3):
            if board[R][C] == 1 and board[R + 1][C] == 1 and board[R + 2][C] == 1 and board[R + 3][C] == 1:
                cnt2 = cnt2 + 1
    print("Vertically there are", cnt2, "quads")
#Ελέγχω για τετράδες διαγώνια και τις τυπώνω
    for C in range(cols - 3):
        for R in range(rows - 3):
            if board[R][C] == 1 and board[R + 1][C + 1] == 1 and board[R + 2][C + 2] == 1 and board[R + 3][C + 3] == 1:
                cnt3 = cnt3 + 1
    print("Diagonally there are", cnt3, "quads")
#Μετράω το σύνολο των τετράδων και τις βάζω στη λίστα που είχα φτιάξει στην αρχή
    cnt4 = cnt1 + cnt2 + cnt3
    print("Total quads are",cnt4)
    lst.extend([cnt4])
#Τέλος βρίσκω το μέσο όρο των τετράδων
sum=0
for i in lst:
    sum=sum+i
print("\nThe average of total quads is: ",sum/100)




