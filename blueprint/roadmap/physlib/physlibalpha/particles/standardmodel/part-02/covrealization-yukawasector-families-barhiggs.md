---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.barDownBlock, StandardModel.CovAlgebraRealization.isSU3FundamentalAntiFundamental_barDownBlock, StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_barDownBlock, StandardModel.CovAlgebraRealization.isBiDualLeftWeyl_barDownBlock, StandardModel.CovAlgebraRealization.repGauge_u1_barDownBlock, StandardModel.CovAlgebraRealization.barDownBlockColour, StandardModel.CovAlgebraRealization.barDownBlockColour_eq, StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_barDownBlockColour
statement: formalized
proof: formalized
---

# The Yukawa terms built on the conjugate Higgs symbol

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.YukawaSector.Families.BarHiggs`, [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean): 70 declarations, 70 with a docstring.

## i. Overview

> The remaining three couplings of the mass-weight-eight Yukawa sector are built on the
> conjugate Higgs symbol: `barH bard Q`, `barH u barQ` and `barH L bare`.  Each is the
> conjugate of one of the three couplings of `Families.Higgs`, and is the same computation
> with every symbol replaced by its conjugate: fundamental and anti-fundamental indices
> exchange, left- and right-handed spinors exchange, and every hypercharge changes sign.  So
> the isospin structure of the conjugate up type is `2 ⊗ 2` where its partner had `2̄ ⊗ 2̄`,
> and its invariant is again the antisymmetric symbol.
>
> With these six couplings the twelve blocks are accounted for: the other six are the same
> six with the two fermion factors exchanged, and by `mul_mul_swap_eq_neg` their terms are
> minus these while by `mul_mul_piece_swap` their blocks are the same submodules.

## ii. Key results

> - `barDownYukawa`, `barUpYukawa`, `barLeptonYukawa` : the three conjugate Yukawa terms.
> - `isSU3FundamentalAntiFundamental_barDownBlock`, `isSU2BiFundamental_barUpBlock` and the
>   rest : the index laws of the three conjugate blocks.
> - `yukawaSpan` : the join of all six couplings over all nine family pairs.
> - `yukawaSpan_le_inf` : the Yukawa span lies inside the gauge- and Lorentz-invariants of
>   the sector at mass weight eight.

## iv. References

> * None.

## A. The conjugate down-type Yukawa term

> The conjugate of the down type: the product `barH bard Q`.  Colour is `3 ⊗ 3̄` with the
> conjugate down singlet supplying the fundamental index, isospin is `2 ⊗ 2̄` with the
> conjugate Higgs symbol supplying the fundamental index and the quark doublet the
> anti-fundamental one, and both fermions are left-handed.

**`StandardModel.CovAlgebraRealization.barDownBlock`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L79).

> The components of the conjugate down-type Yukawa block `barH bard Q`: a conjugate
> Higgs symbol, a conjugate down-singlet symbol and a quark-doublet symbol, none carrying
> derivatives.

```lean
noncomputable def barDownBlock (f f' : Fin 3) (i sbd : Fin 2) (cbd : Fin 3) (sQ : Fin 2)
    (cQ : Fin 3) (wQ : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.isSU3FundamentalAntiFundamental_barDownBlock`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L87).

> The two colour indices of the conjugate down-type block carry one fundamental and one
> anti-fundamental `su(3)` index, the conjugate down singlet supplying the fundamental
> one.

```lean
lemma isSU3FundamentalAntiFundamental_barDownBlock (f f' : Fin 3) (i sbd sQ wQ : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 3 => h.barDownBlock f f' i sbd (l 0) sQ (l 1) wQ)
```

**`StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_barDownBlock`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L102).

> The two isospin indices of the conjugate down-type block carry one fundamental and one
> anti-fundamental `su(2)` index, the conjugate Higgs symbol supplying the fundamental
> one.

```lean
lemma isSU2FundamentalAntiFundamental_barDownBlock (f f' : Fin 3) (sbd : Fin 2) (cbd : Fin 3)
    (sQ : Fin 2) (cQ : Fin 3) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.barDownBlock f f' (l 0) sbd cbd sQ cQ (l 1))
```

**`StandardModel.CovAlgebraRealization.isBiDualLeftWeyl_barDownBlock`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L115).

> The two spinor indices of the conjugate down-type block are both dual left-handed.

```lean
lemma isBiDualLeftWeyl_barDownBlock (f f' : Fin 3) (i : Fin 2) (cbd cQ : Fin 3)
    (wQ : Fin 2) :
    IsBiDualLeftWeyl B repLorentz
      (ofPairComponents fun a b => h.barDownBlock f f' i a cbd b cQ wQ)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_barDownBlock`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L133).

> A hypercharge transformation fixes every component of the conjugate down-type block,
> the three hypercharges `3`, `-2` and `-1` cancelling.

```lean
lemma repGauge_u1_barDownBlock (t : unitary ℂ) (f f' : Fin 3) (i sbd : Fin 2)
    (cbd : Fin 3) (sQ : Fin 2) (cQ : Fin 3) (wQ : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barDownBlock f f' i sbd cbd sQ cQ wQ)
      = h.barDownBlock f f' i sbd cbd sQ cQ wQ
```

**`StandardModel.CovAlgebraRealization.barDownBlockColour`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L147).

> The colour contraction of the conjugate down-type block.

```lean
noncomputable def barDownBlockColour (f f' : Fin 3) (i sbd sQ wQ : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.barDownBlockColour_eq`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L152).

> The colour contraction of the conjugate down-type block written out.

```lean
lemma barDownBlockColour_eq (f f' : Fin 3) (i sbd sQ wQ : Fin 2) :
    h.barDownBlockColour f f' i sbd sQ wQ
      = ∑ a : Fin 3, h.barDownBlock f f' i sbd a sQ a wQ
```

**`StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_barDownBlockColour`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L159).

> The colour contraction of the conjugate down-type block still carries one fundamental
> and one anti-fundamental isospin index.

```lean
lemma isSU2FundamentalAntiFundamental_barDownBlockColour (f f' : Fin 3) (sbd sQ : Fin 2) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.barDownBlockColour f f' (l 0) sbd sQ (l 1))
```

**`StandardModel.CovAlgebraRealization.barDownBlockIsospin`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L167).

> The isospin contraction of the colour-contracted conjugate down-type block.

```lean
noncomputable def barDownBlockIsospin (f f' : Fin 3) (sbd sQ : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.barDownBlockIsospin_eq`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L172).

