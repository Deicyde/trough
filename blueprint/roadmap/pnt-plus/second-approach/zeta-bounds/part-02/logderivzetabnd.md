---
declaration: lemma
origin: cited
lean: LogDerivZetaBnd
statement: formalized
proof: formalized
---

# LogDerivZetaBnd

There is an $A>0$ so that for $1-A/\log^9 |t| \le \sigma < 1+A/\log^9 |t|$ and $3 < |t|$,

$$
|\frac {\zeta'}{\zeta} (\sigma+it)| \ll \log^9 |t|.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaDerivUpperBnd](zetaderivupperbnd.md)
- [ZetaInvBnd](zetainvbnd.md)

## Proof

Combine the bound on $|\zeta'|$ from Lemma [ZetaDerivUpperBnd](zetaderivupperbnd.md) with the bound on $1/|\zeta|$ from Lemma [ZetaInvBnd](zetainvbnd.md).

## Lean

Formalized as [`LogDerivZetaBnd`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/LogDerivZetaBnd).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
