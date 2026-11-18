---
declaration: lemma
origin: cited
lean: LogDerivZetaHolcLargeT9
statement: formalized
proof: formalized
---

# LogDerivZetaHolcLargeT9

There is an $A>0$ so that for all $T>3$, the function $\frac {\zeta'}{\zeta}(s)$ is holomorphic on $\{1-A/\log^9 T \le \Re s \le 2, |\Im s|\le T \}\setminus\{1\}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaZeroFree9](zetazerofree9.md)
- [ZetaNoZerosInBox](zetanozerosinbox.md)

## Proof

The derivative of $\zeta$ is holomorphic away from $s=1$; the denominator $\zeta(s)$ is nonzero in this range by Lemma [ZetaZeroFree9](zetazerofree9.md).

## Lean

Formalized as [`LogDerivZetaHolcLargeT9`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/LogDerivZetaHolcLargeT9).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/ZetaBounds.lean)
