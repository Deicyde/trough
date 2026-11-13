---
declaration: module
origin: cited
lean: StandardModel.IsFermionSector.isStableUnder_iSup_range_deriv_one, StandardModel.IsFermionSector.isStableUnder_range_underived, StandardModel.IsFermionSector.isStableUnder_iSup_range_derived, StandardModel.IsFermionSector.dbardPairSubmodule, StandardModel.IsFermionSector.isStableUnder_dbardPairSubmodule, StandardModel.IsFermionSector.dbardPairSubmodule_le_blockSpan, StandardModel.IsFermionSector.reducesInvariantsTo_dbard, StandardModel.IsFermionSector.barddPairSubmodule
statement: formalized
proof: formalized
---

# The kinetic terms at mass weight eight

The module `PhyslibAlpha.Particles.StandardModel.IsFermionSector.MassWeight.MassDimEight`, [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean): 84 declarations, 84 with a docstring.

## i. Overview

> Mass weight eight is the first weight at which the fermion sector carries an invariant,
> and what it carries is the kinetic terms. The submodule is
> `derivSubmodule 0 * derivSubmodule 1`, one underived tower against one once-derived one,
> and the single derivative is exactly what mass weight six was missing: it supplies a
> four-vector index, and a four-vector index together with a dotted and an undotted spinor
> index has one invariant contraction, against the conjugate Pauli matrices. That
> contraction is `ψ̄ σ̄^μ ∂_μ ψ`.
>
> The classification runs the four stages every sector runs. Hypercharge first, through the
> gauge weight decomposition: `massWeightSubmoduleGaugeWeightEight_piece_zero` cuts the
> hundred pairings of two fermion symbols down to the ten conjugate ones, every other
> pairing having hypercharges that cannot cancel. Then colour, then isospin, then Lorentz,
> one classification each, chained by the `ReducesInvariantsTo` relation of
> `PhyslibAlpha.Mathematics.InvariantReduction` and supplied by the `KineticBlock` packages of
> `KineticTerms`. What is left is the kinetic span: one term for each of the ten pairings and each of
> the nine pairs of generations.

## ii. Key results

> - `isStableUnder_iSup_range_deriv_one` : the join, over the derivative direction, of the ranges of a
>   once-derived symbol map is carried into itself by the Lorentz group: a Lorentz transformation
>   mixes the derivative slot into the other directions and moves the covector, and both stay inside
>   the join
> - `isStableUnder_range_underived` : the range of an underived symbol map is carried into itself by
>   both groups
> - `isStableUnder_iSup_range_derived` : the join, over the derivative direction, of the ranges of a
>   once-derived symbol map is carried into itself by both groups
> - `dbardPairSubmodule` : the submodule of the `d ∂ bard` block of a generation pair: an underived
>   down-singlet range against the once-derived conjugate down-singlet ranges, joined over the
>   derivative direction

## iv. References

> * None.

## A. Symbol ranges and their stability

> The reduction asks two things of the submodule a block is read from: that the two groups
> carry it into itself, and that it lies in the span of the block's components. Both come
> from the symbol maps. A gauge transformation moves only the covector a symbol is evaluated
> at, so a symbol range is gauge stable at any number of derivative slots. The Lorentz group
> moves the covector too, but it also mixes the derivative slots, so an underived range is
> Lorentz stable on its own while a once-derived one is stable only after joining over the
> derivative direction — which is why a block submodule carries that join.

**`StandardModel.IsFermionSector.isStableUnder_iSup_range_deriv_one`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L112).

> The join, over the derivative direction, of the ranges of a once-derived symbol map is
> carried into itself by the Lorentz group: a Lorentz transformation mixes the derivative
> slot into the other directions and moves the covector, and both stay inside the join.

```lean
lemma isStableUnder_iSup_range_deriv_one {M : Type} [AddCommGroup M] [Module ℂ M]
    {ρ : Representation ℂ SL(2,ℂ) M}
    {F : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ M →ₗ[ℂ] B}
    (hF : IsLorentzCovDerivTransforms repLorentz ρ F) (Λ : SL(2,ℂ)) :
    ∀ y ∈ (⨆ μ : Fin 1 ⊕ Fin 3, LinearMap.range (F ![μ])),
      repLorentz Λ y ∈ ⨆ μ : Fin 1 ⊕ Fin 3, LinearMap.range (F ![μ])
```

**`StandardModel.IsFermionSector.isStableUnder_range_underived`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L130).

