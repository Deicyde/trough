---
declaration: module
origin: cited
lean: StandardModel.ScalarSector.isEquivariant_up_rankOne_dotGaugeHiggs_left, StandardModel.ScalarSector.isEquivariant_up_rankOne_dotGaugeHiggs_right, StandardModel.ScalarSector.dotSpan_one_zero_eq, StandardModel.ScalarSector.dotSpan_zero_one_eq, StandardModel.ScalarSector.repLorentz_dotGaugeHiggs_zero, StandardModel.ScalarSector.dotSpan_zero_zero_eq, StandardModel.ScalarSector.repLorentz_of_mem_dotSpan_zero_zero, StandardModel.ScalarSector.rep_of_mem_dotSpan
statement: formalized
proof: formalized
---

# The Higgs invariants below mass weight eight

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.ScalarSector.MassWeight.MassDimLTEight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean): 18 declarations, 18 with a docstring.

> The gauge and Lorentz invariants of the scalar sector below mass weight eight, the Higgs mass
> term alone.

## i. Overview

> The scalar sector is the one sector of the Standard Model already carrying an invariant
> below mass weight eight, and it is the most familiar of all: the mass term `H† H`, of mass
> weight four.  Everything else below weight eight dies, and for three different reasons.
>
> The odd weights are trivial submodules, every Higgs tower carrying even mass weight.
> Weight two dies on hypercharge. A single Higgs symbol carries `6Y = ∓3`, so nothing at that
> weight is neutral, which is the gauge classification of
> `reducesInvariantsTo_massWeightSubmodule_two`.  Weight six dies on Lorentz counting.  Its
> gauge invariants are the isospin contractions with one derivative, `∂_μ H† H` and
> `H† ∂_μ H`, and a single covector index admits no invariant contraction at all — the metric
> ties two indices and the Levi-Civita symbol four — which is
> `complexLorentzTensor.invariants_up_pow_eq_bot_of_odd` at one index.
>
> Weight four survives because the Higgs is a Lorentz scalar.  Its gauge invariants are the
> multiples of `H† H`, and with no derivative slot there is no Lorentz index to contract, so
> the Lorentz group fixes the contraction outright and the whole line survives.  That is why
> the conclusion here is membership in a span rather than in `S`, unlike the gauge and Yukawa
> sectors. The surviving span is the Higgs mass term at weight four and trivial at every
> other weight below eight.
>
> As in the gauge sector the final statement needs `0 < w` as well as `w < 8`. At `w = 0` the
> mass-weight submodule contains the scalars, so `1` is an invariant of weight zero lying in
> no `S`.

## ii. Key results

> - `isEquivariant_up_rankOne_dotGaugeHiggs_left` and its `_right` companion : the isospin
>   contractions with one derivative are Lorentz vectors.
> - `lorentzContractionLTEightSpan` : the surviving span below mass weight eight, the line through
>   the Higgs mass term at weight four.
> - `mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff` : the classification
>   below mass weight eight.

## iv. References

> * None.

## A. The isospin contractions with one derivative as Lorentz vectors

> At mass weight six the gauge classification leaves the isospin contractions carrying one
> derivative, on either of the two towers.  The Higgs is a Lorentz scalar, so the only
> Lorentz index such a contraction has is that derivative slot, and read as a family indexed
> by it the contraction is a Lorentz vector.  `invariants_up_pow_eq_bot_of_odd` says that one index
> admits no invariant contraction, so the span of such a family reduces to `⊥`
> (`ComplexVector.reducesInvariantsTo_bot_of_odd`); the spans are themselves stable, so
> `ReducesInvariantsTo.sup` joins the two.

**`StandardModel.ScalarSector.isEquivariant_up_rankOne_dotGaugeHiggs_left`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L92).

> The isospin contraction of a once-derived Higgs tower against an underived conjugate
> tower, read as a family indexed by its derivative slot, is a Lorentz vector.

```lean
lemma isEquivariant_up_rankOne_dotGaugeHiggs_left :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 1 => .up) repLorentzGroup
      (liftComponents fun d : Fin 1 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs d ![])
```

**`StandardModel.ScalarSector.isEquivariant_up_rankOne_dotGaugeHiggs_right`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L102).

