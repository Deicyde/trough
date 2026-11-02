---
declaration: lemma
origin: cited
lean: Erdos392.Params.initial.balance_medium_prime_ge
statement: formalized
proof: formalized
---

# initial-factorization-medium-prime-ge

A medium prime $\sqrt{n} < p ≤ n/L$ can be in deficit by at most $M$.

## Depends on

- [params-set](params-set.md)
- [initial-factorization-def](initial-factorization-def.md)
- [balance-def](balance-def.md)

## Proof depends on

- [factorization-def](factorization-def.md)

## Proof

The number of times $p$ divides $a_1 \dots a_t$ is at least $M \lfloor n/Mp \rfloor ≥ n/p - M$ (note that the removal of the non-smooth numbers does not remove any multiples of $p$). Meanwhile, the number of times $p$ divides $n!$ is at most $n/p$.

## Lean

Formalized as [`Erdos392.Params.initial.balance_medium_prime_ge`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.Params.initial.balance_medium_prime_ge).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
