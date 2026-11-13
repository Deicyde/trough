---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.standardModelSpan, StandardModel.CovAlgebraRealization.standardModelSpan_eight, StandardModel.CovAlgebraRealization.standardModelSpan_four, StandardModel.CovAlgebraRealization.standardModelSpan_eq_bot, StandardModel.CovAlgebraRealization.hyperchargeDeriv_comp_swap_zero_one, StandardModel.CovAlgebraRealization.hyperchargeDeriv_contractionTensor_one, StandardModel.CovAlgebraRealization.hyperchargeDeriv_contractionTensor_three, StandardModel.CovAlgebraRealization.isGaugeSector_lorentzContractionEightSpan_eq_traceFamilies
statement: formalized
proof: formalized
---

# The invariant content of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.MassWeight.Invariants`, [PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean): 33 declarations, 33 with a docstring.

## i. Overview

> This is where the classification of the Standard Model closes. A word in the covariant
> generators realises a set of generator classes — gauge, Higgs, fermion — and the eight
> class sets cut the field algebra into eight sectors, each of which has been classified
> separately at every mass weight up to eight, that is at every mass dimension up to four.
> This file joins the eight.
>
> At mass dimension four the gauge- and Lorentz-invariant content is spanned by the four
> Lorentz contractions of each of the three `F·F` trace families and of the twice-derived
> hypercharge field strength. The antisymmetry of the field strength cuts these to two of each
> (`IsGaugeSector.lorentzContractionEightSpan_eq`), and the two of the twice-derived hypercharge
> field strength vanish, its covariant derivatives being ordinary ones (A.1). What is left is the
> kinetic-shape and theta-shape contractions of the three gauge groups. Beside them stand the
> Higgs kinetic term with its quartic potential and its two box terms; the kinetic terms of the
> ten fermion species over the nine family pairs; and the six Yukawa couplings over the nine
> family pairs. Below mass dimension four there is a single term, the Higgs mass term `H† H` at
> mass weight four; below that, nothing.
>
> The statement is about formal expressions, the elements of the field algebra with complex
> coefficients. It is a spanning statement: the listed generators are not shown to be
> independent or nonzero. No reality condition is imposed, and nothing is identified modulo
> total derivatives or the equations of motion, so both box terms, both placements of each
> fermion derivative and the theta terms all appear.
>
> The join is the delicate step. `massWeightSubmodule_eq_iSup_sectorMassWeight` writes the
> weight-`w` submodule as the join of the eight sectors' weight-`w` parts, but reading off
> from an invariant of the whole that its eight pieces are separately invariant would need
> the pieces to be determined by their sum — the independence of the sectors, which does
> not follow from `CovAlgebraRealization` (compare `sector_invariant_of_iSupIndep`).
>
> Nothing here uses it. Each sector's classification is a reduction `ReducesInvariantsTo σ V W`
> of `PhyslibAlpha.Mathematics.InvariantReduction` — every `σ`-invariant of `V ⊔ S` lies in
> `W ⊔ S`, for every `σ`-stable `S` — and that relation is closed under joins in its source.
> Joining the sectors therefore asks only that each of them be carried into itself by the two
> groups, which they are (`repGauge_mem_sectorMassWeight`, `repLorentz_mem_sectorMassWeight`).
> The eight are taken one at a time, each in turn joining the error term of the others, and
> independence never enters.
>
> Section A collects the surviving spans of the eight sectors into `standardModelSpan`, and
> section B checks that it is made of invariants of the right mass weight, which is both the
> easy direction of the classification and the stability the reduction asks of its target.
> Section C restricts each sector's reduction to its weight part, section D joins them, and
> sections E and F read off the equivalence, through
> `ReducesInvariantsTo.mem_sup_and_gauge_lorentz_invariant_iff`, and its consequence at mass
> dimension four.
>
>
> The weight is bounded below as well as above. At weight zero the field algebra contains
> the scalars, which are fixed by both groups and lie in no given `S`; every one of the
> sector classifications combined here excludes that weight for the same reason.

## ii. Key results

> - `standardModelSpan` : the gauge- and Lorentz-invariant content of the Standard Model at mass
>   weight `w`: the join of the surviving spans of the eight sectors

## iv. References

> * None.

