---
declaration: module
origin: cited
lean: Fermion.map_eq_smul_map_one_of_conj, Fermion.exists_eq_smul_one_of_conj, Fermion.DualLeftHandedWeyl.invariants_tprod_eq_span_unitVal, Fermion.LeftHandedWeyl.invariants_tprod_eq_span_unitVal, Fermion.DualRightHandedWeyl.invariants_tprod_eq_span_unitVal, Fermion.RightHandedWeyl.invariants_tprod_eq_span_unitVal
statement: formalized
proof: formalized
---

# The units are the unique invariants (Unit)

The module `PhyslibAlpha.Relativity.Fermions.Weyl.Unit`, [PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean): 6 declarations, 6 with a docstring.

> Up to scale, the unit `δ` is the only invariant of a Weyl representation tensored with its dual.

## i. Overview

> On `V ⊗ V*`, for `V` one of the four Weyl representations, `SL(2, ℂ)` acts on the matrix of
> components by conjugation, `X ↦ N X N⁻¹`. The two boosts along `z` combine to give the
> off-diagonal part of `X`, so an invariant has none, and conjugation by `ε` swaps the two diagonal
> entries (A). An invariant of `V ⊗ V*` therefore has a multiple of the identity matrix as
> components, which is the unit `δ` (B). For each of the four pairs this says that the invariants of
> `V ⊗ V*` are the line through `δ` (C).

## ii. Key results

> - `Fermion.DualLeftHandedWeyl.invariants_tprod_eq_span_unitVal` and its three siblings : the
>   invariants of `V ⊗ V*` are the line through the unit.

## iv. References

> The units are in `Physlib.Relativity.Fermions.Weyl.Unit`, where these results are written to move.
> The matrix of components `tensorToMatrix`, the elements `boostTwo`, `boostHalf` and `epsilon`,
> and the tactic `weyl_act` are in `PhyslibAlpha.Relativity.Fermions.Weyl.Metric`, alongside the
> analogous results for the metrics.

## A. Matrices

**`Fermion.map_eq_smul_map_one_of_conj`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean#L64).

> A linear map on matrices which is unchanged by the boosts `X ↦ D X D⁻¹`, on every matrix
> with the same image as `X`, and by `X ↦ ε X ε⁻¹` at `X`, sends `X` to a multiple of the image
> of the identity.

```lean
lemma map_eq_smul_map_one_of_conj (F : Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] B)
    {X : Matrix (Fin 2) (Fin 2) ℂ}
    (hD : ∀ Z, F Z = F X → F !![Z 0 0, 4 * Z 0 1; Z 1 0 / 4, Z 1 1] = F Z)
    (hD' : ∀ Z, F Z = F X → F !![Z 0 0, Z 0 1 / 4; 4 * Z 1 0, Z 1 1] = F Z)
    (hε : F !![X 1 1, -X 1 0; -X 0 1, X 0 0] = F X) :
    F X = ((X 0 0 + X 1 1) / 2) • F 1
```

## B. Tensor products

**`Fermion.exists_eq_smul_one_of_conj`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean#L102).

> When three elements of `SL(2,ℂ)` act on the components of `V ⊗ W` as two boosts and `ε`,
> every invariant of `V ⊗ W` is a multiple of the element with the identity as components.

```lean
lemma exists_eq_smul_one_of_conj {V W : Type*} [AddCommGroup V] [Module ℂ V]
    [AddCommGroup W] [Module ℂ W] (b : Module.Basis (Fin 2) ℂ V) (c : Module.Basis (Fin 2) ℂ W)
    {ρV : Representation ℂ SL(2,ℂ) V} {ρW : Representation ℂ SL(2,ℂ) W} {v : V ⊗[ℂ] W}
    (hv : v ∈ (ρV.tprod ρW).invariants)
    (hD : ∃ g, ∀ X, LinearMap.toMatrix b b (ρV g) * X * (LinearMap.toMatrix c c (ρW g))ᵀ =
      !![X 0 0, 4 * X 0 1; X 1 0 / 4, X 1 1])
    (hD' : ∃ g, ∀ X, LinearMap.toMatrix b b (ρV g) * X * (LinearMap.toMatrix c c (ρW g))ᵀ =
      !![X 0 0, X 0 1 / 4; 4 * X 1 0, X 1 1])
    (hε : ∃ g, ∀ X, LinearMap.toMatrix b b (ρV g) * X * (LinearMap.toMatrix c c (ρW g))ᵀ =
      !![X 1 1, -X 1 0; -X 0 1, X 0 0]) :
    ∃ z : ℂ, v = z • (tensorToMatrix b c).symm 1
```

## C. The four pairs

> For each pair `V ⊗ V*` the statement is in the namespace that holds its unit, as in
> `DualLeftHandedWeyl.unitVal : LeftHandedWeyl ⊗ DualLeftHandedWeyl`.

**`Fermion.DualLeftHandedWeyl.invariants_tprod_eq_span_unitVal`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean#L145).

> The `SL(2,ℂ)`-invariants of `LeftHandedWeyl ⊗ DualLeftHandedWeyl` are the line through the unit
> `δᵃₐ`.

```lean
lemma DualLeftHandedWeyl.invariants_tprod_eq_span_unitVal :
    (LeftHandedWeyl.rep.tprod DualLeftHandedWeyl.rep).invariants = ℂ ∙ unitVal
```

**`Fermion.LeftHandedWeyl.invariants_tprod_eq_span_unitVal`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean#L155).

> The `SL(2,ℂ)`-invariants of `DualLeftHandedWeyl ⊗ LeftHandedWeyl` are the line through the unit
> `δₐᵃ`.

```lean
lemma LeftHandedWeyl.invariants_tprod_eq_span_unitVal :
    (DualLeftHandedWeyl.rep.tprod LeftHandedWeyl.rep).invariants = ℂ ∙ unitVal
```

**`Fermion.DualRightHandedWeyl.invariants_tprod_eq_span_unitVal`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean#L165).

> The `SL(2,ℂ)`-invariants of `RightHandedWeyl ⊗ DualRightHandedWeyl` are the line through the
> unit `δ^{ȧ}_{ȧ}`.

```lean
lemma DualRightHandedWeyl.invariants_tprod_eq_span_unitVal :
    (RightHandedWeyl.rep.tprod DualRightHandedWeyl.rep).invariants = ℂ ∙ unitVal
```

**`Fermion.RightHandedWeyl.invariants_tprod_eq_span_unitVal`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean#L175).

> The `SL(2,ℂ)`-invariants of `DualRightHandedWeyl ⊗ RightHandedWeyl` are the line through the
> unit `δ_{ȧ}^{ȧ}`.

```lean
lemma RightHandedWeyl.invariants_tprod_eq_span_unitVal :
    (DualRightHandedWeyl.rep.tprod RightHandedWeyl.rep).invariants = ℂ ∙ unitVal
```

## Depends on

- [Invariants of two Weyl indices](weyl-metric.md)

## Sources

- [PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/Unit.lean)
