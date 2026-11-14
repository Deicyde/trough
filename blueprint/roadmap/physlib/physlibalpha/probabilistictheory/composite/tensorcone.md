---
declaration: module
origin: cited
lean: ProbabilisticTheory.Composite, ProbabilisticTheory.Composite.tmul, PositiveLinearMap.rslice, PositiveLinearMap.lslice, PositiveLinearMap.rslice_tmul, PositiveLinearMap.lslice_tmul, PositiveLinearMap.tensor, PositiveLinearMap.tensor_tmul
statement: formalized
proof: formalized
---

# Composite systems

The module `PhyslibAlpha.ProbabilisticTheory.Composite.TensorCone`, [PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean): 49 declarations (1 instance with no name), 32 with a docstring.

> Composite systems: the minimal and maximal tensor cones, composites, and nuclear systems.

## i. Overview

> Two systems with observables `E` and `F` are combined into a composite system whose observables
> are the tensor products `E ⊗ F`. Which composite observables are nonnegative is not fixed by the
> parts; there are two extreme choices.
>
> The minimal cone contains only the sums of products `x ⊗ y` of nonnegative observables: nonnegative
> local observations. The maximal cone contains every composite observable that no pair of local
> preparations `φ ⊗ ψ` can assign a negative value. A composite of `E` and `F` is any choice of
> nonnegative composite observables in between. Tensor products of positive maps preserve both
> extreme cones.
>
> A system is nuclear when, for every other system, the maximal cone lies in the closure of the
> minimal cone: its composites are unique.

## ii. Key results

> - `Composite E F` : the observables of the composite system.
> - `PositiveLinearMap.tensor` : the product functional `φ ⊗ ψ`.
> - `minTensorCone E F`, `maxTensorCone E F` : the minimal and the maximal cone.
> - `mem_maxTensorCone` : the maximal cone consists of the composite observables that every product
>   functional keeps nonnegative.
> - `minTensorCone_map_le`, `maxTensorCone_map_le` : tensor products of positive maps preserve the
>   minimal and the maximal cone.
> - `CompositeCone E F` : a composite of `E` and `F`.
> - `isDominatedCone_minTensorCone` : every composite observable plus a large multiple of `1 ⊗ 1` lies
>   in the minimal cone.
> - `minTensorClosure E F` : the Archimedean closure of the minimal cone.
> - `IsNuclear E` : composition with every Archimedean system is unique, up to closure.
> - `mem_maxTensorCone_iff_rslice` : for Archimedean `E`, the maximal cone consists of the composite
>   observables that stay nonnegative when a positive functional is applied to the second factor.

## iv. References

> * None.

**`ProbabilisticTheory.Composite`**, an abbrev, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L74).

> The observables of the composite of two systems: the tensor products `E ⊗ F`.

```lean
abbrev Composite : Type _
```

**`ProbabilisticTheory.Composite.tmul`**, an abbrev, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L77).

> The product `x ⊗ y` of observables of the two parts, as a composite observable.

```lean
abbrev Composite.tmul (x : E) (y : F) : Composite E F
```

## A. Slices and product functionals

**`PositiveLinearMap.rslice`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L90).

> Apply a positive functional to the second factor.

```lean
noncomputable def rslice (ψ : F →ₚ[ℝ] ℝ) : E ⊗[ℝ] F →ₗ[ℝ] E
```

**`PositiveLinearMap.lslice`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L94).

> Apply a positive functional to the first factor.

```lean
noncomputable def lslice (φ : E →ₚ[ℝ] ℝ) : E ⊗[ℝ] F →ₗ[ℝ] F
```

**`PositiveLinearMap.rslice_tmul`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L98).

```lean
lemma rslice_tmul (ψ : F →ₚ[ℝ] ℝ) (x : E) (y : F) : rslice ψ (x ⊗ₜ[ℝ] y) = ψ y • x
```

**`PositiveLinearMap.lslice_tmul`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L102).

