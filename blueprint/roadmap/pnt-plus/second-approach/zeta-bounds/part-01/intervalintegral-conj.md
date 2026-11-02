---
declaration: theorem
origin: cited
lean: intervalIntegral_conj
statement: formalized
proof: formalized
---

# intervalIntegral-conj

The conjugation symmetry of the interval integral. Let $f : \mathbb{R} \to \mathbb{C}$ be a measurable function, and let $a, b \in \mathbb{R}$. Then

$$
\int_{a}^{b} \overline{f(x)} \, dx = \overline{\int_{a}^{b} f(x) \, dx}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We unfold the interval integral into an integral over a uIoc and use the conjugation property of integrals.

## Lean

Formalized as [`intervalIntegral_conj`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/intervalIntegral_conj).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaConj.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaConj.lean)