## A. The span of the Standard Model Lagrangian

**`StandardModel.CovAlgebraRealization.standardModelSpan`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L122).

> The gauge- and Lorentz-invariant content of the Standard Model at mass weight `w`:
> the join of the surviving spans of the eight sectors. At weight eight it is the gauge
> sector's four Lorentz contractions of each of its four families, two of which already span
> for each family (`IsGaugeSector.lorentzContractionEightSpan_eq`), and the two of the
> twice-derived hypercharge field strength vanish, leaving the two contractions of each of the
> three trace families (`isGaugeSector_lorentzContractionEightSpan_eq_traceFamilies`): the
> kinetic-shape and theta-shape contractions of the three gauge groups. Together with these come the
> Higgs sector's two box terms, kinetic term and quartic potential, the fermion sector's ten
> kinetic terms over the nine family pairs, and the six Yukawa couplings over the nine family
> pairs. Below weight eight only the Higgs sector survives, and only at weight four, where it
> contributes the Higgs mass term.

```lean
noncomputable def standardModelSpan (w : ℕ) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.standardModelSpan_eight`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L131).

> At mass weight eight the span is the gauge, Higgs, fermion and Yukawa spans
> together.

```lean
lemma standardModelSpan_eight :
    h.standardModelSpan 8 = h.isGaugeSector.lorentzContractionEightSpan
        ⊔ h.isHiggsSector.lorentzContractionEightSpan
      ⊔ (h.isFermionSector.kineticSpan ⊔ h.yukawaSpan)
```

**`StandardModel.CovAlgebraRealization.standardModelSpan_four`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L139).

> At mass weight four the span is the line through the Higgs mass term `H† H`, the one
> invariant of the Standard Model below mass dimension four.

```lean
lemma standardModelSpan_four : h.standardModelSpan 4 = h.isHiggsSector.dotSpan 0 0
```

**`StandardModel.CovAlgebraRealization.standardModelSpan_eq_bot`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L146).

> At every mass weight other than four and eight the span is trivial: apart from the
> Higgs mass term there is no Standard-Model term below mass dimension four.

```lean
lemma standardModelSpan_eq_bot {w : ℕ} (hw : w ≠ 8) (hw4 : w ≠ 4) :
    h.standardModelSpan w = ⊥
```

### A.1. The twice-derived hypercharge contractions vanish

> The hypercharge coordinate kills brackets, so the covariant derivatives of the hypercharge
> field strength are ordinary derivatives, which commute (`covF_comp_perm_of_map_lie` with
> `GaugeAlgebra.stdBasis_coord_inr_inr_lie`). The twice-derived hypercharge family is therefore
> symmetric in its two derivative slots as well as antisymmetric in its two field-strength slots,
> and `RankFour` sends both of its remaining contractions to zero. So six generators span the
> gauge contribution: for each of the gluon, `W` and hypercharge trace families, the `(0,2)(1,3)`
> metric contraction `η^{μρ} η^{νσ} F_{μν} F_{ρσ}` and the Levi-Civita contraction
> `ε^{μνρσ} F_{μν} F_{ρσ}`, gauge index summed, as the plain component sums of `RankFour` with no
> further normalisation. These are identities of local expressions; no integration by parts,
> total-derivative quotient or equation of motion is involved.
>
> The derivative symmetry is not a law of `IsGaugeSector`, which relates no derivative slots. It
> holds here because `B` receives the covariant jet algebra, and it covers every ordinary
> realization through `AlgebraRealization.toCovAlgebraRealization`. Nothing is said about the
> gluon and `W` components, whose covariant derivatives do not commute.

**`StandardModel.CovAlgebraRealization.hyperchargeDeriv_comp_swap_zero_one`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L175).

> The twice-derived hypercharge field strengths are symmetric in their two derivative
> slots.

```lean
lemma hyperchargeDeriv_comp_swap_zero_one (d : IsGaugeSector.EightIdx) :
    h.isGaugeSector.hyperchargeDeriv (d ∘ Equiv.swap 0 1) = h.isGaugeSector.hyperchargeDeriv d
```

**`StandardModel.CovAlgebraRealization.hyperchargeDeriv_contractionTensor_one`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L189).

