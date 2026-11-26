---
declaration: module
origin: cited
lean: StandardModel.ReducesInvariantsTo.ofSU3, StandardModel.ReducesInvariantsTo.ofSU2, StandardModel.isStableUnder_range_repGauge, StandardModel.isStableUnder_range_repLorentz
statement: formalized
proof: formalized
---

# Invariant reduction for the Standard Model gauge group

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.InvariantReduction`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/InvariantReduction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/InvariantReduction.lean): 4 declarations, 4 with a docstring.

> The colour and isospin reductions, and stable symbol ranges.

## i. Overview

> The Standard Model sectors are classified with `ReducesInvariantsTo` from
> `PhyslibAlpha.Mathematics.InvariantReduction`, one index law at a time: colour, isospin and
> Lorentz. There the gauge and Lorentz groups are read together as one family,
> `gaugeLorentzMaps`, used here with the gauge group `GaugeGroupI`, and a reduction for the gauge
> group or the Lorentz group alone transports to it. This file supplies what the sectors share
> beyond that. A reduction for the colour factor `SU(3)` or the isospin factor `SU(2)` alone also
> transports to the combined family. The range of a symbol map is stable under the gauge group
> and, with no derivative slots, under the Lorentz group. That an element fixed by each of the
> colour, isospin and hypercharge factors separately is gauge invariant,
> `forall_repGauge_eq_self`, is in `GaugeGroup/Basic.lean`.

## ii. Key results

> - `ReducesInvariantsTo.ofSU3`, `ReducesInvariantsTo.ofSU2` : a reduction for the colour or
>   isospin factor is a reduction for the gauge and Lorentz groups together
> - `isStableUnder_range_repGauge`, `isStableUnder_range_repLorentz` : the range of a symbol map
>   is stable under the gauge group and, with no derivative slots, under the Lorentz group

## iv. References

> * None.

## A. Colour and isospin reductions

> The gauge and Lorentz groups are read together as `gaugeLorentzMaps` at `GaugeGroupI`. A
> reduction for the colour factor, through `(U, 1, 1)`, or the isospin factor, through
> `(1, V, 1)`, is transported to it by `ReducesInvariantsTo.comp`.

**`StandardModel.ReducesInvariantsTo.ofSU3`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/InvariantReduction.lean#L70).

> A reduction for the colour factor is a reduction for the gauge and Lorentz groups
> together.

```lean
lemma ReducesInvariantsTo.ofSU3 {V W : Submodule ℂ B}
    (hP : ReducesInvariantsTo (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge (U, 1, 1)) V W) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W
```

**`StandardModel.ReducesInvariantsTo.ofSU2`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/InvariantReduction.lean#L78).

> A reduction for the isospin factor is a reduction for the gauge and Lorentz groups
> together.

```lean
lemma ReducesInvariantsTo.ofSU2 {V W : Submodule ℂ B}
    (hP : ReducesInvariantsTo (fun U : specialUnitaryGroup (Fin 2) ℂ => repGauge (1, U, 1)) V W) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W
```

## B. Stability of symbol ranges

> The range of a symbol map is carried into itself by the gauge group, and, with no
> derivative slots, by the Lorentz group.

**`StandardModel.isStableUnder_range_repGauge`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/InvariantReduction.lean#L101).

> The range of a symbol map is carried into itself by the gauge group. The symbol is
> equivariant, so a gauge transformation only moves the dual vector it is evaluated at.

```lean
lemma isStableUnder_range_repGauge {M : Type} [AddCommGroup M] [Module ℂ M]
    {repGauge : Representation ℂ GaugeGroupI B} {ρ : Representation ℂ GaugeGroupI M}
    {F : Module.Dual ℂ M →ₗ[ℂ] B} (hF : ∀ g φ, repGauge g (F φ) = F (ρ.dual g φ)) :
    ∀ g : GaugeGroupI, ∀ y ∈ LinearMap.range F, repGauge g y ∈ LinearMap.range F
```

**`StandardModel.isStableUnder_range_repLorentz`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/InvariantReduction.lean#L110).

> The range of an underived symbol map is carried into itself by the Lorentz group. With
> no derivative slots to mix, the transformation law moves the dual vector alone.

```lean
lemma isStableUnder_range_repLorentz {M : Type} [AddCommGroup M] [Module ℂ M]
    {repLorentz : Representation ℂ SL(2,ℂ) B} {ρ : Representation ℂ SL(2,ℂ) M}
    {F : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ M →ₗ[ℂ] B}
    (hF : IsLorentzCovDerivTransforms repLorentz ρ F) (Λ : SL(2,ℂ)) :
    ∀ y ∈ LinearMap.range (F (![] : Fin 0 → Fin 1 ⊕ Fin 3)),
      repLorentz Λ y ∈ LinearMap.range (F (![] : Fin 0 → Fin 1 ⊕ Fin 3))
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)
- [Reducing invariants modulo a stable submodule](../../../mathematics/part-01/invariantreduction.md)
- [Class IsLorentzDeriv](../../../relativity/islorentzderiv.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/InvariantReduction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/InvariantReduction.lean)
