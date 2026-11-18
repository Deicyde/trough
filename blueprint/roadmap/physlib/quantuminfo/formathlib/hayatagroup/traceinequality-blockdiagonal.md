---
declaration: module
origin: cited
lean: JensenOperatorInequality.HSum, JensenOperatorInequality.hsumEquiv, JensenOperatorInequality.hsumProj, JensenOperatorInequality.hsumIncl, JensenOperatorInequality.hsumProj_hsumIncl_apply, JensenOperatorInequality.inner_hsumIncl_hsumIncl, JensenOperatorInequality.hsumIncl_adjoint, JensenOperatorInequality.hsumProj_adjoint
statement: formalized
proof: formalized
---

# `2 × 2` block operators on a Hilbert sum

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.BlockDiagonal`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean): 22 declarations, 7 with a docstring.

> This file develops the operator-matrix ("block operator") calculus on the two-fold Hilbert
> sum `ℋ ⊕ ℋ`, the main tool in the block-operator proof of the Jensen operator inequality.

## Main definitions

> * `HSum ℋ`: the `ℓ²` direct sum `ℋ ⊕ ℋ` of two copies of a Hilbert space `ℋ`, realised as
>   `PiLp 2 (fun _ : Fin 2 => ℋ)`.
> * `hsumProj`, `hsumIncl`: the coordinate projections `HSum ℋ →L[ℂ] ℋ` and inclusions
>   `ℋ →L[ℂ] HSum ℋ` exhibiting `HSum ℋ` as a direct sum; they are mutually adjoint.
> * `blockDiagonal A B`: the block-diagonal operator `diag(A, B)` on `HSum ℋ`.
> * `blockOp A00 A01 A10 A11`: a general `2 × 2` block operator on `HSum ℋ`.
> * `blockDiagonalHom`: the `⋆`-algebra homomorphism `(A, B) ↦ diag(A, B)`.
>
> Here `L ℋ = ℋ →L[ℂ] ℋ` is the algebra of bounded operators (quantum observables) on `ℋ`;
> representing a pair of observables as a block-diagonal operator on `ℋ ⊕ ℋ` is the dilation
> trick underlying the operator inequalities used throughout quantum information theory.

**`JensenOperatorInequality.HSum`**, an abbrev, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L47).

> A two-fold Hilbert sum used for the block-operator proof of Jensen's inequality.
> The inner-product instance on `ℋ` is unused by the underlying type synonym but kept to
> document that `HSum ℋ` is the `ℓ²` direct sum of two copies of a Hilbert space.

```lean
abbrev HSum (ℋ : Type u) [NormedAddCommGroup ℋ] [InnerProductSpace ℂ ℋ] : Type u
```

**`JensenOperatorInequality.hsumEquiv`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L52).

> The continuous linear equivalence between the Hilbert sum `HSum ℋ` and the plain
> function space `Fin 2 → ℋ`, forgetting the `ℓ²` inner-product structure on the index.

```lean
noncomputable def hsumEquiv (ℋ : Type u) [NormedAddCommGroup ℋ] [InnerProductSpace ℂ ℋ] :
    HSum ℋ ≃L[ℂ] (Fin 2 → ℋ)
```

**`JensenOperatorInequality.hsumProj`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L58).

> The `i`-th coordinate projection `HSum ℋ →L[ℂ] ℋ` of the Hilbert sum onto its
> `i`-th summand.

```lean
noncomputable def hsumProj (ℋ : Type u) [NormedAddCommGroup ℋ] [InnerProductSpace ℂ ℋ]
    (i : Fin 2) : HSum ℋ →L[ℂ] ℋ
```

**`JensenOperatorInequality.hsumIncl`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L65).

> The `i`-th coordinate inclusion `ℋ →L[ℂ] HSum ℋ`, embedding `ℋ` as the `i`-th summand
> of the Hilbert sum and placing `0` in the other summand.

```lean
noncomputable def hsumIncl (ℋ : Type u) [NormedAddCommGroup ℋ] [InnerProductSpace ℂ ℋ]
    (i : Fin 2) : ℋ →L[ℂ] HSum ℋ
```

**`JensenOperatorInequality.hsumProj_hsumIncl_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L71).

```lean
lemma hsumProj_hsumIncl_apply (i j : Fin 2) (x : ℋ) :
    hsumProj ℋ i (hsumIncl ℋ j x) = if i = j then x else 0
```

**`JensenOperatorInequality.inner_hsumIncl_hsumIncl`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L76).

```lean
lemma inner_hsumIncl_hsumIncl (i j : Fin 2) (x y : ℋ) :
    inner ℂ (hsumIncl ℋ i x) (hsumIncl ℋ j y) = if i = j then inner ℂ x y else 0
```

**`JensenOperatorInequality.hsumIncl_adjoint`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L81).

```lean
lemma hsumIncl_adjoint (i : Fin 2) :
    (hsumIncl ℋ i).adjoint = hsumProj ℋ i
```