> `η^{μρ} η^{νσ} ∇_μ ∇_ν B_{ρσ} = 0`: a symmetric pair of derivatives contracted against the
> antisymmetric pair of field-strength indices.

```lean
lemma hyperchargeDeriv_contractionTensor_one :
    ofComponents h.isGaugeSector.hyperchargeDeriv (RankFour.contractionTensor 1) = 0
```

**`StandardModel.CovAlgebraRealization.hyperchargeDeriv_contractionTensor_three`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L197).

> `ε^{μνρσ} ∇_μ ∇_ν B_{ρσ} = 0`: a symmetric pair of derivatives contracted against the
> antisymmetric symbol.

```lean
lemma hyperchargeDeriv_contractionTensor_three :
    ofComponents h.isGaugeSector.hyperchargeDeriv (RankFour.contractionTensor 3) = 0
```

**`StandardModel.CovAlgebraRealization.isGaugeSector_lorentzContractionEightSpan_eq_traceFamilies`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L209).

> The gauge contribution at mass weight eight is spanned by the Lorentz contractions of the
> three trace families alone: for each of `gluonTrace`, `wTrace` and `hyperchargeTrace`, the
> `(0,2)(1,3)` metric contraction `η^{μρ} η^{νσ} F_{μν} F_{ρσ}` and the Levi-Civita contraction
> `ε^{μνρσ} F_{μν} F_{ρσ}`, as plain component sums. The two twice-derived hypercharge
> generators of `IsGaugeSector.lorentzContractionEightSpan_eq` vanish. The six span; they are
> not shown to be independent or nonzero.

```lean
lemma isGaugeSector_lorentzContractionEightSpan_eq_traceFamilies :
    h.isGaugeSector.lorentzContractionEightSpan
      = Submodule.span ℂ {ofComponents h.isGaugeSector.gluonTrace (contractionTensor 1),
          ofComponents h.isGaugeSector.gluonTrace (contractionTensor 3)}
        ⊔ (Submodule.span ℂ {ofComponents h.isGaugeSector.wTrace (contractionTensor 1),
            ofComponents h.isGaugeSector.wTrace (contractionTensor 3)}
          ⊔ Submodule.span ℂ {ofComponents h.isGaugeSector.hyperchargeTrace (contractionTensor 1),
            ofComponents h.isGaugeSector.hyperchargeTrace (contractionTensor 3)})
```

## B. The span is made of invariants of the right weight

**`StandardModel.CovAlgebraRealization.isGaugeSector_massWeightSubmodule_le`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L229).

> At a non-zero weight the gauge sector's mass-weight submodule sits inside the
> covariant model's, being the `{gauge}` piece of the sector decomposition there.

```lean
lemma isGaugeSector_massWeightSubmodule_le {w : ℕ} (hw : w ≠ 0) :
    h.isGaugeSector.massWeightSubmodule w ≤ h.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.isHiggsSector_massWeightSubmodule_le`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L236).

> At a non-zero weight the Higgs sector's mass-weight submodule sits inside the
> covariant model's.

```lean
lemma isHiggsSector_massWeightSubmodule_le {w : ℕ} (hw : w ≠ 0) :
    h.isHiggsSector.massWeightSubmodule w ≤ h.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.isFermionSector_massWeightSubmodule_le`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L243).

> At a non-zero weight the fermion sector's mass-weight submodule sits inside the
> covariant model's.

```lean
lemma isFermionSector_massWeightSubmodule_le {w : ℕ} (hw : w ≠ 0) :
    h.isFermionSector.massWeightSubmodule w ≤ h.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.standardModelSpan_le_massWeightSubmodule`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L250).

> The span at weight `w` has mass weight `w`: each of its contributions is a
> combination of words of that weight.

```lean
lemma standardModelSpan_le_massWeightSubmodule (w : ℕ) :
    h.standardModelSpan w ≤ h.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.isFixedBy_standardModelSpan`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L275).

> The span at weight `w` is fixed pointwise by the gauge and Lorentz groups together:
> every one of its contributions is a span of invariants. This is the easy direction of
> the classification, and it is also what supplies the stability the reduction asks of its
> target.

```lean
lemma isFixedBy_standardModelSpan (w : ℕ) :
    IsFixedBy (gaugeLorentzMaps repGauge repLorentz) (h.standardModelSpan w)
```

