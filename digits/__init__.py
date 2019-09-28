from digits.hand_writing import HandWriting
if __name__ == '__main__':
    def print_menu():
        print('0 EXIT')
        print('1 손글씨 인식')
        print('2 손글씨인식 머신 러닝')
        print('3 손글씨인식 테스트')
        return input('CHOOSE ONE\n')
    while 1:
        menu = print_menu()
        print('MENU : %s' % menu)
        if menu == '0':
            print('EXIT')
            break
        elif menu == '1':
            m = HandWriting()
            m.read_file()
            break
        elif menu == '2':
            m = HandWriting()
            m.learning()
            break
        elif menu == '3':
            m = HandWriting()
            fname = './data/my4.png'
            print('테스트 ')
            print(m.test(fname))
            break
        elif menu == '4':

            break

        elif menu == '5':

            break
        elif menu == '6':
           pass