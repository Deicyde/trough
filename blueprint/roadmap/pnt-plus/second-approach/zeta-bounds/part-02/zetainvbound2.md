---
declaration: lemma
origin: cited
lean: ZetaInvBound2
statement: formalized
proof: formalized
---

# ZetaInvBound2

For $\sigma>1$ (and $\sigma \le 2$),

$$
1/|\zeta(\sigma+it)| \ll (\sigma-1)^{-3/4}(\log |t|)^{1/4},
$$

as $|t|\to\infty$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaUpperBnd](zetaupperbnd.md)
- [ZetaInvBound1](zetainvbound1.md)
- [ZetaNear1BndExact](zetanear1bndexact.md)

## Proof

Combine Lemma [ZetaInvBound1](zetainvbound1.md) with the bounds in Lemmata [ZetaNear1BndExact](zetanear1bndexact.md) and [ZetaUpperBnd](zetaupperbnd.md).

## Lean

Formalized as [`ZetaInvBound2`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaInvBound2).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
