---
declaration: module
origin: cited
lean: StandardModel.mem_of_lorentz_invariant_iSup_rankTwo_span, StandardModel.mem_of_lorentz_invariant_iSup_rankThree_span, StandardModel.repLorentz_eq_self_of_mem_mul, StandardModel.repLorentz_mem_mul_of_stable, StandardModel.repLorentz_mem_of_fixed, StandardModel.repLorentz_mem_sup_of_stable, StandardModel.LocalCovFieldAlgebra.repLorentz_eq_self_of_mem_higgs_derivSubmodule_zero, StandardModel.LocalCovFieldAlgebra.mem_of_lorentz_invariant_derivSubmodule_zero_mul_fixed_sup
statement: formalized
proof: formalized
---

# The gauge-Higgs invariants below mass weight nine

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.GaugeHiggsSector.MassWeight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean): 19 declarations, 19 with a docstring.

> The gauge-Higgs sector of the Standard Model's covariant field algebra carries no invariant.

## i. Overview

> Everything below is stated about the covariant field algebra `fieldData.LocalCovFieldAlgebra` of the
> Standard Model.
>
> The mixed `{gauge, scalar}` sector is small, and none of it is invariant. A field-strength
> tower weighs at least four and a Higgs tower at least two, and both weights are even, so
> the sector vanishes below weight six and at every odd weight, weight seven included. What
> is left is weight six, the underived field strength against the underived Higgs, and
> weight eight, that same field strength against the weight-four Higgs terms, together with
> the once-derived field strength against the underived Higgs.
>
> None of it can carry an invariant, and the reason is an index count. The Higgs is a Lorentz
> scalar, so an underived Higgs symbol has no covector index at all and is fixed by the whole
> Lorentz group, while a once-derived one carries a single index, its derivative slot. The
> covector indices of these products are therefore those of the field strength — two when it
> is underived and three when it is once derived — plus at most one from the Higgs.
>
> Two indices admit exactly one invariant contraction, the metric trace, and it vanishes, since the
> metric is symmetric in the pair of indices in which `GaugeSector.F_antisymm` says the
> field strength is antisymmetric. Three indices admit no invariant contraction at all, the
> metric tying two and the Levi-Civita symbol four. Weight six and the two-Higgs term of
> weight eight are of the first kind and the other two terms of weight eight of the second,
> so at no weight below nine does the sector add an invariant to what is already there.
>
> Neither count needs the gauge group, and neither needs a basis of the Higgs. The families
> being peeled are indexed by a covector of the gauge algebra together with a piece of Higgs
> material, and neither index is finite; section A peels a join over an arbitrary index type
> by passing to a finite subset of it, which is all an element of a join ever needs.
>
> The bound is `w < 9` rather than the gauge sector's `w < 8`, weight eight being as empty of
> invariants as the weights below it. No lower bound on `w` is needed either. The sector is
> the two-class sector of the gauge and Higgs generators, so both classes must be present
> with a non-zero weight and the scalars, which force `0 < w` in the gauge-sector statement,
> never appear.

## ii. Key results

> - `mem_of_lorentz_invariant_iSup_rankTwo_span` : a Lorentz invariant of a join, over an arbitrary
>   index type, of the spans of bi-Lorentz families with vanishing metric traces lies in the stable
>   submodule it is taken modulo.
> - `mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_six_sup`,
>   `mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_eight_sup` : mass weights six and eight
>   carry no Lorentz invariant.
> - `mem_sectorMassWeight_gauge_higgs_lt_nine_sup_and_gauge_lorentz_invariant_iff` : the
>   classification below mass weight nine as an equivalence.

## iv. References

> * None.

## A. Peeling a join over an arbitrary index

> The gauge sector combines the reductions of a join of spans indexed by a finite set, which
> is what its twelve directions of the gauge algebra need. Here the families are indexed by a
> covector of the gauge algebra together with a piece of Higgs material, and neither index is
> finite. Nothing is lost: an element of a join lies in the join over finitely many of the
> summands, so `ReducesInvariantsTo.iSup` combines the reductions over the whole join, by
> way of `ReducesInvariantsTo.iSup_of_biSup`. The rest of the section collects the
> stability and the inertness of products and joins that section D consumes.

**`StandardModel.mem_of_lorentz_invariant_iSup_rankTwo_span`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L108).

> A Lorentz invariant of a join, over an arbitrary index type, of the spans of
> bi-Lorentz families with vanishing metric traces lies in the stable submodule it is taken
> modulo. Each span reduces to the line through its metric contraction, which is zero; the
> reductions combine over every finite set of indices, and so over the whole join.

