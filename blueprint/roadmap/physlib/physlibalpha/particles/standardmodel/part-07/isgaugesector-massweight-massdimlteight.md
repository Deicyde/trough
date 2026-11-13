---
declaration: module
origin: cited
lean: StandardModel.IsGaugeSector.F_mem_iSup_span_coord, StandardModel.IsGaugeSector.sum_cov_one, StandardModel.IsGaugeSector.sum_cov_three, StandardModel.IsGaugeSector.isLorentzCovariant_F_underived, StandardModel.IsGaugeSector.isLorentzCovariant_F_deriv_one, StandardModel.IsGaugeSector.ofComponents_metric_eq_zero_of_antisymm, StandardModel.IsGaugeSector.mem_of_lorentz_invariant_biSup_rankTwo_span, StandardModel.IsGaugeSector.mem_of_lorentz_invariant_biSup_rankThree_span
statement: formalized
proof: formalized
---

# The invariants below mass weight eight (IsGaugeSector/MassWeight/MassDimLTEight)

The module `PhyslibAlpha.Particles.StandardModel.IsGaugeSector.MassWeight.MassDimLTEight`, [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean): 18 declarations, 18 with a docstring.

## i. Overview

> Mass weight eight is the first weight of the gauge sector carrying a gauge and Lorentz
> invariant. Below it there is nothing: the odd weights and weight two are trivial
> submodules, weight four is a single underived field strength and weight six a single
> once-derived one, and neither of those two carries an invariant.
>
> Weight four fails on parity of a different kind. An underived field strength carries two
> covector indices and one adjoint index, so at a fixed gauge direction it is a bi-Lorentz
> tensor, whose only invariant contraction is the metric trace. That trace vanishes, the
> metric being symmetric in the pair of indices in which `IsGaugeSector.F_antisymm` says
> the field strength is antisymmetric. Weight six fails on counting: a once-derived field
> strength carries three covector indices, and three indices admit no invariant contraction
> at all, the metric tying two and the Levi-Civita symbol four.
>
> Neither argument needs the gauge group. The vanishing at weight four holds at every gauge
> direction separately, the colour and isospin ones included, so no appeal to
> `IsSU3Adjoint` or `IsSU2Adjoint` is required and Lorentz invariance alone does the work.
> What the gauge algebra does contribute is finiteness: a field-strength symbol is
> evaluated on a covector of the gauge algebra, and expanding that covector in the dual of
> the standard basis writes each derivative submodule inside a finite join of Lorentz
> spans, one for each of the twelve basis directions, which is what the peeling arguments
> consume.
>
>
> The final statement `mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff`
> needs `0 < w` as well as `w < 8`: at `w = 0` the mass-weight submodule contains the
> scalars, so `1` is an invariant of weight zero lying in no `S`.

## ii. Key results

> - `mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff` : the classification below
>   mass weight eight as an equivalence, in the shape of
>   `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`: an element of
>   `massWeightSubmodule w ⊔ S` for `0 < w < 8` is fixed by both groups exactly when it is itself an
>   element of `S` fixed by both groups

## iv. References

> * None.

## A. The symbols on the standard basis of the gauge algebra

> The gauge algebra is finite dimensional, so a covector on it is the combination of the
> coordinates of the standard basis with its own values on that basis. A field-strength
> symbol evaluated on an arbitrary covector is therefore a combination of the twelve
> symbols evaluated on those coordinates.

**`StandardModel.IsGaugeSector.F_mem_iSup_span_coord`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L102).

> A field-strength symbol lies in the span of the twelve symbols evaluated on the
> coordinates of the standard basis of the gauge algebra.

```lean
lemma F_mem_iSup_span_coord {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    F l μ ν φ ∈ ⨆ c : Fin 8 ⊕ Fin 3 ⊕ Fin 1,
      ℂ ∙ F l μ ν (GaugeAlgebra.stdBasis.coord c)
```

## B. Sums over tuples of covector indices

> A Lorentz family is indexed by a tuple of covector indices, while the transformation law
> of `IsGaugeSector` presents its sums one index at a time. These two lemmas, with
> `Lorentz.sum_pi_fin_two` for two indices, turn a sum over tuples into an iterated sum and
> back.

