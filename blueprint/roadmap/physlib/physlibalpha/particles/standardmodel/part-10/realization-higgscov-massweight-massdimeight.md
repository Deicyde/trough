---
declaration: module
origin: cited
lean: StandardModel.HiggsAlgebraCovRealization.sum_cov_one, StandardModel.HiggsAlgebraCovRealization.etaExpand_cov_one, StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankTwo_dotGaugeHiggs_left, StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankTwo_dotGaugeHiggs_right, StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankTwo_dotGaugeHiggs_mixed, StandardModel.HiggsAlgebraCovRealization.dotSpan_two_zero_eq, StandardModel.HiggsAlgebraCovRealization.dotSpan_zero_two_eq, StandardModel.HiggsAlgebraCovRealization.dotSpan_one_one_eq
statement: formalized
proof: formalized
---

# The Higgs invariants of mass weight eight

The module `PhyslibAlpha.Particles.StandardModel.Realization.HiggsCov.MassWeight.MassDimEight`, [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean): 18 declarations, 18 with a docstring.

## i. Overview

> Mass weight eight is where the Higgs sector says what it is for.  The gauge classification
> of `reducesInvariantsTo_massWeightSubmodule_eight` leaves four things: the isospin
> contractions carrying two derivatives on one tower or one on each, and the square of the
> underived contraction.  The Lorentz classification then contracts the derivative indices.
>
> The Higgs is a Lorentz scalar, so the only covector indices at this weight are the two
> derivative slots, and two covector indices admit exactly one invariant contraction, the
> metric trace, which is `RankTwo`.  Contracting the mixed family gives the kinetic term
> `∂^μ H† ∂_μ H`; contracting the two families carrying both derivatives on one tower gives
> `□H† H` and `H† □H`.  The square of the underived contraction has no index to contract and
> survives as it stands: it is the quartic potential `(H† H)²`.
>
> So the four surviving terms are the quartic potential, the kinetic term and the two
> box terms, and `lorentzContractionEightSpan` is their span.
>
>
> Everything is stated modulo a submodule `S` stable under both groups, which is what lets
> the other sectors be carried along.

## ii. Key results

> - `lorentzContractionEightSpan` : the gauge and Lorentz invariants of the Higgs sector at mass
>   weight eight: the two box terms `□H† H` and `H† □H`, the kinetic term `∂^μ H† ∂_μ H`, and the
>   quartic potential `(H† H)²`

## iv. References

> * None.

## A. Sums over pairs of covector indices

> A bi-Lorentz family is indexed by a pair of covector indices, while the transformation law
> of the Higgs tower presents its sums one derivative slot at a time.  `sum_cov_one` and,
> for a pair, `Lorentz.sum_pi_fin_two` turn a sum over tuples into an iterated sum and back.

**`StandardModel.HiggsAlgebraCovRealization.sum_cov_one`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L82).

> A sum over families of one covector index is a single sum.

```lean
lemma sum_cov_one {M : Type*} [AddCommMonoid M] (f : (Fin 1 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 1 → Fin 1 ⊕ Fin 3, f d = ∑ x : Fin 1 ⊕ Fin 3, f ![x]
```

**`StandardModel.HiggsAlgebraCovRealization.etaExpand_cov_one`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L91).

> A family of one covector index is the tuple of its own entry.

```lean
lemma etaExpand_cov_one (l : Fin 1 → Fin 1 ⊕ Fin 3) : ![l 0] = l
```

## B. The isospin contractions with two derivatives as bi-Lorentz tensors

> Two derivatives can sit both on the Higgs tower, both on the conjugate tower, or one on
> each.  In each case the isospin contraction is a Lorentz scalar carrying two derivative
> slots, so read as a family indexed by those two slots it is a bi-Lorentz tensor, the
> Lorentz group moving each slot by the Lorentz matrix of the `SL(2,ℂ)` element.

**`StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankTwo_dotGaugeHiggs_left`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L110).

> Both derivatives on the Higgs tower: a bi-Lorentz tensor in the two derivative
> slots.

```lean
lemma isLorentzCovariant_rankTwo_dotGaugeHiggs_left :
    IsLorentzCovariant 2 B repLorentz
      (ofComponents fun d : Fin 2 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs d ![])
```

**`StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankTwo_dotGaugeHiggs_right`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L120).

> Both derivatives on the conjugate tower: a bi-Lorentz tensor in the same way.

```lean
lemma isLorentzCovariant_rankTwo_dotGaugeHiggs_right :
    IsLorentzCovariant 2 B repLorentz
      (ofComponents fun d : Fin 2 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs ![] d)
```