```lean
lemma mem_of_lorentz_invariant_iSup_rankTwo_span {ι : Type}
    {T : ι → (Fin 2 → Fin 1 ⊕ Fin 3) → B}
    (hT : ∀ i, complexLorentzTensor.IsEquivariant (fun _ : Fin 2 => .up) repLorentz
      (liftComponents (T i)))
    (hzero : ∀ i, liftComponents (T i) RankTwo.metric = 0) (S : Submodule ℂ B)
    (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ (⨆ i, Submodule.span ℂ (Set.range (T i))) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.mem_of_lorentz_invariant_iSup_rankThree_span`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L126).

> A Lorentz invariant of a join, over an arbitrary index type, of the spans of triple Lorentz
> families lies in the stable submodule it is taken modulo, since three covector indices admit no
> invariant contraction at all, so each span reduces to `⊥`, and the reductions combine over every
> finite set of indices, and so over the whole join.

```lean
lemma mem_of_lorentz_invariant_iSup_rankThree_span {ι : Type}
    {T : ι → (Fin 3 → Fin 1 ⊕ Fin 3) → B}
    (hT : ∀ i, complexLorentzTensor.IsEquivariant (fun _ : Fin 3 => .up) repLorentz
      (liftComponents (T i)))
    (S : Submodule ℂ B) (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ (⨆ i, Submodule.span ℂ (Set.range (T i))) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.repLorentz_eq_self_of_mem_mul`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L139).

> A product of two pointwise Lorentz-inert submodules is pointwise Lorentz inert.

```lean
lemma repLorentz_eq_self_of_mem_mul
    (hmul : ∀ (Λ : SL(2,ℂ)) (x y : B), repLorentz Λ (x * y) = repLorentz Λ x * repLorentz Λ y)
    {V W : Submodule ℂ B} (hV : ∀ (g : SL(2,ℂ)), ∀ y ∈ V, repLorentz g y = y)
    (hW : ∀ (g : SL(2,ℂ)), ∀ y ∈ W, repLorentz g y = y) (g : SL(2,ℂ)) :
    ∀ y ∈ V * W, repLorentz g y = y
```

**`StandardModel.repLorentz_mem_mul_of_stable`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L150).

> A product of two Lorentz-stable submodules is Lorentz stable.

```lean
lemma repLorentz_mem_mul_of_stable
    (hmul : ∀ (Λ : SL(2,ℂ)) (x y : B), repLorentz Λ (x * y) = repLorentz Λ x * repLorentz Λ y)
    {V W : Submodule ℂ B} (hV : ∀ (g : SL(2,ℂ)), ∀ y ∈ V, repLorentz g y ∈ V)
    (hW : ∀ (g : SL(2,ℂ)), ∀ y ∈ W, repLorentz g y ∈ W) (g : SL(2,ℂ)) :
    ∀ y ∈ V * W, repLorentz g y ∈ V * W
```

**`StandardModel.repLorentz_mem_of_fixed`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L163).

> A pointwise Lorentz-inert submodule is Lorentz stable.

```lean
lemma repLorentz_mem_of_fixed {V : Submodule ℂ B}
    (hV : ∀ (g : SL(2,ℂ)), ∀ y ∈ V, repLorentz g y = y) (g : SL(2,ℂ)) :
    ∀ y ∈ V, repLorentz g y ∈ V
```

**`StandardModel.repLorentz_mem_sup_of_stable`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L168).

> A join of two Lorentz-stable submodules is Lorentz stable.

```lean
lemma repLorentz_mem_sup_of_stable {V W : Submodule ℂ B}
    (hV : ∀ (g : SL(2,ℂ)), ∀ y ∈ V, repLorentz g y ∈ V)
    (hW : ∀ (g : SL(2,ℂ)), ∀ y ∈ W, repLorentz g y ∈ W) (g : SL(2,ℂ)) :
    ∀ y ∈ V ⊔ W, repLorentz g y ∈ V ⊔ W
```

## B. The underived Higgs is Lorentz inert

> The Higgs is a Lorentz scalar, and an underived symbol has no derivative slot for the
> Lorentz matrix to act on, so it is fixed outright — and with it every element of the
> submodule the underived symbols span.

**`StandardModel.LocalCovFieldAlgebra.repLorentz_eq_self_of_mem_higgs_derivSubmodule_zero`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L195).

> The underived Higgs and conjugate-Higgs symbols are Lorentz scalars with no derivative
> slot to rotate, so every element of the weight-two Higgs submodule is fixed by the whole
> Lorentz group.

```lean
lemma repLorentz_eq_self_of_mem_higgs_derivSubmodule_zero (g : SL(2,ℂ))
    {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ ScalarSector.derivSubmodule 0) : repLorentzGroup g y = y
```

## C. Field strengths against Higgs material

