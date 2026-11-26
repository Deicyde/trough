---
declaration: module
origin: cited
lean: LorentzGroup.minkowskiMatrix_map_mul_self, LorentzGroup.minkowskiMatrix_map_mul_minkowskiMatrix_map_mul, LorentzGroup.transpose_minkowskiMatrix_map, LorentzGroup.inv_toComplex, LorentzGroup.minkowskiMatrix_map_mul_inv_toComplex, LorentzGroup.inv_toComplex_transpose_mul_minkowskiMatrix_map, LorentzGroup.inv_toComplex_transpose_mul_conj_minkowskiMatrix_map, Lorentz.toComplex_toLorentzGroup_halfTurn
statement: formalized
proof: formalized
---

# The metrics are the unique invariants

The module `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Metrics.Pre`, [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean): 23 declarations, 23 with a docstring.

> Up to scale, the Minkowski metric is the only invariant of two complex Lorentz vector indices.

## i. Overview

> On `ComplexVector ⊗ ComplexVector` the group `SL(2, ℂ)` acts on the matrix of components by
> `Y ↦ Λ Y Λᵀ`, with `Λ` the complexified Lorentz matrix. The complexified Minkowski matrix `η`
> squares to the identity and gives `Λ⁻¹ = η Λᵀ η` (A), so the other orderings of upper and lower
> indices reduce to this action after multiplying by `η`.
>
> Let `F` be a linear map out of the matrices which intertwines `Y ↦ Λ Y Λᵀ` with an action on `B`,
> and let `F X` be invariant (B). The three half turns act by diagonal sign matrices, and averaging
> over them keeps only the diagonal, so `F X` is the image of the diagonal of `X` (B.1). For a
> diagonal `D` the boost along the axis `i` changes only the time and `i` entries of the diagonal,
> by a multiple of `d_t + d_i`, so `(d_t + d_i) • F P_i = 0`, where `P_i` projects onto the plane
> of time and the axis `i` (B.2). The cyclic rotation of the axes carries `P_i` to `P_{i+1}`, so
> the three `F P_i` vanish together (B.3). If they vanish, `F D` and `F η` are both multiples of
> the image of the time projection, and otherwise `D` is a multiple of `η`. Either way `F X` is a
> multiple of `F η` (B.4).
>
> The result follows for any tensor product whose matrix of components carries this action (C).
> On two contravariant indices the invariants of the tensor product are the line through the metric
> (D). The same holds for two covariant indices, through the matrix of components conjugated by `η`
> (E).

## ii. Key results

> - `Lorentz.map_eq_smul_map_minkowskiMatrix_of_invariant` : on matrices with the action
>   `Y ↦ Λ Y Λᵀ`, an invariant in the image of an equivariant map is a multiple of the image of `η`.
> - `Lorentz.ComplexVector.invariants_tprod_eq_span_metricVal` : the invariants of
>   `ComplexVector ⊗ ComplexVector` are the line through the metric.
> - `Lorentz.ComplexCoVector.invariants_tprod_eq_span_metricVal` : the same for
>   `ComplexCoVector ⊗ ComplexCoVector`.

## iv. References

> …

## A. The complexified Minkowski matrix

**`LorentzGroup.minkowskiMatrix_map_mul_self`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L88).

> The complexified Minkowski matrix squares to the identity.

```lean
lemma minkowskiMatrix_map_mul_self :
    (@minkowskiMatrix d).map ofRealHom * (@minkowskiMatrix d).map ofRealHom = 1
```

**`LorentzGroup.minkowskiMatrix_map_mul_minkowskiMatrix_map_mul`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L93).

> Multiplying twice by the complexified Minkowski matrix is the identity.

```lean
lemma minkowskiMatrix_map_mul_minkowskiMatrix_map_mul
    (X : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℂ) :
    (@minkowskiMatrix d).map ofRealHom * ((@minkowskiMatrix d).map ofRealHom * X) = X
```

**`LorentzGroup.transpose_minkowskiMatrix_map`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L99).

> The complexified Minkowski matrix is symmetric.

```lean
lemma transpose_minkowskiMatrix_map :
    ((@minkowskiMatrix d).map ofRealHom)ᵀ = (@minkowskiMatrix d).map ofRealHom
```

**`LorentzGroup.inv_toComplex`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L104).

