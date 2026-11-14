---
declaration: module
origin: cited
lean: StandardModel.u1AdjointMatrix, StandardModel.u1AdjointMatrix_apply, StandardModel.IsU1BiAdjointMat, StandardModel.isU1BiAdjointMat_iff, StandardModel.IsU1BiAdjointMat.map_T, StandardModel.IsU1BiAdjoint, StandardModel.IsU1BiAdjoint.traceContraction, StandardModel.IsU1BiAdjoint.map_traceContraction
statement: formalized
proof: formalized
---

# Families with two `u(1)` adjoint indices

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.Invariants.IsU1BiAdjoint`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean): 8 declarations, 8 with a docstring.

## i. Overview

> The hypercharge factor is abelian, so its adjoint action on `u(1)` is trivial. A family
> `T : (Fin 2 → Fin 1) → B` obeys the `u(1)` bi-adjoint law when a hypercharge rotation moves
> it by one factor of the `1 × 1` adjoint matrix `1` per index, which is to say not at all
> (`isU1BiAdjointMat_iff`). The law has the same shape as `IsSU2BiAdjoint` and
> `IsSU3BiAdjoint`, so that the three factors can be treated alike. The trace contraction is the
> one component of the family, and every map obeying the law fixes it.

## ii. Key results

> - `isU1BiAdjointMat_iff` : the `u(1)` transformation law says exactly that the map fixes every
>   component: the adjoint matrix is `1`, and there is a single family of two `u(1)` indices to sum
>   over

## iv. References

> * None.

## A. The adjoint matrix and the transformation law

**`StandardModel.u1AdjointMatrix`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean#L52).

> The adjoint matrix of an element of `U(1)`: the one by one matrix `1`, the `u(1)`
> factor being abelian and so acting trivially on its own algebra.

```lean
def u1AdjointMatrix (_u : unitary ℂ) : Matrix (Fin 1) (Fin 1) ℝ
```

**`StandardModel.u1AdjointMatrix_apply`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean#L56).

> The single entry of the adjoint matrix of an element of `U(1)` is `1`.

```lean
lemma u1AdjointMatrix_apply (u : unitary ℂ) (i j : Fin 1) :
    u1AdjointMatrix u i j = 1
```

**`StandardModel.IsU1BiAdjointMat`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean#L62).

> The linear map `f` moves the components of `T` as `u ∈ U(1)` moves a tensor with two
> adjoint indices: one factor of `u1AdjointMatrix u` per index, with the summed index in
> the row slot.

```lean
def IsU1BiAdjointMat {B : Type*} [AddCommMonoid B] [Module ℂ B]
    (u : unitary ℂ) (f : B →ₗ[ℂ] B)
    (T : (Fin 2 → Fin 1) → B) : Prop
```

**`StandardModel.isU1BiAdjointMat_iff`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean#L71).

> The `u(1)` transformation law says exactly that the map fixes every component: the
> adjoint matrix is `1`, and there is a single family of two `u(1)` indices to sum over.

```lean
lemma isU1BiAdjointMat_iff {B : Type*} [AddCommMonoid B] [Module ℂ B]
    (u : unitary ℂ) (f : B →ₗ[ℂ] B) (T : (Fin 2 → Fin 1) → B) :
    IsU1BiAdjointMat u f T ↔ ∀ l : Fin 2 → Fin 1, f (T l) = T l
```

**`StandardModel.IsU1BiAdjointMat.map_T`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean#L79).

> A linear map obeying the `u(1)` transformation law fixes every component.

```lean
lemma IsU1BiAdjointMat.map_T {B : Type*} [AddCommMonoid B] [Module ℂ B] {u : unitary ℂ}
    {f : B →ₗ[ℂ] B} {T : (Fin 2 → Fin 1) → B} (hf : IsU1BiAdjointMat u f T)
    (l : Fin 2 → Fin 1) : f (T l) = T l
```

**`StandardModel.IsU1BiAdjoint`**, a structure, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean#L87).

> A family `T` of elements of `B`, indexed by two `u(1)` adjoint indices, transforms as a
> tensor `T^{a b}` under the hypercharge factor of the gauge group. Nothing is asked of the
> colour and isospin factors.

```lean
structure IsU1BiAdjoint (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B)
    (T : (Fin 2 → Fin 1) → B) : Prop where
  repGauge_T : ∀ g : unitary ℂ, IsU1BiAdjointMat g (repGauge (1, 1, g)) T
```

## B. The trace contraction

**`StandardModel.IsU1BiAdjoint.traceContraction`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean#L105).

> The trace contraction: the Kronecker contraction of the two `u(1)` indices, which is
> the one component of the family.

```lean
def traceContraction (T : (Fin 2 → Fin 1) → B) : B
```

**`StandardModel.IsU1BiAdjoint.map_traceContraction`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean#L108).

> Any map obeying the `u(1)` law fixes the trace contraction.

```lean
lemma map_traceContraction {u : unitary ℂ} {f : B →ₗ[ℂ] B} (hf : IsU1BiAdjointMat u f T) :
    f (traceContraction T) = traceContraction T
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/IsU1BiAdjoint.lean)
