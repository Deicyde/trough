---
declaration: lemma
origin: cited
lean: ZetaInvBnd
statement: formalized
proof: formalized
---

# ZetaInvBnd

For any $A>0$ sufficiently small, there is a constant $C>0$ so that whenever $1- A / \log^9 |t| \le \sigma < 1+A/\log^9 |t|$ and $3 < |t|$, we have that:

$$
1/|\zeta(\sigma+it)| \le C \log^7 |t|.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaInvBound2](zetainvbound2.md)
- [Zeta-diff-Bnd](zeta-diff-bnd.md)

## Proof

Let $\sigma$ be given in the prescribed range, and set $\sigma' := 1+ A / \log^9 |t|$. Then

$$
|\zeta(\sigma+it)| \ge
|\zeta(\sigma'+it)| - |\zeta(\sigma+it) - \zeta(\sigma'+it)|
\ge
C (\sigma'-1)^{3/4}\log |t|^{-1/4} - C \log^2 |t| (\sigma'-\sigma)
$$

$$
\ge
C A^{3/4} \log |t|^{-7} - C \log^2 |t| (2 A / \log^9 |t|),
$$

where we used Lemma [ZetaInvBound2](zetainvbound2.md) and Lemma [Zeta-diff-Bnd](zeta-diff-bnd.md). Now by making $A$ sufficiently small (in particular, something like $A = 1/16$ should work), we can guarantee that

$$
|\zeta(\sigma+it)| \ge \frac C 2 (\log |t|)^{-7},
$$

as desired.

## Lean

Formalized as [`ZetaInvBnd`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaInvBnd).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
