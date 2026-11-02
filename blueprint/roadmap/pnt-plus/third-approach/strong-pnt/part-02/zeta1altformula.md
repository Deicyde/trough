---
declaration: theorem
origin: cited
lean: Zeta1AltFormula
statement: formalized
proof: formalized
---

# Zeta1AltFormula

We have that

$$
\zeta_1(s)=\zeta_0(1,s)
$$

where $\zeta_0(1,s)$ comes from Definition [riemannZeta0](../../../second-approach/zeta-bounds/part-01/riemannzeta0.md).

## Depends on

- [riemannZeta1](riemannzeta1.md)
- [riemannZeta0](../../../second-approach/zeta-bounds/part-01/riemannzeta0.md)

## Proof

Note that

$$
\zeta_0(1,s)=1+\frac{-1}{1-s}+\frac{-1}{2}+
s\int_1^\infty\frac{\lfloor x\rfloor+1/2-x}{x^{s+1}}\,dx.
$$

With minor simplifications we have

$$
\zeta_0(1,s)=1+\frac{1}{s-1}-\frac{1}{2}+
\frac{s}{2}\int_1^\infty x^{-s-1}\,dx-s\int_1^\infty\{x\}\,x^{-s-1}\,dx.
$$

The first integral evaluates to $1/s$ (when $0\lt \mathfrak{R}s$), so this term when multiplied by the $s/2$ cancels with the $-1/2$. This exactly gives $\zeta_1$.

## Lean

Formalized as [`Zeta1AltFormula`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Zeta1AltFormula).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
