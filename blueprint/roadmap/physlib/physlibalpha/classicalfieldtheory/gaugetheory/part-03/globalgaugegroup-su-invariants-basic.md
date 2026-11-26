---
declaration: module
origin: cited
lean: suTensor.offDiag, suTensor.diagDiff, suTensor.adjMat_offDiag, suTensor.adjMat_offDiag_of_ne, suTensor.offDiag_self, suTensor.adjMat_diagDiff, suTensor.diagDiff_self, suTensor.adjMat_adjRep_planeEmbed
statement: formalized
proof: formalized
---

# What commutes with the adjoint action of `SU(N)`, and the Reynolds element of its tensors

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Invariants.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean): 30 declarations, 17 with a docstring.

> Schur's lemma for the adjoint representation, and the Haar average over the tensors.

## i. Overview

> The elements `SU.planeEmbed p q U` of `SU(N)`, an element `U` of `SU(2)` acting on the plane of two
> coordinates (`PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Adjoint`), do all
> the work. A diagonal phase `diag (u, ū)`, the rotation by a quarter turn, and the rotation by an
> eighth of a turn, embedded in every plane, force a linear endomorphism of the complexified Lie
> algebra `ℂ ⊗[ℝ] su(N)` commuting with the adjoint action to be scalar (A); this is computed on the
> matrices `adjMat A`, which identify the complexified Lie algebra with the traceless complex
> matrices. With Schur's lemma for the fundamental representation, `SU.eq_smul_one_of_commute`,
> these are the facts behind the classification of the invariant tensors of `SU(N)` with a
> fundamental and an anti-fundamental index, and with one or two adjoint indices.
>
> The tensors of `SU(N)` have a Reynolds element, the Haar average over the compact group, so the
> invariants in the range of an equivariant map out of them come from invariant tensors (B).

## ii. Key results

> - `suTensor.eq_smul_id_of_commute_adjRep` : an endomorphism of the complexified Lie algebra
>   commuting with the adjoint action is scalar.
> - `suTensor.hasReynolds` : the tensors of `SU(N)` have a Reynolds element.

## iv. References

> * None.

## A. Endomorphisms of the complexified Lie algebra commuting with `SU(N)`

**`suTensor.offDiag`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L67).

> The matrix unit at `(x, y)` off the diagonal, as an element of the complexified Lie algebra,
> and zero on the diagonal.

```lean
noncomputable def offDiag (x y : Fin N) : SUAlgebraComplexified N
```

**`suTensor.diagDiff`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L72).

> The difference of the diagonal matrix units at `x` and at `y`, as an element of the
> complexified Lie algebra.

```lean
noncomputable def diagDiff (x y : Fin N) : SUAlgebraComplexified N
```

**`suTensor.adjMat_offDiag`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L75).

```lean
lemma adjMat_offDiag (x y : Fin N) :
    adjMat N (offDiag x y) = if x = y then 0 else single x y 1
```

**`suTensor.adjMat_offDiag_of_ne`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L82).

```lean
lemma adjMat_offDiag_of_ne {x y : Fin N} (h : x ≠ y) : adjMat N (offDiag x y) = single x y 1
```

**`suTensor.offDiag_self`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L86).

```lean
lemma offDiag_self (x : Fin N) : offDiag x x = 0
```

**`suTensor.adjMat_diagDiff`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L90).

```lean
lemma adjMat_diagDiff (x y : Fin N) : adjMat N (diagDiff x y) = single x x 1 - single y y 1
```

**`suTensor.diagDiff_self`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L94).

```lean
lemma diagDiff_self (x : Fin N) : diagDiff x x = 0
```

**`suTensor.adjMat_adjRep_planeEmbed`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L99).

> The adjoint action of an element of `SU(2)` embedded in a plane of two coordinates on a
> matrix supported on that plane is the conjugation of the matrix on the plane.

```lean
lemma adjMat_adjRep_planeEmbed {p q : Fin N} (hpq : p ≠ q) (U : SU 2)
    (A : SUAlgebraComplexified N) (M : Matrix (Fin 2) (Fin 2) ℂ)
    (hA : adjMat N A = planeInclusion p q * M * (planeInclusion p q)ᵀ) :
    adjMat N (adjRep N (planeEmbed p q hpq U) A)
      = planeInclusion p q * (U.1 * M * U.1ᴴ) * (planeInclusion p q)ᵀ
```

