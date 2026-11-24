---
declaration: lemma
origin: cited
lean: LogDerivZetaHolcSmallT
statement: formalized
proof: formalized
---

# LogDerivZetaHolcSmallT

There is a $\sigma_2 < 1$ so that the function

$$
\frac {\zeta'}{\zeta}(s)
$$

is holomorphic on $\{ \sigma_2 \le \Re s \le 2, |\Im s| \le 3 \} \setminus \{1\}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaNoZerosInBox](zetanozerosinbox.md)

## Proof

The derivative of $\zeta$ is holomorphic away from $s=1$; the denominator $\zeta(s)$ is nonzero in this range by Lemma [ZetaNoZerosInBox](zetanozerosinbox.md).

## Lean

Formalized as [`LogDerivZetaHolcSmallT`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/LogDerivZetaHolcSmallT).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/ZetaBounds.lean)
