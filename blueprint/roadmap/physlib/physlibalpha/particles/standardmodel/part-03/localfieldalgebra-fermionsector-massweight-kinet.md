---
declaration: module
origin: cited
lean: StandardModel.FermionSector.repLorentz_symbol_deriv_one, StandardModel.FermionSector.repLorentz_component_deriv_one, StandardModel.FermionSector.repLorentz_leftComp_deriv_one, StandardModel.FermionSector.repLorentz_rightComp_deriv_one, StandardModel.FermionSector.isEquivariant_colourFundAntiFund_mul, StandardModel.FermionSector.isEquivariant_colourFundAntiFund_mul_swap, StandardModel.FermionSector.isEquivariant_isospinFundAntiFund_mul, StandardModel.FermionSector.isEquivariant_isospinFundAntiFund_mul_swap
statement: formalized
proof: formalized
---

# The kinetic terms of the fermion sector

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.FermionSector.MassWeight.KineticFamilies`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean): 21 declarations, 21 with a docstring.

> The package that turns a kinetic block of the fermion sector into its kinetic term and the
> reduction of the block to it.

## i. Overview

> The invariants of the fermion sector at mass weight eight are the kinetic terms, and this
> file builds them. A kinetic term pairs a species with its own conjugate, one of the two
> carrying a covariant derivative, and joins their indices in the only ways available. The
> colour indices by the Kronecker delta, the isospin indices by the Kronecker delta, and the
> four-vector index against the two opposite-chirality spinor indices by the conjugate Pauli
> matrices. That last contraction is `ψ̄ σ̄^μ ∂_μ ψ`.
>
> Ten blocks arise, the five conjugate pairs each with the derivative on one factor or the
> other, and they differ only in which indices their symbols carry. So the work is done once,
> generically, in terms of `InvariantReductionToSpan`: a `KineticBlock` packages a
> block together with its three classification steps — colour, isospin, Lorentz — and from
> that package alone come the contraction, its invariance under both groups, and the reduction
> of the block down to the line through it. The ten blocks are then ten instantiations.
>
> The three stages are the same three the Yukawa sector runs, in the same order, and for the
> same reason: each contraction is a spectator of the ones after it. Where a block's symbols
> carry no colour index — the two lepton-doublet blocks and the two lepton-singlet ones — the
> colour stage is `InvariantReductionToSpan.ofFixedFamily` rather than a classification, and
> likewise for isospin where the symbols carry none. That keeps all ten blocks in one shape.
>
> The ten blocks themselves are built in `KineticTerms`, which instantiates the package.

## ii. Key results

> - `KineticBlock` : one kinetic block of the fermion sector, together with the three classifications
>   its indices admit.
> - `KineticBlock.reducesInvariantsTo` : the block span reduces to the span of its kinetic term.
> - `KineticBlock.repGauge_kineticTerm`, `KineticBlock.repLorentz_kineticTerm` : the kinetic term
>   is gauge and Lorentz invariant.

## iv. References

> * None.

## A. The once-derived chiral component families

> A tower with one covariant derivative mixes into every assignment of one derivative
> direction, so its Lorentz law is a sum over such assignments, with one column of the
> Lorentz matrix per slot. The value index is untouched by that sum. It still moves by the
> contragredient action, exactly as at zero derivatives. Composing the two gives the laws
> `repLorentz_leftComp_deriv_one` and `repLorentz_rightComp_deriv_one`, the derivative slot
> fundamental and the spinor slot dual.

**`StandardModel.FermionSector.repLorentz_symbol_deriv_one`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L88).

> The Lorentz transformation of a symbol with one covariant derivative. The derivative
> slot moves by the columns of the Lorentz matrix and the value index by the
> contragredient action.

```lean
lemma repLorentz_symbol_deriv_one {V : Type} [AddCommGroup V] [Module ℂ V]
    {rep : Representation ℂ SL(2,ℂ) V}
    {X : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] fieldData.LocalCovFieldAlgebra}
    (hX : IsLorentzCovDerivTransforms repLorentz rep X) (Λ : SL(2,ℂ))
    (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℂ V) :
    repLorentz Λ (X ![μ] φ)
      = ∑ ν, (((SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) • X ![ν] (rep.dual Λ φ)
```

**`StandardModel.FermionSector.repLorentz_component_deriv_one`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L103).

> The Lorentz transformation of a component of a once-derived symbol, when the
> coordinate functionals `c` are permuted by the contragredient action with coefficients
> `m`. This is the once-derived form of the laws of `Components`.

```lean
lemma repLorentz_component_deriv_one {V : Type} [AddCommGroup V] [Module ℂ V]
    {rep : Representation ℂ SL(2,ℂ) V}
    {X : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] fieldData.LocalCovFieldAlgebra}
    (hX : IsLorentzCovDerivTransforms repLorentz rep X)
    {c : Fin 2 → Module.Dual ℂ V} {m : SL(2,ℂ) → Fin 2 → Fin 2 → ℂ}
    (hc : ∀ (Λ : SL(2,ℂ)) (a : Fin 2), rep.dual Λ (c a) = ∑ β, m Λ a β • c β)
    (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (a : Fin 2) :
    repLorentz Λ (X ![μ] (c a))
      = ∑ ν, ∑ β, ((((SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) * m Λ a β) • X ![ν] (c β)
```

**`StandardModel.FermionSector.repLorentz_leftComp_deriv_one`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L119).

> Every undotted component family carries a four-vector index and a dual undotted
> spinor index, at one covariant derivative.

```lean
lemma repLorentz_leftComp_deriv_one (i : LeftIdx) :
    ∀ (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (a : Fin 2), repLorentz Λ (leftComp ![μ] i a)
      = ∑ ν, ∑ β, ((((SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) * (Λ⁻¹).1 a β) •
        leftComp ![ν] i β
```

**`StandardModel.FermionSector.repLorentz_rightComp_deriv_one`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L142).

> Every dotted component family carries a four-vector index and a dual dotted spinor
> index, at one covariant derivative.

```lean
lemma repLorentz_rightComp_deriv_one (i : RightIdx) :
    ∀ (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (a : Fin 2), repLorentz Λ (rightComp ![μ] i a)
      = ∑ ν, ∑ β, ((((SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) * star ((Λ⁻¹).1 a β)) •
        rightComp ![ν] i β
```

## B. Products of two components

> A block is a product of two components, and each of its index laws comes from the laws of
> the two factors. The representation respects multiplication, so the two transform
> independently and their coefficients multiply. Which slot of the classifier a factor
> occupies is decided by its variance, the fundamental one going first, so each law comes in
> two arrangements according to which factor is the barred one.

**`StandardModel.FermionSector.isEquivariant_colourFundAntiFund_mul`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L177).

> A product of a component with a fundamental colour index and one with an
> anti-fundamental colour index carries one colour index of each kind.

```lean
lemma isEquivariant_colourFundAntiFund_mul
    {A C : Fin 3 → fieldData.LocalCovFieldAlgebra}
    (hA : ∀ (U : specialUnitaryGroup (Fin 3) ℂ) (c : Fin 3),
      repGauge ((U, 1, 1) : GaugeGroupI) (A c) = ∑ a, U.1 a c • A a)
    (hC : ∀ (U : specialUnitaryGroup (Fin 3) ℂ) (c : Fin 3),
      repGauge ((U, 1, 1) : GaugeGroupI) (C c) = ∑ a, conj (U.1 a c) • C a) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun l : Fin 2 → Fin 3 => A (l 0) * C (l 1)) ∘ fundAntiFundIdx))
```

**`StandardModel.FermionSector.isEquivariant_colourFundAntiFund_mul_swap`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L192).

> The same with the two factors exchanged, the anti-fundamental one first.

```lean
lemma isEquivariant_colourFundAntiFund_mul_swap
    {A C : Fin 3 → fieldData.LocalCovFieldAlgebra}
    (hA : ∀ (U : specialUnitaryGroup (Fin 3) ℂ) (c : Fin 3),
      repGauge ((U, 1, 1) : GaugeGroupI) (A c) = ∑ a, conj (U.1 a c) • A a)
    (hC : ∀ (U : specialUnitaryGroup (Fin 3) ℂ) (c : Fin 3),
      repGauge ((U, 1, 1) : GaugeGroupI) (C c) = ∑ a, U.1 a c • C a) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun l : Fin 2 → Fin 3 => A (l 1) * C (l 0)) ∘ fundAntiFundIdx))
```

**`StandardModel.FermionSector.isEquivariant_isospinFundAntiFund_mul`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L208).

> A product of a component with a fundamental isospin index and one with an
> anti-fundamental isospin index carries one isospin index of each kind.

```lean
lemma isEquivariant_isospinFundAntiFund_mul
    {A C : Fin 2 → fieldData.LocalCovFieldAlgebra}
    (hA : ∀ (V : specialUnitaryGroup (Fin 2) ℂ) (w : Fin 2),
      repGauge ((1, V, 1) : GaugeGroupI) (A w) = ∑ a, V.1 a w • A a)
    (hC : ∀ (V : specialUnitaryGroup (Fin 2) ℂ) (w : Fin 2),
      repGauge ((1, V, 1) : GaugeGroupI) (C w) = ∑ a, conj (V.1 a w) • C a) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun l : Fin 2 → Fin 2 => A (l 0) * C (l 1)) ∘ fundAntiFundIdx))
```

**`StandardModel.FermionSector.isEquivariant_isospinFundAntiFund_mul_swap`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L223).

> The same with the two factors exchanged, the anti-fundamental one first.

```lean
lemma isEquivariant_isospinFundAntiFund_mul_swap
    {A C : Fin 2 → fieldData.LocalCovFieldAlgebra}
    (hA : ∀ (V : specialUnitaryGroup (Fin 2) ℂ) (w : Fin 2),
      repGauge ((1, V, 1) : GaugeGroupI) (A w) = ∑ a, conj (V.1 a w) • A a)
    (hC : ∀ (V : specialUnitaryGroup (Fin 2) ℂ) (w : Fin 2),
      repGauge ((1, V, 1) : GaugeGroupI) (C w) = ∑ a, V.1 a w • C a) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun l : Fin 2 → Fin 2 => A (l 1) * C (l 0)) ∘ fundAntiFundIdx))
