---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.standardModelSpan, StandardModel.LocalCovFieldAlgebra.standardModelSpan_eight, StandardModel.LocalCovFieldAlgebra.standardModelSpan_four, StandardModel.LocalCovFieldAlgebra.standardModelSpan_eq_bot, StandardModel.LocalCovFieldAlgebra.hyperchargeDeriv_comp_swap_zero_one, StandardModel.LocalCovFieldAlgebra.hyperchargeDeriv_contractionTensor_one, StandardModel.LocalCovFieldAlgebra.hyperchargeDeriv_contractionTensor_three, StandardModel.LocalCovFieldAlgebra.gaugeSector_lorentzContractionEightSpan_eq_traceFamilies
statement: formalized
proof: formalized
---

# The invariant content of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.LocalCovFieldAlgebra.MassWeight.Invariants`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean): 31 declarations, 31 with a docstring.

> The gauge and Lorentz invariants of the Standard Model at each mass weight from one to eight,
> obtained by joining the classifications of the eight sectors.

## i. Overview

> This is where the classification of the Standard Model closes. A product of covariant
> generators realises a set of kinds (gauge, scalar, fermion), and the eight sets of kinds cut the
> field algebra into eight sectors `fieldData.sectorMassWeight A w`, each of which has been classified
> separately at every mass weight up to eight, that is at every mass dimension up to four.
> This file joins the eight.
>
> At mass dimension four the gauge- and Lorentz-invariant content is spanned by the four
> Lorentz contractions of each of the three `F·F` trace families and of the twice-derived
> hypercharge field strength. The antisymmetry of the field strength cuts these to two of each
> (`GaugeSector.lorentzContractionEightSpan_eq`), and the two of the twice-derived hypercharge
> field strength vanish, its covariant derivatives being ordinary ones (A.1). What is left is the
> kinetic-shape and theta-shape contractions of the three gauge groups. Beside them stand the
> Higgs kinetic term with its quartic potential and its two box terms; the kinetic terms of the
> ten fermion species over the nine family pairs; and the six Yukawa couplings over the nine
> family pairs. Below mass dimension four there is a single term, the Higgs mass term `H† H` at
> mass weight four; below that, nothing.
>
> The statement is about formal expressions, the elements of the field algebra with complex
> coefficients. It is a spanning statement, and the listed generators are not shown to be
> independent or nonzero. No reality condition is imposed, and nothing is identified modulo
> total derivatives or the equations of motion, so both box terms, both placements of each
> fermion derivative and the theta terms all appear.
>
> The join is the delicate step. `massWeightSubmodule_eq_iSup_sectorMassWeight` writes the
> weight-`w` submodule as the join of the eight sectors' weight-`w` parts, but reading off
> from an invariant of the whole that its eight pieces are separately invariant would need
> the pieces to be determined by their sum — the independence of the sectors, which does
> not follow from the structure of the covariant field algebra of the Standard Model used here.
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
> The weight is bounded below as well as above. At weight zero the field algebra contains
> the scalars, which are fixed by both groups and lie in no given `S`; every one of the
> sector classifications combined here excludes that weight for the same reason.

## ii. Key results

> In the namespace `StandardModel.LocalCovFieldAlgebra`:
>
> - `standardModelSpan` : the gauge- and Lorentz-invariant content of the Standard Model at mass
>   weight `w`, the join of the surviving spans of the eight sectors.
> - `reducesInvariantsTo_massWeightSubmodule` : the weight-`w` submodule reduces to the span, for
>   `w` from one to eight.
> - `mem_massWeightSubmodule_sup_and_gauge_lorentz_invariant_iff` : the classification at each
>   mass weight from one to eight.
> - `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian` : the invariant
>   content at mass dimension four, written out term by term.

## iv. References

> * None.

## A. The span of the Standard Model Lagrangian

**`StandardModel.LocalCovFieldAlgebra.standardModelSpan`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L130).

> The gauge- and Lorentz-invariant content of the Standard Model at mass weight `w`, the join of
> the surviving spans of the eight sectors. At weight eight it is the gauge sector's four Lorentz
> contractions of each of its four families, two of which already span for each family
> (`GaugeSector.lorentzContractionEightSpan_eq`), and the two of the twice-derived hypercharge field
> strength vanish, leaving the two contractions of each of the three trace families
> (`gaugeSector_lorentzContractionEightSpan_eq_traceFamilies`). These are the kinetic-shape and
> theta-shape contractions of the three gauge groups. Together with these come the Higgs sector's
> two box terms, kinetic term and quartic potential, the fermion sector's ten kinetic terms over the
> nine family pairs, and the six Yukawa couplings over the nine family pairs. Below weight eight
> only the Higgs sector survives, and only at weight four, where it contributes the Higgs mass
> term.

