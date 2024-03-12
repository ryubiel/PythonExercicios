from time import sleep


def maior(* num):
    maior = 0;
    print("-=" * 30)
    print("Analisando os valores passados...")
    for c,n in enumerate(num):
        sleep(0.5)
        print(f"{n}", end=" ")
        if c == 0 or n > maior:
            maior = n
    sleep(0.5)
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")


maior(5, 8, 7, 9, 6, 1, 2, 4, 5, 12)
maior(0)
maior()
