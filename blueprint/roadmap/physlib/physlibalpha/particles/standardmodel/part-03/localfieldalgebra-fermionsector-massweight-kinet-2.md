---
declaration: module
origin: cited
lean: StandardModel.FermionSector.dbardBlk, StandardModel.FermionSector.isEquivariant_colourFundAntiFund_dbardBlk, StandardModel.FermionSector.repGauge_su2_dbardBlk, StandardModel.FermionSector.repGauge_u1_dbardBlk, StandardModel.FermionSector.dbardColourStep, StandardModel.FermionSector.dbardIsospinStep, StandardModel.FermionSector.isEquivariant_upDownRDownL_dbard, StandardModel.FermionSector.dbardLorentzStep
statement: formalized
proof: formalized
---

# The ten kinetic blocks

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionSector.MassWeight.KineticTerms`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean): 94 declarations, 94 with a docstring.

> The ten kinetic blocks of the fermion sector, each a conjugate pair with one covariant
> derivative, as instances of `KineticBlock`.

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
> What comes out of each block is one kinetic term per pair of generations. The join of the
> ten over the nine generation pairs is the kinetic span of the sector, assembled in
> `MassDimEight`.

## ii. Key results

> - `dbardKineticBlock`, `barddKineticBlock`, `ubaruKineticBlock`, `baruuKineticBlock`,
>   `QbarQKineticBlock`, `barQQKineticBlock`, `LbarLKineticBlock`, `barLLKineticBlock`,
>   `ebareKineticBlock`, `bareeKineticBlock` : the ten kinetic blocks.
> - `dbardBlk` and its nine companions : the components of each block, an underived symbol against
>   a once-derived symbol of the conjugate species.

## iv. References

> * None.

## A. The four quark-singlet pairings

> The down and up singlets carry colour and hypercharge and nothing else, so their four
> pairings run a genuine colour stage and a trivial isospin one.

**`StandardModel.FermionSector.dbardBlk`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L81).

> The components of the block `d ∂ bard`, an underived down-singlet symbol against a
> once-derived conjugate down-singlet symbol.

```lean
noncomputable def dbardBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isEquivariant_colourFundAntiFund_dbardBlk`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L88).

> The two colour indices of the `d ∂ bard` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_colourFundAntiFund_dbardBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun n : Fin 2 → Fin 3 => dbardBlk f f' q l (n 0) (n 1) w w') ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.repGauge_su2_dbardBlk`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L99).

> An isospin transformation fixes the `d ∂ bard` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_dbardBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (dbardBlk f f' q l c c' w w')
      = dbardBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.repGauge_u1_dbardBlk`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L108).

> A hypercharge transformation fixes the `d ∂ bard` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_dbardBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (dbardBlk f f' q l c c' w w')
      = dbardBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.dbardColourStep`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L117).

> The colour stage of the `d ∂ bard` block.

```lean
noncomputable def dbardColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => dbardBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.dbardIsospinStep`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L127).

> The isospin stage of the `d ∂ bard` block.

```lean
noncomputable def dbardIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (dbardColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_dbard`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L141).

> The doubly contracted `d ∂ bard` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_dbard (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (dbardIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.dbardLorentzStep`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L156).

> The Lorentz stage of the `d ∂ bard` block.

```lean
noncomputable def dbardLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (dbardIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.dbardKineticBlock`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L164).

> The `d ∂ bard` block as a kinetic block.

```lean
noncomputable def dbardKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.FermionSector.barddBlk`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L176).

> The components of the block `bard ∂ d`, an underived conjugate down-singlet symbol against a
> once-derived down-singlet symbol.

```lean
noncomputable def barddBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isEquivariant_colourFundAntiFund_barddBlk`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L183).

> The two colour indices of the `bard ∂ d` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_colourFundAntiFund_barddBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun n : Fin 2 → Fin 3 => barddBlk f f' q l (n 0) (n 1) w w') ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.repGauge_su2_barddBlk`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L193).

> An isospin transformation fixes the `bard ∂ d` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_barddBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (barddBlk f f' q l c c' w w')
      = barddBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.repGauge_u1_barddBlk`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L202).

> A hypercharge transformation fixes the `bard ∂ d` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_barddBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (barddBlk f f' q l c c' w w')
      = barddBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.barddColourStep`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L211).

> The colour stage of the `bard ∂ d` block.

```lean
noncomputable def barddColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => barddBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.barddIsospinStep`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L221).

> The isospin stage of the `bard ∂ d` block.

```lean
noncomputable def barddIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (barddColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_bardd`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L235).

