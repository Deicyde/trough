---
declaration: theorem
origin: cited
lean: norm_zeta_strict_mono_ofReal
statement: formalized
proof: formalized
---

# norm-zeta-strict-mono-ofReal

If $a,b\in\mathbb{R}$ with $1\lt b\lt a$, then

$$
|\zeta(a)|<|\zeta(b)|.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Expand out $\zeta$ as a summation (we can do this as we are in the region of convergence) and ignore the norm as every term is positive and real. Comparing term by term proves the result.

## Lean

Formalized as [`norm_zeta_strict_mono_ofReal`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/norm_zeta_strict_mono_ofReal).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/StrongPNT.lean)