```lean
noncomputable def standardModelSpan (w : ℕ) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.standardModelSpan_eight`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L139).

> At mass weight eight the span is the gauge, Higgs, fermion and Yukawa spans
> together.

```lean
lemma standardModelSpan_eight :
    standardModelSpan 8 = GaugeSector.lorentzContractionEightSpan
        ⊔ ScalarSector.lorentzContractionEightSpan
      ⊔ (FermionSector.kineticSpan ⊔ yukawaSpan)
```

**`StandardModel.LocalCovFieldAlgebra.standardModelSpan_four`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L147).

> At mass weight four the span is the line through the Higgs mass term `H† H`, the one
> invariant of the Standard Model below mass dimension four.

```lean
lemma standardModelSpan_four : standardModelSpan 4 = ScalarSector.dotSpan 0 0
```

**`StandardModel.LocalCovFieldAlgebra.standardModelSpan_eq_bot`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L154).

> At every mass weight other than four and eight the span is trivial. Apart from the
> Higgs mass term there is no Standard-Model term below mass dimension four.

```lean
lemma standardModelSpan_eq_bot {w : ℕ} (hw : w ≠ 8) (hw4 : w ≠ 4) :
    standardModelSpan w = ⊥
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
> The derivative symmetry is not a law of `GaugeSector`, which relates no derivative slots. It
> holds here because the covariant derivatives of the field strength in the covariant field algebra of
> the Standard Model are ordinary ones. Nothing is said about the
> gluon and `W` components, whose covariant derivatives do not commute.

**`StandardModel.LocalCovFieldAlgebra.hyperchargeDeriv_comp_swap_zero_one`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L183).

> The twice-derived hypercharge field strengths are symmetric in their two derivative
> slots.

```lean
lemma hyperchargeDeriv_comp_swap_zero_one (d : GaugeSector.EightIdx) :
    GaugeSector.hyperchargeDeriv (d ∘ Equiv.swap 0 1) = GaugeSector.hyperchargeDeriv d
```

**`StandardModel.LocalCovFieldAlgebra.hyperchargeDeriv_contractionTensor_one`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L197).

> The metric contraction `η^{μρ} η^{νσ} ∇_μ ∇_ν B_{ρσ}` vanishes, a symmetric pair of
> derivatives being contracted against the antisymmetric pair of field-strength indices.

```lean
lemma hyperchargeDeriv_contractionTensor_one :
    liftComponents GaugeSector.hyperchargeDeriv (RankFour.contractionTensor 1) = 0
```

**`StandardModel.LocalCovFieldAlgebra.hyperchargeDeriv_contractionTensor_three`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L205).

> The Levi-Civita contraction `ε^{μνρσ} ∇_μ ∇_ν B_{ρσ}` vanishes, a symmetric pair of
> derivatives being contracted against the antisymmetric symbol.

```lean
lemma hyperchargeDeriv_contractionTensor_three :
    liftComponents GaugeSector.hyperchargeDeriv (RankFour.contractionTensor 3) = 0
```

**`StandardModel.LocalCovFieldAlgebra.gaugeSector_lorentzContractionEightSpan_eq_traceFamilies`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L217).

> The gauge contribution at mass weight eight is spanned by the Lorentz contractions of the
> three trace families alone. For each of `gluonTrace`, `wTrace` and `hyperchargeTrace` these are
> the `(0,2)(1,3)` metric contraction `η^{μρ} η^{νσ} F_{μν} F_{ρσ}` and the Levi-Civita contraction
> `ε^{μνρσ} F_{μν} F_{ρσ}`, as plain component sums. The two twice-derived hypercharge
> generators of `GaugeSector.lorentzContractionEightSpan_eq` vanish. The six span; they are
> not shown to be independent or nonzero.

```lean
lemma gaugeSector_lorentzContractionEightSpan_eq_traceFamilies :
    GaugeSector.lorentzContractionEightSpan
      = Submodule.span ℂ {liftComponents GaugeSector.gluonTrace (contractionTensor 1),
          liftComponents GaugeSector.gluonTrace (contractionTensor 3)}
        ⊔ (Submodule.span ℂ {liftComponents GaugeSector.wTrace (contractionTensor 1),
            liftComponents GaugeSector.wTrace (contractionTensor 3)}
          ⊔ Submodule.span ℂ {liftComponents GaugeSector.hyperchargeTrace (contractionTensor 1),
            liftComponents GaugeSector.hyperchargeTrace (contractionTensor 3)})