```

**`StandardModel.FermionSector.repGauge_mul_fixed`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L240).

> A product of two components that a gauge transformation fixes is fixed by it. This is the form
> in which a block whose symbols carry no colour, or no isospin, supplies the corresponding
> stage.

```lean
lemma repGauge_mul_fixed
    {g : GaugeGroupI} {a c : fieldData.LocalCovFieldAlgebra} (ha : repGauge g a = a)
    (hc : repGauge g c = c) :
    repGauge g (a * c) = a * c
```

**`StandardModel.FermionSector.repGauge_mul_smul_fixed`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L249).

> A product of two components that a gauge transformation scales by reciprocal scalars
> is fixed by it. This is the form in which the hypercharges of a species and its conjugate
> cancel.

```lean
lemma repGauge_mul_smul_fixed
    {g : GaugeGroupI} {z z' : ℂ} {a c : fieldData.LocalCovFieldAlgebra} (hz : z * z' = 1)
    (ha : repGauge g a = z • a) (hc : repGauge g c = z' • c) :
    repGauge g (a * c) = a * c
```

**`StandardModel.FermionSector.isEquivariant_upDownRDownL_sum`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L260).

> A finite sum of families carrying one four-vector index and a pair of dual
> opposite-chirality Weyl indices is such a family again, the colour and isospin
> contractions are Lorentz spectators.

```lean
lemma isEquivariant_upDownRDownL_sum {ι : Type} [Fintype ι]
    {T : ι → (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → fieldData.LocalCovFieldAlgebra}
    (hT : ∀ i, complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents (T i ∘ dualIndexEquiv))) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p => ∑ i, T i p) ∘ dualIndexEquiv))
