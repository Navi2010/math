import math
import random

def generate_random_angle():
    return random.uniform(0, 360)

def trigonometric_functions(angle):
    radians = math.radians(angle)
    
    
    sine = math.sin(radians)
    cosine = math.cos(radians)
    
    tangent = None
    if cosine != 0:
        tangent = math.tan(radians)
    else:
        tangent = "undefined"
    
    return sine, cosine, tangent

def main():
    print("Trigonometric Functions Calculator")
    for _ in range(5):
        angle = generate_random_angle()
        sine, cosine, tangent = trigonometric_functions(angle)
        
        print(f"angle: {angle:.2f} degrees")
        print(f"sine: {sine:.4f}")
        print(f"cosine: {cosine:.4f}")
        print(f"tangent: {tangent}")
        print("-" * 30)

if __name__ == "__main__":
    main()


