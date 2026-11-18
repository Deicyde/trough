---
declaration: module
origin: cited
lean: StandardModel.IsFermionSector.dbardBlk, StandardModel.IsFermionSector.isSU3FundamentalAntiFundamental_dbardBlk, StandardModel.IsFermionSector.repGauge_su2_dbardBlk, StandardModel.IsFermionSector.repGauge_u1_dbardBlk, StandardModel.IsFermionSector.dbardColourStep, StandardModel.IsFermionSector.dbardColourStep_contraction, StandardModel.IsFermionSector.dbardIsospinStep, StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_dbard
statement: formalized
proof: formalized
---

# The ten kinetic blocks

The module `PhyslibAlpha.Particles.StandardModel.IsFermionSector.MassWeight.KineticTerms`, [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean): 100 declarations, 100 with a docstring.

## i. Overview

> The five conjugate pairs of the fermion sector, each with the covariant derivative on one
> factor or the other, give ten blocks at mass weight eight, and each is packaged here as a
> `KineticBlock` of `KineticFamilies`. The package does the work; what a block has to supply
> is its components, the three index laws they obey, and the cancellation of the two
> hypercharges.
>
> The blocks differ only in which indices their symbols carry. The four quark-singlet
> pairings `d ∂ bard`, `bard ∂ d`, `u ∂ baru` and `baru ∂ u` run a genuine colour stage and a
> trivial isospin one; the two quark-doublet pairings `Q ∂ barQ` and `barQ ∂ Q` run both; the
> two lepton-doublet pairings run a trivial colour stage and a genuine isospin one; and the
> two lepton-singlet pairings run neither, their two symbols carrying only hypercharge and a
> spinor index between them. In every case the unbarred symbol is anti-fundamental and the
> barred one fundamental, since a symbol eats a covector and so carries the contragredient of
> its value space; that is what makes each conjugate pair a fundamental against an
> anti-fundamental, and it is the same fact that makes the two spinor indices of a pair
> opposite in chirality.
>
> What comes out of each block is one kinetic term per pair of generations; the join of the
> ten over the nine generation pairs is the kinetic span of the sector, assembled in
> `MassDimEight`.

## ii. Key results

> - `dbardBlk` : the components of the block `d ∂ bard`: an underived down-singlet symbol against a
>   once-derived conjugate down-singlet symbol
> - `isSU3FundamentalAntiFundamental_dbardBlk` : the two colour indices of the `d ∂ bard` block are
>   one fundamental and one anti-fundamental, the barred symbol supplying the fundamental one
> - `repGauge_su2_dbardBlk` : an isospin transformation fixes the `d ∂ bard` block, neither symbol
>   carrying isospin
> - `repGauge_u1_dbardBlk` : a hypercharge transformation fixes the `d ∂ bard` block, the hypercharges
>   of a species and its conjugate cancelling

## iv. References

> * None.

## A. The four quark-singlet pairings

> The down and up singlets carry colour and hypercharge and nothing else, so their four
> pairings run a genuine colour stage and a trivial isospin one.

**`StandardModel.IsFermionSector.dbardBlk`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L104).

> The components of the block `d ∂ bard`: an underived down-singlet symbol against a
> once-derived conjugate down-singlet symbol.

```lean
noncomputable def dbardBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.isSU3FundamentalAntiFundamental_dbardBlk`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L110).

> The two colour indices of the `d ∂ bard` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU3FundamentalAntiFundamental_dbardBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 3 => h.dbardBlk f f' q l (n 0) (n 1) w w')
```

**`StandardModel.IsFermionSector.repGauge_su2_dbardBlk`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L120).

> An isospin transformation fixes the `d ∂ bard` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_dbardBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.dbardBlk f f' q l c c' w w')
      = h.dbardBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.repGauge_u1_dbardBlk`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L129).

> A hypercharge transformation fixes the `d ∂ bard` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_dbardBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.dbardBlk f f' q l c c' w w')
      = h.dbardBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.dbardColourStep`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L138).

> The colour stage of the `d ∂ bard` block.

```lean
noncomputable def dbardColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.dbardBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.dbardColourStep_contraction`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L148).

> The colour contraction of the `d ∂ bard` block, written out.

```lean
lemma dbardColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.dbardColourStep f f' q l w w').spanningVector
      = ∑ a : Fin 3, h.dbardBlk f f' q l a a w w'
