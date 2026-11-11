---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.mapsTo_eigenspace_comp, MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.injective_restrict_eigenspace_comp, MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.surjective_restrict_eigenspace_comp, MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.eigenspaceCompEquiv, MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.finrank_eigenspace_comp_eq, MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.hasEigenvector_comp, MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.hasEigenvalue_comp_iff, MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.mapsTo_genEigenspace_comp
statement: formalized
proof: formalized
---

# Eigenvalues of the products AB and BA

28 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html).

## Eigenspace of fg maps into the eigenspace of gf

`g` sends the `μ`-eigenspace of `f ∘ₗ g` into the `μ`-eigenspace of
`g ∘ₗ f`: if `(f ∘ₗ g) x = μ • x` then `(g ∘ₗ f) (g x) = μ • (g x)`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.mapsTo_eigenspace_comp`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#maps-to-eigenspace-comp).

## Injectivity of g between eigenspaces of fg and gf

The map `g` restricted to the eigenspaces is injective when `μ ≠ 0`: if
`g x = 0` for an eigenvector `x` of `f ∘ₗ g`, then `(f ∘ₗ g) x = 0 = μ • x`,
so `x = 0`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.injective_restrict_eigenspace_comp`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#injective-restrict-eigenspace-comp).

## Surjectivity of g between eigenspaces of fg and gf

The map `g` restricted to the eigenspaces is surjective when `μ ≠ 0`: an
eigenvector `y` of `g ∘ₗ f` is the image of `μ⁻¹ • f y`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.surjective_restrict_eigenspace_comp`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#surjective-restrict-eigenspace-comp).

## Linear equivalence of eigenspaces of fg and gf

For a nonzero eigenvalue, the eigenspaces of `f ∘ₗ g` and of `g ∘ₗ f`
are linearly equivalent, via `g` in one direction.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.eigenspaceCompEquiv`, a definition declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#eigenspace-comp-equiv).

## Geometric multiplicities of fg and gf agree

The geometric multiplicities of a nonzero eigenvalue of `f ∘ₗ g` and of
`g ∘ₗ f` agree.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.finrank_eigenspace_comp_eq`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finrank-eigenspace-comp-eq).

## Eigenvectors of fg map to eigenvectors of gf

An eigenvector of `f ∘ₗ g` for a nonzero eigenvalue is sent by `g` to an
eigenvector of `g ∘ₗ f` for the same eigenvalue.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.hasEigenvector_comp`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#has-eigenvector-comp).

## Nonzero eigenvalues of fg and gf coincide

A nonzero scalar is an eigenvalue of `f ∘ₗ g` iff it is an eigenvalue of
`g ∘ₗ f`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.hasEigenvalue_comp_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#has-eigenvalue-comp-iff).

## Generalized eigenspace of fg maps into that of gf

`g` sends the generalized `μ`-eigenspace of `f ∘ₗ g` into the generalized
`μ`-eigenspace of `g ∘ₗ f`, for every exponent. This is the intertwining
`(g ∘ₗ f) ∘ₗ g = g ∘ₗ (f ∘ₗ g)` applied to Mathlib's
`Module.End.mapsTo_genEigenspace_of_comp`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.mapsTo_genEigenspace_comp`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#maps-to-gen-eigenspace-comp).

## Kernel of g meets a generalized eigenspace of fg trivially

If `g x = 0` and `x` lies in the generalized `μ`-eigenspace of `f ∘ₗ g`
with `μ ≠ 0`, then `x = 0`. Indeed, on the kernel of `g` the map `f ∘ₗ g`
vanishes, so `(f ∘ₗ g - μ • 1) ^ l` acts as `(-μ) ^ l • 1` there.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.eq_zero_of_apply_eq_zero_of_mem_genEigenspace`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#eq-zero-of-apply-eq-zero-of-mem-gen-eige).

## Restriction of g to generalized eigenspaces of fg and gf

The restriction of `g` to the generalized `μ`-eigenspaces.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.genEigenspaceCompMap`, a definition declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#gen-eigenspace-comp-map).

## Injectivity of g on generalized eigenspaces of fg

The restriction of `g` to a generalized `μ`-eigenspace with `μ ≠ 0` is
injective.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.injective_genEigenspaceCompMap`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#injective-gen-eigenspace-comp-map).

## Generalized eigenspaces of fg and gf are finite-dimensional together

For a nonzero scalar, the generalized eigenspaces of `f ∘ₗ g` and of
`g ∘ₗ f` are finite-dimensional together, for every exponent `k : ℕ∞`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.finite_genEigenspace_comp_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finite-gen-eigenspace-comp-iff).

## Generalized eigenspaces of fg and gf have equal dimension

