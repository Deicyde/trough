---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra, StandardModel.CovAlgebraRealization.fermionMassWeight_mul_gaugeMassWeight_le, StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_fermion_le, StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven, StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_fermion_eight, StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_fermion_seven
statement: formalized
proof: formalized
---

# The mixed gauge-fermion sector

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.FermionGaugeSector.Basic`, [PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean): 6 declarations, 6 with a docstring.

## i. Overview

> The field-strength towers are bosonic, so they commute with every fermion tower
> (`h.F_comm_d`, `h.F_comm_bard`, ..., `h.F_comm_bare`); consequently the gauge algebra
> and the fermion algebra commute (`commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra`),
> and so do their mass-weight submodules in either order
> (`fermionMassWeight_mul_gaugeMassWeight_le`). Feeding this into the abstract two-class
> sector bound `sectorMassWeight_pair_le` gives the mixed `{gauge, fermion}` sector's
> weight-`w` piece as (the join over splittings of `w` into non-zero parts of) products
> of the gauge and fermion sectors' own mass-weight submodules
> (`sectorMassWeight_gauge_fermion_le`).
>
> Since a non-zero gauge weight is at least `4` and a non-zero fermion weight is at
> least `3`, the mixed sector vanishes below weight `7`
> (`sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven`) and at weight `8`
> (`sectorMassWeight_gauge_fermion_eight`), and at weight `7` is exactly the product of
> the underived field-strength submodule with the underived fermion submodule
> (`sectorMassWeight_gauge_fermion_seven`).

## ii. Key results

> - `commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra` : the gauge algebra and the fermion algebra
>   commute element-wise: every generator of the gauge algebra commutes with every generator of the
>   fermion algebra by the structure fields `h.F_comm_d`,
> - `fermionMassWeight_mul_gaugeMassWeight_le` : the fermion sector's mass-weight submodules and the
>   gauge sector's mass-weight submodules commute past each other, in the order needed by
>   `sectorMassWeight_pair_le`
> - `sectorMassWeight_gauge_fermion_le` : the mixed gauge-fermion sector decomposition
> - `sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven` : the mixed gauge-fermion sector vanishes
>   below weight `7`
> - `sectorMassWeight_gauge_fermion_eight` : the mixed gauge-fermion sector vanishes at weight `8`
> - `sectorMassWeight_gauge_fermion_seven` : the mixed gauge-fermion sector at weight `7` is exactly
>   the product of the underived field-strength submodule with the underived fermion submodule: the
>   only splitting of `7` into a non-zero gauge weight and a non-zero fermion weight that survives is
>   `4 + 3`

## iv. References

> * None.

## A. The gauge and fermion algebras commute

**`StandardModel.CovAlgebraRealization.commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean#L84).

> The gauge algebra and the fermion algebra commute element-wise: every generator of
> the gauge algebra commutes with every generator of the fermion algebra by the
> structure fields `h.F_comm_d`, ..., `h.F_comm_bare`, and commutation extends from
> generators to the algebras they generate.

```lean
lemma commute_of_mem_gaugeAlgebra_of_mem_fermionAlgebra {x y : B}
    (hx : x ∈ h.isGaugeSector.gaugeAlgebra) (hy : y ∈ h.isFermionSector.fermionAlgebra) :
    Commute x y
```

**`StandardModel.CovAlgebraRealization.fermionMassWeight_mul_gaugeMassWeight_le`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean#L120).

> The fermion sector's mass-weight submodules and the gauge sector's mass-weight
> submodules commute past each other, in the order needed by
> `sectorMassWeight_pair_le`.

```lean
lemma fermionMassWeight_mul_gaugeMassWeight_le (a b : ℕ) :
    h.isFermionSector.massWeightSubmodule a * h.isGaugeSector.massWeightSubmodule b
      ≤ h.isGaugeSector.massWeightSubmodule b * h.isFermionSector.massWeightSubmodule a
```

## B. The mixed gauge-fermion sector

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_fermion_le`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean#L139).

> **The mixed gauge-fermion sector decomposition.** The weight-`w` piece of the
> `{gauge, fermion}` sector lies in the join, over the splittings of `w` into two
> non-zero parts, of the products of the gauge and fermion sectors' own mass-weight
> submodules.

```lean
lemma sectorMassWeight_gauge_fermion_le (w : ℕ) :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.fermion} w
      ≤ ⨆ (p : ℕ × ℕ) (_ : p.1 + p.2 = w) (_ : p.1 ≠ 0) (_ : p.2 ≠ 0),
        h.isGaugeSector.massWeightSubmodule p.1 * h.isFermionSector.massWeightSubmodule p.2
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean#L156).

> **The mixed gauge-fermion sector vanishes below weight `7`.** A non-zero gauge
> weight is at least `4` and a non-zero fermion weight is at least `3`, so no
> splitting of a weight below `7` into two non-zero parts can supply both.

```lean
lemma sectorMassWeight_gauge_fermion_eq_bot_of_lt_seven {w : ℕ} (hw : w < 7) :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.fermion} w = ⊥
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_fermion_eight`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean#L179).

> **The mixed gauge-fermion sector vanishes at weight `8`.** The only splittings of
> `8` into two non-zero parts with a non-zero gauge weight and a non-zero fermion
> weight would need the gauge part to be `4` or `6`(with fermion part `4` or `2`), but
> the fermion sector vanishes at both `4` and `2`.

```lean
lemma sectorMassWeight_gauge_fermion_eight :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.fermion} 8 = ⊥
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_fermion_seven`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean#L203).

> **The mixed gauge-fermion sector at weight `7`** is exactly the product of the
> underived field-strength submodule with the underived fermion submodule: the only
> splitting of `7` into a non-zero gauge weight and a non-zero fermion weight that
> survives is `4 + 3`.

```lean
lemma sectorMassWeight_gauge_fermion_seven :
    h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.fermion} 7
      = h.isGaugeSector.derivSubmodule 0 * h.isFermionSector.derivSubmodule 0
```

## Depends on

- [The sectors of the field algebra](covrealization-sectors.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/FermionGaugeSector/Basic.lean)