> The inverse of a complexified Lorentz matrix is `η Λᵀ η`.

```lean
lemma inv_toComplex (Λ : LorentzGroup d) : (toComplex Λ)⁻¹ =
    minkowskiMatrix.map ofRealHom * (toComplex Λ)ᵀ * minkowskiMatrix.map ofRealHom
```

**`LorentzGroup.minkowskiMatrix_map_mul_inv_toComplex`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L112).

> Moving `Λ⁻¹` across `η` turns it into `Λᵀ`.

```lean
lemma minkowskiMatrix_map_mul_inv_toComplex (Λ : LorentzGroup d) :
    minkowskiMatrix.map ofRealHom * (toComplex Λ)⁻¹ =
      (toComplex Λ)ᵀ * minkowskiMatrix.map ofRealHom
```

**`LorentzGroup.inv_toComplex_transpose_mul_minkowskiMatrix_map`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L119).

> Moving `Λ⁻¹ᵀ` across `η` turns it into `Λ`.

```lean
lemma inv_toComplex_transpose_mul_minkowskiMatrix_map (Λ : LorentzGroup d) :
    (toComplex Λ)⁻¹ᵀ * minkowskiMatrix.map ofRealHom =
      minkowskiMatrix.map ofRealHom * toComplex Λ
```

**`LorentzGroup.inv_toComplex_transpose_mul_conj_minkowskiMatrix_map`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L128).

> Conjugating by `η` turns the action `X ↦ Λ⁻¹ᵀ X Λ⁻¹` on two covariant indices into the
> action `Y ↦ Λ Y Λᵀ` on two contravariant indices.

```lean
lemma inv_toComplex_transpose_mul_conj_minkowskiMatrix_map (Λ : LorentzGroup d)
    (Y : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℂ) :
    (toComplex Λ)⁻¹ᵀ * (minkowskiMatrix.map ofRealHom * Y * minkowskiMatrix.map ofRealHom) *
      (toComplex Λ)⁻¹ = minkowskiMatrix.map ofRealHom * (toComplex Λ * Y * (toComplex Λ)ᵀ) *
      minkowskiMatrix.map ofRealHom
```

## B. Invariants in the image of an equivariant map on matrices

> Throughout, `F` is a linear map out of the `4 × 4` complex matrices with
> `F (Λ Y Λᵀ) = ρ g (F Y)`, where `Λ` is the complexified Lorentz matrix of `g`.

### B.1. The diagonal part

**`Lorentz.toComplex_toLorentzGroup_halfTurn`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L165).

> The complexified Lorentz matrix of the half turn about the axis `k` is the diagonal matrix of
> the signs `halfTurnSign k`.

```lean
lemma toComplex_toLorentzGroup_halfTurn (k : Fin 3) :
    LorentzGroup.toComplex (SL2C.toLorentzGroup (SL2C.halfTurn k)) =
      diagonal fun μ => (halfTurnSign k μ : ℂ)
```

**`Lorentz.add_sum_halfTurnSign_conj`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L174).

> Adding a matrix to its conjugates by the three half turns keeps four times its diagonal.

```lean
lemma add_sum_halfTurnSign_conj (Y : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ) :
    Y + ∑ k, diagonal (fun μ => (halfTurnSign k μ : ℂ)) * Y *
      (diagonal fun μ => (halfTurnSign k μ : ℂ))ᵀ = (4 : ℂ) • diagonal fun μ => Y μ μ
```

**`Lorentz.map_eq_map_diagonal_of_invariant`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L184).

> When `F Y` is invariant, it is the image of the diagonal of `Y`.

```lean
lemma map_eq_map_diagonal_of_invariant
    (hF : ∀ g Y, F (LorentzGroup.toComplex (SL2C.toLorentzGroup g) * Y *
      (LorentzGroup.toComplex (SL2C.toLorentzGroup g))ᵀ) = ρ g (F Y))
    {Y : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ} (hY : ∀ g, ρ g (F Y) = F Y) :
    F Y = F (diagonal fun μ => Y μ μ)
```

### B.2. Boosts

**`Lorentz.timeAxisProj`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L207).

> The projection onto the plane of time and the axis `i`, the diagonal matrix with `1` in the
> time and `i` slots and `0` in the other two.

```lean
def timeAxisProj (i : Fin 3) : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ
```