The generalized `μ`-eigenspaces of `f ∘ₗ g` and of `g ∘ₗ f` have equal
`Module.finrank`, for every exponent `k : ℕ∞` and every nonzero `μ`.
They are finite-dimensional together; if both are infinite-dimensional, both
finranks are zero. In finite dimension only the stabilized generalized eigenspace
(for example at exponent `⊤`) measures algebraic multiplicity.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.finrank_genEigenspace_comp_eq`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finrank-gen-eigenspace-comp-eq).

## Eigenspaces of fg and gf are equivalent, for endomorphisms

The `*` form of `eigenspaceCompEquiv`, for endomorphisms of one space.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.eigenspaceMulEquiv`, a definition declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#eigenspace-mul-equiv).

## Geometric multiplicities of fg and gf agree, for endomorphisms

The `*` form of `finrank_eigenspace_comp_eq`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.finrank_eigenspace_mul_eq`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finrank-eigenspace-mul-eq-2).

## Eigenvectors of fg map to eigenvectors of gf, for endomorphisms

The `*` form of `hasEigenvector_comp`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.hasEigenvector_mul`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#has-eigenvector-mul).

## Nonzero eigenvalues of fg and gf coincide, for endomorphisms

The `*` form of `hasEigenvalue_comp_iff`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.hasEigenvalue_mul_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#has-eigenvalue-mul-iff-2).

## Generalized eigenspace dimensions agree, for endomorphisms

The `*` form of `finrank_genEigenspace_comp_eq`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.finrank_genEigenspace_mul_eq`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finrank-gen-eigenspace-mul-eq-2).

## Generalized eigenspaces finite-dimensional together, for endomorphisms

The `*` form of `finite_genEigenspace_comp_iff`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.End.finite_genEigenspace_mul_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finite-gen-eigenspace-mul-iff-2).

## Nonzero eigenvalues of matrix products AB and BA coincide

A nonzero scalar is an eigenvalue of the matrix product `A * B` iff it is
an eigenvalue of `B * A`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.Matrix.hasEigenvalue_mul_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#has-eigenvalue-mul-iff-3).

## Geometric multiplicities of matrix products AB and BA agree

The geometric multiplicities of a nonzero eigenvalue of `A * B` and of
`B * A` agree.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.Matrix.finrank_eigenspace_mul_eq`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finrank-eigenspace-mul-eq-3).

## Generalized eigenspaces of AB and BA have equal dimension

The generalized `μ`-eigenspaces of `A * B` and of `B * A` have equal
`Module.finrank`, for every exponent `k : ℕ∞`.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.Matrix.finrank_genEigenspace_mul_eq`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finrank-gen-eigenspace-mul-eq-3).

## Generalized eigenspaces of AB and BA are finite-dimensional together

The generalized eigenspaces of rectangular products in opposite orders
are finite-dimensional together for a nonzero scalar and every exponent.

Formalized by `MathlibExt.LinearAlgebra.Eigenspace.MulComm.Matrix.finite_genEigenspace_mul_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Eigenspace/MulComm.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finite-gen-eigenspace-mul-iff-3).

## Nonzero eigenvalues of ST and TS coincide

A nonzero scalar is an eigenvalue of `S * T` iff it is an eigenvalue of
`T * S`, for bounded operators.

Formalized by `MathlibExt.Analysis.Normed.Operator.EigenvalueMulComm.ContinuousLinearMap.hasEigenvalue_mul_iff`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#has-eigenvalue-mul-iff).

## Equal geometric multiplicities of nonzero eigenvalues of ST and TS

The geometric multiplicities of a nonzero eigenvalue of `S * T` and of
`T * S` agree, for bounded operators.

Formalized by `MathlibExt.Analysis.Normed.Operator.EigenvalueMulComm.ContinuousLinearMap.finrank_eigenspace_mul_eq`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finrank-eigenspace-mul-eq).

## Equal dimensions of generalized eigenspaces of ST and TS

The generalized `μ`-eigenspaces of `S * T` and of `T * S` have equal
`Module.finrank`, for every exponent `k : ℕ∞`, for bounded operators.

Formalized by `MathlibExt.Analysis.Normed.Operator.EigenvalueMulComm.ContinuousLinearMap.finrank_genEigenspace_mul_eq`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finrank-gen-eigenspace-mul-eq).

## Finite-dimensionality of generalized eigenspaces of ST and TS

Generalized eigenspaces of reversed bounded-operator products are
finite-dimensional together for a nonzero scalar and every exponent.

Formalized by `MathlibExt.Analysis.Normed.Operator.EigenvalueMulComm.ContinuousLinearMap.finite_genEigenspace_mul_iff`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#finite-gen-eigenspace-mul-iff).

## Nonzero eigenvalues of an operator times its adjoint, in either order

A nonzero scalar is an eigenvalue of `T† * T` iff it is an eigenvalue of
`T * T†`, on a Hilbert space.

Formalized by `MathlibExt.Analysis.Normed.Operator.EigenvalueMulComm.ContinuousLinearMap.hasEigenvalue_adjoint_mul_self_iff`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/EigenvalueMulComm.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html#has-eigenvalue-adjoint-mul-self-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eigenvalues of the products AB and BA](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-of-the-products-ab-and-ba)
