---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.higgsSubmodule_zero_le, StandardModel.CovAlgebraRealization.barHiggsSubmodule_zero_le, StandardModel.CovAlgebraRealization.range_d_eq, StandardModel.CovAlgebraRealization.range_bard_eq, StandardModel.CovAlgebraRealization.range_u_eq, StandardModel.CovAlgebraRealization.range_baru_eq, StandardModel.CovAlgebraRealization.range_Q_eq, StandardModel.CovAlgebraRealization.range_barQ_eq
statement: formalized
proof: formalized
---

# The Yukawa sector at mass weight eight

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.YukawaSector.MassDimEight`, [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean): 54 declarations, 54 with a docstring.

## i. Overview

> This is the theorem the Yukawa sector exists for.  At mass weight eight the sector is one
> Higgs tower against two underived fermion towers, and the claim proved here is that its
> gauge- and Lorentz-invariant content, modulo a submodule `S` stable under both groups, is
> exactly the span of the six Yukawa couplings over the nine family pairs.  Nothing else
> survives: no fourth coupling, no extra colour or isospin structure inside a surviving
> block, no invariant carrying a free spinor index.
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
> `ReducesInvariantsTo σ V W`: a `σ`-invariant of `V ⊔ S` lies in `W ⊔ S` whenever `S` is
> `σ`-stable. That relation composes — it is transitive, antitone in its source, monotone in its
> target, and closed under joins of stable sources — and each `GaugeGroup` or `LorentzGroup`
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

**`StandardModel.CovAlgebraRealization.higgsSubmodule_zero_le`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L85).

> The Higgs submodule without derivatives lies in the span of the Higgs components.

```lean
lemma higgsSubmodule_zero_le :
    h.isHiggsSector.higgsSubmodule 0
      ≤ Submodule.span ℂ (Set.range (h.isHiggsSector.higgs ![]))
```

**`StandardModel.CovAlgebraRealization.barHiggsSubmodule_zero_le`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L96).

> The conjugate Higgs submodule without derivatives lies in the span of the conjugate
> Higgs components.

```lean
lemma barHiggsSubmodule_zero_le :
    h.isHiggsSector.barHiggsSubmodule 0
      ≤ Submodule.span ℂ (Set.range (h.isHiggsSector.barHiggs ![]))
```

**`StandardModel.CovAlgebraRealization.range_d_eq`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L106).

> The range of the down-singlet symbol map is the span of its components.

```lean
lemma range_d_eq (f : Fin 3) :
    LinearMap.range (h.covD f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.dComponent f ![]))
```

**`StandardModel.CovAlgebraRealization.range_bard_eq`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L112).

> The range of the conjugate down-singlet symbol map is the span of its components.

```lean
lemma range_bard_eq (f : Fin 3) :
    LinearMap.range (h.covBarD f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.bardComponent f ![]))
```

**`StandardModel.CovAlgebraRealization.range_u_eq`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L118).

> The range of the up-singlet symbol map is the span of its components.

```lean
lemma range_u_eq (f : Fin 3) :
    LinearMap.range (h.covU f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.uComponent f ![]))
```

**`StandardModel.CovAlgebraRealization.range_baru_eq`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L124).

> The range of the conjugate up-singlet symbol map is the span of its components.

```lean
lemma range_baru_eq (f : Fin 3) :
    LinearMap.range (h.covBarU f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.baruComponent f ![]))
```

**`StandardModel.CovAlgebraRealization.range_Q_eq`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L130).

> The range of the quark-doublet symbol map is the span of its components.

```lean
lemma range_Q_eq (f : Fin 3) :
    LinearMap.range (h.covQ f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.QComponent f ![]))
```

**`StandardModel.CovAlgebraRealization.range_barQ_eq`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L136).

> The range of the conjugate quark-doublet symbol map is the span of its components.

```lean
lemma range_barQ_eq (f : Fin 3) :
    LinearMap.range (h.covBarQ f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.barQComponent f ![]))
```

**`StandardModel.CovAlgebraRealization.range_L_eq`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L142).

> The range of the lepton-doublet symbol map is the span of its components.

```lean
lemma range_L_eq (f : Fin 3) :
    LinearMap.range (h.covL f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.LComponent f ![]))
```

**`StandardModel.CovAlgebraRealization.range_barL_eq`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L148).

> The range of the conjugate lepton-doublet symbol map is the span of its components.

```lean
lemma range_barL_eq (f : Fin 3) :
    LinearMap.range (h.covBarL f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.barLComponent f ![]))
