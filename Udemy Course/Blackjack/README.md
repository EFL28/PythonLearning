# TicTacToe

Este es un juego de Blackjack implementado en Python.

## Descripción

BlackJack es un juego de cartas popular donde el objetivo es obtener una mano cuyo valor sea lo más cercano posible a 21 sin excederse. Los jugadores compiten contra el crupier (dealer). Los valores de las cartas numéricas son iguales a sus números, las cartas con figuras (J, Q, K) valen 10, y los Ases pueden valer 1 u 11, dependiendo de lo que sea más ventajoso para la mano.

## Cómo jugar

1. El juego comienza con el jugador y el crupier recibiendo dos cartas cada uno. Una de las cartas del crupier se muestra, mientras que la otra permanece oculta.
2. El jugador puede realizar una apuesta inicial antes de recibir sus cartas.
3. El jugador tiene la opción de "Hit" (pedir una carta) o "Stand" (quedarse con su mano actual). Si el jugador pide una carta y el valor total de su mano supera 21, pierde (bust).
4. El crupier debe seguir sacando cartas hasta que su mano alcance un valor de al menos 17.
5. El jugador gana si su mano es mayor que la del crupier sin exceder 21 o si el crupier se pasa de 21. Si el jugador se pasa de 21, pierde la apuesta.
6. En caso de empate (push), ni el jugador ni el crupier ganan la apuesta.
7. El juego continúa permitiendo al jugador hacer nuevas apuestas y jugar más rondas hasta que decida salir.

## Requisitos

- Python 3.x

## Uso

1. Clona este repositorio:
    ```sh
    git clone https://github.com/EFL28/PythonLearning
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd UdemyCourse/Blackjack
    ```
3. Ejecuta el juego:
    ```sh
    python blackjack.py
    ```