```

## B. The span is made of invariants of the right weight

**`StandardModel.LocalCovFieldAlgebra.gaugeSector_massWeightSubmodule_le`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L237).

> At a non-zero weight the gauge sector's mass-weight submodule sits inside that of the
> covariant field algebra, being the `{gauge}` piece of the sector decomposition there.

```lean
lemma gaugeSector_massWeightSubmodule_le {w : ℕ} (hw : w ≠ 0) :
    GaugeSector.massWeightSubmodule w ≤ massWeightSubmodule w
```

**`StandardModel.LocalCovFieldAlgebra.scalarSector_massWeightSubmodule_le`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L244).

> At a non-zero weight the Higgs sector's mass-weight submodule sits inside that of the
> covariant field algebra.

```lean
lemma scalarSector_massWeightSubmodule_le {w : ℕ} (hw : w ≠ 0) :
    ScalarSector.massWeightSubmodule w ≤ massWeightSubmodule w
```

**`StandardModel.LocalCovFieldAlgebra.fermionSector_massWeightSubmodule_le`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L251).

> At a non-zero weight the fermion sector's mass-weight submodule sits inside that of the
> covariant field algebra.

```lean
lemma fermionSector_massWeightSubmodule_le {w : ℕ} (hw : w ≠ 0) :
    FermionSector.massWeightSubmodule w ≤ massWeightSubmodule w
```

**`StandardModel.LocalCovFieldAlgebra.standardModelSpan_le_massWeightSubmodule`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L258).

> The span at weight `w` has mass weight `w`, each of its contributions is a
> combination of words of that weight.

```lean
lemma standardModelSpan_le_massWeightSubmodule (w : ℕ) :
    standardModelSpan w ≤ massWeightSubmodule w
```

**`StandardModel.LocalCovFieldAlgebra.isFixedBy_standardModelSpan`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L283).

> The span at weight `w` is fixed pointwise by the gauge and Lorentz groups together, since
> every one of its contributions is a span of invariants. This is the easy direction of
> the classification, and it is also what supplies the stability the reduction asks of its
> target.

```lean
lemma isFixedBy_standardModelSpan (w : ℕ) :
    IsFixedBy (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (standardModelSpan w)
```

## C. Each sector reduces to the span

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight_empty`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L300).

> The empty sector reduces to the span. Away from weight zero it is trivial, its only word
> being the empty one.

```lean
lemma reducesInvariantsTo_sectorMassWeight_empty {w : ℕ} (hw : w ≠ 0) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight ∅ w) (standardModelSpan w)
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight_gauge`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L308).

> The gauge sector reduces to the span, at weight eight to the four Lorentz contractions of
> its four families, two of each spanning, below it to nothing at all.

```lean
lemma reducesInvariantsTo_sectorMassWeight_gauge {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight {FieldKind.gauge} w) (standardModelSpan w)
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight_higgs`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L323).

> The Higgs sector reduces to the span, at weight eight to the two box terms, the kinetic
> term and the quartic potential, at weight four to the Higgs mass term, and elsewhere to
> nothing.

```lean
lemma reducesInvariantsTo_sectorMassWeight_higgs {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight {FieldKind.scalar} w) (standardModelSpan w)
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight_fermion`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L336).

> The fermion sector reduces to the span, at weight eight to the ten kinetic terms over the
> nine family pairs and below it to nothing. There is no Dirac mass term.

```lean
lemma reducesInvariantsTo_sectorMassWeight_fermion {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight {FieldKind.fermion} w) (standardModelSpan w)
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight_higgs_fermion`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L353).

> The Yukawa sector reduces to the span, at weight eight to the six Yukawa couplings over the
> nine family pairs, below it to nothing.

```lean
lemma reducesInvariantsTo_sectorMassWeight_higgs_fermion {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight {FieldKind.scalar, FieldKind.fermion} w)
      (standardModelSpan w)
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight_gauge_higgs`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L367).

> The gauge-Higgs sector reduces to nothing, as it carries no Lorentz invariant below weight
> nine.

```lean
lemma reducesInvariantsTo_sectorMassWeight_gauge_higgs {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.scalar} w)
      (standardModelSpan w)
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight_gauge_fermion`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L377).

> The gauge-fermion sector reduces to nothing, as it carries no Lorentz invariant below weight
> nine.

```lean
lemma reducesInvariantsTo_sectorMassWeight_gauge_fermion {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight {FieldKind.gauge, FieldKind.fermion} w)
      (standardModelSpan w)
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight_mixed`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L386).

