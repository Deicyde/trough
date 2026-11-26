---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.minKindWeight, StandardModel.LocalCovFieldAlgebra.minKindWeight_le, StandardModel.LocalCovFieldAlgebra.sectorMassWeight_mixed_eq_bot_of_lt_nine, StandardModel.LocalCovFieldAlgebra.mem_of_invariant_sectorMassWeight_mixed_lt_nine_sup, StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff, StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem
statement: formalized
proof: formalized
---

# The mixed sector

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.MixedSector.Basic`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean): 6 declarations, 6 with a docstring.

> The gauge-Higgs-fermion sector of the Standard Model's covariant field algebra, at low weight.

## i. Overview

> Everything below is stated about the covariant field algebra `fieldData.LocalCovFieldAlgebra` of the
> Standard Model.
>
> The sector `fieldData.sectorMassWeight {gauge, scalar, fermion} w` of the generic
> `GaugeFieldData.sectorMassWeight` is the home of any term that mixes all three kinds of
> covariant field at once. A field-strength tower carries weight at least `4`, a Higgs (or
> conjugate Higgs) tower weight at least `2`, and a fermion tower weight at least `3`, so a
> product of generators of all three kinds has total weight at least `4 + 2 + 3 = 9`, by
> `GaugeFieldData.sectorMassWeight_eq_bot_of_lt`.
>
> Consequently the mixed sector vanishes identically below weight nine
> (`sectorMassWeight_mixed_eq_bot_of_lt_nine`), in particular at every weight up to
> eight. There is no Standard-Model term of mass dimension at most four (mass
> weight, twice the mass dimension, at most eight) that mixes gauge, Higgs and fermion
> fields together.
>
> Below weight nine, then, there is nothing left to classify. The sector is `⊥`, so an
> element of `⊥ ⊔ S` is an element of `S` outright, whatever `S` may be. Section B records
> that in the shape the other sectors carry, so that the four can later be combined; unlike
> them it asks no stability of `S` and no invariance of the element, there being nothing to
> peel away and no parity or index count to run.

## ii. Key results

> - `minKindWeight` : the minimum mass weight of a generator of each kind.
> - `sectorMassWeight_mixed_eq_bot_of_lt_nine` : the mixed sector vanishes below weight nine.
> - `mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff` : the classification
>   below mass weight nine as an equivalence.

## iv. References

> * None.

## A. The mixed sector vanishes below weight nine

**`StandardModel.LocalCovFieldAlgebra.minKindWeight`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean#L75).

> The minimum mass weight of a covariant generator of each kind in the Standard Model, four
> for the field strength, two for the Higgs and three for the fermions.

```lean
def minKindWeight : FieldKind → ℕ
```

**`StandardModel.LocalCovFieldAlgebra.minKindWeight_le`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean#L82).

> Every covariant generator of the Standard Model has at least the minimum mass weight of its
> kind.

```lean
lemma minKindWeight_le {k : FieldKind} {v : ℕ} {b : fieldData.LocalCovFieldAlgebra}
    (hb : b ∈ fieldData.weightedGenerators k v) : minKindWeight k ≤ v
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeight_mixed_eq_bot_of_lt_nine`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean#L97).

> The mixed sector vanishes below weight nine, since a product of generators of all three kinds
> carries gauge weight at least four, Higgs weight at least two and fermion weight at least
> three, for a total of at least nine. So no such product exists at a lower weight, and the
> sector's span there is trivial.

```lean
lemma sectorMassWeight_mixed_eq_bot_of_lt_nine {w : ℕ} (hw : w < 9) :
    fieldData.sectorMassWeight
      {FieldKind.gauge, FieldKind.scalar, FieldKind.fermion} w = ⊥
```

## B. The classification below weight nine

> Nine is beyond every weight a dimension-four term can reach, so the vanishing of section A settles
> the whole of the mixed sector at a stroke. An element of `⊥ ⊔ S` is an element of `S`. The three
> statements below are those of the gauge and Yukawa sectors, name for name, so that the four sectors
> can be combined uniformly. There the forward direction is an argument — a metric trace, an index
> count, the sign at the centre of `SL(2,ℂ)` — and needs `S` stable and the element invariant; here it
> is the emptiness of the sector, and the invariance conjuncts ride along in the equivalences only to
> keep the shapes matched.

**`StandardModel.LocalCovFieldAlgebra.mem_of_invariant_sectorMassWeight_mixed_lt_nine_sup`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean#L122).

> Below mass weight nine the mixed sector adds nothing to a submodule `S`. An element of
> `fieldData.sectorMassWeight {gauge, scalar, fermion} w ⊔ S` for `w < 9` already lies in `S`. The
> sector is trivial there, so no invariance is asked of `x` and no stability of `S`.

```lean
lemma mem_of_invariant_sectorMassWeight_mixed_lt_nine_sup (w : ℕ) (hw : w < 9)
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar,
      FieldKind.fermion} w ⊔ S) : x ∈ S
```

**`StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean#L133).

> The classification below mass weight nine as an equivalence, in the shape of the
> gauge- and Yukawa-sector statements. An element of
> `fieldData.sectorMassWeight {gauge, scalar, fermion} w ⊔ S` for `w < 9` is fixed by both groups
> exactly when it is itself an element of `S` fixed by both groups. Neither stability
> hypothesis on `S` is needed, the forward direction being the vanishing of the sector.

```lean
lemma mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff (w : ℕ)
    (hw : w < 9) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar,
          FieldKind.fermion} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x) ∧ ∀ g : SL(2,ℂ),
          repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x = y
```

**`StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean#L153).

> The same classification without the existential. Below mass weight nine an element of
> `fieldData.sectorMassWeight {gauge, scalar, fermion} w ⊔ S` fixed by both groups is an element of
> `S` fixed by both groups, and conversely.

```lean
lemma mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw : w < 9) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar,
          FieldKind.fermion} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x) ∧ ∀ g : SL(2,ℂ),
          repLorentzGroup g x = x)
      ↔ (x ∈ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
```

## Depends on

- [The sectors of a gauge field theory](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-localcovfieldalgebra-sector.md)
- [The covariant field algebra of the Standard Model](localfieldalgebra-localcovfieldalgebra-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/MixedSector/Basic.lean)