> Three products have to be classified. An underived field strength against inert material is
> a bi-Lorentz family whose metric trace vanishes with the antisymmetry of the field strength;
> a once-derived one against inert material is a triple Lorentz family; and an underived one
> against a once-derived Higgs is a triple Lorentz family as well, the Higgs supplying the
> third index. The last is the only one in which a Higgs index moves at all.

**`StandardModel.LocalCovFieldAlgebra.mem_of_lorentz_invariant_derivSubmodule_zero_mul_fixed_sup`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L237).

> An underived field strength against Lorentz-inert material carries no Lorentz
> invariant modulo a Lorentz-stable submodule.

```lean
lemma mem_of_lorentz_invariant_derivSubmodule_zero_mul_fixed_sup
    (C : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hC : ∀ (g : SL(2,ℂ)), ∀ y ∈ C, repLorentzGroup g y = y)
      (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ GaugeSector.derivSubmodule 0 * C ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) : x ∈ S
```

**`StandardModel.LocalCovFieldAlgebra.mem_of_lorentz_invariant_derivSubmodule_one_mul_fixed_sup`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L274).

> A once-derived field strength against Lorentz-inert material carries no Lorentz
> invariant modulo a Lorentz-stable submodule.

```lean
lemma mem_of_lorentz_invariant_derivSubmodule_one_mul_fixed_sup
    (C : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hC : ∀ (g : SL(2,ℂ)), ∀ y ∈ C, repLorentzGroup g y = y)
      (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ GaugeSector.derivSubmodule 1 * C ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) : x ∈ S
```

**`StandardModel.LocalCovFieldAlgebra.repLorentzGroup_higgsOrConj_deriv_one`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L306).

> The once-derived Higgs and conjugate-Higgs symbols, read as one family indexed by the
> derivative direction, transform as a Lorentz vector.

```lean
lemma repLorentzGroup_higgsOrConj_deriv_one
    (j : Module.Dual ℂ HiggsVec ⊕ Module.Dual ℂ (ConjModule HiggsVec))
    (g : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    repLorentzGroup g (Sum.elim (fun φ => higgsField ![μ] φ)
      (fun ψ => conjHiggsField ![μ] ψ) j)
      = ∑ ν : Fin 1 ⊕ Fin 3, (((SL2C.toLorentzGroup g).1 ν μ : ℝ) : ℂ) •
          Sum.elim (fun φ => higgsField ![ν] φ)
            (fun ψ => conjHiggsField ![ν] ψ) j
```

**`StandardModel.LocalCovFieldAlgebra.fieldStrengthHiggsDerivFamily`**, a def, [line 327](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L327).

> The underived field strength against a once-derived Higgs or conjugate-Higgs symbol, as a
> family of three covector indices, the two of the field strength and the derivative direction
> of the Higgs.

```lean
noncomputable def fieldStrengthHiggsDerivFamily
    (i : Module.Dual ℝ GaugeAlgebra ×
      (Module.Dual ℂ HiggsVec ⊕ Module.Dual ℂ (ConjModule HiggsVec)))
    (l : Fin 3 → Fin 1 ⊕ Fin 3) : fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.isEquivariant_up_fieldStrengthHiggsDerivFamily`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L335).

> The underived field strength against a once-derived Higgs is a triple Lorentz tensor.

```lean
lemma isEquivariant_up_fieldStrengthHiggsDerivFamily
    (i : Module.Dual ℝ GaugeAlgebra ×
      (Module.Dual ℂ HiggsVec ⊕ Module.Dual ℂ (ConjModule HiggsVec))) :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 3 => .up) repLorentzGroup
      (liftComponents (fieldStrengthHiggsDerivFamily i))
```

**`StandardModel.LocalCovFieldAlgebra.mul_derivSubmodule_one_le_iSup_span`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L347).

> An underived field-strength symbol times the once-derived Higgs submodule lies in the join
> of the spans of the families `fieldStrengthHiggsDerivFamily`.

```lean
lemma mul_derivSubmodule_one_le_iSup_span (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    ScalarSector.derivSubmodule 1
      ≤ Submodule.comap (LinearMap.mulLeft ℂ (gaugeFieldStrength ![] μ ν φ))
        (⨆ i, Submodule.span ℂ (Set.range (fieldStrengthHiggsDerivFamily i)))
```

**`StandardModel.LocalCovFieldAlgebra.mem_of_lorentz_invariant_derivSubmodule_zero_mul_higgs_one_sup`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L377).

> An underived field strength against a once-derived Higgs carries no Lorentz invariant
> modulo a Lorentz-stable submodule, since three covector indices admit no contraction.

```lean
lemma mem_of_lorentz_invariant_derivSubmodule_zero_mul_higgs_one_sup
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ GaugeSector.derivSubmodule 0 * ScalarSector.derivSubmodule 1 ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) : x ∈ S
```

