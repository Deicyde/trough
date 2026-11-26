---
declaration: module
origin: cited
lean: StandardModel.ScalarSector.isEquivariant_up_rankTwo_dotGaugeHiggs_left, StandardModel.ScalarSector.isEquivariant_up_rankTwo_dotGaugeHiggs_right, StandardModel.ScalarSector.isEquivariant_up_rankTwo_dotGaugeHiggs_mixed, StandardModel.ScalarSector.dotSpan_two_zero_eq, StandardModel.ScalarSector.dotSpan_zero_two_eq, StandardModel.ScalarSector.dotSpan_one_one_eq, StandardModel.ScalarSector.rep_liftComponents_metric, StandardModel.ScalarSector.lorentzContractionEightSpan
statement: formalized
proof: formalized
---

# The Higgs invariants of mass weight eight

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.ScalarSector.MassWeight.MassDimEight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean): 16 declarations, 16 with a docstring.

> The gauge and Lorentz invariants of the scalar sector at mass weight eight, the kinetic term,
> the two box terms and the quartic potential.

## i. Overview

> Mass weight eight is where the scalar sector says what it is for.  The gauge classification
> of `reducesInvariantsTo_massWeightSubmodule_eight` leaves four things: the isospin
> contractions carrying two derivatives on one tower or one on each, and the square of the
> underived contraction.  The Lorentz classification then contracts the derivative indices.
>
> The Higgs is a Lorentz scalar, so the only covector indices at this weight are the two
> derivative slots, and two covector indices admit exactly one invariant contraction, the
> metric trace, `RankTwo.metric`.  Contracting the mixed family gives the kinetic term
> `∂^μ H† ∂_μ H`; contracting the two families carrying both derivatives on one tower gives
> `□H† H` and `H† □H`.  The square of the underived contraction has no index to contract and
> survives as it stands as the quartic potential `(H† H)²`.
>
> So the four surviving terms are the quartic potential, the kinetic term and the two
> box terms, and `lorentzContractionEightSpan` is their span.
>
> Everything is stated modulo a submodule `S` stable under both groups, which is what lets
> the other sectors be carried along.

## ii. Key results

> - `lorentzContractionEightSpan` : the gauge and Lorentz invariants of the scalar sector at mass
>   weight eight, the two box terms `□H† H` and `H† □H`, the kinetic term `∂^μ H† ∂_μ H`, and the
>   quartic potential `(H† H)²`.
> - `reducesInvariantsTo_lorentzContractionEightSpan` : mass weight eight reduces to that span for
>   the gauge and Lorentz groups together.
> - `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff` : the classification at
>   mass weight eight as an equivalence.

## iv. References

> * None.

## A. The isospin contractions with two derivatives as bi-Lorentz tensors

> Two derivatives can sit both on the Higgs tower, both on the conjugate tower, or one on
> each.  In each case the isospin contraction is a Lorentz scalar carrying two derivative
> slots, so read as a family indexed by those two slots it is a bi-Lorentz tensor, the
> Lorentz group moving each slot by the Lorentz matrix of the `SL(2,ℂ)` element.

**`StandardModel.ScalarSector.isEquivariant_up_rankTwo_dotGaugeHiggs_left`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L84).

> Both derivatives on the Higgs tower, a bi-Lorentz tensor in the two derivative
> slots.

```lean
lemma isEquivariant_up_rankTwo_dotGaugeHiggs_left :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 2 => .up) repLorentzGroup
      (liftComponents fun d : Fin 2 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs d ![])
```

**`StandardModel.ScalarSector.isEquivariant_up_rankTwo_dotGaugeHiggs_right`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L93).

> Both derivatives on the conjugate tower, a bi-Lorentz tensor in the same way.

```lean
lemma isEquivariant_up_rankTwo_dotGaugeHiggs_right :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 2 => .up) repLorentzGroup
      (liftComponents fun d : Fin 2 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs ![] d)
```

**`StandardModel.ScalarSector.isEquivariant_up_rankTwo_dotGaugeHiggs_mixed`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L103).

> One derivative on each tower, the family whose metric contraction is the kinetic
> term.

