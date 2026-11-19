---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.indVec, MIPRE.LowDegree.indPair, MIPRE.LowDegree.indPair_eq_eval, MIPRE.LowDegree.acGamma, MIPRE.LowDegree.acTuples, MIPRE.LowDegree.cTuples, MIPRE.LowDegree.card_acTuples_add_card_cTuples, MIPRE.LowDegree.prob_anticommuting_ge, MIPRE.LowDegree.prob_commuting_ge
statement: formalized
proof: formalized
---

# Anticommuting question tuples

Let ${\mathrm{ind}}_m(x) \in \mathbb{F}_q^M$, $M = 2^m$, be the vector $({\mathrm{ind}}_{m,y}(x))_y$ of the indicator polynomials of Definition [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md) evaluated at a point $x \in \mathbb{F}_q^m$, and call a tuple $\omega = (u_X, u_Z, r_X, r_Z) \in (\mathbb{F}_q^m)^2 \times \mathbb{F}_q^2$ *anticommuting* if

$$
\gamma(\omega) \;=\; \operatorname{tr}_{q \to 2}\bigl( (r_X \cdot {\mathrm{ind}}_m(u_X)) \cdot
(r_Z \cdot {\mathrm{ind}}_m(u_Z)) \bigr) \;\neq\; 0\;,
$$

the inner product being the one of $\mathbb{F}_q^M$, and *commuting* otherwise. The two cases partition the sample space. If $m \geq 1$ and $d \geq 1$ then a uniformly random $\omega$ is anticommuting with probability at least $(1 - 3md/q)/2$, and commuting with probability at least $(1 - 3md/q)/2$.

## Depends on

- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)
- [Schwartz–Zippel](../part-05/lem-schwartz-zippel.md)

## Proof depends on

- [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)

## Proof

Because ${\mathrm{ind}}_m(x) \cdot {\mathrm{ind}}_m(z) = g_{{\mathrm{ind}}_m(x)}(z)$ — one low-degree encoding evaluated at the other point — $\gamma(\omega) = \operatorname{tr}_{q \to 2}(r_X r_Z \cdot g_{{\mathrm{ind}}_m(u_X)}(u_Z))$. The vector ${\mathrm{ind}}_m(x)$ has coordinate sum $\prod_i (x_i + (1 - x_i)) = 1$, so it is never zero and $g_{{\mathrm{ind}}_m(u_X)}$ is a nonzero multilinear polynomial; by Lemma [Schwartz–Zippel](../part-05/lem-schwartz-zippel.md) it vanishes at no more than an $m/q$ fraction of the $u_Z$. Fix $u_X, u_Z$ with $g_{{\mathrm{ind}}_m(u_X)}(u_Z) \neq 0$ and $r_X \neq 0$, and put $c = r_X\, g_{{\mathrm{ind}}_m(u_X)}(u_Z) \neq 0$. Then $r \mapsto \operatorname{tr}_{q \to 2}(c r)$ is a nonzero $\mathbb{F}_2$-linear functional on $\mathbb{F}_q$, so its kernel is a hyperplane and exactly $q/2$ of the $r_Z$ give $\gamma \neq 0$, the other $q/2$ giving $\gamma = 0$. Multiplying the three independent estimates gives $(1 - 1/q)(1 - m/q)/2 \geq (1 - (m+1)/q)/2$ for the anticommuting case; the commuting case gains the whole $r_X = 0$ slice and the whole $g_{{\mathrm{ind}}_m(u_X)}(u_Z) = 0$ slice, so $(1 - 1/q)/2$ holds for it with no $m$ at all. Finally $m + 1 \leq 3md$ and $1 \leq 3md$ when $m, d \geq 1$.

## Lean

Formalized as [`MIPRE.LowDegree.indVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.indVec), [`MIPRE.LowDegree.indPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.indPair), [`MIPRE.LowDegree.indPair_eq_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.indPair_eq_eval), [`MIPRE.LowDegree.acGamma`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.acGamma), [`MIPRE.LowDegree.acTuples`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.acTuples), [`MIPRE.LowDegree.cTuples`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.cTuples), [`MIPRE.LowDegree.card_acTuples_add_card_cTuples`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.card_acTuples_add_card_cTuples), [`MIPRE.LowDegree.prob_anticommuting_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.prob_anticommuting_ge), [`MIPRE.LowDegree.prob_commuting_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.prob_commuting_ge).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 1993](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L1993)
