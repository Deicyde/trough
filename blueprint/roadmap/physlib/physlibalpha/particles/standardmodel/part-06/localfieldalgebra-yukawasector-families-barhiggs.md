---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.barDownBlock, StandardModel.LocalCovFieldAlgebra.isEquivariant_colourFundAntiFund_barDownBlock, StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_barDownBlock, StandardModel.LocalCovFieldAlgebra.isEquivariant_downLDownL_barDownBlock, StandardModel.LocalCovFieldAlgebra.repGauge_u1_barDownBlock, StandardModel.LocalCovFieldAlgebra.barDownBlockColour, StandardModel.LocalCovFieldAlgebra.barDownBlockColour_eq, StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_barDownBlockColour
statement: formalized
proof: formalized
---

# The Yukawa terms built on the conjugate Higgs symbol

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.YukawaSector.Families.BarHiggs`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean): 70 declarations, 70 with a docstring.

> The conjugate-Higgs-type Yukawa terms of the Standard Model's covariant field algebra.

## i. Overview

> Everything below is stated about the covariant field algebra `fieldData.LocalCovFieldAlgebra` of the
> Standard Model.
>
> The remaining three couplings of the mass-weight-eight Yukawa sector are built on the
> conjugate Higgs symbol, `barH bard Q`, `barH u barQ` and `barH L bare`.  Each is the
> conjugate of one of the three couplings of `Families/Higgs.lean`, and is the same computation
> with every symbol replaced by its conjugate. Fundamental and anti-fundamental indices
> exchange, left- and right-handed spinors exchange, and every hypercharge changes sign.  So
> the isospin structure of the conjugate up type is `2 ⊗ 2` where its partner had `2̄ ⊗ 2̄`,
> and its invariant is again the antisymmetric symbol.
>
> With these six couplings the twelve blocks are accounted for. The other six are the same
> six with the two fermion factors exchanged, and by `mul_mul_swap_eq_neg` their terms are
> minus these while by `mul_mul_piece_swap` their blocks are the same submodules.

## ii. Key results

> - `barDownYukawa`, `barUpYukawa`, `barLeptonYukawa` : the three conjugate Yukawa terms.
> - `isEquivariant_colourFundAntiFund_barDownBlock`, `isEquivariant_isospinFundFund_barUpBlock` and
>   the rest : the index laws of the three conjugate blocks.
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

**`StandardModel.LocalCovFieldAlgebra.barDownBlock`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L83).

> The components of the conjugate down-type Yukawa block `barH bard Q`, a conjugate
> Higgs symbol, a conjugate down-singlet symbol and a quark-doublet symbol, none carrying
> derivatives.

```lean
noncomputable def barDownBlock (f f' : Fin 3) (i sbd : Fin 2) (cbd : Fin 3) (sQ : Fin 2)
    (cQ : Fin 3) (wQ : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_colourFundAntiFund_barDownBlock`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L91).

> The two colour indices of the conjugate down-type block carry one fundamental and one
> anti-fundamental `su(3)` index, the conjugate down singlet supplying the fundamental
> one.

```lean
lemma isEquivariant_colourFundAntiFund_barDownBlock (f f' : Fin 3) (i sbd sQ wQ : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun l : Fin 2 → Fin 3 =>
        LocalCovFieldAlgebra.barDownBlock f f' i sbd (l 0) sQ (l 1) wQ) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_barDownBlock`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L108).

> The two isospin indices of the conjugate down-type block carry one fundamental and one
> anti-fundamental `su(2)` index, the conjugate Higgs symbol supplying the fundamental
> one.

```lean
lemma isEquivariant_isospinFundAntiFund_barDownBlock (f f' : Fin 3) (sbd : Fin 2) (cbd : Fin 3)
    (sQ : Fin 2) (cQ : Fin 3) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun l : Fin 2 → Fin 2 =>
        LocalCovFieldAlgebra.barDownBlock f f' (l 0) sbd cbd sQ cQ (l 1)) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downLDownL_barDownBlock`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L124).

> The two spinor indices of the conjugate down-type block are both dual left-handed.

```lean
lemma isEquivariant_downLDownL_barDownBlock (f f' : Fin 3) (i : Fin 2) (cbd cQ : Fin 3)
    (wQ : Fin 2) :
    complexLorentzTensor.IsEquivariant ![.downL, .downL] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.barDownBlock f f' i p.1 cbd p.2 cQ wQ) ∘
          pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_barDownBlock`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L144).

> A hypercharge transformation fixes every component of the conjugate down-type block,
> the three hypercharges `3`, `-2` and `-1` cancelling.

```lean
lemma repGauge_u1_barDownBlock (t : unitary ℂ) (f f' : Fin 3) (i sbd : Fin 2)
    (cbd : Fin 3) (sQ : Fin 2) (cQ : Fin 3) (wQ : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.barDownBlock f f' i
      sbd cbd sQ cQ wQ)
      = LocalCovFieldAlgebra.barDownBlock f f' i sbd cbd sQ cQ wQ
```

**`StandardModel.LocalCovFieldAlgebra.barDownBlockColour`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L160).

