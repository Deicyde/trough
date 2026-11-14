---
declaration: theorem
origin: cited
lean: ramanujan_E₂, ramanujan_E₄, ramanujan_E₆, ramanujan_E₂', ramanujan_E₄', ramanujan_E₆'
statement: formalized
proof: formalized
---

# ramanujan-formula

We have

$$
\begin{aligned}
E_2' &= \frac{E_2^2 - E_4}{12}\qquad\text{(36)}\\
E_4' &= \frac{E_2 E_4 - E_6}{3}\qquad\text{(37)}\\
E_6' &= \frac{E_2 E_6 - E_4^2}{2}\qquad\text{(38)}\end{aligned}
$$

## Depends on

- [serre-der-modularity](thm-serre-der-modularity.md)
- [serre-der](def-serre-der.md)
- [E2-transform-general](../part-01/lemma-e2-transform-general.md)
- [dim-mf](../part-02/cor-dim-mf.md)

## Proof

In terms of Serre derivatives, these are equivalent to

$$
\begin{aligned}
\partial_{1}E_2 &= -\frac{1}{12} E_4\qquad\text{(39)}\\
\partial_{4}E_4 &= -\frac{1}{3} E_6\qquad\text{(40)}\\
\partial_{6}E_6 &= -\frac{1}{2} E_4^2\qquad\text{(41)}\end{aligned}
$$

By Theorem [serre-der-modularity](thm-serre-der-modularity.md), all the Serre derivatives are, in fact, modular. To be precise, the modularity of $\partial_{4} E_4$ and $\partial_6 E_6$ directly follows from Theorem [serre-der-modularity](thm-serre-der-modularity.md), and that of $\partial_{1}E_2$ follows from [(7)](../part-01/lemma-e2-transform-general.md). Differentiating and squaring then gives us the following:

$$
\begin{aligned}
E_2'|_{4}\gamma &= E_2' - \frac{ic}{\pi(cz + d)} E_2 - \frac{3c^2}{\pi^2 (cz + d)^2}\qquad\text{(42)}\\
E_2^2|_{4}\gamma &= E_2^2 - \frac{12ic}{\pi(cz + d)} E_2 - \frac{36c^2}{\pi^2 (cz + d)^2}\qquad\text{(43)}\end{aligned}
$$

Hence, (36)$-\frac{1}{12}$(43) is a modular form of weight 4. By [Corollary dim-mf](../part-02/cor-dim-mf.md), they should be multiples of $E_4, E_6, E_4^2$, and the proportionality constants can be determined by observing the constant terms of $q$-expansions.

## Lean

Formalized as [`ramanujan_E₂`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ramanujan_E₂), [`ramanujan_E₄`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ramanujan_E₄), [`ramanujan_E₆`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ramanujan_E₆), [`ramanujan_E₂'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ramanujan_E₂'), [`ramanujan_E₄'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ramanujan_E₄'), [`ramanujan_E₆'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ramanujan_E₆').

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 607](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L607)
