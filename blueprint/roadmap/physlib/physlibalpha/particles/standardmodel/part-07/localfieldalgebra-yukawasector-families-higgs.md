---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.downBlock, StandardModel.LocalCovFieldAlgebra.isEquivariant_colourFundAntiFund_downBlock, StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_downBlock, StandardModel.LocalCovFieldAlgebra.isEquivariant_downRDownR_downBlock, StandardModel.LocalCovFieldAlgebra.repGauge_u1_downBlock, StandardModel.LocalCovFieldAlgebra.downBlockColour, StandardModel.LocalCovFieldAlgebra.downBlockColour_eq, StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_downBlockColour
statement: formalized
proof: formalized
---

# The Yukawa terms built on the Higgs symbol

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.YukawaSector.Families.Higgs`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean): 68 declarations, 68 with a docstring.

> The Higgs-type Yukawa terms of the Standard Model's covariant field algebra.

## i. Overview

> Everything below is stated about the covariant field algebra `fieldData.LocalCovFieldAlgebra` of the
> Standard Model.
>
> Three of the twelve blocks of the mass-weight-eight Yukawa sector are built on the Higgs
> symbol rather than its conjugate, the down type `H d barQ`, the up type `H baru Q` and the
> charged-lepton type `H barL e`.  They are the three genuinely distinct computations of the
> sector — the other nine blocks are their conjugates and the two fermion orderings of each —
> and this file builds, for each of them, the block, the index laws its three symbols obey,
> the iterated contraction those laws admit, and the proof that the contraction is a gauge-
> and Lorentz-invariant element of the sector at mass weight eight.
>
> The three differ in exactly two places. In isospin, the down and lepton types contract a
> `2 ⊗ 2̄` by the trace, the up type a `2̄ ⊗ 2̄` by the antisymmetric symbol, since the Higgs
> symbol and the quark doublet both carry the anti-fundamental. In colour, the two quark types
> contract a `3 ⊗ 3̄` by the Kronecker delta, while the lepton type carries no colour at all,
> so its colour step is plain invariance rather than a classification and its contraction has
> two stages instead of three.
>
> The transposed blocks — the same three triples with the two fermion factors exchanged — are
> not built here. They are minus these terms and span the same submodules, by
> `mul_mul_swap_eq_neg` and `mul_mul_piece_swap`.

## ii. Key results

> - `downYukawa`, `upYukawa`, `leptonYukawa` : the three Yukawa terms of a family pair.
> - `isEquivariant_colourFundAntiFund_downBlock`, `isEquivariant_isospinFundAntiFund_downBlock`,
>   `isEquivariant_downRDownR_downBlock` and their up-type and lepton-type counterparts : the index
>   laws of each block.
> - `repGauge_downYukawa`, `repLorentz_downYukawa` and their counterparts : the invariance of
>   each Yukawa term.
> - `downYukawaSpan`, `upYukawaSpan`, `leptonYukawaSpan` : the join over the nine family
>   pairs, which is the coupling with an arbitrary `3 × 3` matrix.

## iv. References

> * None.

## A. The down-type Yukawa term

> The first block, and the pattern for the other eleven.  The block is the product
> `H d barQ`; the conjugate quark doublet supplies the fundamental colour index and the
> fundamental isospin index, so it goes in the first slot of both mixed families, while the
> down singlet supplies the anti-fundamental colour index and the Higgs symbol the
> anti-fundamental isospin one.  Both fermions are right-handed.  The three contractions are
> then formed in turn, each one a spectator of the next.

**`StandardModel.LocalCovFieldAlgebra.downBlock`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L95).

> The components of the down-type Yukawa block `H d barQ`, a Higgs symbol, a
> down-singlet symbol and a conjugate quark-doublet symbol, none carrying derivatives,
> multiplied in the order in which the block of
> `sectorMassWeightEightGaugeWeight_piece_zero` multiplies them.

```lean
noncomputable def downBlock (f f' : Fin 3) (i sd : Fin 2) (cd : Fin 3) (sq : Fin 2)
    (cq : Fin 3) (wq : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_colourFundAntiFund_downBlock`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L103).

> The two colour indices of the down-type block carry one fundamental and one
> anti-fundamental `su(3)` index. The conjugate quark doublet supplies the fundamental
> index, so it goes in the first slot, and the down singlet the anti-fundamental one.

```lean
lemma isEquivariant_colourFundAntiFund_downBlock (f f' : Fin 3) (i sd sq wq : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun l : Fin 2 → Fin 3 => LocalCovFieldAlgebra.downBlock f f' i sd (l 1) sq
          (l 0) wq) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_downBlock`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L123).

> The two isospin indices of the down-type block carry one fundamental and one
> anti-fundamental `su(2)` index. The conjugate quark doublet supplies the fundamental
> index and the Higgs symbol the anti-fundamental one, so the Higgs index goes in the
> second slot.

```lean
lemma isEquivariant_isospinFundAntiFund_downBlock (f f' : Fin 3) (sd : Fin 2) (cd : Fin 3)
    (sq : Fin 2) (cq : Fin 3) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun l : Fin 2 → Fin 2 =>
        LocalCovFieldAlgebra.downBlock f f' (l 1) sd cd sq cq (l 0)) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downRDownR_downBlock`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L143).

> The two spinor indices of the down-type block are both dual right-handed. The down
> singlet and the conjugate quark doublet are both right-handed, and the Higgs symbol
> without derivatives is a Lorentz scalar.

```lean
lemma isEquivariant_downRDownR_downBlock (f f' : Fin 3) (i : Fin 2) (cd cq : Fin 3) (wq : Fin 2) :
    complexLorentzTensor.IsEquivariant ![.downR, .downR] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.downBlock f f' i p.1 cd p.2 cq wq) ∘
          pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_downBlock`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L162).

> A hypercharge transformation fixes every component of the down-type block, the three
> hypercharges `-3`, `2` and `1` cancelling.

```lean
lemma repGauge_u1_downBlock (t : unitary ℂ) (f f' : Fin 3) (i sd : Fin 2) (cd : Fin 3)
    (sq : Fin 2) (cq : Fin 3) (wq : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.downBlock f f' i sd
      cd sq cq wq)
      = LocalCovFieldAlgebra.downBlock f f' i sd cd sq cq wq
```

**`StandardModel.LocalCovFieldAlgebra.downBlockColour`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L179).

> The colour contraction of the down-type block, the Kronecker delta joining the
> fundamental colour index of the conjugate quark doublet to the anti-fundamental one of
> the down singlet.

```lean
noncomputable def downBlockColour (f f' : Fin 3)
    (i sd sq wq : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.downBlockColour_eq`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L186).

