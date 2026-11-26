---
declaration: module
origin: cited
lean: Fermion.LeftHandedWeyl.metricVal_rep, Lorentz.SL2C.epsilon, Lorentz.SL2C.epsilon_coe, Lorentz.SL2C.epsilon_coe_metricRaw, Lorentz.SL2C.epsilon_mul_inv, Lorentz.SL2C.transpose_mul_epsilon_mul, Lorentz.SL2C.sum_epsilon_mul_inv_transpose, Lorentz.SL2C.sum_epsilon_mul_inv_conjTranspose
statement: formalized
proof: formalized
---

# Invariants of two Weyl indices

The module `PhyslibAlpha.Relativity.Fermions.Weyl.Metric`, [PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean): 28 declarations, 28 with a docstring.

> The invariants of two Weyl indices are the metric `ε` or zero, and `ε` lies in `SL(2, ℂ)`.

## i. Overview

> The Weyl metric `Fermion.metricRaw = !![0, 1; -1, 0]` has determinant one, so it is itself an
> element of `SL(2, ℂ)`, written `Lorentz.SL2C.epsilon`. In that form it is the invariant symplectic
> form, `gᵀ ε g = ε`. Contracting spinor indices needs the single-index version of that invariance. A
> factor of `(g⁻¹)ᵀ`, or of `(g⁻¹)ᴴ`, moved across `ε` becomes a factor of `g`, or of its entrywise
> conjugate, on the other slot. Those are `metricRaw_comm` and `metricRaw_comm_star` at `g⁻¹`, read
> entrywise. Alongside this, `LeftHandedWeyl.metricVal_rep` states the invariance of `εᵃᵃ` as the
> plain equation on the tensor product, rather than through the intertwining property of
> `LeftHandedWeyl.metric`.
>
> Conversely, `ε` is the only invariant: the invariants of the tensor square of a Weyl
> representation are the line through `ε`.
>
> On the matrix of components `SL(2, ℂ)` acts by `X ↦ M X Mᵀ`, up to reparametrising the group (C).
> The argument runs on matrices, for a linear map `F` with `F (M Y Mᵀ) = ρ M (F Y)` and `F X`
> invariant, and shows that `F X` is a multiple of `F ε` (D). Each of the four tensor squares
> reduces to it, with `F` the inverse of the matrix of components (E).
>
> The other tensor products of two Weyl representations are handled through a uniform matrix of
> components (F). The four `V ⊗ V*` have the unit `δ` as their only invariant, and are in
> `PhyslibAlpha.Relativity.Fermions.Weyl.Unit`. A left-handed and a right-handed index have no
> invariants at all, which is `complexLorentzTensor.invariants_upL_upR_eq_bot` in
> `PhyslibAlpha.Relativity.Bispinors.ComplexifiedAction`. A product of an undotted and a dotted
> one-index Weyl family is an equivariant map out of the tensors with a dual left- and a dual
> right-handed index (G). The tensor-level form of the uniqueness of the metric is with the metric
> tensors, in `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Metrics.Basic`.
>
> The results are named after the statement. On a tensor square `X ⊗ X` it is
> `X.invariants_tprod_eq_span_metricVal`. The other forms of these
> statements, for invariant elements, for the invariants in the range of an intertwining map and for
> intertwining maps out of the trivial representation, follow from them by the lemmas of
> `PhyslibAlpha.Mathematics.RepresentationTheory.Invariants`.

## ii. Key results

> - `Fermion.LeftHandedWeyl.metricVal_rep` : `εᵃᵃ` is invariant under `SL(2, ℂ)`.
> - `Lorentz.SL2C.epsilon` : the Weyl metric as an element of `SL(2, ℂ)`.
> - `Lorentz.SL2C.transpose_mul_epsilon_mul` : `ε` is the invariant symplectic form.
> - `Lorentz.SL2C.sum_epsilon_mul_inv_transpose`,
>   `Lorentz.SL2C.sum_epsilon_mul_inv_conjTranspose` : the single-index forms.
> - `Fermion.map_eq_smul_map_metricRaw_of_invariant` : on matrices, an invariant image of `X` is a
>   multiple of the image of `ε`.
> - `Fermion.LeftHandedWeyl.invariants_tprod_eq_span_metricVal` and its three siblings : the
>   invariants of the tensor square are the line through the metric.
> - `Fermion.tensorToMatrix_map` : on the matrix of components of `V ⊗ W` a pair of linear maps acts
>   by `X ↦ A X Bᵀ`.
> - `Lorentz.isEquivariant_downLDownR_mul` : an undotted family times a dotted one is an
>   equivariant map out of `ℂT[.downL, .downR]`.