```lean
lemma lslice_tmul (φ : E →ₚ[ℝ] ℝ) (x : E) (y : F) : lslice φ (x ⊗ₜ[ℝ] y) = φ x • y
```

**`PositiveLinearMap.tensor`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L106).

> The product functional `φ ⊗ ψ`.

```lean
noncomputable def tensor (φ : E →ₚ[ℝ] ℝ) (ψ : F →ₚ[ℝ] ℝ) : E ⊗[ℝ] F →ₗ[ℝ] ℝ
```

**`PositiveLinearMap.tensor_tmul`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L110).

```lean
lemma tensor_tmul (φ : E →ₚ[ℝ] ℝ) (ψ : F →ₚ[ℝ] ℝ) (x : E) (y : F) :
    tensor φ ψ (x ⊗ₜ[ℝ] y) = φ x * ψ y
```

**`PositiveLinearMap.tensor_apply`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L114).

```lean
lemma tensor_apply (φ : E →ₚ[ℝ] ℝ) (ψ : F →ₚ[ℝ] ℝ) (z : E ⊗[ℝ] F) :
    tensor φ ψ z = φ (rslice ψ z)
```

**`PositiveLinearMap.tensor_apply_eq_lslice`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L118).

```lean
lemma tensor_apply_eq_lslice (φ : E →ₚ[ℝ] ℝ) (ψ : F →ₚ[ℝ] ℝ) (z : E ⊗[ℝ] F) :
    tensor φ ψ z = ψ (lslice φ z)
```

## B. The minimal and the maximal cone

**`ProbabilisticTheory.minTensorCone`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L138).

> The minimal tensor cone: sums of products of nonnegative observables.

```lean
noncomputable def minTensorCone : PointedCone ℝ (E ⊗[ℝ] F)
```

**`ProbabilisticTheory.maxTensorCone`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L144).

> The maximal tensor cone: composite observables to which no product of positive functionals
> assigns a negative value.

```lean
noncomputable def maxTensorCone : PointedCone ℝ (E ⊗[ℝ] F)
```

**`ProbabilisticTheory.tmul_mem_minTensorCone`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L147).

```lean
lemma tmul_mem_minTensorCone {x : E} {y : F} (hx : 0 ≤ x) (hy : 0 ≤ y) :
    x ⊗ₜ[ℝ] y ∈ minTensorCone E F
```

**`ProbabilisticTheory.smul_mem_minTensorCone`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L152).

```lean
lemma smul_mem_minTensorCone {c : ℝ} (hc : 0 ≤ c) {w : E ⊗[ℝ] F} (hw : w ∈ minTensorCone E F) :
    c • w ∈ minTensorCone E F
```

**`ProbabilisticTheory.minTensorCone_induction`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L159).

> An induction principle for the minimal cone: a property of composite observables that holds
> for products of nonnegative observables and is stable under sums and nonnegative multiples holds
> on the whole minimal cone.

```lean
lemma minTensorCone_induction {p : E ⊗[ℝ] F → Prop} {z : E ⊗[ℝ] F} (hz : z ∈ minTensorCone E F)
    (tmul : ∀ x y, 0 ≤ x → 0 ≤ y → p (x ⊗ₜ[ℝ] y)) (zero : p 0)
    (add : ∀ z w, p z → p w → p (z + w)) (smul : ∀ c : ℝ, 0 ≤ c → ∀ z, p z → p (c • z)) :
    p z
```

**`ProbabilisticTheory.tensor_eq_dualDistrib`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L172).

> The product functional of positive functionals is the pairing with their dual tensor.

```lean
lemma tensor_eq_dualDistrib (φ : E →ₚ[ℝ] ℝ) (ψ : F →ₚ[ℝ] ℝ) (z : E ⊗[ℝ] F) :
    tensor φ ψ z = dualDistrib ℝ E F (φ.toLinearMap ⊗ₜ[ℝ] ψ.toLinearMap) z
```

**`ProbabilisticTheory.mem_maxTensorCone`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L180).

> A composite observable is in the maximal cone exactly when every product of positive
> functionals assigns it a nonnegative value.

