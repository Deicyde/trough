---
declaration: lemma
origin: cited
lean: MIPRE.sum_ntr_mul_ge
statement: formalized
proof: formalized
---

# Close measurements have close values

Let $\{O_i\}_{i \in I}$, $\{C_i\}_{i \in I}$, $\{D_i\}_{i \in I}$ be finite families of projections on $\mathbb{C}^{d \times d}$ with $\sum_i \tau(O_i) = 1$, and let $\mathrm{acc} \subseteq I$. Then

$$
\sum_{i \in \mathrm{acc}} \tau(O_i)
\;-\; 2 \sqrt{\sum_i \left\| {C_i D_i - O_i} \right\|_{hs}^2}
\;\leq\; \sum_{i \in \mathrm{acc}} \tau(C_i D_i).
$$

## Depends on

- [Normalized Hilbert–Schmidt norm](def-hs-norm.md)

## Proof

This is the measurement-level form of (NW19, Fact 4.31), in the one direction a soundness argument needs and in the synchronous setting, where $\tau((C_iD_i)^\dagger C_iD_i) = \tau(C_iD_i)$ makes the products a measurement on the nose. Put $w_i = C_iD_i - O_i$. Then $\tau(C_iD_i) = \left\| {C_iD_i} \right\|_{hs}^2 = \left\| {O_i + w_i} \right\|_{hs}^2 = \tau(O_i) + 2\langle O_i, w_i\rangle_{hs} + \left\| {w_i} \right\|_{hs}^2$. Summing over $\mathrm{acc}$ and dropping the last term, which is nonnegative,

$$
\sum_{i \in \mathrm{acc}} \tau(C_iD_i) \;\geq\; \sum_{i \in \mathrm{acc}} \tau(O_i)
- 2 \Bigl| \sum_{i \in \mathrm{acc}} \langle O_i, w_i \rangle_{hs} \Bigr|,
$$

and Cauchy–Schwarz over the index bounds the last modulus by $\sqrt{\sum_{i \in \mathrm{acc}} \tau(O_i)} \cdot \sqrt{\sum_{i \in \mathrm{acc}} \left\| {w_i} \right\|_{hs}^2} \leq 1 \cdot \sqrt{\sum_i \left\| {w_i} \right\|_{hs}^2}$.

## Lean

Formalized as [`MIPRE.sum_ntr_mul_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_ntr_mul_ge).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1293](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1293)
