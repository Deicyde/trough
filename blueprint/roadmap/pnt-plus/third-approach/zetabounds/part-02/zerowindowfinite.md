---
declaration: theorem
origin: cited
lean: ZeroWindowFinite
statement: formalized
proof: formalized
---

# ZeroWindowFinite

For all $|t|\geq 2$, $\mathcal{Z}(t)$ contains a finite number of points.

## Depends on

- [ZeroWindow](zerowindow.md)

## Proof

If we suppose the opposite, i.e. that there are an infinite number of zeta zeros in this region, then $\zeta\equiv 0$ by the identity theorem. This is a contradiction, so the statement must be true.

## Lean

Formalized as [`ZeroWindowFinite`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZeroWindowFinite).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/StrongPNT.lean)
