---
declaration: theorem
origin: cited
lean: Derivative.normalizedDerivOfComplex_E₂, Derivative.normalizedDerivOfComplex_E₄, Derivative.normalizedDerivOfComplex_E₆, Derivative.serreDerivative_E₂, Derivative.serreDerivative_E₄, Derivative.serreDerivative_E₆
statement: formalized
---

# ramanujan-formula

We have

$$
\begin{aligned}
E_2' &= \frac{E_2^2 - E_4}{12}\qquad\text{(26)}\\
E_4' &= \frac{E_2 E_4 - E_6}{3}\qquad\text{(27)}\\
E_6' &= \frac{E_2 E_6 - E_4^2}{2}\qquad\text{(28)}\end{aligned}
$$

## Depends on

- [serre-der-modularity](thm-serre-der-modularity.md)
- [serre-der](def-serre-der.md)
- [E2-transform-general](../part-01/lemma-e2-transform-general.md)

## Proof

In terms of Serre derivatives, these are equivalent to

$$
\begin{aligned}
\partial_{1}E_2 &= -\frac{1}{12} E_4\qquad\text{(29)}\\
\partial_{4}E_4 &= -\frac{1}{3} E_6\qquad\text{(30)}\\
\partial_{6}E_6 &= -\frac{1}{2} E_4^2\qquad\text{(31)}\end{aligned}
$$

By Theorem [serre-der-modularity](thm-serre-der-modularity.md), all the Serre derivatives are, in fact, modular. To be precise, the modularity of $\partial_{4} E_4$ and $\partial_6 E_6$ directly follows from Theorem [serre-der-modularity](thm-serre-der-modularity.md), and that of $\partial_{1}E_2$ follows from [(7)](../part-01/lemma-e2-transform-general.md). Differentiating and squaring then gives us the following:

$$
\begin{aligned}
E_2'|_{4}\gamma &= E_2' - \frac{ic}{\pi(cz + d)} E_2 - \frac{3c^2}{\pi^2 (cz + d)^2}\qquad\text{(32)}\\
E_2^2|_{4}\gamma &= E_2^2 - \frac{12ic}{\pi(cz + d)} E_2 - \frac{36c^2}{\pi^2 (cz + d)^2}\qquad\text{(33)}\end{aligned}
$$

Hence, (26)$-\frac{1}{12}$(33) is a modular form of weight 4. By [Corollary dim-mf](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L319), they should be multiples of $E_4, E_6, E_4^2$, and the proportionality constants can be determined by observing the constant terms of $q$-expansions.

## Lean

Stated as [`Derivative.normalizedDerivOfComplex_E₂`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.normalizedDerivOfComplex_E₂), [`Derivative.normalizedDerivOfComplex_E₄`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.normalizedDerivOfComplex_E₄), [`Derivative.normalizedDerivOfComplex_E₆`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.normalizedDerivOfComplex_E₆), [`Derivative.serreDerivative_E₂`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.serreDerivative_E₂), [`Derivative.serreDerivative_E₄`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.serreDerivative_E₄), [`Derivative.serreDerivative_E₆`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.serreDerivative_E₆); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 631](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L631)