```

**`StandardModel.CovAlgebraRealization.range_e_eq`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L154).

> The range of the lepton-singlet symbol map is the span of its components.

```lean
lemma range_e_eq (f : Fin 3) :
    LinearMap.range (h.covE f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.eComponent f ![]))
```

**`StandardModel.CovAlgebraRealization.range_bare_eq`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L160).

> The range of the conjugate lepton-singlet symbol map is the span of its components.

```lean
lemma range_bare_eq (f : Fin 3) :
    LinearMap.range (h.covBarE f (![] : Fin 0 → Fin 1 ⊕ Fin 3))
      = Submodule.span ℂ (Set.range (h.isFermionSector.bareComponent f ![]))
```

## B. The block submodules and their stability

> A surviving block of the decomposition is the product of a Higgs range with two fermion
> ranges, and this is the submodule the classification of that block runs inside.  All six
> are carried into themselves by both groups, each factor being the range of an equivariant
> symbol map with no derivative slots for the Lorentz group to mix, and a product of stable
> submodules being stable.  That stability is what lets the six blocks — fifty-four of them
> once the family pairs are counted — be reduced one at a time, each in turn joining the
> error term of the others.

**`StandardModel.CovAlgebraRealization.isStableUnder_higgsSubmodule_zero`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L180).

> The Higgs submodule without derivatives is carried into itself by both groups.

```lean
lemma isStableUnder_higgsSubmodule_zero :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (h.isHiggsSector.higgsSubmodule 0)
```

**`StandardModel.CovAlgebraRealization.isStableUnder_barHiggsSubmodule_zero`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L190).

> The conjugate Higgs submodule without derivatives is carried into itself by both
> groups.

```lean
lemma isStableUnder_barHiggsSubmodule_zero :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (h.isHiggsSector.barHiggsSubmodule 0)
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_d`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L200).

> The range of the down-singlet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_d (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covD f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_bard`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L210).

> The range of the conjugate down-singlet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_bard (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covBarD f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_u`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L219).

> The range of the up-singlet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_u (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covU f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_baru`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L229).

> The range of the conjugate up-singlet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_baru (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covBarU f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_Q`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L238).

> The range of the quark-doublet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_Q (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covQ f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_barQ`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L248).

> The range of the conjugate quark-doublet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_barQ (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covBarQ f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_L`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L257).

> The range of the lepton-doublet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_L (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covL f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_barL`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L267).

> The range of the conjugate lepton-doublet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_barL (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covBarL f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_e`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L276).

> The range of the lepton-singlet symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_e (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covE f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.CovAlgebraRealization.isStableUnder_range_bare`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L286).

> The range of the conjugate lepton-singlet symbol map is carried into itself by both
> groups.

```lean
lemma isStableUnder_range_bare (f : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (h.covBarE f (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

## C. The twelve surviving blocks as six submodules

> The twelve blocks that hypercharge leaves come in six transposed pairs, and a pair is one
> submodule: the two fermion factors commute as submodules, by `mul_comm_of_le_derivSubmodule`,
> so exchanging them changes nothing.  Under the join over family pairs the transposed block
> of `(f, f')` is the untransposed block of `(f', f)`, and the weight-zero piece of the sector
> lands inside the join of the six.

**`StandardModel.CovAlgebraRealization.downBlockSubmodule`**, a def, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L306).

> The submodule of the down-type block `H d barQ` of a family pair.

```lean
noncomputable def downBlockSubmodule (f f' : Fin 3) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.upBlockSubmodule`**, a def, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L311).

> The submodule of the up-type block `H baru Q` of a family pair.

```lean
noncomputable def upBlockSubmodule (f f' : Fin 3) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.leptonBlockSubmodule`**, a def, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L316).

> The submodule of the charged-lepton block `H barL e` of a family pair.

```lean
noncomputable def leptonBlockSubmodule (f f' : Fin 3) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.barDownBlockSubmodule`**, a def, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L321).

> The submodule of the conjugate down-type block `barH bard Q` of a family pair.

```lean
noncomputable def barDownBlockSubmodule (f f' : Fin 3) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.barUpBlockSubmodule`**, a def, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L327).

> The submodule of the conjugate up-type block `barH u barQ` of a family pair.

```lean
noncomputable def barUpBlockSubmodule (f f' : Fin 3) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.barLeptonBlockSubmodule`**, a def, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L333).

