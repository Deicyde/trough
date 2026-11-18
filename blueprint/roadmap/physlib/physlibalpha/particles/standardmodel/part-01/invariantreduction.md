---
declaration: module
origin: cited
lean: StandardModel.gaugeLorentzMaps, StandardModel.isStableUnder_gaugeLorentzMaps_iff, StandardModel.forall_gaugeLorentzMaps_eq_self_iff, StandardModel.isFixedBy_gaugeLorentzMaps_iff, StandardModel.ReducesInvariantsTo.mem_sup_and_gauge_lorentz_invariant_iff, StandardModel.ReducesInvariantsTo.ofGauge, StandardModel.ReducesInvariantsTo.ofSU3, StandardModel.ReducesInvariantsTo.ofSU2
statement: formalized
proof: formalized
---

# Invariant reduction for the gauge and Lorentz groups

The module `PhyslibAlpha.Particles.StandardModel.InvariantReduction`, [PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean): 28 declarations, 28 with a docstring.

## i. Overview

> The Standard Model sectors are classified with `ReducesInvariantsTo` from
> `PhyslibAlpha.Mathematics.InvariantReduction`, one index law at a time: colour, isospin and Lorentz.
> The reductions for the individual laws are `invariantReductionToSpan` beside each
> classification theorem. This file supplies what the sectors share when combining them.
>
>   endpoint for it, the transport of gauge, colour, isospin and Lorentz reductions to it, and
>   its multiplicativity.
>   by each factor is gauge invariant.

## ii. Key results

> - `gaugeLorentzMaps` : the gauge and Lorentz groups read as a single family of linear maps, indexed
>   by their disjoint union
> - `isStableUnder_gaugeLorentzMaps_iff` : a submodule stable under both groups is stable under the
>   combined family, and conversely
> - `forall_gaugeLorentzMaps_eq_self_iff` : an element fixed by both groups is fixed by the combined
>   family, and conversely
> - `isFixedBy_gaugeLorentzMaps_iff` : a submodule fixed pointwise by both groups is fixed pointwise
>   by the combined family, and conversely

## iv. References

> * None.

## A. The gauge and Lorentz groups together

> The family indexed by the disjoint union of the two groups has as invariants the elements
> fixed by both groups, and as stable submodules those stable under both. A reduction for the
> gauge group, its colour or isospin factor, or the Lorentz group is transported to it by
> `ReducesInvariantsTo.comp`.

**`StandardModel.gaugeLorentzMaps`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L73).

> The gauge and Lorentz groups read as a single family of linear maps, indexed by their
> disjoint union.

```lean
def gaugeLorentzMaps : GaugeGroupI ⊕ SL(2,ℂ) → B →ₗ[ℂ] B
```

**`StandardModel.isStableUnder_gaugeLorentzMaps_iff`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L80).

> A submodule stable under both groups is stable under the combined family, and
> conversely.

```lean
lemma isStableUnder_gaugeLorentzMaps_iff {V : Submodule ℂ B} :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) V
      ↔ (∀ g : GaugeGroupI, ∀ y ∈ V, repGauge g y ∈ V)
        ∧ ∀ Λ : SL(2,ℂ), ∀ y ∈ V, repLorentz Λ y ∈ V
```

**`StandardModel.forall_gaugeLorentzMaps_eq_self_iff`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L91).

> An element fixed by both groups is fixed by the combined family, and conversely.

```lean
lemma forall_gaugeLorentzMaps_eq_self_iff {x : B} :
    (∀ p, gaugeLorentzMaps repGauge repLorentz p x = x)
      ↔ (∀ g : GaugeGroupI, repGauge g x = x) ∧ ∀ Λ : SL(2,ℂ), repLorentz Λ x = x
```

**`StandardModel.isFixedBy_gaugeLorentzMaps_iff`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L102).

> A submodule fixed pointwise by both groups is fixed pointwise by the combined family, and
> conversely.

```lean
lemma isFixedBy_gaugeLorentzMaps_iff {V : Submodule ℂ B} :
    IsFixedBy (gaugeLorentzMaps repGauge repLorentz) V
      ↔ (∀ g : GaugeGroupI, ∀ y ∈ V, repGauge g y = y)
        ∧ ∀ Λ : SL(2,ℂ), ∀ y ∈ V, repLorentz Λ y = y
```

**`StandardModel.ReducesInvariantsTo.mem_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L115).

> The classification endpoint `ReducesInvariantsTo.mem_sup_and_forall_eq_self_iff` for the
> gauge and Lorentz groups together, with the two invariances and the two stabilities stated
> separately.

```lean
lemma ReducesInvariantsTo.mem_sup_and_gauge_lorentz_invariant_iff {V W S : Submodule ℂ B}
    (hP : ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W) (hWV : W ≤ V)
    (hW : IsFixedBy (gaugeLorentzMaps repGauge repLorentz) W)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ Λ : SL(2,ℂ), ∀ y ∈ S, repLorentz Λ y ∈ S) (x : B) :
    (x ∈ V ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x) ∧ ∀ Λ : SL(2,ℂ), repLorentz Λ x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ Λ : SL(2,ℂ), repLorentz Λ y = y) ∧ x - y ∈ W
