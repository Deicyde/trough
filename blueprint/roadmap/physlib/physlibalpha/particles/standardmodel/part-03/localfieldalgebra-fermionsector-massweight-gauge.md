---
declaration: module
origin: cited
lean: StandardModel.FermionSector.massWeightSubmoduleGaugeWeightSix, StandardModel.FermionSector.massWeightSubmoduleGaugeWeightEight, StandardModel.FermionSector.zero_not_mem_fermionGaugeWeights, StandardModel.FermionSector.derivSubmoduleGaugeWeight_piece_zero, StandardModel.FermionSector.piece_sup_mul, StandardModel.FermionSector.piece_mul_sup, StandardModel.FermionSector.mul_piece_zero_eq_bot_of_hypercharge, StandardModel.FermionSector.rangeGaugeWeightD_hc
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the fermion mass-weight submodules

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionSector.MassWeight.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean): 43 declarations, 43 with a docstring.

> The gauge-singlet content of the fermion sector up to mass weight eight, the mass and kinetic
> pairings of each species with its conjugate.

## i. Overview

> Each mass-weight submodule of the fermion sector up to weight eight has an explicit
> description in terms of the derivative submodules, and the derivative submodules carry
> a gauge weight decomposition. Weights one, two and four are trivial, weights three, five and
> seven are the towers with zero, one and two covariant derivatives, weight six is the product
> of two underived towers, and weight eight is the kinetic sector.
>
> No single fermion symbol is a gauge singlet, every species carrying a nonzero hypercharge, so
> the towers of weights three, five and seven carry no gauge invariant modulo a gauge-stable
> submodule (section C). Weights six and eight are products of two towers, and their weight-zero
> pieces are the pairings of each species with its own conjugate (section B).

## ii. Key results

> - `massWeightSubmoduleGaugeWeightSix`, `massWeightSubmoduleGaugeWeightEight` : the gauge weight
>   decompositions of mass weights six and eight.
> - `massWeightSubmoduleGaugeWeightSix_piece_zero`, `massWeightSubmoduleGaugeWeightEight_piece_zero` :
>   their weight-zero pieces, the pairings of each species with its own conjugate.
> - `mem_of_invariant_of_mem_derivSubmodule_sup` : a gauge invariant of a derivative submodule
>   joined with a gauge-stable `S` lies in `S`.

## iv. References

> * None.

## A. The decompositions at mass weights six and eight

> The fermion mass-weight submodules that are products of two towers carry the product of the
> gauge weight decompositions of their factors.

**`StandardModel.FermionSector.massWeightSubmoduleGaugeWeightSix`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L70).

> Weight six is the products of two underived fermion towers.

```lean
noncomputable def massWeightSubmoduleGaugeWeightSix :
    GaugeWeightDecomposition repGauge (massWeightSubmodule 6)
```

**`StandardModel.FermionSector.massWeightSubmoduleGaugeWeightEight`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L78).

> Weight eight is the kinetic sector, an underived tower against a once-derived one.

```lean
noncomputable def massWeightSubmoduleGaugeWeightEight :
    GaugeWeightDecomposition repGauge (massWeightSubmodule 8)
```

## B. The weight-zero pieces

**`StandardModel.FermionSector.zero_not_mem_fermionGaugeWeights`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L94).

> Every gauge weight carried by a fermion symbol has nonzero hypercharge, since each of the
> ten species has a fixed nonzero hypercharge, independent of colour, isospin and
> family, and the barred species carry the negative of the unbarred one. So the zero
> weight never occurs.

```lean
lemma zero_not_mem_fermionGaugeWeights : (0 : GaugeWeight) ∉ fermionGaugeWeights
```

**`StandardModel.FermionSector.derivSubmoduleGaugeWeight_piece_zero`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L102).

> The weight-zero piece of the fermion derivative submodules is trivial. Unlike
> the gauge sector, no single fermion symbol is a gauge singlet, since every one of the
> ten species carries a fixed nonzero hypercharge. A gauge-invariant combination needs
> at least two fermion insertions, which is why it is the mass weights six and eight,
> the products of two towers, that carry the interesting weight-zero content.

```lean
lemma derivSubmoduleGaugeWeight_piece_zero (n : ℕ) :
    (derivSubmoduleGaugeWeight n).piece 0 = ⊥
```

### B.1. Infrastructure for the product weights six and eight