> The colour contraction written out, the sum of the three components with equal colour
> indices.

```lean
lemma downBlockColour_eq (f f' : Fin 3) (i sd sq wq : Fin 2) :
    LocalCovFieldAlgebra.downBlockColour f f' i sd sq wq
      = ∑ a : Fin 3, LocalCovFieldAlgebra.downBlock f f' i sd a sq a wq
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_downBlockColour`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L193).

> The colour contraction of the down-type block still carries one fundamental and one
> anti-fundamental isospin index, the colour sum being an isospin spectator.

```lean
lemma isEquivariant_isospinFundAntiFund_downBlockColour (f f' : Fin 3) (sd sq : Fin 2) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun l : Fin 2 → Fin 2 =>
        LocalCovFieldAlgebra.downBlockColour f f' (l 1) sd sq (l 0)) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.downBlockIsospin`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L204).

> The isospin contraction of the colour-contracted down-type block, the Kronecker delta
> joining the fundamental isospin index of the conjugate quark doublet to the
> anti-fundamental one of the Higgs.

```lean
noncomputable def downBlockIsospin (f f' : Fin 3)
    (sd sq : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.downBlockIsospin_eq`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L211).

> The doubly contracted block written out as a single sum over the isospin and colour
> indices it identifies.

```lean
lemma downBlockIsospin_eq (f f' : Fin 3) (sd sq : Fin 2) :
    LocalCovFieldAlgebra.downBlockIsospin f f' sd sq
      = ∑ p : Fin 2 × Fin 3, LocalCovFieldAlgebra.downBlock f f' p.1 sd p.2 sq p.2 p.1
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downRDownR_downBlockIsospin`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L221).