> The range of an underived symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_underived {M : Type} [AddCommGroup M] [Module ℂ M]
    {ρG : Representation ℂ GaugeGroupI M} {ρL : Representation ℂ SL(2,ℂ) M}
    {F : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ M →ₗ[ℂ] B}
    (hG : ∀ (g : GaugeGroupI) (φ : Module.Dual ℂ M),
      repGauge g (F (![] : Fin 0 → Fin 1 ⊕ Fin 3) φ)
        = F (![] : Fin 0 → Fin 1 ⊕ Fin 3) (ρG.dual g φ))
    (hL : IsLorentzCovDerivTransforms repLorentz ρL F) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (F (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.IsFermionSector.isStableUnder_iSup_range_derived`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L144).

> The join, over the derivative direction, of the ranges of a once-derived symbol map is
> carried into itself by both groups.

```lean
lemma isStableUnder_iSup_range_derived {M : Type} [AddCommGroup M] [Module ℂ M]
    {ρG : Representation ℂ GaugeGroupI M} {ρL : Representation ℂ SL(2,ℂ) M}
    {F : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ M →ₗ[ℂ] B}
    (hG : ∀ (g : GaugeGroupI) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℂ M),
      repGauge g (F ![μ] φ) = F ![μ] (ρG.dual g φ))
    (hL : IsLorentzCovDerivTransforms repLorentz ρL F) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (⨆ μ : Fin 1 ⊕ Fin 3, LinearMap.range (F ![μ]))
```

## B. The block submodules

> Each of the ten conjugate pairings gives one submodule per pair of generations: the
> underived range of one species against the once-derived ranges of its conjugate, joined
> over the derivative direction so that the Lorentz group has somewhere to move it. Each is
> carried into itself by both groups and lies in the span of the components of the matching
> kinetic block, which is all the reduction asks.

**`StandardModel.IsFermionSector.dbardPairSubmodule`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L173).

> The submodule of the `d ∂ bard` block of a generation pair: an underived
> down-singlet range against the once-derived conjugate down-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def dbardPairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_dbardPairSubmodule`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L181).

> The `d ∂ bard` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_dbardPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.dbardPairSubmodule f f')
```

**`StandardModel.IsFermionSector.dbardPairSubmodule_le_blockSpan`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L192).

> The `d ∂ bard` block submodule lies in the span of the block's components.

```lean
lemma dbardPairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.dbardPairSubmodule f f' ≤ (h.dbardKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_dbard`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L209).