```lean
lemma mem_maxTensorCone {z : E ⊗[ℝ] F} :
    z ∈ maxTensorCone E F ↔ ∀ (φ : E →ₚ[ℝ] ℝ) (ψ : F →ₚ[ℝ] ℝ), 0 ≤ tensor φ ψ z
```

**`ProbabilisticTheory.minTensorCone_le_maxTensorCone`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L189).

> Every observable in the minimal cone is in the maximal cone.

```lean
lemma minTensorCone_le_maxTensorCone : minTensorCone E F ≤ maxTensorCone E F
```

## C. Tensor products of positive maps

**`ProbabilisticTheory.posCone_map_le`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L198).

```lean
lemma posCone_map_le (φ : E →ₚ[ℝ] E') : (PosCone E).map φ.toLinearMap ≤ PosCone E'
```

**`ProbabilisticTheory.minTensorCone_map_le`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L203).

> Tensor products of positive maps preserve the minimal cone.

```lean
lemma minTensorCone_map_le (φ : E →ₚ[ℝ] E') (ψ : F →ₚ[ℝ] F') :
    (minTensorCone E F).map (TensorProduct.map φ.toLinearMap ψ.toLinearMap) ≤
      minTensorCone E' F'
```

**`ProbabilisticTheory.maxTensorCone_map_le`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L210).

> Tensor products of positive maps preserve the maximal cone.

```lean
lemma maxTensorCone_map_le (φ : E →ₚ[ℝ] E') (ψ : F →ₚ[ℝ] F') :
    (maxTensorCone E F).map (TensorProduct.map φ.toLinearMap ψ.toLinearMap) ≤
      maxTensorCone E' F'
```

**`ProbabilisticTheory.map_mem_minTensorCone`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L216).

```lean
lemma map_mem_minTensorCone (φ : E →ₚ[ℝ] E') (ψ : F →ₚ[ℝ] F') {z : E ⊗[ℝ] F}
    (hz : z ∈ minTensorCone E F) :
    TensorProduct.map φ.toLinearMap ψ.toLinearMap z ∈ minTensorCone E' F'
```

**`ProbabilisticTheory.map_mem_maxTensorCone`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L221).

```lean
lemma map_mem_maxTensorCone (φ : E →ₚ[ℝ] E') (ψ : F →ₚ[ℝ] F') {z : E ⊗[ℝ] F}
    (hz : z ∈ maxTensorCone E F) :
    TensorProduct.map φ.toLinearMap ψ.toLinearMap z ∈ maxTensorCone E' F'
```

## D. Composites

**`ProbabilisticTheory.IsArchimedeanTensorCone`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L232).

> A cone of composite observables is Archimedean when a composite observable that becomes
> nonnegative after adding any positive multiple of the unit `1 ⊗ 1` is already nonnegative.

```lean
def IsArchimedeanTensorCone (C : PointedCone ℝ (E ⊗[ℝ] F)) : Prop
```

**`ProbabilisticTheory.CompositeCone`**, a structure, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L238).

> A composite of two systems: a choice of nonnegative composite observables that contains every
> product of nonnegative observables and that no product of positive functionals makes negative.

```lean
structure CompositeCone where
  /-- The nonnegative composite observables. -/
  toPointedCone : PointedCone ℝ (E ⊗[ℝ] F)
  /-- Products of nonnegative observables are nonnegative. -/
  min_le : minTensorCone E F ≤ toPointedCone
  /-- Products of positive functionals stay nonnegative. -/
  le_max : toPointedCone ≤ maxTensorCone E F
```

**An instance with no name**, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L248).

```lean
instance : SetLike (CompositeCone E F) (E ⊗[ℝ] F)
```

**`ProbabilisticTheory.CompositeCone.mem_toPointedCone`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L253).

```lean
lemma mem_toPointedCone {C : CompositeCone E F} {z : E ⊗[ℝ] F} :
    z ∈ C.toPointedCone ↔ z ∈ C
```

**`ProbabilisticTheory.CompositeCone.ext`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L257).

