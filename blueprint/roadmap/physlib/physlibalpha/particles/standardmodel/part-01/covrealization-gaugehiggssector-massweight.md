---
declaration: module
origin: cited
lean: Lorentz.IsLorentzCovariant.mul_fixed, Lorentz.ofComponents_mul_right, Lorentz.IsLorentzCovariant.mul_vector, StandardModel.mem_of_lorentz_invariant_iSup_rankTwo_span, StandardModel.mem_of_lorentz_invariant_iSup_rankThree_span, StandardModel.repLorentz_eq_self_of_mem_mul, StandardModel.repLorentz_mem_mul_of_stable, StandardModel.repLorentz_mem_of_fixed
statement: formalized
proof: formalized
---

# The gauge-Higgs invariants below mass weight nine

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.GaugeHiggsSector.MassWeight`, [PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean): 18 declarations, 18 with a docstring.

## i. Overview

> The mixed `{gauge, higgs}` sector is small, and none of it is invariant. A field-strength
> tower weighs at least four and a Higgs tower at least two, and both weights are even, so
> the sector vanishes below weight six and at every odd weight, weight seven included. What
> is left is weight six, the underived field strength against the underived Higgs, and
> weight eight: that same field strength against the weight-four Higgs terms, together with
> the once-derived field strength against the underived Higgs.
>
> None of it can carry an invariant, and the reason is an index count. The Higgs is a Lorentz
> scalar, so an underived Higgs symbol has no covector index at all and is fixed by the whole
> Lorentz group, while a once-derived one carries a single index, its derivative slot. The
> covector indices of these products are therefore those of the field strength — two when it
> is underived and three when it is once derived — plus at most one from the Higgs.
>
> Two indices admit exactly one invariant contraction, the metric trace, and it vanishes: the
> metric is symmetric in the pair of indices in which `IsGaugeSector.F_antisymm` says the
> field strength is antisymmetric. Three indices admit no invariant contraction at all, the
> metric tying two and the Levi-Civita symbol four. Weight six and the two-Higgs term of
> weight eight are of the first kind and the other two terms of weight eight of the second,
> so at no weight below nine does the sector add an invariant to what is already there.
>
> Neither count needs the gauge group, and neither needs a basis of the Higgs. The families
> being peeled are indexed by a covector of the gauge algebra together with a piece of Higgs
> material, and neither index is finite; section B peels a join over an arbitrary index type
> by passing to a finite subset of it, which is all an element of a join ever needs.
>
>
> The bound is `w < 9` rather than the gauge sector's `w < 8`, weight eight being as empty of
> invariants as the weights below it. No lower bound on `w` is needed either: the sector is
> the two-class sector of the gauge and Higgs generators, so both classes must be present
> with a non-zero weight and the scalars, which force `0 < w` in the gauge-sector statement,
> never appear.

## ii. Key results

> - `IsLorentzCovariant.mul_fixed` : multiplying a Lorentz tensor family by a Lorentz-inert element
>   gives a family of the same rank: the element rides through the transformation law untouched
> - `ofComponents_mul_right` : the map of a family multiplied on the right by an element is the map of
>   the family, multiplied by that element
> - `IsLorentzCovariant.mul_vector` : a rank-two family against a Lorentz vector is a rank-three
>   family: the two covector indices of the first factor and the single index of the second make three
> - `mem_of_lorentz_invariant_iSup_rankTwo_span` : a Lorentz invariant of a join, over an arbitrary
>   index type, of the spans of bi-Lorentz families with vanishing metric traces lies in the stable
>   submodule it is taken modulo

## iv. References

> * None.

## A. Field strengths against Lorentz-inert material

> A family transforming as a Lorentz tensor stays one when multiplied by an element the
> Lorentz group fixes, and its metric trace is multiplied by that element too. So a field
> strength against an underived Higgs is a tensor of the same two or three indices as the
> field strength alone. A once-derived Higgs contributes an index of its own, and a
> rank-two family against a Lorentz vector is a rank-three family.

**`Lorentz.IsLorentzCovariant.mul_fixed`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L96).

> Multiplying a Lorentz tensor family by a Lorentz-inert element gives a family of the
> same rank: the element rides through the transformation law untouched.

```lean
lemma IsLorentzCovariant.mul_fixed {n : ℕ}
    (hmul : ∀ (Λ : SL(2,ℂ)) (x y : B), repLorentz Λ (x * y) = repLorentz Λ x * repLorentz Λ y)
    {T : (Fin n → Fin 1 ⊕ Fin 3) → B} (hT : IsLorentzCovariant n B repLorentz (ofComponents T))
    {y : B} (hy : ∀ g : SL(2,ℂ), repLorentz g y = y) :
    IsLorentzCovariant n B repLorentz (ofComponents fun d => T d * y)
