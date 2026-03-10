# 🧪 Pruebas de Casos Edge

## 1. Caso: 1 dado de 4 caras (1d4)
Ideal para verificar el límite inferior de los dados poliédricos.

- Resultado: 3
- Análisis: Dentro del rango $[1, 4]$.

## 2. Caso: 10 dados de 20 caras (10d20)
Aquí probamos la generación masiva y la suma total.

- Tiradas individuales: 18, 5, 20, 12, 3, 9, 15, 7, 11, 2.
- Suma Total: 102
- Promedio obtenido: 10.2 (El promedio teórico es 10.5, así que estamos en rango).

## 3. Caso: 20 tiradas seguidas (Estrés de repetición)
Simularemos 20 lanzamientos rápidos de un d6 para observar la variabilidad y detectar patrones inusuales (que no debería haber).

### Registro de 20 Tiradas (d6)

| Tirada | Resultado | Tirada | Resultado |
| :---: | :---: | :---: | :---: |
| 1 | 6 | 11 | 2 |
| 2 | 1 | 12 | 5 |
| 3 | 4 | 13 | 3 |
| 4 | 4 | 14 | 6 |
| 5 | 2 | 15 | 1 |
| 6 | 5 | 16 | 4 |
| 7 | 3 | 17 | 2 |
| 8 | 6 | 18 | 5 |
| 9 | 1 | 19 | 3 |
| 10 | 4 | 20 | 6 |