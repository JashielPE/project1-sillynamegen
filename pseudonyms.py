import sys, random


def main():
    print("Welcome to the Mugi90 'Apodos chidos'. \n ")

    first = ('Bambino', 'Mugiwara', 'Zombie', 'El pepe', 'Ferras', 'Dios Eolo', 'Tiburon',
             'Mojarra',
             'Master', 'Doc', 'El Caderas', 'Mensi', 'El placas', 'La mercury', 'Aluche', 'Maracas',
             'Tester', 'Jalisquillo', 'Terreneitor', 'Manager', 'Malagol', 'Chaca', 'El birrias',
             'Python', 'Caguamas', 'Artesanal', 'Veracruz', 'Orizabalas', 'Paranormal',
             'Farmacias Similares')

    last = ('camara', 'voraz', 'en alta', 'oscuro', '666', 'america', 'Jenkins',
            'el senor de la noche',
            'cruzito', 'gato', 'chicote', 'nene', 'sacatito pal conejo', 'magnate', 'pajarete')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        print('\n\n')
        print(f'{first_name} {last_name}', file=sys.stderr)
        print('\n\n')

        try_again = input('\n\n Try again? (Press Enter else n to quit)\n')
        if try_again.lower() == 'n':
            break
    input('\nPress Enter to exit.')


if __name__ == "__main__":
    main()