> The doubly contracted conjugate down-type block written out.

```lean
lemma barDownBlockIsospin_eq (f f' : Fin 3) (sbd sQ : Fin 2) :
    h.barDownBlockIsospin f f' sbd sQ
      = ∑ p : Fin 2 × Fin 3, h.barDownBlock f f' p.1 sbd p.2 sQ p.2 p.1
```

**`StandardModel.CovAlgebraRealization.isBiDualLeftWeyl_barDownBlockIsospin`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L181).

> The doubly contracted conjugate down-type block carries two dual left-handed Weyl
> indices.

```lean
lemma isBiDualLeftWeyl_barDownBlockIsospin (f f' : Fin 3) :
    IsBiDualLeftWeyl B repLorentz (ofPairComponents (h.barDownBlockIsospin f f'))
```

**`StandardModel.CovAlgebraRealization.barDownYukawa`**, a def, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L190).

> The conjugate down-type Yukawa term of the family pair `(f, f')`. It is the image of the metric
> `εL'` under the map with the contracted block as its components.

```lean
noncomputable def barDownYukawa (f f' : Fin 3) : B
```

## B. The invariance of the conjugate down-type Yukawa term, and its mass weight

**`StandardModel.CovAlgebraRealization.repGauge_su3_barDownBlockColour`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L201).

> The colour contraction of the conjugate down-type block is fixed by the colour
> factor.

```lean
lemma repGauge_su3_barDownBlockColour (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i sbd sQ wQ : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.barDownBlockColour f f' i sbd sQ wQ)
      = h.barDownBlockColour f f' i sbd sQ wQ
```

**`StandardModel.CovAlgebraRealization.repGauge_su3_barDownBlockIsospin`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L209).

