---
declaration: module
origin: cited
lean: ProbabilisticTheory.WStarAlgebraStructure, ProbabilisticTheory.WStarAlgebraStructure.weakStarTopology, ProbabilisticTheory.WStarAlgebraStructure.norm_le_weakStarTopology, ProbabilisticTheory.WStarAlgebraStructure.predualPairing, ProbabilisticTheory.WStarAlgebraStructure.predualPairing_apply, ProbabilisticTheory.WStarAlgebraStructure.norm_predualPairing_apply, ProbabilisticTheory.WStarAlgebraStructure.predualPairing_weakStar_continuous, ProbabilisticTheory.WStarAlgebraStructure.ext_of_forall_predualPairing_eq
statement: formalized
proof: formalized
---

# W⋆-algebras and normal states

The module `PhyslibAlpha.ProbabilisticTheory.WStarAlgebra.Basic`, [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean): 13 declarations (1 instance with no name), 8 with a docstring.

> W⋆-algebras with a chosen predual, their weak-⋆ topology, and normal states.

## i. Overview

> A W⋆-algebra is a C⋆-algebra that is the dual of a Banach space, its predual. Mathlib's
> `WStarAlgebra` only asserts that a predual exists. The weak-⋆ topology depends on the predual, so
> `WStarAlgebraStructure` fixes one together with the isometric identification of `A` with its dual.
> The weak-⋆ topology is coarser than the norm topology. A normal state is a state that is continuous
> for the weak-⋆ topology.

## ii. Key results

> - `WStarAlgebraStructure` : a C⋆-algebra with a chosen predual.
> - `WStarAlgebraStructure.weakStarTopology` : the weak-⋆ topology.
> - `WStarAlgebraStructure.norm_le_weakStarTopology` : the weak-⋆ topology is coarser than the norm
>   topology.
> - `NormalState` : a weak-⋆ continuous state.

## iv. References

> * None.

## A. W⋆-algebras

**`ProbabilisticTheory.WStarAlgebraStructure`**, a class, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L60).

> **A W⋆-algebra**: a C⋆-algebra with a chosen predual and an isometric identification of the
> algebra with the dual of its predual.

```lean
class WStarAlgebraStructure (A : Type*) extends CStarAlgebra A, PartialOrder A, StarOrderedRing A
    where
  /-- The predual: a Banach space `E` with `A ≃ₗᵢ[ℂ] StrongDual ℂ E` isometrically. -/
  Predual : Type*
  predualNormedAddCommGroup : NormedAddCommGroup Predual
  predualNormedSpace : NormedSpace ℂ Predual
  predualCompleteSpace : CompleteSpace Predual
  /-- The defining isometric identification `A ≃ₗᵢ[ℂ] StrongDual ℂ (Predual A)`, `a ↦ (ξ ↦
  ⟨a, ξ⟩)` for the duality pairing `A` inherits from being `Predual A`'s dual. -/
  toDual : A ≃ₗᵢ[ℂ] StrongDual ℂ Predual
```

**`ProbabilisticTheory.WStarAlgebraStructure.weakStarTopology`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L85).

> **The weak-⋆ topology**, induced from the dual of the predual. States converge in it when their
> values on each predual element converge. It is not an instance, since `A` already carries its norm
> topology.

```lean
def weakStarTopology : TopologicalSpace A
```

**`ProbabilisticTheory.WStarAlgebraStructure.norm_le_weakStarTopology`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L89).

> **The weak-⋆ topology is coarser than the norm topology.**

```lean
lemma norm_le_weakStarTopology :
    (inferInstance : TopologicalSpace A) ≤ weakStarTopology A
```

## B. The predual pairing

**`ProbabilisticTheory.WStarAlgebraStructure.predualPairing`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L103).

> The continuous functional on `A` given by a predual element.

```lean
def predualPairing (ξ : WStarAlgebraStructure.Predual A) : A →L[ℂ] ℂ
```

**`ProbabilisticTheory.WStarAlgebraStructure.predualPairing_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L108).

```lean
lemma predualPairing_apply (ξ : WStarAlgebraStructure.Predual A) (a : A) :
    predualPairing ξ a = toDual a ξ
```

**`ProbabilisticTheory.WStarAlgebraStructure.norm_predualPairing_apply`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L111).

```lean
lemma norm_predualPairing_apply (ξ : WStarAlgebraStructure.Predual A) (a : A) :
    ‖predualPairing ξ a‖ ≤ ‖a‖ * ‖ξ‖
```

**`ProbabilisticTheory.WStarAlgebraStructure.predualPairing_weakStar_continuous`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L117).

> The functional of a predual element is weak-⋆ continuous.

```lean
lemma predualPairing_weakStar_continuous (ξ : WStarAlgebraStructure.Predual A) :
    Continuous[WStarAlgebraStructure.weakStarTopology A, inferInstance]
      (predualPairing ξ)
```

**`ProbabilisticTheory.WStarAlgebraStructure.ext_of_forall_predualPairing_eq`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L138).

> Predual elements separate the points of a W⋆-algebra.

```lean
lemma ext_of_forall_predualPairing_eq {a b : A}
    (h : ∀ ξ : WStarAlgebraStructure.Predual A, predualPairing ξ a = predualPairing ξ b) :
    a = b
```

> Weak-⋆ convergence is convergence of all predual pairings, for filters.

**`ProbabilisticTheory.WStarAlgebraStructure.tendsto_weakStar_iff_forall_predualPairing_tendsto`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L147).

```lean
lemma tendsto_weakStar_iff_forall_predualPairing_tendsto
    {α : Type*} {l : Filter α} {f : α → A} {a : A} :
    Tendsto f l (@nhds A (WStarAlgebraStructure.weakStarTopology A) a) ↔
      ∀ ξ : WStarAlgebraStructure.Predual A,
        Tendsto (fun i => predualPairing ξ (f i)) l
          (𝓝 (predualPairing ξ a))
```

## C. Normal states

**`ProbabilisticTheory.NormalState`**, a structure, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L171).

> A state that is continuous for the weak-* topology of the chosen predual.

```lean
structure NormalState (A : Type*) [WStarAlgebraStructure A] where
  /-- The underlying state. -/
  toState : 𝓢[ℂ, A]
  /-- The state is continuous for the chosen weak-* topology. -/
  weakStar_continuous :
    Continuous[WStarAlgebraStructure.weakStarTopology A, inferInstance] (⇑toState : A → ℂ)
```

**An instance with no name**, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L182).

```lean
noncomputable instance : CoeFun (NormalState A) (fun _ => A → ℂ)
```

**`ProbabilisticTheory.NormalState.toState_apply`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L186).

```lean
lemma toState_apply (ω : NormalState A) (a : A) : ω.toState a = ω a
```

**`ProbabilisticTheory.NormalState.continuous`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean#L189).

> Weak-* continuity implies ordinary norm continuity because the weak-* topology is coarser.

```lean
lemma continuous (ω : NormalState A) : Continuous (ω : A → ℂ)
```

## Depends on

- [Channels](../channel/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Basic.lean)
