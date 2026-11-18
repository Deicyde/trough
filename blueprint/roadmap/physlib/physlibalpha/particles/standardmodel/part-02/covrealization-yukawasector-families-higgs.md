---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.downBlock, StandardModel.CovAlgebraRealization.isSU3FundamentalAntiFundamental_downBlock, StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_downBlock, StandardModel.CovAlgebraRealization.isBiDualRightWeyl_downBlock, StandardModel.CovAlgebraRealization.repGauge_u1_downBlock, StandardModel.CovAlgebraRealization.downBlockColour, StandardModel.CovAlgebraRealization.downBlockColour_eq, StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_downBlockColour
statement: formalized
proof: formalized
---

# The Yukawa terms built on the Higgs symbol

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.YukawaSector.Families.Higgs`, [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean): 68 declarations, 68 with a docstring.

## i. Overview

> Three of the twelve blocks of the mass-weight-eight Yukawa sector are built on the Higgs
> symbol rather than its conjugate: the down type `H d barQ`, the up type `H baru Q` and the
> charged-lepton type `H barL e`.  They are the three genuinely distinct computations of the
> sector — the other nine blocks are their conjugates and the two fermion orderings of each —
> and this file builds, for each of them, the block, the index laws its three symbols obey,
> the iterated contraction those laws admit, and the proof that the contraction is a gauge-
> and Lorentz-invariant element of the sector at mass weight eight.
>
> The three differ in exactly two places.  Isospin: the down and lepton types contract a
> `2 ⊗ 2̄` by the trace, the up type a `2̄ ⊗ 2̄` by the antisymmetric symbol, since the Higgs
> symbol and the quark doublet both carry the anti-fundamental.  Colour: the two quark types
> contract a `3 ⊗ 3̄` by the Kronecker delta, while the lepton type carries no colour at all,
> so its colour step is plain invariance rather than a classification and its contraction has
> two stages instead of three.
>
> The transposed blocks — the same three triples with the two fermion factors exchanged — are
> not built here: they are minus these terms and span the same submodules, by
> `mul_mul_swap_eq_neg` and `mul_mul_piece_swap`.

## ii. Key results

> - `downYukawa`, `upYukawa`, `leptonYukawa` : the three Yukawa terms of a family pair.
> - `isSU3FundamentalAntiFundamental_downBlock`, `isSU2FundamentalAntiFundamental_downBlock`,
>   `isBiDualRightWeyl_downBlock` and their up-type and lepton-type counterparts : the index laws
>   of each block.
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

**`StandardModel.CovAlgebraRealization.downBlock`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L91).

> The components of the down-type Yukawa block `H d barQ`: a Higgs symbol, a
> down-singlet symbol and a conjugate quark-doublet symbol, none carrying derivatives,
> multiplied in the order in which the block of
> `sectorMassWeightEightGaugeWeight_piece_zero` multiplies them.

```lean
noncomputable def downBlock (f f' : Fin 3) (i sd : Fin 2) (cd : Fin 3) (sq : Fin 2)
    (cq : Fin 3) (wq : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.isSU3FundamentalAntiFundamental_downBlock`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L99).

> The two colour indices of the down-type block carry one fundamental and one
> anti-fundamental `su(3)` index: the conjugate quark doublet supplies the fundamental
> index, so it goes in the first slot, and the down singlet the anti-fundamental one.

```lean
lemma isSU3FundamentalAntiFundamental_downBlock (f f' : Fin 3) (i sd sq wq : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 3 => h.downBlock f f' i sd (l 1) sq (l 0) wq)
```

**`StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_downBlock`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L117).

> The two isospin indices of the down-type block carry one fundamental and one
> anti-fundamental `su(2)` index: the conjugate quark doublet supplies the fundamental
> index and the Higgs symbol the anti-fundamental one, so the Higgs index goes in the
> second slot.

```lean
lemma isSU2FundamentalAntiFundamental_downBlock (f f' : Fin 3) (sd : Fin 2) (cd : Fin 3)
    (sq : Fin 2) (cq : Fin 3) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.downBlock f f' (l 1) sd cd sq cq (l 0))
```

**`StandardModel.CovAlgebraRealization.isBiDualRightWeyl_downBlock`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L134).

> The two spinor indices of the down-type block are both dual right-handed: the down
> singlet and the conjugate quark doublet are both right-handed, and the Higgs symbol
> without derivatives is a Lorentz scalar.

```lean
lemma isBiDualRightWeyl_downBlock (f f' : Fin 3) (i : Fin 2) (cd cq : Fin 3) (wq : Fin 2) :
    IsBiDualRightWeyl B repLorentz
      (ofPairComponents fun a b => h.downBlock f f' i a cd b cq wq)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_downBlock`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L151).

> A hypercharge transformation fixes every component of the down-type block, the three
> hypercharges `-3`, `2` and `1` cancelling.

```lean
lemma repGauge_u1_downBlock (t : unitary ℂ) (f f' : Fin 3) (i sd : Fin 2) (cd : Fin 3)
    (sq : Fin 2) (cq : Fin 3) (wq : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.downBlock f f' i sd cd sq cq wq)
      = h.downBlock f f' i sd cd sq cq wq
```

**`StandardModel.CovAlgebraRealization.downBlockColour`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L165).

> The colour contraction of the down-type block: the Kronecker delta joining the
> fundamental colour index of the conjugate quark doublet to the anti-fundamental one of
> the down singlet.

```lean
noncomputable def downBlockColour (f f' : Fin 3) (i sd sq wq : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.downBlockColour_eq`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L171).

> The colour contraction written out: the sum of the three components with equal colour
> indices.

```lean
lemma downBlockColour_eq (f f' : Fin 3) (i sd sq wq : Fin 2) :
    h.downBlockColour f f' i sd sq wq
      = ∑ a : Fin 3, h.downBlock f f' i sd a sq a wq
```

**`StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_downBlockColour`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L178).

> The colour contraction of the down-type block still carries one fundamental and one
> anti-fundamental isospin index, the colour sum being an isospin spectator.

```lean
lemma isSU2FundamentalAntiFundamental_downBlockColour (f f' : Fin 3) (sd sq : Fin 2) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.downBlockColour f f' (l 1) sd sq (l 0))
```

**`StandardModel.CovAlgebraRealization.downBlockIsospin`**, a def, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L188).

> The isospin contraction of the colour-contracted down-type block: the Kronecker delta
> joining the fundamental isospin index of the conjugate quark doublet to the
> anti-fundamental one of the Higgs.

```lean
noncomputable def downBlockIsospin (f f' : Fin 3) (sd sq : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.downBlockIsospin_eq`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L194).

