---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.higgsSubmodule_zero_le, StandardModel.LocalCovFieldAlgebra.barHiggsSubmodule_zero_le, StandardModel.LocalCovFieldAlgebra.range_d_eq, StandardModel.LocalCovFieldAlgebra.range_bard_eq, StandardModel.LocalCovFieldAlgebra.range_u_eq, StandardModel.LocalCovFieldAlgebra.range_baru_eq, StandardModel.LocalCovFieldAlgebra.range_Q_eq, StandardModel.LocalCovFieldAlgebra.range_barQ_eq
statement: formalized
proof: formalized
---

# The Yukawa sector at mass weight eight

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.YukawaSector.MassDimEight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean): 55 declarations, 55 with a docstring.

> The gauge- and Lorentz-invariant Yukawa terms of the Standard Model's covariant field algebra.

## i. Overview

> Everything below is stated about the covariant field algebra `fieldData.LocalCovFieldAlgebra` of the
> Standard Model.
>
> This is the theorem the Yukawa sector exists for.  At mass weight eight the sector is one
> Higgs tower against two underived fermion towers, and the claim proved here is that its
> gauge- and Lorentz-invariant content, modulo a submodule `S` stable under both groups, is
> exactly the span of the six Yukawa couplings over the nine family pairs.  Nothing else
> survives, neither a fourth coupling, nor extra colour or isospin structure inside a surviving
> block, nor an invariant carrying a free spinor index.
>
> Three things are already done and are used as given.  Hypercharge has sieved the two
> hundred blocks of the gauge weight decomposition down to twelve, in
> `sectorMassWeightEightGaugeWeight_piece_zero`.  A gauge invariant of the sector lies in
> that weight-zero piece modulo `S`, by `mem_sectorMassWeightEight_piece_zero_sup_of_invariant`.
> And the six couplings, their index laws and their contractions are built in the `Families`
> files, together with `yukawaSpan_le_inf`, which is the easy direction of the equivalence.
>
> What is left is the reduction.  A block of the decomposition is a product of three symbol
> ranges, and the classification of its invariants is three classifications in a row —
> colour, then isospin, then Lorentz — each cutting the span down to the span of one
> contraction.  The three groups are different, and the fifty-four surviving blocks have to
> be reduced one at a time, so the argument is organised around a single relation
> `ReducesInvariantsTo σ V W`, saying that a `σ`-invariant of `V ⊔ S` lies in `W ⊔ S` whenever `S` is
> `σ`-stable. That relation composes, being transitive, antitone in its source, monotone in its
> target, and closed under joins of stable sources, and each `GaugeGroup` or `LorentzGroup`
> classification used here is an instance of it, packaged as an `InvariantReductionToSpan`.

## ii. Key results

> - `sectorMassWeightEightGaugeWeight_piece_zero_le` : the weight-zero piece inside the six
>   surviving block submodules.
> - `reducesInvariantsTo_yukawaSpan` : the six blocks, over the nine family pairs, reduce to the
>   Yukawa span.
> - `reducesInvariantsTo_sectorMassWeight_higgs_fermion_eight` : the sector at mass weight
>   eight reduces to the Yukawa span.
> - `mem_sectorMassWeight_higgs_fermion_eight_sup_and_gauge_lorentz_invariant_iff` : the
>   classification as an equivalence, in the form the sibling sectors state it in.

## iv. References

> * None.

## A. The symbol ranges as spans of components

**`StandardModel.LocalCovFieldAlgebra.higgsSubmodule_zero_le`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L89).

> The Higgs submodule without derivatives lies in the span of the Higgs components.

```lean
lemma higgsSubmodule_zero_le :
    ScalarSector.higgsSubmodule 0
      ≤ Submodule.span ℂ (Set.range (ScalarSector.higgs ![]))
```

**`StandardModel.LocalCovFieldAlgebra.barHiggsSubmodule_zero_le`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L100).

> The conjugate Higgs submodule without derivatives lies in the span of the conjugate
> Higgs components.

```lean
lemma barHiggsSubmodule_zero_le :
    ScalarSector.barHiggsSubmodule 0
      ≤ Submodule.span ℂ (Set.range (ScalarSector.barHiggs ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_d_eq`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L110).

> The range of the down-singlet symbol map is the span of its components.