> The isospin contraction of an underived Higgs tower against a once-derived conjugate
> tower is a Lorentz vector in the same way.

```lean
lemma isEquivariant_up_rankOne_dotGaugeHiggs_right :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 1 => .up) repLorentzGroup
      (liftComponents fun d : Fin 1 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs ![] d)
```

**`StandardModel.ScalarSector.dotSpan_one_zero_eq`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L112).

> The span of the isospin contractions with one derivative on the Higgs tower is the
> span of the components of the corresponding Lorentz vector.

```lean
lemma dotSpan_one_zero_eq :
    dotSpan 1 0
      = Submodule.span ℂ (Set.range fun d : Fin 1 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs d ![])
```

**`StandardModel.ScalarSector.dotSpan_zero_one_eq`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L121).

> The span of the isospin contractions with one derivative on the conjugate tower is the
> span of the components of the corresponding Lorentz vector.

```lean
lemma dotSpan_zero_one_eq :
    dotSpan 0 1
      = Submodule.span ℂ (Set.range fun d : Fin 1 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs ![] d)
```

## B. The underived isospin contraction as a Lorentz scalar

> At mass weight four the gauge classification leaves the multiples of `H† H`.  An underived
> Higgs symbol carries no derivative slot, so the Lorentz group moves it by an empty product
> of Lorentz matrix entries, that is not at all, and the contraction and the whole line
> through it are fixed.  Nothing peels off here; the line is the answer.

**`StandardModel.ScalarSector.repLorentz_dotGaugeHiggs_zero`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L141).

> The underived isospin contraction is a Lorentz scalar.

```lean
lemma repLorentz_dotGaugeHiggs_zero (g : SL(2,ℂ)) :
    repLorentzGroup g (dotGaugeHiggs (![] : Fin 0 → Fin 1 ⊕ Fin 3) ![])
      = dotGaugeHiggs ![] ![]
```

**`StandardModel.ScalarSector.dotSpan_zero_zero_eq`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L148).

> The span of the underived isospin contractions is the line through the mass term.

```lean
lemma dotSpan_zero_zero_eq :
    dotSpan 0 0 = ℂ ∙ dotGaugeHiggs (![] : Fin 0 → Fin 1 ⊕ Fin 3) ![]
```

**`StandardModel.ScalarSector.repLorentz_of_mem_dotSpan_zero_zero`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L158).

> Every element of the line through the underived isospin contraction is a Lorentz
> invariant.

```lean
lemma repLorentz_of_mem_dotSpan_zero_zero (g : SL(2,ℂ)) {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ dotSpan 0 0) :
    repLorentzGroup g y = y
```

**`StandardModel.ScalarSector.rep_of_mem_dotSpan`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L166).

> Every element of a span of isospin contractions is a gauge invariant.

```lean
lemma rep_of_mem_dotSpan {n m : ℕ} (g : GaugeGroupI) {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ dotSpan n m) :
    repGaugeGroupI g y = y
```

**`StandardModel.ScalarSector.dotSpan_zero_zero_le_massWeightSubmodule`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L172).

> The line through the underived isospin contraction lies in mass weight four.

```lean
lemma dotSpan_zero_zero_le_massWeightSubmodule :
    dotSpan 0 0 ≤ massWeightSubmodule 4
```

## C. Mass weight six

> The gauge classification leaves, at mass weight six, the two spans of once-derived isospin
> contractions (`reducesInvariantsTo_massWeightSubmodule_six`). Section A reduces each to `⊥`
> for the Lorentz group, since a single covector index carries no invariant contraction, and
> `ReducesInvariantsTo.sup` joins them: nothing is left behind.

**`StandardModel.ScalarSector.reducesInvariantsTo_dotSpan_one_zero_sup_zero_one`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L192).

> The once-derived isospin contractions reduce to `⊥` for the Lorentz group. Each span is
> spanned by a Lorentz vector, and a single covector index carries no invariant.

```lean
lemma reducesInvariantsTo_dotSpan_one_zero_sup_zero_one :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentzGroup g) (dotSpan 1 0 ⊔ dotSpan 0 1) ⊥
```