## iv. References

> The Weyl metrics and `Fermion.metricRaw` are in `Physlib.Relativity.Fermions.Weyl.Metric`, and
> sections C to F are written to move there, with `tensorToMatrix` beside the matrix equivalences
> of `Physlib.Relativity.Fermions.Weyl.Two` and the elements of F.2 in `Physlib.Relativity.SL2C`.
> …

## A. Invariance of the left metric

**`Fermion.LeftHandedWeyl.metricVal_rep`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L110).

> The metric `εᵃᵃ` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma LeftHandedWeyl.metricVal_rep (M : SL(2,ℂ)) :
    TensorProduct.map (LeftHandedWeyl.rep M) (LeftHandedWeyl.rep M) LeftHandedWeyl.metricVal =
      LeftHandedWeyl.metricVal
```

## B. The symplectic form as an element of `SL(2, ℂ)`

> `ε = metricRaw` has determinant one, so it lies in `SL(2,ℂ)`, and `gᵀ ε g = ε` for every `g`
> there. The single-index identities move a factor of `(g⁻¹)ᵀ` or `(g⁻¹)ᴴ` across `ε`, where it
> becomes a factor of `g` or of its conjugate on the other slot: they are `metricRaw_comm` and
> `metricRaw_comm_star` at `g⁻¹`, read entrywise.

**`Lorentz.SL2C.epsilon`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L137).

> The antisymmetric symplectic form `ε = !![0, 1; -1, 0]`, the Weyl metric
> `Fermion.metricRaw`, as an element of `SL(2,ℂ)`.

```lean
def epsilon : SL(2,ℂ)
```

**`Lorentz.SL2C.epsilon_coe`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L141).

> The matrix underlying `epsilon`.

```lean
lemma epsilon_coe : (epsilon : Matrix (Fin 2) (Fin 2) ℂ) = !![0, 1; -1, 0]
```

**`Lorentz.SL2C.epsilon_coe_metricRaw`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L144).

> The matrix underlying `epsilon` is the Weyl metric `Fermion.metricRaw`.

```lean
lemma epsilon_coe_metricRaw : (epsilon : Matrix (Fin 2) (Fin 2) ℂ) = Fermion.metricRaw
```

**`Lorentz.SL2C.epsilon_mul_inv`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L147).

> `ε g⁻¹ = gᵀ ε`, `Fermion.metricRaw_comm` at `g⁻¹`.

```lean
lemma epsilon_mul_inv (g : SL(2,ℂ)) : epsilon.1 * g.1⁻¹ = g.1ᵀ * epsilon.1
```

**`Lorentz.SL2C.transpose_mul_epsilon_mul`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L153).

> `ε` is the invariant symplectic form of `SL(2,ℂ)`, `gᵀ ε g = ε`.

```lean
lemma transpose_mul_epsilon_mul (g : SL(2,ℂ)) : g.1ᵀ * epsilon.1 * g.1 = epsilon.1
```

**`Lorentz.SL2C.sum_epsilon_mul_inv_transpose`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L158).

> Single-index form. A factor of `(g⁻¹)ᵀ` moved across `ε` becomes a factor of `g` on the
> other slot.

```lean
lemma sum_epsilon_mul_inv_transpose (g : SL(2,ℂ)) (l a : Fin 2) :
    ∑ k : Fin 2, epsilon.1 l k * (g.1⁻¹)ᵀ a k = ∑ b : Fin 2, g.1 b l * epsilon.1 b a
```

**`Lorentz.SL2C.sum_epsilon_mul_inv_conjTranspose`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L165).

> The conjugate single-index form. A factor of `(g⁻¹)ᴴ` moved across `ε` becomes a factor of
> the conjugate of `g` on the other slot.

```lean
lemma sum_epsilon_mul_inv_conjTranspose (g : SL(2,ℂ)) (l a : Fin 2) :
    ∑ k : Fin 2, epsilon.1 l k * (g.1⁻¹)ᴴ a k
      = ∑ b : Fin 2, star (g.1 b l) * epsilon.1 b a
