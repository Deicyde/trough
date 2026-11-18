---
declaration: module
origin: cited
lean: ProbabilisticTheory.POVM, ProbabilisticTheory.POVM.IsPVM, ProbabilisticTheory.POVM.isSharp_apply_empty, ProbabilisticTheory.POVM.isSharp_apply_univ, ProbabilisticTheory.POVM.isPVM_of_forall_isIdempotentElem, ProbabilisticTheory.PVM, ProbabilisticTheory.PVM.ext, ProbabilisticTheory.PVM.isSharp_apply
statement: formalized
proof: formalized
---

# POVMs and PVMs

The module `PhyslibAlpha.ProbabilisticTheory.Representation.PVM`, [PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean): 9 declarations (1 instance with no name), 8 with a docstring.

> POVMs as effect-valued measures, and PVMs as POVMs whose values are sharp effects.

## i. Overview

> For the self-adjoint part of an operator algebra, an effect-valued measure is a POVM. A PVM is a
> POVM whose values are sharp effects. A POVM whose values are projections is a PVM.

## ii. Key results

> - `POVM` : positive-operator-valued measures.
> - `POVM.IsPVM`, `PVM` : projection-valued measures.
> - `POVM.isPVM_of_forall_isIdempotentElem` : a POVM of projections is a PVM.

## iv. References

> * None.

## A. POVMs

**`ProbabilisticTheory.POVM`**, an abbrev, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean#L47).

> A positive-operator-valued measure: the physics name for `EffectValuedMeasure`.

```lean
abbrev POVM (Ω E : Type*) [MeasurableSpace Ω] [OrderUnitSpace E]
```

**`ProbabilisticTheory.POVM.IsPVM`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean#L54).

> A POVM is a PVM (projection-valued measure) when every effect it assigns is sharp.

```lean
def IsPVM (μ : POVM Ω E) : Prop
```

**`ProbabilisticTheory.POVM.isSharp_apply_empty`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean#L57).

> The impossible event is always sharp, in any POVM: it is assigned the effect `0`.

```lean
lemma isSharp_apply_empty (μ : POVM Ω E) : Effect.IsSharp (μ ∅ MeasurableSet.empty)
```

**`ProbabilisticTheory.POVM.isSharp_apply_univ`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean#L61).

> The certain event is always sharp, in any POVM: it is assigned the effect `1`.

```lean
lemma isSharp_apply_univ (μ : POVM Ω E) : Effect.IsSharp (μ Set.univ MeasurableSet.univ)
```

## B. POVMs of projections

**`ProbabilisticTheory.POVM.isPVM_of_forall_isIdempotentElem`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean#L73).

> A POVM whose values are projections is a PVM.

```lean
lemma POVM.isPVM_of_forall_isIdempotentElem {Ω : Type*} [MeasurableSpace Ω]
    {μ : POVM Ω (selfAdjoint A)}
    (h : ∀ s hs, IsIdempotentElem (((μ s hs : Effect (selfAdjoint A)) : selfAdjoint A) : A)) :
    μ.IsPVM
```

## C. PVMs

**`ProbabilisticTheory.PVM`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean#L84).

> Projection-valued measures: POVMs whose values are sharp effects.

```lean
def PVM (Ω E : Type*) [MeasurableSpace Ω] [OrderUnitSpace E]
```

**An instance with no name**, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean#L90).

> A PVM, viewed as a POVM, forgetting the sharpness of its effects.

```lean
instance : CoeOut (PVM Ω E) (POVM Ω E)
```

**`ProbabilisticTheory.PVM.ext`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean#L93).

```lean
lemma ext {π ρ : PVM Ω E} (h : ∀ s hs, (π : POVM Ω E) s hs = (ρ : POVM Ω E) s hs) : π = ρ
```

**`ProbabilisticTheory.PVM.isSharp_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean#L97).

> Every effect of a PVM is sharp: unfolding what it means to be one.

```lean
lemma isSharp_apply (π : PVM Ω E) (s : Set Ω) (hs : MeasurableSet s) :
    Effect.IsSharp ((π : POVM Ω E) s hs)
```

## Depends on

- [The observables of a C⋆-algebra](../../../physlib/probabilistictheory/cstaralgebra/orderunit.md)
- [Sharp effects](../../../physlib/probabilistictheory/effect/sharp.md)
- [Effect-valued measures](../measurement/effectvaluedmeasure.md)

## Proof depends on

- [Projections are sharp](../cstaralgebra/sharpeffect.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/PVM.lean)