> The doubly contracted block written out as a single sum over the isospin and colour
> indices it identifies.

```lean
lemma downBlockIsospin_eq (f f' : Fin 3) (sd sq : Fin 2) :
    h.downBlockIsospin f f' sd sq
      = ∑ p : Fin 2 × Fin 3, h.downBlock f f' p.1 sd p.2 sq p.2 p.1
```

**`StandardModel.CovAlgebraRealization.isBiDualRightWeyl_downBlockIsospin`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L203).

> The doubly contracted block carries two dual right-handed Weyl indices, the colour and
> isospin sums being Lorentz spectators.

```lean
lemma isBiDualRightWeyl_downBlockIsospin (f f' : Fin 3) :
    IsBiDualRightWeyl B repLorentz (ofPairComponents (h.downBlockIsospin f f'))
```

**`StandardModel.CovAlgebraRealization.downYukawa`**, a def, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L215).

> The down-type Yukawa term of the family pair `(f, f')`: the down-singlet symbol of family `f`
> against the conjugate quark doublet of family `f'` and a Higgs symbol, with the colour indices
> joined by the Kronecker delta, the isospin indices by the Kronecker delta, and the two
> right-handed spinor indices by the antisymmetric symbol. It is the image of the metric `εR'` under
> the map with the contracted block as its components.

```lean
noncomputable def downYukawa (f f' : Fin 3) : B
```

## B. The invariance of the down-type Yukawa term, and its mass weight

> Each contraction is invariant under the factor it contracts, and inert under the other two,
> so the composite is fixed by all three factors and hence gauge invariant.  Hypercharge is
> already invariant component by component, the three charges `-3`, `2` and `1` summing to
> zero.

