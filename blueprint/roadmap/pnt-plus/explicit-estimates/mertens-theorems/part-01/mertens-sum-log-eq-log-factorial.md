---
declaration: proposition
origin: cited
lean: Mertens.sum_log_eq_log_factorial
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1315
---

# Partial sum of logarithm as logarithm of factorial

For any $x \geq 1$, one has

$$
\sum_{n \leq x} \log n = \log(\lfloor x \rfloor!).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Follows from the definition of the factorial function. Is not needed for the Mertens theorems, but is a natural fact to have.

## Lean

Formalized as [`Mertens.sum_log_eq_log_factorial`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_log_eq_log_factorial).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
