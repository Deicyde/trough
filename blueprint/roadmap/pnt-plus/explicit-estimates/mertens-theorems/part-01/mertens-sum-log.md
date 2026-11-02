---
declaration: lemma
origin: cited
lean: Mertens.sum_log_eq
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1303
---

# Partial sum of logarithm identity

For any $x \geq 1$, one has

$$
\sum_{n \leq x} \log n = x \log x - (\{ x \}-1/2) \log x - x + 1 + \int_1^x (\{ t \}-1/2) \frac{dt}{t}
$$

(NOTE: this identity is not actually needed in the proof of Mertens' theorems, but may be worth recording nevertheless.)

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Apply the Euler-Maclaurin formula.

## Lean

Formalized as [`Mertens.sum_log_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_log_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