```

## C. Reparametrising the group

> On two undotted indices `SL(2,ℂ)` acts on the matrix of components by `X ↦ M X Mᵀ`, and `ε` is
> fixed by it. On the other three Weyl representations the group acts through `(M⁻¹)ᵀ`, the
> conjugate of `M`, or `(M⁻¹)ᴴ`, and each of these runs over all of `SL(2,ℂ)` as `M` does.

**`Fermion.inv_coe_transpose_inv`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L193).

> The element of `SL(2,ℂ)` whose matrix `(M⁻¹)ᵀ` is the given `N`.

```lean
lemma inv_coe_transpose_inv (N : SL(2,ℂ)) : (N.transpose⁻¹ : SL(2,ℂ)).1⁻¹ = N.1ᵀ
```

**`Fermion.map_star_coe_map_starRingEnd`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L197).

> The element of `SL(2,ℂ)` whose conjugate matrix is the given `N`.

```lean
lemma map_star_coe_map_starRingEnd (N : SL(2,ℂ)) :
    (SpecialLinearGroup.map (starRingEnd ℂ) N).1.map star = N.1
```

**`Fermion.conjTranspose_inv_coe_transpose_inv_map`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L203).

> The element of `SL(2,ℂ)` whose matrix `(M⁻¹)ᴴ` is the given `N`.

```lean
lemma conjTranspose_inv_coe_transpose_inv_map (N : SL(2,ℂ)) :
    ((SpecialLinearGroup.map (starRingEnd ℂ) N).transpose⁻¹ : SL(2,ℂ)).1⁻¹ᴴ = N.1
```

**`Fermion.mul_metricRaw_mul_transpose`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L210).

> The Weyl metric is fixed by the action `X ↦ M X Mᵀ` of `SL(2,ℂ)` on two undotted indices.

```lean
lemma mul_metricRaw_mul_transpose (M : SL(2,ℂ)) : M.1 * metricRaw * M.1ᵀ = metricRaw
```

## D. Matrices with an invariant image

> The argument runs on the matrix of components, through a linear map `F` with
> `F (M Y Mᵀ) = ρ M (F Y)`, and with `F Y` invariant. Here `ρ` is any family of linear maps, so
> that it can be a representation composed with one of the reparametrisations of C. The boosts
> `diag (2, 2⁻¹)` and `diag (2⁻¹, 2)` combine to give the diagonal part of `Y`, so `F` kills it
> (D.1). The element `!![1, -1; 1, 0]` sends the symmetric off-diagonal matrix `O` to minus itself
> plus a diagonal matrix, so `F O` is its own negative and vanishes (D.2). What is left of `Y` is
> its antisymmetric part, a multiple of `ε` (D.3).

### D.1. The diagonal part

**`Fermion.diagonal_eq_smul_boost_sub`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L241).

> The diagonal part of a `2 × 2` matrix as a combination of its images under the boosts
> `diag (2, 2⁻¹)` and `diag (2⁻¹, 2)`, with coefficients summing to zero.

```lean
lemma diagonal_eq_smul_boost_sub (Y : Matrix (Fin 2) (Fin 2) ℂ) :
    !![Y 0 0, 0; 0, Y 1 1] = (4 / 9 : ℂ) • (!![2, 0; 0, 2⁻¹] * Y * !![2, 0; 0, 2⁻¹]ᵀ +
      !![2⁻¹, 0; 0, 2] * Y * !![2⁻¹, 0; 0, 2]ᵀ - (2 : ℂ) • Y)
```

**`Fermion.map_diagonal_eq_zero_of_invariant`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L249).

> An equivariant map with `F Y` invariant vanishes on the diagonal part of `Y`.

```lean
lemma map_diagonal_eq_zero_of_invariant (hF : ∀ (M : SL(2,ℂ)) Y, F (M.1 * Y * M.1ᵀ) = ρ M (F Y))
    {Y : Matrix (Fin 2) (Fin 2) ℂ} (hY : ∀ g, ρ g (F Y) = F Y) :
    F !![Y 0 0, 0; 0, Y 1 1] = 0
```

### D.2. The symmetric off-diagonal part

**`Fermion.map_offDiagonal_eq_zero_of_invariant`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L266).

> An equivariant map with `F !![0, c; c, 0]` invariant vanishes on `!![0, c; c, 0]`.

```lean
lemma map_offDiagonal_eq_zero_of_invariant
    (hF : ∀ (M : SL(2,ℂ)) Y, F (M.1 * Y * M.1ᵀ) = ρ M (F Y)) {c : ℂ}
    (hc : ∀ g, ρ g (F !![0, c; c, 0]) = F !![0, c; c, 0]) : F !![0, c; c, 0] = 0