**`Lorentz.diagonal_boost_conj_sub`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L212).

> The boost along the axis `i` with parameter `2` changes the diagonal of a diagonal matrix
> `diagonal d` only in the time and `i` slots, by `(225 / 64) (d_t + d_i)`.

```lean
lemma diagonal_boost_conj_sub (i : Fin 3) (d : Fin 1 ⊕ Fin 3 → ℂ) :
    (diagonal fun μ => (LorentzGroup.toComplex (SL2C.toLorentzGroup
      (SL2C.boostAxis i 2 two_ne_zero)) * diagonal d * (LorentzGroup.toComplex
      (SL2C.toLorentzGroup (SL2C.boostAxis i 2 two_ne_zero)))ᵀ) μ μ) - diagonal d =
      ((225 / 64 : ℂ) * (d (Sum.inl 0) + d (Sum.inr i))) • timeAxisProj i
```

**`Lorentz.add_smul_map_timeAxisProj_eq_zero`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L231).

> When `F (diagonal d)` is invariant, `d_t + d_i` kills the image of the projection onto the
> plane of time and the axis `i`.

```lean
lemma add_smul_map_timeAxisProj_eq_zero
    (hF : ∀ g Y, F (LorentzGroup.toComplex (SL2C.toLorentzGroup g) * Y *
      (LorentzGroup.toComplex (SL2C.toLorentzGroup g))ᵀ) = ρ g (F Y))
    {d : Fin 1 ⊕ Fin 3 → ℂ} (hd : ∀ g, ρ g (F (diagonal d)) = F (diagonal d)) (i : Fin 3) :
    (d (Sum.inl 0) + d (Sum.inr i)) • F (timeAxisProj i) = 0
```

### B.3. Cycling the axes

**`Lorentz.rotationCycle_conj_timeAxisProj`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L250).

> The cyclic rotation of the axes carries the projection onto the plane of time and the axis
> `i` to that of the axis `i + 1`.

```lean
lemma rotationCycle_conj_timeAxisProj (i : Fin 3) :
    LorentzGroup.toComplex (SL2C.toLorentzGroup SL2C.rotationCycle) * timeAxisProj i *
      (LorentzGroup.toComplex (SL2C.toLorentzGroup SL2C.rotationCycle))ᵀ =
      timeAxisProj (i + 1)
```

**`Lorentz.map_timeAxisProj_eq_zero_of_eq_zero`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L262).

> The images of the projections onto the three planes of time and an axis vanish together.

```lean
lemma map_timeAxisProj_eq_zero_of_eq_zero
    (hF : ∀ g Y, F (LorentzGroup.toComplex (SL2C.toLorentzGroup g) * Y *
      (LorentzGroup.toComplex (SL2C.toLorentzGroup g))ᵀ) = ρ g (F Y))
    {i : Fin 3} (h : F (timeAxisProj i) = 0) (j : Fin 3) : F (timeAxisProj j) = 0
```

### B.4. Invariants are multiples of the image of the metric

**`Lorentz.diagonal_eq_sum_timeAxisProj`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L280).

> A diagonal matrix in terms of the time projection and the projections onto the planes of
> time and an axis.

```lean
lemma diagonal_eq_sum_timeAxisProj (d : Fin 1 ⊕ Fin 3 → ℂ) :
    diagonal d = (d (Sum.inl 0) - ∑ i, d (Sum.inr i)) • diagonal (Pi.single (Sum.inl 0) 1) +
      ∑ i, d (Sum.inr i) • timeAxisProj i
```

**`Lorentz.minkowskiMatrix_map_eq_sum_timeAxisProj`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L289).

> The complexified Minkowski matrix in terms of the time projection and the projections onto
> the planes of time and an axis.

```lean
lemma minkowskiMatrix_map_eq_sum_timeAxisProj :
    minkowskiMatrix.map ofRealHom =
      (4 : ℂ) • diagonal (Pi.single (Sum.inl 0) 1) - ∑ i, timeAxisProj i
```

**`Lorentz.diagonal_eq_smul_minkowskiMatrix_map`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L297).

> A diagonal matrix with `d_t + d_i = 0` for each axis `i` is `d_t η`.

