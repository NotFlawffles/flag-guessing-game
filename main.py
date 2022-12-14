import random, sys, os, enum, time


class Flag:
    def __init__(self, name, location):
        self.name = name.replace('_', ' ')
        self.location = location


def load_flags(mode):
    flags = []
    if mode == 0:
        for section in os.listdir("flags/"):
            if section == "special":
                continue

            for flag in os.listdir(f"flags/{section}"):
                flags.append(Flag(flag.split('.')[0], f"flags/{section}/{flag}"))

    elif mode == 1:
        for flag in os.listdir("flags/asia/"):
            flags.append(Flag(flag.split('.')[0], f"flags/asia/{flag}"))

    elif mode == 2:
        for flag in os.listdir("flags/europe/"):
            flags.append(Flag(flag.split('.')[0], f"flags/europe/{flag}"))

    elif mode == 3:
        for flag in os.listdir("flags/africa/"):
            flags.append(Flag(flag.split('.')[0], f"flags/africa/{flag}"))

    elif mode == 4:
        for flag in os.listdir("flags/north_america/"):
            flags.append(Flag(flag.split('.')[0], f"flags/north_america/{flag}"))

    elif mode == 5:
        for flag in os.listdir("flags/south_america/"):
            flags.append(Flag(flag.split('.')[0], f"flags/south_america/{flag}"))

    elif mode == 6:
        for flag in os.listdir("flags/oceania/"):
            flags.append(Flag(flag.split('.')[0], f"flags/oceania/{flag}"))

    elif mode == 7:
        for flag in os.listdir("flags/special/eurasia/"):
            flags.append(Flag(flag.split('.')[0], f"flags/special/eurasia/{flag}"))

    elif mode == 8:
        for flag in os.listdir("flags/special/islands/"):
            flags.append(Flag(flag.split('.')[0], f"flags/special/islands/{flag}"))

    elif mode == 9:
        flags = load_flags(random.randint(0, 8))

    return flags


class Mode(enum.Enum):
    All          = load_flags(0)
    Asia         = load_flags(1)
    Europe       = load_flags(2)
    Africa       = load_flags(3)
    NorthAmerica = load_flags(4)
    SouthAmerica = load_flags(5)
    Oceania      = load_flags(6)
    Eurasia      = load_flags(7)
    Islands      = load_flags(8)
    Random       = load_flags(9)


def main(mode=Mode.Random, count=10):
    flags = []
    for _ in range(count):
        picked = random.choice(mode.value)
        if picked not in flags:
            flags.append(picked)

    for flag in flags:
        print()
        os.system(f"viu {flag.location}")
        guess = input("\nwhat flag is that: ")
        if guess == flag.name:
            print("correct!")
            time.sleep(0.5)

        else:
            print(f"it was {flag.name}")
            time.sleep(2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        main()
        exit(0)

    mode = Mode.All
    fail = True
    if sys.argv[1].lower() == "all":
        mode = Mode.All

    elif sys.argv[1].lower() == "asia":
        mode = Mode.Asia

    elif sys.argv[1].lower() == "europe":
        mode = Mode.Europe

    elif sys.argv[1].lower() == "africa":
        mode = Mode.Africa

    elif sys.argv[1].lower() in ["na", "northamerica"]:
        mode = Mode.NorthAmerica

    elif sys.argv[1].lower() in ["sa", "southamerica"]:
        mode = Mode.SouthAmerica

    elif sys.argv[1].lower() == "oceania":
        mode = Mode.Oceania

    elif sys.argv[1].lower() == "eurasia":
        mode = Mode.Eurasia

    elif sys.argv[1].lower() == "islands":
        mode = Mode.Islands

    elif sys.argv[1].lower() == "random":
        mode = Mode.Random

    else:
        print(f"could not recognize the flags section `{sys.argv[1]}`")

    if len(sys.argv) == 3:
        count = 10
        try:
            count = int(sys.argv[2])
            if count < 1:
                print("the count must be >= 1")
                exit(1)

            elif count > len(mode.value):
                count = len(mode.value)
            
            main(mode, count)
            fail = False
            exit(0)

        except:
            if not(fail):
                exit(0)

            print("the second argument must be a number count")
            exit(1)

    main(mode)