```lean
lemma range_d_eq (f : Fin 3) :
    LinearMap.range (downSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.dComponent f ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_bard_eq`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L117).

> The range of the conjugate down-singlet symbol map is the span of its components.

```lean
lemma range_bard_eq (f : Fin 3) :
    LinearMap.range (conjDownSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.bardComponent f ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_u_eq`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L124).

> The range of the up-singlet symbol map is the span of its components.

```lean
lemma range_u_eq (f : Fin 3) :
    LinearMap.range (upSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.uComponent f ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_baru_eq`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L130).

> The range of the conjugate up-singlet symbol map is the span of its components.

```lean
lemma range_baru_eq (f : Fin 3) :
    LinearMap.range (conjUpSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.baruComponent f ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_Q_eq`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L137).

> The range of the quark-doublet symbol map is the span of its components.

```lean
lemma range_Q_eq (f : Fin 3) :
    LinearMap.range (quarkDoubletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.QComponent f ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_barQ_eq`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L144).

> The range of the conjugate quark-doublet symbol map is the span of its components.

```lean
lemma range_barQ_eq (f : Fin 3) :
    LinearMap.range (conjQuarkDoubletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.barQComponent f ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_L_eq`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L151).

> The range of the lepton-doublet symbol map is the span of its components.

```lean
lemma range_L_eq (f : Fin 3) :
    LinearMap.range (leptonDoubletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.LComponent f ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_barL_eq`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L158).

> The range of the conjugate lepton-doublet symbol map is the span of its components.

```lean
lemma range_barL_eq (f : Fin 3) :
    LinearMap.range (conjLeptonDoubletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.barLComponent f ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_e_eq`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L165).

> The range of the lepton-singlet symbol map is the span of its components.

```lean
lemma range_e_eq (f : Fin 3) :
    LinearMap.range (leptonSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.eComponent f ![]))
```

**`StandardModel.LocalCovFieldAlgebra.range_bare_eq`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L172).

> The range of the conjugate lepton-singlet symbol map is the span of its components.

```lean
lemma range_bare_eq (f : Fin 3) :
    LinearMap.range (conjLeptonSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (FermionSector.bareComponent f ![]))
```

## B. The block submodules and their stability

> A surviving block of the decomposition is the product of a Higgs range with two fermion
> ranges, and this is the submodule the classification of that block runs inside.  All six
> are carried into themselves by both groups, each factor being the range of an equivariant
> symbol map with no derivative slots for the Lorentz group to mix, and a product of stable
> submodules being stable.  That stability is what lets the six blocks — fifty-four of them
> once the family pairs are counted — be reduced one at a time, each in turn joining the
> error term of the others.

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_higgsSubmodule_zero`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L193).

> The Higgs submodule without derivatives is carried into itself by both groups.

```lean
lemma isStableUnder_higgsSubmodule_zero :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (ScalarSector.higgsSubmodule 0)
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_barHiggsSubmodule_zero`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L203).

> The conjugate Higgs submodule without derivatives is carried into itself by both
> groups.

```lean
lemma isStableUnder_barHiggsSubmodule_zero :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (ScalarSector.barHiggsSubmodule 0)
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_d`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L212).

> The range of the down-singlet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_d (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (downSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_bard`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L221).