```lean
lemma ext {C D : CompositeCone E F} (h : ∀ z, z ∈ C ↔ z ∈ D) : C = D
```

**`ProbabilisticTheory.CompositeCone.tmul_mem`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L259).

```lean
lemma tmul_mem (C : CompositeCone E F) {x : E} {y : F} (hx : 0 ≤ x) (hy : 0 ≤ y) :
    x ⊗ₜ[ℝ] y ∈ C
```

**`ProbabilisticTheory.CompositeCone.tensor_nonneg`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L264).

> Every product of positive functionals is nonnegative on a composite.

```lean
lemma tensor_nonneg (C : CompositeCone E F) (φ : E →ₚ[ℝ] ℝ) (ψ : F →ₚ[ℝ] ℝ) {z : E ⊗[ℝ] F}
    (hz : z ∈ C) : 0 ≤ tensor φ ψ z
```

**`ProbabilisticTheory.CompositeCone.instModuleNNReal`**, an instance, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L269).

> The elements of a composite form an `ℝ≥0`-module.

```lean
instance instModuleNNReal (C : CompositeCone E F) : Module ℝ≥0 C.toPointedCone
```

**`ProbabilisticTheory.CompositeCone.minimal`**, a def, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L280).

> The minimal composite.

```lean
noncomputable def minimal : CompositeCone E F
```

**`ProbabilisticTheory.CompositeCone.maximal`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L285).

> The maximal composite.

```lean
noncomputable def maximal : CompositeCone E F
```

**`ProbabilisticTheory.CompositeCone.IsArchimedean`**, a def, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L290).

> A composite is Archimedean when a composite observable that becomes nonnegative after adding
> any positive multiple of the unit `1 ⊗ 1` is already nonnegative.

```lean
def IsArchimedean (C : CompositeCone E F) : Prop
```

**`ProbabilisticTheory.CompositeCone.tmulRight`**, a def, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L294).

> For fixed `0 ≤ y₀`, tensoring on the right with `y₀` maps nonnegative observables of `E`
> `ℝ≥0`-linearly into any composite.

```lean
def tmulRight (C : CompositeCone E F) {y₀ : F} (hy₀ : 0 ≤ y₀) :
    PosCone E →ₗ[ℝ≥0] C.toPointedCone
```

**`ProbabilisticTheory.CompositeCone.tmulRight_apply`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L301).

```lean
lemma tmulRight_apply (C : CompositeCone E F) {y₀ : F} (hy₀ : 0 ≤ y₀) (x : PosCone E) :
    (C.tmulRight hy₀ x : E ⊗[ℝ] F) = (x : E) ⊗ₜ[ℝ] y₀
```

**`ProbabilisticTheory.CompositeCone.tmulLeft`**, a def, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L306).

> For fixed `0 ≤ x₀`, tensoring on the left with `x₀` maps nonnegative observables of `F`
> `ℝ≥0`-linearly into any composite.

```lean
def tmulLeft (C : CompositeCone E F) {x₀ : E} (hx₀ : 0 ≤ x₀) :
    PosCone F →ₗ[ℝ≥0] C.toPointedCone
```

**`ProbabilisticTheory.CompositeCone.tmulLeft_apply`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L313).

```lean
lemma tmulLeft_apply (C : CompositeCone E F) {x₀ : E} (hx₀ : 0 ≤ x₀) (y : PosCone F) :
    (C.tmulLeft hx₀ y : E ⊗[ℝ] F) = x₀ ⊗ₜ[ℝ] (y : F)
```

**`ProbabilisticTheory.exists_eq_sub_minTensorCone`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L320).

> Every composite observable is a difference of two sums of products of nonnegative
> observables.

```lean
lemma exists_eq_sub_minTensorCone (t : E ⊗[ℝ] F) :
    ∃ tp ∈ minTensorCone E F, ∃ tn ∈ minTensorCone E F, t = tp - tn
```

## E. The closure of the minimal cone and nuclear systems

**`ProbabilisticTheory.exists_tmul_add_smul_mem`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L341).

