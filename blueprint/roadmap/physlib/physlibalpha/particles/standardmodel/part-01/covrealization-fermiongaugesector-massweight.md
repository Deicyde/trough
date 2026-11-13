---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.mem_of_lorentz_invariant_sectorMassWeight_gauge_fermion_seven_sup, StandardModel.CovAlgebraRealization.mem_of_invariant_sectorMassWeight_gauge_fermion_lt_nine_sup, StandardModel.CovAlgebraRealization.mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff, StandardModel.CovAlgebraRealization.mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem
statement: formalized
proof: formalized
---

# The gauge-fermion invariants below mass weight nine

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.FermionGaugeSector.MassWeight`, [PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/MassWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/MassWeight.lean): 4 declarations, 4 with a docstring; 1 private, not shown.

## i. Overview

> The mixed `{gauge, fermion}` sector is almost empty below weight nine, and what little
> there is cannot be invariant. A field-strength tower weighs at least four and a fermion
> tower at least three, so the sector vanishes below weight seven; at weight eight the two
> splittings that arithmetic allows are `4 + 4` and `6 + 2`, and the fermion sector is
> trivial at both four and two, so weight eight vanishes too. That leaves weight seven, the
> single product `F ψ` of the underived field strength against the underived fermion towers.
>
> Weight seven is barred from carrying an invariant by the same parity count on spin that
> empties the Yukawa sector at weights five and seven. The field strength is of integer spin,
> its two covector indices and its derivative slots all mixing by the Lorentz matrix and its
> adjoint index not seeing the Lorentz group at all, while a fermion carries one Weyl-spinor
> index. The one product at weight seven has exactly one fermion factor, so it is of
> half-integer spin; and a half-integer spin carries no Lorentz invariant.
>
> The machinery is the Yukawa sector's: `mul_le_centreEigenspace` multiplies the signs the
> two factors carry at the centre of `SL(2,ℂ)`, and
> `mem_of_invariant_of_mem_sup_centreEigenspace_neg_one` turns the sign `-1` into the absence
> of invariants modulo a Lorentz-stable submodule. Only the left-hand factor changes: the
> Higgs sign `+1` is replaced by the gauge one, which is `+1` for the same reason.
>
>
> The bound is `w < 9` rather than `w < 8`: weight eight is as empty as the weights below
> seven, so nothing is gained by stopping short of the first weight the sector can occupy.

## ii. Key results

> - `gaugeFermion_le_centreEigenspace` : a field-strength derivative submodule against a fermion one
>   is of half-integer spin: `+1` times `-1`
> - `mem_of_lorentz_invariant_sectorMassWeight_gauge_fermion_seven_sup`
> - `mem_of_invariant_sectorMassWeight_gauge_fermion_lt_nine_sup`
> - `mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff` : the
>   classification below mass weight nine as an equivalence, in the shape of the gauge- and
>   Yukawa-sector statements: an element of `sectorMassWeight {gauge, fermion} w ⊔ S` for `w < 9` is
>   fixed by both groups exactly when it is itself an element of `S` fixed by both groups

## iv. References

> * None.

## A. Integer field strength against half-integer fermion

> The signs the two factors carry at the centre are already proved: the field-strength
> derivative submodules carry `+1`, every one of their indices being inert there, and the
> fermion ones carry `-1`, the Weyl-spinor value index doing the work. The Lorentz action on
> `B` is by algebra maps, so the product carries `+1` times `-1`.

## B. Mass weight seven

> Weight seven is the single product `F ψ`, the underived field strength against the
> underived fermion towers. It has exactly one fermion factor, so section A gives it the sign
> `-1`, and a subspace of sign `-1` carries no invariant modulo a Lorentz-stable submodule.

**`StandardModel.CovAlgebraRealization.mem_of_lorentz_invariant_sectorMassWeight_gauge_fermion_seven_sup`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/MassWeight.lean#L111).

> Mass weight seven carries no Lorentz invariant modulo a Lorentz-stable submodule: a
> Lorentz invariant of `sectorMassWeight {gauge, fermion} 7 ⊔ S` lies in `S`. The weight is
> the underived field strength against the underived fermion towers, of half-integer
> spin.

```lean
lemma mem_of_lorentz_invariant_sectorMassWeight_gauge_fermion_seven_sup (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.fermion} 7 ⊔ S)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## C. The classification below mass weight nine

> The nine weights below nine are now settled: the sector vanishes below weight seven and
> again at weight eight, and weight seven is section B. So below weight nine the
> gauge-fermion sector supplies no invariant beyond what `S` already carries, and the
> equivalences record it in the shape the other sectors carry, so that all of them can be
> combined.
>
> No lower bound on the weight is needed. The sector is the two-class sector of the gauge
> and fermion generators, so both classes must be present with a non-zero weight and the
> sector is already trivial at weight zero; the scalars, which force `0 < w` in the
> gauge-sector statement, never appear.

**`StandardModel.CovAlgebraRealization.mem_of_invariant_sectorMassWeight_gauge_fermion_lt_nine_sup`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/MassWeight.lean#L140).

> Below mass weight nine the gauge-fermion sector carries no Lorentz invariant: a
> Lorentz invariant of `sectorMassWeight {gauge, fermion} w ⊔ S` for `w < 9` lies in `S`.
> Weights below seven and weight eight are trivial submodules, and weight seven is section
> B.

```lean
lemma mem_of_invariant_sectorMassWeight_gauge_fermion_lt_nine_sup (w : ℕ) (hw : w < 9)
    (S : Submodule ℂ B) (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.fermion} w ⊔ S)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.CovAlgebraRealization.mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/MassWeight.lean#L156).

> The classification below mass weight nine as an equivalence, in the shape of the gauge-
> and Yukawa-sector statements: an element of `sectorMassWeight {gauge, fermion} w ⊔ S` for
> `w < 9` is fixed by both groups exactly when it is itself an element of `S` fixed by both
> groups. Gauge stability of `S` is not needed, and neither is gauge invariance of `x`: the
> forward direction is the boost-weight parity argument, which uses the Lorentz group
> alone.

```lean
lemma mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff
    (w : ℕ) (hw : w < 9) (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.fermion} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGauge g x = x) ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x = y
```

**`StandardModel.CovAlgebraRealization.mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/MassWeight.lean#L174).

> The same classification without the existential: below mass weight nine an element of
> `sectorMassWeight {gauge, fermion} w ⊔ S` fixed by both groups is an element of `S` fixed
> by both groups, and conversely.

```lean
lemma mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem
    (w : ℕ) (hw : w < 9) (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.fermion} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGauge g x = x) ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

## Depends on

- [The sectors of the field algebra](covrealization-sectors.md)

## Proof depends on

- [The mixed gauge-fermion sector](covrealization-fermiongaugesector-basic.md)
- [The centre of `SL(2,ℂ)` on the fermion sector](../part-05/isfermionsector-deriv-centre.md)
- [The centre of `SL(2,ℂ)` on the gauge sector](../part-06/isgaugesector-deriv-centre.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/MassWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/MassWeight.lean)
