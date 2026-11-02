---
declaration: lemma
origin: cited
lean: cauchy_formula_deriv
statement: formalized
proof: formalized
---

# cauchy-formula-deriv

Let $f$ be analytic on $|z|\leq R$. For any $z$ with $|z|\leq r$ and any $r'$ with $0 < r < r' < R$ we have

$$
f'(z)=\frac{1}{2\pi i}\oint_{|w|=r'}\frac{f(w)}{(w-z)^2}\,dw=\frac{1}{2\pi}
\int_0^{2\pi}\frac{r'e^{it}\,f(r'e^{it})}{(r'e^{it}-z)^2}\,dt.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is just Cauchy's integral formula for derivatives.

## Lean

Formalized as [`cauchy_formula_deriv`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/cauchy_formula_deriv).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