```

### D.3. The antisymmetric part

**`Fermion.map_eq_smul_map_metricRaw_of_invariant`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L293).

> An equivariant map with `F X` invariant sends `X` to a multiple of the image of the Weyl
> metric.

```lean
lemma map_eq_smul_map_metricRaw_of_invariant
    (hF : ∀ (M : SL(2,ℂ)) Y, F (M.1 * Y * M.1ᵀ) = ρ M (F Y)) {X : Matrix (Fin 2) (Fin 2) ℂ}
    (hX : ∀ g, ρ g (F X) = F X) : F X = ((X 0 1 - X 1 0) / 2) • F metricRaw
```

## E. The metrics are the unique invariants

> On the matrix of components `SL(2,ℂ)` acts by `X ↦ N X Nᵀ`, where `N` is `M`, `(M⁻¹)ᵀ`, the
> conjugate of `M`, or `(M⁻¹)ᴴ`, and by section C section D applies to each, with `F` the inverse of
> the matrix of components. So the invariants of each tensor square are the line through its
> metric.

**`Fermion.LeftHandedWeyl.invariants_tprod_eq_span_metricVal`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L325).

> The `SL(2,ℂ)`-invariants of `LeftHandedWeyl ⊗ LeftHandedWeyl` are the line through the
> metric `εᵃᵃ`.

```lean
lemma LeftHandedWeyl.invariants_tprod_eq_span_metricVal :
    (rep.tprod rep).invariants = ℂ ∙ metricVal
```

**`Fermion.DualLeftHandedWeyl.invariants_tprod_eq_span_metricVal`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L341).

> The `SL(2,ℂ)`-invariants of `DualLeftHandedWeyl ⊗ DualLeftHandedWeyl` are the line through
> the metric `εₐₐ`.

```lean
lemma DualLeftHandedWeyl.invariants_tprod_eq_span_metricVal :
    (rep.tprod rep).invariants = ℂ ∙ metricVal
```

**`Fermion.RightHandedWeyl.invariants_tprod_eq_span_metricVal`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L359).

> The `SL(2,ℂ)`-invariants of `RightHandedWeyl ⊗ RightHandedWeyl` are the line through the
> metric `ε^{ȧȧ}`.

```lean
lemma RightHandedWeyl.invariants_tprod_eq_span_metricVal :
    (rep.tprod rep).invariants = ℂ ∙ metricVal
```

**`Fermion.DualRightHandedWeyl.invariants_tprod_eq_span_metricVal`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L377).

> The `SL(2,ℂ)`-invariants of `DualRightHandedWeyl ⊗ DualRightHandedWeyl` are the line through
> the metric `ε_{ȧȧ}`.

```lean
lemma DualRightHandedWeyl.invariants_tprod_eq_span_metricVal :
    (rep.tprod rep).invariants = ℂ ∙ metricVal
```

## F. Components of a tensor product of two Weyl representations

> The other twelve tensor products of two Weyl representations are handled uniformly through
> their matrix of components, `tensorToMatrix`, on which `SL(2,ℂ)` acts by `X ↦ K₁ X K₂ᵀ` with
> `Kᵢ` the matrices of the two factors (F.1). The arguments of
> `PhyslibAlpha.Relativity.Fermions.Weyl.Unit` only test this action against three elements of
> `SL(2,ℂ)`, the boosts `boostTwo` and `boostHalf` along `z`, and `epsilon` (F.2).

### F.1. The matrix of components

**`Fermion.tensorToMatrix`**, a def, [line 418](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L418).

> The matrix of components of an element of `V ⊗ W`, in a basis of `V` and a basis of `W`.

```lean
def tensorToMatrix : V ⊗[ℂ] W ≃ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.tensorToMatrix_tmul`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L423).

> The components of a pure tensor are the products of the components of its factors.

```lean
lemma tensorToMatrix_tmul (x : V) (y : W) (i j : Fin 2) :
    tensorToMatrix b c (x ⊗ₜ y) i j = b.repr x i * c.repr y j
```

**`Fermion.tensorToMatrix_map`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L429).

> A pair of linear maps acts on the matrix of components by `X ↦ A X Bᵀ`.

```lean
lemma tensorToMatrix_map (f : V →ₗ[ℂ] V) (g : W →ₗ[ℂ] W) (v : V ⊗[ℂ] W) :
    tensorToMatrix b c (TensorProduct.map f g v) =
      LinearMap.toMatrix b b f * tensorToMatrix b c v * (LinearMap.toMatrix c c g)ᵀ