```

## C. The kinetic block package

> A kinetic block is classified in three stages, and every block runs the same three: colour,
> then isospin, then Lorentz, each contraction a spectator of the ones after it. `KineticBlock`
> packages a block together with the three steps, and from the package alone come the kinetic
> term, its invariance under both groups, and the reduction of the block to the line
> through it.
>
> The colour and isospin indices of the block are listed in the order the classifiers read
> them, fundamental first; a block whose symbols carry no colour, or no isospin, simply
> ignores the corresponding pair and supplies `InvariantReductionToSpan.ofFixedFamily` for that
> stage. Each step comes with the fact that its contraction lies in the submodule it classifies, which
> is what carries the invariance of one stage through the stages after it.

**`StandardModel.FermionSector.KineticBlock`**, a structure, [line 296](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L296).

> One kinetic block of the fermion sector, together with the three classifications its
> indices admit. The block is indexed by the derivative direction, the pair of spinor
> indices in the order `(undotted, dotted)`, the pair of colour indices and the pair of
> isospin indices, each pair in the order `(fundamental, anti-fundamental)`.

```lean
structure KineticBlock where
  /-- The components of the block. -/
  blk : (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
  /-- The colour stage. At fixed derivative, spinor and isospin indices the colour pair is
    classified, by the delta contraction if the block carries colour and trivially if it
    does not. -/
  colourStep : ∀ (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (w w' : Fin 2),
    InvariantReductionToSpan (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge (U, 1, 1))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 3 => blk q l (n 0) (n 1) w w'))
  /-- The colour contraction lies in the span of the components it contracts. -/
  colourStep_mem : ∀ q l w w', (colourStep q l w w').spanningVector
    ∈ Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 3 => blk q l (n 0) (n 1) w w')
  /-- The isospin stage, applied to the colour contraction. -/
  isospinStep : ∀ (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2),
    InvariantReductionToSpan (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge (1, V, 1))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 2 => (colourStep q l (n 0) (n 1)).spanningVector))
  /-- The isospin contraction lies in the span of the colour contractions. -/
  isospinStep_mem : ∀ q l, (isospinStep q l).spanningVector
    ∈ Submodule.span ℂ
      (Set.range fun n : Fin 2 → Fin 2 => (colourStep q l (n 0) (n 1)).spanningVector)
  /-- The Lorentz stage, applied to the doubly contracted block, one four-vector index
    against a dual dotted and a dual undotted spinor index. -/
  lorentzStep : InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
    (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
      (isospinStep p.1 p.2).spanningVector))
  /-- The Lorentz contraction lies in the span of the isospin contractions. -/
  lorentzStep_mem : lorentzStep.spanningVector
    ∈ Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
      (isospinStep p.1 p.2).spanningVector)
  /-- A hypercharge transformation fixes every component of the block, the hypercharges of
    a species and its conjugate cancelling. -/
  hyper : ∀ (t : unitary ℂ) q l c c' w w',
    repGauge ((1, 1, t) : GaugeGroupI) (blk q l c c' w w') = blk q l c c' w w'
