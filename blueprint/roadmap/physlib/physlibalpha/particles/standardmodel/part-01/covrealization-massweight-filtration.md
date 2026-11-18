---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.massWeightSubmoduleLE, StandardModel.CovAlgebraRealization.massWeightSubmodule_le_massWeightSubmoduleLE, StandardModel.CovAlgebraRealization.mem_massWeightSubmoduleLE, StandardModel.CovAlgebraRealization.massWeightSubmoduleLE_le, StandardModel.CovAlgebraRealization.massWeightSubmoduleLE_mono, StandardModel.CovAlgebraRealization.massWeightSubmoduleLE_eq_iSup, StandardModel.CovAlgebraRealization.isStableUnder_massWeightSubmoduleLE, StandardModel.CovAlgebraRealization.massWeightSubmodule_zero
statement: formalized
proof: formalized
---

# The mass-weight filtration and the constant term

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.MassWeight.Filtration`, [PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean): 24 declarations, 24 with a docstring.

## i. Overview

> The grading of the field algebra by mass weight answers one weight at a time. A
> Lagrangian is not graded: it is a sum of terms of every weight up to a cut-off, and the
> object that holds such a sum is the filtration `massWeightSubmoduleLE w`, the join of the
> weight pieces of weight at most `w`.
>
> Passing from the grading to the filtration adds exactly one thing, and it is the thing the
> graded statement had to exclude. `Invariants.lean` classifies the invariants of
> `massWeightSubmodule w` for `0 < w ≤ 8`, and the lower bound is not an artefact: at weight
> zero the field algebra contains the scalars, which are fixed by both groups and lie in no
> given `S`, so no classification into a span plus a remainder in `S` can hold there. The
> filtration contains weight zero, so the scalars have to be met rather than avoided — and
> they are a genuine invariant, the constant term of mass dimension zero, the cosmological
> term.
>
> Section B settles what the weight-zero piece is: the only word of total weight zero is the
> empty word, every generator carrying positive weight, so `massWeightSubmodule 0` is exactly
> the scalars, and the unit is fixed by both groups because both act by algebra maps.
>
> The classification then runs as it does for the grading. `ReducesInvariantsTo` is closed under
> joins in its source, and the filtration is a join: each weight from one to eight reduces to
> the Standard-Model span of that weight by `reducesInvariantsTo_massWeightSubmodule`, weight
> zero reduces to itself, and the join of the nine is a reduction of the filtration. No independence
> of the sectors, and none of the weights, is used anywhere.
>
> The answer at bound eight is spanned by the constant term, the Higgs mass term `H† H`, and
> the dimension-four span of `Invariants.lean`, with the same scope: formal expressions,
> spanning generators, and no quotient by total derivatives or the equations of motion.

## ii. Key results

> - `massWeightSubmoduleLE` : the elements of the field algebra of mass weight at most `w`: the join
>   of the mass-weight submodules of weight `0` through `w`
> - `massWeightSubmodule_le_massWeightSubmoduleLE` : each graded piece of weight at most `w` sits
>   inside the filtration at `w`
> - `mem_massWeightSubmoduleLE` : an element of a graded piece of weight at most `w` lies in the
>   filtration at `w`
> - `massWeightSubmoduleLE_le` : a submodule containing every graded piece of weight at most `w`
>   contains the filtration at `w`: the join is taken over exactly those pieces

## iv. References

> * None.

## A. The mass-weight filtration

**`StandardModel.CovAlgebraRealization.massWeightSubmoduleLE`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L91).

> The elements of the field algebra of mass weight at most `w`: the join of the
> mass-weight submodules of weight `0` through `w`. This is where a Lagrangian lives, a
> sum of terms of every mass dimension up to a cut-off rather than of a single one.

```lean
noncomputable def massWeightSubmoduleLE (w : ℕ) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.massWeightSubmodule_le_massWeightSubmoduleLE`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L95).

> Each graded piece of weight at most `w` sits inside the filtration at `w`.

```lean
lemma massWeightSubmodule_le_massWeightSubmoduleLE {k w : ℕ} (hk : k ≤ w) :
    h.massWeightSubmodule k ≤ h.massWeightSubmoduleLE w