**`suTensor.sqrtI`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L108).

> The phase `(1 + i) / √2`, a square root of `i` of modulus one.

```lean
noncomputable def sqrtI : ℂ
```

**`suTensor.star_sqrtI`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L110).

```lean
lemma star_sqrtI : star sqrtI = (1 - Complex.I) / (Real.sqrt 2 : ℂ)
```

**`suTensor.sqrtI_mul_star`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L113).

```lean
lemma sqrtI_mul_star : sqrtI * star sqrtI = 1
```

**`suTensor.sqrtI_mul_self`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L122).

```lean
lemma sqrtI_mul_self : sqrtI * sqrtI = Complex.I
```

**`suTensor.star_sqrtI_mul_self`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L131).

```lean
lemma star_sqrtI_mul_self : star sqrtI * star sqrtI = -Complex.I
```

**`suTensor.sqrtI_ne_I`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L134).

```lean
lemma sqrtI_ne_I : sqrtI ≠ Complex.I
```

**`suTensor.star_sqrtI_ne_I`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L140).

```lean
lemma star_sqrtI_ne_I : star sqrtI ≠ Complex.I
```

**`suTensor.adjMat_adjRep_apply_of_diagonal`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L148).

> The adjoint action of a diagonal matrix of `SU(N)` scales the entry at `(x, y)` by
> `d x * star (d y)`.

```lean
lemma adjMat_adjRep_apply_of_diagonal {g : SU N} {d : Fin N → ℂ} (hg : g.1 = diagonal d)
    (A : SUAlgebraComplexified N) (x y : Fin N) :
    adjMat N (adjRep N g A) x y = d x * adjMat N A x y * star (d y)
```

**`suTensor.map_offDiag_eq_smul`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L161).

> For two distinct coordinates `p` and `q`, an endomorphism commuting with the adjoint action
> sends the matrix unit at `(p, q)` to a multiple of itself. The phase `diag (ω, ω̄)` in the
> plane of `p` and `q`, with `ω² = i`, multiplies that matrix unit by `i` and no other entry
> by `i`.

```lean
lemma map_offDiag_eq_smul (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) {p q : Fin N} (hpq : p ≠ q) :
    L (offDiag p q) = adjMat N (L (offDiag p q)) p q • offDiag p q
```

**`suTensor.adjRep_quarterTurn_offDiag`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L208).

> The quarter turn in the plane of `p` and `q` sends the matrix unit at `(p, q)` to minus the
> one at `(q, p)`.

```lean
lemma adjRep_quarterTurn_offDiag {p q : Fin N} (hpq : p ≠ q) :
    adjRep N (planeEmbed p q hpq (rotation 0 1 (by norm_num))) (offDiag p q) = -offDiag q p
```

**`suTensor.coeff_offDiag_swap`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L223).

> The coefficients of the matrix units at `(p, q)` and at `(q, p)` agree.

```lean
lemma coeff_offDiag_swap (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) {p q : Fin N} (hpq : p ≠ q) :
    adjMat N (L (offDiag q p)) q p = adjMat N (L (offDiag p q)) p q
```

**`suTensor.invSqrtTwo`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L233).

> The cosine and sine of an eighth of a turn, the real number `1 / √2`.

```lean
noncomputable def invSqrtTwo : ℝ
```

**`suTensor.invSqrtTwo_sq_add`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L235).

```lean
lemma invSqrtTwo_sq_add : invSqrtTwo ^ 2 + invSqrtTwo ^ 2 = 1
```

**`suTensor.invSqrtTwo_mul_self`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L239).

```lean
lemma invSqrtTwo_mul_self : (invSqrtTwo : ℂ) * invSqrtTwo = 1 / 2
```

**`suTensor.adjRep_eighthTurn_offDiag`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L246).

> The eighth turn in the plane of `p` and `q` sends the sum of the matrix units at `(p, q)`
> and at `(q, p)` to minus the difference of the diagonal matrix units at `p` and at `q`.

