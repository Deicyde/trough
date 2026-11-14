---
declaration: lemma
origin: cited
lean: MIPRE.sum_hsNormSq_sub_le
statement: formalized
proof: formalized
---

# Closeness from two disagreements

Let $\{O_i\}_{i \in I}$, $\{C_i\}_{i \in I}$, $\{D_i\}_{i \in I}$ be finite families of projections on $\mathbb{C}^{d \times d}$ with $\sum_i \tau(O_i) = 1$ and $\sum_i \tau(C_i D_i) = 1$. Then

$$
\sum_i \left\| {C_i D_i - O_i} \right\|_{hs}^2 \;\leq\; 3 \Bigl( \sum_i \tau\bigl(O_i (1 - D_i)\bigr)
+ \sum_i \tau\bigl(O_i (1 - C_i)\bigr) \Bigr).
$$

## Depends on

- [Normalized Hilbert–Schmidt norm](def-hs-norm.md)

## Proof

Write $X_i = (1 - C_i) O_i$ and $Y_i = (1 - D_i) O_i$, so that $C_i O_i = O_i - X_i$ and $D_i O_i = O_i - Y_i$. Since $1 - C_i$ and $1 - D_i$ are projections, $\left\| {X_i} \right\|_{hs}^2 = \tau(O_i (1 - C_i))$ and $\left\| {Y_i} \right\|_{hs}^2 = \tau(O_i (1 - D_i))$; write $\beta$ and $\alpha$ for the two sums, which are therefore nonnegative. Expanding the left-hand side and using $\sum_i \tau(C_i D_i) = \sum_i \tau(O_i) = 1$,

$$
\sum_i \left\| {C_i D_i - O_i} \right\|_{hs}^2 \;=\; 2 - 2 \sum_i \tau(O_i D_i C_i).
$$

Since $O_i$ is a projection, $\tau(O_i D_i C_i) = \langle D_i O_i, C_i O_i \rangle_{hs} = \langle O_i - Y_i, O_i - X_i \rangle_{hs}$, which expands to $\tau(O_i) - \tau(O_i(1 - C_i)) - \tau(O_i(1 - D_i)) + \langle Y_i, X_i \rangle_{hs}$. Summing over $i$, $\sum_i \tau(O_i D_i C_i) = 1 - \alpha - \beta + \sum_i \langle Y_i, X_i \rangle_{hs}$, and Cauchy–Schwarz followed by the arithmetic–geometric mean inequality gives $\bigl| \sum_i \langle Y_i, X_i \rangle_{hs} \bigr| \leq \sqrt{\alpha}\sqrt{\beta} \leq (\alpha + \beta)/2$. Hence $\sum_i \left\| {C_i D_i - O_i} \right\|_{hs}^2 \leq 2(\alpha + \beta) + (\alpha + \beta)$.

## Lean

Formalized as [`MIPRE.sum_hsNormSq_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_hsNormSq_sub_le).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1260](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1260)