> The mixed sector reduces to nothing, as it is trivial below weight nine.

```lean
lemma reducesInvariantsTo_sectorMassWeight_mixed {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight
        {FieldKind.gauge, FieldKind.scalar, FieldKind.fermion} w)
      (standardModelSpan w)
```

## D. Joining the eight sectors

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_sectorMassWeight`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L402).

> Every weight part of every sector is carried into itself by both groups. This is the
> stability the join of the reductions asks of its summands.

```lean
lemma isStableUnder_sectorMassWeight (T : Finset FieldKind) (w : ℕ) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight T w)
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_sectorMassWeight`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L412).

> Every sector reduces to the span, at every weight from one to eight. The three
> constructors of `GaugeFieldData.FieldKind` give eight sets of kinds, and section C treats
> each.

```lean
lemma reducesInvariantsTo_sectorMassWeight {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8)
    (T : Finset FieldKind) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup)
      (fieldData.sectorMassWeight T w) (standardModelSpan w)
```

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_massWeightSubmodule`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L438).

> The whole weight-`w` submodule reduces to the span, for `w` from one to eight. The
> mass-weight submodule is the join of the eight sectors' weight-`w` parts, each of them
> stable under both groups, and `ReducesInvariantsTo` is closed under joins in its source. The
> sectors are taken one at a time, each in turn joining the error term of the others. No
> independence of the sectors is used, and none is available.

```lean
lemma reducesInvariantsTo_massWeightSubmodule {w : ℕ} (hw0 : 0 < w) (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (massWeightSubmodule w)
      (standardModelSpan w)
```

## E. The classification at mass dimension at most four

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmodule_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L460).

> The classification of the Standard Model at mass dimension at most four as an
> equivalence, in the shape every sector uses. An element of `massWeightSubmodule w ⊔ S`
> for `0 < w ≤ 8`, with `S` stable under both groups, is fixed by both groups exactly when
> it is a combination of the Standard-Model terms of weight `w` up to a remainder in `S`
> fixed by both groups. Forwards this is the reduction of section D; backwards it uses
> that the span is made of invariants of weight `w`, section B. The weight-four Higgs mass
> term is what makes the span, rather than the bare equation `x = y`, the right form of
> the statement.

```lean
lemma mem_massWeightSubmodule_sup_and_gauge_lorentz_invariant_iff (w : ℕ) (hw0 : 0 < w)
    (hw : w ≤ 8) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ standardModelSpan w
```

**`StandardModel.LocalCovFieldAlgebra.exists_mem_standardModelSpan_of_gauge_and_lorentz_invariant`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L477).

> The gauge and Lorentz invariants of mass weight `w` for `0 < w ≤ 8`, modulo a
> submodule `S` stable under both groups. Such an invariant is a combination of the
> Standard-Model terms of that weight plus a remainder in `S`, and the remainder is fixed
> by both groups as well, being the difference of two invariants.

```lean
lemma exists_mem_standardModelSpan_of_gauge_and_lorentz_invariant (w : ℕ)
    (hw0 : 0 < w) (hw : w ≤ 8) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule w ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGaugeGroupI g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) :
    ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
      ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
      ∧ x - y ∈ standardModelSpan w
```

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmodule_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L493).

> The same classification without the existential. At every weight from one to eight an
> element of `massWeightSubmodule w ⊔ S` fixed by both groups is an element of the
> Standard-Model span joined with `S` fixed by both groups, and conversely.

```lean
lemma mem_massWeightSubmodule_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw0 : 0 < w) (hw : w ≤ 8) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule w ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ (x ∈ standardModelSpan w ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
```

## F. The Standard Model Lagrangian

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L528).

> The invariant content of the Standard Model at mass dimension four. An element of
> `massWeightSubmodule 8 ⊔ S`, for `S` a submodule stable under both groups, is fixed by
> the gauge group and the Lorentz group exactly when it is a combination of
> the four Lorentz contractions of the three `F·F` trace families and of the twice-derived
> hypercharge field strength (`GaugeSector.lorentzContractionEightSpan`), two of each
> spanning by `GaugeSector.lorentzContractionEightSpan_eq` (the kinetic-shape and
> theta-shape contractions of the three gauge groups and two contractions of the
> twice-derived hypercharge field strength, which vanish
> (`mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian_traceFamilies`)),
> the Higgs kinetic term, its quartic potential and its two box terms
> (`ScalarSector.lorentzContractionEightSpan`),
> the kinetic terms of the ten fermion species over the nine family pairs
> (`FermionSector.kineticSpan`),
> and the six Yukawa couplings over the nine family pairs (`yukawaSpan`),
> up to a remainder in `S` fixed by both groups — and nothing else. The generators span;
> they are not shown to be independent, and no quotient by total derivatives is taken.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ GaugeSector.lorentzContractionEightSpan
                ⊔ ScalarSector.lorentzContractionEightSpan
              ⊔ (FermionSector.kineticSpan ⊔ yukawaSpan)