```

**`Fermion.symm_act_eq`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L443).

> An element of `V ⊗ W` with invariant components `Y` is unchanged by an element of
> `SL(2,ℂ)` acting on the components.

```lean
lemma symm_act_eq {ρV : Representation ℂ SL(2,ℂ) V} {ρW : Representation ℂ SL(2,ℂ) W}
    {Y : Matrix (Fin 2) (Fin 2) ℂ} (hY : (tensorToMatrix b c).symm Y ∈ (ρV.tprod ρW).invariants)
    {Φ : Matrix (Fin 2) (Fin 2) ℂ → Matrix (Fin 2) (Fin 2) ℂ}
    (h : ∃ g, ∀ X, LinearMap.toMatrix b b (ρV g) * X * (LinearMap.toMatrix c c (ρW g))ᵀ = Φ X) :
    (tensorToMatrix b c).symm (Φ Y) = (tensorToMatrix b c).symm Y
```

### F.2. Three elements of `SL(2, ℂ)`

**`Lorentz.SL2C.boostTwo`**, a def, [line 463](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L463).

> The boost along `z` with matrix `diag (2, 2⁻¹)`.

```lean
def _root_.Lorentz.SL2C.boostTwo : SL(2,ℂ)
```

**`Lorentz.SL2C.boostHalf`**, a def, [line 466](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L466).

> The boost along `z` with matrix `diag (2⁻¹, 2)`, the inverse of `boostTwo`.

```lean
def _root_.Lorentz.SL2C.boostHalf : SL(2,ℂ)
```

## G. One-index Weyl families and their products

> A two-element family of elements of an algebra `B` can carry one dual Weyl index, undotted or
> dotted. Both laws are contragredient, and the dotted law carries the extra complex conjugation. A
> fermion field of the Standard Model with every index but its spinor index frozen is such a family.
> When the Lorentz action is multiplicative, an undotted family times a dotted one is an equivariant
> map out of `ℂT[.downL, .downR]`, in either order, the shape of a Dirac mass term `ψ̄ ψ`. That such
> a map carries no invariant is `Lorentz.reducesInvariantsTo_bot_leftRight`, in
> `PhyslibAlpha.Relativity.Bispinors.ComplexifiedAction`.

**`Lorentz.isEquivariant_downLDownR_mul`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L516).

> A family `X` with a dual undotted spinor index, moved by the contragredient of the
> left-handed Weyl representation, times a family `Y` with a dual dotted spinor index, moved by
> its conjugate, is an equivariant map out of `ℂT[.downL, .downR]`.

```lean
lemma isEquivariant_downLDownR_mul {X Y : Fin 2 → B}
    (hX : ∀ (Λ : SL(2,ℂ)) (a : Fin 2), repLorentz Λ (X a) = ∑ β, (Λ⁻¹).1 a β • X β)
    (hY : ∀ (Λ : SL(2,ℂ)) (a : Fin 2), repLorentz Λ (Y a) = ∑ β, star ((Λ⁻¹).1 a β) • Y β) :
    complexLorentzTensor.IsEquivariant ![.downL, .downR] repLorentz
      (liftComponents ((fun p => X p.1 * Y p.2) ∘ pairIdx))
```

**`Lorentz.isEquivariant_downLDownR_mul_swap`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L532).

> A dotted family times an undotted one is an equivariant map out of `ℂT[.downL, .downR]`, the
> two spinor slots exchanged.

```lean
lemma isEquivariant_downLDownR_mul_swap {X Y : Fin 2 → B}
    (hX : ∀ (Λ : SL(2,ℂ)) (a : Fin 2), repLorentz Λ (X a) = ∑ β, star ((Λ⁻¹).1 a β) • X β)
    (hY : ∀ (Λ : SL(2,ℂ)) (a : Fin 2), repLorentz Λ (Y a) = ∑ β, (Λ⁻¹).1 a β • Y β) :
    complexLorentzTensor.IsEquivariant ![.downL, .downR] repLorentz
      (liftComponents ((fun p => X p.2 * Y p.1) ∘ pairIdx))
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [Equivariant maps out of the tensors of a species](../tensors/equivariant.md)

## Proof depends on

- [Reynolds elements for complex Lorentz tensors](../lorentzgroup/invariants-reynolds.md)

## Sources

- [PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean)
