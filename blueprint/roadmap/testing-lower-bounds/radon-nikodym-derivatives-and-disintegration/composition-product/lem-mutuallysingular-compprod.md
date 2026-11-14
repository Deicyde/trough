---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure.MutuallySingular.compProd_of_left, MeasureTheory.Measure.mutuallySingular_compProd_iff, MeasureTheory.Measure.mutuallySingular_of_mutuallySingular_compProd
---

# mutuallySingular_compProd

Let $\mu, \nu$ be two $\sigma$-finite measures on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels. Let $\mu \sqcap \nu$ denote the infimum of $\mu$ and $\nu$. Then

1. if $\mu \perp \nu$ then $\mu \otimes \kappa \perp \nu \otimes \eta$,
2. $\mu \otimes \kappa \perp \nu \otimes \eta \iff (\mu \sqcap \nu) \otimes \kappa \perp (\mu \sqcap \nu) \otimes \eta$, and the same holds for any measure which is equivalent to $\mu \sqcap \nu$, like $\frac{d \mu}{d \nu} \cdot \nu$ ,
3. if $\mu \otimes \kappa \perp \nu \otimes \eta$ then for $(\mu \sqcap \nu)$-almost every $x$, $\kappa(x) \perp \eta(x)$.

## Depends on

Its statement uses no other node that has an article here.

## Proof

First, let's state two facts about mutually singular measures that we will use without proof:

- $\mu \perp (\nu + \nu') \iff \mu \perp \nu \ \wedge \ \mu \perp \nu'$ ,
- if $\mu \ll \mu'$ and $\mu' \ll \mu$ then $\mu \perp \nu \iff \mu' \perp \nu$ .

*1.* Let $s$ be a measurable set of $\mathcal X$ such that $\mu(s) = 0$ and $\nu(s^c) = 0$. One can check that the sets $s \times \mathcal Y$ and $s^c \times \mathcal Y$ demonstrate $\mu \otimes \kappa \perp \nu \otimes \eta$.

*2.* Write $\mu = \frac{d \mu}{d \nu} \cdot \nu + \mu_{\perp \nu}$ and $\nu = \frac{d \nu}{d \mu} \cdot \mu + \nu_{\perp \mu}$. Then

$$
\begin{aligned}
\mu \otimes \kappa \perp \nu \otimes \eta
&\iff \left(\frac{d \mu}{d \nu} \cdot \nu\right) \otimes \kappa \perp \left(\frac{d \nu}{d \mu} \cdot \mu\right) \otimes \eta
\\&\qquad \wedge \ \left(\frac{d \mu}{d \nu} \cdot \nu\right) \otimes \kappa \perp \nu_{\perp \mu} \otimes \eta
\\&\qquad \wedge \ \mu_{\perp \nu} \otimes \kappa \perp \left(\frac{d \nu}{d \mu} \cdot \mu\right) \otimes \eta
\\&\qquad \wedge \ \mu_{\perp \nu} \otimes \kappa \perp \nu_{\perp \mu} \otimes \eta
\end{aligned}
$$

The three last lines are true since $\mu \perp \nu_{\perp \mu}$ and $\mu_{\perp \nu} \perp \nu$. Only the first line remains. It suffices then to prove that $\mu \sqcap \nu$, $\frac{d \mu}{d \nu} \cdot \nu$ and $\frac{d \nu}{d \mu} \cdot \mu$ are equivalent.

TODO

*3.* By 2. it suffices to consider the case $\nu = \mu$ and show that for $\mu$-almost every $x$, $\kappa(x) \perp \eta(x)$. Let $s$ be a measurable set of $\mathcal X \times \mathcal Y$ such that $(\mu \otimes \kappa)(s) = 0$ and $(\mu \otimes \eta)(s^c) = 0$. Then

$$
\begin{aligned}
0 &= (\mu \otimes \kappa)(s)
\\
&= \int_{x} \kappa(x)(\{y \mid (x, y) \in s\}) \partial \mu
\: .
\end{aligned}
$$

Hence for $\mu$-almost all $x$, $\kappa(x)(\{y \mid (x, y) \in s\}) = 0$. Similarly, for $\mu$-almost all $x$, $\eta(x)(\{y \mid (x, y) \in s^c\}) = 0$. Since $\{y \mid (x, y) \in s^c\} = \{y \mid (x, y) \in s\}^c$, we have a measurable set witnessing $\kappa(x) \perp \eta(x)$ for $\mu$-almost all $x$.

## Lean

Formalized as [`MeasureTheory.Measure.MutuallySingular.compProd_of_left`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.Measure.MutuallySingular.compProd_of_left), [`MeasureTheory.Measure.mutuallySingular_compProd_iff`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.Measure.mutuallySingular_compProd_iff), [`MeasureTheory.Measure.mutuallySingular_of_mutuallySingular_compProd`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.Measure.mutuallySingular_of_mutuallySingular_compProd).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 83](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L83)