> Mass weights six and eight are products of two fermion towers, and their weight-zero
> piece is genuinely nontrivial: it is spanned by pairing each species with its own
> conjugate (a mass term). Splitting the product decomposition down to the ten species
> and discarding the non-conjugate pairings, whose hypercharges never cancel, takes the
> infrastructure developed here.

**`StandardModel.FermionSector.piece_sup_mul`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L121).

> If the left factor of a product decomposition is a join `VA ⊔ VB`, its weight-`w`
> piece splits along the join.

```lean
lemma piece_sup_mul {VA VB VC : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (dA : GaugeWeightDecomposition repGauge VA) (dB : GaugeWeightDecomposition repGauge VB)
    (dC : GaugeWeightDecomposition repGauge VC) (w : GaugeWeight) :
    (GaugeWeightDecomposition.mul (d := GaugeWeightDecomposition.sup (d := dA) (d' := dB))
        (d' := dC)).piece w
      = (GaugeWeightDecomposition.mul (d := dA) (d' := dC)).piece w
        ⊔ (GaugeWeightDecomposition.mul (d := dB) (d' := dC)).piece w
```

**`StandardModel.FermionSector.piece_mul_sup`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L137).

> If the right factor of a product decomposition is a join `VA ⊔ VB`, its weight-`w`
> piece splits along the join.

```lean
lemma piece_mul_sup {VA VB VC : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (dC : GaugeWeightDecomposition repGauge VC) (dA : GaugeWeightDecomposition repGauge VA)
    (dB : GaugeWeightDecomposition repGauge VB) (w : GaugeWeight) :
    (GaugeWeightDecomposition.mul (d := dC)
        (d' := GaugeWeightDecomposition.sup (d := dA) (d' := dB))).piece w
      = (GaugeWeightDecomposition.mul (d := dC) (d' := dA)).piece w
        ⊔ (GaugeWeightDecomposition.mul (d := dC) (d' := dB)).piece w
```

**`StandardModel.FermionSector.mul_piece_zero_eq_bot_of_hypercharge`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L154).

> Two decompositions with constant, non-cancelling hypercharge across their whole
> supports have a trivial product at weight zero, since a weight from one can never cancel
> a weight from the other.

```lean
lemma mul_piece_zero_eq_bot_of_hypercharge {V V' : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    {dV : GaugeWeightDecomposition repGauge V} {dV' : GaugeWeightDecomposition repGauge V'}
    {hc hc' : ℤ} (hV : ∀ w ∈ dV.supp, w.2.2.2 = hc) (hV' : ∀ w ∈ dV'.supp, w.2.2.2 = hc')
    (hne : hc + hc' ≠ 0) :
    (GaugeWeightDecomposition.mul (d := dV) (d' := dV')).piece 0 = ⊥
```

**`StandardModel.FermionSector.rangeGaugeWeightD_hc`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L175).

> The `d` symbols carry hypercharge `2` (the negative of the down-singlet's `-2`),
> independent of colour and family.

```lean
lemma rangeGaugeWeightD_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightD f l).supp, w.2.2.2 = 2
```

**`StandardModel.FermionSector.rangeGaugeWeightBarD_hc`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L184).

> The `bard` symbols carry hypercharge `-2`, independent of colour and family.

```lean
lemma rangeGaugeWeightBarD_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightBarD f l).supp, w.2.2.2 = -2
```

**`StandardModel.FermionSector.rangeGaugeWeightU_hc`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L193).

> The `u` symbols carry hypercharge `-4`, independent of colour and family.

```lean
lemma rangeGaugeWeightU_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightU f l).supp, w.2.2.2 = -4
```

**`StandardModel.FermionSector.rangeGaugeWeightBarU_hc`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L202).

> The `baru` symbols carry hypercharge `4`, independent of colour and family.

```lean
lemma rangeGaugeWeightBarU_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightBarU f l).supp, w.2.2.2 = 4
```

**`StandardModel.FermionSector.rangeGaugeWeightQ_hc`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L212).

> The `Q` symbols carry hypercharge `-1`, independent of colour, isospin and
> family.

```lean
lemma rangeGaugeWeightQ_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightQ f l).supp, w.2.2.2 = -1
```

**`StandardModel.FermionSector.rangeGaugeWeightBarQ_hc`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L222).

> The `barQ` symbols carry hypercharge `1`, independent of colour, isospin and
> family.

