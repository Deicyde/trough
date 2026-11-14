---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.sectorMassWeight_mixed_eq_bot_of_lt_nine, StandardModel.CovAlgebraRealization.sectorMassWeight_mixed_eight, StandardModel.CovAlgebraRealization.mem_of_invariant_sectorMassWeight_mixed_lt_nine_sup, StandardModel.CovAlgebraRealization.mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff, StandardModel.CovAlgebraRealization.mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem
statement: formalized
proof: formalized
---

# The mixed sector

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.MixedSector.Basic`, [PhyslibAlpha/Particles/StandardModel/CovRealization/MixedSector/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MixedSector/Basic.lean): 5 declarations, 5 with a docstring.

## i. Overview

> The `{gauge, higgs, fermion}` three-class sector of `Sectors.lean` is the home of any
> term that mixes all three kinds of covariant field at once. Its words are the least
> weighty of any two- or three-class sector: a field-strength tower carries weight at
> least `4`, a Higgs (or conjugate Higgs) tower weight at least `2`, and a fermion tower
> weight at least `3`, so a word realising all three classes has total weight at least
> `4 + 2 + 3 = 9`.
>
> Consequently the mixed sector vanishes identically below weight nine
> (`sectorMassWeight_mixed_eq_bot_of_lt_nine`) — in particular at every weight up to
> eight, i.e. there is no Standard-Model term of mass dimension at most four (mass
> weight, twice the mass dimension, at most eight) that mixes gauge, Higgs and fermion
> fields together.
>
> Below weight nine, then, there is nothing left to classify. The sector is `⊥`, so an
> element of `⊥ ⊔ S` is an element of `S` outright, whatever `S` may be. Section B records
> that in the shape the other sectors carry, so that the four can later be combined; unlike
> them it asks no stability of `S` and no invariance of the element, there being nothing to
> peel away and no parity or index count to run.

## ii. Key results

> - `sectorMassWeight_mixed_eq_bot_of_lt_nine` : the mixed sector vanishes below weight nine: a word
>   realising all three classes carries gauge weight at least four, Higgs weight at least two and
>   fermion weight at least three, for a total of at least nine — so no such word exists at a lower
>   weight, and the sector's span there is trivial

## iv. References

> * None.

## A. The mixed sector vanishes below weight nine

**`StandardModel.CovAlgebraRealization.sectorMassWeight_mixed_eq_bot_of_lt_nine`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MixedSector/Basic.lean#L76).

> The mixed sector vanishes below weight nine: a word realising all three
> classes carries gauge weight at least four, Higgs weight at least two and fermion
> weight at least three, for a total of at least nine — so no such word exists at a
> lower weight, and the sector's span there is trivial.

```lean
lemma sectorMassWeight_mixed_eq_bot_of_lt_nine {w : ℕ} (hw : w < 9) :
    h.sectorMassWeight
      {GeneratorClass.gauge, GeneratorClass.higgs, GeneratorClass.fermion} w = ⊥
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_mixed_eight`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MixedSector/Basic.lean#L94).

> The weight-eight mixed sector vanishes: the mass weight of a dimension-four
> Standard-Model term is at most eight, and the mixed sector is trivial there — no
> dimension-four term mixes gauge, Higgs and fermion fields together.

```lean
lemma sectorMassWeight_mixed_eight :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs, GeneratorClass.fermion} 8
      = ⊥
```

## B. The classification below weight nine

> Nine is beyond every weight a dimension-four term can reach, so the vanishing of section A
> settles the whole of the mixed sector at a stroke: an element of `⊥ ⊔ S` is an element of
> `S`. The three statements below are those of the gauge and Yukawa sectors, name for name,
> so that the four sectors can be combined uniformly. There the forward direction is an
> argument — a metric trace, an index count, a boost-weight parity — and needs `S` stable
> and the element invariant; here it is the emptiness of the sector, and the invariance
> conjuncts ride along in the equivalences only to keep the shapes matched.

**`StandardModel.CovAlgebraRealization.mem_of_invariant_sectorMassWeight_mixed_lt_nine_sup`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MixedSector/Basic.lean#L116).

> Below mass weight nine the mixed sector adds nothing to a submodule `S`: an element of
> `sectorMassWeight {gauge, higgs, fermion} w ⊔ S` for `w < 9` already lies in `S`. The
> sector is trivial there, so no invariance is asked of `x` and no stability of `S`.

```lean
lemma mem_of_invariant_sectorMassWeight_mixed_lt_nine_sup (w : ℕ) (hw : w < 9)
    (S : Submodule ℂ B) {x : B}
    (hx : x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs,
      GeneratorClass.fermion} w ⊔ S) : x ∈ S
```

**`StandardModel.CovAlgebraRealization.mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MixedSector/Basic.lean#L127).

> The classification below mass weight nine as an equivalence, in the shape of the
> gauge- and Yukawa-sector statements: an element of
> `sectorMassWeight {gauge, higgs, fermion} w ⊔ S` for `w < 9` is fixed by both groups
> exactly when it is itself an element of `S` fixed by both groups. Neither stability
> hypothesis on `S` is needed, the forward direction being the vanishing of the sector.

```lean
lemma mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff (w : ℕ)
    (hw : w < 9) (S : Submodule ℂ B) (x : B) :
    (x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs,
          GeneratorClass.fermion} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGauge g x = x) ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x = y
```

**`StandardModel.CovAlgebraRealization.mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MixedSector/Basic.lean#L144).

> The same classification without the existential: below mass weight nine an element of
> `sectorMassWeight {gauge, higgs, fermion} w ⊔ S` fixed by both groups is an element of
> `S` fixed by both groups, and conversely.

```lean
lemma mem_sectorMassWeight_mixed_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw : w < 9) (S : Submodule ℂ B) (x : B) :
    (x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs,
          GeneratorClass.fermion} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGauge g x = x) ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

## Depends on

- [The sectors of the field algebra](../part-01/covrealization-sectors.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/MixedSector/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MixedSector/Basic.lean)
