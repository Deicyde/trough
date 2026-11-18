---
declaration: module
origin: cited
lean: ProbabilisticTheory.CompositeCone.map_one_tmul_one, ProbabilisticTheory.CompositeCone.map_mem_minTensorClosure, ProbabilisticTheory.CompositeCone.map_mem_of_isNuclear_left, ProbabilisticTheory.CompositeCone.map_mem_of_isNuclear_right, ProbabilisticTheory.CompositeCone.map_mem_of_isNuclear_left', ProbabilisticTheory.CompositeCone.map_mem_of_isNuclear_right', ProbabilisticTheory.CompositeCone.map_mem_of_isClassical_left, ProbabilisticTheory.CompositeCone.map_mem_of_isClassical_right
statement: formalized
proof: formalized
---

# Complete positivity of classical channels

The module `PhyslibAlpha.ProbabilisticTheory.Composite.CompletePositivity`, [PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean): 8 declarations, 8 with a docstring.

> Channels into or out of a classical (nuclear) system are completely positive.

## i. Overview

> A channel acting on one part of a composite system should keep every nonnegative composite
> observable nonnegative, whatever the other part is. This is complete positivity, and it depends
> on which composite is used. For a channel into or out of a classical system it holds for every
> choice of composites: a classical system composes uniquely, so there is only one composite to
> check, and positive maps preserve the minimal and the maximal cone.
>
> Precisely, let `A` be any Archimedean ancilla. Then `φ ⊗ id` maps every composite observable in
> the maximal cone into every Archimedean cone that contains the minimal cone, whenever the input or
> the output of `φ` is classical. In particular it maps any composite of the input with `A` into any
> Archimedean composite of the output with `A`. For a classical input `φ` must be a channel;
> for a classical output any positive map works.

## ii. Key results

> - `CompositeCone.map_mem_of_isNuclear_left` : a channel out of a nuclear system is completely
>   positive.
> - `CompositeCone.map_mem_of_isNuclear_right` : a positive map into a nuclear system is completely
>   positive.
> - `CompositeCone.map_mem_of_isNuclear_left'`, `CompositeCone.map_mem_of_isNuclear_right'` : the
>   same, stated for composites.
> - `CompositeCone.map_mem_of_isClassical_left`, `CompositeCone.map_mem_of_isClassical_right` : the
>   same for classical systems.

## iv. References

> * None.

## A. Tensoring with the identity

**`ProbabilisticTheory.CompositeCone.map_one_tmul_one`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean#L66).

> Applying a channel to the first part of a composite leaves the unit `1 ⊗ 1` in place.

```lean
lemma map_one_tmul_one (φ : Channel E F) :
    TensorProduct.map φ.toLinearMap (LinearMap.id (R := ℝ) (M := A)) ((1 : E) ⊗ₜ[ℝ] (1 : A)) =
      (1 : F) ⊗ₜ[ℝ] (1 : A)
```

**`ProbabilisticTheory.CompositeCone.map_mem_minTensorClosure`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean#L74).

> Applying a channel to the first part maps the Archimedean closure of the minimal cone into
> itself.

```lean
lemma map_mem_minTensorClosure (φ : Channel E F) {z : E ⊗[ℝ] A}
    (hz : z ∈ minTensorClosure E A) :
    TensorProduct.map φ.toLinearMap LinearMap.id z ∈ minTensorClosure F A
```

## B. Nuclear inputs and outputs

**`ProbabilisticTheory.CompositeCone.map_mem_of_isNuclear_left`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean#L88).

> **A channel out of a nuclear system is completely positive.** Applied to the first part of a
> composite observable in the maximal cone with an Archimedean ancilla, it lands in every Archimedean
> cone of composite observables that contains the minimal cone.

```lean
lemma map_mem_of_isNuclear_left (hE : IsNuclear E) (φ : Channel E F) {z : E ⊗[ℝ] A}
    (hz : z ∈ maxTensorCone E A) {C : PointedCone ℝ (F ⊗[ℝ] A)} (hC : IsArchimedeanTensorCone C)
    (hmin : minTensorCone F A ≤ C) : TensorProduct.map φ.toLinearMap LinearMap.id z ∈ C
```

**`ProbabilisticTheory.CompositeCone.map_mem_of_isNuclear_right`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean#L96).

> **A positive map into a nuclear system is completely positive.** Applied to the first part of
> a composite observable in the maximal cone with an Archimedean ancilla, it lands in every
> Archimedean cone of composite observables that contains the minimal cone.

```lean
lemma map_mem_of_isNuclear_right (hF : IsNuclear F) (φ : E →ₚ[ℝ] F) {z : E ⊗[ℝ] A}
    (hz : z ∈ maxTensorCone E A) {C : PointedCone ℝ (F ⊗[ℝ] A)} (hC : IsArchimedeanTensorCone C)
    (hmin : minTensorCone F A ≤ C) : TensorProduct.map φ.toLinearMap LinearMap.id z ∈ C
```

**`ProbabilisticTheory.CompositeCone.map_mem_of_isNuclear_left'`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean#L104).

> A channel out of a nuclear system maps every composite into every Archimedean composite.

```lean
lemma map_mem_of_isNuclear_left' (hE : IsNuclear E) (φ : Channel E F) (C₁ : CompositeCone E A)
    {C₂ : CompositeCone F A} (hC₂ : C₂.IsArchimedean) {z : E ⊗[ℝ] A} (hz : z ∈ C₁) :
    TensorProduct.map φ.toLinearMap LinearMap.id z ∈ C₂
```

**`ProbabilisticTheory.CompositeCone.map_mem_of_isNuclear_right'`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean#L110).

> A positive map into a nuclear system maps every composite into every Archimedean composite.

```lean
lemma map_mem_of_isNuclear_right' (hF : IsNuclear F) (φ : E →ₚ[ℝ] F) (C₁ : CompositeCone E A)
    {C₂ : CompositeCone F A} (hC₂ : C₂.IsArchimedean) {z : E ⊗[ℝ] A} (hz : z ∈ C₁) :
    TensorProduct.map φ.toLinearMap LinearMap.id z ∈ C₂
```

## C. Classical inputs and outputs

**`ProbabilisticTheory.CompositeCone.map_mem_of_isClassical_left`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean#L118).

> **A channel out of a classical system is completely positive.**

```lean
lemma map_mem_of_isClassical_left {E : Type*} [ArchimedeanOrderUnitSpace E] (hE : IsClassical E)
    (φ : Channel E F) (C₁ : CompositeCone E A) {C₂ : CompositeCone F A} (hC₂ : C₂.IsArchimedean)
    {z : E ⊗[ℝ] A} (hz : z ∈ C₁) : TensorProduct.map φ.toLinearMap LinearMap.id z ∈ C₂
```

**`ProbabilisticTheory.CompositeCone.map_mem_of_isClassical_right`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean#L124).

> **A positive map into a classical system is completely positive.**

```lean
lemma map_mem_of_isClassical_right {F : Type*} [ArchimedeanOrderUnitSpace F] (hF : IsClassical F)
    (φ : E →ₚ[ℝ] F) (C₁ : CompositeCone E A) {C₂ : CompositeCone F A} (hC₂ : C₂.IsArchimedean)
    {z : E ⊗[ℝ] A} (hz : z ∈ C₁) : TensorProduct.map φ.toLinearMap LinearMap.id z ∈ C₂
```

## Depends on

- [Channels](../channel/basic.md)
- [Classical systems](../classical/basic.md)
- [Composite systems](tensorcone.md)

## Proof depends on

- [Classical systems are nuclear](../classical/nuclear.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Composite/CompletePositivity.lean)