```

**`StandardModel.IsFermionSector.dbardIsospinStep`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L154).

> The isospin stage of the `d ∂ bard` block.

```lean
noncomputable def dbardIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.dbardColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_dbard`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L168).

> The doubly contracted `d ∂ bard` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_dbard (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.dbardIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.dbardLorentzStep`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L183).

> The Lorentz stage of the `d ∂ bard` block.

```lean
noncomputable def dbardLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.dbardIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.dbardKineticBlock`**, a def, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L191).

> The `d ∂ bard` block as a kinetic block.

```lean
noncomputable def dbardKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.IsFermionSector.barddBlk`**, a def, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L203).

> The components of the block `bard ∂ d`: an underived conjugate down-singlet symbol against a
> once-derived down-singlet symbol.

```lean
noncomputable def barddBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.isSU3FundamentalAntiFundamental_barddBlk`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L209).

> The two colour indices of the `bard ∂ d` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU3FundamentalAntiFundamental_barddBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 3 => h.barddBlk f f' q l (n 0) (n 1) w w')
```

**`StandardModel.IsFermionSector.repGauge_su2_barddBlk`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L218).

> An isospin transformation fixes the `bard ∂ d` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_barddBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.barddBlk f f' q l c c' w w')
      = h.barddBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.repGauge_u1_barddBlk`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L227).

> A hypercharge transformation fixes the `bard ∂ d` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_barddBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barddBlk f f' q l c c' w w')
      = h.barddBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.barddColourStep`**, a def, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L236).

> The colour stage of the `bard ∂ d` block.

```lean
noncomputable def barddColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.barddBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.barddColourStep_contraction`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L246).

> The colour contraction of the `bard ∂ d` block, written out.

```lean
lemma barddColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.barddColourStep f f' q l w w').spanningVector
      = ∑ a : Fin 3, h.barddBlk f f' q l a a w w'
```

**`StandardModel.IsFermionSector.barddIsospinStep`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L252).

> The isospin stage of the `bard ∂ d` block.

```lean
noncomputable def barddIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.barddColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_bardd`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L266).

> The doubly contracted `bard ∂ d` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_bardd (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.barddIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.barddLorentzStep`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L282).

> The Lorentz stage of the `bard ∂ d` block.

```lean
noncomputable def barddLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.barddIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.barddKineticBlock`**, a def, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L290).

> The `bard ∂ d` block as a kinetic block.

```lean
noncomputable def barddKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.IsFermionSector.ubaruBlk`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L302).

> The components of the block `u ∂ baru`: an underived up-singlet symbol against a
> once-derived conjugate up-singlet symbol.

```lean
noncomputable def ubaruBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.isSU3FundamentalAntiFundamental_ubaruBlk`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L308).

> The two colour indices of the `u ∂ baru` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU3FundamentalAntiFundamental_ubaruBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 3 => h.ubaruBlk f f' q l (n 0) (n 1) w w')
```

**`StandardModel.IsFermionSector.repGauge_su2_ubaruBlk`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L318).

> An isospin transformation fixes the `u ∂ baru` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_ubaruBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.ubaruBlk f f' q l c c' w w')
      = h.ubaruBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.repGauge_u1_ubaruBlk`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L327).

> A hypercharge transformation fixes the `u ∂ baru` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_ubaruBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.ubaruBlk f f' q l c c' w w')
      = h.ubaruBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.ubaruColourStep`**, a def, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L336).

> The colour stage of the `u ∂ baru` block.

```lean
noncomputable def ubaruColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.ubaruBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.ubaruColourStep_contraction`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L346).

> The colour contraction of the `u ∂ baru` block, written out.

```lean
lemma ubaruColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.ubaruColourStep f f' q l w w').spanningVector
      = ∑ a : Fin 3, h.ubaruBlk f f' q l a a w w'
```

**`StandardModel.IsFermionSector.ubaruIsospinStep`**, a def, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L352).

> The isospin stage of the `u ∂ baru` block.

```lean
noncomputable def ubaruIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.ubaruColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_ubaru`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L366).

> The doubly contracted `u ∂ baru` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_ubaru (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.ubaruIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.ubaruLorentzStep`**, a def, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L382).