**`StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankTwo_dotGaugeHiggs_mixed`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L131).

> One derivative on each tower: the family whose metric contraction is the kinetic
> term.

```lean
lemma isLorentzCovariant_rankTwo_dotGaugeHiggs_mixed :
    IsLorentzCovariant 2 B repLorentz
      (ofComponents fun d : Fin 2 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs ![d 0] ![d 1])
```

**`StandardModel.HiggsAlgebraCovRealization.dotSpan_two_zero_eq`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L144).

> The span of the isospin contractions with both derivatives on the Higgs tower is the
> span of the components of the corresponding bi-Lorentz tensor.

```lean
lemma dotSpan_two_zero_eq :
    h.dotSpan 2 0
      = Submodule.span ℂ (Set.range fun d : Fin 2 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs d ![])
```

**`StandardModel.HiggsAlgebraCovRealization.dotSpan_zero_two_eq`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L153).

> The span of the isospin contractions with both derivatives on the conjugate tower is
> the span of the components of the corresponding bi-Lorentz tensor.

```lean
lemma dotSpan_zero_two_eq :
    h.dotSpan 0 2
      = Submodule.span ℂ (Set.range fun d : Fin 2 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs ![] d)
```

**`StandardModel.HiggsAlgebraCovRealization.dotSpan_one_one_eq`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L163).

> The span of the isospin contractions with one derivative on each tower is the span of
> the components of the mixed bi-Lorentz tensor.

```lean
lemma dotSpan_one_one_eq :
    h.dotSpan 1 1
      = Submodule.span ℂ
        (Set.range fun d : Fin 2 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs ![d 0] ![d 1])
```

## C. The metric contraction is fixed by both groups

> Two covector indices admit one invariant contraction, the metric trace, and the metric is
> carried to itself by a Lorentz matrix — that is the defining property of the Lorentz group,
> recorded as `LorentzGroup.sum_minkowskiMatrixZ_mul` — so the trace of a bi-Lorentz family is a
> Lorentz invariant, `RankTwo.metric_invariant`.  It is a gauge invariant too whenever
> the components are, and the components here are isospin contractions, which the gauge group
> fixes.

**`StandardModel.HiggsAlgebraCovRealization.rep_ofComponents_metric`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L187).

> The metric trace of a family of gauge invariants is a gauge invariant.

```lean
lemma rep_ofComponents_metric {T : (Fin 2 → Fin 1 ⊕ Fin 3) → B}
    (hTG : ∀ (g : GaugeGroupI) (d : Fin 2 → Fin 1 ⊕ Fin 3), rep g (T d) = T d)
    (g : GaugeGroupI) :
    rep g (ofComponents T RankTwo.metric) = ofComponents T RankTwo.metric
```

## D. The invariants of mass weight eight

> The gauge classification reduces mass weight eight to the three spans of twice-derived
> isospin contractions and the line through the square of the underived one.  Each of the
> three spans is spanned by a bi-Lorentz tensor and reduces, for the Lorentz group, to the
> line through its metric trace (`RankTwo.reducesInvariantsTo_span_metric`); the
> line through the square is fixed and reduces to itself.  What is left is a combination of
> the three metric traces and the square: the two box terms, the kinetic term and the quartic
> potential.

**`StandardModel.HiggsAlgebraCovRealization.lorentzContractionEightSpan`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L211).

> The gauge and Lorentz invariants of the Higgs sector at mass weight eight: the two box
> terms `□H† H` and `H† □H`, the kinetic term `∂^μ H† ∂_μ H`, and the quartic potential
> `(H† H)²`.

```lean
noncomputable def lorentzContractionEightSpan
    (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly) :
    Submodule ℂ B
```

**`StandardModel.HiggsAlgebraCovRealization.invariant_dotGaugeHiggs_sq`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L223).

> The square of the underived isospin contraction is fixed by both groups: it is a
> product of two invariants and both representations are multiplicative.

```lean
lemma invariant_dotGaugeHiggs_sq :
    (∀ g : SL(2,ℂ), repLorentz g (h.dotGaugeHiggs (![] : Fin 0 → Fin 1 ⊕ Fin 3) ![]
        * h.dotGaugeHiggs ![] ![])
      = h.dotGaugeHiggs ![] ![] * h.dotGaugeHiggs ![] ![])
    ∧ ∀ g : GaugeGroupI, rep g (h.dotGaugeHiggs (![] : Fin 0 → Fin 1 ⊕ Fin 3) ![]
        * h.dotGaugeHiggs ![] ![])
      = h.dotGaugeHiggs ![] ![] * h.dotGaugeHiggs ![] ![]
```