```lean
lemma rangeGaugeWeightBarQ_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightBarQ f l).supp, w.2.2.2 = 1
```

**`StandardModel.FermionSector.rangeGaugeWeightL_hc`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L231).

> The `L` symbols carry hypercharge `3`, independent of isospin and family.

```lean
lemma rangeGaugeWeightL_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightL f l).supp, w.2.2.2 = 3
```

**`StandardModel.FermionSector.rangeGaugeWeightBarL_hc`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L240).

> The `barL` symbols carry hypercharge `-3`, independent of isospin and family.

```lean
lemma rangeGaugeWeightBarL_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightBarL f l).supp, w.2.2.2 = -3
```

**`StandardModel.FermionSector.rangeGaugeWeightE_hc`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L249).

> The `e` symbols carry hypercharge `6`, independent of family.

```lean
lemma rangeGaugeWeightE_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightE f l).supp, w.2.2.2 = 6
```

**`StandardModel.FermionSector.rangeGaugeWeightBarE_hc`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L258).

> The `bare` symbols carry hypercharge `-6`, independent of family.

```lean
lemma rangeGaugeWeightBarE_hc {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    ∀ w ∈ (rangeGaugeWeightBarE f l).supp, w.2.2.2 = -6
```

**`StandardModel.FermionSector.speciesGaugeWeight`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L270).

> The gauge weight decomposition of one family's full set of symbols at fixed
> derivative slots, matching the recipe of `derivSubmodule` itself, the join of the
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

**`StandardModel.FermionSector.rangeGaugeWeightD_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L298).

> Against the full symbol set of a family, the `d` symbols reach gauge weight zero only
> with the `bard` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightD_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightD f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightD f l)
        (d' := rangeGaugeWeightBarD f' l')).piece 0
```

**`StandardModel.FermionSector.rangeGaugeWeightBarD_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L316).

> Against the full symbol set of a family, the `bard` symbols reach gauge weight zero only
> with the `d` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightBarD_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarD f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarD f l)
        (d' := rangeGaugeWeightD f' l')).piece 0
```

**`StandardModel.FermionSector.rangeGaugeWeightU_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L334).

> Against the full symbol set of a family, the `u` symbols reach gauge weight zero only
> with the `baru` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightU_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightU f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightU f l)
        (d' := rangeGaugeWeightBarU f' l')).piece 0
```

**`StandardModel.FermionSector.rangeGaugeWeightBarU_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L352).

> Against the full symbol set of a family, the `baru` symbols reach gauge weight zero only
> with the `u` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightBarU_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarU f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarU f l)
        (d' := rangeGaugeWeightU f' l')).piece 0
```

**`StandardModel.FermionSector.rangeGaugeWeightQ_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L370).

> Against the full symbol set of a family, the `Q` symbols reach gauge weight zero only
> with the `barQ` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightQ_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightQ f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightQ f l)
        (d' := rangeGaugeWeightBarQ f' l')).piece 0
```

**`StandardModel.FermionSector.rangeGaugeWeightBarQ_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L388).

> Against the full symbol set of a family, the `barQ` symbols reach gauge weight zero only
> with the `Q` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightBarQ_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarQ f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarQ f l)
        (d' := rangeGaugeWeightQ f' l')).piece 0
```

**`StandardModel.FermionSector.rangeGaugeWeightL_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L406).

> Against the full symbol set of a family, the `L` symbols reach gauge weight zero only
> with the `barL` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightL_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightL f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightL f l)
        (d' := rangeGaugeWeightBarL f' l')).piece 0
```

**`StandardModel.FermionSector.rangeGaugeWeightBarL_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L424).

> Against the full symbol set of a family, the `barL` symbols reach gauge weight zero only
> with the `L` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightBarL_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarL f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarL f l)
        (d' := rangeGaugeWeightL f' l')).piece 0
```

**`StandardModel.FermionSector.rangeGaugeWeightE_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L442).

> Against the full symbol set of a family, the `e` symbols reach gauge weight zero only
> with the `bare` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightE_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightE f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightE f l)
        (d' := rangeGaugeWeightBarE f' l')).piece 0
```

**`StandardModel.FermionSector.rangeGaugeWeightBarE_mul_speciesGaugeWeight_piece_zero`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L460).

> Against the full symbol set of a family, the `bare` symbols reach gauge weight zero only
> with the `e` symbols, the hypercharges of every other species not cancelling theirs.

