---
declaration: module
origin: cited
lean: StandardModel.FermionSector.isStableUnder_iSup_range_deriv_one, StandardModel.FermionSector.isStableUnder_range_underived, StandardModel.FermionSector.isStableUnder_iSup_range_derived, StandardModel.FermionSector.dbardPairSubmodule, StandardModel.FermionSector.isStableUnder_dbardPairSubmodule, StandardModel.FermionSector.dbardPairSubmodule_le_blockSpan, StandardModel.FermionSector.reducesInvariantsTo_dbard, StandardModel.FermionSector.barddPairSubmodule
statement: formalized
proof: formalized
---

# The kinetic terms at mass weight eight

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionSector.MassWeight.MassDimEight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean): 84 declarations, 84 with a docstring.

> The gauge and Lorentz invariants of the fermion sector at mass weight eight, the kinetic terms.

## i. Overview

> Mass weight eight is the first weight at which the fermion sector carries an invariant,
> and what it carries is the kinetic terms. The submodule is
> `derivSubmodule 0 * derivSubmodule 1`, one underived tower against one once-derived one,
> and the single derivative is exactly what mass weight six was missing. It supplies a
> four-vector index, and a four-vector index together with a dotted and an undotted spinor
> index has one invariant contraction, against the conjugate Pauli matrices. That
> contraction is `ψ̄ σ̄^μ ∂_μ ψ`.
>
> The classification runs the four stages every sector runs. Hypercharge first, through the
> gauge weight decomposition, where `massWeightSubmoduleGaugeWeightEight_piece_zero` cuts the
> hundred pairings of two fermion symbols down to the ten conjugate ones, every other
> pairing having hypercharges that cannot cancel. Then colour, then isospin, then Lorentz,
> one classification each, chained by the `ReducesInvariantsTo` relation of
> `PhyslibAlpha.Mathematics.InvariantReduction` and supplied by the `KineticBlock` packages of
> `KineticTerms`. What is left is the kinetic span: one term for each of the ten pairings and each of
> the nine pairs of generations.

## ii. Key results

> - `dbardPairSubmodule` and its nine companions : the submodule of each block of a generation pair.
> - `kineticSpan` : the join of the kinetic terms over the ten conjugate pairings and the nine
>   pairs of generations.
> - `reducesInvariantsTo_kineticSpan` : the fermion sector at mass weight eight reduces to the
>   kinetic span.
> - `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff` : the classification at mass
>   weight eight as an equivalence.

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

**`StandardModel.FermionSector.isStableUnder_iSup_range_deriv_one`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L84).

> The join, over the derivative direction, of the ranges of a once-derived symbol map is
> carried into itself by the Lorentz group. A Lorentz transformation mixes the derivative
> slot into the other directions and moves the covector, and both stay inside the join.

```lean
lemma isStableUnder_iSup_range_deriv_one {M : Type} [AddCommGroup M] [Module ℂ M]
    {ρ : Representation ℂ SL(2,ℂ) M}
    {F : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ M →ₗ[ℂ] fieldData.LocalCovFieldAlgebra}
    (hF : IsLorentzCovDerivTransforms repLorentz ρ F) (Λ : SL(2,ℂ)) :
    ∀ y ∈ (⨆ μ : Fin 1 ⊕ Fin 3, LinearMap.range (F ![μ])),
      repLorentz Λ y ∈ ⨆ μ : Fin 1 ⊕ Fin 3, LinearMap.range (F ![μ])
```

**`StandardModel.FermionSector.isStableUnder_range_underived`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L102).

> The range of an underived symbol map is carried into itself by both groups.

```lean
lemma isStableUnder_range_underived {M : Type} [AddCommGroup M] [Module ℂ M]
    {ρG : Representation ℂ GaugeGroupI M} {ρL : Representation ℂ SL(2,ℂ) M}
    {F : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ M →ₗ[ℂ] fieldData.LocalCovFieldAlgebra}
    (hG : ∀ (g : GaugeGroupI) (φ : Module.Dual ℂ M),
      repGauge g (F (![] : Fin 0 → Fin 1 ⊕ Fin 3) φ)
        = F (![] : Fin 0 → Fin 1 ⊕ Fin 3) (ρG.dual g φ))
    (hL : IsLorentzCovDerivTransforms repLorentz ρL F) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz)
      (LinearMap.range (F (![] : Fin 0 → Fin 1 ⊕ Fin 3)))
```