**`StandardModel.CovAlgebraRealization.repGauge_su3_downBlockColour`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L230).

> The colour contraction of the down-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_downBlockColour (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i sd sq wq : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.downBlockColour f f' i sd sq wq)
      = h.downBlockColour f f' i sd sq wq
```

**`StandardModel.CovAlgebraRealization.repGauge_su3_downBlockIsospin`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L238).

> The doubly contracted down-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_downBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (sd sq : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.downBlockIsospin f f' sd sq)
      = h.downBlockIsospin f f' sd sq
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_downBlockIsospin`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L246).

> The doubly contracted down-type block is fixed by the isospin factor.

```lean
lemma repGauge_su2_downBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (sd sq : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.downBlockIsospin f f' sd sq)
      = h.downBlockIsospin f f' sd sq
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_downBlockIsospin`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L255).

> The doubly contracted down-type block is fixed by the hypercharge factor, already
> component by component.

```lean
lemma repGauge_u1_downBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (sd sq : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.downBlockIsospin f f' sd sq)
      = h.downBlockIsospin f f' sd sq
```

**`StandardModel.CovAlgebraRealization.repGauge_downYukawa`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L264).

> The down-type Yukawa term is gauge invariant: the colour indices are joined by the
> Kronecker delta, the isospin indices by the Kronecker delta, and the three hypercharges
> cancel.

```lean
lemma repGauge_downYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGauge g (h.downYukawa f f') = h.downYukawa f f'
```

**`StandardModel.CovAlgebraRealization.repLorentz_downYukawa`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L274).

> The down-type Yukawa term is Lorentz invariant, the two right-handed spinor indices
> being joined by the antisymmetric symbol.

```lean
lemma repLorentz_downYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentz Λ (h.downYukawa f f') = h.downYukawa f f'
```

**`StandardModel.CovAlgebraRealization.downBlock_mem_sectorMassWeight`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L281).

> Every component of the down-type block sits at mass weight eight in the Yukawa
> sector.

```lean
lemma downBlock_mem_sectorMassWeight (f f' : Fin 3) (i sd : Fin 2) (cd : Fin 3)
    (sq : Fin 2) (cq : Fin 3) (wq : Fin 2) :
    h.downBlock f f' i sd cd sq cq wq
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.downYukawa_mem_sectorMassWeight`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L291).

> The down-type Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma downYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    h.downYukawa f f' ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

## C. The up-type Yukawa term

> The second computation.  Colour is again `3 ⊗ 3̄`, the conjugate up singlet supplying the
> fundamental index, but isospin is `2̄ ⊗ 2̄`: the Higgs symbol and the quark doublet both
> carry the anti-fundamental, whose only invariant is the antisymmetric symbol.  Both
> fermions are left-handed.

**`StandardModel.CovAlgebraRealization.upBlock`**, a def, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L311).

> The components of the up-type Yukawa block `H baru Q`: a Higgs symbol, a conjugate
> up-singlet symbol and a quark-doublet symbol, none carrying derivatives.

```lean
noncomputable def upBlock (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3) (sQ : Fin 2)
    (cQ : Fin 3) (wQ : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.isSU3FundamentalAntiFundamental_upBlock`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L319).

> The two colour indices of the up-type block carry one fundamental and one
> anti-fundamental `su(3)` index, the conjugate up singlet supplying the fundamental
> one.

```lean
lemma isSU3FundamentalAntiFundamental_upBlock (f f' : Fin 3) (i su sQ wQ : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 3 => h.upBlock f f' i su (l 0) sQ (l 1) wQ)
```

**`StandardModel.CovAlgebraRealization.isSU2BiAntiFundamental_upBlock`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L333).

> The two isospin indices of the up-type block are both anti-fundamental: the Higgs
> symbol and the quark doublet both carry the anti-fundamental of `su(2)`.

```lean
lemma isSU2BiAntiFundamental_upBlock (f f' : Fin 3) (su : Fin 2) (cu : Fin 3) (sQ : Fin 2)
    (cQ : Fin 3) :
    IsSU2BiAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.upBlock f f' (l 0) su cu sQ cQ (l 1))
```

**`StandardModel.CovAlgebraRealization.isBiDualLeftWeyl_upBlock`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L346).

