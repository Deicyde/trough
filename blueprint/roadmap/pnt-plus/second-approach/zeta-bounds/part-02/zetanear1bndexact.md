---
declaration: lemma
origin: cited
lean: ZetaNear1BndExact
statement: formalized
proof: formalized
---

# ZetaNear1BndExact

There exists a $c>0$ such that for all $1 < \sigma ≤ 2$,

$$
|\zeta(\sigma)| ≤ c/(\sigma-1).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaNear1BndFilter](zetanear1bndfilter.md)

## Proof

Split into two cases, use Lemma [ZetaNear1BndFilter](zetanear1bndfilter.md) for $\sigma$ sufficiently small and continuity on a compact interval otherwise.

## Lean

Formalized as [`ZetaNear1BndExact`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaNear1BndExact).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
