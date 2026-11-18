---
declaration: module
origin: cited
lean: Lorentz.Vector.minkowskiProductMap, Lorentz.Vector.minkowskiProductMap_toCoord, Lorentz.Vector.minkowskiProductMap_symm, Lorentz.Vector.minkowskiProductMap_add_fst, Lorentz.Vector.minkowskiProductMap_add_snd, Lorentz.Vector.minkowskiProductMap_smul_fst, Lorentz.Vector.minkowskiProductMap_smul_snd, Lorentz.Vector.minkowskiProduct
statement: formalized
proof: formalized
---

# Minkowski product on Lorentz vectors

The module `Physlib.Relativity.Tensors.RealTensor.Vector.MinkowskiProduct`, [Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean): 32 declarations, 8 with a docstring.

> In this module we define and create an API around the Minkowski product on Lorentz vectors.

## The minkowskiProduct

**`Lorentz.Vector.minkowskiProductMap`**, a def, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L40).

> The Minkowski product of Lorentz vectors in the +--- convention..

```lean
def minkowskiProductMap {d : ℕ} (p q : Vector d) : ℝ
```

**`Lorentz.Vector.minkowskiProductMap_toCoord`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L43).

```lean
lemma minkowskiProductMap_toCoord {d : ℕ} (p q : Vector d) :
    minkowskiProductMap p q = p (Sum.inl 0) * q (Sum.inl 0) -
    ∑ i, p (Sum.inr i) * q (Sum.inr i)
```

**`Lorentz.Vector.minkowskiProductMap_symm`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L66).

```lean
lemma minkowskiProductMap_symm {d : ℕ} (p q : Vector d) :
    minkowskiProductMap p q = minkowskiProductMap q p
```

**`Lorentz.Vector.minkowskiProductMap_add_fst`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L71).

```lean
lemma minkowskiProductMap_add_fst {d : ℕ} (p q r : Vector d) :
    minkowskiProductMap (p + q) r = minkowskiProductMap p r + minkowskiProductMap q r
```

**`Lorentz.Vector.minkowskiProductMap_add_snd`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L77).

```lean
lemma minkowskiProductMap_add_snd {d : ℕ} (p q r : Vector d) :
    minkowskiProductMap p (q + r) = minkowskiProductMap p q + minkowskiProductMap p r
```

**`Lorentz.Vector.minkowskiProductMap_smul_fst`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L83).

```lean
lemma minkowskiProductMap_smul_fst {d : ℕ} (c : ℝ) (p q : Vector d) :
    minkowskiProductMap (c • p) q = c * minkowskiProductMap p q
```

**`Lorentz.Vector.minkowskiProductMap_smul_snd`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L88).

```lean
lemma minkowskiProductMap_smul_snd {d : ℕ} (c : ℝ) (p q : Vector d) :
    minkowskiProductMap p (c • q) = c * minkowskiProductMap p q
```

**`Lorentz.Vector.minkowskiProduct`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L93).

> The Minkowski product of two Lorentz vectors as a linear map.

```lean
def minkowskiProduct {d : ℕ} : Vector d →L[ℝ] Vector d →L[ℝ] ℝ
```

**`Lorentz.Vector.minkowskiProduct_apply`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L126).

```lean
lemma minkowskiProduct_apply {d : ℕ} (p q : Vector d) :
    ⟪p, q⟫ₘ = minkowskiProductMap p q
```

**`Lorentz.Vector.minkowskiProduct_symm`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L129).

```lean
lemma minkowskiProduct_symm {d : ℕ} (p q : Vector d) :
    ⟪p, q⟫ₘ = ⟪q, p⟫ₘ
```

**`Lorentz.Vector.minkowskiProduct_toCoord`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L134).

```lean
lemma minkowskiProduct_toCoord {d : ℕ} (p q : Vector d) :
    ⟪p, q⟫ₘ = p (Sum.inl 0) * q (Sum.inl 0) - ∑ i, p (Sum.inr i) * q (Sum.inr i)
```

**`Lorentz.Vector.minkowskiProduct_toCoord_minkowskiMatrix`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L138).

```lean
lemma minkowskiProduct_toCoord_minkowskiMatrix {d : ℕ} (p q : Vector d) :
    ⟪p, q⟫ₘ = ∑ μ, minkowskiMatrix μ μ * p μ * q μ
```

**`Lorentz.Vector.minkowskiProduct_invariant`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L147).

```lean
lemma minkowskiProduct_invariant {d : ℕ} (p q : Vector d) (Λ : LorentzGroup d) :
    ⟪Λ • p, Λ • q⟫ₘ = ⟪p, q⟫ₘ
```

**`Lorentz.Vector.minkowskiProduct_eq_timeComponent_spatialPart`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L156).

```lean
lemma minkowskiProduct_eq_timeComponent_spatialPart {d : ℕ} (p q : Vector d) :
    ⟪p, q⟫ₘ = p.timeComponent * q.timeComponent -
      ⟪p.spatialPart, q.spatialPart⟫_ℝ
```

**`Lorentz.Vector.minkowskiProduct_self_eq_timeComponent_spatialPart`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L162).

```lean
lemma minkowskiProduct_self_eq_timeComponent_spatialPart {d : ℕ} (p : Vector d) :
    ⟪p, p⟫ₘ = ‖p.timeComponent‖ ^ 2 - ‖p.spatialPart‖ ^ 2
```

**`Lorentz.Vector.minkowskiProduct_self_le_timeComponent_sq`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L170).

```lean
lemma minkowskiProduct_self_le_timeComponent_sq {d : ℕ} (p : Vector d) :
    ⟪p, p⟫ₘ ≤ p.timeComponent ^ 2
```

**`Lorentz.Vector.minkowskiProduct_self_eq_sq_sub`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L176).