```

**`Lorentz.ofComponents_mul_right`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L107).

> The map of a family multiplied on the right by an element is the map of the family,
> multiplied by that element.

```lean
lemma ofComponents_mul_right {n : ℕ} (T : (Fin n → Fin 1 ⊕ Fin 3) → B) (y : B)
    (t : ℂT(fun _ : Fin n => Color.up)) :
    ofComponents (fun d => T d * y) t = ofComponents T t * y
```

**`Lorentz.IsLorentzCovariant.mul_vector`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L114).

> A rank-two family against a Lorentz vector is a rank-three family: the two covector
> indices of the first factor and the single index of the second make three.

```lean
lemma IsLorentzCovariant.mul_vector
    (hmul : ∀ (Λ : SL(2,ℂ)) (x y : B), repLorentz Λ (x * y) = repLorentz Λ x * repLorentz Λ y)
    {T : (Fin 2 → Fin 1 ⊕ Fin 3) → B} (hT : IsLorentzCovariant 2 B repLorentz (ofComponents T))
    {U : (Fin 1 ⊕ Fin 3) → B}
    (hU : ∀ (g : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3), repLorentz g (U μ)
      = ∑ ν : Fin 1 ⊕ Fin 3, (((SL2C.toLorentzGroup g).1 ν μ : ℝ) : ℂ) • U ν) :
    IsLorentzCovariant 3 B repLorentz
      (ofComponents fun d : Fin 3 → Fin 1 ⊕ Fin 3 => T ![d 0, d 1] * U (d 2))