## D. Mass weights six and eight

> Weight six is a single product and section C settles it outright. Weight eight is a join of
> three, and they are peeled one at a time, the two not yet peeled joining the error term —
> which asks that they be Lorentz stable. The gauge and Higgs derivative submodules are, and
> so are their products and joins.

**`StandardModel.LocalCovFieldAlgebra.mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_six_sup`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L412).

> Mass weight six carries no Lorentz invariant modulo a Lorentz-stable submodule. A
> Lorentz invariant of `fieldData.sectorMassWeight {gauge, scalar} 6 ⊔ S` lies in `S`. The weight is
> the underived field strength against the underived Higgs, whose two covector indices are
> contracted only by the metric, and that trace vanishes.

```lean
lemma mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_six_sup
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} 6 ⊔
      S)
    (hinv : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) : x ∈ S
```

**`StandardModel.LocalCovFieldAlgebra.mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_eight_sup`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L428).

> Mass weight eight carries no Lorentz invariant modulo a Lorentz-stable submodule. A
> Lorentz invariant of `fieldData.sectorMassWeight {gauge, scalar} 8 ⊔ S` lies in `S`. The three
> products making up the weight are peeled off one at a time, the two carrying three
> covector indices by the absence of any contraction and the one carrying two by the
> vanishing of the metric trace.

```lean
lemma mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_eight_sup
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} 8 ⊔
      S)
    (hinv : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) : x ∈ S
```

## E. The classification below mass weight nine

> The nine weights below nine are now settled: the sector vanishes below weight six and at
> weight seven, and weights six and eight are section D. So below weight nine the gauge-Higgs
> sector supplies no invariant beyond what `S` already carries, and the equivalences record it
> in the shape the other sectors carry, so that all of them can be combined.

**`StandardModel.LocalCovFieldAlgebra.mem_of_invariant_sectorMassWeight_gauge_higgs_lt_nine_sup`**, a lemma, [line 471](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L471).

> Below mass weight nine the gauge-Higgs sector carries no Lorentz invariant. A Lorentz
> invariant of `fieldData.sectorMassWeight {gauge, scalar} w ⊔ S` for `w < 9` lies in `S`. Weights
> below six and weight seven are trivial submodules, and weights six and eight are the two
> index counts.

```lean
lemma mem_of_invariant_sectorMassWeight_gauge_higgs_lt_nine_sup (w : ℕ) (hw : w < 9)
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y
      ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} w ⊔
      S)
    (hL : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) : x ∈ S
```

**`StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_gauge_higgs_lt_nine_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L492).

> The classification below mass weight nine as an equivalence, in the shape of the gauge-
> and Yukawa-sector statements. An element of `fieldData.sectorMassWeight {gauge, scalar} w ⊔ S` for
> `w < 9` is fixed by both groups exactly when it is itself an element of `S` fixed by both
> groups. Gauge stability of `S` is not needed, and neither is gauge invariance of `x`, since the
> forward direction is the index count, which uses the Lorentz group alone.

```lean
lemma mem_sectorMassWeight_gauge_higgs_lt_nine_sup_and_gauge_lorentz_invariant_iff
    (w : ℕ) (hw : w < 9) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x) ∧ ∀ g : SL(2,ℂ),
          repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x = y
```

**`StandardModel.LocalCovFieldAlgebra.mem_sectorMassWeight_gauge_higgs_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean#L512).

> The same classification without the existential. Below mass weight nine an element of
> `fieldData.sectorMassWeight {gauge, scalar} w ⊔ S` fixed by both groups is an element of `S`
> fixed by both groups, and conversely.

```lean
lemma mem_sectorMassWeight_gauge_higgs_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem
    (w : ℕ) (hw : w < 9) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x) ∧ ∀ g : SL(2,ℂ),
          repLorentzGroup g x = x)
      ↔ (x ∈ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
```

## Depends on

- [The sectors of a gauge field theory](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-localcovfieldalgebra-sector.md)
- [The gauge sector](localfieldalgebra-gaugesector-basic.md)
- [The derivative submodules of the scalar sector](../part-05/localfieldalgebra-scalarsector-derivsubmodule-ba.md)
- [The metrics are the unique invariant tensors with two indices of one colour](../../../relativity/tensors/complextensor-metrics-basic.md)

## Proof depends on

- [The mixed gauge-Higgs sector](localfieldalgebra-gaugehiggssector-basic.md)
- [The invariants below mass weight eight (GaugeSector/MassWeight/MassDimLTEight)](localfieldalgebra-gaugesector-massweight-massdim-2.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/GaugeHiggsSector/MassWeight.lean)
