---
declaration: lemma
origin: cited
lean: MIPRE.snorm_sq_mul_le_of_contraction, MIPRE.snorm_sq_sum_proj_mul, MIPRE.sum_snorm_sq_cool, MIPRE.sum_fibre_fst, MIPRE.sum_snorm_sq_cool_prod, MIPRE.IsPVM.aOp, MIPRE.IsPVM.bOp, MIPRE.sum_xSqNorm_marg_le, MIPRE.sum_snorm_sq_mul_proj_le, MIPRE.sum_xSqNorm_marg_le'
statement: formalized
proof: formalized
---

# Cool closeness fact, and the marginal step

Let $\{A_i\}_{i \in {\mathcal{A}}}$ be a projective measurement and $\{B_i\}$ any family of operators on the same space, with $\sum_i \left\| {(A_i - B_i)|\psi\rangle} \right\|^2 \leq \delta$. Then for any map $f : {\mathcal{A}} \to {\mathcal{B}}$,

$$
\sum_{k} \Bigl\| \sum_{i \,:\, f(i) = k} \bigl( A_i - A_i B_i \bigr) |\psi\rangle \Bigr\|^2
\;\leq\; \delta\;,\qquad\text{(5)}
$$

*simultaneously* over all the fibres of $f$ — multiplying each element by $A$'s own element costs nothing, and neither does summing along a fibre.

Consequently, if $\{Q_{a,b}\}$ is a projective measurement on $\mathbb{C}^{d_\textsc{A}}$ with outcomes pairs, $\{Z_b\}$ is a projective measurement on $\mathbb{C}^{d_\textsc{B}}$, and $\{X_a\}$ is any family on $\mathbb{C}^{d_\textsc{B}}$, then the $b$-marginal of $Q$ inherits $Q$'s consistency with the ordered product:

$$
\sum_a \left\| {\Bigl( \bigl(\sum_b Q_{a,b}\bigr) \otimes {I} - {I} \otimes X_a \Bigr)
|\psi\rangle} \right\|^2
\;\leq\; 2 \sum_{a, b} \left\| {\bigl( Q_{a,b} \otimes Z_b - Q_{a,b} \otimes {I} \bigr)|\psi\rangle} \right\|^2
+ 2 \sum_{a, b} \left\| {\bigl( Q_{a,b} \otimes {I} - {I} \otimes Z_b X_a \bigr)|\psi\rangle} \right\|^2\;.\qquad\text{(6)}
$$

## Depends on

- [State-dependent POVM distance](def-state-distance.md)
- [Cross-party state-dependent distance](def-cross-distance.md)

## Proof

For (5): projectivity gives $A_i - A_i B_i = A_i (A_i - B_i)$, and the cross terms of one fibre vanish because $A_i A_{i'} = 0$ for $i \neq i'$, so the fibre's squared norm is the sum of its terms' squared norms. Each term loses only $A_i \leq {I}$, and the fibres are disjoint, so the outer sum is absorbed rather than repeated.

For (6), the intermediate operator is $\sum_b Q_{a,b} \otimes Z_b$. Reaching it from $\sum_b Q_{a,b} \otimes {I}$ is exactly the first part, applied along the fibres of the first projection. Reaching ${I} \otimes X_a$ from it uses $\sum_b Z_b = {I}$ to write the difference as $\sum_b ({I} \otimes Z_b)\bigl( Q_{a,b} \otimes {I} - {I} \otimes Z_b X_a \bigr)$, whose terms are again mutually orthogonal — which is what makes the sum over the summed-out outcome free rather than a factor $|{\mathcal{B}}|$. One triangle inequality joins the two.

## Lean

Formalized as [`MIPRE.snorm_sq_mul_le_of_contraction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.snorm_sq_mul_le_of_contraction), [`MIPRE.snorm_sq_sum_proj_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.snorm_sq_sum_proj_mul), [`MIPRE.sum_snorm_sq_cool`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_cool), [`MIPRE.sum_fibre_fst`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_fibre_fst), [`MIPRE.sum_snorm_sq_cool_prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_cool_prod), [`MIPRE.IsPVM.aOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.aOp), [`MIPRE.IsPVM.bOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.bOp), [`MIPRE.sum_xSqNorm_marg_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_xSqNorm_marg_le), [`MIPRE.sum_snorm_sq_mul_proj_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_mul_proj_le), [`MIPRE.sum_xSqNorm_marg_le'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_xSqNorm_marg_le').

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 820](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L820)