> The doubly contracted block carries two dual right-handed Weyl indices, the colour and
> isospin sums being Lorentz spectators.

```lean
lemma isEquivariant_downRDownR_downBlockIsospin (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.downR, .downR] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.downBlockIsospin f f' p.1 p.2) ∘
        pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.downYukawa`**, a def, [line 234](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L234).

> The down-type Yukawa term of the family pair `(f, f')`, the down-singlet symbol of family `f`
> against the conjugate quark doublet of family `f'` and a Higgs symbol, with the colour indices
> joined by the Kronecker delta, the isospin indices by the Kronecker delta, and the two
> right-handed spinor indices by the antisymmetric symbol. It is the image of the metric `εR'` under
> the map with the contracted block as its components.

```lean
noncomputable def downYukawa (f f' : Fin 3) : fieldData.LocalCovFieldAlgebra
```

## B. The invariance of the down-type Yukawa term, and its mass weight

> Each contraction is invariant under the factor it contracts, and inert under the other two,
> so the composite is fixed by all three factors and hence gauge invariant.  Hypercharge is
> already invariant component by component, the three charges `-3`, `2` and `1` summing to
> zero.

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_downBlockColour`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L250).

> The colour contraction of the down-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_downBlockColour (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i sd sq wq : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.downBlockColour f
      f' i sd sq wq)
      = LocalCovFieldAlgebra.downBlockColour f f' i sd sq wq
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_downBlockIsospin`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L259).