```

## B. Peeling a join over an arbitrary index

> The gauge sector combines the reductions of a join of spans indexed by a finite set, which
> is what its twelve directions of the gauge algebra need. Here the families are indexed by a
> covector of the gauge algebra together with a piece of Higgs material, and neither index is
> finite. Nothing is lost: an element of a join lies in the join over finitely many of the
> summands, so `ReducesInvariantsTo.iSup` combines the reductions over the whole join, by
> way of `ReducesInvariantsTo.iSup_of_biSup`. The rest of the section collects the
> stability and the inertness of products and joins that section E consumes.

**`StandardModel.mem_of_lorentz_invariant_iSup_rankTwo_span`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L162).

> A Lorentz invariant of a join, over an arbitrary index type, of the spans of
> bi-Lorentz families with vanishing metric traces lies in the stable submodule it is taken
> modulo. Each span reduces to the line through its metric contraction, which is zero; the
> reductions combine over every finite set of indices, and so over the whole join.

```lean
lemma mem_of_lorentz_invariant_iSup_rankTwo_span {ι : Type}
    {T : ι → (Fin 2 → Fin 1 ⊕ Fin 3) → B}
    (hT : ∀ i, IsLorentzCovariant 2 B repLorentz (ofComponents (T i)))
    (hzero : ∀ i, ofComponents (T i) RankTwo.metric = 0) (S : Submodule ℂ B)
    (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ (⨆ i, Submodule.span ℂ (Set.range (T i))) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.mem_of_lorentz_invariant_iSup_rankThree_span`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L179).

> A Lorentz invariant of a join, over an arbitrary index type, of the spans of triple
> Lorentz families lies in the stable submodule it is taken modulo: three covector indices
> admit no invariant contraction at all, so each span reduces to `⊥`, and the reductions
> combine over every finite set of indices, and so over the whole join.

```lean
lemma mem_of_lorentz_invariant_iSup_rankThree_span {ι : Type}
    {T : ι → (Fin 3 → Fin 1 ⊕ Fin 3) → B}
    (hT : ∀ i, IsLorentzCovariant 3 B repLorentz (ofComponents (T i)))
    (S : Submodule ℂ B) (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ (⨆ i, Submodule.span ℂ (Set.range (T i))) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.repLorentz_eq_self_of_mem_mul`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L190).

> A product of two pointwise Lorentz-inert submodules is pointwise Lorentz inert.

```lean
lemma repLorentz_eq_self_of_mem_mul
    (hmul : ∀ (Λ : SL(2,ℂ)) (x y : B), repLorentz Λ (x * y) = repLorentz Λ x * repLorentz Λ y)
    {V W : Submodule ℂ B} (hV : ∀ (g : SL(2,ℂ)), ∀ y ∈ V, repLorentz g y = y)
    (hW : ∀ (g : SL(2,ℂ)), ∀ y ∈ W, repLorentz g y = y) (g : SL(2,ℂ)) :
    ∀ y ∈ V * W, repLorentz g y = y
```

**`StandardModel.repLorentz_mem_mul_of_stable`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L201).

> A product of two Lorentz-stable submodules is Lorentz stable.

```lean
lemma repLorentz_mem_mul_of_stable
    (hmul : ∀ (Λ : SL(2,ℂ)) (x y : B), repLorentz Λ (x * y) = repLorentz Λ x * repLorentz Λ y)
    {V W : Submodule ℂ B} (hV : ∀ (g : SL(2,ℂ)), ∀ y ∈ V, repLorentz g y ∈ V)
    (hW : ∀ (g : SL(2,ℂ)), ∀ y ∈ W, repLorentz g y ∈ W) (g : SL(2,ℂ)) :
    ∀ y ∈ V * W, repLorentz g y ∈ V * W
```

**`StandardModel.repLorentz_mem_of_fixed`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L214).

> A pointwise Lorentz-inert submodule is Lorentz stable.

```lean
lemma repLorentz_mem_of_fixed {V : Submodule ℂ B}
    (hV : ∀ (g : SL(2,ℂ)), ∀ y ∈ V, repLorentz g y = y) (g : SL(2,ℂ)) :
    ∀ y ∈ V, repLorentz g y ∈ V
```

**`StandardModel.repLorentz_mem_sup_of_stable`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L219).

> A join of two Lorentz-stable submodules is Lorentz stable.

```lean
lemma repLorentz_mem_sup_of_stable {V W : Submodule ℂ B}
    (hV : ∀ (g : SL(2,ℂ)), ∀ y ∈ V, repLorentz g y ∈ V)
    (hW : ∀ (g : SL(2,ℂ)), ∀ y ∈ W, repLorentz g y ∈ W) (g : SL(2,ℂ)) :
    ∀ y ∈ V ⊔ W, repLorentz g y ∈ V ⊔ W
```

## C. The underived Higgs is Lorentz inert

> The Higgs is a Lorentz scalar, and an underived symbol has no derivative slot for the
> Lorentz matrix to act on, so it is fixed outright — and with it every element of the
> submodule the underived symbols span.

**`StandardModel.CovAlgebraRealization.repLorentz_eq_self_of_mem_higgs_derivSubmodule_zero`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L252).

> The underived Higgs and conjugate-Higgs symbols are Lorentz scalars with no derivative
> slot to rotate, so every element of the weight-two Higgs submodule is fixed by the whole
> Lorentz group.

```lean
lemma repLorentz_eq_self_of_mem_higgs_derivSubmodule_zero (g : SL(2,ℂ)) {y : B}
    (hy : y ∈ h.isHiggsSector.derivSubmodule 0) : repLorentz g y = y
```

## D. Field strengths against Higgs material

> Three products have to be classified. An underived field strength against inert material is
> a bi-Lorentz family whose metric trace vanishes with the antisymmetry of the field strength;
> a once-derived one against inert material is a triple Lorentz family; and an underived one
> against a once-derived Higgs is a triple Lorentz family as well, the Higgs supplying the
> third index. The last is the only one in which a Higgs index moves at all.

**`StandardModel.CovAlgebraRealization.mem_of_lorentz_invariant_derivSubmodule_zero_mul_fixed_sup`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L293).

> An underived field strength against Lorentz-inert material carries no Lorentz
> invariant modulo a Lorentz-stable submodule.

```lean
lemma mem_of_lorentz_invariant_derivSubmodule_zero_mul_fixed_sup (C : Submodule ℂ B)
    (hC : ∀ (g : SL(2,ℂ)), ∀ y ∈ C, repLorentz g y = y) (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.isGaugeSector.derivSubmodule 0 * C ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.CovAlgebraRealization.mem_of_lorentz_invariant_derivSubmodule_one_mul_fixed_sup`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L325).

> A once-derived field strength against Lorentz-inert material carries no Lorentz
> invariant modulo a Lorentz-stable submodule.

```lean
lemma mem_of_lorentz_invariant_derivSubmodule_one_mul_fixed_sup (C : Submodule ℂ B)
    (hC : ∀ (g : SL(2,ℂ)), ∀ y ∈ C, repLorentz g y = y) (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.isGaugeSector.derivSubmodule 1 * C ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.CovAlgebraRealization.mem_of_lorentz_invariant_derivSubmodule_zero_mul_higgs_one_sup`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L352).

> An underived field strength against a once-derived Higgs carries no Lorentz invariant
> modulo a Lorentz-stable submodule: three covector indices admit no contraction.

```lean
lemma mem_of_lorentz_invariant_derivSubmodule_zero_mul_higgs_one_sup (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.isGaugeSector.derivSubmodule 0 * h.isHiggsSector.derivSubmodule 1 ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## E. Mass weights six and eight

> Weight six is a single product and section D settles it outright. Weight eight is a join of
> three, and they are peeled one at a time, the two not yet peeled joining the error term —
> which asks that they be Lorentz stable. The gauge and Higgs derivative submodules are, and
> so are their products and joins.

**`StandardModel.CovAlgebraRealization.mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_six_sup`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L434).

> Mass weight six carries no Lorentz invariant modulo a Lorentz-stable submodule: a
> Lorentz invariant of `sectorMassWeight {gauge, higgs} 6 ⊔ S` lies in `S`. The weight is
> the underived field strength against the underived Higgs, whose two covector indices are
> contracted only by the metric, and that trace vanishes.

```lean
lemma mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_six_sup (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} 6 ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.CovAlgebraRealization.mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_eight_sup`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L447).

> Mass weight eight carries no Lorentz invariant modulo a Lorentz-stable submodule: a
> Lorentz invariant of `sectorMassWeight {gauge, higgs} 8 ⊔ S` lies in `S`. The three
> products making up the weight are peeled off one at a time, the two carrying three
> covector indices by the absence of any contraction and the one carrying two by the
> vanishing of the metric trace.

```lean
lemma mem_of_lorentz_invariant_sectorMassWeight_gauge_higgs_eight_sup (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} 8 ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## F. The classification below mass weight nine

> The nine weights below nine are now settled: the sector vanishes below weight six and at
> weight seven, and weights six and eight are section E. So below weight nine the gauge-Higgs
> sector supplies no invariant beyond what `S` already carries, and the equivalences record it
> in the shape the other sectors carry, so that all of them can be combined.

**`StandardModel.CovAlgebraRealization.mem_of_invariant_sectorMassWeight_gauge_higgs_lt_nine_sup`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L486).

> Below mass weight nine the gauge-Higgs sector carries no Lorentz invariant: a Lorentz
> invariant of `sectorMassWeight {gauge, higgs} w ⊔ S` for `w < 9` lies in `S`. Weights
> below six and weight seven are trivial submodules, and weights six and eight are the two
> index counts.

```lean
lemma mem_of_invariant_sectorMassWeight_gauge_higgs_lt_nine_sup (w : ℕ) (hw : w < 9)
    (S : Submodule ℂ B) (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} w ⊔ S)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.CovAlgebraRealization.mem_sectorMassWeight_gauge_higgs_lt_nine_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L502).

> The classification below mass weight nine as an equivalence, in the shape of the gauge-
> and Yukawa-sector statements: an element of `sectorMassWeight {gauge, higgs} w ⊔ S` for
> `w < 9` is fixed by both groups exactly when it is itself an element of `S` fixed by both
> groups. Gauge stability of `S` is not needed, and neither is gauge invariance of `x`: the
> forward direction is the index count, which uses the Lorentz group alone.

```lean
lemma mem_sectorMassWeight_gauge_higgs_lt_nine_sup_and_gauge_lorentz_invariant_iff
    (w : ℕ) (hw : w < 9) (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGauge g x = x) ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x = y
```

**`StandardModel.CovAlgebraRealization.mem_sectorMassWeight_gauge_higgs_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 520](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean#L520).

> The same classification without the existential: below mass weight nine an element of
> `sectorMassWeight {gauge, higgs} w ⊔ S` fixed by both groups is an element of `S` fixed by
> both groups, and conversely.

```lean
lemma mem_sectorMassWeight_gauge_higgs_lt_nine_sup_and_gauge_lorentz_invariant_iff_mem
    (w : ℕ) (hw : w < 9) (S : Submodule ℂ B)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} w ⊔ S
        ∧ (∀ g : GaugeGroupI, repGauge g x = x) ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

## Depends on

- [The sectors of the field algebra](covrealization-sectors.md)
- [The derivative submodules of the Higgs sector](../part-10/realization-higgscov-derivsubmodule-basic.md)
- [Lorentz invariants among two four-vector indices](../../../relativity/lorentzgroup/invariants-ranktwo.md)

## Proof depends on

- [The mixed gauge-Higgs sector](covrealization-gaugehiggssector-basic.md)
- [The invariants below mass weight eight](../part-07/isgaugesector-massweight-massdimlteight.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/GaugeHiggsSector/MassWeight.lean)
