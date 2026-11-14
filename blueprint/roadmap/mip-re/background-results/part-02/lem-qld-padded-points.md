---
declaration: lemma
origin: cited
lean: MIPRE.sum_norm_fourierVecRaw_sq, MIPRE.trVecRaw, MIPRE.sum_norm_trVecRaw_sq, MIPRE.sum_norm_char_two_sq, MIPRE.sum_avg_norm_fibre_sq, MIPRE.sum_xSqNorm_map_le, MIPRE.sum_mulVec', MIPRE.xSqNorm_eq_norm_evec_sq, MIPRE.sum_fibre_dev, MIPRE.QLD.hatOrdZX, MIPRE.QLD.hatOrdXZ, MIPRE.QLD.sum_hatOrdZX, MIPRE.QLD.sum_hatOrdXZ, MIPRE.QLD.sum_avg_xSqNorm_fibre_eq, MIPRE.QLD.padded_points
statement: formalized
proof: formalized
---

# Padded point measurements

Write a point of the padded space $\mathbb{F}_q^{4m}$ as $u = (x, z, \alpha, \beta, w)$ with $x, z \in \mathbb{F}_q^m$, $\alpha, \beta \in \mathbb{F}_q$ and $w \in \mathbb{F}_q^{2m - 2}$ the dummy coordinates. With $\delta_Q$ as in Lemma [Combined $XZ$ point measurements](lem-qld-combined-points.md), put

$$
\widehat{Q}^u_c \;=\; \widehat{Q}^{x, z, \alpha, \beta}_c
\;=\; \sum_{\substack{a, b \,:\\ \alpha a + \beta b = c}} \widehat{Q}^{x, z}_{a, b}\;,
$$

which returns the combined value $\alpha g_X(x) + \beta g_Z(z)$ and depends on $u$ only through $(x, z, \alpha, \beta)$ — that is what “independent of the dummy coordinates” means. Then $\{\widehat{Q}^{u}_c\}_{c \in \mathbb{F}_q}$ is *projective*, and

1. (**Self-consistency**) for *every* $(\alpha, \beta)$, on average over the content, $\widehat{Q}^{u}_c \otimes {I} \simeq_{2\delta_Q} {I} \otimes \widehat{Q}^{u}_c$;

2. (**Consistency with $\widehat{M}$**) on average over the content *and* over uniform $(\alpha, \beta)$,

    $$
    \begin{gathered}
    \widehat{Q}^{u}_c \otimes {I} \;\simeq_{4\delta_Q + 115352832\varepsilon}\;
    {I} \otimes \sum_{\alpha a + \beta b = c} \widehat{M}^{(\mathtt{Point}, Z), z}_b
    \widehat{M}^{(\mathtt{Point}, X), x}_a\;, \\
    \widehat{Q}^{u}_c \otimes {I} \;\simeq_{4\delta_Q + 461411328\varepsilon}\;
    {I} \otimes \sum_{\alpha a + \beta b = c} \widehat{M}^{(\mathtt{Point}, X), x}_a
    \widehat{M}^{(\mathtt{Point}, Z), z}_b\;.
    \end{gathered}
    $$

The Lean proves it for a strategy in any bipartite model, on the extension of its register model that $\widehat{Q}$ acts on (Lemma [Combined $XZ$ point measurements](lem-qld-combined-points.md)); the statement above is its tensor-product instance.

## Depends on

- [Combined $XZ$ point measurements](lem-qld-combined-points.md)
- [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)

## Proof

Both items are about the same coarse-graining and they are free for opposite reasons.

**Item 1 is free because both families are projective.** The fibres $\{(a, b) : \alpha a + \beta b = c\}$ partition $\mathbb{F}_q^2$, so the coarse-grained families are projective too — a sum of mutually orthogonal projections is a projection. For projective families the summed cross-party deviation and the agreement probability determine each other exactly, $1 - \sum_c \langle\psi| A_c \otimes B_c |\psi\rangle = \tfrac12 \sum_c \left\| {(A_c \otimes {I} - {I} \otimes B_c)|\psi\rangle} \right\|^2$, and agreement can only increase under a coarse-graining applied to both sides. So the error is unchanged, for each $(\alpha, \beta)$ separately. Note that the state-dependent distance has *no* data-processing inequality of its own; projectivity is what buys the two conversions.

