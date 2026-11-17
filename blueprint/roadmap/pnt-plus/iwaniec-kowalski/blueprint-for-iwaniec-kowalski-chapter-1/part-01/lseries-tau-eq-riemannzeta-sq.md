---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeries_tau_eq_riemannZeta_sq
statement: formalized
proof: formalized
---

# LSeries tau eq riemannZeta sq

The L-series of $\tau$ equals the square of the Riemann zeta function for $\Re(s) > 1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [zeta mul zeta](zeta-mul-zeta.md)

## Proof

From the previous theorem, we have that the Dirichlet convolution of $\zeta$ with itself is $\tau$. Taking L-series on both sides, we get $L(\tau, s) = L(\zeta, s) \cdot L(\zeta, s)$. Since $L(\zeta, s)$ is the Riemann zeta function $\zeta(s)$, we conclude that $L(\tau, s) = \zeta(s)^2$ for $\Re(s) > 1$.

## Lean

Formalized as [`ArithmeticFunction.LSeries_tau_eq_riemannZeta_sq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeries_tau_eq_riemannZeta_sq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