> The two spinor indices of the up-type block are both dual left-handed.

```lean
lemma isBiDualLeftWeyl_upBlock (f f' : Fin 3) (i : Fin 2) (cu cQ : Fin 3) (wQ : Fin 2) :
    IsBiDualLeftWeyl B repLorentz
      (ofPairComponents fun a b => h.upBlock f f' i a cu b cQ wQ)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_upBlock`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L363).

> A hypercharge transformation fixes every component of the up-type block, the three
> hypercharges `-3`, `4` and `-1` cancelling.

```lean
lemma repGauge_u1_upBlock (t : unitary ℂ) (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3)
    (sQ : Fin 2) (cQ : Fin 3) (wQ : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.upBlock f f' i su cu sQ cQ wQ)
      = h.upBlock f f' i su cu sQ cQ wQ
```

**`StandardModel.CovAlgebraRealization.upBlockColour`**, a def, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L376).

> The colour contraction of the up-type block.

```lean
noncomputable def upBlockColour (f f' : Fin 3) (i su sQ wQ : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.upBlockColour_eq`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L381).

> The colour contraction of the up-type block written out.

```lean
lemma upBlockColour_eq (f f' : Fin 3) (i su sQ wQ : Fin 2) :
    h.upBlockColour f f' i su sQ wQ = ∑ a : Fin 3, h.upBlock f f' i su a sQ a wQ
```

**`StandardModel.CovAlgebraRealization.isSU2BiAntiFundamental_upBlockColour`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L387).

> The colour contraction of the up-type block still carries two anti-fundamental isospin
> indices.

```lean
lemma isSU2BiAntiFundamental_upBlockColour (f f' : Fin 3) (su sQ : Fin 2) :
    IsSU2BiAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.upBlockColour f f' (l 0) su sQ (l 1))
```

**`StandardModel.CovAlgebraRealization.upBlockIsospin`**, a def, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L395).

> The isospin contraction of the colour-contracted up-type block, by the antisymmetric
> symbol: two anti-fundamental isospin indices admit no trace.

```lean
noncomputable def upBlockIsospin (f f' : Fin 3) (su sQ : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.upBlockIsospin_eq`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L400).

> The doubly contracted up-type block written out.

```lean
lemma upBlockIsospin_eq (f f' : Fin 3) (su sQ : Fin 2) :
    h.upBlockIsospin f f' su sQ = (∑ a : Fin 3, h.upBlock f f' 0 su a sQ a 1)
      - ∑ a : Fin 3, h.upBlock f f' 1 su a sQ a 0
```

**`StandardModel.CovAlgebraRealization.isBiDualLeftWeyl_upBlockIsospin`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L407).

> The doubly contracted up-type block carries two dual left-handed Weyl indices.

```lean
lemma isBiDualLeftWeyl_upBlockIsospin (f f' : Fin 3) :
    IsBiDualLeftWeyl B repLorentz (ofPairComponents (h.upBlockIsospin f f'))
```

**`StandardModel.CovAlgebraRealization.upYukawa`**, a def, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L418).

> The up-type Yukawa term of the family pair `(f, f')`: the colour indices are joined by the
> Kronecker delta, the isospin indices by the antisymmetric symbol, and the two left-handed spinor
> indices by the antisymmetric symbol. It is the image of the metric `εL'` under the map with the
> contracted block as its components.

```lean
noncomputable def upYukawa (f f' : Fin 3) : B
```

## D. The invariance of the up-type Yukawa term, and its mass weight

**`StandardModel.CovAlgebraRealization.repGauge_su3_upBlockColour`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L428).

