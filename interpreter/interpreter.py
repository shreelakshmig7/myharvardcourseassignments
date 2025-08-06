def doMath(var1, sym, var2):
    ans = 0.0
    match sym:
        case "+":
            ans = var1 + var2
        case "-":
            ans = var1 - var2
        case "*":
            ans = var1 * var2
        case "/":
            ans = var1 / var2
    return ans

def main():
    x, y, z = input("Expression: ").split(" ")
    finalOpt = doMath(float(x), y, float(z))
    print(f"{finalOpt:0.1f}")

main()
