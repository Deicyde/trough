---
declaration: lemma
origin: cited
lean: finsum_range_eq_sum_range
statement: formalized
proof: formalized
---

# finsum-range-eq-sum-range

For any arithmetic function $f$ and real number $x$, one has

$$
\sum_{n \leq x} f(n) = \sum_{n \leq ⌊x⌋_+} f(n)
$$

and

$$
\sum_{n < x} f(n) = \sum_{n < ⌈x⌉_+} f(n).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Straightforward.

## Lean

Formalized as [`finsum_range_eq_sum_range`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/finsum_range_eq_sum_range).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