> The colour contraction of the up-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_upBlockColour (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i su sQ wQ : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.upBlockColour f f' i su sQ wQ)
      = h.upBlockColour f f' i su sQ wQ
```

**`StandardModel.CovAlgebraRealization.repGauge_su3_upBlockIsospin`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L436).

> The doubly contracted up-type block is fixed by the colour factor.

```lean
lemma repGauge_su3_upBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (su sQ : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.upBlockIsospin f f' su sQ)
      = h.upBlockIsospin f f' su sQ
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_upBlockIsospin`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L444).

> The doubly contracted up-type block is fixed by the isospin factor.

```lean
lemma repGauge_su2_upBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (su sQ : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.upBlockIsospin f f' su sQ)
      = h.upBlockIsospin f f' su sQ
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_upBlockIsospin`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L452).

> The doubly contracted up-type block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_upBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (su sQ : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.upBlockIsospin f f' su sQ)
      = h.upBlockIsospin f f' su sQ
```

**`StandardModel.CovAlgebraRealization.repGauge_upYukawa`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L460).

> The up-type Yukawa term is gauge invariant.

```lean
lemma repGauge_upYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGauge g (h.upYukawa f f') = h.upYukawa f f'
```

**`StandardModel.CovAlgebraRealization.repLorentz_upYukawa`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L469).

> The up-type Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_upYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentz Λ (h.upYukawa f f') = h.upYukawa f f'
```

**`StandardModel.CovAlgebraRealization.upBlock_mem_sectorMassWeight`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L475).

> Every component of the up-type block sits at mass weight eight in the Yukawa sector.

```lean
lemma upBlock_mem_sectorMassWeight (f f' : Fin 3) (i su : Fin 2) (cu : Fin 3)
    (sQ : Fin 2) (cQ : Fin 3) (wQ : Fin 2) :
    h.upBlock f f' i su cu sQ cQ wQ
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.upYukawa_mem_sectorMassWeight`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L485).

> The up-type Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma upYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    h.upYukawa f f' ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

## E. The charged-lepton Yukawa term

> The lepton blocks carry no colour at all, so there is no colour family to classify and no
> colour contraction to form: the three symbols are separately fixed by the colour factor,
> which is `repGauge_su3_leptonBlock`.  The isospin and Lorentz steps are the same two steps
> as for the quark blocks, and the contraction is the composite of those two alone.

**`StandardModel.CovAlgebraRealization.leptonBlock`**, a def, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L510).

> The components of the charged-lepton Yukawa block `H barL e`: a Higgs symbol, a
> conjugate lepton-doublet symbol and a lepton-singlet symbol, none carrying
> derivatives.

```lean
noncomputable def leptonBlock (f f' : Fin 3) (i sL wL se : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.repGauge_su3_leptonBlock`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L517).

> The lepton block is colour invariant outright: none of its three symbols carries a
> colour index. This is what stands in for the colour classification of the quark
> blocks.

```lean
lemma repGauge_su3_leptonBlock (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (i sL wL se : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.leptonBlock f f' i sL wL se)
      = h.leptonBlock f f' i sL wL se
```

**`StandardModel.CovAlgebraRealization.isSU2FundamentalAntiFundamental_leptonBlock`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L527).

> The two isospin indices of the lepton block carry one fundamental and one
> anti-fundamental `su(2)` index, the conjugate lepton doublet supplying the fundamental
> one.

```lean
lemma isSU2FundamentalAntiFundamental_leptonBlock (f f' : Fin 3) (sL se : Fin 2) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun l : Fin 2 → Fin 2 => h.leptonBlock f f' (l 1) sL (l 0) se)
```

**`StandardModel.CovAlgebraRealization.isBiDualRightWeyl_leptonBlock`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L541).

> The two spinor indices of the lepton block are both dual right-handed.

```lean
lemma isBiDualRightWeyl_leptonBlock (f f' : Fin 3) (i wL : Fin 2) :
    IsBiDualRightWeyl B repLorentz
      (ofPairComponents fun a b => h.leptonBlock f f' i a wL b)
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_leptonBlock`**, a lemma, [line 558](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L558).

> A hypercharge transformation fixes every component of the lepton block, the three
> hypercharges `-3`, `-3` and `6` cancelling.

```lean
lemma repGauge_u1_leptonBlock (t : unitary ℂ) (f f' : Fin 3) (i sL wL se : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.leptonBlock f f' i sL wL se)
      = h.leptonBlock f f' i sL wL se
```

**`StandardModel.CovAlgebraRealization.leptonBlockIsospin`**, a def, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L570).

> The isospin contraction of the lepton block.

```lean
noncomputable def leptonBlockIsospin (f f' : Fin 3) (sL se : Fin 2) : B
```

**`StandardModel.CovAlgebraRealization.leptonBlockIsospin_eq`**, a lemma, [line 575](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L575).

> The isospin contraction of the lepton block written out.

```lean
lemma leptonBlockIsospin_eq (f f' : Fin 3) (sL se : Fin 2) :
    h.leptonBlockIsospin f f' sL se = ∑ w : Fin 2, h.leptonBlock f f' w sL w se
```

**`StandardModel.CovAlgebraRealization.isBiDualRightWeyl_leptonBlockIsospin`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L581).

