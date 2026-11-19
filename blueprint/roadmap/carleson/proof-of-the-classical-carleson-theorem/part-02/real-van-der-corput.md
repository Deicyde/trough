---
declaration: lemma
origin: cited
lean: real_van_der_Corput
statement: formalized
proof: formalized
---

# real van der Corput

For any $x\in {\mathbb{R}}$ and $R>0$ and any function $\varphi: X\to {\mathbb{C}}$ supported on $B'=B(x,R)$ such that

$$
\|\varphi\|_{\operatorname{\operatorname{Lip}}(B')} = \sup_{x \in B'} |\varphi(x)| + R \sup_{x,y \in B', x \neq y} \frac{|\varphi(x) - \varphi(y)|}{\rho(x,y)}
$$

is finite and for any $n,m\in \mathbb{Z}$, we have

$$
\left|\int_{B'} e({\vartheta}_n(x)-{{\vartheta}_m(x)}) \varphi(x) d\mu(x)\right|\le 2\pi \mu(B')\frac{\|\varphi\|_{\operatorname{\operatorname{Lip}}(B')}}{1+d_{B'}({\vartheta}_n,{\vartheta}_m)}
\, .\qquad\text{(50)}
$$

## Depends on

- [van der Corput](../part-01/van-der-corput.md)

## Proof

Set $n'=n-m$. Then we have to prove

$$
\left|\int_{x-R}^{x+R} e^{in'y}\varphi(y) dy\right|\le 4\pi R\|\varphi\|_{\operatorname{\operatorname{Lip}}(B')}
(1+2R|n'|)^{-1}\, .\qquad\text{(51)}
$$

This follows from [van der Corput](../part-01/van-der-corput.md) with $\alpha = x - R$ and $\beta = x + R$.

## Lean

Formalized as [`real_van_der_Corput`](https://fpvandoorn.github.io/carleson/docs/find/#doc/real_van_der_Corput).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9467](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9467)
