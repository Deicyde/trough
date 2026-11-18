---
declaration: module
origin: cited
lean: StandardModel.HiggsAlgebraCovRealization.sum_cov_zero, StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankOne_dotGaugeHiggs_left, StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankOne_dotGaugeHiggs_right, StandardModel.HiggsAlgebraCovRealization.dotSpan_one_zero_eq, StandardModel.HiggsAlgebraCovRealization.dotSpan_zero_one_eq, StandardModel.HiggsAlgebraCovRealization.repLorentz_dotGaugeHiggs_zero, StandardModel.HiggsAlgebraCovRealization.dotSpan_zero_zero_eq, StandardModel.HiggsAlgebraCovRealization.repLorentz_of_mem_dotSpan_zero_zero
statement: formalized
proof: formalized
---

# The Higgs invariants below mass weight eight

The module `PhyslibAlpha.Particles.StandardModel.Realization.HiggsCov.MassWeight.MassDimLTEight`, [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean): 19 declarations, 19 with a docstring.

## i. Overview

> The Higgs sector is the one sector of the Standard Model already carrying an invariant
> below mass weight eight, and it is the most familiar of all: the mass term `H† H`, of mass
> weight four.  Everything else below weight eight dies, and for three different reasons.
>
> The odd weights are trivial submodules, every Higgs tower carrying even mass weight.
> Weight two dies on hypercharge: a single Higgs symbol carries `6Y = ∓3`, so nothing at that
> weight is neutral, which is the gauge classification of
> `reducesInvariantsTo_massWeightSubmodule_two`.  Weight six dies on Lorentz counting.  Its
> gauge invariants are the isospin contractions with one derivative, `∂_μ H† H` and
> `H† ∂_μ H`, and a single covector index admits no invariant contraction at all — the metric
> ties two indices and the Levi-Civita symbol four — which is `RankOne`.
>
> Weight four survives because the Higgs is a Lorentz scalar.  Its gauge invariants are the
> multiples of `H† H`, and with no derivative slot there is no Lorentz index to contract, so
> the Lorentz group fixes the contraction outright and the whole line survives.  That is why
> the conclusion here is membership in a span rather than in `S`, unlike the gauge and Yukawa
> sectors: the surviving span is the Higgs mass term at weight four and trivial at every
> other weight below eight.
>
>
> As in the gauge sector the final statement needs `0 < w` as well as `w < 8`: at `w = 0` the
> mass-weight submodule contains the scalars, so `1` is an invariant of weight zero lying in
> no `S`.

## ii. Key results

> - `sum_cov_zero` : a sum over families of no covector indices is its single term
> - `isLorentzCovariant_rankOne_dotGaugeHiggs_left` : the isospin contraction of a once-derived Higgs
>   tower against an underived conjugate tower, read as a family indexed by its derivative slot, is a
>   Lorentz vector
> - `isLorentzCovariant_rankOne_dotGaugeHiggs_right` : the isospin contraction of an underived Higgs
>   tower against a once-derived conjugate tower is a Lorentz vector in the same way
> - `dotSpan_one_zero_eq` : the span of the isospin contractions with one derivative on the Higgs
>   tower is the span of the components of the corresponding Lorentz vector

## iv. References

> * None.

## A. Sums over the empty tuple of covector indices

> An underived tower is indexed by the empty tuple of covector indices, of which there is
> exactly one, so the Lorentz transformation law of such a tower collapses: the sum over its
> derivative indices has a single term and the product of Lorentz matrix entries over its
> slots is empty.  Both collapses are this one lemma.

**`StandardModel.HiggsAlgebraCovRealization.sum_cov_zero`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L93).

> A sum over families of no covector indices is its single term.

```lean
lemma sum_cov_zero {M : Type*} [AddCommMonoid M] (f : (Fin 0 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 0 → Fin 1 ⊕ Fin 3, f d = f ![]
```

## B. The isospin contractions with one derivative as Lorentz vectors

> At mass weight six the gauge classification leaves the isospin contractions carrying one
> derivative, on either of the two towers.  The Higgs is a Lorentz scalar, so the only
> Lorentz index such a contraction has is that derivative slot, and read as a family indexed
> by it the contraction is a Lorentz vector.  `RankOne` says that one covector index
> admits no invariant contraction, so the span of such a family reduces to `⊥`
> (`RankOne.reducesInvariantsTo_bot`); the spans are themselves stable, so
> `ReducesInvariantsTo.sup` joins the two.

**`StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankOne_dotGaugeHiggs_left`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L116).

> The isospin contraction of a once-derived Higgs tower against an underived conjugate
> tower, read as a family indexed by its derivative slot, is a Lorentz vector.

```lean
lemma isLorentzCovariant_rankOne_dotGaugeHiggs_left :
    IsLorentzCovariant 1 B repLorentz
      (ofComponents fun d : Fin 1 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs d ![])
```

