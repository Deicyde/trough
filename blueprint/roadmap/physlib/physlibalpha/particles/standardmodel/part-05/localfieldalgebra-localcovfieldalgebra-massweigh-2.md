---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.isStableUnder_massWeightSubmoduleLE, StandardModel.LocalCovFieldAlgebra.isFixedBy_massWeightSubmodule_zero, StandardModel.LocalCovFieldAlgebra.standardModelSpanLE, StandardModel.LocalCovFieldAlgebra.massWeightSubmodule_zero_le_standardModelSpanLE, StandardModel.LocalCovFieldAlgebra.standardModelSpan_le_standardModelSpanLE, StandardModel.LocalCovFieldAlgebra.standardModelSpanLE_le_massWeightSubmoduleLE, StandardModel.LocalCovFieldAlgebra.isFixedBy_standardModelSpanLE, StandardModel.LocalCovFieldAlgebra.repGauge_of_mem_standardModelSpanLE
statement: formalized
proof: formalized
---

# The mass-weight filtration and the constant term

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.LocalCovFieldAlgebra.MassWeight.Filtration`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean): 18 declarations, 18 with a docstring.

> The gauge and Lorentz invariants of the Standard Model of mass dimension at most four, the
> constant term included.

## i. Overview

> The grading of the field algebra by mass weight answers one weight at a time. A
> Lagrangian is not graded. It is a sum of terms of every weight up to a cut-off, and the
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
> Section B settles what the weight-zero piece is. By the generic
> `GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmodule_zero`, every generator carrying positive
> weight, `massWeightSubmodule 0` is exactly the scalars, and the unit is fixed by both groups
> because both act by algebra maps.
>
> The classification then runs as it does for the grading. `ReducesInvariantsTo` is closed under
> joins in its source, and the filtration is a join. Each weight from one to eight reduces to
> the Standard-Model span of that weight by `reducesInvariantsTo_massWeightSubmodule`, weight
> zero reduces to itself, and the join of the nine is a reduction of the filtration. No independence
> of the sectors, and none of the weights, is used anywhere.
>
> The answer at bound eight is spanned by the constant term, the Higgs mass term `H† H`, and
> the dimension-four span of `Invariants.lean`, with the same scope: formal expressions,
> spanning generators, and no quotient by total derivatives or the equations of motion.

## ii. Key results

> - `isStableUnder_massWeightSubmoduleLE` : the filtration is stable under both groups.
> - `standardModelSpanLE` : the constant term joined with the Standard-Model span of every weight
>   up to `w`.
> - `mem_standardModelSpanLE_eight_of_mem_sector` : an invariant element of a sector of mass
>   weight at most eight lies in the span of the filtration.
> - `mem_massWeightSubmoduleLE_sup_and_gauge_lorentz_invariant_iff` : the classification up to
>   mass weight `w ≤ 8`.
> - `mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian` : the
>   invariant content of the Standard Model up to mass dimension four, written out term by term.

## iv. References

> * None.

## A. The mass-weight filtration

**`StandardModel.LocalCovFieldAlgebra.isStableUnder_massWeightSubmoduleLE`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L92).

> The filtration is carried into itself by both groups, since each graded piece is.

```lean
lemma isStableUnder_massWeightSubmoduleLE (w : ℕ) :
    IsStableUnder (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (massWeightSubmoduleLE w)
```

## B. The constant term at weight zero

**`StandardModel.LocalCovFieldAlgebra.isFixedBy_massWeightSubmodule_zero`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L109).

> The scalars are fixed by both groups, since each acts by an algebra map, so each fixes the
> unit. This is what makes the constant term an invariant, and it is what the backward
> direction of the classification needs of the weight-zero part of the span.

```lean
lemma isFixedBy_massWeightSubmodule_zero :
    IsFixedBy (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (massWeightSubmodule 0)
```

## C. The span of the filtration

**`StandardModel.LocalCovFieldAlgebra.standardModelSpanLE`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L126).

> The gauge- and Lorentz-invariant content of the Standard Model up to mass weight `w`. It is
> the weight-zero part of the field algebra, which is the constant term, joined with the
> Standard-Model span of every weight up to `w`.

```lean
noncomputable def standardModelSpanLE (w : ℕ) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.massWeightSubmodule_zero_le_standardModelSpanLE`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L130).

> The constant term lies in the span of the filtration, at every bound.

```lean
lemma massWeightSubmodule_zero_le_standardModelSpanLE (w : ℕ) :
    massWeightSubmodule 0 ≤ standardModelSpanLE w
```

**`StandardModel.LocalCovFieldAlgebra.standardModelSpan_le_standardModelSpanLE`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L136).

> The graded span of a weight at most `w` lies in the span of the filtration at `w`.

```lean
lemma standardModelSpan_le_standardModelSpanLE {k w : ℕ} (hk : k ≤ w) :
    standardModelSpan k ≤ standardModelSpanLE w
```

**`StandardModel.LocalCovFieldAlgebra.standardModelSpanLE_le_massWeightSubmoduleLE`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L143).

> The span of the filtration at `w` has mass weight at most `w`. The constant term has
> weight zero and each graded span has its own weight.

```lean
lemma standardModelSpanLE_le_massWeightSubmoduleLE (w : ℕ) :
    standardModelSpanLE w ≤ massWeightSubmoduleLE w
```

**`StandardModel.LocalCovFieldAlgebra.isFixedBy_standardModelSpanLE`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L153).

> The span of the filtration is fixed pointwise by the gauge and Lorentz groups
> together. At positive weight this is the fixedness of the graded spans; at weight zero
> it is the fixedness of the unit, and that is the only new content of the filtration.

```lean
lemma isFixedBy_standardModelSpanLE (w : ℕ) :
    IsFixedBy (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (standardModelSpanLE w)
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_of_mem_standardModelSpanLE`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L159).

> Every element of the span of the filtration is a gauge invariant.

```lean
lemma repGauge_of_mem_standardModelSpanLE (w : ℕ) (g : GaugeGroupI)
    {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ standardModelSpanLE w) : repGaugeGroupI g y = y
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_of_mem_standardModelSpanLE`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L165).

> Every element of the span of the filtration is a Lorentz invariant.

```lean
lemma repLorentz_of_mem_standardModelSpanLE (w : ℕ) (Λ : SL(2,ℂ))
    {y : fieldData.LocalCovFieldAlgebra}
    (hy : y ∈ standardModelSpanLE w) : repLorentzGroup Λ y = y
```

**`StandardModel.LocalCovFieldAlgebra.standardModelSpanLE_eight`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L174).

> The span of the filtration at bound eight in reduced form. Of the nine graded spans
> only two are non-trivial, the Higgs mass term at weight four and the dimension-four
> Lagrangian at weight eight, so what survives up to mass dimension four is the constant
> term, the Higgs mass term, and the Lagrangian.

```lean
lemma standardModelSpanLE_eight :
    standardModelSpanLE 8 = (1 : Submodule ℂ fieldData.LocalCovFieldAlgebra) ⊔
    (ScalarSector.dotSpan 0 0
      ⊔ (GaugeSector.lorentzContractionEightSpan
            ⊔ ScalarSector.lorentzContractionEightSpan
          ⊔ (FermionSector.kineticSpan ⊔ yukawaSpan)))
```

## D. Reducing the filtration

**`StandardModel.LocalCovFieldAlgebra.reducesInvariantsTo_massWeightSubmoduleLE`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L208).

> The filtration reduces to its span, at every bound up to eight. The filtration is a
> join of the graded pieces, each of them stable under both groups, and `ReducesInvariantsTo` is
> closed under joins in its source, so the weights are taken one at a time, each in turn joining the
> error term of the others. At positive weight the graded reduction of `Invariants.lean` is
> used; at weight zero a submodule reduces to itself, the constant term being carried in the
> span.

```lean
lemma reducesInvariantsTo_massWeightSubmoduleLE {w : ℕ} (hw : w ≤ 8) :
    ReducesInvariantsTo (gaugeLorentzMaps repGaugeGroupI repLorentzGroup) (massWeightSubmoduleLE w)
      (standardModelSpanLE w)
```

**`StandardModel.LocalCovFieldAlgebra.mem_standardModelSpanLE_eight_of_mem_sector`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L228).

> An element of a sector of mass weight at most eight fixed by both groups lies in the span
> of the filtration at bound eight. Its weight components lie in the weight pieces of the
> sector and are fixed by both groups. The weight-zero component is a constant, and every other
> component lies in the Standard-Model span of its weight by the sector's reduction.

```lean
lemma mem_standardModelSpanLE_eight_of_mem_sector {A : Finset GaugeFieldData.FieldKind}
    {y : fieldData.LocalCovFieldAlgebra} (hyA : y ∈ fieldData.sector A)
    (hyLE : y ∈ massWeightSubmoduleLE 8)
    (hG : ∀ g : GaugeGroupI, repGaugeGroupI g y = y) (hL : ∀ Λ : SL(2,ℂ), repLorentzGroup Λ y = y) :
    y ∈ standardModelSpanLE 8
```

## E. The classification up to mass dimension four

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmoduleLE_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L266).

> The classification of the Standard Model up to mass weight `w ≤ 8` as an equivalence,
> in the shape every sector uses. An element of `massWeightSubmoduleLE w ⊔ S`, with `S`
> stable under both groups, is fixed by both groups exactly when it is a combination of
> the constant term and the Standard-Model terms of weight at most `w`, up to a remainder
> in `S` fixed by both groups.

```lean
lemma mem_massWeightSubmoduleLE_sup_and_gauge_lorentz_invariant_iff (w : ℕ) (hw : w ≤ 8)
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmoduleLE w ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ standardModelSpanLE w
```

**`StandardModel.LocalCovFieldAlgebra.exists_mem_standardModelSpanLE_of_gauge_and_lorentz_invariant`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L285).

> The gauge and Lorentz invariants of mass weight at most `w`, for `w ≤ 8`, modulo a
> submodule `S` stable under both groups. Such an invariant is a combination of the
> constant term and the Standard-Model terms of weight at most `w`, plus a remainder in
> `S`, and the remainder is fixed by both groups as well, being the difference of two
> invariants.

```lean
lemma exists_mem_standardModelSpanLE_of_gauge_and_lorentz_invariant (w : ℕ) (hw : w ≤ 8)
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) {x : fieldData.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmoduleLE w ⊔ S)
    (hG : ∀ g : GaugeGroupI, repGaugeGroupI g x = x)
    (hL : ∀ g : SL(2,ℂ), repLorentzGroup g x = x) :
    ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
      ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
      ∧ x - y ∈ standardModelSpanLE w
```

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmoduleLE_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L301).

> The same classification without the existential. At every bound up to eight an element
> of `massWeightSubmoduleLE w ⊔ S` fixed by both groups is an element of the span of the
> filtration joined with `S` fixed by both groups, and conversely.

```lean
lemma mem_massWeightSubmoduleLE_sup_and_gauge_lorentz_invariant_iff_mem (w : ℕ)
    (hw : w ≤ 8) (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmoduleLE w ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ (x ∈ standardModelSpanLE w ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
```

## F. The Standard Model Lagrangian with its constant and mass terms

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L325).

> The classification at bound eight, that is at mass dimension at most four, as an
> equivalence. An element of `massWeightSubmoduleLE 8 ⊔ S`, with `S` stable under both
> groups, is fixed by both groups exactly when it lies in the span of the filtration up to
> a remainder in `S` fixed by both groups.

```lean
lemma mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmoduleLE 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ standardModelSpanLE 8
```

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff_mem`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L337).

> The same at bound eight without the existential.

```lean
lemma mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff_mem
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmoduleLE 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ (x ∈ standardModelSpanLE 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
          ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
```

**`StandardModel.LocalCovFieldAlgebra.mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean#L361).

> The invariant content of the Standard Model up to mass dimension four. An element of
> `massWeightSubmoduleLE 8 ⊔ S`, for `S` a submodule stable under both groups, is fixed by
> the gauge group and the Lorentz group exactly when it is a combination of
> the constant term, of mass dimension zero,
> the Higgs mass term `H† H`, of mass dimension two (`ScalarSector.dotSpan`),
> and the dimension-four span — the four Lorentz contractions of the three `F·F` trace
> families and of the twice-derived hypercharge field strength, among them the gauge
> kinetic and theta terms (`GaugeSector.lorentzContractionEightSpan`), the Higgs
> kinetic term, its quartic potential and its two box terms
> (`ScalarSector.lorentzContractionEightSpan`), the kinetic terms of the ten fermion
> species over the nine family pairs (`FermionSector.kineticSpan`), and the six Yukawa
> couplings over the nine family pairs (`yukawaSpan`) —
> up to a remainder in `S` fixed by both groups, and nothing else. The generators span;
> they are not shown to be independent, and no quotient by total derivatives is taken.

```lean
lemma mem_massWeightSubmoduleLE_eight_sup_and_gauge_lorentz_invariant_iff_lagrangian
    (S : Submodule ℂ fieldData.LocalCovFieldAlgebra)
    (hS : ∀ g : GaugeGroupI, ∀ y ∈ S, repGaugeGroupI g y ∈ S)
    (hSL : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentzGroup g y ∈ S) (x : fieldData.LocalCovFieldAlgebra) :
    (x ∈ massWeightSubmoduleLE 8 ⊔ S ∧ (∀ g : GaugeGroupI, repGaugeGroupI g x = x)
        ∧ ∀ g : SL(2,ℂ), repLorentzGroup g x = x)
      ↔ ∃ y ∈ S, (∀ g : GaugeGroupI, repGaugeGroupI g y = y)
          ∧ (∀ g : SL(2,ℂ), repLorentzGroup g y = y)
          ∧ x - y ∈ (1 : Submodule ℂ fieldData.LocalCovFieldAlgebra) ⊔ (ScalarSector.dotSpan 0 0
              ⊔ (GaugeSector.lorentzContractionEightSpan
                    ⊔ ScalarSector.lorentzContractionEightSpan
                  ⊔ (FermionSector.kineticSpan ⊔ yukawaSpan)))
```

## Depends on

- [The invariant content of the Standard Model](localfieldalgebra-localcovfieldalgebra-massweigh-3.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight/Filtration.lean)
