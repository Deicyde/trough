---
declaration: lemma
origin: cited
lean: general_hoelder
statement: formalized
proof: formalized
---

# general_hoelder

Let $G$ be a finite abelian group and $f:G\to\mathbb{C}$. Let $\nu:G\to \mathbb{R}_{\geq 0}$ be such that whenever $\left\lvert f\right\rvert\neq 0$ we have $\nu \geq 1$. Let $\Delta\subseteq \Delta_\eta(f)$. Then, for any $m\geq 1$.

$$
\eta^{2m}\frac{\lVert f\rVert_1^2}{\lVert f\rVert_2^2}\left\lvert \Delta\right\rvert^{2m}\le E_{2m}(\Delta;\nu).
$$

## Depends on

- [Large spectrum](large-spec.md)
- [Weighted energy](weight-energy.md)

## Proof

By definition of $\Delta_\eta(f)$ we know that

$$
\eta\lVert f\rVert_1\left\lvert \Delta\right\rvert\le \sum_{\gamma\in\Delta} \lvert \widehat{f}(\gamma)\rvert.
$$

There exists some $c_\gamma\in\mathbb{C}$ with $\lvert c_\gamma\rvert=1$ for all $\gamma$ such that

$$
\lvert \widehat{f}(\gamma)\rvert=c_\gamma\widehat{f}(\gamma)=c_\gamma \sum_{x\in G}f(x)\overline{\gamma(x)}.
$$

Interchanging the sums, therefore,

$$
\eta\lVert f\rVert_1\left\lvert \Delta\right\rvert\le \sum_{x\in G}f(x)\sum_{\gamma\in\Delta} c_\gamma \overline{\gamma(x)}.
$$

By Hölder's inequality the right-hand side is at most

$$
\left( \sum_x \left\lvert f(x)\right\rvert\right)^{1-1/m}\left( \sum_x \left\lvert f(x)\right\rvert\left\lvert \sum_{\gamma\in\Delta}c_\gamma\overline{\gamma(x)}\right\rvert^m\right)^{1/m}.
$$

Taking $m$th powers, therefore, we have

$$
\eta^m\left\lvert \Delta\right\rvert^m\lVert f\rVert_1\le \sum_{x}\left\lvert f(x)\right\rvert\left\lvert \sum_{\gamma\in\Delta}c_\gamma\overline{\gamma(x)}\right\rvert^m.
$$

By assumption we can bound $\left\lvert f(x)\right\rvert\le \left\lvert f(x)\right\rvert\nu(x)^{1/2}$, and therefore by the Cauchy-Schwarz inequality the right-hand side is bounded above by

$$
\lVert f\rVert_2\left( \sum_x \nu(x)\left\lvert \sum_{\gamma\in\Delta}c_\gamma\overline{\gamma(x)}\right\rvert^{2m}\right)^{1/2}.
$$

Squaring and simplifying, we deduce that

$$
\eta^{2m}\left\lvert \Delta\right\rvert^{2m}\frac{\lVert f\rVert_1^2}{\lVert f\rVert_2^2}\le \sum_x \nu(x)\left\lvert \sum_{\gamma\in\Delta}c_\gamma\overline{\gamma(x)}\right\rvert^{2m}.
$$

Expanding out the power, the right-hand side is equal to

$$
\sum_x \nu(x)\sum_{\gamma_1,\ldots,\gamma_{2m}}c_{\gamma_1}\cdots \overline{c_{\gamma_{2m}}} (\overline{\gamma_1}\cdots \gamma_{2m})(x).
$$

Changing the order of summation this is equal to

$$
\sum_{\gamma_1,\ldots,\gamma_{2m}}c_{\gamma_1}\cdots \overline{c_{\gamma_{2m}}}
\widehat{\nu}(\gamma_1\cdots \overline{\gamma_{2m}}).
$$

The result follows by the triangle inequality.

## Lean

Formalized as [`general_hoelder`](https://yaeldillies.github.io/apap/docs/find/#doc/general_hoelder).

## Sources

- [Kelley-Meka bound blueprint: chapter/chang.tex, line 100](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/chang.tex#L100)