> The Lorentz stage of the `u ∂ baru` block.

```lean
noncomputable def ubaruLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.ubaruIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.ubaruKineticBlock`**, a def, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L390).

> The `u ∂ baru` block as a kinetic block.

```lean
noncomputable def ubaruKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.IsFermionSector.baruuBlk`**, a def, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L402).

> The components of the block `baru ∂ u`: an underived conjugate up-singlet symbol against a
> once-derived up-singlet symbol.

```lean
noncomputable def baruuBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.isSU3FundamentalAntiFundamental_baruuBlk`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L408).

> The two colour indices of the `baru ∂ u` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU3FundamentalAntiFundamental_baruuBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 3 => h.baruuBlk f f' q l (n 0) (n 1) w w')
```

**`StandardModel.IsFermionSector.repGauge_su2_baruuBlk`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L417).

> An isospin transformation fixes the `baru ∂ u` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_baruuBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.baruuBlk f f' q l c c' w w')
      = h.baruuBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.repGauge_u1_baruuBlk`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L426).

> A hypercharge transformation fixes the `baru ∂ u` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_baruuBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.baruuBlk f f' q l c c' w w')
      = h.baruuBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.baruuColourStep`**, a def, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L435).

> The colour stage of the `baru ∂ u` block.

```lean
noncomputable def baruuColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.baruuBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.baruuColourStep_contraction`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L445).

> The colour contraction of the `baru ∂ u` block, written out.

```lean
lemma baruuColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.baruuColourStep f f' q l w w').spanningVector
      = ∑ a : Fin 3, h.baruuBlk f f' q l a a w w'
```

**`StandardModel.IsFermionSector.baruuIsospinStep`**, a def, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L451).

> The isospin stage of the `baru ∂ u` block.

```lean
noncomputable def baruuIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.baruuColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_baruu`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L465).

> The doubly contracted `baru ∂ u` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_baruu (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.baruuIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.baruuLorentzStep`**, a def, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L481).

> The Lorentz stage of the `baru ∂ u` block.

```lean
noncomputable def baruuLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.baruuIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.baruuKineticBlock`**, a def, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L489).

> The `baru ∂ u` block as a kinetic block.

```lean
noncomputable def baruuKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

## B. The two quark-doublet pairings

> The quark doublet carries colour, isospin and hypercharge, so its two pairings are the only
> blocks that run both a colour and an isospin stage.

**`StandardModel.IsFermionSector.QbarQBlk`**, a def, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L510).

> The components of the block `Q ∂ barQ`: an underived quark-doublet symbol against a
> once-derived conjugate quark-doublet symbol.

```lean
noncomputable def QbarQBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.isSU3FundamentalAntiFundamental_QbarQBlk`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L516).

> The two colour indices of the `Q ∂ barQ` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU3FundamentalAntiFundamental_QbarQBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 3 => h.QbarQBlk f f' q l (n 0) (n 1) w w')
```

**`StandardModel.IsFermionSector.isSU2FundamentalAntiFundamental_QbarQBlk`**, a lemma, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L526).

> The two isospin indices of the `Q ∂ barQ` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU2FundamentalAntiFundamental_QbarQBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' : Fin 3) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 2 => h.QbarQBlk f f' q l c c' (n 0) (n 1))
```

**`StandardModel.IsFermionSector.repGauge_u1_QbarQBlk`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L536).

> A hypercharge transformation fixes the `Q ∂ barQ` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_QbarQBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.QbarQBlk f f' q l c c' w w')
      = h.QbarQBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.QbarQColourStep`**, a def, [line 545](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L545).

> The colour stage of the `Q ∂ barQ` block.

```lean
noncomputable def QbarQColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.QbarQBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.QbarQColourStep_contraction`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L555).

> The colour contraction of the `Q ∂ barQ` block, written out.

```lean
lemma QbarQColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.QbarQColourStep f f' q l w w').spanningVector
      = ∑ a : Fin 3, h.QbarQBlk f f' q l a a w w'
```

**`StandardModel.IsFermionSector.QbarQIsospinStep`**, a def, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L561).

> The isospin stage of the `Q ∂ barQ` block.

