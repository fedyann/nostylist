import random


def manipulate_word(word, skip_prob=0.075, replace_prob=0.05):
    manipulated_word = list(word)

    for i in range(len(manipulated_word)):
        if random.random() < skip_prob:
            manipulated_word[i] = ''
        elif random.random() < replace_prob:
            new_char = chr(random.randint(ord('а'), ord('я')))
            manipulated_word[i] = new_char

    return ''.join(manipulated_word)


def Rand(input_i):
    out_e = []
    for input in input_i:

        input_n = []
        if input.find('улица') == -1:
            if input.find('площадь') == -1:
                if input.find('переулок') == -1:
                    if input.find('проспект') == -1:
                        inp = input.replace('Проспект', '')
                        input_n.append(inp)
                        input_n.append('Проспект')
                    else:
                        inp = input.replace('проспект', '')
                        input_n.append('проспект')
                        input_n.append(inp)

        elif input.find('переулок') == -1:
            if input.find('площадь') == -1:
                if input.find('проспект') == -1 or input.find('Проспект') == -1:
                    inp = input.replace('улица', '')
                    input_n.append(inp)
                    input_n.append('улица')

        elif input.find('переулок') == -1:
            if input.find('улица') == -1:
                if input.find('проспект') == -1 or input.find('Проспект') == -1:
                    inp = input.replace('площадь', '')
                    input_n.append(inp)
                    input_n.append('площадь')

        elif input.find('площадь') == -1:
            if input.find('улица') == -1:
                if input.find('проспект') == -1 or input.find('Проспект') == -1:
                    inp = input.replace('переулок', '')
                    input_n.append(inp)
                    input_n.append('переулок')

        street = [' ул ', ' у ', " улица "]
        p = [" п ", " пр ", " проспект "]
        pl = [" пл ", " площадь "]
        per = [" пер ", " переулок "]
        # if input[1] == 'проспект'
        if input_n[1] == 'проспект':
            input_n[1] = p[random.randint(0, 2)]

        elif input_n[1] == 'улица':
            input_n[1] = street[random.randint(0, 2)]

        elif input_n[1] == 'площадь':
            input_n[1] = pl[random.randint(0, 2)]

        elif input_n[1] == 'переулок':
            input_n[1] = per[random.randint(0, 2)]

        elif input_n[1] == 'Проспект':
            input_n[1] = p[random.randint(0, 2)]

        out = manipulate_word(input_n[0])

        if input.find('Проспект') == 0:
            out_e.append(input_n[1] + out)

        else:
            out_e.append(out + input_n[1])

        print(out_e)

    return out + input_n[1]


S = Rand(['Невский проспект', 'Проспект Энгельса'])
print(S)