```lean
lemma isEquivariant_up_rankTwo_dotGaugeHiggs_mixed :
    complexLorentzTensor.IsEquivariant (fun _ : Fin 2 => .up) repLorentzGroup
      (liftComponents fun d : Fin 2 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs ![d 0] ![d 1])
```

**`StandardModel.ScalarSector.dotSpan_two_zero_eq`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L116).

> The span of the isospin contractions with both derivatives on the Higgs tower is the
> span of the components of the corresponding bi-Lorentz tensor.

```lean
lemma dotSpan_two_zero_eq :
    dotSpan 2 0
      = Submodule.span ℂ (Set.range fun d : Fin 2 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs d ![])
```

**`StandardModel.ScalarSector.dotSpan_zero_two_eq`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L125).

> The span of the isospin contractions with both derivatives on the conjugate tower is
> the span of the components of the corresponding bi-Lorentz tensor.

```lean
lemma dotSpan_zero_two_eq :
    dotSpan 0 2
      = Submodule.span ℂ (Set.range fun d : Fin 2 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs ![] d)
```

**`StandardModel.ScalarSector.dotSpan_one_one_eq`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L135).

> The span of the isospin contractions with one derivative on each tower is the span of
> the components of the mixed bi-Lorentz tensor.

```lean
lemma dotSpan_one_one_eq :
    dotSpan 1 1
      = Submodule.span ℂ
        (Set.range fun d : Fin 2 → Fin 1 ⊕ Fin 3 => dotGaugeHiggs ![d 0] ![d 1])
```

## B. The metric contraction is fixed by both groups

> Two covector indices admit one invariant contraction, the metric trace, and the metric is
> carried to itself by a Lorentz matrix — that is the defining property of the Lorentz group,
> recorded as `LorentzGroup.sum_minkowskiMatrixZ_mul` — so the trace of a bi-Lorentz family is a
> Lorentz invariant, `RankTwo.metric_invariant`.  It is a gauge invariant too whenever
> the components are, and the components here are isospin contractions, which the gauge group
> fixes.

**`StandardModel.ScalarSector.rep_liftComponents_metric`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L159).

> The metric trace of a family of gauge invariants is a gauge invariant.

```lean
lemma rep_liftComponents_metric {T : (Fin 2 → Fin 1 ⊕ Fin 3) → fieldData.LocalCovFieldAlgebra}
    (hTG : ∀ (g : GaugeGroupI) (d : Fin 2 → Fin 1 ⊕ Fin 3), repGaugeGroupI g (T d) = T d)
    (g : GaugeGroupI) :
    repGaugeGroupI g (liftComponents T RankTwo.metric) = liftComponents T RankTwo.metric
```

## C. The invariants of mass weight eight

> The gauge classification reduces mass weight eight to the three spans of twice-derived
> isospin contractions and the line through the square of the underived one.  Each of the
> three spans is spanned by a bi-Lorentz tensor and reduces, for the Lorentz group, to the
> line through its metric trace (`ComplexVector.reducesInvariantsTo_span_metric`); the
> line through the square is fixed and reduces to itself.  What is left is a combination of
> the three metric traces and the square: the two box terms, the kinetic term and the quartic
> potential.

**`StandardModel.ScalarSector.lorentzContractionEightSpan`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L183).

> The gauge and Lorentz invariants of the scalar sector at mass weight eight, the two box
> terms `□H† H` and `H† □H`, the kinetic term `∂^μ H† ∂_μ H`, and the quartic potential
> `(H† H)²`.

```lean
noncomputable def lorentzContractionEightSpan :
    Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.ScalarSector.invariant_dotGaugeHiggs_sq`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L193).

> The square of the underived isospin contraction is fixed by both groups, being a
> product of two invariants and both representations are multiplicative.

```lean
lemma invariant_dotGaugeHiggs_sq :
    (∀ g : SL(2,ℂ), repLorentzGroup g (dotGaugeHiggs (![] : Fin 0 → Fin 1 ⊕ Fin 3) ![]
        * dotGaugeHiggs ![] ![])
      = dotGaugeHiggs ![] ![] * dotGaugeHiggs ![] ![])
    ∧ ∀ g : GaugeGroupI, repGaugeGroupI g (dotGaugeHiggs (![] : Fin 0 → Fin 1 ⊕ Fin 3) ![]
        * dotGaugeHiggs ![] ![])
      = dotGaugeHiggs ![] ![] * dotGaugeHiggs ![] ![]
```