```

**`StandardModel.FermionSector.KineticBlock.kineticTerm`**, a def, [line 337](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L337).

> The kinetic term of a block, the conjugate Pauli contraction of its doubly contracted
> form, which is `ψ̄ σ̄^μ ∂_μ ψ` with the colour and isospin indices already joined.

```lean
noncomputable def kineticTerm : B
```

**`StandardModel.FermionSector.KineticBlock.blockSpan`**, a def, [line 341](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L341).

> The join, over the derivative, spinor and isospin indices, of the colour spans of the
> block, the span the block submodule is reduced from.

```lean
noncomputable def blockSpan : Submodule ℂ B
```

**`StandardModel.FermionSector.KineticBlock.reducesInvariantsTo`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L347).

> The three stages in sequence. The block span reduces to the span of the kinetic term.

```lean
lemma reducesInvariantsTo :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) K.blockSpan (ℂ ∙ K.kineticTerm)
```

**`StandardModel.FermionSector.KineticBlock.kineticTerm_mem`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L372).

> The kinetic term lies in any submodule containing every component of the block, since each
> contraction lies in the span of the objects of the stage before it.

```lean
lemma kineticTerm_mem {V : Submodule ℂ B}
    (hV : ∀ q l c c' w w', K.blk q l c c' w w' ∈ V) : K.kineticTerm ∈ V
```

**`StandardModel.FermionSector.KineticBlock.repGauge_su3_kineticTerm`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L387).

> The kinetic term is fixed by the colour factor, since the colour contractions are, and every
> later stage stays inside their span.

```lean
lemma repGauge_su3_kineticTerm (U : specialUnitaryGroup (Fin 3) ℂ) :
    repGauge ((U, 1, 1) : GaugeGroupI) K.kineticTerm = K.kineticTerm
```

**`StandardModel.FermionSector.KineticBlock.repGauge_su2_kineticTerm`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L398).

> The kinetic term is fixed by the isospin factor.

```lean
lemma repGauge_su2_kineticTerm (V : specialUnitaryGroup (Fin 2) ℂ) :
    repGauge ((1, V, 1) : GaugeGroupI) K.kineticTerm = K.kineticTerm
```

**`StandardModel.FermionSector.KineticBlock.repGauge_u1_kineticTerm`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L405).

> The kinetic term is fixed by the hypercharge factor, the hypercharges of a species and
> its conjugate cancelling on every component of the block.

```lean
lemma repGauge_u1_kineticTerm (t : unitary ℂ) :
    repGauge ((1, 1, t) : GaugeGroupI) K.kineticTerm = K.kineticTerm
```

**`StandardModel.FermionSector.KineticBlock.repGauge_kineticTerm`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L421).

> The kinetic term is gauge invariant. A gauge transformation is the product of its
> colour, isospin and hypercharge parts, and each fixes it.

```lean
lemma repGauge_kineticTerm (g : GaugeGroupI) : repGauge g K.kineticTerm = K.kineticTerm
```

**`StandardModel.FermionSector.KineticBlock.repLorentz_kineticTerm`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean#L427).

> The kinetic term is Lorentz invariant, being the conjugate Pauli contraction of a
> vector dual left-right Weyl family.

```lean
lemma repLorentz_kineticTerm (Λ : SL(2,ℂ)) :
    repLorentz Λ K.kineticTerm = K.kineticTerm
```

## Depends on

- [Families of colour and isospin components and their invariants](../part-02/gaugegroup-invariants-basic.md)
- [The invariants below mass weight eight (FermionSector/MassWeight/MassDimLTEight)](../part-04/localfieldalgebra-fermionsector-massweight-massd-2.md)
- [The Pauli tensor is the unique invariant](../../../relativity/bispinors/pauli-basic.md)

## Proof depends on

- [Invariant reduction for the Standard Model gauge group](../part-02/localfieldalgebra-invariantreduction.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/FermionSector/MassWeight/KineticFamilies.lean)