**`StandardModel.IsGaugeSector.sum_cov_one`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L129).

> A sum over families of one covector index is a single sum.

```lean
lemma sum_cov_one {M : Type*} [AddCommMonoid M] (f : (Fin 1 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 1 → Fin 1 ⊕ Fin 3, f d = ∑ x : Fin 1 ⊕ Fin 3, f ![x]
```

**`StandardModel.IsGaugeSector.sum_cov_three`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L138).

> A sum over families of three covector indices is a triple sum.

```lean
lemma sum_cov_three {M : Type*} [AddCommMonoid M] (f : (Fin 3 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 3 → Fin 1 ⊕ Fin 3, f d
      = ∑ x : Fin 1 ⊕ Fin 3, ∑ y : Fin 1 ⊕ Fin 3, ∑ z : Fin 1 ⊕ Fin 3, f ![x, y, z]
```

## C. The field-strength symbols as Lorentz families

> An underived field-strength symbol carries two covector indices and nothing else, and a
> once-derived one carries three, its derivative slot included. Read as families indexed by
> those indices they are a bi-Lorentz and a triple Lorentz tensor, the transformation law
> of `IsGaugeSector` moving every index by the Lorentz matrix of the `SL(2,ℂ)` element.

**`StandardModel.IsGaugeSector.isLorentzCovariant_F_underived`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L168).

> An underived field-strength symbol, viewed as a family indexed by its two covector
> indices, is a bi-Lorentz tensor.

```lean
lemma isLorentzCovariant_F_underived (φ : Module.Dual ℝ GaugeAlgebra) :
    IsLorentzCovariant 2 B repLorentz
      (ofComponents fun d : Fin 2 → Fin 1 ⊕ Fin 3 => F ![] (d 0) (d 1) φ)
```

**`StandardModel.IsGaugeSector.isLorentzCovariant_F_deriv_one`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L186).

> A once-derived field-strength symbol, viewed as a family indexed by its derivative
> slot and its two covector indices, is a triple Lorentz tensor.

```lean
lemma isLorentzCovariant_F_deriv_one (φ : Module.Dual ℝ GaugeAlgebra) :
    IsLorentzCovariant 3 B repLorentz
      (ofComponents fun d : Fin 3 → Fin 1 ⊕ Fin 3 => F ![d 0] (d 1) (d 2) φ)
```

## D. The vanishing of the metric trace of an antisymmetric family

> Two covector indices admit a single invariant contraction, the metric trace, and the
> metric is diagonal, so that trace is the sum of the components on the diagonal. A family
> antisymmetric in its two indices has every diagonal component equal to its own negative,
> hence zero, and the trace vanishes with them.

**`StandardModel.IsGaugeSector.ofComponents_metric_eq_zero_of_antisymm`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L213).

> The metric trace of a bi-Lorentz family antisymmetric in its two indices vanishes:
> the metric is diagonal, and the diagonal components of such a family are zero.

```lean
lemma ofComponents_metric_eq_zero_of_antisymm {T : (Fin 2 → Fin 1 ⊕ Fin 3) → B}
    (hswap : ∀ x y : Fin 1 ⊕ Fin 3, T ![y, x] = - T ![x, y]) :
    ofComponents T RankTwo.metric = 0
```

## E. Peeling Lorentz spans off a stable submodule

> Both classifications come in a form relative to a Lorentz-stable submodule `S`: an
> invariant of the span of a family together with `S` is a contraction of the family up to
> a remainder in `S`. When the contraction vanishes, or when there is none, the span of the
> family reduces to `⊥`, and the invariant lies in `S` outright. The spans themselves are
> Lorentz stable, so `ReducesInvariantsTo.biSup` combines these reductions over a finite
> join of them.

**`StandardModel.IsGaugeSector.mem_of_lorentz_invariant_biSup_rankTwo_span`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L249).

> A finite join of the spans of bi-Lorentz families with vanishing metric traces carries
> no Lorentz invariant modulo a Lorentz-stable submodule: a Lorentz invariant of the join
> together with `S` lies in `S`. Each span reduces to the line through its metric
> contraction, which is zero, and `ReducesInvariantsTo.biSup` combines the reductions.

