def main():
    f = open(r"C:\Users\rdh03\source\Python\Python313\BasicProPy\FileIO_ex\gasprices.txt")
    content = f.read()
    tokens = content.split()

    sum_bel = 0
    sum_usa = 0

    for i in range(0, len(tokens), 3):
        sum_bel = float(tokens[i])
        sum_usa = float(tokens[i+1])
        
    num_prices = len(tokens) / 3

    avg_bel = sum_bel / num_prices
    avg_usa = sum_usa / num_prices

    print(f'Average gas price in belgium: {avg_bel:.2f}')
    print(f'Average gas price in belgium: {avg_usa}')


main()