**`StandardModel.CovAlgebraRealization.repGauge_of_mem_standardModelSpan`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L285).

> Every element of the span at weight `w` is a gauge invariant.

```lean
lemma repGauge_of_mem_standardModelSpan (w : ℕ) (g : GaugeGroupI) {y : B}
    (hy : y ∈ h.standardModelSpan w) : repGauge g y = y
```

**`StandardModel.CovAlgebraRealization.repLorentz_of_mem_standardModelSpan`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L290).

> Every element of the span at weight `w` is a Lorentz invariant.

```lean
lemma repLorentz_of_mem_standardModelSpan (w : ℕ) (Λ : SL(2,ℂ)) {y : B}
    (hy : y ∈ h.standardModelSpan w) : repLorentz Λ y = y
```

## C. Each sector reduces to the span

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight_empty`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L302).

> The empty sector reduces to the span: away from weight zero it is trivial, its only word
> being the empty one.

```lean
lemma reducesInvariantsTo_sectorMassWeight_empty {w : ℕ} (hw : w ≠ 0) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.sectorMassWeight ∅ w)
      (h.standardModelSpan w)
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight_gauge`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L310).

> The gauge sector reduces to the span: at weight eight to the four Lorentz contractions of
> its four families, two of each spanning, below it to nothing at all.

```lean
lemma reducesInvariantsTo_sectorMassWeight_gauge {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz)
      (h.sectorMassWeight {GeneratorClass.gauge} w) (h.standardModelSpan w)
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight_higgs`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L325).

> The Higgs sector reduces to the span: at weight eight to the two box terms, the kinetic
> term and the quartic potential, at weight four to the Higgs mass term, and elsewhere to
> nothing.

```lean
lemma reducesInvariantsTo_sectorMassWeight_higgs {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz)
      (h.sectorMassWeight {GeneratorClass.higgs} w) (h.standardModelSpan w)
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight_fermion`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L338).

> The fermion sector reduces to the span: at weight eight to the ten kinetic terms over the
> nine family pairs, below it to nothing — there is no Dirac mass term.

```lean
lemma reducesInvariantsTo_sectorMassWeight_fermion {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz)
      (h.sectorMassWeight {GeneratorClass.fermion} w) (h.standardModelSpan w)
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight_higgs_fermion`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L355).

> The Yukawa sector reduces to the span: at weight eight to the six Yukawa couplings over the
> nine family pairs, below it to nothing.

```lean
lemma reducesInvariantsTo_sectorMassWeight_higgs_fermion {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz)
      (h.sectorMassWeight {GeneratorClass.higgs, GeneratorClass.fermion} w)
      (h.standardModelSpan w)
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight_gauge_higgs`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L369).

> The gauge-Higgs sector reduces to nothing: it carries no Lorentz invariant below weight
> nine.

```lean
lemma reducesInvariantsTo_sectorMassWeight_gauge_higgs {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz)
      (h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.higgs} w)
      (h.standardModelSpan w)
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight_gauge_fermion`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L379).

> The gauge-fermion sector reduces to nothing: it carries no Lorentz invariant below weight
> nine.

```lean
lemma reducesInvariantsTo_sectorMassWeight_gauge_fermion {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz)
      (h.sectorMassWeight {GeneratorClass.gauge, GeneratorClass.fermion} w)
      (h.standardModelSpan w)
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight_mixed`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L388).

> The mixed sector reduces to nothing: it is trivial below weight nine.

```lean
lemma reducesInvariantsTo_sectorMassWeight_mixed {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz)
      (h.sectorMassWeight
        {GeneratorClass.gauge, GeneratorClass.higgs, GeneratorClass.fermion} w)
      (h.standardModelSpan w)
```

## D. Joining the eight sectors

**`StandardModel.CovAlgebraRealization.isStableUnder_sectorMassWeight`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L404).

> Every weight part of every sector is carried into itself by both groups: the stability
> the join of the reductions asks of its summands.

```lean
lemma isStableUnder_sectorMassWeight (T : Finset GeneratorClass) (w : ℕ) :
    IsStableUnder (gaugeLorentzMaps repGauge repLorentz) (h.sectorMassWeight T w)
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_sectorMassWeight`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L412).

> Every sector reduces to the span, at every weight from one to eight. The three
> constructors of `GeneratorClass` give eight class sets, and section C treats each.

```lean
lemma reducesInvariantsTo_sectorMassWeight {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8)
    (T : Finset GeneratorClass) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.sectorMassWeight T w)
      (h.standardModelSpan w)