```lean
lemma mem_of_lorentz_invariant_biSup_rankTwo_span {ι : Type} [DecidableEq ι]
    {T : ι → (Fin 2 → Fin 1 ⊕ Fin 3) → B}
    (hT : ∀ i, IsLorentzCovariant 2 B repLorentz (ofComponents (T i)))
    (hzero : ∀ i, ofComponents (T i) RankTwo.metric = 0) (S : Submodule ℂ B)
    (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (s : Finset ι) {x : B}
    (hx : x ∈ (⨆ i ∈ s, Submodule.span ℂ (Set.range (T i))) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.IsGaugeSector.mem_of_lorentz_invariant_biSup_rankThree_span`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L266).

> A finite join of the spans of triple Lorentz families carries no Lorentz invariant
> modulo a Lorentz-stable submodule: three covector indices carry no invariant contraction
> at all, so each span reduces to `⊥`, and `ReducesInvariantsTo.biSup` combines the
> reductions.

```lean
lemma mem_of_lorentz_invariant_biSup_rankThree_span {ι : Type} [DecidableEq ι]
    {T : ι → (Fin 3 → Fin 1 ⊕ Fin 3) → B}
    (hT : ∀ i, IsLorentzCovariant 3 B repLorentz (ofComponents (T i)))
    (S : Submodule ℂ B) (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (s : Finset ι)
    {x : B} (hx : x ∈ (⨆ i ∈ s, Submodule.span ℂ (Set.range (T i))) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.IsGaugeSector.iSup_eq_biSup_univ`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L277).

> A join over a finite index type is the join over its universal finite set.

```lean
lemma iSup_eq_biSup_univ {ι : Type} [Fintype ι] (f : ι → Submodule ℂ B) :
    ⨆ i, f i = ⨆ i ∈ (Finset.univ : Finset ι), f i
```

## F. Mass weight four

> Mass weight four is the underived field strength. At each of the twelve directions of the
> standard basis of the gauge algebra it is a bi-Lorentz family, whose metric trace vanishes
> by the antisymmetry of the field strength in its two covector indices, so section E peels
> the twelve spans off and leaves nothing behind. No gauge hypothesis enters: the vanishing
> holds at the colour and isospin directions just as at the hypercharge one.

**`StandardModel.IsGaugeSector.ofComponents_F_underived_metric_eq_zero`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L295).

> The metric trace of the underived field-strength symbols at a fixed direction of the
> gauge algebra vanishes, the symbol being antisymmetric in its two covector indices.

```lean
lemma ofComponents_F_underived_metric_eq_zero (φ : Module.Dual ℝ GaugeAlgebra) :
    ofComponents (fun d : Fin 2 → Fin 1 ⊕ Fin 3 => F ![] (d 0) (d 1) φ) RankTwo.metric = 0
```

**`StandardModel.IsGaugeSector.derivSubmodule_zero_le_iSup_span`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L305).

> The underived field strengths lie in the join, over the twelve directions of the
> standard basis of the gauge algebra, of the spans of the bi-Lorentz families they
> form.

```lean
lemma derivSubmodule_zero_le_iSup_span :
    h.derivSubmodule 0 ≤ ⨆ c : Fin 8 ⊕ Fin 3 ⊕ Fin 1,
      Submodule.span ℂ (Set.range fun d : Fin 2 → Fin 1 ⊕ Fin 3 =>
        F ![] (d 0) (d 1) (GaugeAlgebra.stdBasis.coord c))
```

**`StandardModel.IsGaugeSector.mem_of_lorentz_invariant_massWeightSubmodule_four_sup`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L327).

> Mass weight four carries no Lorentz invariant modulo a Lorentz-stable submodule: a
> Lorentz invariant of `massWeightSubmodule 4 ⊔ S` lies in `S`.