> The doubly contracted conjugate down-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_barDownBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (sbd sQ : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.barDownBlockIsospin f f' sbd sQ)
      = h.barDownBlockIsospin f f' sbd sQ
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_barDownBlockIsospin`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L217).

> The doubly contracted conjugate down-type block is fixed by the isospin factor.

```lean
lemma repGauge_su2_barDownBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (sbd sQ : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.barDownBlockIsospin f f' sbd sQ)
      = h.barDownBlockIsospin f f' sbd sQ
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_barDownBlockIsospin`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L225).

> The doubly contracted conjugate down-type block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_barDownBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (sbd sQ : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barDownBlockIsospin f f' sbd sQ)
      = h.barDownBlockIsospin f f' sbd sQ
```

**`StandardModel.CovAlgebraRealization.repGauge_barDownYukawa`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L233).

> The conjugate down-type Yukawa term is gauge invariant.

```lean
lemma repGauge_barDownYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGauge g (h.barDownYukawa f f') = h.barDownYukawa f f'
```

**`StandardModel.CovAlgebraRealization.repLorentz_barDownYukawa`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L242).

> The conjugate down-type Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_barDownYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentz Λ (h.barDownYukawa f f') = h.barDownYukawa f f'
```

**`StandardModel.CovAlgebraRealization.barDownBlock_mem_sectorMassWeight`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L249).

> Every component of the conjugate down-type block sits at mass weight eight in the
> Yukawa sector.

```lean
lemma barDownBlock_mem_sectorMassWeight (f f' : Fin 3) (i sbd : Fin 2) (cbd : Fin 3)
    (sQ : Fin 2) (cQ : Fin 3) (wQ : Fin 2) :
    h.barDownBlock f f' i sbd cbd sQ cQ wQ
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.barDownYukawa_mem_sectorMassWeight`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L259).

> The conjugate down-type Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma barDownYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    h.barDownYukawa f f'
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

## C. The conjugate up-type Yukawa term

> The conjugate of the up type: the product `barH u barQ`.  Colour is `3 ⊗ 3̄` with the
> conjugate quark doublet supplying the fundamental index, isospin is `2 ⊗ 2` — the conjugate
> Higgs symbol and the conjugate quark doublet both carry the fundamental, so the invariant
> is again the antisymmetric symbol — and both fermions are right-handed.

**`StandardModel.CovAlgebraRealization.barUpBlock`**, a def, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L279).

> The components of the conjugate up-type Yukawa block `barH u barQ`.

```lean
noncomputable def barUpBlock (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3) (sbQ : Fin 2)
    (cbQ : Fin 3) (wbQ : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.isSU3FundamentalAntiFundamental_barUpBlock`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L287).

> The two colour indices of the conjugate up-type block carry one fundamental and one
> anti-fundamental `su(3)` index, the conjugate quark doublet supplying the fundamental
> one.

```lean
lemma isSU3FundamentalAntiFundamental_barUpBlock (f f' : Fin 3) (i su sbQ wbQ : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 3 => h.barUpBlock f f' i su (l 1) sbQ (l 0) wbQ)
```

**`StandardModel.CovAlgebraRealization.isSU2BiFundamental_barUpBlock`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L304).

> The two isospin indices of the conjugate up-type block are both fundamental: the
> conjugate Higgs symbol and the conjugate quark doublet both carry the fundamental of
> `su(2)`.

```lean
lemma isSU2BiFundamental_barUpBlock (f f' : Fin 3) (su : Fin 2) (cu : Fin 3)
    (sbQ : Fin 2) (cbQ : Fin 3) :
    IsSU2BiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.barUpBlock f f' (l 0) su cu sbQ cbQ (l 1))
```

**`StandardModel.CovAlgebraRealization.isBiDualRightWeyl_barUpBlock`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L317).

> The two spinor indices of the conjugate up-type block are both dual right-handed.

```lean
lemma isBiDualRightWeyl_barUpBlock (f f' : Fin 3) (i : Fin 2) (cu cbQ : Fin 3)
    (wbQ : Fin 2) :
    IsBiDualRightWeyl B repLorentz
      (ofPairComponents fun a b => h.barUpBlock f f' i a cu b cbQ wbQ)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_barUpBlock`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L335).

> A hypercharge transformation fixes every component of the conjugate up-type block, the
> three hypercharges `3`, `-4` and `1` cancelling.

```lean
lemma repGauge_u1_barUpBlock (t : unitary ℂ) (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3)
    (sbQ : Fin 2) (cbQ : Fin 3) (wbQ : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barUpBlock f f' i su cu sbQ cbQ wbQ)
      = h.barUpBlock f f' i su cu sbQ cbQ wbQ
```

**`StandardModel.CovAlgebraRealization.barUpBlockColour`**, a def, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L348).

> The colour contraction of the conjugate up-type block.

```lean
noncomputable def barUpBlockColour (f f' : Fin 3) (i su sbQ wbQ : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.barUpBlockColour_eq`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L353).

> The colour contraction of the conjugate up-type block written out.

```lean
lemma barUpBlockColour_eq (f f' : Fin 3) (i su sbQ wbQ : Fin 2) :
    h.barUpBlockColour f f' i su sbQ wbQ
      = ∑ a : Fin 3, h.barUpBlock f f' i su a sbQ a wbQ
```

**`StandardModel.CovAlgebraRealization.isSU2BiFundamental_barUpBlockColour`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L360).

> The colour contraction of the conjugate up-type block still carries two fundamental
> isospin indices.

```lean
lemma isSU2BiFundamental_barUpBlockColour (f f' : Fin 3) (su sbQ : Fin 2) :
    IsSU2BiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.barUpBlockColour f f' (l 0) su sbQ (l 1))
```

**`StandardModel.CovAlgebraRealization.barUpBlockIsospin`**, a def, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L368).

> The isospin contraction of the colour-contracted conjugate up-type block, by the
> antisymmetric symbol.

```lean
noncomputable def barUpBlockIsospin (f f' : Fin 3) (su sbQ : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.barUpBlockIsospin_eq`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L373).

> The doubly contracted conjugate up-type block written out.

```lean
lemma barUpBlockIsospin_eq (f f' : Fin 3) (su sbQ : Fin 2) :
    h.barUpBlockIsospin f f' su sbQ = (∑ a : Fin 3, h.barUpBlock f f' 0 su a sbQ a 1)
      - ∑ a : Fin 3, h.barUpBlock f f' 1 su a sbQ a 0
```

**`StandardModel.CovAlgebraRealization.isBiDualRightWeyl_barUpBlockIsospin`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L381).