```lean
lemma rangeGaugeWeightBarE_mul_speciesGaugeWeight_piece_zero {n m : ℕ} (f f' : Fin 3)
    (l : Fin n → Fin 1 ⊕ Fin 3) (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarE f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      = (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarE f l)
        (d' := rangeGaugeWeightE f' l')).piece 0
```

**`StandardModel.FermionSector.speciesGaugeWeight_mul_piece_zero`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L479).

> The weight-zero piece of the product of two families' full symbol sets collapses
> to the ten conjugate pairings, since every other combination of species has hypercharges
> that cannot cancel.

```lean
lemma speciesGaugeWeight_mul_piece_zero {n m : ℕ} (f f' : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3)
    (l' : Fin m → Fin 1 ⊕ Fin 3) :
    (GaugeWeightDecomposition.mul (d := speciesGaugeWeight f l)
        (d' := speciesGaugeWeight f' l')).piece 0
      =
      (GaugeWeightDecomposition.mul (d := rangeGaugeWeightD f l)
            (d' := rangeGaugeWeightBarD f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarD f l)
            (d' := rangeGaugeWeightD f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightU f l)
            (d' := rangeGaugeWeightBarU f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarU f l)
            (d' := rangeGaugeWeightU f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightQ f l)
            (d' := rangeGaugeWeightBarQ f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarQ f l)
            (d' := rangeGaugeWeightQ f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightL f l)
            (d' := rangeGaugeWeightBarL f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarL f l)
            (d' := rangeGaugeWeightL f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightE f l)
            (d' := rangeGaugeWeightBarE f' l')).piece 0
        ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarE f l)
            (d' := rangeGaugeWeightE f' l')).piece 0
```

**`StandardModel.FermionSector.iSup_fin_zero_eq`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L517).

> The zero-index derivative slot collapses a supremum over it to its value, as there
> is nothing to derive with respect to.

```lean
lemma iSup_fin_zero_eq {α : Type} [CompleteLattice α] (F : (Fin 0 → Fin 1 ⊕ Fin 3) → α) :
    ⨆ l, F l = F ![]
```

**`StandardModel.FermionSector.derivSubmodule_zero_eq`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L523).

> The underived derivative submodule as a join over families alone, the trivial
> derivative slot dropped.

```lean
lemma derivSubmodule_zero_eq :
    derivSubmodule 0 = ⨆ (f : Fin 3),
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

**`StandardModel.FermionSector.derivSubmodule_one_eq`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L540).

> The once-derived derivative submodule as a join over families and the single derivative
> slot.

```lean
lemma derivSubmodule_one_eq :
    derivSubmodule 1 = ⨆ (f' : Fin 3) (l' : Fin 1 → Fin 1 ⊕ Fin 3),
      (LinearMap.range (d f' l') ⊔
        LinearMap.range (bard f' l') ⊔
        LinearMap.range (u f' l') ⊔
        LinearMap.range (baru f' l') ⊔
        LinearMap.range (Q f' l') ⊔
        LinearMap.range (barQ f' l') ⊔
        LinearMap.range (L f' l') ⊔
        LinearMap.range (barL f' l') ⊔
        LinearMap.range (e f' l') ⊔
        LinearMap.range (bare f' l'))