```

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmoduleLE`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L100).

> An element of a graded piece of weight at most `w` lies in the filtration at `w`.

```lean
lemma mem_massWeightSubmoduleLE {k w : ℕ} (hk : k ≤ w) {x : B}
    (hx : x ∈ h.massWeightSubmodule k) : x ∈ h.massWeightSubmoduleLE w
```

**`StandardModel.CovAlgebraRealization.massWeightSubmoduleLE_le`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L106).

> A submodule containing every graded piece of weight at most `w` contains the
> filtration at `w`: the join is taken over exactly those pieces.

```lean
lemma massWeightSubmoduleLE_le {w : ℕ} {V : Submodule ℂ B}
    (hV : ∀ k ≤ w, h.massWeightSubmodule k ≤ V) : h.massWeightSubmoduleLE w ≤ V
```

**`StandardModel.CovAlgebraRealization.massWeightSubmoduleLE_mono`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L111).

> The filtration grows with the bound.

```lean
lemma massWeightSubmoduleLE_mono {w w' : ℕ} (hw : w ≤ w') :
    h.massWeightSubmoduleLE w ≤ h.massWeightSubmoduleLE w'
```

**`StandardModel.CovAlgebraRealization.massWeightSubmoduleLE_eq_iSup`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L118).

> The filtration as a join over a finite index type, which is the form in which the
> reduction of a join consumes it.

```lean
lemma massWeightSubmoduleLE_eq_iSup (w : ℕ) :
    h.massWeightSubmoduleLE w = ⨆ k : Fin (w + 1), h.massWeightSubmodule (k : ℕ)
```

**`StandardModel.CovAlgebraRealization.isStableUnder_massWeightSubmoduleLE`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L128).

> The filtration is carried into itself by both groups: each graded piece is, and a
> join of stable submodules is stable.

```lean
lemma isStableUnder_massWeightSubmoduleLE (w : ℕ) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.massWeightSubmoduleLE w)
```

## B. The constant term at weight zero

**`StandardModel.CovAlgebraRealization.massWeightSubmodule_zero`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L145).

> The weight-zero part of the field algebra is the scalars. Every covariant generator
> carries positive mass weight, so the only word of total weight zero is the empty one,
> whose value is the unit. This is the constant term of the Lagrangian, of mass dimension
> zero — the cosmological term.

```lean
lemma massWeightSubmodule_zero : h.massWeightSubmodule 0 = 1
```

**`StandardModel.CovAlgebraRealization.isFixedBy_massWeightSubmodule_zero`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L160).

> The scalars are fixed by both groups: each acts by an algebra map, so each fixes the
> unit. This is what makes the constant term an invariant, and it is what the backward
> direction of the classification needs of the weight-zero part of the span.

```lean
lemma isFixedBy_massWeightSubmodule_zero :
    IsFixedBy (gaugeLorentzMaps repGauge repLorentz) (h.massWeightSubmodule 0)
```

## C. The span of the filtration

**`StandardModel.CovAlgebraRealization.standardModelSpanLE`**, a def, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L177).

> The gauge- and Lorentz-invariant content of the Standard Model up to mass weight `w`:
> the weight-zero part of the field algebra, which is the constant term, joined with the
> Standard-Model span of every weight up to `w`.

```lean
noncomputable def standardModelSpanLE (w : ℕ) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.massWeightSubmodule_zero_le_standardModelSpanLE`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L181).

> The constant term lies in the span of the filtration, at every bound.

```lean
lemma massWeightSubmodule_zero_le_standardModelSpanLE (w : ℕ) :
    h.massWeightSubmodule 0 ≤ h.standardModelSpanLE w
```