```lean
noncomputable def QbarQIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.QbarQColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_QbarQ`**, a lemma, [line 574](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L574).

> The doubly contracted `Q ∂ barQ` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_QbarQ (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.QbarQIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.QbarQLorentzStep`**, a def, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L594).

> The Lorentz stage of the `Q ∂ barQ` block.

```lean
noncomputable def QbarQLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.QbarQIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.QbarQKineticBlock`**, a def, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L602).

> The `Q ∂ barQ` block as a kinetic block.

```lean
noncomputable def QbarQKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.IsFermionSector.barQQBlk`**, a def, [line 614](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L614).

> The components of the block `barQ ∂ Q`: an underived conjugate quark-doublet symbol against a
> once-derived quark-doublet symbol.

```lean
noncomputable def barQQBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.isSU3FundamentalAntiFundamental_barQQBlk`**, a lemma, [line 620](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L620).

> The two colour indices of the `barQ ∂ Q` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU3FundamentalAntiFundamental_barQQBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    IsSU3FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 3 => h.barQQBlk f f' q l (n 0) (n 1) w w')
```

**`StandardModel.IsFermionSector.isSU2FundamentalAntiFundamental_barQQBlk`**, a lemma, [line 630](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L630).

> The two isospin indices of the `barQ ∂ Q` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU2FundamentalAntiFundamental_barQQBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' : Fin 3) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 2 => h.barQQBlk f f' q l c c' (n 0) (n 1))
```

**`StandardModel.IsFermionSector.repGauge_u1_barQQBlk`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L640).

> A hypercharge transformation fixes the `barQ ∂ Q` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_barQQBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barQQBlk f f' q l c c' w w')
      = h.barQQBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.barQQColourStep`**, a def, [line 649](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L649).

> The colour stage of the `barQ ∂ Q` block.

```lean
noncomputable def barQQColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.barQQBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.barQQColourStep_contraction`**, a lemma, [line 659](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L659).

> The colour contraction of the `barQ ∂ Q` block, written out.

```lean
lemma barQQColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.barQQColourStep f f' q l w w').spanningVector
      = ∑ a : Fin 3, h.barQQBlk f f' q l a a w w'
```

**`StandardModel.IsFermionSector.barQQIsospinStep`**, a def, [line 665](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L665).

> The isospin stage of the `barQ ∂ Q` block.

```lean
noncomputable def barQQIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.barQQColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_barQQ`**, a lemma, [line 678](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L678).

> The doubly contracted `barQ ∂ Q` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_barQQ (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.barQQIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.barQQLorentzStep`**, a def, [line 698](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L698).

> The Lorentz stage of the `barQ ∂ Q` block.

```lean
noncomputable def barQQLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.barQQIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.barQQKineticBlock`**, a def, [line 706](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L706).

> The `barQ ∂ Q` block as a kinetic block.

```lean
noncomputable def barQQKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

## C. The two lepton-doublet pairings

> The lepton doublet carries isospin and hypercharge but no colour, so its colour stage is
> the trivial one.

**`StandardModel.IsFermionSector.LbarLBlk`**, a def, [line 727](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L727).

> The components of the block `L ∂ barL`: an underived lepton-doublet symbol against a
> once-derived conjugate lepton-doublet symbol.

```lean
noncomputable def LbarLBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.repGauge_su3_LbarLBlk`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L733).

> A colour transformation fixes the `L ∂ barL` block, neither symbol carrying
> colour.

```lean
lemma repGauge_su3_LbarLBlk (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.LbarLBlk f f' q l c c' w w')
      = h.LbarLBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.isSU2FundamentalAntiFundamental_LbarLBlk`**, a lemma, [line 742](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L742).

> The two isospin indices of the `L ∂ barL` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU2FundamentalAntiFundamental_LbarLBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' : Fin 3) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 2 => h.LbarLBlk f f' q l c c' (n 0) (n 1))
```

**`StandardModel.IsFermionSector.repGauge_u1_LbarLBlk`**, a lemma, [line 752](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L752).

> A hypercharge transformation fixes the `L ∂ barL` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_LbarLBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.LbarLBlk f f' q l c c' w w')
      = h.LbarLBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.LbarLColourStep`**, a def, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L761).

> The colour stage of the `L ∂ barL` block.