> The doubly contracted conjugate up-type block carries two dual right-handed Weyl
> indices.

```lean
lemma isBiDualRightWeyl_barUpBlockIsospin (f f' : Fin 3) :
    IsBiDualRightWeyl B repLorentz (ofPairComponents (h.barUpBlockIsospin f f'))
```

**`StandardModel.CovAlgebraRealization.barUpYukawa`**, a def, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L391).

> The conjugate up-type Yukawa term of the family pair `(f, f')`. It is the image of the metric
> `εR'` under the map with the contracted block as its components.

```lean
noncomputable def barUpYukawa (f f' : Fin 3) : B
```

## D. The invariance of the conjugate up-type Yukawa term, and its mass weight

**`StandardModel.CovAlgebraRealization.repGauge_su3_barUpBlockColour`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L401).

> The colour contraction of the conjugate up-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_barUpBlockColour (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i su sbQ wbQ : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.barUpBlockColour f f' i su sbQ wbQ)
      = h.barUpBlockColour f f' i su sbQ wbQ
```

**`StandardModel.CovAlgebraRealization.repGauge_su3_barUpBlockIsospin`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L409).

> The doubly contracted conjugate up-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_barUpBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (su sbQ : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.barUpBlockIsospin f f' su sbQ)
      = h.barUpBlockIsospin f f' su sbQ
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_barUpBlockIsospin`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L417).

> The doubly contracted conjugate up-type block is fixed by the isospin factor.

```lean
lemma repGauge_su2_barUpBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (su sbQ : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.barUpBlockIsospin f f' su sbQ)
      = h.barUpBlockIsospin f f' su sbQ
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_barUpBlockIsospin`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L425).