**`JensenOperatorInequality.hsumProj_adjoint`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L94).

```lean
lemma hsumProj_adjoint (i : Fin 2) :
    (hsumProj ℋ i).adjoint = hsumIncl ℋ i
```

**`JensenOperatorInequality.hsumIncl_proj_sum`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L102).

```lean
lemma hsumIncl_proj_sum (z : HSum ℋ) :
    hsumIncl ℋ 0 (hsumProj ℋ 0 z) + hsumIncl ℋ 1 (hsumProj ℋ 1 z) = z
```

**`JensenOperatorInequality.blockDiagonal`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L108).

> The block diagonal operator `diag(A, B)` on the two-fold Hilbert sum.

```lean
noncomputable def blockDiagonal (A B : L ℋ) : L (HSum ℋ)
```

**`JensenOperatorInequality.blockOp`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L112).

> A general `2 × 2` block operator on `HSum ℋ`.

```lean
noncomputable def blockOp (A00 A01 A10 A11 : L ℋ) : L (HSum ℋ)
```

**`JensenOperatorInequality.blockOp_ext`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L119).

```lean
lemma blockOp_ext {T S : L (HSum ℋ)}
    (h0 : ∀ z : HSum ℋ, hsumProj ℋ 0 (T z) = hsumProj ℋ 0 (S z))
    (h1 : ∀ z : HSum ℋ, hsumProj ℋ 1 (T z) = hsumProj ℋ 1 (S z)) :
    T = S
```

**`JensenOperatorInequality.blockDiagonal_star`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L129).

```lean
lemma blockDiagonal_star (A B : L ℋ) :
    star (blockDiagonal (ℋ := ℋ) A B) = blockDiagonal (ℋ := ℋ) (star A) (star B)
```

**`JensenOperatorInequality.blockDiagonalHom`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L138).

> The `ℝ`-`⋆`-algebra homomorphism sending a pair of operators `(A, B)` to the
> block-diagonal operator `diag(A, B)` on the Hilbert sum.

```lean
noncomputable def blockDiagonalHom : (L ℋ × L ℋ) →⋆ₐ[ℝ] L (HSum ℋ)
```

**`JensenOperatorInequality.blockDiagonalHom_apply`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L167).

```lean
lemma blockDiagonalHom_apply (p : L ℋ × L ℋ) :
    blockDiagonalHom (ℋ := ℋ) p = blockDiagonal (ℋ := ℋ) p.1 p.2
```

**`JensenOperatorInequality.hsumProj_blockDiagonal_zero`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L172).

```lean
lemma hsumProj_blockDiagonal_zero (A B : L ℋ) (z : HSum ℋ) :
    hsumProj ℋ 0 (blockDiagonal A B z) = A (hsumProj ℋ 0 z)
```

**`JensenOperatorInequality.hsumProj_blockDiagonal_one`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L177).

```lean
lemma hsumProj_blockDiagonal_one (A B : L ℋ) (z : HSum ℋ) :
    hsumProj ℋ 1 (blockDiagonal A B z) = B (hsumProj ℋ 1 z)
```

**`JensenOperatorInequality.blockDiagonal_one`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L182).

```lean
lemma blockDiagonal_one :
    blockDiagonal (ℋ := ℋ) (1 : L ℋ) (1 : L ℋ) = (1 : L (HSum ℋ))
```

**`JensenOperatorInequality.blockDiagonal_nonneg`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L188).

```lean
lemma blockDiagonal_nonneg {A B : L ℋ} (hA : 0 ≤ A) (hB : 0 ≤ B) :
    0 ≤ blockDiagonal (ℋ := ℋ) A B
```

**`JensenOperatorInequality.hsumProj_blockOp_zero`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L233).

```lean
lemma hsumProj_blockOp_zero (A00 A01 A10 A11 : L ℋ) (z : HSum ℋ) :
    hsumProj ℋ 0 (blockOp (ℋ := ℋ) A00 A01 A10 A11 z) =
      A00 (hsumProj ℋ 0 z) + A01 (hsumProj ℋ 1 z)
```

**`JensenOperatorInequality.hsumProj_blockOp_one`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L239).

```lean
lemma hsumProj_blockOp_one (A00 A01 A10 A11 : L ℋ) (z : HSum ℋ) :
    hsumProj ℋ 1 (blockOp (ℋ := ℋ) A00 A01 A10 A11 z) =
      A10 (hsumProj ℋ 0 z) + A11 (hsumProj ℋ 1 z)
```

**`JensenOperatorInequality.blockOp_star`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean#L245).

```lean
lemma blockOp_star (A00 A01 A10 A11 : L ℋ) :
    star (blockOp (ℋ := ℋ) A00 A01 A10 A11) =
      blockOp (ℋ := ℋ) (star A00) (star A10) (star A01) (star A11)
```

## Depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LownerHeinzTheorem](traceinequality-lownerheinztheorem.md)

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/BlockDiagonal.lean)
