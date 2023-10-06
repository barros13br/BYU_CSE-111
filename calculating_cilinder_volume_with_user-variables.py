import math

def main():
    r = float(input("say the radius:"))
    h =float(input("say the height: "))
    volume = cilinder_volume_math(r, h)
    print(f"{volume:.2f}")

def cilinder_volume_math(r,h):
    volume = math.pi * r**2 * h
    return volume

main()