> The doubly contracted down-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_downBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (sd sq : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.downBlockIsospin f
      f' sd sq)
      = LocalCovFieldAlgebra.downBlockIsospin f f' sd sq
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su2_downBlockIsospin`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L269).

> The doubly contracted down-type block is fixed by the isospin factor.

```lean
lemma repGauge_su2_downBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (sd sq : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (LocalCovFieldAlgebra.downBlockIsospin f
      f' sd sq)
      = LocalCovFieldAlgebra.downBlockIsospin f f' sd sq
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_downBlockIsospin`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L279).

> The doubly contracted down-type block is fixed by the hypercharge factor, already
> component by component.

```lean
lemma repGauge_u1_downBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (sd sq : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.downBlockIsospin f
      f' sd sq)
      = LocalCovFieldAlgebra.downBlockIsospin f f' sd sq
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_downYukawa`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L290).

> The down-type Yukawa term is gauge invariant. The colour indices are joined by the
> Kronecker delta, the isospin indices by the Kronecker delta, and the three hypercharges
> cancel.

```lean
lemma repGauge_downYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGaugeGroupI g (LocalCovFieldAlgebra.downYukawa f f') =
      LocalCovFieldAlgebra.downYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_downYukawa`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L301).

> The down-type Yukawa term is Lorentz invariant, the two right-handed spinor indices
> being joined by the antisymmetric symbol.

```lean
lemma repLorentz_downYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentzGroup Λ (LocalCovFieldAlgebra.downYukawa f f') =
      LocalCovFieldAlgebra.downYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.downBlock_mem_sectorMassWeight`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L309).

> Every component of the down-type block sits at mass weight eight in the Yukawa
> sector.

```lean
lemma downBlock_mem_sectorMassWeight (f f' : Fin 3) (i sd : Fin 2) (cd : Fin 3)
    (sq : Fin 2) (cq : Fin 3) (wq : Fin 2) :
    LocalCovFieldAlgebra.downBlock f f' i sd cd sq cq wq
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.downYukawa_mem_sectorMassWeight`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L319).

> The down-type Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma downYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    LocalCovFieldAlgebra.downYukawa f f' ∈ fieldData.sectorMassWeight
      {FieldKind.scalar, FieldKind.fermion} 8
```

## C. The up-type Yukawa term

> The second computation.  Colour is again `3 ⊗ 3̄`, the conjugate up singlet supplying the
> fundamental index, but isospin is `2̄ ⊗ 2̄`: the Higgs symbol and the quark doublet both
> carry the anti-fundamental, whose only invariant is the antisymmetric symbol.  Both
> fermions are left-handed.

**`StandardModel.LocalCovFieldAlgebra.upBlock`**, a def, [line 340](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L340).

> The components of the up-type Yukawa block `H baru Q`, a Higgs symbol, a conjugate
> up-singlet symbol and a quark-doublet symbol, none carrying derivatives.

```lean
noncomputable def upBlock (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3) (sQ : Fin 2)
    (cQ : Fin 3) (wQ : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_colourFundAntiFund_upBlock`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L348).

> The two colour indices of the up-type block carry one fundamental and one
> anti-fundamental `su(3)` index, the conjugate up singlet supplying the fundamental
> one.

```lean
lemma isEquivariant_colourFundAntiFund_upBlock (f f' : Fin 3) (i su sQ wQ : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun l : Fin 2 → Fin 3 =>
        LocalCovFieldAlgebra.upBlock f f' i su (l 0) sQ (l 1) wQ) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinAntiFundAntiFund_upBlock`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L364).

> The two isospin indices of the up-type block are both anti-fundamental. The Higgs
> symbol and the quark doublet both carry the anti-fundamental of `su(2)`.

```lean
lemma isEquivariant_isospinAntiFundAntiFund_upBlock (f f' : Fin 3) (su : Fin 2) (cu : Fin 3)
    (sQ : Fin 2)
    (cQ : Fin 3) :
    (suTensor 2).IsEquivariant (fun _ : Fin 2 => .antiFund) (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents (fun l : Fin 2 → Fin 2 => LocalCovFieldAlgebra.upBlock f f' (l 0) su cu sQ cQ
          (l 1)))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downLDownL_upBlock`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L381).

> The two spinor indices of the up-type block are both dual left-handed.

```lean
lemma isEquivariant_downLDownL_upBlock (f f' : Fin 3) (i : Fin 2) (cu cQ : Fin 3) (wQ : Fin 2) :
    complexLorentzTensor.IsEquivariant ![.downL, .downL] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.upBlock f f' i p.1 cu p.2 cQ wQ) ∘
        pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_upBlock`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L400).

> A hypercharge transformation fixes every component of the up-type block, the three
> hypercharges `-3`, `4` and `-1` cancelling.

```lean
lemma repGauge_u1_upBlock (t : unitary ℂ) (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3)
    (sQ : Fin 2) (cQ : Fin 3) (wQ : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.upBlock f f' i su
      cu sQ cQ wQ)
      = LocalCovFieldAlgebra.upBlock f f' i su cu sQ cQ wQ
```

**`StandardModel.LocalCovFieldAlgebra.upBlockColour`**, a def, [line 416](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L416).

> The colour contraction of the up-type block.

```lean
noncomputable def upBlockColour (f f' : Fin 3)
    (i su sQ wQ : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.upBlockColour_eq`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L422).

> The colour contraction of the up-type block written out.

```lean
lemma upBlockColour_eq (f f' : Fin 3) (i su sQ wQ : Fin 2) :
    LocalCovFieldAlgebra.upBlockColour f f' i su sQ wQ = ∑ a : Fin 3, LocalCovFieldAlgebra.upBlock f
      f' i su a sQ a wQ
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinAntiFundAntiFund_upBlockColour`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L429).

> The colour contraction of the up-type block still carries two anti-fundamental isospin
> indices.

```lean
lemma isEquivariant_isospinAntiFundAntiFund_upBlockColour (f f' : Fin 3) (su sQ : Fin 2) :
    (suTensor 2).IsEquivariant (fun _ : Fin 2 => .antiFund) (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents (fun l : Fin 2 → Fin 2 => LocalCovFieldAlgebra.upBlockColour f f' (l 0) su sQ
          (l 1)))
```

**`StandardModel.LocalCovFieldAlgebra.upBlockIsospin`**, a def, [line 440](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L440).

> The isospin contraction of the colour-contracted up-type block, by the antisymmetric
> symbol. Two anti-fundamental isospin indices admit no trace.

```lean
noncomputable def upBlockIsospin (f f' : Fin 3) (su sQ : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.upBlockIsospin_eq`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L445).

