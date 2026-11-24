---
declaration: lemma
origin: cited
lean: limitOfConstant
statement: formalized
proof: formalized
---

# limitOfConstant

Let $a:\mathbb{R}\to\mathbb{C}$ be a function, and let $\sigma>0$ be a real number. Suppose that, for all $\sigma, \sigma'>0$, we have $a(\sigma')=a(\sigma)$, and that $\lim_{\sigma\to\infty}a(\sigma)=0$. Then $a(\sigma)=0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

$$
\begin{aligned}
\lim_{\sigma'\to\infty}a(\sigma) &= \lim_{\sigma'\to\infty}a(\sigma') \\
&= 0
\end{aligned}
$$

## Lean

Formalized as [`limitOfConstant`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/limitOfConstant).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/PerronFormula.lean)