```lean
noncomputable def LbarLColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.LbarLBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.LbarLColourStep_contraction`**, a lemma, [line 771](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L771).

> The colour contraction of the `L ∂ barL` block, written out.

```lean
lemma LbarLColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.LbarLColourStep f f' q l w w').spanningVector
      = h.LbarLBlk f f' q l 0 0 w w'
```

**`StandardModel.IsFermionSector.LbarLIsospinStep`**, a def, [line 777](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L777).

> The isospin stage of the `L ∂ barL` block.

```lean
noncomputable def LbarLIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.LbarLColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_LbarL`**, a lemma, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L789).

> The doubly contracted `L ∂ barL` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_LbarL (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.LbarLIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.LbarLLorentzStep`**, a def, [line 808](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L808).

> The Lorentz stage of the `L ∂ barL` block.

```lean
noncomputable def LbarLLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.LbarLIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.LbarLKineticBlock`**, a def, [line 816](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L816).

> The `L ∂ barL` block as a kinetic block.

```lean
noncomputable def LbarLKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.IsFermionSector.barLLBlk`**, a def, [line 828](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L828).

> The components of the block `barL ∂ L`: an underived conjugate lepton-doublet symbol against a
> once-derived lepton-doublet symbol.

```lean
noncomputable def barLLBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.repGauge_su3_barLLBlk`**, a lemma, [line 834](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L834).

> A colour transformation fixes the `barL ∂ L` block, neither symbol carrying
> colour.

```lean
lemma repGauge_su3_barLLBlk (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.barLLBlk f f' q l c c' w w')
      = h.barLLBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.isSU2FundamentalAntiFundamental_barLLBlk`**, a lemma, [line 843](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L843).

> The two isospin indices of the `barL ∂ L` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isSU2FundamentalAntiFundamental_barLLBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' : Fin 3) :
    IsSU2FundamentalAntiFundamental B repGauge
      (fun n : Fin 2 → Fin 2 => h.barLLBlk f f' q l c c' (n 0) (n 1))
```

**`StandardModel.IsFermionSector.repGauge_u1_barLLBlk`**, a lemma, [line 852](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L852).

> A hypercharge transformation fixes the `barL ∂ L` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_barLLBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barLLBlk f f' q l c c' w w')
      = h.barLLBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.barLLColourStep`**, a def, [line 861](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L861).

> The colour stage of the `barL ∂ L` block.

```lean
noncomputable def barLLColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.barLLBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.barLLColourStep_contraction`**, a lemma, [line 871](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L871).

> The colour contraction of the `barL ∂ L` block, written out.

```lean
lemma barLLColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.barLLColourStep f f' q l w w').spanningVector
      = h.barLLBlk f f' q l 0 0 w w'
```

**`StandardModel.IsFermionSector.barLLIsospinStep`**, a def, [line 877](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L877).

> The isospin stage of the `barL ∂ L` block.

```lean
noncomputable def barLLIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.barLLColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_barLL`**, a lemma, [line 889](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L889).

> The doubly contracted `barL ∂ L` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_barLL (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.barLLIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.barLLLorentzStep`**, a def, [line 908](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L908).

> The Lorentz stage of the `barL ∂ L` block.

```lean
noncomputable def barLLLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.barLLIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.barLLKineticBlock`**, a def, [line 916](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L916).

> The `barL ∂ L` block as a kinetic block.

```lean
noncomputable def barLLKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

## D. The two lepton-singlet pairings

> The lepton singlet carries only hypercharge and a spinor index, so both gauge stages are
> trivial and the whole classification is the Lorentz one.

**`StandardModel.IsFermionSector.ebareBlk`**, a def, [line 937](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L937).

> The components of the block `e ∂ bare`: an underived lepton-singlet symbol against a
> once-derived conjugate lepton-singlet symbol.

```lean
noncomputable def ebareBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.repGauge_su3_ebareBlk`**, a lemma, [line 943](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L943).

> A colour transformation fixes the `e ∂ bare` block, neither symbol carrying
> colour.

```lean
lemma repGauge_su3_ebareBlk (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.ebareBlk f f' q l c c' w w')
      = h.ebareBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.repGauge_su2_ebareBlk`**, a lemma, [line 952](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L952).

> An isospin transformation fixes the `e ∂ bare` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_ebareBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.ebareBlk f f' q l c c' w w')
      = h.ebareBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.repGauge_u1_ebareBlk`**, a lemma, [line 961](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L961).

> A hypercharge transformation fixes the `e ∂ bare` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_ebareBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.ebareBlk f f' q l c c' w w')
      = h.ebareBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.ebareColourStep`**, a def, [line 970](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L970).

> The colour stage of the `e ∂ bare` block.

```lean
noncomputable def ebareColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.ebareBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.ebareColourStep_contraction`**, a lemma, [line 980](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L980).

> The colour contraction of the `e ∂ bare` block, written out.

```lean
lemma ebareColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.ebareColourStep f f' q l w w').spanningVector
      = h.ebareBlk f f' q l 0 0 w w'
```

**`StandardModel.IsFermionSector.ebareIsospinStep`**, a def, [line 986](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L986).

> The isospin stage of the `e ∂ bare` block.

```lean
noncomputable def ebareIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.ebareColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_ebare`**, a lemma, [line 1000](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1000).

> The doubly contracted `e ∂ bare` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_ebare (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.ebareIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.ebareLorentzStep`**, a def, [line 1015](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1015).

> The Lorentz stage of the `e ∂ bare` block.

```lean
noncomputable def ebareLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.ebareIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.ebareKineticBlock`**, a def, [line 1023](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1023).

> The `e ∂ bare` block as a kinetic block.

```lean
noncomputable def ebareKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.IsFermionSector.bareeBlk`**, a def, [line 1035](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1035).

> The components of the block `bare ∂ e`: an underived conjugate lepton-singlet symbol against a
> once-derived lepton-singlet symbol.

```lean
noncomputable def bareeBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
```

**`StandardModel.IsFermionSector.repGauge_su3_bareeBlk`**, a lemma, [line 1041](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1041).

> A colour transformation fixes the `bare ∂ e` block, neither symbol carrying
> colour.

```lean
lemma repGauge_su3_bareeBlk (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.bareeBlk f f' q l c c' w w')
      = h.bareeBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.repGauge_su2_bareeBlk`**, a lemma, [line 1050](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1050).

> An isospin transformation fixes the `bare ∂ e` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_bareeBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.bareeBlk f f' q l c c' w w')
      = h.bareeBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.repGauge_u1_bareeBlk`**, a lemma, [line 1059](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1059).

> A hypercharge transformation fixes the `bare ∂ e` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_bareeBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.bareeBlk f f' q l c c' w w')
      = h.bareeBlk f f' q l c c' w w'
```

**`StandardModel.IsFermionSector.bareeColourStep`**, a def, [line 1068](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1068).

> The colour stage of the `bare ∂ e` block.

```lean
noncomputable def bareeColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => h.bareeBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.IsFermionSector.bareeColourStep_contraction`**, a lemma, [line 1078](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1078).

> The colour contraction of the `bare ∂ e` block, written out.

```lean
lemma bareeColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (h.bareeColourStep f f' q l w w').spanningVector
      = h.bareeBlk f f' q l 0 0 w w'
```

**`StandardModel.IsFermionSector.bareeIsospinStep`**, a def, [line 1084](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1084).

> The isospin stage of the `bare ∂ e` block.

```lean
noncomputable def bareeIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (h.bareeColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_baree`**, a lemma, [line 1098](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1098).

> The doubly contracted `bare ∂ e` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isVectorDualLeftRightWeyl_baree (f f' : Fin 3) :
    IsVectorDualLeftRightWeyl B repLorentz
      (ofDualVectorComponents fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.bareeIsospinStep f f' p.1 p.2).spanningVector)
```

**`StandardModel.IsFermionSector.bareeLorentzStep`**, a def, [line 1113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1113).

> The Lorentz stage of the `bare ∂ e` block.

```lean
noncomputable def bareeLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (h.bareeIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.IsFermionSector.bareeKineticBlock`**, a def, [line 1121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean#L1121).

> The `bare ∂ e` block as a kinetic block.

```lean
noncomputable def bareeKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

## Depends on

- [The kinetic terms of the fermion sector](../part-05/isfermionsector-massweight-kineticfamilies.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticTerms.lean)