> The doubly contracted up-type block written out.

```lean
lemma upBlockIsospin_eq (f f' : Fin 3) (su sQ : Fin 2) :
    LocalCovFieldAlgebra.upBlockIsospin f f' su sQ = (∑ a : Fin 3, LocalCovFieldAlgebra.upBlock f f'
      0 su a sQ a 1)
      - ∑ a : Fin 3, LocalCovFieldAlgebra.upBlock f f' 1 su a sQ a 0
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downLDownL_upBlockIsospin`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L453).

> The doubly contracted up-type block carries two dual left-handed Weyl indices.

```lean
lemma isEquivariant_downLDownL_upBlockIsospin (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.downL, .downL] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.upBlockIsospin f f' p.1 p.2) ∘ pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.upYukawa`**, a def, [line 469](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L469).

> The up-type Yukawa term of the family pair `(f, f')`. The colour indices are joined by the
> Kronecker delta, the isospin indices by the antisymmetric symbol, and the two left-handed spinor
> indices by the antisymmetric symbol. It is the image of the metric `εL'` under the map with the
> contracted block as its components.

```lean
noncomputable def upYukawa (f f' : Fin 3) : fieldData.LocalCovFieldAlgebra
```

## D. The invariance of the up-type Yukawa term, and its mass weight

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_upBlockColour`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L480).

> The colour contraction of the up-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_upBlockColour (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i su sQ wQ : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.upBlockColour f f'
      i su sQ wQ)
      = LocalCovFieldAlgebra.upBlockColour f f' i su sQ wQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_upBlockIsospin`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L489).

> The doubly contracted up-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_upBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (su sQ : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.upBlockIsospin f f'
      su sQ)
      = LocalCovFieldAlgebra.upBlockIsospin f f' su sQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su2_upBlockIsospin`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L499).

> The doubly contracted up-type block is fixed by the isospin factor.

```lean
lemma repGauge_su2_upBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (su sQ : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (LocalCovFieldAlgebra.upBlockIsospin f f'
      su sQ)
      = LocalCovFieldAlgebra.upBlockIsospin f f' su sQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_upBlockIsospin`**, a lemma, [line 508](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L508).