> The doubly contracted conjugate up-type block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_barUpBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (su sbQ : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barUpBlockIsospin f f' su sbQ)
      = h.barUpBlockIsospin f f' su sbQ
```

**`StandardModel.CovAlgebraRealization.repGauge_barUpYukawa`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L434).

> The conjugate up-type Yukawa term is gauge invariant.

```lean
lemma repGauge_barUpYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGauge g (h.barUpYukawa f f') = h.barUpYukawa f f'
```

**`StandardModel.CovAlgebraRealization.repLorentz_barUpYukawa`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L443).

> The conjugate up-type Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_barUpYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentz Λ (h.barUpYukawa f f') = h.barUpYukawa f f'
```

**`StandardModel.CovAlgebraRealization.barUpBlock_mem_sectorMassWeight`**, a lemma, [line 450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L450).

> Every component of the conjugate up-type block sits at mass weight eight in the Yukawa
> sector.

```lean
lemma barUpBlock_mem_sectorMassWeight (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3)
    (sbQ : Fin 2) (cbQ : Fin 3) (wbQ : Fin 2) :
    h.barUpBlock f f' i su cu sbQ cbQ wbQ
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.barUpYukawa_mem_sectorMassWeight`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L460).

> The conjugate up-type Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma barUpYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    h.barUpYukawa f f'
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

## E. The conjugate charged-lepton Yukawa term

> The conjugate of the charged-lepton type: the product `barH L bare`.  As with its
> unconjugated partner there is no colour at all, so the colour step is plain invariance;
> isospin is `2 ⊗ 2̄` with the conjugate Higgs symbol supplying the fundamental index, and
> both fermions are left-handed.

**`StandardModel.CovAlgebraRealization.barLeptonBlock`**, a def, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L485).

> The components of the conjugate charged-lepton Yukawa block `barH L bare`.

```lean
noncomputable def barLeptonBlock (f f' : Fin 3) (i sL wL sbe : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.repGauge_su3_barLeptonBlock`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L490).

> The conjugate lepton block is colour invariant outright.

```lean
lemma repGauge_su3_barLeptonBlock (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i sL wL sbe : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.barLeptonBlock f f' i sL wL sbe)
      = h.barLeptonBlock f f' i sL wL sbe
```

**`StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_barLeptonBlock`**, a lemma, [line 500](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L500).

> The two isospin indices of the conjugate lepton block carry one fundamental and one
> anti-fundamental `su(2)` index, the conjugate Higgs symbol supplying the fundamental
> one.

```lean
lemma isSU2FundamentalAntiFundamental_barLeptonBlock (f f' : Fin 3) (sL sbe : Fin 2) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.barLeptonBlock f f' (l 0) sL (l 1) sbe)
```

**`StandardModel.CovAlgebraRealization.isBiDualLeftWeyl_barLeptonBlock`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L513).

> The two spinor indices of the conjugate lepton block are both dual left-handed.

```lean
lemma isBiDualLeftWeyl_barLeptonBlock (f f' : Fin 3) (i wL : Fin 2) :
    IsBiDualLeftWeyl B repLorentz
      (ofPairComponents fun a b => h.barLeptonBlock f f' i a wL b)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_barLeptonBlock`**, a lemma, [line 530](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L530).

> A hypercharge transformation fixes every component of the conjugate lepton block, the
> three hypercharges `3`, `3` and `-6` cancelling.

```lean
lemma repGauge_u1_barLeptonBlock (t : unitary ℂ) (f f' : Fin 3) (i sL wL sbe : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barLeptonBlock f f' i sL wL sbe)
      = h.barLeptonBlock f f' i sL wL sbe
```

**`StandardModel.CovAlgebraRealization.barLeptonBlockIsospin`**, a def, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L543).

> The isospin contraction of the conjugate lepton block.

```lean
noncomputable def barLeptonBlockIsospin (f f' : Fin 3) (sL sbe : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.barLeptonBlockIsospin_eq`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L548).

> The isospin contraction of the conjugate lepton block written out.