**`StandardModel.CovAlgebraRealization.standardModelSpan_le_standardModelSpanLE`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L187).

> The graded span of a weight at most `w` lies in the span of the filtration at `w`.

```lean
lemma standardModelSpan_le_standardModelSpanLE {k w : ℕ} (hk : k ≤ w) :
    h.standardModelSpan k ≤ h.standardModelSpanLE w
```

**`StandardModel.CovAlgebraRealization.standardModelSpanLE_le_massWeightSubmoduleLE`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L194).

> The span of the filtration at `w` has mass weight at most `w`: the constant term has
> weight zero and each graded span has its own weight.

```lean
lemma standardModelSpanLE_le_massWeightSubmoduleLE (w : ℕ) :
    h.standardModelSpanLE w ≤ h.massWeightSubmoduleLE w
```

**`StandardModel.CovAlgebraRealization.isFixedBy_standardModelSpanLE`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L204).

> The span of the filtration is fixed pointwise by the gauge and Lorentz groups
> together. At positive weight this is the fixedness of the graded spans; at weight zero
> it is the fixedness of the unit, and that is the only new content of the filtration.

```lean
lemma isFixedBy_standardModelSpanLE (w : ℕ) :
    IsFixedBy (gaugeLorentzMaps repGauge repLorentz) (h.standardModelSpanLE w)
```

**`StandardModel.CovAlgebraRealization.repGauge_of_mem_standardModelSpanLE`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L210).

> Every element of the span of the filtration is a gauge invariant.

```lean
lemma repGauge_of_mem_standardModelSpanLE (w : ℕ) (g : GaugeGroupI) {y : B}
    (hy : y ∈ h.standardModelSpanLE w) : repGauge g y = y
```

**`StandardModel.CovAlgebraRealization.repLorentz_of_mem_standardModelSpanLE`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L215).

> Every element of the span of the filtration is a Lorentz invariant.

```lean
lemma repLorentz_of_mem_standardModelSpanLE (w : ℕ) (Λ : SL(2,ℂ)) {y : B}
    (hy : y ∈ h.standardModelSpanLE w) : repLorentz Λ y = y
```

**`StandardModel.CovAlgebraRealization.standardModelSpanLE_eight`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L223).

> The span of the filtration at bound eight in reduced form. Of the nine graded spans
> only two are non-trivial, the Higgs mass term at weight four and the dimension-four
> Lagrangian at weight eight, so what survives up to mass dimension four is the constant
> term, the Higgs mass term, and the Lagrangian.

```lean
lemma standardModelSpanLE_eight :
    h.standardModelSpanLE 8 = (1 : Submodule ℂ B) ⊔ (h.isHiggsSector.dotSpan 0 0
      ⊔ (h.isGaugeSector.lorentzContractionEightSpan
            ⊔ h.isHiggsSector.lorentzContractionEightSpan
          ⊔ (h.isFermionSector.kineticSpan ⊔ h.yukawaSpan)))
```

## D. Reducing the filtration

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_massWeightSubmoduleLE`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L256).

> The filtration reduces to its span, at every bound up to eight. The filtration is a
> join of the graded pieces, each of them stable under both groups, and `ReducesInvariantsTo` is
> closed under joins in its source: the weights are taken one at a time, each in turn joining the
> error term of the others. At positive weight the graded reduction of `Invariants.lean` is
> used; at weight zero a submodule reduces to itself, the constant term being carried in the
> span.

```lean
lemma reducesInvariantsTo_massWeightSubmoduleLE {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.massWeightSubmoduleLE w)
      (h.standardModelSpanLE w)