> The submodule of the conjugate charged-lepton block `barH L bare` of a family pair.

```lean
noncomputable def barLeptonBlockSubmodule (f f' : Fin 3) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.isStableUnder_downBlockSubmodule`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L339).

> The down-type block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_downBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.downBlockSubmodule f f')
```

**`StandardModel.CovAlgebraRealization.isStableUnder_upBlockSubmodule`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L347).

> The up-type block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_upBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.upBlockSubmodule f f')
```

**`StandardModel.CovAlgebraRealization.isStableUnder_leptonBlockSubmodule`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L355).

> The charged-lepton block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_leptonBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.leptonBlockSubmodule f f')
```

**`StandardModel.CovAlgebraRealization.isStableUnder_barDownBlockSubmodule`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L363).

> The conjugate down-type block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barDownBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.barDownBlockSubmodule f f')
```

**`StandardModel.CovAlgebraRealization.isStableUnder_barUpBlockSubmodule`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L371).

> The conjugate up-type block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barUpBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.barUpBlockSubmodule f f')
```

**`StandardModel.CovAlgebraRealization.isStableUnder_barLeptonBlockSubmodule`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L379).

> The conjugate charged-lepton block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barLeptonBlockSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.barLeptonBlockSubmodule f f')
```

**`StandardModel.CovAlgebraRealization.blockSubmodule`**, a def, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L388).

> The join of the six block submodules over the nine family pairs: what the weight-zero
> piece of the Yukawa sector at mass weight eight is contained in.

```lean
noncomputable def blockSubmodule : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.sectorMassWeightEightGaugeWeight_piece_zero_le`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L399).

> The weight-zero piece of the Yukawa sector at mass weight eight lies in the join of the
> six block submodules over the nine family pairs. The twelve blocks of
> `sectorMassWeightEightGaugeWeight_piece_zero` become six because the two fermion factors
> of a block commute, so the transposed block of `(f, f')` is the block of `(f', f)`; and
> the weight refinement inside a block is dropped, hypercharge having already done its
> work and colour, isospin and Lorentz being what decide the rest.

```lean
lemma sectorMassWeightEightGaugeWeight_piece_zero_le :
    h.sectorMassWeightEightGaugeWeight.piece 0 ≤ h.blockSubmodule
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

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_downYukawa`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L467).

> The down-type block reduces to the down-type Yukawa term.

```lean
lemma reducesInvariantsTo_downYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.downBlockSubmodule f f')
      (ℂ ∙ h.downYukawa f f')
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_upYukawa`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L511).

> The up-type block reduces to the up-type Yukawa term. Isospin is contracted by the
> antisymmetric symbol here, the Higgs symbol and the quark doublet both carrying the
> anti-fundamental.

```lean
lemma reducesInvariantsTo_upYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.upBlockSubmodule f f')
      (ℂ ∙ h.upYukawa f f')
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_leptonYukawa`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L554).

> The charged-lepton block reduces to the charged-lepton Yukawa term. Its colour stage is
> the trivial one: the three symbols carry no colour index between them, so the block is
> fixed by the colour factor and the stage reduces it to itself.

```lean
lemma reducesInvariantsTo_leptonYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.leptonBlockSubmodule f f')
      (ℂ ∙ h.leptonYukawa f f')
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_barDownYukawa`**, a lemma, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L594).

> The conjugate down-type block reduces to the conjugate down-type Yukawa term.

```lean
lemma reducesInvariantsTo_barDownYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.barDownBlockSubmodule f f')
      (ℂ ∙ h.barDownYukawa f f')
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_barUpYukawa`**, a lemma, [line 636](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L636).

> The conjugate up-type block reduces to the conjugate up-type Yukawa term.

```lean
lemma reducesInvariantsTo_barUpYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.barUpBlockSubmodule f f')
      (ℂ ∙ h.barUpYukawa f f')
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_barLeptonYukawa`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L679).

> The conjugate charged-lepton block reduces to the conjugate charged-lepton Yukawa term,
> again with the trivial colour stage.

```lean
lemma reducesInvariantsTo_barLeptonYukawa (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.barLeptonBlockSubmodule f f')
      (ℂ ∙ h.barLeptonYukawa f f')
```

## E. The classification of the invariants of mass weight eight