```

**`StandardModel.CovAlgebraRealization.reducesInvariantsTo_massWeightSubmodule`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L438).

> The whole weight-`w` submodule reduces to the span, for `w` from one to eight. The
> mass-weight submodule is the join of the eight sectors' weight-`w` parts, each of them
> stable under both groups, and `ReducesInvariantsTo` is closed under joins in its source: the
> sectors are taken one at a time, each in turn joining the error term of the others. No
> independence of the sectors is used, and none is available.

```lean
lemma reducesInvariantsTo_massWeightSubmodule {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) (h.massWeightSubmodule w)
      (h.standardModelSpan w)
```

## E. The classification at mass dimension at most four

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmodule_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L460).

> The classification of the Standard Model at mass dimension at most four as an
> equivalence, in the shape every sector uses: an element of `massWeightSubmodule w ⊔ S`
> for `0 < w ≤ 8`, with `S` stable under both groups, is fixed by both groups exactly when
> it is a combination of the Standard-Model terms of weight `w` up to a remainder in `S`
> fixed by both groups. Forwards this is the reduction of section D; backwards it uses
> that the span is made of invariants of weight `w`, section B. The weight-four Higgs mass
> term is what makes the span, rather than the bare equation `x = y`, the right form of
> the statement.

```lean
lemma mem_massWeightSubmodule_sup_and_gauge_lorentz_invariant_iff (w : ℕ) (hw0 : 0 < w)
    (hw : w ≤ 8) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.standardModelSpan w
```

**`StandardModel.CovAlgebraRealization.exists_mem_standardModelSpan_of_gauge_and_lorentz_invariant`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L477).

> The gauge and Lorentz invariants of mass weight `w` for `0 < w ≤ 8`, modulo a
> submodule `S` stable under both groups: such an invariant is a combination of the
> Standard-Model terms of that weight plus a remainder in `S`, and the remainder is fixed
> by both groups as well, being the difference of two invariants.

```lean
lemma exists_mem_standardModelSpan_of_gauge_and_lorentz_invariant (w : ℕ)
    (hw0 : 0 < w) (hw : w ≤ 8) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.massWeightSubmodule w ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGauge g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) :
    ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
      ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
      ∧ x - y ∈ h.standardModelSpan w