```lean
lemma adjRep_eighthTurn_offDiag {p q : Fin N} (hpq : p ≠ q) :
    adjRep N (planeEmbed p q hpq (rotation invSqrtTwo invSqrtTwo invSqrtTwo_sq_add))
      (offDiag p q + offDiag q p) = -diagDiff p q
```

**`suTensor.map_diagDiff_eq_smul`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L269).

> For two distinct coordinates `p` and `q`, an endomorphism commuting with the adjoint action
> scales the difference of the diagonal matrix units at `p` and at `q` by the coefficient of the
> matrix unit at `(p, q)`.

```lean
lemma map_diagDiff_eq_smul (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) {p q : Fin N} (hpq : p ≠ q) :
    L (diagDiff p q) = adjMat N (L (offDiag p q)) p q • diagDiff p q
```

**`suTensor.coeff_offDiag_eq`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L282).

> For three distinct coordinates `p`, `q` and `r`, the coefficients of the matrix units at
> `(p, q)` and at `(p, r)` agree. The difference of the diagonal units at `p` and `r` is the sum
> of those at `p` and `q` and at `q` and `r`.

```lean
lemma coeff_offDiag_eq (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) {p q r : Fin N} (hpq : p ≠ q) (hpr : p ≠ r)
    (hqr : q ≠ r) : adjMat N (L (offDiag p r)) p r = adjMat N (L (offDiag p q)) p q
```

**`suTensor.exists_coeff_offDiag_eq`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L295).

> All the matrix units off the diagonal have the same coefficient under an endomorphism
> commuting with the adjoint action.

```lean
lemma exists_coeff_offDiag_eq (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) :
    ∃ μ : ℂ, ∀ x y : Fin N, x ≠ y → adjMat N (L (offDiag x y)) x y = μ
```

**`suTensor.eq_sum_offDiag_add_sum_diagDiff`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L324).

> An element of the complexified Lie algebra is the combination of the entries of its matrix off
> the diagonal against the matrix units, and of its diagonal entries against the differences of
> the diagonal matrix units at a fixed coordinate.

```lean
lemma eq_sum_offDiag_add_sum_diagDiff (A : SUAlgebraComplexified N) (x₀ : Fin N) :
    A = ∑ x, ∑ y, adjMat N A x y • offDiag x y + ∑ x, adjMat N A x x • diagDiff x x₀
```

**`suTensor.eq_smul_id_of_commute_adjRep`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L359).

> An endomorphism of the complexified Lie algebra commuting with the adjoint action of every
> element of `SU(N)` is scalar, a form of Schur's lemma for the adjoint representation.

```lean
lemma eq_smul_id_of_commute_adjRep (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) :
    ∃ z : ℂ, L = z • LinearMap.id
```

## B. Reynolds elements for the tensors

> `SU(N)` is identified with the global gauge group `GlobalGaugeGroup.SU N`, a compact topological
> group, by `GlobalGaugeGroup.SU.groupEquiv`. On it the matrix entries of every color are continuous,
> being those of `g`, of `g⁻¹ = g†` and the traces `tr (λ_a g λ_b g⁻¹) / 2` of the adjoint action, so
> the Haar average gives a Reynolds element, which is pushed forward to `SU(N)`.

**`suTensor.continuous_toMatrix_rep`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L396).

> The matrix entries of every color depend continuously on the element of the global gauge group
> `SU(N)`.

```lean
lemma continuous_toMatrix_rep (k : Color) (x y : basisIdx N k) :
    Continuous fun h : (GlobalGaugeGroup.SU N).group => LinearMap.toMatrix (basis N k)
      (basis N k) (rep N k ((GlobalGaugeGroup.SU.groupEquiv N).symm h)) x y
```

**`suTensor.hasReynolds`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean#L423).

> The tensors of `SU(N)` with any list of colors have a Reynolds element, the Haar average over
> the compact group `SU(N)`.

```lean
lemma hasReynolds {n : ℕ} (c : Fin n → Color) : (suTensor N).HasReynolds c
```

## Depends on

- [The global gauge group SU(n)](../part-02/globalgaugegroup-su.md)
- [The complex tensor species of `SU(N)`](globalgaugegroup-su-tensorspecies.md)

## Proof depends on

- [Conditions for the reduction of invariants](../part-05/localfieldalgebra-realization-conditions.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Basic.lean)
