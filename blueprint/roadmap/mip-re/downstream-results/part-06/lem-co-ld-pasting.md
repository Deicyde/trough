---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.Pasting.chernoffBernoulliMatrix, MIPRE.LIDT.Co.Pasting.LdPastingConclusion, MIPRE.LIDT.Co.Pasting.ldPastingNCompleteness, MIPRE.LIDT.Co.Pasting.ldPastingSubMeas, MIPRE.LIDT.Co.Pasting.ldPastingNontrivial, MIPRE.LIDT.Co.Pasting.ldPasting
statement: formalized
proof: formalized
---

# Pasting, in a symmetric model

Consider an $(\varepsilon, \delta, \gamma)$-good symmetric strategy in $S$ for the low individual degree test in $m + 1$ variables, with point measurements $A^w$ in $\mathcal{P}$ for $w = (u, x) \in \mathbb{F}_q^{m+1}$. For each $x \in \mathbb{F}_q$ let $G^x$ be a projective submeasurement in $\mathcal{P}$ whose outcomes are the polynomials in $m$ variables, and $Z^x \in \mathcal{P}$. Suppose that for some $\kappa$ and $\eta$:

1. *(completeness)* $\mathrm{ev}\bigl(L(\mathop{\mathbb{E}}_x G^x_{\mathrm{total}})\bigr) \geq 1 - \kappa$;
2. *(consistency with the points)* $\mathop{\mathbb{E}}_{(u, x)} \mathrm{cons}\bigl(A^{(u, x)}, G^{x, [u]}\bigr) \leq \eta$;
3. *(strong self-consistency)* $\mathop{\mathbb{E}}_x \sum_g \| (L(G^x_g) - R(G^x_g)) \Psi \|^2 \leq \eta$;
4. *(boundedness)* $Z^x \geq 0$ and $\mathop{\mathbb{E}}_u A^{(u, x)}_{g(u)} \leq Z^x$ for all $x$ and $g$, and $\mathop{\mathbb{E}}_x \mathrm{ev}\bigl(L(1 - G^x_{\mathrm{total}})\, R(Z^x)\bigr) \leq \eta$;

with uniformly random $u$ and $x$. Then for every $k \geq 400\, m d$ there is a measurement $H$ in $\mathcal{P}$ whose outcomes are the polynomials in $m + 1$ variables with

$$
\mathop{\mathbb{E}}_w \mathrm{cons}\bigl(A^w, H^{[w]}\bigr) \leq \kappa \Bigl(1 + \frac{1}{100 m}\Bigr) + 2 \nu +
e^{-k / (80000 m^2)}, \qquad \nu = 100\, k^2 m \Bigl(\varepsilon^{1/32} + \delta^{1/32} +
\gamma^{1/32} + \eta^{1/32} + \Bigl(\frac{d}{q}\Bigr)^{1/32}\Bigr),
$$

for a uniformly random point $w \in \mathbb{F}_q^{m+1}$.

## Depends on

- [Symmetric models](../part-05/def-sym-model.md)
- [Commutation of the slice measurements, in a symmetric model](lem-co-commutation-g.md)

## Proof depends on

- [The switch sandwich and self-consistency, in a symmetric model](lem-co-switch-sandwich-self-consistency.md)
- [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)

## Proof

The proof is the vendored one, `MIPStarRE.LDT.Pasting.ldPasting` in `MIPRE/Background/LIDT/MIPStarRE/LDT/Pasting/`, rewritten over the symmetric model (`planning/c6b-plan.md`, milestone M11). For $k$ distinct heights $x_1, \dots, x_k$ the sandwiched product $G^{x_1}_{g_1} \dots G^{x_k}_{g_k} \dots G^{x_1}_{g_1}$ is a submeasurement in $\mathcal{P}$, and $H$ interpolates the tuples $(g_1, \dots, g_k)$ that at least $d + 1$ slices answer and that agree with one polynomial in $m + 1$ variables; the missing mass goes to one fixed outcome. Consistency with the points is a chain of comparisons, each a Cauchy–Schwarz estimate for the vector state: the slice measurements commute approximately (Lemma [Commutation of the slice measurements, in a symmetric model](lem-co-commutation-g.md)), so a slice can be moved through the sandwich; a line through the heights is consistent with the interpolant except on a set of tuples of small mass; and the tuples that miss interpolation are at most a binomial tail in the averaged complete operator $\mathop{\mathbb{E}}_x G^x_{\mathrm{total}}$. The vendored proof bounds that tail by a matrix Chernoff estimate, which is the scalar Hoeffding bound lifted through the continuous functional calculus with no factor of the dimension, and holds verbatim for an operator on $K$ in a vector state. When $k = 0$, or $\gamma$, $\eta$ or $d/q$ exceeds $1$, the bound is at least $1$; when $d = 0$, $H$ is built from the average of the slices, each read as a polynomial in $m + 1$ variables. Where the vendored proof uses the permutation invariance of the state, the port uses $\mathrm{ev}(L(x)) = \mathrm{ev}(R(x))$ (Lemma [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)).

## Lean

Formalized as [`MIPRE.LIDT.Co.Pasting.chernoffBernoulliMatrix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Pasting.chernoffBernoulliMatrix), [`MIPRE.LIDT.Co.Pasting.LdPastingConclusion`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Pasting.LdPastingConclusion), [`MIPRE.LIDT.Co.Pasting.ldPastingNCompleteness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Pasting.ldPastingNCompleteness), [`MIPRE.LIDT.Co.Pasting.ldPastingSubMeas`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Pasting.ldPastingSubMeas), [`MIPRE.LIDT.Co.Pasting.ldPastingNontrivial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Pasting.ldPastingNontrivial), [`MIPRE.LIDT.Co.Pasting.ldPasting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Pasting.ldPasting).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 4040](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L4040)