> A product plus a large enough multiple of `1 ⊗ 1` lies in the minimal cone:
> `x ⊗ y + (a * b) • (1 ⊗ 1)` is half the sum of `(a • 1 ± x) ⊗ (b • 1 ± y)`.

```lean
lemma exists_tmul_add_smul_mem (x : E) (y : F) :
    ∃ t : ℝ, x ⊗ₜ[ℝ] y + t • ((1 : E) ⊗ₜ[ℝ] (1 : F)) ∈ minTensorCone E F
```

**`ProbabilisticTheory.exists_add_smul_mem`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L356).

> Every composite observable plus a large enough multiple of `1 ⊗ 1` lies in the minimal cone.

```lean
lemma exists_add_smul_mem (z : E ⊗[ℝ] F) :
    ∃ t : ℝ, z + t • ((1 : E) ⊗ₜ[ℝ] (1 : F)) ∈ minTensorCone E F
```

**`ProbabilisticTheory.isDominatedCone_minTensorCone`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L370).

> The minimal cone is a convex cone dominated by `1 ⊗ 1`.

```lean
lemma isDominatedCone_minTensorCone :
    IsDominatedCone (minTensorCone E F : Set (E ⊗[ℝ] F)) ((1 : E) ⊗ₜ[ℝ] (1 : F))
```

**`ProbabilisticTheory.minTensorClosure`**, a def, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L381).

> The Archimedean closure of the minimal cone: composite observables that become sums of products
> of nonnegative observables after adding any positive multiple of the unit `1 ⊗ 1`.

```lean
def minTensorClosure : Set (E ⊗[ℝ] F)
```

**`ProbabilisticTheory.minTensorCone_subset_closure`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L384).

```lean
lemma minTensorCone_subset_closure :
    (minTensorCone E F : Set (E ⊗[ℝ] F)) ⊆ minTensorClosure E F
```

**`ProbabilisticTheory.minTensorClosure_subset_maxTensorCone`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L393).

> The closure of the minimal cone lies in the maximal cone.

```lean
lemma minTensorClosure_subset_maxTensorCone :
    minTensorClosure E F ⊆ (maxTensorCone E F : Set (E ⊗[ℝ] F))
```

**`ProbabilisticTheory.IsArchimedeanTensorCone.closure_subset`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L406).

> An Archimedean cone containing the minimal cone contains its closure.

```lean
lemma IsArchimedeanTensorCone.closure_subset {C : PointedCone ℝ (E ⊗[ℝ] F)}
    (hC : IsArchimedeanTensorCone C) (hmin : minTensorCone E F ≤ C) :
    minTensorClosure E F ⊆ C
```

**`ProbabilisticTheory.CompositeCone.IsArchimedean.closure_subset`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L411).

> An Archimedean composite contains the closure of the minimal cone.

```lean
lemma CompositeCone.IsArchimedean.closure_subset {C : CompositeCone E F} (hC : C.IsArchimedean) :
    minTensorClosure E F ⊆ C
```

**`ProbabilisticTheory.IsNuclear`**, a def, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L417).

> A system is nuclear when it composes uniquely with every Archimedean system: every composite
> observable in the maximal cone lies in the closure of the minimal cone.

```lean
def IsNuclear : Prop
```

**`ProbabilisticTheory.mem_maxTensorCone_iff_rslice`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean#L427).

> For Archimedean `E`, a composite observable is in the maximal cone exactly when applying any
> positive functional to the second factor leaves a nonnegative observable.

```lean
lemma mem_maxTensorCone_iff_rslice {z : E ⊗[ℝ] F} :
    z ∈ maxTensorCone E F ↔ ∀ ψ : F →ₚ[ℝ] ℝ, 0 ≤ rslice ψ z
```

## Depends on

- [Ordered positive cones](../../../physlib/probabilistictheory/orderunit/cone.md)
- [Separation from dominated cones](../../mathematics/part-01/convex/dominatedcone.md)

## Proof depends on

- [Separation by states (PhyslibAlpha)](../state/separation.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/TensorCone.lean)