> The contracted lepton block carries two dual right-handed Weyl indices.

```lean
lemma isBiDualRightWeyl_leptonBlockIsospin (f f' : Fin 3) :
    IsBiDualRightWeyl B repLorentz (ofPairComponents (h.leptonBlockIsospin f f'))
```

**`StandardModel.CovAlgebraRealization.leptonYukawa`**, a def, [line 591](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L591).

> The charged-lepton Yukawa term of the family pair `(f, f')`: the isospin indices are joined by
> the Kronecker delta and the two right-handed spinor indices by the antisymmetric symbol, colour
> playing no part. It is the image of the metric `εR'` under the map with the contracted block as
> its components.

```lean
noncomputable def leptonYukawa (f f' : Fin 3) : B
```

## F. The invariance of the charged-lepton Yukawa term, and its mass weight

**`StandardModel.CovAlgebraRealization.repGauge_su3_leptonBlockIsospin`**, a lemma, [line 601](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L601).

> The contracted lepton block is fixed by the colour factor.

```lean
lemma repGauge_su3_leptonBlockIsospin (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (sL se : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.leptonBlockIsospin f f' sL se)
      = h.leptonBlockIsospin f f' sL se
```

**`StandardModel.CovAlgebraRealization.repGauge_su2_leptonBlockIsospin`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L609).

> The contracted lepton block is fixed by the isospin factor.

```lean
lemma repGauge_su2_leptonBlockIsospin (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (sL se : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.leptonBlockIsospin f f' sL se)
      = h.leptonBlockIsospin f f' sL se
```

**`StandardModel.CovAlgebraRealization.repGauge_u1_leptonBlockIsospin`**, a lemma, [line 617](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L617).

> The contracted lepton block is fixed by the hypercharge factor.

```lean
lemma repGauge_u1_leptonBlockIsospin (t : unitary ℂ) (f f' : Fin 3) (sL se : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.leptonBlockIsospin f f' sL se)
      = h.leptonBlockIsospin f f' sL se
```

**`StandardModel.CovAlgebraRealization.repGauge_leptonYukawa`**, a lemma, [line 624](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L624).

> The charged-lepton Yukawa term is gauge invariant.

```lean
lemma repGauge_leptonYukawa (f f' : Fin 3) (g : GaugeGroupI) :
    repGauge g (h.leptonYukawa f f') = h.leptonYukawa f f'
```

**`StandardModel.CovAlgebraRealization.repLorentz_leptonYukawa`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L633).

> The charged-lepton Yukawa term is Lorentz invariant.

```lean
lemma repLorentz_leptonYukawa (f f' : Fin 3) (Λ : SL(2,ℂ)) :
    repLorentz Λ (h.leptonYukawa f f') = h.leptonYukawa f f'
```

**`StandardModel.CovAlgebraRealization.leptonBlock_mem_sectorMassWeight`**, a lemma, [line 639](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L639).

> Every component of the lepton block sits at mass weight eight in the Yukawa sector.

```lean
lemma leptonBlock_mem_sectorMassWeight (f f' : Fin 3) (i sL wL se : Fin 2) :
    h.leptonBlock f f' i sL wL se
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.leptonYukawa_mem_sectorMassWeight`**, a lemma, [line 648](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L648).

> The charged-lepton Yukawa term sits at mass weight eight in the Yukawa sector.