> The doubly contracted up-type block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_upBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (su sQ : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.upBlockIsospin f f'
      su sQ)
      = LocalCovFieldAlgebra.upBlockIsospin f f' su sQ
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_upYukawa`**, a lemma, [line 518](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L518).

> The up-type Yukawa term is gauge invariant.

```lean
lemma repGauge_upYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGaugeGroupI g (LocalCovFieldAlgebra.upYukawa f f') =
      LocalCovFieldAlgebra.upYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_upYukawa`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L528).

> The up-type Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_upYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentzGroup Λ (LocalCovFieldAlgebra.upYukawa f f') =
      LocalCovFieldAlgebra.upYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.upBlock_mem_sectorMassWeight`**, a lemma, [line 535](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L535).

> Every component of the up-type block sits at mass weight eight in the Yukawa sector.

```lean
lemma upBlock_mem_sectorMassWeight (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3)
    (sQ : Fin 2) (cQ : Fin 3) (wQ : Fin 2) :
    LocalCovFieldAlgebra.upBlock f f' i su cu sQ cQ wQ
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.upYukawa_mem_sectorMassWeight`**, a lemma, [line 545](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L545).

> The up-type Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma upYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    LocalCovFieldAlgebra.upYukawa f f' ∈ fieldData.sectorMassWeight
      {FieldKind.scalar, FieldKind.fermion} 8
```

## E. The charged-lepton Yukawa term

> The lepton blocks carry no colour at all, so there is no colour family to classify and no
> colour contraction to form: the three symbols are separately fixed by the colour factor,
> which is `repGauge_su3_leptonBlock`.  The isospin and Lorentz steps are the same two steps
> as for the quark blocks, and the contraction is the composite of those two alone.

**`StandardModel.LocalCovFieldAlgebra.leptonBlock`**, a def, [line 572](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L572).

> The components of the charged-lepton Yukawa block `H barL e`, a Higgs symbol, a
> conjugate lepton-doublet symbol and a lepton-singlet symbol, none carrying
> derivatives.

```lean
noncomputable def leptonBlock (f f' : Fin 3)
    (i sL wL se : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_leptonBlock`**, a lemma, [line 580](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L580).

> The lepton block is colour invariant outright. None of its three symbols carries a
> colour index. This is what stands in for the colour classification of the quark
> blocks.

```lean
lemma repGauge_su3_leptonBlock (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i sL wL se : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.leptonBlock f f' i
      sL wL se)
      = LocalCovFieldAlgebra.leptonBlock f f' i sL wL se
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_isospinFundAntiFund_leptonBlock`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L592).

> The two isospin indices of the lepton block carry one fundamental and one
> anti-fundamental `su(2)` index, the conjugate lepton doublet supplying the fundamental
> one.

```lean
lemma isEquivariant_isospinFundAntiFund_leptonBlock (f f' : Fin 3) (sL se : Fin 2) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGaugeGroupI.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun l : Fin 2 → Fin 2 =>
        LocalCovFieldAlgebra.leptonBlock f f' (l 1) sL (l 0) se) ∘ fundAntiFundIdx))
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downRDownR_leptonBlock`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L609).

> The two spinor indices of the lepton block are both dual right-handed.

```lean
lemma isEquivariant_downRDownR_leptonBlock (f f' : Fin 3) (i wL : Fin 2) :
    complexLorentzTensor.IsEquivariant ![.downR, .downR] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.leptonBlock f f' i p.1 wL p.2) ∘ pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_leptonBlock`**, a lemma, [line 627](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L627).

> A hypercharge transformation fixes every component of the lepton block, the three
> hypercharges `-3`, `-3` and `6` cancelling.

```lean
lemma repGauge_u1_leptonBlock (t : unitary ℂ) (f f' : Fin 3) (i sL wL se : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.leptonBlock f f' i
      sL wL se)
      = LocalCovFieldAlgebra.leptonBlock f f' i sL wL se
```

**`StandardModel.LocalCovFieldAlgebra.leptonBlockIsospin`**, a def, [line 642](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L642).

> The isospin contraction of the lepton block.

```lean
noncomputable def leptonBlockIsospin (f f' : Fin 3)
    (sL se : Fin 2) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.leptonBlockIsospin_eq`**, a lemma, [line 648](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L648).

> The isospin contraction of the lepton block written out.

```lean
lemma leptonBlockIsospin_eq (f f' : Fin 3) (sL se : Fin 2) :
    LocalCovFieldAlgebra.leptonBlockIsospin f f' sL se = ∑ w : Fin 2,
      LocalCovFieldAlgebra.leptonBlock f f' w sL w se
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_downRDownR_leptonBlockIsospin`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L655).

> The contracted lepton block carries two dual right-handed Weyl indices.

```lean
lemma isEquivariant_downRDownR_leptonBlockIsospin (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.downR, .downR] repLorentzGroup
      (liftComponents ((fun p => LocalCovFieldAlgebra.leptonBlockIsospin f f' p.1 p.2) ∘
          pairIdx))
```

**`StandardModel.LocalCovFieldAlgebra.leptonYukawa`**, a def, [line 667](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L667).

> The charged-lepton Yukawa term of the family pair `(f, f')`. The isospin indices are joined by
> the Kronecker delta and the two right-handed spinor indices by the antisymmetric symbol, colour
> playing no part. It is the image of the metric `εR'` under the map with the contracted block as
> its components.

```lean
noncomputable def leptonYukawa (f f' : Fin 3) : fieldData.LocalCovFieldAlgebra
```

## F. The invariance of the charged-lepton Yukawa term, and its mass weight

**`StandardModel.LocalCovFieldAlgebra.repGauge_su3_leptonBlockIsospin`**, a lemma, [line 678](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L678).

> The contracted lepton block is fixed by the colour factor.

```lean
lemma repGauge_su3_leptonBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (sL se : Fin 2) :
    repGaugeGroupI ((U, 1, 1) : GaugeGroupI) (LocalCovFieldAlgebra.leptonBlockIsospin
      f f' sL se)
      = LocalCovFieldAlgebra.leptonBlockIsospin f f' sL se
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_su2_leptonBlockIsospin`**, a lemma, [line 688](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L688).

> The contracted lepton block is fixed by the isospin factor.

```lean
lemma repGauge_su2_leptonBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (sL se : Fin 2) :
    repGaugeGroupI ((1, V, 1) : GaugeGroupI) (LocalCovFieldAlgebra.leptonBlockIsospin
      f f' sL se)
      = LocalCovFieldAlgebra.leptonBlockIsospin f f' sL se
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_u1_leptonBlockIsospin`**, a lemma, [line 697](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L697).

> The contracted lepton block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_leptonBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (sL se : Fin 2) :
    repGaugeGroupI ((1, 1, t) : GaugeGroupI) (LocalCovFieldAlgebra.leptonBlockIsospin
      f f' sL se)
      = LocalCovFieldAlgebra.leptonBlockIsospin f f' sL se
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_leptonYukawa`**, a lemma, [line 706](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L706).

> The charged-lepton Yukawa term is gauge invariant.

```lean
lemma repGauge_leptonYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGaugeGroupI g (LocalCovFieldAlgebra.leptonYukawa f f') =
      LocalCovFieldAlgebra.leptonYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_leptonYukawa`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L716).

> The charged-lepton Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_leptonYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentzGroup Λ (LocalCovFieldAlgebra.leptonYukawa f f') =
      LocalCovFieldAlgebra.leptonYukawa f f'
```

**`StandardModel.LocalCovFieldAlgebra.leptonBlock_mem_sectorMassWeight`**, a lemma, [line 723](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L723).

> Every component of the lepton block sits at mass weight eight in the Yukawa sector.

```lean
lemma leptonBlock_mem_sectorMassWeight (f f' : Fin 3) (i sL wL se : Fin 2) :
    LocalCovFieldAlgebra.leptonBlock f f' i sL wL se
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.leptonYukawa_mem_sectorMassWeight`**, a lemma, [line 732](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L732).

> The charged-lepton Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma leptonYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    LocalCovFieldAlgebra.leptonYukawa f f'
      ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8
```

## G. The spans of the Yukawa terms

> The nine family pairs are what the Yukawa coupling matrices are: joining the line of a
> Yukawa term over `(f, f') : Fin 3 × Fin 3` gives exactly the space of terms with an
> arbitrary `3 × 3` complex coupling matrix, and no matrix has to be written down.  Each such
> join lies inside the sector at mass weight eight and inside both spaces of invariants,
> which is the direction that will make the eventual classification an equivalence rather
> than a one-way inclusion.

**`StandardModel.LocalCovFieldAlgebra.downYukawaSpan`**, a def, [line 755](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L755).

> The span of the down-type Yukawa terms over the nine family pairs, the down-type
> Yukawa coupling with an arbitrary `3 × 3` matrix.

```lean
noncomputable def downYukawaSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.upYukawaSpan`**, a def, [line 759](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L759).

> The span of the up-type Yukawa terms over the nine family pairs.

```lean
noncomputable def upYukawaSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.leptonYukawaSpan`**, a def, [line 763](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L763).

> The span of the charged-lepton Yukawa terms over the nine family pairs.

```lean
noncomputable def leptonYukawaSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.downYukawaSpan_le_sectorMassWeight`**, a lemma, [line 767](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L767).

> The down-type Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma downYukawaSpan_le_sectorMassWeight :
    LocalCovFieldAlgebra.downYukawaSpan ≤ fieldData.sectorMassWeight
      {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.downYukawaSpan_le_invariants`**, a lemma, [line 774](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L774).

> The down-type Yukawa span is a space of gauge invariants.

```lean
lemma downYukawaSpan_le_invariants : LocalCovFieldAlgebra.downYukawaSpan ≤
    repGaugeGroupI.invariants
```

**`StandardModel.LocalCovFieldAlgebra.downYukawaSpan_le_lorentzInvariants`**, a lemma, [line 780](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L780).

> The down-type Yukawa span is a space of Lorentz invariants.

```lean
lemma downYukawaSpan_le_lorentzInvariants : LocalCovFieldAlgebra.downYukawaSpan ≤
    repLorentzGroup.invariants
```

**`StandardModel.LocalCovFieldAlgebra.upYukawaSpan_le_sectorMassWeight`**, a lemma, [line 786](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L786).

> The up-type Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma upYukawaSpan_le_sectorMassWeight :
    LocalCovFieldAlgebra.upYukawaSpan ≤ fieldData.sectorMassWeight
      {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.upYukawaSpan_le_invariants`**, a lemma, [line 793](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L793).

> The up-type Yukawa span is a space of gauge invariants.

```lean
lemma upYukawaSpan_le_invariants : LocalCovFieldAlgebra.upYukawaSpan ≤
    repGaugeGroupI.invariants
```

**`StandardModel.LocalCovFieldAlgebra.upYukawaSpan_le_lorentzInvariants`**, a lemma, [line 799](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L799).

> The up-type Yukawa span is a space of Lorentz invariants.

```lean
lemma upYukawaSpan_le_lorentzInvariants : LocalCovFieldAlgebra.upYukawaSpan ≤
    repLorentzGroup.invariants
```

**`StandardModel.LocalCovFieldAlgebra.leptonYukawaSpan_le_sectorMassWeight`**, a lemma, [line 805](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L805).

> The charged-lepton Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma leptonYukawaSpan_le_sectorMassWeight :
    LocalCovFieldAlgebra.leptonYukawaSpan ≤ fieldData.sectorMassWeight
      {FieldKind.scalar, FieldKind.fermion} 8
```

**`StandardModel.LocalCovFieldAlgebra.leptonYukawaSpan_le_invariants`**, a lemma, [line 812](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L812).

> The charged-lepton Yukawa span is a space of gauge invariants.

```lean
lemma leptonYukawaSpan_le_invariants : LocalCovFieldAlgebra.leptonYukawaSpan ≤
    repGaugeGroupI.invariants
```

**`StandardModel.LocalCovFieldAlgebra.leptonYukawaSpan_le_lorentzInvariants`**, a lemma, [line 818](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean#L818).

> The charged-lepton Yukawa span is a space of Lorentz invariants.

```lean
lemma leptonYukawaSpan_le_lorentzInvariants : LocalCovFieldAlgebra.leptonYukawaSpan ≤
    repLorentzGroup.invariants
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic](../../../../physlib/relativity/tensors/part-01/complextensor-metrics-basic.md)
- [The sectors of a gauge field theory](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-localcovfieldalgebra-sector.md)
- [Families of colour and isospin components and their invariants](../part-02/gaugegroup-invariants-basic.md)
- [The components of the fermion symbols](../part-03/localfieldalgebra-fermionsector-components.md)
- [The scalar sector of the covariant field algebra](../part-05/localfieldalgebra-scalarsector-basic.md)

## Proof depends on

- [The Yukawa sector's mass-weight submodules](../part-06/localfieldalgebra-yukawasector-basic.md)
- [The symbols of the Yukawa blocks](localfieldalgebra-yukawasector-families-symbols.md)
- [Reynolds elements for complex Lorentz tensors](../../../relativity/lorentzgroup/invariants-reynolds.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/Families/Higgs.lean)