> The two directions meet.  Forwards: the torus reduces the sector to its weight-zero piece,
> the piece lies in the six block submodules, and the blocks reduce to the Yukawa span.
> Backwards: `yukawaSpan_le_inf` says the Yukawa span is made of invariants of the right mass
> weight to begin with, which turns the reduction into an equivalence rather than a one-way
> inclusion.

**`StandardModel.CovAlgebraRealization.isFixedBy_yukawaSpan`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L733).

> The Yukawa span is fixed pointwise by both groups, `yukawaSpan_le_inf` placing it inside
> both spaces of invariants.

```lean
lemma isFixedBy_yukawaSpan : IsFixedBy (gaugeLorentzMaps repGauge repLorentz) h.yukawaSpan
```

**`StandardModel.CovAlgebraRealization.span_downYukawa_le_yukawaSpan`**, a lemma, [line 742](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L742).

> The line through a down-type Yukawa term lies in the Yukawa span.

```lean
lemma span_downYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ h.downYukawa f f' ≤ h.yukawaSpan
```

**`StandardModel.CovAlgebraRealization.span_upYukawa_le_yukawaSpan`**, a lemma, [line 750](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L750).

> The line through an up-type Yukawa term lies in the Yukawa span.

```lean
lemma span_upYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ h.upYukawa f f' ≤ h.yukawaSpan
```

**`StandardModel.CovAlgebraRealization.span_leptonYukawa_le_yukawaSpan`**, a lemma, [line 758](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L758).

> The line through a charged-lepton Yukawa term lies in the Yukawa span.

```lean
lemma span_leptonYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ h.leptonYukawa f f' ≤ h.yukawaSpan
```

**`StandardModel.CovAlgebraRealization.span_barDownYukawa_le_yukawaSpan`**, a lemma, [line 766](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L766).

> The line through a conjugate down-type Yukawa term lies in the Yukawa span.

```lean
lemma span_barDownYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ h.barDownYukawa f f' ≤ h.yukawaSpan
```

**`StandardModel.CovAlgebraRealization.span_barUpYukawa_le_yukawaSpan`**, a lemma, [line 773](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L773).

> The line through a conjugate up-type Yukawa term lies in the Yukawa span.

```lean
lemma span_barUpYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ h.barUpYukawa f f' ≤ h.yukawaSpan
```

**`StandardModel.CovAlgebraRealization.span_barLeptonYukawa_le_yukawaSpan`**, a lemma, [line 780](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L780).

> The line through a conjugate charged-lepton Yukawa term lies in the Yukawa span.

```lean
lemma span_barLeptonYukawa_le_yukawaSpan (f f' : Fin 3) :
    ℂ ∙ h.barLeptonYukawa f f' ≤ h.yukawaSpan
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_yukawaSpan`**, a lemma, [line 790](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L790).

> The join of the six block submodules over the nine family pairs reduces to the Yukawa
> span: the fifty-four blocks are taken one at a time, each in turn joining the error term
> of the others, which is what their stability is for.

```lean
lemma reducesInvariantsTo_yukawaSpan :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) h.blockSubmodule h.yukawaSpan
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight_higgs_fermion_eight`**, a lemma, [line 833](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L833).

> The Yukawa sector at mass weight eight reduces, for the gauge and Lorentz groups
> together, to the Yukawa span. Hypercharge puts an invariant in the weight-zero piece, the
> piece lies in the six block submodules, and colour, isospin and Lorentz reduce each block
> to its Yukawa term.

```lean
lemma reducesInvariantsTo_sectorMassWeight_higgs_fermion_eight :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz)
      (h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8) h.yukawaSpan
```

**`StandardModel.CovAlgebraRealization.mem_sectorMassWeight_higgs_fermion_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 845](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean#L845).

> The classification of the Yukawa sector at mass weight eight as an equivalence: an
> element of the sector joined with a submodule `S` stable under both groups is fixed by
> both groups exactly when it is a combination of the six Yukawa couplings over the nine
> family pairs up to a remainder in `S` fixed by both groups.

```lean
lemma mem_sectorMassWeight_higgs_fermion_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} 8 ⊔ S
        ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.yukawaSpan
```

## Depends on

- [The Yukawa terms built on the conjugate Higgs symbol](covrealization-yukawasector-families-barhiggs.md)
- [The gauge weight decomposition of the Yukawa sector at mass weight eight](covrealization-yukawasector-gaugeweight.md)
- [Invariant reduction for the gauge and Lorentz groups](../part-01/invariantreduction.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/YukawaSector/MassDimEight.lean)
