---
declaration: module
origin: cited
lean: StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightOne, StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightTwo, StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightThree, StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightFour, StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightFive, StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightSix, StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightSeven, StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightEight
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the fermion mass-weight submodules

The module `PhyslibAlpha.Particles.StandardModel.IsFermionSector.MassWeight.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean): 42 declarations, 42 with a docstring.

## i. Overview

> Each mass-weight submodule of the fermion sector up to weight eight has an explicit
> description in terms of the derivative submodules, and the derivative submodules carry
> a gauge weight decomposition.  Transporting the latter along the former decomposes
> every mass-weight submodule up to weight eight: weights one, two and four are trivial,
> weights three, five and seven are the towers with zero, one and two covariant
> derivatives, weight six is the product of two underived towers, and weight eight is the
> kinetic sector.

## ii. Key results

> - `massWeightSubmoduleGaugeWeightOne` : weight one is trivial
> - `massWeightSubmoduleGaugeWeightTwo` : weight two is trivial
> - `massWeightSubmoduleGaugeWeightThree` : weight three is the underived fermion towers
> - `massWeightSubmoduleGaugeWeightFour` : weight four is trivial

## iv. References

> * None.

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightOne`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L77).

> Weight one is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightOne :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 1)
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightTwo`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L84).

> Weight two is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightTwo :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 2)
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightThree`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L91).

> Weight three is the underived fermion towers.

```lean
noncomputable def massWeightSubmoduleGaugeWeightThree :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 3)
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightFour`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L98).

> Weight four is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightFour :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 4)
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightFive`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L105).

> Weight five is the once-derived fermion towers.

```lean
noncomputable def massWeightSubmoduleGaugeWeightFive :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 5)
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightSix`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L112).

> Weight six is the products of two underived fermion towers.

```lean
noncomputable def massWeightSubmoduleGaugeWeightSix :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 6)
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightSeven`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L120).

> Weight seven is the twice-derived fermion towers.

```lean
noncomputable def massWeightSubmoduleGaugeWeightSeven :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 7)
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightEight`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L127).

> Weight eight is the kinetic sector: an underived tower against a once-derived one.

```lean
noncomputable def massWeightSubmoduleGaugeWeightEight :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 8)
```

## A. The weight-zero pieces

**`StandardModel.IsFermionSector.zero_not_mem_fermionGaugeWeights`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L143).

> Every gauge weight carried by a fermion symbol has nonzero hypercharge: each of the
> ten species has a fixed nonzero hypercharge, independent of colour, isospin and
> family, and the barred species carry the negative of the unbarred one. So the zero
> weight never occurs.

```lean
lemma zero_not_mem_fermionGaugeWeights : (0 : GaugeWeight) ∉ fermionGaugeWeights
```

**`StandardModel.IsFermionSector.derivSubmoduleGaugeWeight_piece_zero`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L151).

> The weight-zero piece of the fermion derivative submodules is trivial: unlike
> the gauge sector, no single fermion symbol is a gauge singlet, since every one of the
> ten species carries a fixed nonzero hypercharge. A gauge-invariant combination needs
> at least two fermion insertions, which is why it is the mass weights six and eight,
> the products of two towers, that carry the interesting weight-zero content.

```lean
lemma derivSubmoduleGaugeWeight_piece_zero (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).piece 0 = ⊥
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightOne_piece_zero`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L157).

> The weight-zero piece at mass weight 1: the submodule itself is trivial.

```lean
lemma massWeightSubmoduleGaugeWeightOne_piece_zero :
    (h.massWeightSubmoduleGaugeWeightOne).piece 0 = ⊥
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightTwo_piece_zero`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L161).

> The weight-zero piece at mass weight 2: the submodule itself is trivial.

```lean
lemma massWeightSubmoduleGaugeWeightTwo_piece_zero :
    (h.massWeightSubmoduleGaugeWeightTwo).piece 0 = ⊥
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightThree_piece_zero`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L166).

> The weight-zero piece at mass weight three: the underived fermion towers carry no
> gauge singlet, since every fermion symbol has nonzero hypercharge.

```lean
lemma massWeightSubmoduleGaugeWeightThree_piece_zero :
    (h.massWeightSubmoduleGaugeWeightThree).piece 0 = ⊥
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightFour_piece_zero`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L171).

> The weight-zero piece at mass weight 4: the submodule itself is trivial.

```lean
lemma massWeightSubmoduleGaugeWeightFour_piece_zero :
    (h.massWeightSubmoduleGaugeWeightFour).piece 0 = ⊥
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightFive_piece_zero`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L176).

> The weight-zero piece at mass weight five: the once-derived fermion towers carry no
> gauge singlet, since every fermion symbol has nonzero hypercharge.

```lean
lemma massWeightSubmoduleGaugeWeightFive_piece_zero :
    (h.massWeightSubmoduleGaugeWeightFive).piece 0 = ⊥
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightSeven_piece_zero`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L182).

> The weight-zero piece at mass weight seven: the twice-derived fermion towers carry
> no gauge singlet, since every fermion symbol has nonzero hypercharge.

```lean
lemma massWeightSubmoduleGaugeWeightSeven_piece_zero :
    (h.massWeightSubmoduleGaugeWeightSeven).piece 0 = ⊥
