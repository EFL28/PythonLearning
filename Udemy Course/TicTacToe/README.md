# TicTacToe

Este es un juego de TicTacToe simple implementado en Python.

## Descripción

El juego de TicTacToe es un juego clásico de dos jugadores donde los jugadores se turnan para marcar los espacios en una cuadrícula de 3x3. El primer jugador en alinear tres de sus marcas en una fila horizontal, vertical o diagonal gana el juego. Si todos los espacios están llenos y ningún jugador ha alineado tres marcas, el juego termina en empate.

## Cómo jugar

1. Los jugadores se turnan para ingresar una posición (del 1 al 9) para colocar su marca (`X` o `O`) en la cuadrícula.
2. El juego determina automáticamente quién es el primer jugador de forma aleatoria.
3. El juego revisa después de cada movimiento si hay un ganador o si el juego ha terminado en empate.
4. Se ofrece la opción de jugar de nuevo al final de cada partida.

## Requisitos

- Python 3.x

## Uso

1. Clona este repositorio:
    ```sh
    git clone https://github.com/EFL28/TTTpython
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd TicTacToe
    ```
3. Ejecuta el juego:
    ```sh
    python tictactoe.py
    ```
