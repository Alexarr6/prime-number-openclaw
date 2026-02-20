# Prime Number OpenClaw

Programa en **Python** que indica si un número entero es primo o no.

## Requisitos

- Python 3.8+
- Solo librería estándar (no dependencias externas)

## Uso

```bash
python3 primo.py <numero>
```

### Ejemplos

```bash
python3 primo.py 2
# primo

python3 primo.py 15
# no primo

python3 primo.py -7
# no primo
```

## Ejecutar tests

```bash
python3 -m unittest -v
```

## Estructura del proyecto

- `primo.py`: lógica principal + CLI con `argparse`
- `test_primo.py`: tests unitarios y de CLI (`unittest`)

## Comportamiento esperado

- `n < 2` → `no primo`
- `n == 2` → `primo`
- pares mayores que 2 → `no primo`
- impares > 2 se evalúan hasta `sqrt(n)`
