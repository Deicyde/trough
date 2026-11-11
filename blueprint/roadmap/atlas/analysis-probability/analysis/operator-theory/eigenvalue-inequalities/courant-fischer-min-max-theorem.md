---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CourantFischer.rayleighForm, MathlibExt.Analysis.InnerProductSpace.CourantFischer.rayleighForm_smul, MathlibExt.Analysis.InnerProductSpace.CourantFischer.inner_self_apply_eq_expansion, MathlibExt.Analysis.InnerProductSpace.CourantFischer.rayleighForm_eq_expansion, MathlibExt.Analysis.InnerProductSpace.CourantFischer.inner_eigenvectorBasis_eq_zero_of_mem_span, MathlibExt.Analysis.InnerProductSpace.CourantFischer.tailFamily, MathlibExt.Analysis.InnerProductSpace.CourantFischer.headFamily, MathlibExt.Analysis.InnerProductSpace.CourantFischer.tailFamily_linearIndependent
statement: formalized
proof: formalized
---

# Courant–Fischer min–max theorem

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html).

## Rayleigh form of an operator

The Rayleigh form of a vector for an operator `T`: `re ⟪T x, x⟫`.
On unit vectors this is the Rayleigh quotient.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.rayleighForm`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#rayleigh-form).

## Rayleigh form scales quadratically

Scaling a vector by a real scalar scales the Rayleigh form by the
square of the scalar.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.rayleighForm_smul`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#rayleigh-form-smul).

## Eigenbasis expansion of the quadratic form of a self-adjoint operator

Expansion of `⟪x, T x⟫` in the orthonormal eigenbasis: a weighted sum
of the eigenvalues with weights `‖⟪eᵢ, x⟫‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.inner_self_apply_eq_expansion`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#inner-self-apply-eq-expansion).

## Eigenbasis expansion of the Rayleigh form

The Rayleigh form expanded in the orthonormal eigenbasis.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.rayleighForm_eq_expansion`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#rayleigh-form-eq-expansion).

## Span of some eigenvectors is orthogonal to the remaining ones

A vector in the span of some of the eigenvectors is orthogonal to the
remaining eigenvectors.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.inner_eigenvectorBasis_eq_zero_of_mem_span`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#inner-eigenvector-basis-eq-zero-of-mem-s).

## Tail of an orthonormal eigenbasis

The tail of the eigenbasis: the eigenvectors with index `≥ k`,
as a family indexed by `Fin (n - k)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.tailFamily`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#tail-family).

## Head of an orthonormal eigenbasis

The head of the eigenbasis: the eigenvectors with index `≤ k`,
as a family indexed by `Fin (k + 1)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.headFamily`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#head-family).

## Linear independence of the eigenbasis tail

The tail family is linearly independent, as a restriction of the
orthonormal eigenbasis.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.tailFamily_linearIndependent`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#tail-family-linear-independent).

## Linear independence of the eigenbasis head

The head family is linearly independent, as a restriction of the
orthonormal eigenbasis.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.headFamily_linearIndependent`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#head-family-linear-independent).

## Dimension of the span of the eigenbasis tail

The span of the tail of the eigenbasis has dimension `n - k`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.finrank_span_tailFamily`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#finrank-span-tail-family).

## Dimension of the span of the eigenbasis head

The span of the head of the eigenbasis has dimension `k + 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.finrank_span_headFamily`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#finrank-span-head-family).

## Upper bound for the Rayleigh form on the eigenbasis tail

On the span of the tail of the eigenbasis, the Rayleigh form is at
most `λₖ * ‖x‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.rayleighForm_le_of_mem_tail`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#rayleigh-form-le-of-mem-tail).

## Lower bound for the Rayleigh form on the eigenbasis head

On the span of the head of the eigenbasis, the Rayleigh form is at
least `λₖ * ‖x‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.rayleighForm_ge_of_mem_head`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#rayleigh-form-ge-of-mem-head).

## The k-th eigenvector attains the Rayleigh bound on the tail

The `k`-th eigenvector lies in the tail span, is a unit vector, and
attains the Rayleigh value `λₖ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.exists_eigenvector_mem_tail`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#exists-eigenvector-mem-tail).

## The k-th eigenvector attains the Rayleigh bound on the head

The `k`-th eigenvector lies in the head span, is a unit vector, and
attains the Rayleigh value `λₖ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.exists_eigenvector_mem_head`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#exists-eigenvector-mem-head).

## Courant–Fischer min–max, extremal subspace form

There is a
subspace `W` of dimension `n - k` on which every unit vector has Rayleigh
quotient at most `λₖ`, and the bound is attained.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.exists_tail_submodule`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#exists-tail-submodule).

## Courant–Fischer min–max, lower-bound form

Every subspace of
dimension `n - k` contains a unit vector with Rayleigh quotient at
least `λₖ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.exists_unit_ge_of_submodule`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#exists-unit-ge-of-submodule).

## Courant–Fischer max–min, extremal subspace form

There is a
subspace `U` of dimension `k + 1` on which every unit vector has Rayleigh
quotient at least `λₖ`, and the bound is attained.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.exists_head_submodule`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#exists-head-submodule).

## Courant–Fischer max–min, lower-bound form

Every subspace of
dimension `k + 1` contains a unit vector with Rayleigh quotient at
most `λₖ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CourantFischer.exists_unit_le_of_submodule`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CourantFischer.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html#exists-unit-le-of-submodule).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Courant–Fischer min–max theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/eigenvalue-inequalities/courant-fischer-min-max-theorem)