```lean
lemma leptonYukawa_mem_sectorMassWeight (f f' : Fin 3) :
    h.leptonYukawa f f'
      ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

## G. The spans of the Yukawa terms

> The nine family pairs are what the Yukawa coupling matrices are: joining the line of a
> Yukawa term over `(f, f') : Fin 3 × Fin 3` gives exactly the space of terms with an
> arbitrary `3 × 3` complex coupling matrix, and no matrix has to be written down.  Each such
> join lies inside the sector at mass weight eight and inside both spaces of invariants,
> which is the direction that will make the eventual classification an equivalence rather
> than a one-way inclusion.

**`StandardModel.CovAlgebraRealization.downYukawaSpan`**, a def, [line 671](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L671).

> The span of the down-type Yukawa terms over the nine family pairs: the down-type
> Yukawa coupling with an arbitrary `3 × 3` matrix.

```lean
noncomputable def downYukawaSpan : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.upYukawaSpan`**, a def, [line 675](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L675).

> The span of the up-type Yukawa terms over the nine family pairs.

```lean
noncomputable def upYukawaSpan : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.leptonYukawaSpan`**, a def, [line 679](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L679).

> The span of the charged-lepton Yukawa terms over the nine family pairs.

```lean
noncomputable def leptonYukawaSpan : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.downYukawaSpan_le_sectorMassWeight`**, a lemma, [line 683](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L683).

> The down-type Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma downYukawaSpan_le_sectorMassWeight :
    h.downYukawaSpan ≤ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.downYukawaSpan_le_invariants`**, a lemma, [line 689](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L689).

> The down-type Yukawa span is a space of gauge invariants.

```lean
lemma downYukawaSpan_le_invariants : h.downYukawaSpan ≤ repGauge.invariants
```

**`StandardModel.CovAlgebraRealization.downYukawaSpan_le_lorentzInvariants`**, a lemma, [line 694](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L694).

> The down-type Yukawa span is a space of Lorentz invariants.

```lean
lemma downYukawaSpan_le_lorentzInvariants : h.downYukawaSpan ≤ repLorentz.invariants
```

**`StandardModel.CovAlgebraRealization.upYukawaSpan_le_sectorMassWeight`**, a lemma, [line 699](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L699).

> The up-type Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma upYukawaSpan_le_sectorMassWeight :
    h.upYukawaSpan ≤ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.upYukawaSpan_le_invariants`**, a lemma, [line 705](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L705).

> The up-type Yukawa span is a space of gauge invariants.

```lean
lemma upYukawaSpan_le_invariants : h.upYukawaSpan ≤ repGauge.invariants
```

**`StandardModel.CovAlgebraRealization.upYukawaSpan_le_lorentzInvariants`**, a lemma, [line 710](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L710).

> The up-type Yukawa span is a space of Lorentz invariants.

```lean
lemma upYukawaSpan_le_lorentzInvariants : h.upYukawaSpan ≤ repLorentz.invariants
```

**`StandardModel.CovAlgebraRealization.leptonYukawaSpan_le_sectorMassWeight`**, a lemma, [line 715](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L715).

> The charged-lepton Yukawa span sits at mass weight eight in the Yukawa sector.

```lean
lemma leptonYukawaSpan_le_sectorMassWeight :
    h.leptonYukawaSpan ≤ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8
```

**`StandardModel.CovAlgebraRealization.leptonYukawaSpan_le_invariants`**, a lemma, [line 721](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L721).

> The charged-lepton Yukawa span is a space of gauge invariants.

```lean
lemma leptonYukawaSpan_le_invariants : h.leptonYukawaSpan ≤ repGauge.invariants
```

**`StandardModel.CovAlgebraRealization.leptonYukawaSpan_le_lorentzInvariants`**, a lemma, [line 726](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean#L726).

> The charged-lepton Yukawa span is a space of Lorentz invariants.

```lean
lemma leptonYukawaSpan_le_lorentzInvariants : h.leptonYukawaSpan ≤ repLorentz.invariants
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic](../../../../physlib/relativity/tensors/part-01/complextensor-metrics-basic.md)
- [The sectors of the field algebra](../part-01/covrealization-sectors.md)
- [Families of colour and isospin components and their invariants](../part-04/gaugegroup-invariants-basic.md)
- [The components of the fermion symbols](../part-05/isfermionsector-components.md)
- [Lorentz invariants of two Weyl indices of the same kind](../../../relativity/lorentzgroup/invariants-isbileftweyl.md)

## Proof depends on

- [The Yukawa sector's mass-weight submodules](covrealization-yukawasector-basic.md)
- [The symbols of the Yukawa blocks](covrealization-yukawasector-families-symbols.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/Families/Higgs.lean)