> The colour contraction of the conjugate down-type block.

```lean
noncomputable def barDownBlockColour (f f' : Fin 3)
    (i sbd sQ wQ : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barDownBlockColour_eq`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L166).

> The colour contraction of the conjugate down-type block written out.

```lean
lemma barDownBlockColour_eq (f f' : Fin 3) (i sbd sQ wQ : Fin 2) :
    LocalCovFieldAlgebra.barDownBlockColour f f' i sbd sQ wQ
      = ∑ a : Fin 3, LocalCovFieldAlgebra.barDownBlock f f' i sbd a sQ a wQ
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_barDownBlockColour`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L173).

> The colour contraction of the conjugate down-type block still carries one fundamental
> and one anti-fundamental isospin index.

```lean
lemma isEquivariant_isospinFundAntiFund_barDownBlockColour (f f' : Fin 3) (sbd sQ : Fin 2) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun l : Fin 2 → Fin 2 =>
        LocalCovFieldAlgebra.barDownBlockColour f f' (l 0) sbd sQ (l 1)) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.barDownBlockIsospin`**, a def, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L182).

> The isospin contraction of the colour-contracted conjugate down-type block.

```lean
noncomputable def barDownBlockIsospin (f f' : Fin 3)
    (sbd sQ : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barDownBlockIsospin_eq`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L188).

> The doubly contracted conjugate down-type block written out.

```lean
lemma barDownBlockIsospin_eq (f f' : Fin 3) (sbd sQ : Fin 2) :
    LocalCovFieldAlgebra.barDownBlockIsospin f f' sbd sQ
      = ∑ p : Fin 2 × Fin 3, LocalCovFieldAlgebra.barDownBlock f f' p.1 sbd p.2 sQ p.2 p.1
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downLDownL_barDownBlockIsospin`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L198).

> The doubly contracted conjugate down-type block carries two dual left-handed Weyl
> indices.

```lean
lemma isEquivariant_downLDownL_barDownBlockIsospin (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.downL, .downL] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.barDownBlockIsospin f f' p.1 p.2) ∘
          pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.barDownYukawa`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L208).

> The conjugate down-type Yukawa term of the family pair `(f, f')`. It is the image of the metric
> `εL'` under the map with the contracted block as its components.

```lean
noncomputable def barDownYukawa (f f' : Fin 3) : fieldData.LocalCovFieldAlgebra
```