```

## E. The classification up to mass dimension four

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmoduleLE_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L283).

> The classification of the Standard Model up to mass weight `w ≤ 8` as an equivalence,
> in the shape every sector uses: an element of `massWeightSubmoduleLE w ⊔ S`, with `S`
> stable under both groups, is fixed by both groups exactly when it is a combination of
> the constant term and the Standard-Model terms of weight at most `w`, up to a remainder
> in `S` fixed by both groups.

```lean
lemma mem_massWeightSubmoduleLE_sup_and_gauge_lorentz_invariant_iff (w : ℕ) (hw : w ≤ 8)
    (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmoduleLE w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.standardModelSpanLE w
```

**`StandardModel.CovAlgebraRealization.exists_mem_standardModelSpanLE_of_gauge_and_lorentz_invariant`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L302).

> The gauge and Lorentz invariants of mass weight at most `w`, for `w ≤ 8`, modulo a
> submodule `S` stable under both groups: such an invariant is a combination of the
> constant term and the Standard-Model terms of weight at most `w`, plus a remainder in
> `S`, and the remainder is fixed by both groups as well, being the difference of two
> invariants.

```lean
lemma exists_mem_standardModelSpanLE_of_gauge_and_lorentz_invariant (w : ℕ) (hw : w ≤ 8)
    (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.massWeightSubmoduleLE w ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGauge g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) :
    ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
      ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
      ∧ x - y ∈ h.standardModelSpanLE w
```

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmoduleLE_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L318).

> The same classification without the existential: at every bound up to eight an element
> of `massWeightSubmoduleLE w ⊔ S` fixed by both groups is an element of the span of the
> filtration joined with `S` fixed by both groups, and conversely.

```lean
lemma mem_massWeightSubmoduleLE_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw : w ≤ 8) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmoduleLE w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ h.standardModelSpanLE w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

## F. The Standard Model Lagrangian with its constant and mass terms

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L342).

> The classification at bound eight, that is at mass dimension at most four, as an
> equivalence: an element of `massWeightSubmoduleLE 8 ⊔ S`, with `S` stable under both
> groups, is fixed by both groups exactly when it lies in the span of the filtration up to
> a remainder in `S` fixed by both groups.

```lean
lemma mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmoduleLE 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.standardModelSpanLE 8
```

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L353).

> The same at bound eight without the existential.

```lean
lemma mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff_mem
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmoduleLE 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ h.standardModelSpanLE 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean#L376).

> The invariant content of the Standard Model up to mass dimension four. An element of
> `massWeightSubmoduleLE 8 ⊔ S`, for `S` a submodule stable under both groups, is fixed by
> the gauge group and the Lorentz group exactly when it is a combination of
> the constant term, of mass dimension zero,
> the Higgs mass term `H† H`, of mass dimension two (`HiggsAlgebraCovRealization.dotSpan`),
> and the dimension-four span — the four Lorentz contractions of the three `F·F` trace
> families and of the twice-derived hypercharge field strength, among them the gauge
> kinetic and theta terms (`IsGaugeSector.lorentzContractionEightSpan`), the Higgs
> kinetic term, its quartic potential and its two box terms
> (`HiggsAlgebraCovRealization.lorentzContractionEightSpan`), the kinetic terms of the ten fermion
> species over the nine family pairs (`IsFermionSector.kineticSpan`), and the six Yukawa
> couplings over the nine family pairs (`yukawaSpan`) —
> up to a remainder in `S` fixed by both groups, and nothing else. The generators span;
> they are not shown to be independent, and no quotient by total derivatives is taken.

```lean
lemma mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmoduleLE 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ (1 : Submodule ℂ B) ⊔ (h.isHiggsSector.dotSpan 0 0
              ⊔ (h.isGaugeSector.lorentzContractionEightSpan
                    ⊔ h.isHiggsSector.lorentzContractionEightSpan
                  ⊔ (h.isFermionSector.kineticSpan ⊔ h.yukawaSpan)))
```

## Depends on

- [The invariant content of the Standard Model](../part-02/covrealization-massweight-invariants.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Filtration.lean)