```lean
lemma barLeptonBlockIsospin_eq (f f' : Fin 3) (sL sbe : Fin 2) :
    h.barLeptonBlockIsospin f f' sL sbe
      = ∑ w : Fin 2, h.barLeptonBlock f f' w sL w sbe
```

**`StandardModel.CovAlgebraRealization.isBiDualLeftWeyl_barLeptonBlockIsospin`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L555).

> The contracted conjugate lepton block carries two dual left-handed Weyl indices.

```lean
lemma isBiDualLeftWeyl_barLeptonBlockIsospin (f f' : Fin 3) :
    IsBiDualLeftWeyl B repLorentz (ofPairComponents (h.barLeptonBlockIsospin f f'))
```

**`StandardModel.CovAlgebraRealization.barLeptonYukawa`**, a def, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L563).

> The conjugate charged-lepton Yukawa term of the family pair `(f, f')`. It is the image of the
> metric `εL'` under the map with the contracted block as its components.

```lean
noncomputable def barLeptonYukawa (f f' : Fin 3) : B
```

## F. The invariance of the conjugate charged-lepton Yukawa term, and its mass weight

**`StandardModel.CovAlgebraRealization.repGauge_su3_barLeptonBlockIsospin`**, a lemma, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L573).

> The contracted conjugate lepton block is fixed by the colour factor.

```lean
lemma repGauge_su3_barLeptonBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ)
    (f f' : Fin 3) (sL sbe : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.barLeptonBlockIsospin f f' sL sbe)
      = h.barLeptonBlockIsospin f f' sL sbe
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_barLeptonBlockIsospin`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L581).

> The contracted conjugate lepton block is fixed by the isospin factor.

```lean
lemma repGauge_su2_barLeptonBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ)
    (f f' : Fin 3) (sL sbe : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.barLeptonBlockIsospin f f' sL sbe)
      = h.barLeptonBlockIsospin f f' sL sbe
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_barLeptonBlockIsospin`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L589).

> The contracted conjugate lepton block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_barLeptonBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (sL sbe : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barLeptonBlockIsospin f f' sL sbe)
      = h.barLeptonBlockIsospin f f' sL sbe
```

**`StandardModel.CovAlgebraRealization.repGauge_barLeptonYukawa`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L596).

> The conjugate charged-lepton Yukawa term is gauge invariant.

```lean
lemma repGauge_barLeptonYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGauge g (h.barLeptonYukawa f f') = h.barLeptonYukawa f f'
```

**`StandardModel.CovAlgebraRealization.repLorentz_barLeptonYukawa`**, a lemma, [line 605](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L605).

> The conjugate charged-lepton Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_barLeptonYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentz Λ (h.barLeptonYukawa f f') = h.barLeptonYukawa f f'
```

**`StandardModel.CovAlgebraRealization.barLeptonBlock_mem_sectorMassWeight`**, a lemma, [line 612](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L612).

> Every component of the conjugate lepton block sits at mass weight eight in the Yukawa
> sector.

```lean
lemma barLeptonBlock_mem_sectorMassWeight (f f' : Fin 3) (i sL wL sbe : Fin 2) :
    h.barLeptonBlock f f' i sL wL sbe
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.barLeptonYukawa_mem_sectorMassWeight`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L622).

> The conjugate charged-lepton Yukawa term sits at mass weight eight in the Yukawa
> sector.

```lean
lemma barLeptonYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    h.barLeptonYukawa f f'
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

## G. The Yukawa span

> The six couplings, each joined over the nine family pairs, are the whole Yukawa content of
> the sector at mass weight eight: six arbitrary `3 × 3` coupling matrices, and no matrix
> written down anywhere.  The join lies inside the sector and inside both spaces of
> invariants, which is the direction that makes the eventual classification an equivalence
> rather than a one-way inclusion.  The six transposed blocks add nothing: by
> `mul_mul_swap_eq_neg` their terms are minus these.

**`StandardModel.CovAlgebraRealization.barDownYukawaSpan`**, a def, [line 644](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L644).

> The span of the conjugate down-type Yukawa terms over the nine family pairs.

```lean
noncomputable def barDownYukawaSpan : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.barUpYukawaSpan`**, a def, [line 648](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L648).

> The span of the conjugate up-type Yukawa terms over the nine family pairs.

```lean
noncomputable def barUpYukawaSpan : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.barLeptonYukawaSpan`**, a def, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L652).

> The span of the conjugate charged-lepton Yukawa terms over the nine family pairs.

```lean
noncomputable def barLeptonYukawaSpan : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.barDownYukawaSpan_le_sectorMassWeight`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L656).

> The conjugate down-type Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma barDownYukawaSpan_le_sectorMassWeight :
    h.barDownYukawaSpan
      ≤ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.barDownYukawaSpan_le_invariants`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L663).