```

**`StandardModel.FermionSector.derivSubmodule_zero_mul_derivSubmodule_zero`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L554).

> The product of two underived derivative submodules as a join over pairs of families.

```lean
lemma derivSubmodule_zero_mul_derivSubmodule_zero : derivSubmodule 0 * derivSubmodule 0
    = ⨆ (f : Fin 3) (f' : Fin 3),
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
        * (LinearMap.range (d f' ![]) ⊔
        LinearMap.range (bard f' ![]) ⊔
        LinearMap.range (u f' ![]) ⊔
        LinearMap.range (baru f' ![]) ⊔
        LinearMap.range (Q f' ![]) ⊔
        LinearMap.range (barQ f' ![]) ⊔
        LinearMap.range (L f' ![]) ⊔
        LinearMap.range (barL f' ![]) ⊔
        LinearMap.range (e f' ![]) ⊔
        LinearMap.range (bare f' ![]))
```

**`StandardModel.FermionSector.derivSubmodule_zero_mul_derivSubmodule_one`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L581).

> The product of an underived and a once-derived derivative submodule as a join over pairs of
> families and the derivative slot.

```lean
lemma derivSubmodule_zero_mul_derivSubmodule_one : derivSubmodule 0 * derivSubmodule 1
    = ⨆ (f : Fin 3) (f' : Fin 3) (l' : Fin 1 → Fin 1 ⊕ Fin 3),
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
        * (LinearMap.range (d f' l') ⊔
        LinearMap.range (bard f' l') ⊔
        LinearMap.range (u f' l') ⊔
        LinearMap.range (baru f' l') ⊔
        LinearMap.range (Q f' l') ⊔
        LinearMap.range (barQ f' l') ⊔
        LinearMap.range (L f' l') ⊔
        LinearMap.range (barL f' l') ⊔
        LinearMap.range (e f' l') ⊔
        LinearMap.range (bare f' l'))
```

**`StandardModel.FermionSector.massWeightSubmoduleGaugeWeightSix_piece_zero`**, a lemma, [line 612](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L612).

> The weight-zero piece at mass weight six, written out in the mass terms
> themselves, the join, over pairs of families, of the ten ways to pair each
> species with its own conjugate. Every other pairing of species has hypercharges
> that cannot cancel, by `speciesGaugeWeight_mul_piece_zero`.

```lean
lemma massWeightSubmoduleGaugeWeightSix_piece_zero :
    (massWeightSubmoduleGaugeWeightSix).piece 0
      = ⨆ (f : Fin 3) (f' : Fin 3),
        (GaugeWeightDecomposition.mul (d := rangeGaugeWeightD f ![])
              (d' := rangeGaugeWeightBarD f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarD f ![])
              (d' := rangeGaugeWeightD f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightU f ![])
              (d' := rangeGaugeWeightBarU f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarU f ![])
              (d' := rangeGaugeWeightU f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightQ f ![])
              (d' := rangeGaugeWeightBarQ f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarQ f ![])
              (d' := rangeGaugeWeightQ f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightL f ![])
              (d' := rangeGaugeWeightBarL f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarL f ![])
              (d' := rangeGaugeWeightL f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightE f ![])
              (d' := rangeGaugeWeightBarE f' ![])).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarE f ![])
              (d' := rangeGaugeWeightE f' ![])).piece 0
```

**`StandardModel.FermionSector.massWeightSubmoduleGaugeWeightEight_piece_zero`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L653).

> The weight-zero piece at mass weight eight, written out in the kinetic terms
> themselves, the join, over pairs of families and a once-derived slot, of the ten
> ways to pair each species with its own conjugate. Every other pairing of species has
> hypercharges that cannot cancel, by `speciesGaugeWeight_mul_piece_zero`.

```lean
lemma massWeightSubmoduleGaugeWeightEight_piece_zero :
    (massWeightSubmoduleGaugeWeightEight).piece 0
      = ⨆ (f : Fin 3) (f' : Fin 3) (l' : Fin 1 → Fin 1 ⊕ Fin 3),
        (GaugeWeightDecomposition.mul (d := rangeGaugeWeightD f ![])
              (d' := rangeGaugeWeightBarD f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarD f ![])
              (d' := rangeGaugeWeightD f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightU f ![])
              (d' := rangeGaugeWeightBarU f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarU f ![])
              (d' := rangeGaugeWeightU f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightQ f ![])
              (d' := rangeGaugeWeightBarQ f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarQ f ![])
              (d' := rangeGaugeWeightQ f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightL f ![])
              (d' := rangeGaugeWeightBarL f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarL f ![])
              (d' := rangeGaugeWeightL f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightE f ![])
              (d' := rangeGaugeWeightBarE f' l')).piece 0
          ⊔ (GaugeWeightDecomposition.mul (d := rangeGaugeWeightBarE f ![])
              (d' := rangeGaugeWeightE f' l')).piece 0
```

## C. Invariants modulo a gauge-stable submodule

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

**`StandardModel.FermionSector.mem_of_invariant_of_mem_derivSubmodule_sup`**, a lemma, [line 712](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L712).

> A gauge-invariant element of `derivSubmodule n ⊔ S`, for any submodule `S` closed under
> the gauge action, already lies in `S`. The fermionic part carries no gauge singlet, since
> each of the ten species has a fixed nonzero hypercharge, so it cannot survive; what is left
> is the part in `S`. Compare `derivSubmoduleGaugeWeight_piece_zero`.

```lean
lemma mem_of_invariant_of_mem_derivSubmodule_sup {n : ℕ}
    {S : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hS : ∀ (g : GaugeGroupI) (y : fieldData.LocalCovFieldAlgebra), y ∈ S → repGauge g y ∈ S)
    {x : fieldData.LocalCovFieldAlgebra} (hx : x ∈ derivSubmodule n ⊔ S)
    (hinv : ∀ g : GaugeGroupI, repGauge g x = x) : x ∈ S
```

**`StandardModel.FermionSector.mem_of_mem_massWeightSubmoduleOne_sup`**, a lemma, [line 723](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L723).

> Mass weight one contributes nothing to a join, since the submodule is trivial, so no invariance
> hypothesis is needed.

```lean
lemma mem_of_mem_massWeightSubmoduleOne_sup {S : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    {x : fieldData.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmodule 1 ⊔ S) : x ∈ S
```

**`StandardModel.FermionSector.mem_of_mem_massWeightSubmoduleTwo_sup`**, a lemma, [line 729](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L729).

> Mass weight two contributes nothing to a join, since the submodule is trivial, so no invariance
> hypothesis is needed.

```lean
lemma mem_of_mem_massWeightSubmoduleTwo_sup {S : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    {x : fieldData.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmodule 2 ⊔ S) : x ∈ S
```

**`StandardModel.FermionSector.mem_of_mem_massWeightSubmoduleFour_sup`**, a lemma, [line 735](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L735).

> Mass weight four contributes nothing to a join, since the submodule is trivial, so no
> invariance hypothesis is needed.

```lean
lemma mem_of_mem_massWeightSubmoduleFour_sup {S : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    {x : fieldData.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmodule 4 ⊔ S) : x ∈ S
```

**`StandardModel.FermionSector.mem_of_invariant_of_mem_massWeightSubmoduleThree_sup`**, a lemma, [line 742](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L742).

> A gauge-invariant element of `massWeightSubmodule 3 ⊔ S`, for `S` closed under the
> gauge action, lies in `S`, since mass weight three is the underived fermion towers, which carry
> no gauge singlet.

```lean
lemma mem_of_invariant_of_mem_massWeightSubmoduleThree_sup
    {S : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hS : ∀ (g : GaugeGroupI) (y : fieldData.LocalCovFieldAlgebra), y ∈ S → repGauge g y ∈ S)
    {x : fieldData.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmodule 3 ⊔ S)
    (hinv : ∀ g : GaugeGroupI, repGauge g x = x) : x ∈ S
```

**`StandardModel.FermionSector.mem_of_invariant_of_mem_massWeightSubmoduleFive_sup`**, a lemma, [line 753](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L753).

> A gauge-invariant element of `massWeightSubmodule 5 ⊔ S`, for `S` closed under the
> gauge action, lies in `S`, since mass weight five is the once-derived fermion towers, which carry
> no gauge singlet.

```lean
lemma mem_of_invariant_of_mem_massWeightSubmoduleFive_sup
    {S : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hS : ∀ (g : GaugeGroupI) (y : fieldData.LocalCovFieldAlgebra), y ∈ S → repGauge g y ∈ S)
    {x : fieldData.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmodule 5 ⊔ S)
    (hinv : ∀ g : GaugeGroupI, repGauge g x = x) : x ∈ S
```

**`StandardModel.FermionSector.mem_of_invariant_of_mem_massWeightSubmoduleSeven_sup`**, a lemma, [line 764](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean#L764).

> A gauge-invariant element of `massWeightSubmodule 7 ⊔ S`, for `S` closed under the
> gauge action, lies in `S`, since mass weight seven is the twice-derived fermion towers, which
> carry no gauge singlet.

```lean
lemma mem_of_invariant_of_mem_massWeightSubmoduleSeven_sup
    {S : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hS : ∀ (g : GaugeGroupI) (y : fieldData.LocalCovFieldAlgebra), y ∈ S → repGauge g y ∈ S)
    {x : fieldData.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmodule 7 ⊔ S)
    (hinv : ∀ g : GaugeGroupI, repGauge g x = x) : x ∈ S
```

## Depends on

- [The gauge weight decomposition of the fermion sector](localfieldalgebra-fermionsector-deriv-gaugeweigh.md)
- [The mass-weight grading of the fermion sector](localfieldalgebra-fermionsector-massweight-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/GaugeWeight.lean)