```lean
lemma mem_of_lorentz_invariant_massWeightSubmodule_four_sup (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.massWeightSubmodule 4 ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## G. Mass weight six

> Mass weight six is the once-derived field strength, a triple Lorentz family at each
> direction of the standard basis. Three covector indices carry no invariant contraction at
> all, so the rank-three classification needs no antisymmetry and no gauge input either: the
> twelve spans peel off and the invariant is left in `S`.

**`StandardModel.IsGaugeSector.etaExpand_cov_one`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L351).

> A family of one covector index is the tuple of its own entry.

```lean
lemma etaExpand_cov_one (l : Fin 1 → Fin 1 ⊕ Fin 3) : ![l 0] = l
```

**`StandardModel.IsGaugeSector.derivSubmodule_one_le_iSup_span`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L360).

> The once-derived field strengths lie in the join, over the twelve directions of the
> standard basis of the gauge algebra, of the spans of the triple Lorentz families they
> form.

```lean
lemma derivSubmodule_one_le_iSup_span :
    h.derivSubmodule 1 ≤ ⨆ c : Fin 8 ⊕ Fin 3 ⊕ Fin 1,
      Submodule.span ℂ (Set.range fun d : Fin 3 → Fin 1 ⊕ Fin 3 =>
        F ![d 0] (d 1) (d 2) (GaugeAlgebra.stdBasis.coord c))
```

**`StandardModel.IsGaugeSector.mem_of_lorentz_invariant_massWeightSubmodule_six_sup`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L384).

> Mass weight six carries no Lorentz invariant modulo a Lorentz-stable submodule: a
> Lorentz invariant of `massWeightSubmodule 6 ⊔ S` lies in `S`.

```lean
lemma mem_of_lorentz_invariant_massWeightSubmodule_six_sup (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.massWeightSubmodule 6 ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## H. The classification below mass weight eight

> The seven weights between zero and eight are now settled: weights one, two, three, five
> and seven are trivial submodules, weight four is section F and weight six section G. So
> between weight zero and weight eight there is no invariant beyond what `S` already
> supplies, and the equivalence records it.
>
> The lower bound `0 < w` cannot be dropped. Weight zero contains the scalars by
> `one_le_massWeightSubmodule_zero`, and `1` is fixed by both groups, the two
> representations being multiplicative, without lying in any given `S`.

**`StandardModel.IsGaugeSector.mem_of_lorentz_invariant_massWeightSubmodule_lt_eight_sup`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L416).

> Between mass weight zero and mass weight eight there is no Lorentz invariant: a
> Lorentz invariant of `massWeightSubmodule w ⊔ S` for `0 < w < 8` lies in `S`. The five
> odd or small weights are trivial submodules, and weights four and six are sections F
> and G.

```lean
lemma mem_of_lorentz_invariant_massWeightSubmodule_lt_eight_sup (w : ℕ) (hw0 : 0 < w)
    (hw : w < 8) (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.massWeightSubmodule w ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.IsGaugeSector.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L439).

> The classification below mass weight eight as an equivalence, in the shape of
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff`: an element of
> `massWeightSubmodule w ⊔ S` for `0 < w < 8` is fixed by both groups exactly when it is
> itself an element of `S` fixed by both groups. The span of invariants that the weight
> eight statement leaves over is here the trivial one, so `x - y` lies in it exactly when
> `x = y`. Gauge stability of `S` is not needed, and neither is gauge invariance of `x`:
> the forward direction is
> `mem_of_lorentz_invariant_massWeightSubmodule_lt_eight_sup`, which uses the Lorentz
> group alone.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x = y
```

**`StandardModel.IsGaugeSector.mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean#L457).

> The same classification without the existential: below mass weight eight an element
> of `massWeightSubmodule w ⊔ S` fixed by both groups is an element of `S` fixed by both
> groups, and conversely.

```lean
lemma mem_massWeightSubmodule_lt_eight_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw0 : 0 < w) (hw : w < 8) (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

## Depends on

- [The mass-weight grading of the gauge sector](../part-06/isgaugesector-massweight-basic.md)
- [Lorentz invariants among two four-vector indices](../../../relativity/lorentzgroup/invariants-ranktwo.md)

## Proof depends on

- [Lorentz invariants of three four-vector indices](../../../relativity/lorentzgroup/invariants-rankthree.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/MassDimLTEight.lean)