```

**`StandardModel.ReducesInvariantsTo.ofGauge`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L127).

> A gauge reduction is a reduction for the gauge and Lorentz groups together.

```lean
lemma ReducesInvariantsTo.ofGauge {V W : Submodule ℂ B}
    (hP : ReducesInvariantsTo (fun g : GaugeGroupI => repGauge g) V W) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W
```

**`StandardModel.ReducesInvariantsTo.ofSU3`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L134).

> A reduction for the colour factor is a reduction for the gauge and Lorentz groups
> together.

```lean
lemma ReducesInvariantsTo.ofSU3 {V W : Submodule ℂ B}
    (hP : ReducesInvariantsTo (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge (U, 1, 1)) V W) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W
```

**`StandardModel.ReducesInvariantsTo.ofSU2`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L142).

> A reduction for the isospin factor is a reduction for the gauge and Lorentz groups
> together.

```lean
lemma ReducesInvariantsTo.ofSU2 {V W : Submodule ℂ B}
    (hP : ReducesInvariantsTo (fun U : specialUnitaryGroup (Fin 2) ℂ => repGauge (1, U, 1)) V W) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W
```

**`StandardModel.ReducesInvariantsTo.ofLorentz`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L149).

> A Lorentz reduction is a reduction for the gauge and Lorentz groups together.

```lean
lemma ReducesInvariantsTo.ofLorentz {V W : Submodule ℂ B}
    (hP : ReducesInvariantsTo (fun Λ : SL(2,ℂ) => repLorentz Λ) V W) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) V W
```

**`StandardModel.gaugeLorentzMaps_mul`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L163).

> The two groups read as one family of maps respect multiplication, each of the two
> representations doing so.

```lean
lemma gaugeLorentzMaps_mul
    (hG : ∀ (g : GaugeGroupI) (b₁ b₂ : B),
      repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂)
    (hL : ∀ (Λ : SL(2,ℂ)) (b₁ b₂ : B),
      repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂)
    (p : GaugeGroupI ⊕ SL(2,ℂ)) (a b : B) :
    gaugeLorentzMaps repGauge repLorentz p (a * b)
      = gaugeLorentzMaps repGauge repLorentz p a
        * gaugeLorentzMaps repGauge repLorentz p b
```

## B. The three factors of a gauge transformation

> A gauge transformation is a triple `(U, V, t)`, and the colour, isospin and hypercharge laws
> each constrain one factor. This section records the factors and inverses of `(U, 1, 1)`,
> `(1, V, 1)` and `(1, 1, t)`, the entries of inverses in `SU(3)` and `SU(2)`, and the
> factorisation that turns three separate invariances into gauge invariance.

**`StandardModel.su3_inv_apply`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L191).

> The entries of the inverse of an `SU(3)` element are the conjugated transposed
> entries, the inverse of a unitary matrix being its conjugate transpose.

```lean
lemma su3_inv_apply (U : specialUnitaryGroup (Fin 3) ℂ) (a b : Fin 3) :
    (U⁻¹).1 a b = conj (U.1 b a)
```

**`StandardModel.su2_inv_apply`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L198).

> The entries of the inverse of an `SU(2)` element are the conjugated transposed
> entries.

```lean
lemma su2_inv_apply (U : specialUnitaryGroup (Fin 2) ℂ) (a b : Fin 2) :
    (U⁻¹).1 a b = conj (U.1 b a)
```

**`StandardModel.unitary_inv_coe`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L204).

> The inverse of a unitary scalar is its conjugate.

```lean
lemma unitary_inv_coe (t : unitary ℂ) : ((t⁻¹ : unitary ℂ) : ℂ) = star (t : ℂ)
```

**`StandardModel.toSU3_su3Elt`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L207).

> The colour factor of a colour gauge transformation.

```lean
lemma toSU3_su3Elt (U : specialUnitaryGroup (Fin 3) ℂ) :
    GaugeGroupI.toSU3 ((U, 1, 1) : GaugeGroupI) = U
```

**`StandardModel.toSU2_su3Elt`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L211).

> The isospin factor of a colour gauge transformation is trivial.

```lean
lemma toSU2_su3Elt (U : specialUnitaryGroup (Fin 3) ℂ) :
    GaugeGroupI.toSU2 ((U, 1, 1) : GaugeGroupI) = 1
```

**`StandardModel.toU1_su3Elt`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L215).

> The hypercharge factor of a colour gauge transformation is trivial.

```lean
lemma toU1_su3Elt (U : specialUnitaryGroup (Fin 3) ℂ) :
    GaugeGroupI.toU1 ((U, 1, 1) : GaugeGroupI) = 1
