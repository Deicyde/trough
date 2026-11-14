---
declaration: lemma
origin: cited
lean: MIPRE.ValueApprox.ExactStrategy, MIPRE.ValueApprox.ExactStrategy.IsValid, MIPRE.ValueApprox.ExactStrategy.EntriesIn, MIPRE.ValueApprox.ExactStrategy.value, MIPRE.ValueApprox.ExactStrategy.toStrategy, MIPRE.ValueApprox.ExactStrategy.value_le_quantumValue, MIPRE.ValueApprox.abs_bornValue_sub_le, MIPRE.ValueApprox.exists_exactStrategy_value_gt, MIPRE.ValueApprox.lt_quantumValue_iff
statement: formalized
proof: formalized
---

# Exact rational strategies suffice

An *exact strategy* for a game $\mathfrak{G}$ is the data of dimensions $d_\textsc{A}, d_\textsc{B}$, matrices $A^x_a \in \mathbb{C}^{d_\textsc{A} \times d_\textsc{A}}$ and $B^y_b \in \mathbb{C}^{d_\textsc{B} \times d_\textsc{B}}$, and a vector $u \in \mathbb{C}^{d_\textsc{A}} \otimes \mathbb{C}^{d_\textsc{B}}$; it is *valid* if each $\{A^x_a\}_a$ and each $\{B^y_b\}_b$ is a projective measurement and $u \neq 0$, and its value is

$$
\omega \;=\; \frac{1}{\left\| {u} \right\|^2} \sum_{x,y} \mu(x,y) \sum_{a,b} D(x,y,a,b)\,
\langleu| A^x_a \otimes B^y_b |u\rangle,
$$

a rational function of the entries. Suppose the answer alphabets of $\mathfrak{G}$ are nonempty. Then for every real $t$, $\mathrm{val}^*(\mathfrak{G}) > t$ if and only if some valid exact strategy with all entries in $\mathbb{Q}(i)$ has value $\omega > t$.

## Depends on

- [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)
- [Gaussian-rational projective measurements are dense](lem-rational-pvm-dense.md)
- [The perturbation split](lem-perturbation-split.md)

## Proof

A valid exact strategy with the state normalized to $u/\left\| {u} \right\|$ is a tensor-product strategy of value $\omega$, so $\omega \leq \mathrm{val}^*(\mathfrak{G})$. Conversely, if $\mathrm{val}^*(\mathfrak{G}) > t$ then, $\mathrm{val}^*$ being a supremum over a nonempty set, some tensor-product strategy $(\psi, \{A^x_a\}, \{B^y_b\})$ has value $v > t$, and it suffices to find, for every $\varepsilon > 0$, a valid exact strategy with $\mathbb{Q}(i)$ entries of value $> v - \varepsilon$. Replace each $\{A^x_a\}_a$ and $\{B^y_b\}_b$ by a $\mathbb{Q}(i)$ projective measurement within $\eta$ of it (Lemma [Gaussian-rational projective measurements are dense](lem-rational-pvm-dense.md)), and $\psi$ by an entrywise rounding $u \neq 0$ with $\left\| {u - \psi} \right\| \leq \eta/4$, so that $\left\| {u/\left\| {u} \right\| - \psi} \right\| \leq \eta/2$. The value is Lipschitz in the data: by Lemma [The perturbation split](lem-perturbation-split.md), a Born term $\langle\psi| A \otimes B |\psi\rangle$ changes by at most $\left\| {A - A'} \right\|\left\| {B} \right\| + \left\| {A'} \right\|\left\| {B - B'} \right\| + 2\left\| {A'} \right\|\left\| {B'} \right\|\left\| {\psi - \psi'} \right\|$ between unit vectors $\psi, \psi'$, using $\left\| {A \otimes B} \right\| \leq \left\| {A} \right\|\left\| {B} \right\|$; projections have norm at most one, so each term moves by at most $4\eta$ and the value, a $\mu$-average of sums of at most $\left\vert {\mathcal{A}} \right\vert\left\vert {\mathcal{B}} \right\vert$ such terms, by at most $4\left\vert {\mathcal{A}} \right\vert\left\vert {\mathcal{B}} \right\vert\eta$. Take $\eta < \varepsilon / (4\left\vert {\mathcal{A}} \right\vert\left\vert {\mathcal{B}} \right\vert)$.

## Lean

Formalized as [`MIPRE.ValueApprox.ExactStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.ExactStrategy), [`MIPRE.ValueApprox.ExactStrategy.IsValid`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.ExactStrategy.IsValid), [`MIPRE.ValueApprox.ExactStrategy.EntriesIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.ExactStrategy.EntriesIn), [`MIPRE.ValueApprox.ExactStrategy.value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.ExactStrategy.value), [`MIPRE.ValueApprox.ExactStrategy.toStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.ExactStrategy.toStrategy), [`MIPRE.ValueApprox.ExactStrategy.value_le_quantumValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.ExactStrategy.value_le_quantumValue), [`MIPRE.ValueApprox.abs_bornValue_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.abs_bornValue_sub_le), [`MIPRE.ValueApprox.exists_exactStrategy_value_gt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.exists_exactStrategy_value_gt), [`MIPRE.ValueApprox.lt_quantumValue_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.lt_quantumValue_iff).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 7388](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L7388)
