---
declaration: theorem
origin: cited
lean: GlobalBound
statement: formalized
proof: formalized
---

# GlobalBound

For all $s\in\mathbb{C}$ with $|s|\leq 1$ and $t\in\mathbb{R}$ with $|t|\geq 2$, we have that

$$
|\zeta(s+3/2+it)|\leq 7+2\,|t|.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaAltFormula](zetaaltformula.md)
- [riemannZeta1](riemannzeta1.md)

## Proof

For the sake of clearer proof writing let $z=s+3/2+it$. Since $|s|\leq 1$ we know that $1/2\leq\mathfrak{R}z$; additionally, as $|t|\geq 2$, we know $1\leq|\mathfrak{I}z|$. So, $z\in S$. Thus, from Lemma [ZetaAltFormula](zetaaltformula.md) we know that

$$
|\zeta(z)|\leq 1+\frac{1}{|z-1|}
+|z|\cdot\left|\int_1^\infty\{x\}\,x^{-z}\,\frac{dx}{x}\right|
$$

by applying the triangle inequality. Now note that $|z-1|\geq 1$. Likewise,

$$
|z|\cdot\left|\int_1^\infty\{x\}\,x^{-z}\,\frac{dx}{x}\right|
\leq|z|\int_1^\infty|\{x\}\,x^{-z-1}|\,dx
\leq|z|\int_1^\infty x^{-\Re z-1}\,dx=\frac{|z|}{\Re z}\leq 2\,|z|.
$$

Thus we have that,

$$
|\zeta(s+3/2+it)|=|\zeta(z)|\leq 1+1+2\,|z|=2+2\,|s+3/2+it|
\leq2+2\,|s|+3+2\,|it|\leq 7+2\,|t|.
$$

## Lean

Formalized as [`GlobalBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/GlobalBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