```

**`StandardModel.inv_su3Elt`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L220).

> The inverse of a colour gauge transformation is the colour transformation of the
> inverse.

```lean
lemma inv_su3Elt (U : specialUnitaryGroup (Fin 3) ℂ) :
    ((U, 1, 1) : GaugeGroupI)⁻¹ = ((U⁻¹, 1, 1) : GaugeGroupI)
```

**`StandardModel.toSU3_su2Elt`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L225).

> The colour factor of an isospin gauge transformation is trivial.

```lean
lemma toSU3_su2Elt (V : specialUnitaryGroup (Fin 2) ℂ) :
    GaugeGroupI.toSU3 ((1, V, 1) : GaugeGroupI) = 1
```

**`StandardModel.toSU2_su2Elt`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L229).

> The isospin factor of an isospin gauge transformation.

```lean
lemma toSU2_su2Elt (V : specialUnitaryGroup (Fin 2) ℂ) :
    GaugeGroupI.toSU2 ((1, V, 1) : GaugeGroupI) = V
```

**`StandardModel.toU1_su2Elt`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L233).

> The hypercharge factor of an isospin gauge transformation is trivial.

```lean
lemma toU1_su2Elt (V : specialUnitaryGroup (Fin 2) ℂ) :
    GaugeGroupI.toU1 ((1, V, 1) : GaugeGroupI) = 1
```

**`StandardModel.inv_su2Elt`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L238).

> The inverse of an isospin gauge transformation is the isospin transformation of the
> inverse.

```lean
lemma inv_su2Elt (V : specialUnitaryGroup (Fin 2) ℂ) :
    ((1, V, 1) : GaugeGroupI)⁻¹ = ((1, V⁻¹, 1) : GaugeGroupI)
```

**`StandardModel.toSU3_u1Elt`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L243).

> The colour factor of a hypercharge gauge transformation is trivial.

```lean
lemma toSU3_u1Elt (t : unitary ℂ) :
    GaugeGroupI.toSU3 ((1, 1, t) : GaugeGroupI) = 1
```

**`StandardModel.toSU2_u1Elt`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L247).

> The isospin factor of a hypercharge gauge transformation is trivial.

```lean
lemma toSU2_u1Elt (t : unitary ℂ) :
    GaugeGroupI.toSU2 ((1, 1, t) : GaugeGroupI) = 1
```

**`StandardModel.toU1_u1Elt`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L251).

> The hypercharge factor of a hypercharge gauge transformation.

```lean
lemma toU1_u1Elt (t : unitary ℂ) :
    GaugeGroupI.toU1 ((1, 1, t) : GaugeGroupI) = t
```

**`StandardModel.inv_u1Elt`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L256).

> The inverse of a hypercharge gauge transformation is the hypercharge transformation of
> the inverse.

```lean
lemma inv_u1Elt (t : unitary ℂ) :
    ((1, 1, t) : GaugeGroupI)⁻¹ = ((1, 1, t⁻¹) : GaugeGroupI)
```

**`StandardModel.forall_repGauge_eq_self`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L262).

> A gauge transformation is the product of its colour, isospin and hypercharge parts, so
> an element fixed by each of the three factors separately is gauge invariant.

```lean
lemma forall_repGauge_eq_self {B : Type*} [AddCommGroup B] [Module ℂ B]
    {rep : Representation ℂ GaugeGroupI B} {x : B}
    (h3 : ∀ U : specialUnitaryGroup (Fin 3) ℂ, rep (U, 1, 1) x = x)
    (h2 : ∀ V : specialUnitaryGroup (Fin 2) ℂ, rep (1, V, 1) x = x)
    (h1 : ∀ t : unitary ℂ, rep (1, 1, t) x = x) (g : GaugeGroupI) : rep g x = x
```

## C. Stability of symbol ranges

> The range of a symbol map is carried into itself by the gauge group, and, with no
> derivative slots, by the Lorentz group.

**`StandardModel.isStableUnder_range_repGauge`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L287).

> The range of a symbol map is carried into itself by the gauge group: the symbol is
> equivariant, so a gauge transformation only moves the dual vector it is evaluated at.

```lean
lemma isStableUnder_range_repGauge {M : Type} [AddCommGroup M] [Module ℂ M]
    {repGauge : Representation ℂ GaugeGroupI B} {ρ : Representation ℂ GaugeGroupI M}
    {F : Module.Dual ℂ M →ₗ[ℂ] B} (hF : ∀ g φ, repGauge g (F φ) = F (ρ.dual g φ)) :
    ∀ g : GaugeGroupI, ∀ y ∈ LinearMap.range F, repGauge g y ∈ LinearMap.range F
```

**`StandardModel.isStableUnder_range_repLorentz`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean#L296).

> The range of an underived symbol map is carried into itself by the Lorentz group: with
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

- [PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/InvariantReduction.lean)