```lean
lemma diagonal_eq_smul_minkowskiMatrix_map {d : Fin 1 ⊕ Fin 3 → ℂ}
    (hd : ∀ i, d (Sum.inl 0) + d (Sum.inr i) = 0) :
    diagonal d = d (Sum.inl 0) • minkowskiMatrix.map ofRealHom
```

**`Lorentz.map_diagonal_eq_smul_of_invariant`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L307).

> When `F (diagonal d)` is invariant, it is a multiple of `F η`. If the images of the
> projections onto the planes of time and an axis vanish, both are multiples of the image of the
> time projection, and otherwise `diagonal d` is a multiple of `η`.

```lean
lemma map_diagonal_eq_smul_of_invariant
    (hF : ∀ g Y, F (LorentzGroup.toComplex (SL2C.toLorentzGroup g) * Y *
      (LorentzGroup.toComplex (SL2C.toLorentzGroup g))ᵀ) = ρ g (F Y))
    {d : Fin 1 ⊕ Fin 3 → ℂ} (hd : ∀ g, ρ g (F (diagonal d)) = F (diagonal d)) :
    ∃ c : ℂ, F (diagonal d) = c • F (minkowskiMatrix.map ofRealHom)
```

**`Lorentz.map_eq_smul_map_minkowskiMatrix_of_invariant`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L327).

> When `F X` is invariant, it is a multiple of the image `F η` of the complexified Minkowski
> matrix.

```lean
lemma map_eq_smul_map_minkowskiMatrix_of_invariant
    (hF : ∀ g Y, F (LorentzGroup.toComplex (SL2C.toLorentzGroup g) * Y *
      (LorentzGroup.toComplex (SL2C.toLorentzGroup g))ᵀ) = ρ g (F Y))
    {X : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ} (hX : ∀ g, ρ g (F X) = F X) :
    ∃ c : ℂ, F X = c • F (minkowskiMatrix.map ofRealHom)
```

## C. Tensor products with a matrix of components

**`Lorentz.invariants_eq_span_map_minkowskiMatrix`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L348).

> Let `T` be a linear map from the matrices onto `V` which intertwines `Y ↦ Λ Y Λᵀ` with the
> action on `V`. The invariants of `V` are the line through `T η`.

```lean
lemma invariants_eq_span_map_minkowskiMatrix {V : Type*} [AddCommGroup V]
    [Module ℂ V] {σ : Representation ℂ SL(2,ℂ) V}
    (T : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℂ →ₗ[ℂ] V) (hT : Function.Surjective T)
    (hσ : ∀ g Y, T (LorentzGroup.toComplex (SL2C.toLorentzGroup g) * Y *
      (LorentzGroup.toComplex (SL2C.toLorentzGroup g))ᵀ) = σ g (T Y)) :
    σ.invariants = ℂ ∙ T (minkowskiMatrix.map ofRealHom)
```

## D. Two contravariant indices

**`Lorentz.ComplexVector.invariants_tprod_eq_span_metricVal`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L366).

> Up to scale, the metric `ηᵃᵃ` is the unique invariant of `ComplexVector ⊗ ComplexVector`.

```lean
lemma ComplexVector.invariants_tprod_eq_span_metricVal :
    (ComplexVector.SL2CRep.tprod ComplexVector.SL2CRep).invariants =
      ℂ ∙ ComplexVector.metricVal
```

## E. Two covariant indices

**`Lorentz.ComplexCoVector.invariants_tprod_eq_span_metricVal`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L380).

> Up to scale, the metric `ηᵢᵢ` is the unique invariant of `ComplexCoVector ⊗ ComplexCoVector`.

```lean
lemma ComplexCoVector.invariants_tprod_eq_span_metricVal :
    (ComplexCoVector.SL2CRep.tprod ComplexCoVector.SL2CRep).invariants =
      ℂ ∙ ComplexCoVector.metricVal
```

## Depends on

- [Coordinate-axis boosts in `SL(2,ℂ)` and the Lorentz group](../../../physlib/relativity/lorentzgroup/boosts-axis.md)
- [Metric for complex Lorentz vectors](../../../physlib/relativity/tensors/part-01/complextensor-metrics-pre.md)
- [The cyclic rotation and the half turns](../sl2c/axisrotations.md)

## Proof depends on

- [Invariants and intertwining maps out of the trivial representation](../../mathematics/part-02/representationtheory/invariants.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean)
