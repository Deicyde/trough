---
declaration: theorem
origin: cited
lean: deriv_riemannZeta_conj
statement: formalized
proof: formalized
---

# deriv-riemannZeta-conj

Conjugation symmetry of the derivative of the Riemann zeta function. Let $s \in \mathbb{C}$. Then

$$
\zeta'(\overline{s}) = \overline{\zeta'(s)}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [deriv-conj-conj](deriv-conj-conj.md)

## Proof

We apply the derivative conjugation symmetry to the Riemann zeta function and use the conjugation symmetry of the Riemann zeta function itself.

## Lean

Formalized as [`deriv_riemannZeta_conj`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/deriv_riemannZeta_conj).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaConj.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/ZetaConj.lean)