## E. The span consists of invariants of mass weight eight

> The reduction of section F is one-directional, and the converse is easy:
> each of the four generators is built from isospin contractions of the right mass weight,
> which both groups fix, so the span is made of invariants of mass weight eight already.
> The metric trace inherits the mass weight of the components and both invariances from
> section C, and the square of the underived contraction is a product of two invariants of
> mass weight four.

**`StandardModel.HiggsAlgebraCovRealization.ofComponents_metric_mem_massWeightSubmodule`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L249).

> The metric trace of a family of elements of mass weight eight has mass weight
> eight.

```lean
lemma ofComponents_metric_mem_massWeightSubmodule {T : (Fin 2 → Fin 1 ⊕ Fin 3) → B}
    (hT : ∀ d, T d ∈ h.massWeightSubmodule 8) :
    ofComponents T RankTwo.metric ∈ h.massWeightSubmodule 8
```

**`StandardModel.HiggsAlgebraCovRealization.lorentzContractionEightSpan_le_massWeightSubmodule`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L257).

> The weight-eight span lies in the mass-weight submodule of weight eight.

```lean
lemma lorentzContractionEightSpan_le_massWeightSubmodule :
    h.lorentzContractionEightSpan ≤ h.massWeightSubmodule 8
```

**`StandardModel.HiggsAlgebraCovRealization.rep_of_mem_lorentzContractionEightSpan`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L274).

> Every element of the weight-eight span is a gauge invariant.

```lean
lemma rep_of_mem_lorentzContractionEightSpan (g : GaugeGroupI) {y : B}
    (hy : y ∈ h.lorentzContractionEightSpan) : rep g y = y
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_of_mem_lorentzContractionEightSpan`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L292).

> Every element of the weight-eight span is a Lorentz invariant.

```lean
lemma repLorentz_of_mem_lorentzContractionEightSpan (g : SL(2,ℂ)) {y : B}
    (hy : y ∈ h.lorentzContractionEightSpan) : repLorentz g y = y
```

## F. The classification

> The gauge classification and the Lorentz classification compose: the first reduces mass
> weight eight to the gauge invariants of section D, the second reduces those to the span,
> and neither step needs the intermediate span to be fixed by the other group. Section E
> says the span is made of invariants of mass weight eight, which turns the reduction into
> an equivalence.

**`StandardModel.HiggsAlgebraCovRealization.isFixedBy_lorentzContractionEightSpan`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L325).

> The weight-eight span is fixed pointwise by both groups.

```lean
lemma isFixedBy_lorentzContractionEightSpan :
    IsFixedBy (gaugeLorentzMaps rep repLorentz) h.lorentzContractionEightSpan
```

**`StandardModel.HiggsAlgebraCovRealization.reducesInvariantsTo_lorentzContractionEightSpan`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L337).

> The Higgs sector at mass weight eight reduces, for the gauge and Lorentz groups
> together, to the two box terms, the kinetic term and the quartic potential. The gauge group
> leaves the isospin contractions with two derivatives and the square of the underived one;
> the Lorentz group contracts the two derivative slots of each family with the metric, and
> the square, which carries no index, is fixed.

```lean
lemma reducesInvariantsTo_lorentzContractionEightSpan :
    ReducesInvariantsTo (gaugeLorentzMaps rep repLorentz) (h.massWeightSubmodule 8)
      h.lorentzContractionEightSpan
```

**`StandardModel.HiggsAlgebraCovRealization.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean#L370).

> The gauge and Lorentz classification of mass weight eight as an equivalence: an element
> of `massWeightSubmodule 8 ⊔ S` is fixed by both groups exactly when it is a combination of
> the two box terms, the kinetic term and the quartic potential, up to a remainder in `S`
> fixed by both groups.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, rep g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, rep g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, rep g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.lorentzContractionEightSpan
```

## Depends on

- [Invariant reduction for the gauge and Lorentz groups](../part-01/invariantreduction.md)
- [The gauge weight decomposition of the Higgs mass-weight submodules](realization-higgscov-massweight-gaugeweight.md)
- [Lorentz invariants among two four-vector indices](../../../relativity/lorentzgroup/invariants-ranktwo.md)

## Proof depends on

- [The Higgs invariants below mass weight eight](../part-11/realization-higgscov-massweight-massdimlteight.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimEight.lean)