**`StandardModel.HiggsAlgebraCovRealization.isLorentzCovariant_rankOne_dotGaugeHiggs_right`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L127).

> The isospin contraction of an underived Higgs tower against a once-derived conjugate
> tower is a Lorentz vector in the same way.

```lean
lemma isLorentzCovariant_rankOne_dotGaugeHiggs_right :
    IsLorentzCovariant 1 B repLorentz
      (ofComponents fun d : Fin 1 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs ![] d)
```

**`StandardModel.HiggsAlgebraCovRealization.dotSpan_one_zero_eq`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L137).

> The span of the isospin contractions with one derivative on the Higgs tower is the
> span of the components of the corresponding Lorentz vector.

```lean
lemma dotSpan_one_zero_eq :
    h.dotSpan 1 0
      = Submodule.span ℂ (Set.range fun d : Fin 1 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs d ![])
```

**`StandardModel.HiggsAlgebraCovRealization.dotSpan_zero_one_eq`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L146).

> The span of the isospin contractions with one derivative on the conjugate tower is the
> span of the components of the corresponding Lorentz vector.

```lean
lemma dotSpan_zero_one_eq :
    h.dotSpan 0 1
      = Submodule.span ℂ (Set.range fun d : Fin 1 → Fin 1 ⊕ Fin 3 => h.dotGaugeHiggs ![] d)
```

## C. The underived isospin contraction as a Lorentz scalar

> At mass weight four the gauge classification leaves the multiples of `H† H`.  An underived
> Higgs symbol carries no derivative slot, so the Lorentz group moves it by an empty product
> of Lorentz matrix entries, that is not at all, and the contraction and the whole line
> through it are fixed.  Nothing peels off here; the line is the answer.

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_dotGaugeHiggs_zero`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L167).

> The underived isospin contraction is a Lorentz scalar.

```lean
lemma repLorentz_dotGaugeHiggs_zero (g : SL(2,ℂ)) :
    repLorentz g (h.dotGaugeHiggs (![] : Fin 0 → Fin 1 ⊕ Fin 3) ![])
      = h.dotGaugeHiggs ![] ![]
```

**`StandardModel.HiggsAlgebraCovRealization.dotSpan_zero_zero_eq`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L174).

> The span of the underived isospin contractions is the line through the mass term.

```lean
lemma dotSpan_zero_zero_eq :
    h.dotSpan 0 0 = ℂ ∙ h.dotGaugeHiggs (![] : Fin 0 → Fin 1 ⊕ Fin 3) ![]
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_of_mem_dotSpan_zero_zero`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L185).

> Every element of the line through the underived isospin contraction is a Lorentz
> invariant.

```lean
lemma repLorentz_of_mem_dotSpan_zero_zero (g : SL(2,ℂ)) {y : B} (hy : y ∈ h.dotSpan 0 0) :
    repLorentz g y = y
```

**`StandardModel.HiggsAlgebraCovRealization.rep_of_mem_dotSpan`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L193).

> Every element of a span of isospin contractions is a gauge invariant.

```lean
lemma rep_of_mem_dotSpan {n m : ℕ} (g : GaugeGroupI) {y : B} (hy : y ∈ h.dotSpan n m) :
    rep g y = y
```

**`StandardModel.HiggsAlgebraCovRealization.dotSpan_zero_zero_le_massWeightSubmodule`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L199).

> The line through the underived isospin contraction lies in mass weight four.

```lean
lemma dotSpan_zero_zero_le_massWeightSubmodule :
    h.dotSpan 0 0 ≤ h.massWeightSubmodule 4
```

## D. Mass weight six

> The gauge classification leaves, at mass weight six, the two spans of once-derived isospin
> contractions (`reducesInvariantsTo_massWeightSubmodule_six`). Section B reduces each to `⊥`
> for the Lorentz group, since a single covector index carries no invariant contraction, and
> `ReducesInvariantsTo.sup` joins them: nothing is left behind.

**`StandardModel.HiggsAlgebraCovRealization.reducesInvariantsTo_dotSpan_one_zero_sup_zero_one`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L220).

> The once-derived isospin contractions reduce to `⊥` for the Lorentz group: each span is
> spanned by a Lorentz vector, and a single covector index carries no invariant.

```lean
lemma reducesInvariantsTo_dotSpan_one_zero_sup_zero_one :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (h.dotSpan 1 0 ⊔ h.dotSpan 0 1) ⊥
```

## E. The classification below mass weight eight

> The seven weights between zero and eight are now settled: weights one, three, five and
> seven are trivial submodules, weight two is killed by hypercharge, weight six by section D,
> and weight four leaves the line through the mass term.  `lorentzContractionLTEightSpan`
> records that answer as a single submodule depending on the weight, and
> `reducesInvariantsTo_lorentzContractionLTEightSpan` reduces each weight to it, so the
> statement has the shape of the weight-eight one and of the other sectors' below-eight ones,
> whose spans happen to be trivial.

**`StandardModel.HiggsAlgebraCovRealization.lorentzContractionLTEightSpan`**, a def, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L244).

> The gauge and Lorentz invariants of the Higgs sector at mass weight `w` for
> `0 < w < 8`: the line through the Higgs mass term at weight four, and nothing at any
> other weight.

```lean
noncomputable def lorentzContractionLTEightSpan
    (h : HiggsAlgebraCovRealization B rep repLorentz massWeightPoly)
    (w : ℕ) : Submodule ℂ B