**`StandardModel.FermionSector.isStableUnder_iSup_range_derived`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L116).

> The join, over the derivative direction, of the ranges of a once-derived symbol map is
> carried into itself by both groups.

```lean
lemma isStableUnder_iSup_range_derived {M : Type} [AddCommGroup M] [Module ℂ M]
    {ρG : Representation ℂ GaugeGroupI M} {ρL : Representation ℂ SL(2,ℂ) M}
    {F : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ M →ₗ[ℂ] fieldData.LocalCovFieldAlgebra}
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

**`StandardModel.FermionSector.dbardPairSubmodule`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L143).

> The submodule of the `d ∂ bard` block of a generation pair, an underived
> down-singlet range against the once-derived conjugate down-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def dbardPairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_dbardPairSubmodule`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L149).

> The `d ∂ bard` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_dbardPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (dbardPairSubmodule f f')
```

**`StandardModel.FermionSector.dbardPairSubmodule_le_blockSpan`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L159).

> The `d ∂ bard` block submodule lies in the span of the block's components.

```lean
lemma dbardPairSubmodule_le_blockSpan (f f' : Fin 3) :
    dbardPairSubmodule f f' ≤ (dbardKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_dbard`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L177).

> The `d ∂ bard` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_dbard (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (dbardPairSubmodule f f')
      (ℂ ∙ (dbardKineticBlock f f').kineticTerm)
```

**`StandardModel.FermionSector.barddPairSubmodule`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L186).

> The submodule of the `bard ∂ d` block of a generation pair, an underived
> conjugate down-singlet range against the once-derived down-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def barddPairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_barddPairSubmodule`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L192).

> The `bard ∂ d` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barddPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (barddPairSubmodule f f')
```

**`StandardModel.FermionSector.barddPairSubmodule_le_blockSpan`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L202).

> The `bard ∂ d` block submodule lies in the span of the block's components.

```lean
lemma barddPairSubmodule_le_blockSpan (f f' : Fin 3) :
    barddPairSubmodule f f' ≤ (barddKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_bardd`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L219).

> The `bard ∂ d` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_bardd (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (barddPairSubmodule f f')
      (ℂ ∙ (barddKineticBlock f f').kineticTerm)
```

**`StandardModel.FermionSector.ubaruPairSubmodule`**, a def, [line 228](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L228).

> The submodule of the `u ∂ baru` block of a generation pair, an underived
> up-singlet range against the once-derived conjugate up-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def ubaruPairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_ubaruPairSubmodule`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L234).

> The `u ∂ baru` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_ubaruPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (ubaruPairSubmodule f f')
```

**`StandardModel.FermionSector.ubaruPairSubmodule_le_blockSpan`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L244).

> The `u ∂ baru` block submodule lies in the span of the block's components.

```lean
lemma ubaruPairSubmodule_le_blockSpan (f f' : Fin 3) :
    ubaruPairSubmodule f f' ≤ (ubaruKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_ubaru`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L262).

> The `u ∂ baru` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_ubaru (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (ubaruPairSubmodule f f')
      (ℂ ∙ (ubaruKineticBlock f f').kineticTerm)
```

**`StandardModel.FermionSector.baruuPairSubmodule`**, a def, [line 271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L271).

> The submodule of the `baru ∂ u` block of a generation pair, an underived
> conjugate up-singlet range against the once-derived up-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def baruuPairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_baruuPairSubmodule`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L277).

> The `baru ∂ u` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_baruuPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (baruuPairSubmodule f f')
```

**`StandardModel.FermionSector.baruuPairSubmodule_le_blockSpan`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L287).

> The `baru ∂ u` block submodule lies in the span of the block's components.

```lean
lemma baruuPairSubmodule_le_blockSpan (f f' : Fin 3) :
    baruuPairSubmodule f f' ≤ (baruuKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_baruu`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L303).

> The `baru ∂ u` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_baruu (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (baruuPairSubmodule f f')
      (ℂ ∙ (baruuKineticBlock f f').kineticTerm)
```

**`StandardModel.FermionSector.QbarQPairSubmodule`**, a def, [line 312](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L312).

> The submodule of the `Q ∂ barQ` block of a generation pair, an underived
> quark-doublet range against the once-derived conjugate quark-doublet ranges,
> joined over the derivative direction.

```lean
noncomputable def QbarQPairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_QbarQPairSubmodule`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L318).

> The `Q ∂ barQ` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_QbarQPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (QbarQPairSubmodule f f')
```

**`StandardModel.FermionSector.QbarQPairSubmodule_le_blockSpan`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L328).

> The `Q ∂ barQ` block submodule lies in the span of the block's components.

```lean
lemma QbarQPairSubmodule_le_blockSpan (f f' : Fin 3) :
    QbarQPairSubmodule f f' ≤ (QbarQKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_QbarQ`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L347).

> The `Q ∂ barQ` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_QbarQ (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (QbarQPairSubmodule f f')
      (ℂ ∙ (QbarQKineticBlock f f').kineticTerm)
```

**`StandardModel.FermionSector.barQQPairSubmodule`**, a def, [line 356](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L356).

> The submodule of the `barQ ∂ Q` block of a generation pair, an underived
> conjugate quark-doublet range against the once-derived quark-doublet ranges,
> joined over the derivative direction.

```lean
noncomputable def barQQPairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_barQQPairSubmodule`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L362).

> The `barQ ∂ Q` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barQQPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (barQQPairSubmodule f f')
```

**`StandardModel.FermionSector.barQQPairSubmodule_le_blockSpan`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L372).

> The `barQ ∂ Q` block submodule lies in the span of the block's components.

```lean
lemma barQQPairSubmodule_le_blockSpan (f f' : Fin 3) :
    barQQPairSubmodule f f' ≤ (barQQKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_barQQ`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L391).

> The `barQ ∂ Q` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_barQQ (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (barQQPairSubmodule f f')
      (ℂ ∙ (barQQKineticBlock f f').kineticTerm)
```

**`StandardModel.FermionSector.LbarLPairSubmodule`**, a def, [line 400](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L400).

> The submodule of the `L ∂ barL` block of a generation pair, an underived
> lepton-doublet range against the once-derived conjugate lepton-doublet ranges,
> joined over the derivative direction.

```lean
noncomputable def LbarLPairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_LbarLPairSubmodule`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L406).

> The `L ∂ barL` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_LbarLPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (LbarLPairSubmodule f f')
```

**`StandardModel.FermionSector.LbarLPairSubmodule_le_blockSpan`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L416).

> The `L ∂ barL` block submodule lies in the span of the block's components.

```lean
lemma LbarLPairSubmodule_le_blockSpan (f f' : Fin 3) :
    LbarLPairSubmodule f f' ≤ (LbarLKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_LbarL`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L435).

> The `L ∂ barL` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_LbarL (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (LbarLPairSubmodule f f')
      (ℂ ∙ (LbarLKineticBlock f f').kineticTerm)
```

**`StandardModel.FermionSector.barLLPairSubmodule`**, a def, [line 444](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L444).

> The submodule of the `barL ∂ L` block of a generation pair, an underived
> conjugate lepton-doublet range against the once-derived lepton-doublet ranges,
> joined over the derivative direction.

```lean
noncomputable def barLLPairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_barLLPairSubmodule`**, a lemma, [line 450](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L450).

> The `barL ∂ L` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_barLLPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (barLLPairSubmodule f f')
```

**`StandardModel.FermionSector.barLLPairSubmodule_le_blockSpan`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L460).

> The `barL ∂ L` block submodule lies in the span of the block's components.

```lean
lemma barLLPairSubmodule_le_blockSpan (f f' : Fin 3) :
    barLLPairSubmodule f f' ≤ (barLLKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_barLL`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L479).

> The `barL ∂ L` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_barLL (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (barLLPairSubmodule f f')
      (ℂ ∙ (barLLKineticBlock f f').kineticTerm)
```

**`StandardModel.FermionSector.ebarePairSubmodule`**, a def, [line 488](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L488).

> The submodule of the `e ∂ bare` block of a generation pair, an underived
> lepton-singlet range against the once-derived conjugate lepton-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def ebarePairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_ebarePairSubmodule`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L494).

> The `e ∂ bare` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_ebarePairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (ebarePairSubmodule f f')
```

**`StandardModel.FermionSector.ebarePairSubmodule_le_blockSpan`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L504).

> The `e ∂ bare` block submodule lies in the span of the block's components.

```lean
lemma ebarePairSubmodule_le_blockSpan (f f' : Fin 3) :
    ebarePairSubmodule f f' ≤ (ebareKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_ebare`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L521).

> The `e ∂ bare` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_ebare (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (ebarePairSubmodule f f')
      (ℂ ∙ (ebareKineticBlock f f').kineticTerm)
```

**`StandardModel.FermionSector.bareePairSubmodule`**, a def, [line 530](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L530).

> The submodule of the `bare ∂ e` block of a generation pair, an underived
> conjugate lepton-singlet range against the once-derived lepton-singlet ranges,
> joined over the derivative direction.

```lean
noncomputable def bareePairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_bareePairSubmodule`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L536).

> The `bare ∂ e` block submodule is carried into itself by both groups.

```lean
lemma isStableUnder_bareePairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (bareePairSubmodule f f')
```

**`StandardModel.FermionSector.bareePairSubmodule_le_blockSpan`**, a lemma, [line 546](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L546).

> The `bare ∂ e` block submodule lies in the span of the block's components.

```lean
lemma bareePairSubmodule_le_blockSpan (f f' : Fin 3) :
    bareePairSubmodule f f' ≤ (bareeKineticBlock f f').blockSpan
```

**`StandardModel.FermionSector.reducesInvariantsTo_baree`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L563).

> The `bare ∂ e` block reduces to its kinetic term.

```lean
lemma reducesInvariantsTo_baree (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (bareePairSubmodule f f')
      (ℂ ∙ (bareeKineticBlock f f').kineticTerm)
```

## C. The symbol ranges inside the derivative submodules, and the mass weight

> An underived symbol range lies in `derivSubmodule 0` and a once-derived one in
> `derivSubmodule 1`, so every component of a kinetic block is a product of the two, which
> is `massWeightSubmodule 8`. Each stage of a block's classification stays inside the span
> of the stage before it, so the kinetic term is there too.

**`StandardModel.FermionSector.range_d_le_derivSubmodule`**, a lemma, [line 582](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L582).

> The range of the down-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_d_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (d f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.range_bard_le_derivSubmodule`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L592).

> The range of the conjugate down-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_bard_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bard f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.range_u_le_derivSubmodule`**, a lemma, [line 602](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L602).

> The range of the up-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_u_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (u f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.range_baru_le_derivSubmodule`**, a lemma, [line 612](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L612).

> The range of the conjugate up-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_baru_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (baru f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.range_Q_le_derivSubmodule`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L621).

> The range of the quark-doublet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_Q_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (Q f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.range_barQ_le_derivSubmodule`**, a lemma, [line 630](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L630).

> The range of the conjugate quark-doublet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_barQ_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barQ f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.range_L_le_derivSubmodule`**, a lemma, [line 639](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L639).

> The range of the lepton-doublet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_L_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (L f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.range_barL_le_derivSubmodule`**, a lemma, [line 647](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L647).

> The range of the conjugate lepton-doublet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_barL_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (barL f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.range_e_le_derivSubmodule`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L655).

> The range of the lepton-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_e_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (e f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.range_bare_le_derivSubmodule`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L663).

> The range of the conjugate lepton-singlet symbols lies in the derivative
> submodule of its slots.

```lean
lemma range_bare_le_derivSubmodule {n : ℕ} (f : Fin 3) (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (bare f l) ≤ derivSubmodule n
```

**`StandardModel.FermionSector.dbardKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 671](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L671).

> The kinetic term of the `d ∂ bard` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma dbardKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (dbardKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

**`StandardModel.FermionSector.barddKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 680](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L680).

> The kinetic term of the `bard ∂ d` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma barddKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (barddKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

**`StandardModel.FermionSector.ubaruKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 689](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L689).

> The kinetic term of the `u ∂ baru` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma ubaruKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (ubaruKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

**`StandardModel.FermionSector.baruuKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 698](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L698).

> The kinetic term of the `baru ∂ u` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma baruuKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (baruuKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

**`StandardModel.FermionSector.QbarQKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 707](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L707).

> The kinetic term of the `Q ∂ barQ` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma QbarQKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (QbarQKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

**`StandardModel.FermionSector.barQQKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L716).

> The kinetic term of the `barQ ∂ Q` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma barQQKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (barQQKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

**`StandardModel.FermionSector.LbarLKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 725](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L725).

> The kinetic term of the `L ∂ barL` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma LbarLKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (LbarLKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

**`StandardModel.FermionSector.barLLKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 734](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L734).

> The kinetic term of the `barL ∂ L` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma barLLKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (barLLKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

**`StandardModel.FermionSector.ebareKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 743](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L743).

> The kinetic term of the `e ∂ bare` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma ebareKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (ebareKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

**`StandardModel.FermionSector.bareeKineticTerm_mem_massWeightSubmodule`**, a lemma, [line 752](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L752).

> The kinetic term of the `bare ∂ e` block has mass weight eight, since every component of the
> block is an underived tower against a once-derived one.

```lean
lemma bareeKineticTerm_mem_massWeightSubmodule (f f' : Fin 3) :
    (bareeKineticBlock f f').kineticTerm ∈ massWeightSubmodule 8
```

## D. The kinetic span

> The kinetic span of the fermion sector at mass weight eight is the join, over the ten
> conjugate pairings and the nine pairs of generations, of the lines through the kinetic
> terms. Each generator is a gauge and Lorentz invariant of mass weight eight, which is the
> easy direction of the classification and what makes it an equivalence rather than an
> inclusion.

**`StandardModel.FermionSector.kineticSpan`**, a def, [line 773](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L773).

> The kinetic span of the fermion sector at mass weight eight, the join of the ten
> conjugate pairings, each over the nine pairs of generations.

```lean
noncomputable def kineticSpan : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.span_dbard_le_kineticSpan`**, a lemma, [line 787](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L787).

> The line through the `dbard` kinetic term lies in the kinetic span.

```lean
lemma span_dbard_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (dbardKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.span_bardd_le_kineticSpan`**, a lemma, [line 796](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L796).

> The line through the `bardd` kinetic term lies in the kinetic span.

```lean
lemma span_bardd_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (barddKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.span_ubaru_le_kineticSpan`**, a lemma, [line 805](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L805).

> The line through the `ubaru` kinetic term lies in the kinetic span.

```lean
lemma span_ubaru_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (ubaruKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.span_baruu_le_kineticSpan`**, a lemma, [line 813](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L813).

> The line through the `baruu` kinetic term lies in the kinetic span.

```lean
lemma span_baruu_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (baruuKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.span_QbarQ_le_kineticSpan`**, a lemma, [line 821](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L821).

> The line through the `QbarQ` kinetic term lies in the kinetic span.

```lean
lemma span_QbarQ_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (QbarQKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.span_barQQ_le_kineticSpan`**, a lemma, [line 829](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L829).

> The line through the `barQQ` kinetic term lies in the kinetic span.

```lean
lemma span_barQQ_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (barQQKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.span_LbarL_le_kineticSpan`**, a lemma, [line 837](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L837).

> The line through the `LbarL` kinetic term lies in the kinetic span.

```lean
lemma span_LbarL_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (LbarLKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.span_barLL_le_kineticSpan`**, a lemma, [line 844](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L844).

> The line through the `barLL` kinetic term lies in the kinetic span.

```lean
lemma span_barLL_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (barLLKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.span_ebare_le_kineticSpan`**, a lemma, [line 851](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L851).

> The line through the `ebare` kinetic term lies in the kinetic span.

```lean
lemma span_ebare_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (ebareKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.span_baree_le_kineticSpan`**, a lemma, [line 858](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L858).

> The line through the `baree` kinetic term lies in the kinetic span.

```lean
lemma span_baree_le_kineticSpan (f f' : Fin 3) :
    ℂ ∙ (bareeKineticBlock f f').kineticTerm ≤ kineticSpan
```

**`StandardModel.FermionSector.isFixedBy_kineticSpan`**, a lemma, [line 866](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L866).

> The kinetic span is fixed pointwise by both groups, each of its generators being a
> gauge and Lorentz invariant.

```lean
lemma isFixedBy_kineticSpan :
    IsFixedBy (gaugeLorentzMaps repGauge repLorentz) kineticSpan
```

**`StandardModel.FermionSector.kineticSpan_le_massWeightSubmodule`**, a lemma, [line 911](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L911).

> The kinetic span lies at mass weight eight.

```lean
lemma kineticSpan_le_massWeightSubmodule : kineticSpan ≤ massWeightSubmodule 8
```

## E. The blocks reduce to the kinetic terms

> The weight-zero piece of the gauge weight decomposition lies in the join of the ten block
> submodules, hypercharge having already cut the hundred pairings down to ten; and each
> block reduces to its kinetic term, by the three stages its `KineticBlock` package supplies.
> Joining the ten and then the nine generation pairs is `ReducesInvariantsTo.sup` and
> `ReducesInvariantsTo.iSup`, which is where the stability of the blocks and of the kinetic span is
> spent.

**`StandardModel.FermionSector.kineticPairSubmodule`**, a def, [line 951](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L951).

> The ten block submodules of a generation pair, joined.

```lean
noncomputable def kineticPairSubmodule (f f' : Fin 3) :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.kineticBlockSubmodule`**, a def, [line 965](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L965).

> The join of the ten block submodules over the nine pairs of generations.

```lean
noncomputable def kineticBlockSubmodule :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.FermionSector.isStableUnder_kineticPairSubmodule`**, a lemma, [line 971](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L971).

> The joined block submodules of a generation pair are carried into themselves by both
> groups, each block submodule being.

```lean
lemma isStableUnder_kineticPairSubmodule (f f' : Fin 3) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (kineticPairSubmodule f f')
```

**`StandardModel.FermionSector.reducesInvariantsTo_kineticPairSubmodule`**, a lemma, [line 995](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L995).

> The joined block submodules of a generation pair reduce to the kinetic span, each block
> reducing to its kinetic term.

```lean
lemma reducesInvariantsTo_kineticPairSubmodule (f f' : Fin 3) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (kineticPairSubmodule f f')
      kineticSpan
```

**`StandardModel.FermionSector.massWeightSubmoduleGaugeWeightEight_piece_zero_le`**, a lemma, [line 1032](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L1032).

> The weight-zero piece at mass weight eight lies in the join of the ten block submodules, since
> each of the ten conjugate pairings of `massWeightSubmoduleGaugeWeightEight_piece_zero` is an
> underived range against a once-derived one, and the derivative direction is joined over.

```lean
lemma massWeightSubmoduleGaugeWeightEight_piece_zero_le :
    (massWeightSubmoduleGaugeWeightEight).piece 0 ≤ kineticBlockSubmodule
```

**`StandardModel.FermionSector.reducesInvariantsTo_kineticBlockSubmodule`**, a lemma, [line 1047](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L1047).

> The join of the ten block submodules reduces to the kinetic span.

```lean
lemma reducesInvariantsTo_kineticBlockSubmodule :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) kineticBlockSubmodule
      kineticSpan
```

## F. The classification as an equivalence

> The two directions meet. Forwards, hypercharge puts a gauge invariant in the weight-zero
> piece (`GaugeWeightDecomposition.reducesInvariantsTo_piece_zero`), and section E reduces
> that to the kinetic span. Backwards, the kinetic span is a space of gauge and Lorentz
> invariants of mass weight eight (section D), which turns the reduction into an equivalence.
>
> So the fermion sector at mass weight eight carries exactly the kinetic terms — one for
> each species, each pair of generations and each placement of the derivative — and nothing
> else. Compare mass weight six, where the same argument leaves nothing at all. Without a
> derivative there is no four-vector index for the conjugate Pauli matrices to carry, and
> the Dirac mass term does not exist.

**`StandardModel.FermionSector.reducesInvariantsTo_kineticSpan`**, a lemma, [line 1077](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L1077).

> The fermion sector at mass weight eight reduces, for the gauge and Lorentz groups
> together, to the kinetic span. The torus puts an invariant in the weight-zero piece, which
> lies in the ten block submodules, and those reduce to the kinetic terms.

```lean
lemma reducesInvariantsTo_kineticSpan :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (massWeightSubmodule 8)
      kineticSpan
```

**`StandardModel.FermionSector.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 1089](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean#L1089).

> The classification of mass weight eight as an equivalence, in the shape of the
> sibling sectors. An element of `massWeightSubmodule 8 ⊔ S` is fixed by both groups
> exactly when it is a combination of the kinetic terms up to a remainder in `S` fixed by
> both groups.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ kineticSpan
```

## Depends on

- [The ten kinetic blocks](../part-03/localfieldalgebra-fermionsector-massweight-kinet-2.md)

## Proof depends on

- [Finite linear combinations under a linear map](../../../mathematics/part-01/linearcombination.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/MassDimEight.lean)
