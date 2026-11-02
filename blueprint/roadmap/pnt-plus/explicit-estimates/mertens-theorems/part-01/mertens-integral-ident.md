---
declaration: lemma
origin: cited
lean: _private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.sum_div_log_eq
statement: formalized
proof: formalized
---

# Integral identity involving inverse log weight

For any $x \geq 2$ and any $f : {\mathbb N} \mapsto {\mathbb R}$, one has

$$
\sum_{2 \leq n \leq x} \frac{f(n)}{\log n} = \frac{1}{\log x} \sum_{2 \leq n \leq x} f(n) + \int_2^x \frac{1}{t \log^2 t} \sum_{2 \leq n \leq t} f(n) \, dt
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Establish the identity

$$
\frac{1}{\log n} = \frac{1}{\log x} + \int_2^x \frac{1}{t \log^2 t} 1_{t \geq n}\ dt
$$

for $2 \leq n \leq x$,multiply by $f(n)$, then sum.

## Lean

Formalized as [`_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.sum_div_log_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.sum_div_log_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