## D. The classification below mass weight eight

> The seven weights between zero and eight are now settled: weights one, three, five and
> seven are trivial submodules, weight two is killed by hypercharge, weight six by section C,
> and weight four leaves the line through the mass term.  `lorentzContractionLTEightSpan`
> records that answer as a single submodule depending on the weight, and
> `reducesInvariantsTo_lorentzContractionLTEightSpan` reduces each weight to it, so the
> statement has the shape of the weight-eight one and of the other sectors' below-eight ones,
> whose spans happen to be trivial.

**`StandardModel.ScalarSector.lorentzContractionLTEightSpan`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L220).

> The gauge and Lorentz invariants of the scalar sector at mass weight `w` for
> `0 < w < 8`, the line through the Higgs mass term at weight four, and nothing at any
> other weight.

```lean
noncomputable def lorentzContractionLTEightSpan
    (w : ℕ) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.lorentzContractionLTEightSpan_le_massWeightSubmodule`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L225).

> The surviving span at weight `w` lies in the mass-weight submodule of weight `w`.

```lean
lemma lorentzContractionLTEightSpan_le_massWeightSubmodule (w : ℕ) :
    lorentzContractionLTEightSpan w ≤ massWeightSubmodule w
```

**`StandardModel.ScalarSector.rep_of_mem_lorentzContractionLTEightSpan`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L234).

> Every element of the surviving span is a gauge invariant.

```lean
lemma rep_of_mem_lorentzContractionLTEightSpan (w : ℕ) (g : GaugeGroupI)
    {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ lorentzContractionLTEightSpan w) : repGaugeGroupI g y = y
```

**`StandardModel.ScalarSector.repLorentz_of_mem_lorentzContractionLTEightSpan`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L244).

> Every element of the surviving span is a Lorentz invariant.

```lean
lemma repLorentz_of_mem_lorentzContractionLTEightSpan (w : ℕ) (g : SL(2,ℂ))
    {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ lorentzContractionLTEightSpan w) : repLorentzGroup g y = y
```

**`StandardModel.ScalarSector.isFixedBy_lorentzContractionLTEightSpan`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L254).

> The surviving span below weight eight is fixed pointwise by both groups.

```lean
lemma isFixedBy_lorentzContractionLTEightSpan (w : ℕ) :
    IsFixedBy (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (lorentzContractionLTEightSpan w)
```

**`StandardModel.ScalarSector.reducesInvariantsTo_lorentzContractionLTEightSpan`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L265).

> Below mass weight eight the scalar sector reduces, for the gauge and Lorentz groups
> together, to the surviving span. The four odd weights are trivial submodules, weight two
> dies on hypercharge, weight four leaves the Higgs mass term, which the Lorentz group fixes,
> and at weight six the gauge group leaves the once-derived contractions and the Lorentz
> group nothing.

```lean
lemma reducesInvariantsTo_lorentzContractionLTEightSpan {w : ℕ} (hw0 : 0 < w) (hw : w < 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (massWeightSubmodule w)
      (lorentzContractionLTEightSpan w)
```

**`StandardModel.ScalarSector.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L291).

> The classification below mass weight eight as an equivalence, in the shape of
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`. An element of
> `massWeightSubmodule w ⊔ S` for `0 < w < 8` is fixed by both groups exactly when it is an
> element of the surviving span up to a remainder in `S` fixed by both groups.  That span
> is the line through the Higgs mass term at weight four and trivial elsewhere, so at every
> weight but four this says `x = y`, as in the gauge and Yukawa sectors.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ lorentzContractionLTEightSpan w
```

**`StandardModel.ScalarSector.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean#L308).

> The same classification without the existential. Below mass weight eight an element of
> `massWeightSubmodule w ⊔ S` fixed by both groups is an element of the surviving span
> joined with `S` fixed by both groups, and conversely.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ (x ∈ lorentzContractionLTEightSpan w ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [The gauge weight decomposition of the Higgs mass-weight submodules](localfieldalgebra-scalarsector-massweight-gaugew.md)

## Proof depends on

- [The complexified Lorentz group acting on Weyl tensors](../../../relativity/bispinors/complexifiedaction.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimLTEight.lean)