> The `d ∂ bard` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_dbard (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.dbardPairSubmodule f f')
      (ℂ ∙ (h.dbardKineticBlock f f').kineticTerm)
```

**`StandardModel.IsFermionSector.barddPairSubmodule`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L220).

> The submodule of the `bard ∂ d` block of a generation pair: an underived
> conjugate down-singlet range against the once-derived down-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def barddPairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_barddPairSubmodule`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L228).

> The `bard ∂ d` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barddPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.barddPairSubmodule f f')
```

**`StandardModel.IsFermionSector.barddPairSubmodule_le_blockSpan`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L239).

> The `bard ∂ d` block submodule lies in the span of the block's components.

```lean
lemma barddPairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.barddPairSubmodule f f' ≤ (h.barddKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_bardd`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L257).

> The `bard ∂ d` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_bardd (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.barddPairSubmodule f f')
      (ℂ ∙ (h.barddKineticBlock f f').kineticTerm)
```

**`StandardModel.IsFermionSector.ubaruPairSubmodule`**, a def, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L268).

> The submodule of the `u ∂ baru` block of a generation pair: an underived
> up-singlet range against the once-derived conjugate up-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def ubaruPairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_ubaruPairSubmodule`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L276).

> The `u ∂ baru` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_ubaruPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.ubaruPairSubmodule f f')
```

**`StandardModel.IsFermionSector.ubaruPairSubmodule_le_blockSpan`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L287).

> The `u ∂ baru` block submodule lies in the span of the block's components.

```lean
lemma ubaruPairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.ubaruPairSubmodule f f' ≤ (h.ubaruKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_ubaru`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L304).

> The `u ∂ baru` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_ubaru (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.ubaruPairSubmodule f f')
      (ℂ ∙ (h.ubaruKineticBlock f f').kineticTerm)
```

**`StandardModel.IsFermionSector.baruuPairSubmodule`**, a def, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L315).

> The submodule of the `baru ∂ u` block of a generation pair: an underived
> conjugate up-singlet range against the once-derived up-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def baruuPairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_baruuPairSubmodule`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L323).

> The `baru ∂ u` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_baruuPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.baruuPairSubmodule f f')
```

**`StandardModel.IsFermionSector.baruuPairSubmodule_le_blockSpan`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L334).

> The `baru ∂ u` block submodule lies in the span of the block's components.

```lean
lemma baruuPairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.baruuPairSubmodule f f' ≤ (h.baruuKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_baruu`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L351).

> The `baru ∂ u` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_baruu (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.baruuPairSubmodule f f')
      (ℂ ∙ (h.baruuKineticBlock f f').kineticTerm)
```

**`StandardModel.IsFermionSector.QbarQPairSubmodule`**, a def, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L362).

> The submodule of the `Q ∂ barQ` block of a generation pair: an underived
> quark-doublet range against the once-derived conjugate quark-doublet ranges,
> joined over the derivative direction.

```lean
noncomputable def QbarQPairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_QbarQPairSubmodule`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L370).

> The `Q ∂ barQ` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_QbarQPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.QbarQPairSubmodule f f')
```

**`StandardModel.IsFermionSector.QbarQPairSubmodule_le_blockSpan`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L381).

> The `Q ∂ barQ` block submodule lies in the span of the block's components.

```lean
lemma QbarQPairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.QbarQPairSubmodule f f' ≤ (h.QbarQKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_QbarQ`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L399).

> The `Q ∂ barQ` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_QbarQ (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.QbarQPairSubmodule f f')
      (ℂ ∙ (h.QbarQKineticBlock f f').kineticTerm)
```

**`StandardModel.IsFermionSector.barQQPairSubmodule`**, a def, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L410).

> The submodule of the `barQ ∂ Q` block of a generation pair: an underived
> conjugate quark-doublet range against the once-derived quark-doublet ranges,
> joined over the derivative direction.

```lean
noncomputable def barQQPairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_barQQPairSubmodule`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L418).

> The `barQ ∂ Q` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barQQPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.barQQPairSubmodule f f')
```

**`StandardModel.IsFermionSector.barQQPairSubmodule_le_blockSpan`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L429).

> The `barQ ∂ Q` block submodule lies in the span of the block's components.

```lean
lemma barQQPairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.barQQPairSubmodule f f' ≤ (h.barQQKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_barQQ`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L447).

> The `barQ ∂ Q` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_barQQ (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.barQQPairSubmodule f f')
      (ℂ ∙ (h.barQQKineticBlock f f').kineticTerm)
```

**`StandardModel.IsFermionSector.LbarLPairSubmodule`**, a def, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L458).

> The submodule of the `L ∂ barL` block of a generation pair: an underived
> lepton-doublet range against the once-derived conjugate lepton-doublet ranges,
> joined over the derivative direction.

```lean
noncomputable def LbarLPairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_LbarLPairSubmodule`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L466).

> The `L ∂ barL` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_LbarLPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.LbarLPairSubmodule f f')
```

**`StandardModel.IsFermionSector.LbarLPairSubmodule_le_blockSpan`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L477).

> The `L ∂ barL` block submodule lies in the span of the block's components.

```lean
lemma LbarLPairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.LbarLPairSubmodule f f' ≤ (h.LbarLKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_LbarL`**, a lemma, [line 495](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L495).

> The `L ∂ barL` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_LbarL (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.LbarLPairSubmodule f f')
      (ℂ ∙ (h.LbarLKineticBlock f f').kineticTerm)
```

**`StandardModel.IsFermionSector.barLLPairSubmodule`**, a def, [line 506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L506).

> The submodule of the `barL ∂ L` block of a generation pair: an underived
> conjugate lepton-doublet range against the once-derived lepton-doublet ranges,
> joined over the derivative direction.

```lean
noncomputable def barLLPairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_barLLPairSubmodule`**, a lemma, [line 514](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L514).

> The `barL ∂ L` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barLLPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.barLLPairSubmodule f f')
```

**`StandardModel.IsFermionSector.barLLPairSubmodule_le_blockSpan`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L525).

> The `barL ∂ L` block submodule lies in the span of the block's components.

```lean
lemma barLLPairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.barLLPairSubmodule f f' ≤ (h.barLLKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_barLL`**, a lemma, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L543).

> The `barL ∂ L` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_barLL (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.barLLPairSubmodule f f')
      (ℂ ∙ (h.barLLKineticBlock f f').kineticTerm)
```

**`StandardModel.IsFermionSector.ebarePairSubmodule`**, a def, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L554).

> The submodule of the `e ∂ bare` block of a generation pair: an underived
> lepton-singlet range against the once-derived conjugate lepton-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def ebarePairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_ebarePairSubmodule`**, a lemma, [line 562](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L562).

> The `e ∂ bare` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_ebarePairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.ebarePairSubmodule f f')
```

**`StandardModel.IsFermionSector.ebarePairSubmodule_le_blockSpan`**, a lemma, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L573).

> The `e ∂ bare` block submodule lies in the span of the block's components.

```lean
lemma ebarePairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.ebarePairSubmodule f f' ≤ (h.ebareKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_ebare`**, a lemma, [line 591](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L591).

> The `e ∂ bare` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_ebare (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.ebarePairSubmodule f f')
      (ℂ ∙ (h.ebareKineticBlock f f').kineticTerm)
```

**`StandardModel.IsFermionSector.bareePairSubmodule`**, a def, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L602).

> The submodule of the `bare ∂ e` block of a generation pair: an underived
> conjugate lepton-singlet range against the once-derived lepton-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def bareePairSubmodule (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) (f f' : Fin 3) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.isStableUnder_bareePairSubmodule`**, a lemma, [line 610](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L610).

> The `bare ∂ e` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_bareePairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.bareePairSubmodule f f')
```

**`StandardModel.IsFermionSector.bareePairSubmodule_le_blockSpan`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L621).

> The `bare ∂ e` block submodule lies in the span of the block's components.

```lean
lemma bareePairSubmodule_le_blockSpan (f f' : Fin 3) :
    h.bareePairSubmodule f f' ≤ (h.bareeKineticBlock f f').blockSpan
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_baree`**, a lemma, [line 639](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L639).

> The `bare ∂ e` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_baree (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.bareePairSubmodule f f')
      (ℂ ∙ (h.bareeKineticBlock f f').kineticTerm)
```

## C. The symbol ranges inside the derivative submodules, and the mass weight

> An underived symbol range lies in `derivSubmodule 0` and a once-derived one in
> `derivSubmodule 1`, so every component of a kinetic block is a product of the two, which
> is `massWeightSubmodule 8`. Each stage of a block's classification stays inside the span
> of the stage before it, so the kinetic term is there too.

**`StandardModel.IsFermionSector.etaExpand_deriv_one`**, a lemma, [line 657](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L657).

> A family of one derivative direction is the tuple of its own entry.

```lean
lemma etaExpand_deriv_one (l : Fin 1 → Fin 1 ⊕ Fin 3) : ![l 0] = l
```

**`StandardModel.IsFermionSector.range_d_le_derivSubmodule`**, a lemma, [line 665](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L665).

> The range of the down-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_d_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (d f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.range_bard_le_derivSubmodule`**, a lemma, [line 676](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L676).

> The range of the conjugate down-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_bard_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bard f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.range_u_le_derivSubmodule`**, a lemma, [line 687](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L687).

> The range of the up-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_u_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (u f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.range_baru_le_derivSubmodule`**, a lemma, [line 698](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L698).

> The range of the conjugate up-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_baru_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (baru f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.range_Q_le_derivSubmodule`**, a lemma, [line 708](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L708).

> The range of the quark-doublet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_Q_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (Q f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.range_barQ_le_derivSubmodule`**, a lemma, [line 718](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L718).

> The range of the conjugate quark-doublet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_barQ_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barQ f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.range_L_le_derivSubmodule`**, a lemma, [line 728](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L728).

> The range of the lepton-doublet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_L_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (L f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.range_barL_le_derivSubmodule`**, a lemma, [line 737](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L737).

> The range of the conjugate lepton-doublet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_barL_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barL f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.range_e_le_derivSubmodule`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L746).

> The range of the lepton-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_e_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (e f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.range_bare_le_derivSubmodule`**, a lemma, [line 755](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L755).

> The range of the conjugate lepton-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_bare_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bare f l) ≤ h.derivSubmodule n
```

**`StandardModel.IsFermionSector.dbardKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 764](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L764).

> The kinetic term of the `d ∂ bard` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma dbardKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.dbardKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.barddKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 774](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L774).

> The kinetic term of the `bard ∂ d` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma barddKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.barddKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.ubaruKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 784](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L784).

> The kinetic term of the `u ∂ baru` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma ubaruKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.ubaruKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.baruuKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 794](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L794).

> The kinetic term of the `baru ∂ u` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma baruuKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.baruuKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.QbarQKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 804](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L804).

> The kinetic term of the `Q ∂ barQ` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma QbarQKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.QbarQKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.barQQKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 814](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L814).

> The kinetic term of the `barQ ∂ Q` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma barQQKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.barQQKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.LbarLKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 824](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L824).

> The kinetic term of the `L ∂ barL` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma LbarLKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.LbarLKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.barLLKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 834](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L834).

> The kinetic term of the `barL ∂ L` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma barLLKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.barLLKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.ebareKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 844](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L844).

> The kinetic term of the `e ∂ bare` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma ebareKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.ebareKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.bareeKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 854](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L854).

> The kinetic term of the `bare ∂ e` block has mass weight eight: every component of the
> block is an underived tower against a once-derived one.

```lean
lemma bareeKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (h.bareeKineticBlock f f').kineticTerm ∈ h.massWeightSubmodule 8
```

## D. The kinetic span

> The kinetic span of the fermion sector at mass weight eight: the join, over the ten
> conjugate pairings and the nine pairs of generations, of the lines through the kinetic
> terms. Each generator is a gauge and Lorentz invariant of mass weight eight, which is the
> easy direction of the classification and what makes it an equivalence rather than an
> inclusion.

**`StandardModel.IsFermionSector.kineticSpan`**, a def, [line 876](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L876).

> The kinetic span of the fermion sector at mass weight eight: the join of the ten
> conjugate pairings, each over the nine pairs of generations.

```lean
noncomputable def kineticSpan (h : IsFermionSector B repGauge hrepGauge_mul repLorentz
      hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) : Submodule ℂ B
```

**`StandardModel.IsFermionSector.span_dbard_le_kineticSpan`**, a lemma, [line 892](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L892).

> The line through the `dbard` kinetic term lies in the kinetic span.

```lean
lemma span_dbard_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.dbardKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.span_bardd_le_kineticSpan`**, a lemma, [line 902](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L902).

> The line through the `bardd` kinetic term lies in the kinetic span.

```lean
lemma span_bardd_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.barddKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.span_ubaru_le_kineticSpan`**, a lemma, [line 912](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L912).

> The line through the `ubaru` kinetic term lies in the kinetic span.

```lean
lemma span_ubaru_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.ubaruKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.span_baruu_le_kineticSpan`**, a lemma, [line 921](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L921).

> The line through the `baruu` kinetic term lies in the kinetic span.

```lean
lemma span_baruu_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.baruuKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.span_QbarQ_le_kineticSpan`**, a lemma, [line 930](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L930).

> The line through the `QbarQ` kinetic term lies in the kinetic span.

```lean
lemma span_QbarQ_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.QbarQKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.span_barQQ_le_kineticSpan`**, a lemma, [line 939](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L939).

> The line through the `barQQ` kinetic term lies in the kinetic span.

```lean
lemma span_barQQ_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.barQQKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.span_LbarL_le_kineticSpan`**, a lemma, [line 948](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L948).

> The line through the `LbarL` kinetic term lies in the kinetic span.

```lean
lemma span_LbarL_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.LbarLKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.span_barLL_le_kineticSpan`**, a lemma, [line 956](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L956).

> The line through the `barLL` kinetic term lies in the kinetic span.

```lean
lemma span_barLL_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.barLLKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.span_ebare_le_kineticSpan`**, a lemma, [line 964](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L964).

> The line through the `ebare` kinetic term lies in the kinetic span.

```lean
lemma span_ebare_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.ebareKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.span_baree_le_kineticSpan`**, a lemma, [line 972](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L972).

> The line through the `baree` kinetic term lies in the kinetic span.

```lean
lemma span_baree_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (h.bareeKineticBlock f f').kineticTerm ≤ h.kineticSpan
```

**`StandardModel.IsFermionSector.isFixedBy_kineticSpan`**, a lemma, [line 981](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L981).

> The kinetic span is fixed pointwise by both groups, each of its generators being a
> gauge and Lorentz invariant.

```lean
lemma isFixedBy_kineticSpan :
    IsFixedBy (gaugeLorentzMaps repGauge repLorentz) h.kineticSpan
```

**`StandardModel.IsFermionSector.kineticSpan_le_massWeightSubmodule`**, a lemma, [line 1027](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L1027).

> The kinetic span lies at mass weight eight.

```lean
lemma kineticSpan_le_massWeightSubmodule : h.kineticSpan ≤ h.massWeightSubmodule 8
```

**`StandardModel.IsFermionSector.kineticSpan_le_invariants`**, a lemma, [line 1055](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L1055).

> The kinetic span is a space of gauge invariants.

```lean
lemma kineticSpan_le_invariants : h.kineticSpan ≤ repGauge.invariants
```

**`StandardModel.IsFermionSector.kineticSpan_le_lorentzInvariants`**, a lemma, [line 1093](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L1093).

> The kinetic span is a space of Lorentz invariants.

```lean
lemma kineticSpan_le_lorentzInvariants : h.kineticSpan ≤ repLorentz.invariants
```

## E. The blocks reduce to the kinetic terms

> The weight-zero piece of the gauge weight decomposition lies in the join of the ten block
> submodules, hypercharge having already cut the hundred pairings down to ten; and each
> block reduces to its kinetic term, by the three stages its `KineticBlock` package supplies.
> Joining the ten and then the nine generation pairs is `ReducesInvariantsTo.sup` and
> `ReducesInvariantsTo.iSup`, which is where the stability of the blocks and of the kinetic span is
> spent.

**`StandardModel.IsFermionSector.kineticBlockSubmodule`**, a def, [line 1144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L1144).

> The join of the ten block submodules over the nine pairs of generations.

```lean
noncomputable def kineticBlockSubmodule (h : IsFermionSector B repGauge hrepGauge_mul
      repLorentz hrepLorentz_mul d bard u baru Q barQ L barL e bare massWeightPoly) :
    Submodule ℂ B
```

**`StandardModel.IsFermionSector.massWeightSubmoduleGaugeWeightEight_piece_zero_le`**, a lemma, [line 1164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L1164).

> The weight-zero piece at mass weight eight lies in the join of the ten block
> submodules: each of the ten conjugate pairings of
> `massWeightSubmoduleGaugeWeightEight_piece_zero` is an underived range against a
> once-derived one, and the derivative direction is joined over.

```lean
lemma massWeightSubmoduleGaugeWeightEight_piece_zero_le :
    (h.massWeightSubmoduleGaugeWeightEight).piece 0 ≤ h.kineticBlockSubmodule
```

**`StandardModel.IsFermionSector.reducesInvariantsTo_kineticBlockSubmodule`**, a lemma, [line 1233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L1233).

> The join of the ten block submodules reduces to the kinetic span.

```lean
lemma reducesInvariantsTo_kineticBlockSubmodule :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) h.kineticBlockSubmodule
      h.kineticSpan
```

## F. The classification as an equivalence

> The two directions meet. Forwards: hypercharge puts a gauge invariant in the weight-zero
> piece (`GaugeWeightDecomposition.reducesInvariantsTo_piece_zero`), and section E reduces
> that to the kinetic span. Backwards: the kinetic span is a space of gauge and Lorentz
> invariants of mass weight eight (section D), which turns the reduction into an equivalence.
>
> So the fermion sector at mass weight eight carries exactly the kinetic terms — one for
> each species, each pair of generations and each placement of the derivative — and nothing
> else. Compare mass weight six, where the same argument leaves nothing at all: without a
> derivative there is no four-vector index for the conjugate Pauli matrices to carry, and
> the Dirac mass term does not exist.

**`StandardModel.IsFermionSector.reducesInvariantsTo_kineticSpan`**, a lemma, [line 1334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L1334).

> The fermion sector at mass weight eight reduces, for the gauge and Lorentz groups
> together, to the kinetic span: the torus puts an invariant in the weight-zero piece, which
> lies in the ten block submodules, and those reduce to the kinetic terms.

```lean
lemma reducesInvariantsTo_kineticSpan :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.massWeightSubmodule 8)
      h.kineticSpan
```

**`StandardModel.IsFermionSector.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 1347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean#L1347).

> The classification of mass weight eight as an equivalence, in the shape of the
> sibling sectors: an element of `massWeightSubmodule 8 ⊔ S` is fixed by both groups
> exactly when it is a combination of the kinetic terms up to a remainder in `S` fixed by
> both groups.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.kineticSpan
```

## Depends on

- [The ten kinetic blocks](isfermionsector-massweight-kineticterms.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/MassDimEight.lean)