> The conjugate down-type Yukawa span is a space of gauge invariants.

```lean
lemma barDownYukawaSpan_le_invariants : h.barDownYukawaSpan ≤ repGauge.invariants
```

**`StandardModel.CovAlgebraRealization.barDownYukawaSpan_le_lorentzInvariants`**, a lemma, [line 668](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L668).

> The conjugate down-type Yukawa span is a space of Lorentz invariants.

```lean
lemma barDownYukawaSpan_le_lorentzInvariants :
    h.barDownYukawaSpan ≤ repLorentz.invariants
```

**`StandardModel.CovAlgebraRealization.barUpYukawaSpan_le_sectorMassWeight`**, a lemma, [line 674](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L674).

> The conjugate up-type Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma barUpYukawaSpan_le_sectorMassWeight :
    h.barUpYukawaSpan
      ≤ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.barUpYukawaSpan_le_invariants`**, a lemma, [line 681](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L681).

> The conjugate up-type Yukawa span is a space of gauge invariants.

```lean
lemma barUpYukawaSpan_le_invariants : h.barUpYukawaSpan ≤ repGauge.invariants
```

**`StandardModel.CovAlgebraRealization.barUpYukawaSpan_le_lorentzInvariants`**, a lemma, [line 686](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L686).

> The conjugate up-type Yukawa span is a space of Lorentz invariants.

```lean
lemma barUpYukawaSpan_le_lorentzInvariants : h.barUpYukawaSpan ≤ repLorentz.invariants
```

**`StandardModel.CovAlgebraRealization.barLeptonYukawaSpan_le_sectorMassWeight`**, a lemma, [line 692](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L692).

> The conjugate charged-lepton Yukawa span sits at mass weight eight in the Yukawa
> sector.

```lean
lemma barLeptonYukawaSpan_le_sectorMassWeight :
    h.barLeptonYukawaSpan
      ≤ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.barLeptonYukawaSpan_le_invariants`**, a lemma, [line 699](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L699).

> The conjugate charged-lepton Yukawa span is a space of gauge invariants.

```lean
lemma barLeptonYukawaSpan_le_invariants : h.barLeptonYukawaSpan ≤ repGauge.invariants
```

**`StandardModel.CovAlgebraRealization.barLeptonYukawaSpan_le_lorentzInvariants`**, a lemma, [line 704](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L704).

> The conjugate charged-lepton Yukawa span is a space of Lorentz invariants.

```lean
lemma barLeptonYukawaSpan_le_lorentzInvariants :
    h.barLeptonYukawaSpan ≤ repLorentz.invariants
```

**`StandardModel.CovAlgebraRealization.yukawaSpan`**, a def, [line 711](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L711).

> The Yukawa span of the Standard Model at mass weight eight: the join of the six
> couplings, each over the nine family pairs.

```lean
noncomputable def yukawaSpan : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.yukawaSpan_le_inf`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean#L719).

> The Yukawa span lies inside the gauge- and Lorentz-invariants of the Yukawa sector at
> mass weight eight. This is the easy direction of the classification: every Yukawa term
> is an invariant of the right mass weight, so the eventual classification is an
> equivalence and not merely a one-way inclusion.

```lean
lemma yukawaSpan_le_inf :
    h.yukawaSpan ≤ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
        ⊓ repGauge.invariants ⊓ repLorentz.invariants
```

## Depends on

- [The Yukawa terms built on the Higgs symbol](covrealization-yukawasector-families-higgs.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/BarHiggs.lean)