## D. The span consists of invariants of mass weight eight

> The reduction of section E is one-directional, and the converse is easy:
> each of the four generators is built from isospin contractions of the right mass weight,
> which both groups fix, so the span is made of invariants of mass weight eight already.
> The metric trace inherits the mass weight of the components and both invariances from
> section B, and the square of the underived contraction is a product of two invariants of
> mass weight four.

**`StandardModel.ScalarSector.liftComponents_metric_mem_massWeightSubmodule`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L218).

> The metric trace of a family of elements of mass weight eight has mass weight
> eight.

```lean
lemma liftComponents_metric_mem_massWeightSubmodule
    {T : (Fin 2 → Fin 1 ⊕ Fin 3) → fieldData.LocalCovFieldAlgebra}
    (hT : ∀ d, T d ∈ massWeightSubmodule 8) :
    liftComponents T RankTwo.metric ∈ massWeightSubmodule 8
```

**`StandardModel.ScalarSector.lorentzContractionEightSpan_le_massWeightSubmodule`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L226).

> The weight-eight span lies in the mass-weight submodule of weight eight.

```lean
lemma lorentzContractionEightSpan_le_massWeightSubmodule :
    lorentzContractionEightSpan ≤ massWeightSubmodule 8
```

**`StandardModel.ScalarSector.rep_of_mem_lorentzContractionEightSpan`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L242).

> Every element of the weight-eight span is a gauge invariant.

```lean
lemma rep_of_mem_lorentzContractionEightSpan (g : GaugeGroupI) {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ lorentzContractionEightSpan) : repGaugeGroupI g y = y
```

**`StandardModel.ScalarSector.repLorentz_of_mem_lorentzContractionEightSpan`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L259).

> Every element of the weight-eight span is a Lorentz invariant.

```lean
lemma repLorentz_of_mem_lorentzContractionEightSpan (g : SL(2,ℂ))
    {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ lorentzContractionEightSpan) : repLorentzGroup g y = y
```

## E. The classification

> The gauge classification and the Lorentz classification compose: the first reduces mass
> weight eight to the gauge invariants of section C, the second reduces those to the span,
> and neither step needs the intermediate span to be fixed by the other group. Section D
> says the span is made of invariants of mass weight eight, which turns the reduction into
> an equivalence.

**`StandardModel.ScalarSector.isFixedBy_lorentzContractionEightSpan`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L292).

> The weight-eight span is fixed pointwise by both groups.

```lean
lemma isFixedBy_lorentzContractionEightSpan :
    IsFixedBy (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) lorentzContractionEightSpan
```

**`StandardModel.ScalarSector.reducesInvariantsTo_lorentzContractionEightSpan`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L303).

> The scalar sector at mass weight eight reduces, for the gauge and Lorentz groups
> together, to the two box terms, the kinetic term and the quartic potential. The gauge group
> leaves the isospin contractions with two derivatives and the square of the underived one;
> the Lorentz group contracts the two derivative slots of each family with the metric, and
> the square, which carries no index, is fixed.

```lean
lemma reducesInvariantsTo_lorentzContractionEightSpan :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (massWeightSubmodule 8)
      lorentzContractionEightSpan
```

**`StandardModel.ScalarSector.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean#L337).

> The gauge and Lorentz classification of mass weight eight as an equivalence. An element
> of `massWeightSubmodule 8 ⊔ S` is fixed by both groups exactly when it is a combination of
> the two box terms, the kinetic term and the quartic potential, up to a remainder in `S`
> fixed by both groups.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ lorentzContractionEightSpan
```

## Depends on

- [The gauge weight decomposition of the Higgs mass-weight submodules](localfieldalgebra-scalarsector-massweight-gaugew.md)
- [The metrics are the unique invariant tensors with two indices of one colour](../../../relativity/tensors/complextensor-metrics-basic.md)

## Proof depends on

- [The Higgs invariants below mass weight eight](localfieldalgebra-scalarsector-massweight-massdi-2.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/MassDimEight.lean)