**Item 2 is not free, and Parseval is what pays for it.** The right-hand families are *not* POVMs — they are products of two measurements — so the argument above does not apply, and a per-fibre triangle inequality would cost the fibre size $q$, which the conclusion cannot afford. Instead, write

$$
U_{a, b} \;=\; \bigl(\widehat{Q}^{x,z}_{a,b}\bigr)_{\textsc{A}\textsc{A}'}
- \bigl(\widehat{M}^{Z, z}_b \widehat{M}^{X, x}_a\bigr)_{\textsc{B}\textsc{A}''}\;,
\qquad
D_c \;=\; \sum_{\alpha a + \beta b = c} U_{a, b}\;,
$$

so that item 2's deviation is $\left\| {D_c |\hat\psi\rangle} \right\|$. Parseval over $\mathbb{F}_q$ turns the sum over fibres into an average over one probe, $\sum_c \left\| {D_c|\hat\psi\rangle} \right\|^2 = \mathop{\mathbb{E}}_r \left\| {\sum_{a,b} (-1)^{\operatorname{tr}(r(\alpha a + \beta b))} U_{a,b} |\hat\psi\rangle} \right\|^2$, and two things then happen. The $r = 0$ term vanishes *identically*, because $\sum_{a,b} U_{a,b} = {I} - (\sum_a \widehat{M}^X_a)(\sum_b \widehat{M}^Z_b) = 0$ — completeness of all three families, and the only place the zero-sum property is used. For $r \neq 0$ the pair $(r\alpha, r\beta)$ is uniform on $\mathbb{F}_q^2$ when $(\alpha, \beta)$ is, so averaging over $(\alpha, \beta)$ and applying Parseval over $\mathbb{F}_q^2$ (Definition [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)) returns $\sum_{a,b} \left\| {U_{a,b}|\hat\psi\rangle} \right\|^2$ exactly. Summing the $q - 1$ nonzero probes gives $\tfrac{q-1}{q} \sum_{a,b} \left\| {U_{a,b}|\hat\psi\rangle} \right\|^2$, which is item 2 of Lemma [Combined $XZ$ point measurements](lem-qld-combined-points.md) with a factor below one.

The second relation is the same argument with the two orders exchanged, using $\sum_{a,b} \widehat{M}^{X, x}_a \widehat{M}^{Z, z}_b = {I}$ in place of the other order.

## Lean

Formalized as [`MIPRE.sum_norm_fourierVecRaw_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_norm_fourierVecRaw_sq), [`MIPRE.trVecRaw`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.trVecRaw), [`MIPRE.sum_norm_trVecRaw_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_norm_trVecRaw_sq), [`MIPRE.sum_norm_char_two_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_norm_char_two_sq), [`MIPRE.sum_avg_norm_fibre_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_avg_norm_fibre_sq), [`MIPRE.sum_xSqNorm_map_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_xSqNorm_map_le), [`MIPRE.sum_mulVec'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_mulVec'), [`MIPRE.xSqNorm_eq_norm_evec_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.xSqNorm_eq_norm_evec_sq), [`MIPRE.sum_fibre_dev`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_fibre_dev), [`MIPRE.QLD.hatOrdZX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatOrdZX), [`MIPRE.QLD.hatOrdXZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatOrdXZ), [`MIPRE.QLD.sum_hatOrdZX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_hatOrdZX), [`MIPRE.QLD.sum_hatOrdXZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_hatOrdXZ), [`MIPRE.QLD.sum_avg_xSqNorm_fibre_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_avg_xSqNorm_fibre_eq), [`MIPRE.QLD.padded_points`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.padded_points).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 3260](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L3260)
