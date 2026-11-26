---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.mem_of_lorentz_invariant_sectorMassWeight_gauge_fermion_seven_sup, StandardModel.LocalCovFieldAlgebra.mem_of_invariant_sectorMassWeight_gauge_fermion_lt_nine_sup, StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff, StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem
statement: formalized
proof: formalized
---

# The gauge-fermion invariants below mass weight nine

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionGaugeSector.MassWeight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/MassWeight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/MassWeight.lean): 4 declarations, 4 with a docstring; 1 private, not shown.

> The gauge-fermion sector of the Standard Model's covariant field algebra carries no invariant.

## i. Overview

> Everything below is stated about the covariant field algebra `fieldData.LocalCovFieldAlgebra` of the
> Standard Model.
>
> The mixed `{gauge, fermion}` sector is almost empty below weight nine, and what little
> there is cannot be invariant. A field-strength tower weighs at least four and a fermion
> tower at least three, so the sector vanishes below weight seven. At weight eight the two
> splittings that arithmetic allows are `4 + 4` and `6 + 2`, and the fermion sector is
> trivial at both four and two, so weight eight vanishes too. That leaves weight seven, the
> single product `F ψ` of the underived field strength against the underived fermion towers.
>
> Weight seven is barred from carrying an invariant by the same parity count on spin that
> empties the Yukawa sector at weights five and seven. The field strength is of integer spin,
> its two covector indices and its derivative slots all mixing by the Lorentz matrix and its
> adjoint index not seeing the Lorentz group at all, while a fermion carries one Weyl-spinor
> index. The one product at weight seven has exactly one fermion factor, so it is of
> half-integer spin, and a half-integer spin carries no Lorentz invariant.
>
> The machinery is the Yukawa sector's: `mul_le_centreEigenspace` multiplies the signs the
> two factors carry at the centre of `SL(2,ℂ)`, and
> `mem_of_invariant_of_mem_sup_centreEigenspace_neg_one` turns the sign `-1` into the absence
> of invariants modulo a Lorentz-stable submodule. Only the left-hand factor changes. The
> Higgs sign `+1` is replaced by the gauge one, which is `+1` for the same reason.
>
> The bound is `w < 9` rather than `w < 8`, since weight eight is as empty as the weights below
> seven, so nothing is gained by stopping short of the first weight the sector can occupy.

## ii. Key results

> - `mem_of_lorentz_invariant_sectorMassWeight_gauge_fermion_seven_sup` : mass weight seven carries
>   no Lorentz invariant, being of half-integer spin.
> - `mem_of_invariant_sectorMassWeight_gauge_fermion_lt_nine_sup` : below mass weight nine the
>   sector carries no Lorentz invariant.
> - `mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff` : the
>   classification below mass weight nine as an equivalence. An element of
>   `fieldData.sectorMassWeight {gauge, fermion} w ⊔ S` for `w < 9` is fixed by both groups exactly
>   when it is itself an element of `S` fixed by both groups.

## iv. References

> * None.

## A. Integer field strength against half-integer fermion

> The signs the two factors carry at the centre are already proved: the field-strength
> derivative submodules carry `+1`, every one of their indices being inert there, and the
> fermion ones carry `-1`, the Weyl-spinor value index doing the work. The Lorentz action on
> the covariant field algebra is by algebra maps, so the product carries `+1` times `-1`.

## B. Mass weight seven

> Weight seven is the single product `F ψ`, the underived field strength against the
> underived fermion towers. It has exactly one fermion factor, so section A gives it the sign
> `-1`, and a subspace of sign `-1` carries no invariant modulo a Lorentz-stable submodule.

**`StandardModel.LocalCovFieldAlgebra.mem_of_lorentz_invariant_sectorMassWeight_gauge_fermion_seven_sup`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/MassWeight.lean#L111).

> Mass weight seven carries no Lorentz invariant modulo a Lorentz-stable submodule. A
> Lorentz invariant of `fieldData.sectorMassWeight {gauge, fermion} 7 ⊔ S` lies in `S`. The
> weight is the underived field strength against the underived fermion towers, of half-integer
> spin.

```lean
lemma mem_of_lorentz_invariant_sectorMassWeight_gauge_fermion_seven_sup
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.fermion} 7
      ⊔ S)
    (hL : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) : x ∈ S
```

## C. The classification below mass weight nine

> The nine weights below nine are now settled. The sector vanishes below weight seven and
> again at weight eight, and weight seven is section B. So below weight nine the
> gauge-fermion sector supplies no invariant beyond what `S` already carries, and the
> equivalences record it in the shape the other sectors carry, so that all of them can be
> combined.
>
> No lower bound on the weight is needed. The sector is the two-class sector of the gauge
> and fermion generators, so both classes must be present with a non-zero weight and the
> sector is already trivial at weight zero. The scalars, which force `0 < w` in the
> gauge-sector statement, never appear.

**`StandardModel.LocalCovFieldAlgebra.mem_of_invariant_sectorMassWeight_gauge_fermion_lt_nine_sup`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/MassWeight.lean#L142).

> Below mass weight nine the gauge-fermion sector carries no Lorentz invariant. A
> Lorentz invariant of `fieldData.sectorMassWeight {gauge, fermion} w ⊔ S` for `w < 9` lies in `S`.
> Weights below seven and weight eight are trivial submodules, and weight seven is section
> B.

```lean
lemma mem_of_invariant_sectorMassWeight_gauge_fermion_lt_nine_sup (w : ℕ) (hw : w < 9)
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y
      ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.fermion} w
      ⊔ S)
    (hL : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) : x ∈ S
```

**`StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/MassWeight.lean#L163).

> The classification below mass weight nine as an equivalence, in the shape of the gauge-
> and Yukawa-sector statements. An element of
> `fieldData.sectorMassWeight {gauge, fermion} w ⊔ S` for `w < 9` is fixed by both groups
> exactly when it is itself an element of `S` fixed by both groups. Gauge stability of `S` is
> not needed, and neither is gauge invariance of `x`, since the forward direction is the sign at
> the centre of `SL(2,ℂ)`, which uses the Lorentz group alone.

```lean
lemma mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff
    (w : ℕ) (hw : w < 9) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.fermion} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x) ∧ ∀ g : SL(2,ℂ),
          repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x = y
```

**`StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/MassWeight.lean#L183).

> The same classification without the existential. Below mass weight nine an element of
> `fieldData.sectorMassWeight {gauge, fermion} w ⊔ S` fixed by both groups is an element of
> `S` fixed by both groups, and conversely.

```lean
lemma mem_sectorMassWeight_gauge_fermion_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem
    (w : ℕ) (hw : w < 9) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.fermion} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x) ∧ ∀ g : SL(2,ℂ),
          repLorentzGroup g x = x)
      ↔ (x ∈ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
```

## Depends on

- [The sectors of a gauge field theory](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-localcovfieldalgebra-sector.md)
- [The covariant field algebra of the Standard Model](../part-05/localfieldalgebra-localcovfieldalgebra-basic.md)

## Proof depends on

- [The mixed gauge-fermion sector](localfieldalgebra-fermiongaugesector-basic.md)
- [The centre of `SL(2,ℂ)` on the fermion sector](../part-03/localfieldalgebra-fermionsector-deriv-centre.md)
- [The centre of `SL(2,ℂ)` on the gauge sector](../part-04/localfieldalgebra-gaugesector-deriv-centre.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/MassWeight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionGaugeSector/MassWeight.lean)