## B. The invariance of the conjugate down-type Yukawa term, and its mass weight

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_barDownBlockColour`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L220).

> The colour contraction of the conjugate down-type block is fixed by the colour
> factor.

```lean
lemma repGauge_su3_barDownBlockColour (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i sbd sQ wQ : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.barDownBlockColour
      f f' i sbd sQ wQ)
      = LocalCovFieldAlgebra.barDownBlockColour f f' i sbd sQ wQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_barDownBlockIsospin`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L229).

> The doubly contracted conjugate down-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_barDownBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (sbd sQ : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.barDownBlockIsospin
      f f' sbd sQ)
      = LocalCovFieldAlgebra.barDownBlockIsospin f f' sbd sQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su2_barDownBlockIsospin`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L239).

> The doubly contracted conjugate down-type block is fixed by the isospin factor.

```lean
lemma repGauge_su2_barDownBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (sbd sQ : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (LocalCovFieldAlgebra.barDownBlockIsospin
      f f' sbd sQ)
      = LocalCovFieldAlgebra.barDownBlockIsospin f f' sbd sQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_barDownBlockIsospin`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L248).

> The doubly contracted conjugate down-type block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_barDownBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (sbd sQ : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.barDownBlockIsospin
      f f' sbd sQ)
      = LocalCovFieldAlgebra.barDownBlockIsospin f f' sbd sQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_barDownYukawa`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L257).

> The conjugate down-type Yukawa term is gauge invariant.

```lean
lemma repGauge_barDownYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGaugeGroupI g (LocalCovFieldAlgebra.barDownYukawa f f') =
      LocalCovFieldAlgebra.barDownYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_barDownYukawa`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L267).

> The conjugate down-type Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_barDownYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentzGroup Λ (LocalCovFieldAlgebra.barDownYukawa f f') =
      LocalCovFieldAlgebra.barDownYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.barDownBlock_mem_sectorMassWeight`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L275).

> Every component of the conjugate down-type block sits at mass weight eight in the
> Yukawa sector.

```lean
lemma barDownBlock_mem_sectorMassWeight (f f' : Fin 3) (i sbd : Fin 2) (cbd : Fin 3)
    (sQ : Fin 2) (cQ : Fin 3) (wQ : Fin 2) :
    LocalCovFieldAlgebra.barDownBlock f f' i sbd cbd sQ cQ wQ
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.barDownYukawa_mem_sectorMassWeight`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L285).

> The conjugate down-type Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma barDownYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    LocalCovFieldAlgebra.barDownYukawa f f'
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

## C. The conjugate up-type Yukawa term

> The conjugate of the up type: the product `barH u barQ`.  Colour is `3 ⊗ 3̄` with the
> conjugate quark doublet supplying the fundamental index, isospin is `2 ⊗ 2` — the conjugate
> Higgs symbol and the conjugate quark doublet both carry the fundamental, so the invariant
> is again the antisymmetric symbol — and both fermions are right-handed.

**`StandardModel.LocalCovFieldAlgebra.barUpBlock`**, a def, [line 305](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L305).

> The components of the conjugate up-type Yukawa block `barH u barQ`.

```lean
noncomputable def barUpBlock (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3) (sbQ : Fin 2)
    (cbQ : Fin 3) (wbQ : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_colourFundAntiFund_barUpBlock`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L313).

> The two colour indices of the conjugate up-type block carry one fundamental and one
> anti-fundamental `su(3)` index, the conjugate quark doublet supplying the fundamental
> one.

```lean
lemma isEquivariant_colourFundAntiFund_barUpBlock (f f' : Fin 3) (i su sbQ wbQ : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun l : Fin 2 → Fin 3 => LocalCovFieldAlgebra.barUpBlock f f' i su (l 1) sbQ
          (l 0) wbQ) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundFund_barUpBlock`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L332).

> The two isospin indices of the conjugate up-type block are both fundamental. The
> conjugate Higgs symbol and the conjugate quark doublet both carry the fundamental of
> `su(2)`.

```lean
lemma isEquivariant_isospinFundFund_barUpBlock (f f' : Fin 3) (su : Fin 2) (cu : Fin 3)
    (sbQ : Fin 2) (cbQ : Fin 3) :
    (suTensor 2).IsEquivariant (fun _ : Fin 2 => .fund) (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents (fun l : Fin 2 → Fin 2 => LocalCovFieldAlgebra.barUpBlock f f' (l 0) su cu sbQ
          cbQ (l 1)))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downRDownR_barUpBlock`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L348).

> The two spinor indices of the conjugate up-type block are both dual right-handed.

```lean
lemma isEquivariant_downRDownR_barUpBlock (f f' : Fin 3) (i : Fin 2) (cu cbQ : Fin 3)
    (wbQ : Fin 2) :
    complexLorentzTensor.IsEquivariant ![.downR, .downR] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.barUpBlock f f' i p.1 cu p.2 cbQ wbQ) ∘
          pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_barUpBlock`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L368).

> A hypercharge transformation fixes every component of the conjugate up-type block, the
> three hypercharges `3`, `-4` and `1` cancelling.

```lean
lemma repGauge_u1_barUpBlock (t : unitary ℂ) (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3)
    (sbQ : Fin 2) (cbQ : Fin 3) (wbQ : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.barUpBlock f f' i
      su cu sbQ cbQ wbQ)
      = LocalCovFieldAlgebra.barUpBlock f f' i su cu sbQ cbQ wbQ
```

**`StandardModel.LocalCovFieldAlgebra.barUpBlockColour`**, a def, [line 384](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L384).

> The colour contraction of the conjugate up-type block.

```lean
noncomputable def barUpBlockColour (f f' : Fin 3)
    (i su sbQ wbQ : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barUpBlockColour_eq`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L390).

> The colour contraction of the conjugate up-type block written out.

```lean
lemma barUpBlockColour_eq (f f' : Fin 3) (i su sbQ wbQ : Fin 2) :
    LocalCovFieldAlgebra.barUpBlockColour f f' i su sbQ wbQ
      = ∑ a : Fin 3, LocalCovFieldAlgebra.barUpBlock f f' i su a sbQ a wbQ
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundFund_barUpBlockColour`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L397).

> The colour contraction of the conjugate up-type block still carries two fundamental
> isospin indices.

```lean
lemma isEquivariant_isospinFundFund_barUpBlockColour (f f' : Fin 3) (su sbQ : Fin 2) :
    (suTensor 2).IsEquivariant (fun _ : Fin 2 => .fund) (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents (fun l : Fin 2 → Fin 2 => LocalCovFieldAlgebra.barUpBlockColour f f' (l 0) su
          sbQ (l 1)))
```

**`StandardModel.LocalCovFieldAlgebra.barUpBlockIsospin`**, a def, [line 408](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L408).

> The isospin contraction of the colour-contracted conjugate up-type block, by the
> antisymmetric symbol.

```lean
noncomputable def barUpBlockIsospin (f f' : Fin 3)
    (su sbQ : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barUpBlockIsospin_eq`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L414).

> The doubly contracted conjugate up-type block written out.

```lean
lemma barUpBlockIsospin_eq (f f' : Fin 3) (su sbQ : Fin 2) :
    LocalCovFieldAlgebra.barUpBlockIsospin f f' su sbQ =
      (∑ a : Fin 3, LocalCovFieldAlgebra.barUpBlock f f' 0 su a sbQ a 1)
      - ∑ a : Fin 3, LocalCovFieldAlgebra.barUpBlock f f' 1 su a sbQ a 0
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downRDownR_barUpBlockIsospin`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L423).

> The doubly contracted conjugate up-type block carries two dual right-handed Weyl
> indices.

```lean
lemma isEquivariant_downRDownR_barUpBlockIsospin (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.downR, .downR] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.barUpBlockIsospin f f' p.1 p.2) ∘
          pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.barUpYukawa`**, a def, [line 437](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L437).

> The conjugate up-type Yukawa term of the family pair `(f, f')`. It is the image of the metric
> `εR'` under the map with the contracted block as its components.

```lean
noncomputable def barUpYukawa (f f' : Fin 3) : fieldData.LocalCovFieldAlgebra
```

## D. The invariance of the conjugate up-type Yukawa term, and its mass weight

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_barUpBlockColour`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L448).

> The colour contraction of the conjugate up-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_barUpBlockColour (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i su sbQ wbQ : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.barUpBlockColour f
      f' i su sbQ wbQ)
      = LocalCovFieldAlgebra.barUpBlockColour f f' i su sbQ wbQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_barUpBlockIsospin`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L457).

> The doubly contracted conjugate up-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_barUpBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (su sbQ : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.barUpBlockIsospin f
      f' su sbQ)
      = LocalCovFieldAlgebra.barUpBlockIsospin f f' su sbQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su2_barUpBlockIsospin`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L467).

> The doubly contracted conjugate up-type block is fixed by the isospin factor.

```lean
lemma repGauge_su2_barUpBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (su sbQ : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (LocalCovFieldAlgebra.barUpBlockIsospin f
      f' su sbQ)
      = LocalCovFieldAlgebra.barUpBlockIsospin f f' su sbQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_barUpBlockIsospin`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L476).

> The doubly contracted conjugate up-type block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_barUpBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (su sbQ : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.barUpBlockIsospin f
      f' su sbQ)
      = LocalCovFieldAlgebra.barUpBlockIsospin f f' su sbQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_barUpYukawa`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L488).

> The conjugate up-type Yukawa term is gauge invariant.

```lean
lemma repGauge_barUpYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGaugeGroupI g (LocalCovFieldAlgebra.barUpYukawa f f') =
      LocalCovFieldAlgebra.barUpYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_barUpYukawa`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L498).

> The conjugate up-type Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_barUpYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentzGroup Λ (LocalCovFieldAlgebra.barUpYukawa f f') =
      LocalCovFieldAlgebra.barUpYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.barUpBlock_mem_sectorMassWeight`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L506).

> Every component of the conjugate up-type block sits at mass weight eight in the Yukawa
> sector.

```lean
lemma barUpBlock_mem_sectorMassWeight (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3)
    (sbQ : Fin 2) (cbQ : Fin 3) (wbQ : Fin 2) :
    LocalCovFieldAlgebra.barUpBlock f f' i su cu sbQ cbQ wbQ
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.barUpYukawa_mem_sectorMassWeight`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L516).

> The conjugate up-type Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma barUpYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    LocalCovFieldAlgebra.barUpYukawa f f'
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

## E. The conjugate charged-lepton Yukawa term

> The conjugate of the charged-lepton type: the product `barH L bare`.  As with its
> unconjugated partner there is no colour at all, so the colour step is plain invariance;
> isospin is `2 ⊗ 2̄` with the conjugate Higgs symbol supplying the fundamental index, and
> both fermions are left-handed.

**`StandardModel.LocalCovFieldAlgebra.barLeptonBlock`**, a def, [line 541](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L541).

> The components of the conjugate charged-lepton Yukawa block `barH L bare`.

```lean
noncomputable def barLeptonBlock (f f' : Fin 3)
    (i sL wL sbe : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_barLeptonBlock`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L547).

> The conjugate lepton block is colour invariant outright.

```lean
lemma repGauge_su3_barLeptonBlock (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i sL wL sbe : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.barLeptonBlock f f'
      i sL wL sbe)
      = LocalCovFieldAlgebra.barLeptonBlock f f' i sL wL sbe
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_barLeptonBlock`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L559).

> The two isospin indices of the conjugate lepton block carry one fundamental and one
> anti-fundamental `su(2)` index, the conjugate Higgs symbol supplying the fundamental
> one.

```lean
lemma isEquivariant_isospinFundAntiFund_barLeptonBlock (f f' : Fin 3) (sL sbe : Fin 2) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun l : Fin 2 → Fin 2 => LocalCovFieldAlgebra.barLeptonBlock f f' (l 0) sL
          (l 1) sbe) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downLDownL_barLeptonBlock`**, a lemma, [line 574](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L574).

> The two spinor indices of the conjugate lepton block are both dual left-handed.

```lean
lemma isEquivariant_downLDownL_barLeptonBlock (f f' : Fin 3) (i wL : Fin 2) :
    complexLorentzTensor.IsEquivariant ![.downL, .downL] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.barLeptonBlock f f' i p.1 wL p.2) ∘
        pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_barLeptonBlock`**, a lemma, [line 593](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L593).

> A hypercharge transformation fixes every component of the conjugate lepton block, the
> three hypercharges `3`, `3` and `-6` cancelling.

```lean
lemma repGauge_u1_barLeptonBlock (t : unitary ℂ) (f f' : Fin 3) (i sL wL sbe : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.barLeptonBlock f f'
      i sL wL sbe)
      = LocalCovFieldAlgebra.barLeptonBlock f f' i sL wL sbe
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonBlockIsospin`**, a def, [line 608](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L608).

> The isospin contraction of the conjugate lepton block.

```lean
noncomputable def barLeptonBlockIsospin (f f' : Fin 3)
    (sL sbe : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonBlockIsospin_eq`**, a lemma, [line 614](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L614).

> The isospin contraction of the conjugate lepton block written out.

```lean
lemma barLeptonBlockIsospin_eq (f f' : Fin 3) (sL sbe : Fin 2) :
    LocalCovFieldAlgebra.barLeptonBlockIsospin f f' sL sbe
      = ∑ w : Fin 2, LocalCovFieldAlgebra.barLeptonBlock f f' w sL w sbe
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downLDownL_barLeptonBlockIsospin`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L621).

> The contracted conjugate lepton block carries two dual left-handed Weyl indices.

```lean
lemma isEquivariant_downLDownL_barLeptonBlockIsospin (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.downL, .downL] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.barLeptonBlockIsospin f f' p.1 p.2) ∘
          pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonYukawa`**, a def, [line 631](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L631).

> The conjugate charged-lepton Yukawa term of the family pair `(f, f')`. It is the image of the
> metric `εL'` under the map with the contracted block as its components.

```lean
noncomputable def barLeptonYukawa (f f' : Fin 3) : fieldData.LocalCovFieldAlgebra
```

## F. The invariance of the conjugate charged-lepton Yukawa term, and its mass weight

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_barLeptonBlockIsospin`**, a lemma, [line 643](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L643).

> The contracted conjugate lepton block is fixed by the colour factor.

```lean
lemma repGauge_su3_barLeptonBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ)
    (f f' : Fin 3) (sL sbe : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI)
      (LocalCovFieldAlgebra.barLeptonBlockIsospin f f' sL sbe)
      = LocalCovFieldAlgebra.barLeptonBlockIsospin f f' sL sbe
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su2_barLeptonBlockIsospin`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L653).

> The contracted conjugate lepton block is fixed by the isospin factor.

```lean
lemma repGauge_su2_barLeptonBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ)
    (f f' : Fin 3) (sL sbe : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI)
      (LocalCovFieldAlgebra.barLeptonBlockIsospin f f' sL sbe)
      = LocalCovFieldAlgebra.barLeptonBlockIsospin f f' sL sbe
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_barLeptonBlockIsospin`**, a lemma, [line 662](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L662).

> The contracted conjugate lepton block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_barLeptonBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (sL sbe : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI)
      (LocalCovFieldAlgebra.barLeptonBlockIsospin f f' sL sbe)
      = LocalCovFieldAlgebra.barLeptonBlockIsospin f f' sL sbe
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_barLeptonYukawa`**, a lemma, [line 671](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L671).

> The conjugate charged-lepton Yukawa term is gauge invariant.

```lean
lemma repGauge_barLeptonYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGaugeGroupI g (LocalCovFieldAlgebra.barLeptonYukawa f f') =
      LocalCovFieldAlgebra.barLeptonYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_barLeptonYukawa`**, a lemma, [line 681](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L681).

> The conjugate charged-lepton Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_barLeptonYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentzGroup Λ (LocalCovFieldAlgebra.barLeptonYukawa f f') =
      LocalCovFieldAlgebra.barLeptonYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonBlock_mem_sectorMassWeight`**, a lemma, [line 689](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L689).

> Every component of the conjugate lepton block sits at mass weight eight in the Yukawa
> sector.

```lean
lemma barLeptonBlock_mem_sectorMassWeight (f f' : Fin 3) (i sL wL sbe : Fin 2) :
    LocalCovFieldAlgebra.barLeptonBlock f f' i sL wL sbe
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonYukawa_mem_sectorMassWeight`**, a lemma, [line 699](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L699).

> The conjugate charged-lepton Yukawa term sits at mass weight eight in the Yukawa
> sector.

```lean
lemma barLeptonYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    LocalCovFieldAlgebra.barLeptonYukawa f f'
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

## G. The Yukawa span

> The six couplings, each joined over the nine family pairs, are the whole Yukawa content of
> the sector at mass weight eight: six arbitrary `3 × 3` coupling matrices, and no matrix
> written down anywhere.  The join lies inside the sector and inside both spaces of
> invariants, which is the direction that makes the eventual classification an equivalence
> rather than a one-way inclusion.  The six transposed blocks add nothing: by
> `mul_mul_swap_eq_neg` their terms are minus these.

**`StandardModel.LocalCovFieldAlgebra.barDownYukawaSpan`**, a def, [line 721](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L721).

> The span of the conjugate down-type Yukawa terms over the nine family pairs.

```lean
noncomputable def barDownYukawaSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barUpYukawaSpan`**, a def, [line 725](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L725).

> The span of the conjugate up-type Yukawa terms over the nine family pairs.

```lean
noncomputable def barUpYukawaSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonYukawaSpan`**, a def, [line 729](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L729).

> The span of the conjugate charged-lepton Yukawa terms over the nine family pairs.

```lean
noncomputable def barLeptonYukawaSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barDownYukawaSpan_le_sectorMassWeight`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L733).

> The conjugate down-type Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma barDownYukawaSpan_le_sectorMassWeight :
    LocalCovFieldAlgebra.barDownYukawaSpan
      ≤ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.barDownYukawaSpan_le_invariants`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L740).

> The conjugate down-type Yukawa span is a space of gauge invariants.

```lean
lemma barDownYukawaSpan_le_invariants : LocalCovFieldAlgebra.barDownYukawaSpan ≤
    repGaugeGroupI.invariants
```

**`StandardModel.LocalCovFieldAlgebra.barDownYukawaSpan_le_lorentzInvariants`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L746).

> The conjugate down-type Yukawa span is a space of Lorentz invariants.

```lean
lemma barDownYukawaSpan_le_lorentzInvariants :
    LocalCovFieldAlgebra.barDownYukawaSpan ≤ repLorentzGroup.invariants
```

**`StandardModel.LocalCovFieldAlgebra.barUpYukawaSpan_le_sectorMassWeight`**, a lemma, [line 752](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L752).

> The conjugate up-type Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma barUpYukawaSpan_le_sectorMassWeight :
    LocalCovFieldAlgebra.barUpYukawaSpan
      ≤ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.barUpYukawaSpan_le_invariants`**, a lemma, [line 759](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L759).

> The conjugate up-type Yukawa span is a space of gauge invariants.

```lean
lemma barUpYukawaSpan_le_invariants : LocalCovFieldAlgebra.barUpYukawaSpan ≤
    repGaugeGroupI.invariants
```

**`StandardModel.LocalCovFieldAlgebra.barUpYukawaSpan_le_lorentzInvariants`**, a lemma, [line 765](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L765).

> The conjugate up-type Yukawa span is a space of Lorentz invariants.

```lean
lemma barUpYukawaSpan_le_lorentzInvariants : LocalCovFieldAlgebra.barUpYukawaSpan ≤
    repLorentzGroup.invariants
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonYukawaSpan_le_sectorMassWeight`**, a lemma, [line 772](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L772).

> The conjugate charged-lepton Yukawa span sits at mass weight eight in the Yukawa
> sector.

```lean
lemma barLeptonYukawaSpan_le_sectorMassWeight :
    LocalCovFieldAlgebra.barLeptonYukawaSpan
      ≤ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonYukawaSpan_le_invariants`**, a lemma, [line 779](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L779).

> The conjugate charged-lepton Yukawa span is a space of gauge invariants.

```lean
lemma barLeptonYukawaSpan_le_invariants : LocalCovFieldAlgebra.barLeptonYukawaSpan ≤
    repGaugeGroupI.invariants
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonYukawaSpan_le_lorentzInvariants`**, a lemma, [line 785](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L785).

> The conjugate charged-lepton Yukawa span is a space of Lorentz invariants.

```lean
lemma barLeptonYukawaSpan_le_lorentzInvariants :
    LocalCovFieldAlgebra.barLeptonYukawaSpan ≤ repLorentzGroup.invariants
```

**`StandardModel.LocalCovFieldAlgebra.yukawaSpan`**, a def, [line 792](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L792).

> The Yukawa span of the Standard Model at mass weight eight, the join of the six
> couplings, each over the nine family pairs.

```lean
noncomputable def yukawaSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.yukawaSpan_le_inf`**, a lemma, [line 802](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean#L802).

> The Yukawa span lies inside the gauge- and Lorentz-invariants of the Yukawa sector at
> mass weight eight. This is the easy direction of the classification. Every Yukawa term
> is an invariant of the right mass weight, so the eventual classification is an
> equivalence and not merely a one-way inclusion.

```lean
lemma yukawaSpan_le_inf :
    LocalCovFieldAlgebra.yukawaSpan ≤ fieldData.sectorMassWeight
      {FieldKind.scalar, FieldKind.fermion} 8
        ⊓ repGaugeGroupI.invariants ⊓ repLorentzGroup.invariants
```

## Depends on

- [The Yukawa terms built on the Higgs symbol](../part-07/localfieldalgebra-yukawasector-families-higgs.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/BarHiggs.lean)