> `⟪u, u⟫ₘ = (u⁰)² - ‖u_spatial‖²`.

```lean
lemma minkowskiProduct_self_eq_sq_sub {d : ℕ} (u : Vector d) :
    ⟪u, u⟫ₘ = u.timeComponent ^ 2 - ‖u.spatialPart‖ ^ 2
```

**`Lorentz.Vector.minkowskiProduct_add_self`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L181).

> `⟪u + v, u + v⟫ₘ = ⟪u, u⟫ₘ + 2 ⟪u, v⟫ₘ + ⟪v, v⟫ₘ`.

```lean
lemma minkowskiProduct_add_self {d : ℕ} (u v : Vector d) :
    ⟪u + v, u + v⟫ₘ = ⟪u, u⟫ₘ + 2 * ⟪u, v⟫ₘ + ⟪v, v⟫ₘ
```

**`Lorentz.Vector.minkowskiProduct_smul_self`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L188).

> `⟪μ • u, μ • u⟫ₘ = μ² ⟪u, u⟫ₘ`.

```lean
lemma minkowskiProduct_smul_self {d : ℕ} (μ : ℝ) (u : Vector d) :
    ⟪μ • u, μ • u⟫ₘ = μ ^ 2 * ⟪u, u⟫ₘ
```

**`Lorentz.Vector.sqrt_minkowskiProduct_smul_self`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L194).

> `√⟪μ • u, μ • u⟫ₘ = μ √⟪u, u⟫ₘ` for `μ ≥ 0`.

```lean
lemma sqrt_minkowskiProduct_smul_self {d : ℕ} {μ : ℝ} (hμ : 0 ≤ μ) (u : Vector d) :
    √⟪μ • u, μ • u⟫ₘ = μ * √⟪u, u⟫ₘ
```

**`Lorentz.Vector.minkowskiProduct_basis_left`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L199).

```lean
lemma minkowskiProduct_basis_left {d : ℕ} (μ : Fin 1 ⊕ Fin d) (p : Vector d) :
    ⟪basis μ, p⟫ₘ = minkowskiMatrix μ μ * p μ
```

**`Lorentz.Vector.minkowskiProduct_basis_right`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L205).

```lean
lemma minkowskiProduct_basis_right {d : ℕ} (μ : Fin 1 ⊕ Fin d) (p : Vector d) :
    ⟪p, basis μ⟫ₘ = minkowskiMatrix μ μ * p μ
```

**`Lorentz.Vector.minkowskiProduct_eq_zero_forall_iff`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L210).

```lean
lemma minkowskiProduct_eq_zero_forall_iff {d : ℕ} (p : Vector d) :
    (∀ q : Vector d, ⟪p, q⟫ₘ = 0) ↔ p = 0
```

## The adjoint of a linear map

**`Lorentz.Vector.map_minkowskiProduct_eq_self_forall_iff`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L227).

```lean
lemma map_minkowskiProduct_eq_self_forall_iff {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) :
    (∀ p q : Vector d, ⟪f p, q⟫ₘ = ⟪p, q⟫ₘ) ↔ f = LinearMap.id
```

**`Lorentz.Vector.adjoint`**, a def, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L246).

> The adjoint of a linear map from `Vector d` to itself with respect to
> the `minkowskiProduct`.

```lean
def adjoint {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) : Vector d →ₗ[ℝ] Vector d
```

**`Lorentz.Vector.map_minkowskiProduct_eq_adjoint`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L251).

```lean
lemma map_minkowskiProduct_eq_adjoint {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) (p q : Vector d) :
    ⟪f p, q⟫ₘ = ⟪p, adjoint f q⟫ₘ
```

**`Lorentz.Vector.minkowskiProduct_map_eq_adjoint`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L263).

```lean
lemma minkowskiProduct_map_eq_adjoint {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) (p q : Vector d) :
    ⟪p, f q⟫ₘ = ⟪adjoint f p, q⟫ₘ
```

## The property `IsLorentz` of linear maps

**`Lorentz.Vector.IsLorentz`**, a def, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L276).

> A linear map `Vector d →ₗ[ℝ] Vector d` satisfies `IsLorentz` if it preserves
> the minkowski product.

```lean
def IsLorentz {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) :
    Prop
```

**`Lorentz.Vector.isLorentz_iff`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L279).

```lean
lemma isLorentz_iff {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) :
    IsLorentz f ↔ ∀ p q : Vector d, ⟪f p, f q⟫ₘ = ⟪p, q⟫ₘ
```

**`Lorentz.Vector.isLorentz_iff_basis`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L283).

```lean
lemma isLorentz_iff_basis {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) :
    IsLorentz f ↔ ∀ μ ν : Fin 1 ⊕ Fin d, ⟪f (basis μ), f (basis ν)⟫ₘ = ⟪basis μ, basis ν⟫ₘ
```

**`Lorentz.Vector.isLorentz_iff_comp_adjoint_eq_id`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L294).

```lean
lemma isLorentz_iff_comp_adjoint_eq_id {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) :
    IsLorentz f ↔ adjoint f ∘ₗ f = LinearMap.id
```

**`Lorentz.Vector.isLorentz_iff_toMatrix_mem_lorentzGroup`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean#L304).

```lean
lemma isLorentz_iff_toMatrix_mem_lorentzGroup {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) :
    IsLorentz f ↔ LinearMap.toMatrix Vector.basis Vector.basis f ∈ LorentzGroup d
```

## Depends on

- [Physlib.Relativity.Tensors.RealTensor.Metrics.Basic](realtensor-metrics-basic.md)
- [Tensorial nature of Lorentz vectors](../part-04/realtensor-vector-tensorial.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/MinkowskiProduct.lean)