> The range of the conjugate down-singlet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_bard (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (conjDownSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_u`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L229).

> The range of the up-singlet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_u (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (upSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_baru`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L238).

> The range of the conjugate up-singlet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_baru (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (conjUpSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_Q`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L246).

> The range of the quark-doublet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_Q (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (quarkDoubletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_barQ`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L255).

> The range of the conjugate quark-doublet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_barQ (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (conjQuarkDoubletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_L`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L263).

> The range of the lepton-doublet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_L (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (leptonDoubletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_barL`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L272).

> The range of the conjugate lepton-doublet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_barL (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (conjLeptonDoubletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_e`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L280).

> The range of the lepton-singlet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_e (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (leptonSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_range_bare`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L289).

> The range of the conjugate lepton-singlet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_bare (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LinearMap.range (conjLeptonSingletField f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

## C. The twelve surviving blocks as six submodules

> The twelve blocks that hypercharge leaves come in six transposed pairs, and a pair is one
> submodule: the two fermion factors commute as submodules, by `mul_comm_of_le_derivSubmodule`,
> so exchanging them changes nothing.  Under the join over family pairs the transposed block
> of `(f, f')` is the untransposed block of `(f', f)`, and the weight-zero piece of the sector
> lands inside the join of the six.

**`StandardModel.LocalCovFieldAlgebra.downBlockSubmodule`**, a def, [line 309](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L309).

> The submodule of the down-type block `H d barQ` of a family pair.

```lean
noncomputable def downBlockSubmodule (f f' : Fin 3) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.upBlockSubmodule`**, a def, [line 315](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L315).

> The submodule of the up-type block `H baru Q` of a family pair.

```lean
noncomputable def upBlockSubmodule (f f' : Fin 3) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.leptonBlockSubmodule`**, a def, [line 321](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L321).

> The submodule of the charged-lepton block `H barL e` of a family pair.

```lean
noncomputable def leptonBlockSubmodule (f f' : Fin 3) : Submodule ℂ
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barDownBlockSubmodule`**, a def, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L328).

> The submodule of the conjugate down-type block `barH bard Q` of a family pair.

```lean
noncomputable def barDownBlockSubmodule (f f' : Fin 3) : Submodule ℂ
    fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barUpBlockSubmodule`**, a def, [line 335](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L335).

> The submodule of the conjugate up-type block `barH u barQ` of a family pair.

```lean
noncomputable def barUpBlockSubmodule (f f' : Fin 3) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.barLeptonBlockSubmodule`**, a def, [line 341](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L341).

> The submodule of the conjugate charged-lepton block `barH L bare` of a family pair.

```lean
noncomputable def barLeptonBlockSubmodule
    (f f' : Fin 3) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_downBlockSubmodule`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L348).

> The down-type block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_downBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LocalCovFieldAlgebra.downBlockSubmodule f f')
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_upBlockSubmodule`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L360).

> The up-type block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_upBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LocalCovFieldAlgebra.upBlockSubmodule f f')
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_leptonBlockSubmodule`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L372).

> The charged-lepton block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_leptonBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LocalCovFieldAlgebra.leptonBlockSubmodule f f')
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_barDownBlockSubmodule`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L384).

> The conjugate down-type block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barDownBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LocalCovFieldAlgebra.barDownBlockSubmodule f f')
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_barUpBlockSubmodule`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L396).

> The conjugate up-type block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barUpBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LocalCovFieldAlgebra.barUpBlockSubmodule f f')
```

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_barLeptonBlockSubmodule`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L408).

> The conjugate charged-lepton block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barLeptonBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (LocalCovFieldAlgebra.barLeptonBlockSubmodule f f')
```

**`StandardModel.LocalCovFieldAlgebra.blockSubmodule`**, a def, [line 421](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L421).

> The join of the six block submodules over the nine family pairs, the submodule the weight-zero
> piece of the Yukawa sector at mass weight eight is contained in.

```lean
noncomputable def blockSubmodule : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.mul_mul_le_of_swap`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L431).

> A Yukawa product with its two fermion factors in the transposed order lies in any
> submodule containing the product in the original order, the two fermion ranges commuting.

```lean
lemma mul_mul_le_of_swap {H A B W : Submodule ℂ fieldData.LocalCovFieldAlgebra}
    (hA : A ≤ FermionSector.derivSubmodule 0) (hB : B ≤ FermionSector.derivSubmodule 0)
    (h : H * (B * A) ≤ W) : H * (A * B) ≤ W
```

**`StandardModel.LocalCovFieldAlgebra.sectorMassWeightEightGaugeWeight_piece_zero_le`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L442).

> The weight-zero piece of the Yukawa sector at mass weight eight lies in the join of the
> six block submodules over the nine family pairs. The twelve blocks of
> `sectorMassWeightEightGaugeWeight_piece_zero` become six because the two fermion factors
> of a block commute, so the transposed block of `(f, f')` is the block of `(f', f)`; and
> the weight refinement inside a block is dropped, hypercharge having already done its
> work and colour, isospin and Lorentz being what decide the rest.

```lean
lemma sectorMassWeightEightGaugeWeight_piece_zero_le :
    LocalCovFieldAlgebra.sectorMassWeightEightGaugeWeight.piece 0 ≤
      LocalCovFieldAlgebra.blockSubmodule
```

## D. The blocks reduce to the Yukawa terms

> Each block is classified in three stages, and each stage is the same move: one index law
> holds at every value of the indices it does not see, so a family of steps is applied at
> once by `InvariantReductionToSpan.reducesInvariantsTo_iSup`, and what comes out is the span of
> the contractions, which is the source of the next stage. Colour first, then isospin, then Lorentz —
> the order is forced, each contraction being a spectator of the ones after it.
>
> The two lepton blocks have no colour index at all, so their first stage is
> `InvariantReductionToSpan.ofFixed` rather than a classification: the block is already fixed by the
> colour factor and the stage reduces it to itself. That keeps them in the same three-stage shape as
> the four quark blocks.

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_downYukawa`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L504).

> The down-type block reduces to the down-type Yukawa term.

```lean
lemma reducesInvariantsTo_downYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI
      repLorentzGroup) (LocalCovFieldAlgebra.downBlockSubmodule f f')
      (ℂ ∙ LocalCovFieldAlgebra.downYukawa f f')
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_upYukawa`**, a lemma, [line 558](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L558).

> The up-type block reduces to the up-type Yukawa term. Isospin is contracted by the
> antisymmetric symbol here, the Higgs symbol and the quark doublet both carrying the
> anti-fundamental.

```lean
lemma reducesInvariantsTo_upYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI
      repLorentzGroup) (LocalCovFieldAlgebra.upBlockSubmodule f f')
      (ℂ ∙ LocalCovFieldAlgebra.upYukawa f f')
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_leptonYukawa`**, a lemma, [line 611](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L611).

> The charged-lepton block reduces to the charged-lepton Yukawa term. Its colour stage is
> the trivial one. The three symbols carry no colour index between them, so the block is
> fixed by the colour factor and the stage reduces it to itself.

```lean
lemma reducesInvariantsTo_leptonYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI
      repLorentzGroup) (LocalCovFieldAlgebra.leptonBlockSubmodule f f')
      (ℂ ∙ LocalCovFieldAlgebra.leptonYukawa f f')
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_barDownYukawa`**, a lemma, [line 662](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L662).

> The conjugate down-type block reduces to the conjugate down-type Yukawa term.

```lean
lemma reducesInvariantsTo_barDownYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI
      repLorentzGroup) (LocalCovFieldAlgebra.barDownBlockSubmodule f f')
      (ℂ ∙ LocalCovFieldAlgebra.barDownYukawa f f')
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_barUpYukawa`**, a lemma, [line 713](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L713).

> The conjugate up-type block reduces to the conjugate up-type Yukawa term.

```lean
lemma reducesInvariantsTo_barUpYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI
      repLorentzGroup) (LocalCovFieldAlgebra.barUpBlockSubmodule f f')
      (ℂ ∙ LocalCovFieldAlgebra.barUpYukawa f f')
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_barLeptonYukawa`**, a lemma, [line 766](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L766).

> The conjugate charged-lepton block reduces to the conjugate charged-lepton Yukawa term,
> again with the trivial colour stage.

```lean
lemma reducesInvariantsTo_barLeptonYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI
      repLorentzGroup) (LocalCovFieldAlgebra.barLeptonBlockSubmodule f f')
      (ℂ ∙ LocalCovFieldAlgebra.barLeptonYukawa f f')
```

## E. The classification of the invariants of mass weight eight

> The two directions meet.  Forwards: the torus reduces the sector to its weight-zero piece,
> the piece lies in the six block submodules, and the blocks reduce to the Yukawa span.
> Backwards: `yukawaSpan_le_inf` says the Yukawa span is made of invariants of the right mass
> weight to begin with, which turns the reduction into an equivalence rather than a one-way
> inclusion.

**`StandardModel.LocalCovFieldAlgebra.isFixedBy_yukawaSpan`**, a lemma, [line 830](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L830).

> The Yukawa span is fixed pointwise by both groups, `yukawaSpan_le_inf` placing it inside
> both spaces of invariants.

```lean
lemma isFixedBy_yukawaSpan : IsFixedBy (gaugeLorentzMaps repGaugeGroupI
    repLorentzGroup) LocalCovFieldAlgebra.yukawaSpan
```

**`StandardModel.LocalCovFieldAlgebra.span_downYukawa_le_yukawaSpan`**, a lemma, [line 840](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L840).

> The line through a down-type Yukawa term lies in the Yukawa span.

```lean
lemma span_downYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ LocalCovFieldAlgebra.downYukawa f f' ≤ LocalCovFieldAlgebra.yukawaSpan
```

**`StandardModel.LocalCovFieldAlgebra.span_upYukawa_le_yukawaSpan`**, a lemma, [line 848](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L848).

> The line through an up-type Yukawa term lies in the Yukawa span.

```lean
lemma span_upYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ LocalCovFieldAlgebra.upYukawa f f' ≤ LocalCovFieldAlgebra.yukawaSpan
```

**`StandardModel.LocalCovFieldAlgebra.span_leptonYukawa_le_yukawaSpan`**, a lemma, [line 856](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L856).

> The line through a charged-lepton Yukawa term lies in the Yukawa span.

```lean
lemma span_leptonYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ LocalCovFieldAlgebra.leptonYukawa f f' ≤ LocalCovFieldAlgebra.yukawaSpan
```

**`StandardModel.LocalCovFieldAlgebra.span_barDownYukawa_le_yukawaSpan`**, a lemma, [line 864](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L864).

> The line through a conjugate down-type Yukawa term lies in the Yukawa span.

```lean
lemma span_barDownYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ LocalCovFieldAlgebra.barDownYukawa f f' ≤ LocalCovFieldAlgebra.yukawaSpan
```

**`StandardModel.LocalCovFieldAlgebra.span_barUpYukawa_le_yukawaSpan`**, a lemma, [line 871](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L871).

> The line through a conjugate up-type Yukawa term lies in the Yukawa span.

```lean
lemma span_barUpYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ LocalCovFieldAlgebra.barUpYukawa f f' ≤ LocalCovFieldAlgebra.yukawaSpan
```

**`StandardModel.LocalCovFieldAlgebra.span_barLeptonYukawa_le_yukawaSpan`**, a lemma, [line 878](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L878).

> The line through a conjugate charged-lepton Yukawa term lies in the Yukawa span.

```lean
lemma span_barLeptonYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ LocalCovFieldAlgebra.barLeptonYukawa f f' ≤ LocalCovFieldAlgebra.yukawaSpan
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_yukawaSpan`**, a lemma, [line 887](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L887).

> The join of the six block submodules over the nine family pairs reduces to the Yukawa
> span. The fifty-four blocks are taken one at a time, each in turn joining the error term
> of the others, which is what their stability is for.

```lean
lemma reducesInvariantsTo_yukawaSpan :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI
      repLorentzGroup) LocalCovFieldAlgebra.blockSubmodule
      LocalCovFieldAlgebra.yukawaSpan
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight_higgs_fermion_eight`**, a lemma, [line 942](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L942).

> The Yukawa sector at mass weight eight reduces, for the gauge and Lorentz groups
> together, to the Yukawa span. Hypercharge puts an invariant in the weight-zero piece, the
> piece lies in the six block submodules, and colour, isospin and Lorentz reduce each block
> to its Yukawa term.

```lean
lemma reducesInvariantsTo_sectorMassWeight_higgs_fermion_eight :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI
      repLorentzGroup)
      (fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8)
        LocalCovFieldAlgebra.yukawaSpan
```

**`StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_higgs_fermion_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 958](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean#L958).

> The classification of the Yukawa sector at mass weight eight as an equivalence. An
> element of the sector joined with a submodule `S` stable under both groups is fixed by
> both groups exactly when it is a combination of the six Yukawa couplings over the nine
> family pairs up to a remainder in `S` fixed by both groups.

```lean
lemma mem_sectorMassWeight_higgs_fermion_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g
      y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} 8 ⊔ S
        ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ LocalCovFieldAlgebra.yukawaSpan
```

## Depends on

- [The Yukawa terms built on the conjugate Higgs symbol](localfieldalgebra-yukawasector-families-barhiggs.md)
- [The gauge weight decomposition of the Yukawa sector at mass weight eight](localfieldalgebra-yukawasector-gaugeweight.md)

## Proof depends on

- [Finite linear combinations under a linear map](../../../mathematics/part-01/linearcombination.md)
- [Invariant reduction for the Standard Model gauge group](../part-02/localfieldalgebra-invariantreduction.md)
- [The metrics are the unique invariant tensors with two indices of one colour](../../../relativity/tensors/complextensor-metrics-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/YukawaSector/MassDimEight.lean)
