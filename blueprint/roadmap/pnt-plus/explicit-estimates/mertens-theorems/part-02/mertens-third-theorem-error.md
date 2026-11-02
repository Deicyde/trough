---
declaration: theorem
origin: cited
lean: Mertens.prod_one_minus_div_prime_eq
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1329
---

# Mertens' third theorem error term

For any $x \geq 2$, one has

$$
\prod_{p \leq x} \left(1 - \frac{1}{p}\right) = \frac{e^{-\gamma}}{\log x} \exp(E_3(x)).
$$

## Depends on

- [The remainder term in Mertens third theorem](mertens-third-error.md)

## Proof

Immediate from definition

## Lean

Formalized as [`Mertens.prod_one_minus_div_prime_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.prod_one_minus_div_prime_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