```

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian_traceFamilies`**, a lemma, [line 551](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L551).

> The invariant content of the Standard Model at mass dimension four with the gauge
> contribution written through the Lorentz contractions of the three trace families alone,
> the `(0,2)(1,3)` metric contraction and the Levi-Civita contraction of each of `gluonTrace`,
> `wTrace` and `hyperchargeTrace` (`gaugeSector_lorentzContractionEightSpan_eq_traceFamilies`).
> The Higgs, fermion and Yukawa contributions are as in
> `mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian`. The
> generators span; they are not shown to be independent or nonzero.

```lean
lemma mem_massWeightSubmodule_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian_traceFamilies
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ (Submodule.span ℂ
                {liftComponents GaugeSector.gluonTrace (contractionTensor 1),
                  liftComponents GaugeSector.gluonTrace (contractionTensor 3)}
              ⊔ (Submodule.span ℂ {liftComponents GaugeSector.wTrace (contractionTensor 1),
                  liftComponents GaugeSector.wTrace (contractionTensor 3)}
                ⊔ Submodule.span ℂ
                  {liftComponents GaugeSector.hyperchargeTrace (contractionTensor 1),
                    liftComponents GaugeSector.hyperchargeTrace (contractionTensor 3)}))
                ⊔ ScalarSector.lorentzContractionEightSpan
              ⊔ (FermionSector.kineticSpan ⊔ yukawaSpan)
```

**`StandardModel.LocalCovFieldAlgebra.mem_of_gauge_and_lorentz_invariant_massWeightSubmodule_sup`**, a lemma, [line 575](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L575).

> Below mass dimension two there is nothing at all, and at mass dimension two only the
> Higgs mass term. At every weight from one to seven other than four an element of
> `massWeightSubmodule w ⊔ S` fixed by both groups already lies in `S`.

```lean
lemma mem_of_gauge_and_lorentz_invariant_massWeightSubmodule_sup (w : ℕ) (hw0 : 0 < w)
    (hw : w < 8) (hw4 : w ≠ 4) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule w ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGaugeGroupI g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) : x ∈ S
```

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmodule_four_sup_and_gauge_lorentz_invariant_iff_higgsMass`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean#L589).

> At mass dimension two the only invariant of the Standard Model is the Higgs mass term
> `H† H`. An element of `massWeightSubmodule 4 ⊔ S` fixed by both groups is a multiple of
> it up to a remainder in `S` fixed by both groups.

```lean
lemma mem_massWeightSubmodule_four_sup_and_gauge_lorentz_invariant_iff_higgsMass
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmodule 4 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ ScalarSector.dotSpan 0 0
```

## Depends on

- [The kinetic terms at mass weight eight](../part-04/localfieldalgebra-fermionsector-massweight-massd.md)
- [Products of two field strengths as bi-adjoint gauge tensors](../part-04/localfieldalgebra-gaugesector-massweight-massdim.md)
- [The mass-weight grading of the covariant field algebra of the Standard Model](localfieldalgebra-localcovfieldalgebra-massweigh.md)
- [The Higgs invariants of mass weight eight](../part-06/localfieldalgebra-scalarsector-massweight-massdi.md)
- [The Higgs invariants below mass weight eight](../part-06/localfieldalgebra-scalarsector-massweight-massdi-2.md)
- [The Yukawa terms built on the conjugate Higgs symbol](../part-06/localfieldalgebra-yukawasector-families-barhiggs.md)

## Proof depends on

- [The gauge-fermion invariants below mass weight nine](../part-02/localfieldalgebra-fermiongaugesector-massweight.md)
- [The gauge-Higgs invariants below mass weight nine](../part-04/localfieldalgebra-gaugehiggssector-massweight.md)
- [The mixed sector](localfieldalgebra-mixedsector-basic.md)
- [The Yukawa sector at mass weight eight](../part-06/localfieldalgebra-yukawasector-massdimeight.md)
- [The Yukawa invariants below mass weight eight](../part-06/localfieldalgebra-yukawasector-massdimlteight.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Invariants.lean)