```

### A.1. Infrastructure for the product weights six and eight

> Mass weights six and eight are products of two fermion towers, and their weight-zero
> piece is genuinely nontrivial: it is spanned by pairing each species with its own
> conjugate (a mass term). Splitting the product decomposition down to the ten species
> and discarding the non-conjugate pairings, whose hypercharges never cancel, takes the
> infrastructure developed here.

**`StandardModel.IsFermionSector.piece_sup_mul`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L200).

> If the left factor of a product decomposition is a join `VA ⊔ VB`, its weight-`w`
> piece splits along the join.

```lean
lemma piece_sup_mul {VA VB VC : Submodule ℂ B}
    (dA : GaugeWeightDecomposition repGauge VA) (dB : GaugeWeightDecomposition repGauge VB)
    (dC : GaugeWeightDecomposition repGauge VC) (w : GaugeWeight) :
    (GaugeWeightDecomposition.mul (d := GaugeWeightDecomposition.sup (d := dA) (d' := dB))
        (d' := dC)).piece w
      = (GaugeWeightDecomposition.mul (d := dA) (d' := dC)).piece w
        ⊔ (GaugeWeightDecomposition.mul (d := dB) (d' := dC)).piece w
```

**`StandardModel.IsFermionSector.piece_mul_sup`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L216).

> If the right factor of a product decomposition is a join `VA ⊔ VB`, its weight-`w`
> piece splits along the join.

```lean
lemma piece_mul_sup {VA VB VC : Submodule ℂ B}
    (dC : GaugeWeightDecomposition repGauge VC) (dA : GaugeWeightDecomposition repGauge VA)
    (dB : GaugeWeightDecomposition repGauge VB) (w : GaugeWeight) :
    (GaugeWeightDecomposition.mul (d := dC)
        (d' := GaugeWeightDecomposition.sup (d := dA) (d' := dB))).piece w
      = (GaugeWeightDecomposition.mul (d := dC) (d' := dA)).piece w
        ⊔ (GaugeWeightDecomposition.mul (d := dC) (d' := dB)).piece w
```

**`StandardModel.IsFermionSector.mul_piece_zero_eq_bot_of_hypercharge`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L233).

> Two decompositions with constant, non-cancelling hypercharge across their whole
> supports have a trivial product at weight zero: a weight from one can never cancel
> a weight from the other.

```lean
lemma mul_piece_zero_eq_bot_of_hypercharge {V V' : Submodule ℂ B}
    {dV : GaugeWeightDecomposition repGauge V} {dV' : GaugeWeightDecomposition repGauge V'}
    {hc hc' : ℤ} (hV : ∀ w ∈ dV.supp, w.2.2.2 = hc) (hV' : ∀ w ∈ dV'.supp, w.2.2.2 = hc')
    (hne : hc + hc' ≠ 0) :
    (GaugeWeightDecomposition.mul (d := dV) (d' := dV')).piece 0 = ⊥
```

**`StandardModel.IsFermionSector.rangeGaugeWeightD_hc`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L254).

> The `d` symbols carry hypercharge `2` (the negative of the down-singlet's `-2`),
> independent of colour and family.

```lean
lemma rangeGaugeWeightD_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightD f l).supp, w.2.2.2 = 2
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarD_hc`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L263).

> The `bard` symbols carry hypercharge `-2`, independent of colour and family.

```lean
lemma rangeGaugeWeightBarD_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightBarD f l).supp, w.2.2.2 = -2
```

**`StandardModel.IsFermionSector.rangeGaugeWeightU_hc`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L272).

> The `u` symbols carry hypercharge `-4`, independent of colour and family.

```lean
lemma rangeGaugeWeightU_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightU f l).supp, w.2.2.2 = -4
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarU_hc`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L281).

> The `baru` symbols carry hypercharge `4`, independent of colour and family.

```lean
lemma rangeGaugeWeightBarU_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightBarU f l).supp, w.2.2.2 = 4
```

**`StandardModel.IsFermionSector.rangeGaugeWeightQ_hc`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L291).

> The `Q` symbols carry hypercharge `-1`, independent of colour, isospin and
> family.

```lean
lemma rangeGaugeWeightQ_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightQ f l).supp, w.2.2.2 = -1
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarQ_hc`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L301).

> The `barQ` symbols carry hypercharge `1`, independent of colour, isospin and
> family.

```lean
lemma rangeGaugeWeightBarQ_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightBarQ f l).supp, w.2.2.2 = 1
```

**`StandardModel.IsFermionSector.rangeGaugeWeightL_hc`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L310).

> The `L` symbols carry hypercharge `3`, independent of isospin and family.

```lean
lemma rangeGaugeWeightL_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightL f l).supp, w.2.2.2 = 3
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarL_hc`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L319).

> The `barL` symbols carry hypercharge `-3`, independent of isospin and family.

```lean
lemma rangeGaugeWeightBarL_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightBarL f l).supp, w.2.2.2 = -3
```

**`StandardModel.IsFermionSector.rangeGaugeWeightE_hc`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L328).

> The `e` symbols carry hypercharge `6`, independent of family.

```lean
lemma rangeGaugeWeightE_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightE f l).supp, w.2.2.2 = 6
```

**`StandardModel.IsFermionSector.rangeGaugeWeightBarE_hc`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L337).

> The `bare` symbols carry hypercharge `-6`, independent of family.

```lean
lemma rangeGaugeWeightBarE_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (h.rangeGaugeWeightBarE f l).supp, w.2.2.2 = -6
```

**`StandardModel.IsFermionSector.speciesGaugeWeight`**, a def, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L349).

> The gauge weight decomposition of one family's full set of symbols at fixed
> derivative slots, matching the recipe of `derivSubmodule` itself: the join of the
> ten species' ranges.

```lean
noncomputable def speciesGaugeWeight (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    GaugeWeightDecomposition repGauge
      (LinearMap.range (d f l) ⊔ LinearMap.range (bard f l) ⊔
        LinearMap.range (u f l) ⊔ LinearMap.range (baru f l) ⊔
        LinearMap.range (Q f l) ⊔ LinearMap.range (barQ f l) ⊔
        LinearMap.range (L f l) ⊔ LinearMap.range (barL f l) ⊔
        LinearMap.range (e f l) ⊔ LinearMap.range (bare f l))
```

**`StandardModel.IsFermionSector.speciesGaugeWeight_mul_piece_zero`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L378).

> The weight-zero piece of the product of two families' full symbol sets collapses
> to the ten conjugate pairings: every other combination of species has hypercharges
> that cannot cancel.

```lean
lemma speciesGaugeWeight_mul_piece_zero {n m : ℕ} (f f' : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3)
    (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := h.speciesGaugeWeight f l)
        (d' := h.speciesGaugeWeight f' l')).piece 0
      =
      (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightD f l)
            (d' := h.rangeGaugeWeightBarD f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarD f l)
            (d' := h.rangeGaugeWeightD f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightU f l)
            (d' := h.rangeGaugeWeightBarU f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarU f l)
            (d' := h.rangeGaugeWeightU f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightQ f l)
            (d' := h.rangeGaugeWeightBarQ f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarQ f l)
            (d' := h.rangeGaugeWeightQ f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightL f l)
            (d' := h.rangeGaugeWeightBarL f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarL f l)
            (d' := h.rangeGaugeWeightL f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightE f l)
            (d' := h.rangeGaugeWeightBarE f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarE f l)
            (d' := h.rangeGaugeWeightE f' l')).piece 0
```

**`StandardModel.IsFermionSector.iSup_fin_zero_eq`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L589).

> The zero-index derivative slot collapses a supremum over it to its value: there
> is nothing to derive with respect to.

```lean
lemma iSup_fin_zero_eq {α : Type} [CompleteLattice α] (F : (Fin 0 → Fin 1 ⊕ Fin 3) → α) :
    ⨆ l, F l = F ![]
```

**`StandardModel.IsFermionSector.derivSubmodule_zero_eq`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L595).

> The underived derivative submodule as a join over families alone, the trivial
> derivative slot dropped.

```lean
lemma derivSubmodule_zero_eq :
    h.derivSubmodule 0 = ⨆ (f : Fin 3),
      (LinearMap.range (d f ![]) ⊔
        LinearMap.range (bard f ![]) ⊔
        LinearMap.range (u f ![]) ⊔
        LinearMap.range (baru f ![]) ⊔
        LinearMap.range (Q f ![]) ⊔
        LinearMap.range (barQ f ![]) ⊔
        LinearMap.range (L f ![]) ⊔
        LinearMap.range (barL f ![]) ⊔
        LinearMap.range (e f ![]) ⊔
        LinearMap.range (bare f ![]))
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightSix_piece_zero`**, a lemma, [line 614](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L614).

> The weight-zero piece at mass weight six, written out in the mass terms
> themselves: the join, over pairs of families, of the ten ways to pair each
> species with its own conjugate. Every other pairing of species has hypercharges
> that cannot cancel, by `speciesGaugeWeight_mul_piece_zero`.

```lean
lemma massWeightSubmoduleGaugeWeightSix_piece_zero :
    (h.massWeightSubmoduleGaugeWeightSix).piece 0
      = ⨆ (f : Fin 3) (f' : Fin 3),
        (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightD f ![])
              (d' := h.rangeGaugeWeightBarD f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarD f ![])
              (d' := h.rangeGaugeWeightD f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightU f ![])
              (d' := h.rangeGaugeWeightBarU f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarU f ![])
              (d' := h.rangeGaugeWeightU f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightQ f ![])
              (d' := h.rangeGaugeWeightBarQ f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarQ f ![])
              (d' := h.rangeGaugeWeightQ f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightL f ![])
              (d' := h.rangeGaugeWeightBarL f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarL f ![])
              (d' := h.rangeGaugeWeightL f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightE f ![])
              (d' := h.rangeGaugeWeightBarE f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarE f ![])
              (d' := h.rangeGaugeWeightE f' ![])).piece 0
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightEight_piece_zero`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L679).

> The weight-zero piece at mass weight eight, written out in the kinetic terms
> themselves: the join, over pairs of families and a once-derived slot, of the ten
> ways to pair each species with its own conjugate. Every other pairing of species has
> hypercharges that cannot cancel, by `speciesGaugeWeight_mul_piece_zero`.

```lean
lemma massWeightSubmoduleGaugeWeightEight_piece_zero :
    (h.massWeightSubmoduleGaugeWeightEight).piece 0
      = ⨆ (f : Fin 3) (f' : Fin 3) (l' : Fin 1 → Fin 1 ⊕ Fin 3),
        (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightD f ![])
              (d' := h.rangeGaugeWeightBarD f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarD f ![])
              (d' := h.rangeGaugeWeightD f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightU f ![])
              (d' := h.rangeGaugeWeightBarU f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarU f ![])
              (d' := h.rangeGaugeWeightU f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightQ f ![])
              (d' := h.rangeGaugeWeightBarQ f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarQ f ![])
              (d' := h.rangeGaugeWeightQ f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightL f ![])
              (d' := h.rangeGaugeWeightBarL f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarL f ![])
              (d' := h.rangeGaugeWeightL f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightE f ![])
              (d' := h.rangeGaugeWeightBarE f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := h.rangeGaugeWeightBarE f ![])
              (d' := h.rangeGaugeWeightE f' l')).piece 0
```

## B. Invariants modulo a gauge-stable submodule

> A submodule `S` closed under the gauge action can be discarded from a gauge-invariant
> element: if `x` is gauge invariant and lies in a fermionic submodule joined with `S`, then
> its fermionic part has to vanish and `x` already lies in `S`. The reason is the one behind
> `derivSubmoduleGaugeWeight_piece_zero`: every one of the ten species carries a fixed nonzero
> hypercharge, so no nonzero fermionic element is a gauge singlet.
>
> The argument is the torus sieve `GaugeWeightDecomposition.mem_piece_zero_sup_of_invariant`:
> each piece of nonzero weight is scaled by a torus generator by a scalar other than one, so
> modulo `S` an invariant lies in the weight-zero piece, and the weight-zero piece of a single
> tower is trivial (`derivSubmoduleGaugeWeight_piece_zero`).
>
> This is the fermionic analogue of `exists_smul_contraction_of_invariant_subset` for the
> Lorentz group.

**`StandardModel.IsFermionSector.mem_of_invariant_of_mem_derivSubmodule_sup`**, a lemma, [line 779](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L779).

> A gauge-invariant element of `h.derivSubmodule n ⊔ S`, for any submodule `S` closed under
> the gauge action, already lies in `S`. The fermionic part carries no gauge singlet, since
> each of the ten species has a fixed nonzero hypercharge, so it cannot survive; what is left
> is the part in `S`. Compare `derivSubmoduleGaugeWeight_piece_zero`.

```lean
lemma mem_of_invariant_of_mem_derivSubmodule_sup {n : ℕ} {S : Submodule ℂ B}
    (hS : ∀ (g : GaugeGroupI) (y : B), y ∈ S → repGauge g y ∈ S)
    {x : B} (hx : x ∈ h.derivSubmodule n ⊔ S)
    (hinv : ∀ g : GaugeGroupI, repGauge g x = x) : x ∈ S
```

**`StandardModel.IsFermionSector.mem_of_mem_massWeightSubmoduleOne_sup`**, a lemma, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L789).

> Mass weight one contributes nothing to a join: the submodule is trivial, so no invariance
> hypothesis is needed.

```lean
lemma mem_of_mem_massWeightSubmoduleOne_sup {S : Submodule ℂ B}
    {x : B} (hx : x ∈ h.massWeightSubmodule 1 ⊔ S) : x ∈ S
```

**`StandardModel.IsFermionSector.mem_of_mem_massWeightSubmoduleTwo_sup`**, a lemma, [line 795](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L795).

> Mass weight two contributes nothing to a join: the submodule is trivial, so no invariance
> hypothesis is needed.

```lean
lemma mem_of_mem_massWeightSubmoduleTwo_sup {S : Submodule ℂ B}
    {x : B} (hx : x ∈ h.massWeightSubmodule 2 ⊔ S) : x ∈ S
```

**`StandardModel.IsFermionSector.mem_of_mem_massWeightSubmoduleFour_sup`**, a lemma, [line 801](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L801).

> Mass weight four contributes nothing to a join: the submodule is trivial, so no
> invariance hypothesis is needed.

```lean
lemma mem_of_mem_massWeightSubmoduleFour_sup {S : Submodule ℂ B}
    {x : B} (hx : x ∈ h.massWeightSubmodule 4 ⊔ S) : x ∈ S
```

**`StandardModel.IsFermionSector.mem_of_invariant_of_mem_massWeightSubmoduleThree_sup`**, a lemma, [line 808](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L808).

> A gauge-invariant element of `h.massWeightSubmodule 3 ⊔ S`, for `S` closed under the
> gauge action, lies in `S`: mass weight three is the underived fermion towers, which carry
> no gauge singlet.

```lean
lemma mem_of_invariant_of_mem_massWeightSubmoduleThree_sup {S : Submodule ℂ B}
    (hS : ∀ (g : GaugeGroupI) (y : B), y ∈ S → repGauge g y ∈ S)
    {x : B} (hx : x ∈ h.massWeightSubmodule 3 ⊔ S)
    (hinv : ∀ g : GaugeGroupI, repGauge g x = x) : x ∈ S
```

**`StandardModel.IsFermionSector.mem_of_invariant_of_mem_massWeightSubmoduleFive_sup`**, a lemma, [line 818](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L818).

> A gauge-invariant element of `h.massWeightSubmodule 5 ⊔ S`, for `S` closed under the
> gauge action, lies in `S`: mass weight five is the once-derived fermion towers, which carry
> no gauge singlet.

```lean
lemma mem_of_invariant_of_mem_massWeightSubmoduleFive_sup {S : Submodule ℂ B}
    (hS : ∀ (g : GaugeGroupI) (y : B), y ∈ S → repGauge g y ∈ S)
    {x : B} (hx : x ∈ h.massWeightSubmodule 5 ⊔ S)
    (hinv : ∀ g : GaugeGroupI, repGauge g x = x) : x ∈ S
```

**`StandardModel.IsFermionSector.mem_of_invariant_of_mem_massWeightSubmoduleSeven_sup`**, a lemma, [line 828](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean#L828).

> A gauge-invariant element of `h.massWeightSubmodule 7 ⊔ S`, for `S` closed under the
> gauge action, lies in `S`: mass weight seven is the twice-derived fermion towers, which
> carry no gauge singlet.

```lean
lemma mem_of_invariant_of_mem_massWeightSubmoduleSeven_sup {S : Submodule ℂ B}
    (hS : ∀ (g : GaugeGroupI) (y : B), y ∈ S → repGauge g y ∈ S)
    {x : B} (hx : x ∈ h.massWeightSubmodule 7 ⊔ S)
    (hinv : ∀ g : GaugeGroupI, repGauge g x = x) : x ∈ S
```

## Depends on

- [The gauge weight decomposition of the fermion sector](isfermionsector-deriv-gaugeweight.md)
- [The mass-weight grading of the fermion sector](isfermionsector-massweight-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/GaugeWeight.lean)