```

**`StandardModel.HiggsAlgebraCovRealization.lorentzContractionLTEightSpan_le_massWeightSubmodule`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L251).

> The surviving span at weight `w` lies in the mass-weight submodule of weight `w`.

```lean
lemma lorentzContractionLTEightSpan_le_massWeightSubmodule (w : ℕ) :
    h.lorentzContractionLTEightSpan w ≤ h.massWeightSubmodule w
```

**`StandardModel.HiggsAlgebraCovRealization.rep_of_mem_lorentzContractionLTEightSpan`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L261).

> Every element of the surviving span is a gauge invariant.

```lean
lemma rep_of_mem_lorentzContractionLTEightSpan (w : ℕ) (g : GaugeGroupI) {y : B}
    (hy : y ∈ h.lorentzContractionLTEightSpan w) : rep g y = y
```

**`StandardModel.HiggsAlgebraCovRealization.repLorentz_of_mem_lorentzContractionLTEightSpan`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L271).

> Every element of the surviving span is a Lorentz invariant.

```lean
lemma repLorentz_of_mem_lorentzContractionLTEightSpan (w : ℕ) (g : SL(2,ℂ)) {y : B}
    (hy : y ∈ h.lorentzContractionLTEightSpan w) : repLorentz g y = y
```

**`StandardModel.HiggsAlgebraCovRealization.isFixedBy_lorentzContractionLTEightSpan`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L281).

> The surviving span below weight eight is fixed pointwise by both groups.

```lean
lemma isFixedBy_lorentzContractionLTEightSpan (w : ℕ) :
    IsFixedBy (gaugeLorentzMaps rep repLorentz) (h.lorentzContractionLTEightSpan w)
```

**`StandardModel.HiggsAlgebraCovRealization.reducesInvariantsTo_lorentzContractionLTEightSpan`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L293).

> Below mass weight eight the Higgs sector reduces, for the gauge and Lorentz groups
> together, to the surviving span. The four odd weights are trivial submodules, weight two
> dies on hypercharge, weight four leaves the Higgs mass term, which the Lorentz group fixes,
> and at weight six the gauge group leaves the once-derived contractions and the Lorentz
> group nothing.

```lean
lemma reducesInvariantsTo_lorentzContractionLTEightSpan {w : ℕ} (hw0 : 0 < w) (hw : w < 8) :
    ReducesInvariantsTo (gaugeLorentzMaps rep repLorentz) (h.massWeightSubmodule w)
      (h.lorentzContractionLTEightSpan w)
```

**`StandardModel.HiggsAlgebraCovRealization.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L320).

> The classification below mass weight eight as an equivalence, in the shape of
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`: an element of
> `massWeightSubmodule w ⊔ S` for `0 < w < 8` is fixed by both groups exactly when it is an
> element of the surviving span up to a remainder in `S` fixed by both groups.  That span
> is the line through the Higgs mass term at weight four and trivial elsewhere, so at every
> weight but four this says `x = y`, as in the gauge and Yukawa sectors.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, rep g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, rep g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, rep g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.lorentzContractionLTEightSpan w
```

**`StandardModel.HiggsAlgebraCovRealization.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean#L338).

> The same classification without the existential: below mass weight eight an element of
> `massWeightSubmodule w ⊔ S` fixed by both groups is an element of the surviving span
> joined with `S` fixed by both groups, and conversely.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, rep g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, rep g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ h.lorentzContractionLTEightSpan w ⊔ S ∧ (∀ g : GaugeGroupI, rep g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

## Depends on

- [Invariant reduction for the gauge and Lorentz groups](../part-01/invariantreduction.md)
- [The gauge weight decomposition of the Higgs mass-weight submodules](../part-10/realization-higgscov-massweight-gaugeweight.md)
- [Equivariant maps out of tensors with four-vector indices](../../../relativity/lorentzgroup/invariants-lorentzcovariance.md)

## Proof depends on

- [Lorentz invariants of a single four-vector index](../../../relativity/lorentzgroup/invariants-rankone.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/MassDimLTEight.lean)