```

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmodule_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L493).

> The same classification without the existential: at every weight from one to eight an
> element of `massWeightSubmodule w ⊔ S` fixed by both groups is an element of the
> Standard-Model span joined with `S` fixed by both groups, and conversely.

```lean
lemma mem_massWeightSubmodule_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw0 : 0 < w) (hw : w ≤ 8) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ (x ∈ h.standardModelSpan w ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
```

## F. The Standard Model Lagrangian

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L528).

> The invariant content of the Standard Model at mass dimension four. An element of
> `massWeightSubmodule 8 ⊔ S`, for `S` a submodule stable under both groups, is fixed by
> the gauge group and the Lorentz group exactly when it is a combination of
> the four Lorentz contractions of the three `F·F` trace families and of the twice-derived
> hypercharge field strength (`IsGaugeSector.lorentzContractionEightSpan`), two of each
> spanning by `IsGaugeSector.lorentzContractionEightSpan_eq`: the kinetic-shape and
> theta-shape contractions of the three gauge groups and two contractions of the
> twice-derived hypercharge field strength, which vanish
> (`mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian_traceFamilies`),
> the Higgs kinetic term, its quartic potential and its two box terms
> (`HiggsAlgebraCovRealization.lorentzContractionEightSpan`),
> the kinetic terms of the ten fermion species over the nine family pairs
> (`IsFermionSector.kineticSpan`),
> and the six Yukawa couplings over the nine family pairs (`yukawaSpan`),
> up to a remainder in `S` fixed by both groups — and nothing else. The generators span;
> they are not shown to be independent, and no quotient by total derivatives is taken.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.isGaugeSector.lorentzContractionEightSpan
                ⊔ h.isHiggsSector.lorentzContractionEightSpan
              ⊔ (h.isFermionSector.kineticSpan ⊔ h.yukawaSpan)
```

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian_traceFamilies`**, a lemma, [line 550](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L550).

> The invariant content of the Standard Model at mass dimension four with the gauge
> contribution written through the Lorentz contractions of the three trace families alone:
> the `(0,2)(1,3)` metric contraction and the Levi-Civita contraction of each of `gluonTrace`,
> `wTrace` and `hyperchargeTrace` (`isGaugeSector_lorentzContractionEightSpan_eq_traceFamilies`).
> The Higgs, fermion and Yukawa contributions are as in
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian`. The
> generators span; they are not shown to be independent or nonzero.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian_traceFamilies
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ (Submodule.span ℂ
                {ofComponents h.isGaugeSector.gluonTrace (contractionTensor 1),
                  ofComponents h.isGaugeSector.gluonTrace (contractionTensor 3)}
              ⊔ (Submodule.span ℂ {ofComponents h.isGaugeSector.wTrace (contractionTensor 1),
                  ofComponents h.isGaugeSector.wTrace (contractionTensor 3)}
                ⊔ Submodule.span ℂ
                  {ofComponents h.isGaugeSector.hyperchargeTrace (contractionTensor 1),
                    ofComponents h.isGaugeSector.hyperchargeTrace (contractionTensor 3)}))
                ⊔ h.isHiggsSector.lorentzContractionEightSpan
              ⊔ (h.isFermionSector.kineticSpan ⊔ h.yukawaSpan)
```

**`StandardModel.CovAlgebraRealization.mem_of_gauge_and_lorentz_invariant_massWeightSubmodule_sup`**, a lemma, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L573).

> Below mass dimension two there is nothing at all, and at mass dimension two only the
> Higgs mass term: at every weight from one to seven other than four an element of
> `massWeightSubmodule w ⊔ S` fixed by both groups already lies in `S`.

```lean
lemma mem_of_gauge_and_lorentz_invariant_massWeightSubmodule_sup (w : ℕ) (hw0 : 0 < w)
    (hw : w < 8) (hw4 : w ≠ 4) (S : Submodule ℂ B)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ h.massWeightSubmodule w ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGauge g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`StandardModel.CovAlgebraRealization.mem_massWeightSubmodule_four_sup_and_gauge_lorentz_invariant_iff_higgsMass`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean#L587).

> At mass dimension two the only invariant of the Standard Model is the Higgs mass term
> `H† H`: an element of `massWeightSubmodule 4 ⊔ S` fixed by both groups is a multiple of
> it up to a remainder in `S` fixed by both groups.

```lean
lemma mem_massWeightSubmodule_four_sup_and_gauge_lorentz_invariant_iff_higgsMass
    (S : Submodule ℂ B) (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGauge g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (x : B) :
    (x ∈ h.massWeightSubmodule 4 ⊔ S ∧ (∀ g : GaugeGroupI, repGauge g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentz g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGauge g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentz g y = y)
          ∧ x - y ∈ h.isHiggsSector.dotSpan 0 0
```

## Depends on

- [The Yukawa terms built on the conjugate Higgs symbol](covrealization-yukawasector-families-barhiggs.md)
- [The kinetic terms at mass weight eight](../part-06/isfermionsector-massweight-massdimeight.md)
- [Products of two field strengths as bi-adjoint gauge tensors](../part-07/isgaugesector-massweight-massdimeight.md)
- [The Higgs invariants of mass weight eight](../part-10/realization-higgscov-massweight-massdimeight.md)
- [The Higgs invariants below mass weight eight](../part-11/realization-higgscov-massweight-massdimlteight.md)

## Proof depends on

- [The gauge-fermion invariants below mass weight nine](../part-01/covrealization-fermiongaugesector-massweight.md)
- [The gauge-Higgs invariants below mass weight nine](../part-01/covrealization-gaugehiggssector-massweight.md)
- [The mixed sector](covrealization-mixedsector-basic.md)
- [The Yukawa sector at mass weight eight](covrealization-yukawasector-massdimeight.md)
- [The Yukawa invariants below mass weight eight](covrealization-yukawasector-massdimlteight.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/MassWeight/Invariants.lean)
