---
declaration: lemma
origin: cited
lean: Zeta_diff_Bnd
statement: formalized
proof: formalized
---

# Zeta-diff-Bnd

For any $A>0$ sufficiently small, there is a constant $C>0$ so that whenever $1- A / \log t \le \sigma_1 < \sigma_2\le 2$ and $3 < |t|$, we have that:

$$
|\zeta (\sigma_2 + it) - \zeta (\sigma_1 + it)|
\le C (\log |t|)^2 (\sigma_2 - \sigma_1).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Zeta-eq-int-derivZeta](zeta-eq-int-derivzeta.md)
- [ZetaDerivUpperBnd](zetaderivupperbnd.md)

## Proof

Use Lemma [Zeta-eq-int-derivZeta](zeta-eq-int-derivzeta.md) and estimate trivially using Lemma [ZetaDerivUpperBnd](zetaderivupperbnd.md).

## Lean

Formalized as [`Zeta_diff_Bnd`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Zeta_diff_Bnd).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