> The doubly contracted `bard ∂ d` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_bardd (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (barddIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.barddLorentzStep`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L251).

> The Lorentz stage of the `bard ∂ d` block.

```lean
noncomputable def barddLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (barddIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.barddKineticBlock`**, a def, [line 259](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L259).

> The `bard ∂ d` block as a kinetic block.

```lean
noncomputable def barddKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.FermionSector.ubaruBlk`**, a def, [line 271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L271).

> The components of the block `u ∂ baru`, an underived up-singlet symbol against a
> once-derived conjugate up-singlet symbol.

```lean
noncomputable def ubaruBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isEquivariant_colourFundAntiFund_ubaruBlk`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L278).

> The two colour indices of the `u ∂ baru` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_colourFundAntiFund_ubaruBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun n : Fin 2 → Fin 3 => ubaruBlk f f' q l (n 0) (n 1) w w') ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.repGauge_su2_ubaruBlk`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L289).

> An isospin transformation fixes the `u ∂ baru` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_ubaruBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (ubaruBlk f f' q l c c' w w')
      = ubaruBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.repGauge_u1_ubaruBlk`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L298).

> A hypercharge transformation fixes the `u ∂ baru` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_ubaruBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (ubaruBlk f f' q l c c' w w')
      = ubaruBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.ubaruColourStep`**, a def, [line 307](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L307).

> The colour stage of the `u ∂ baru` block.

```lean
noncomputable def ubaruColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => ubaruBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.ubaruIsospinStep`**, a def, [line 317](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L317).

> The isospin stage of the `u ∂ baru` block.

```lean
noncomputable def ubaruIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (ubaruColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_ubaru`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L331).

> The doubly contracted `u ∂ baru` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_ubaru (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (ubaruIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.ubaruLorentzStep`**, a def, [line 347](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L347).

> The Lorentz stage of the `u ∂ baru` block.

```lean
noncomputable def ubaruLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (ubaruIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.ubaruKineticBlock`**, a def, [line 355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L355).

> The `u ∂ baru` block as a kinetic block.

```lean
noncomputable def ubaruKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.FermionSector.baruuBlk`**, a def, [line 367](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L367).

> The components of the block `baru ∂ u`, an underived conjugate up-singlet symbol against a
> once-derived up-singlet symbol.

```lean
noncomputable def baruuBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isEquivariant_colourFundAntiFund_baruuBlk`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L374).

> The two colour indices of the `baru ∂ u` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_colourFundAntiFund_baruuBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun n : Fin 2 → Fin 3 => baruuBlk f f' q l (n 0) (n 1) w w') ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.repGauge_su2_baruuBlk`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L384).

> An isospin transformation fixes the `baru ∂ u` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_baruuBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (baruuBlk f f' q l c c' w w')
      = baruuBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.repGauge_u1_baruuBlk`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L393).

> A hypercharge transformation fixes the `baru ∂ u` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_baruuBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (baruuBlk f f' q l c c' w w')
      = baruuBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.baruuColourStep`**, a def, [line 402](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L402).

> The colour stage of the `baru ∂ u` block.

```lean
noncomputable def baruuColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => baruuBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.baruuIsospinStep`**, a def, [line 412](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L412).

> The isospin stage of the `baru ∂ u` block.

```lean
noncomputable def baruuIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (baruuColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_baruu`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L426).

> The doubly contracted `baru ∂ u` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_baruu (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (baruuIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.baruuLorentzStep`**, a def, [line 442](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L442).

> The Lorentz stage of the `baru ∂ u` block.

```lean
noncomputable def baruuLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (baruuIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.baruuKineticBlock`**, a def, [line 450](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L450).

> The `baru ∂ u` block as a kinetic block.

```lean
noncomputable def baruuKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

## B. The two quark-doublet pairings

> The quark doublet carries colour, isospin and hypercharge, so its two pairings are the only
> blocks that run both a colour and an isospin stage.

**`StandardModel.FermionSector.QbarQBlk`**, a def, [line 471](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L471).

> The components of the block `Q ∂ barQ`, an underived quark-doublet symbol against a
> once-derived conjugate quark-doublet symbol.

```lean
noncomputable def QbarQBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isEquivariant_colourFundAntiFund_QbarQBlk`**, a lemma, [line 478](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L478).

> The two colour indices of the `Q ∂ barQ` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_colourFundAntiFund_QbarQBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun n : Fin 2 → Fin 3 => QbarQBlk f f' q l (n 0) (n 1) w w') ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.isEquivariant_isospinFundAntiFund_QbarQBlk`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L489).

> The two isospin indices of the `Q ∂ barQ` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_isospinFundAntiFund_QbarQBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' : Fin 3) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun n : Fin 2 → Fin 2 => QbarQBlk f f' q l c c' (n 0) (n 1)) ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.repGauge_u1_QbarQBlk`**, a lemma, [line 500](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L500).

> A hypercharge transformation fixes the `Q ∂ barQ` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_QbarQBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (QbarQBlk f f' q l c c' w w')
      = QbarQBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.QbarQColourStep`**, a def, [line 509](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L509).

> The colour stage of the `Q ∂ barQ` block.

```lean
noncomputable def QbarQColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => QbarQBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.QbarQColourStep_contraction`**, a lemma, [line 519](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L519).

> The colour contraction of the `Q ∂ barQ` block, written out.

```lean
lemma QbarQColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (QbarQColourStep f f' q l w w').spanningVector
      = ∑ a : Fin 3, QbarQBlk f f' q l a a w w'
```

**`StandardModel.FermionSector.QbarQIsospinStep`**, a def, [line 525](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L525).

> The isospin stage of the `Q ∂ barQ` block.

```lean
noncomputable def QbarQIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (QbarQColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_QbarQ`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L538).

> The doubly contracted `Q ∂ barQ` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_QbarQ (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (QbarQIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.QbarQLorentzStep`**, a def, [line 558](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L558).

> The Lorentz stage of the `Q ∂ barQ` block.

```lean
noncomputable def QbarQLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (QbarQIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.QbarQKineticBlock`**, a def, [line 566](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L566).

> The `Q ∂ barQ` block as a kinetic block.

```lean
noncomputable def QbarQKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.FermionSector.barQQBlk`**, a def, [line 578](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L578).

> The components of the block `barQ ∂ Q`, an underived conjugate quark-doublet symbol against a
> once-derived quark-doublet symbol.

```lean
noncomputable def barQQBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isEquivariant_colourFundAntiFund_barQQBlk`**, a lemma, [line 585](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L585).

> The two colour indices of the `barQ ∂ Q` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_colourFundAntiFund_barQQBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (w w' : Fin 2) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun n : Fin 2 → Fin 3 => barQQBlk f f' q l (n 0) (n 1) w w') ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.isEquivariant_isospinFundAntiFund_barQQBlk`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L596).

> The two isospin indices of the `barQ ∂ Q` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_isospinFundAntiFund_barQQBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' : Fin 3) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun n : Fin 2 → Fin 2 => barQQBlk f f' q l c c' (n 0) (n 1)) ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.repGauge_u1_barQQBlk`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L607).

> A hypercharge transformation fixes the `barQ ∂ Q` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_barQQBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (barQQBlk f f' q l c c' w w')
      = barQQBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.barQQColourStep`**, a def, [line 616](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L616).

> The colour stage of the `barQ ∂ Q` block.

```lean
noncomputable def barQQColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => barQQBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.barQQColourStep_contraction`**, a lemma, [line 626](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L626).

> The colour contraction of the `barQ ∂ Q` block, written out.

```lean
lemma barQQColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (barQQColourStep f f' q l w w').spanningVector
      = ∑ a : Fin 3, barQQBlk f f' q l a a w w'
```

**`StandardModel.FermionSector.barQQIsospinStep`**, a def, [line 632](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L632).

> The isospin stage of the `barQ ∂ Q` block.

```lean
noncomputable def barQQIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (barQQColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_barQQ`**, a lemma, [line 645](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L645).

> The doubly contracted `barQ ∂ Q` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_barQQ (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (barQQIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.barQQLorentzStep`**, a def, [line 665](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L665).

> The Lorentz stage of the `barQ ∂ Q` block.

```lean
noncomputable def barQQLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (barQQIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.barQQKineticBlock`**, a def, [line 673](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L673).

> The `barQ ∂ Q` block as a kinetic block.

```lean
noncomputable def barQQKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

## C. The two lepton-doublet pairings

> The lepton doublet carries isospin and hypercharge but no colour, so its colour stage is
> the trivial one.

**`StandardModel.FermionSector.LbarLBlk`**, a def, [line 694](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L694).

> The components of the block `L ∂ barL`, an underived lepton-doublet symbol against a
> once-derived conjugate lepton-doublet symbol.

```lean
noncomputable def LbarLBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.repGauge_su3_LbarLBlk`**, a lemma, [line 701](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L701).

> A colour transformation fixes the `L ∂ barL` block, neither symbol carrying
> colour.

```lean
lemma repGauge_su3_LbarLBlk (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((U, 1, 1) : GaugeGroupI) (LbarLBlk f f' q l c c' w w')
      = LbarLBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.isEquivariant_isospinFundAntiFund_LbarLBlk`**, a lemma, [line 710](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L710).

> The two isospin indices of the `L ∂ barL` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_isospinFundAntiFund_LbarLBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' : Fin 3) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun n : Fin 2 → Fin 2 => LbarLBlk f f' q l c c' (n 0) (n 1)) ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.repGauge_u1_LbarLBlk`**, a lemma, [line 721](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L721).

> A hypercharge transformation fixes the `L ∂ barL` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_LbarLBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (LbarLBlk f f' q l c c' w w')
      = LbarLBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.LbarLColourStep`**, a def, [line 730](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L730).

> The colour stage of the `L ∂ barL` block.

```lean
noncomputable def LbarLColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => LbarLBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.LbarLColourStep_contraction`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L740).

> The colour contraction of the `L ∂ barL` block, written out.

```lean
lemma LbarLColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (LbarLColourStep f f' q l w w').spanningVector
      = LbarLBlk f f' q l 0 0 w w'
```

**`StandardModel.FermionSector.LbarLIsospinStep`**, a def, [line 746](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L746).

> The isospin stage of the `L ∂ barL` block.

```lean
noncomputable def LbarLIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (LbarLColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_LbarL`**, a lemma, [line 758](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L758).

> The doubly contracted `L ∂ barL` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_LbarL (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (LbarLIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.LbarLLorentzStep`**, a def, [line 777](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L777).

> The Lorentz stage of the `L ∂ barL` block.

```lean
noncomputable def LbarLLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (LbarLIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.LbarLKineticBlock`**, a def, [line 785](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L785).

> The `L ∂ barL` block as a kinetic block.

```lean
noncomputable def LbarLKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.FermionSector.barLLBlk`**, a def, [line 797](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L797).

> The components of the block `barL ∂ L`, an underived conjugate lepton-doublet symbol against a
> once-derived lepton-doublet symbol.

```lean
noncomputable def barLLBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.repGauge_su3_barLLBlk`**, a lemma, [line 804](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L804).

> A colour transformation fixes the `barL ∂ L` block, neither symbol carrying
> colour.

```lean
lemma repGauge_su3_barLLBlk (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((U, 1, 1) : GaugeGroupI) (barLLBlk f f' q l c c' w w')
      = barLLBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.isEquivariant_isospinFundAntiFund_barLLBlk`**, a lemma, [line 813](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L813).

> The two isospin indices of the `barL ∂ L` block are one fundamental and one
> anti-fundamental, the barred symbol supplying the fundamental one.

```lean
lemma isEquivariant_isospinFundAntiFund_barLLBlk (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' : Fin 3) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun n : Fin 2 → Fin 2 => barLLBlk f f' q l c c' (n 0) (n 1)) ∘
          fundAntiFundIdx))
```

**`StandardModel.FermionSector.repGauge_u1_barLLBlk`**, a lemma, [line 823](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L823).

> A hypercharge transformation fixes the `barL ∂ L` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_barLLBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (barLLBlk f f' q l c c' w w')
      = barLLBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.barLLColourStep`**, a def, [line 832](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L832).

> The colour stage of the `barL ∂ L` block.

```lean
noncomputable def barLLColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => barLLBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.barLLColourStep_contraction`**, a lemma, [line 842](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L842).

> The colour contraction of the `barL ∂ L` block, written out.

```lean
lemma barLLColourStep_contraction (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    (barLLColourStep f f' q l w w').spanningVector
      = barLLBlk f f' q l 0 0 w w'
```

**`StandardModel.FermionSector.barLLIsospinStep`**, a def, [line 848](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L848).

> The isospin stage of the `barL ∂ L` block.

```lean
noncomputable def barLLIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (barLLColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_barLL`**, a lemma, [line 860](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L860).

> The doubly contracted `barL ∂ L` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_barLL (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (barLLIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.barLLLorentzStep`**, a def, [line 879](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L879).

> The Lorentz stage of the `barL ∂ L` block.

```lean
noncomputable def barLLLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (barLLIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.barLLKineticBlock`**, a def, [line 887](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L887).

> The `barL ∂ L` block as a kinetic block.

```lean
noncomputable def barLLKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

## D. The two lepton-singlet pairings

> The lepton singlet carries only hypercharge and a spinor index, so both gauge stages are
> trivial and the whole classification is the Lorentz one.

**`StandardModel.FermionSector.ebareBlk`**, a def, [line 908](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L908).

> The components of the block `e ∂ bare`, an underived lepton-singlet symbol against a
> once-derived conjugate lepton-singlet symbol.

```lean
noncomputable def ebareBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.repGauge_su3_ebareBlk`**, a lemma, [line 915](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L915).

> A colour transformation fixes the `e ∂ bare` block, neither symbol carrying
> colour.

```lean
lemma repGauge_su3_ebareBlk (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((U, 1, 1) : GaugeGroupI) (ebareBlk f f' q l c c' w w')
      = ebareBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.repGauge_su2_ebareBlk`**, a lemma, [line 924](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L924).

> An isospin transformation fixes the `e ∂ bare` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_ebareBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (ebareBlk f f' q l c c' w w')
      = ebareBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.repGauge_u1_ebareBlk`**, a lemma, [line 933](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L933).

> A hypercharge transformation fixes the `e ∂ bare` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_ebareBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (ebareBlk f f' q l c c' w w')
      = ebareBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.ebareColourStep`**, a def, [line 942](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L942).

> The colour stage of the `e ∂ bare` block.

```lean
noncomputable def ebareColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => ebareBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.ebareIsospinStep`**, a def, [line 952](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L952).

> The isospin stage of the `e ∂ bare` block.

```lean
noncomputable def ebareIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (ebareColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_ebare`**, a lemma, [line 966](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L966).

> The doubly contracted `e ∂ bare` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_ebare (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (ebareIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.ebareLorentzStep`**, a def, [line 981](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L981).

> The Lorentz stage of the `e ∂ bare` block.

```lean
noncomputable def ebareLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (ebareIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.ebareKineticBlock`**, a def, [line 989](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L989).

> The `e ∂ bare` block as a kinetic block.

```lean
noncomputable def ebareKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

**`StandardModel.FermionSector.bareeBlk`**, a def, [line 1001](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L1001).

> The components of the block `bare ∂ e`, an underived conjugate lepton-singlet symbol against a
> once-derived lepton-singlet symbol.

```lean
noncomputable def bareeBlk (f f' : Fin 3) :
    (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 →
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.repGauge_su3_bareeBlk`**, a lemma, [line 1008](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L1008).

> A colour transformation fixes the `bare ∂ e` block, neither symbol carrying
> colour.

```lean
lemma repGauge_su3_bareeBlk (U : specialUnitaryGroup (Fin 3) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((U, 1, 1) : GaugeGroupI) (bareeBlk f f' q l c c' w w')
      = bareeBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.repGauge_su2_bareeBlk`**, a lemma, [line 1017](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L1017).

> An isospin transformation fixes the `bare ∂ e` block, neither symbol carrying
> isospin.

```lean
lemma repGauge_su2_bareeBlk (V : specialUnitaryGroup (Fin 2) ℂ) (f f' : Fin 3)
    (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, V, 1) : GaugeGroupI) (bareeBlk f f' q l c c' w w')
      = bareeBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.repGauge_u1_bareeBlk`**, a lemma, [line 1026](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L1026).

> A hypercharge transformation fixes the `bare ∂ e` block, the hypercharges of a
> species and its conjugate cancelling.

```lean
lemma repGauge_u1_bareeBlk (t : unitary ℂ) (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) (c c' w w' : _) :
    repGauge ((1, 1, t) : GaugeGroupI) (bareeBlk f f' q l c c' w w')
      = bareeBlk f f' q l c c' w w'
```

**`StandardModel.FermionSector.bareeColourStep`**, a def, [line 1035](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L1035).

> The colour stage of the `bare ∂ e` block.

```lean
noncomputable def bareeColourStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2)
    (w w' : Fin 2) :
    InvariantReductionToSpan
      (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 3 => bareeBlk f f' q l (n 0) (n 1) w w'))
```

**`StandardModel.FermionSector.bareeIsospinStep`**, a def, [line 1045](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L1045).

> The isospin stage of the `bare ∂ e` block.

```lean
noncomputable def bareeIsospinStep (f f' : Fin 3) (q : Fin 1 ⊕ Fin 3)
    (l : Fin 2 × Fin 2) :
    InvariantReductionToSpan
      (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 2 =>
        (bareeColourStep f f' q l (n 0) (n 1)).spanningVector))
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_baree`**, a lemma, [line 1059](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L1059).

> The doubly contracted `bare ∂ e` block carries one four-vector index and a pair of
> dual opposite-chirality Weyl indices.

```lean
lemma isEquivariant_upDownRDownL_baree (f f' : Fin 3) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (bareeIsospinStep f f' p.1 p.2).spanningVector) ∘ dualIndexEquiv))
```

**`StandardModel.FermionSector.bareeLorentzStep`**, a def, [line 1074](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L1074).

> The Lorentz stage of the `bare ∂ e` block.

```lean
noncomputable def bareeLorentzStep (f f' : Fin 3) :
    InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
      (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
        (bareeIsospinStep f f' p.1 p.2).spanningVector))
```

**`StandardModel.FermionSector.bareeKineticBlock`**, a def, [line 1082](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean#L1082).

> The `bare ∂ e` block as a kinetic block.

```lean
noncomputable def bareeKineticBlock (f f' : Fin 3) : KineticBlock repGauge repLorentz
```

## Depends on

- [The kinetic terms of the fermion sector](localfieldalgebra-fermionsector-massweight-kinet.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticTerms.lean)
