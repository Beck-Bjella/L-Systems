import turtle


def generate_fractal(sentence, rules, iterations):
    for n in range(iterations):
        new_sentence = ""
        for current_letter in sentence:
            in_rule = False
            for current_rule in rules:
                if current_letter == current_rule[0]:
                    new_sentence = new_sentence + current_rule[1]
                    in_rule = True
            if not in_rule:
                new_sentence = new_sentence + current_letter
        sentence = new_sentence

    return sentence


def setup_turtle(start_angle, start_x, start_y, visualize=True):
    turtle.colormode(255)
    turtle.speed("fastest")
    turtle.delay(-1)

    if visualize:
        turtle.tracer(True)
    else:
        turtle.tracer(False)

    turtle.penup()
    turtle.setposition(start_x, start_y)
    turtle.setheading(start_angle)
    turtle.pendown()
    turtle.clear()


def draw_fractal(sentence, rotation_angle, move_distance):
    log_x = []
    log_y = []
    log_angle = []

    for letter in sentence:
        match letter:
            # case "0":
            #     turtle.pencolor("black")
            # case "1":
            #     turtle.pencolor("red")
            # case "2":
            #     turtle.pencolor("green")
            # case "3":
            #     turtle.pencolor("blue")
            case "F" | "G":
                turtle.forward(move_distance)
            case "f" | "g":
                turtle.penup()
                turtle.forward(move_distance)
                turtle.pendown()
            case "+":
                turtle.left(rotation_angle)
            case "-":
                turtle.right(rotation_angle)
            case "[":
                log_x.append(turtle.xcor())
                log_y.append(turtle.ycor())
                log_angle.append(turtle.heading())
            case "]":
                x_pos = float(log_x[-1])
                y_pos = float(log_y[-1])
                rotation = float(log_angle[-1])

                log_x.pop()
                log_y.pop()
                log_angle.pop()

                turtle.penup()
                turtle.setposition(x_pos, y_pos)
                turtle.setheading(rotation)
                turtle.pendown()

    window = turtle.Screen()
    window.mainloop()


def main():
    print("Fractal Options")
    print("   - '1' for 'Fractal plant'")
    print("   - '2' for 'Dragon Curve'")
    print("   - '3' for 'Sierpinski triangle'")
    print("   - '4' for 'Hilbert Curve'")
    print("   - '5' for 'Penrose Tiling'")
    print("   - '6' for 'Mandala'")
    print("")

    option = None
    valid_input = False
    while not valid_input:
        try:
            option = int(input("Please select a option: "))

        except:
            print("[!] Invalid input")

        if option >= 1 and option <= 6:
            valid_input = True
        else:
            print("[!] Invalid input")
        print("")

    print("----------------------------------------")
    print("")

    axiom = None
    rules = None
    match option:
        case 1:
            # --Fractal plant--
            axiom = "X"
            rules = [["X", "F+[[X]-X]-F[-FX]+X"], ["F", "FF"]]
            rotation_angle = 25

        case 2:
            # --Dragon Curve--
            axiom = "X"
            rules = [["X", "F+[[X]-X]-F[-FX]+X"], ["F", "FF"]]
            rotation_angle = 90

        case 3:
            # --Sierpinski triangle--
            axiom = "F-G-G"
            rules = [["F", "F-G+F+G-F"], ["G", "GG"]]
            rotation_angle = 120

        case 4:
            # --Hilbert Curve--
            axiom = "A"
            rules = [["A", "-BF + AFA + FB -"], ["B", "+AF-BFB-FA+"]]
            rotation_angle = 90

        case 5:
            # --Penrose Tiling--
            axiom = "[N]++[N]++[N]++[N]++[N]"
            rules = [["M", "OF++PF----NF[-OF----MF]++"], ["N", "+OF--PF[---MF--NF]+"], ["O", "-MF++NF[+++OF++PF]-"], ["P", "--OF++++MF[+PF++++NF]--NF"], ["F", ""]]
            rotation_angle = 36

        case 6:
            # --Mandala--
            axiom = "X---------X-------X"
            rules = [["X", "[G][+G][-G][++G][--G][+++G][---G][++++G][----G]"], ["G", "GG[--G][++G]"]]
            rotation_angle = 15

    print("[INFO] The smaller the iterations the smaller the fractal.")
    print("[INFO] The number of iterations has to be between 1 and 10.")
    print("")
    print("[INFO] 7 iterations is recomended.")
    print("")

    iteration_count = None
    valid_input = False
    while not valid_input:
        try:
            iteration_count = int(input("Please select a iteration count: "))
        except:
            print("[!] Invalid input")

        if iteration_count >= 1 and iteration_count <= 10:
            valid_input = True
        else:
            print("[!] Invalid input")
        print("")

    print("----------------------------------------")
    print("")

    print("What color do you want the fractal to be?")
    print("")

    color = None
    valid_input = False
    while not valid_input:
        try:
            color = input("Please input a color: ")
            turtle.color(color)
            valid_input = True

        except:
            print("[!] Invalid input")

        print("")

    print("----------------------------------------")
    print("")

    setup_turtle(start_angle=90, start_x=0, start_y=-300, visualize=True)

    fractal_command = generate_fractal(axiom, rules, iteration_count)

    draw_fractal(fractal_command, rotation_angle, 3)

    print("Quitting...")
    print("")


if __name__ == '__main__':
    main()
