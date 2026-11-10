---
declaration: section
origin: cited
lean: Stacks.Cohomology.existsUnique_cechRestrictionHomologyMap, Stacks.Cohomology.isZero_homology_cechComplex_of_injective, Stacks.Cohomology.CechSheaf.existsUnique_cechRestrictionHomologyMap, Stacks.Cohomology.CechSheaf.isZero_cechComplex_homology_of_injective, Stacks.Cohomology.CechDerived.cechToDerivedGlobalSections, Stacks.Cohomology.CechDerived.cechCohomologyToCohomology, Stacks.Cohomology.CechDerived.nonempty_cechResolutionComparison, Stacks.Cohomology.CechOne.cechH1ToRightDerivedSections
statement: formalized
proof: formalized
---

# 20.11 Čech cohomology and cohomology

Section 20.11 of the Stacks Project, [Tag 01EO](https://stacks.math.columbia.edu/tag/01EO). 12 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01EP, a lemma

[Tag 01EP](https://stacks.math.columbia.edu/tag/01EP) in the Stacks Project.

**`Stacks.Cohomology.existsUnique_cechRestrictionHomologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/CechModules.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/CechModules.lean#L250). The attribute's comment: “degree zero”.

> There is a unique `R(V)`-linear map from the sections of `I` over the covered open `V` to
> the degree `0` Čech cohomology whose composite with the inclusion of the homology into the
> opcycles is induced by the restriction map, and it is an isomorphism.

```lean
theorem existsUnique_cechRestrictionHomologyMap (V : Opens X) (U : ι → Opens X)
    (hU : V = ⨆ i, U i) (I : SheafOfModules.{uM} R) :
    ∃! f : (SheafOfModules.evaluation R (op V)).obj I ⟶ (cechComplex V U hU I).homology 0,
      IsIso f ∧ f ≫ (cechComplex V U hU I).homologyι 0 =
        cechDegreeZeroRestriction V U hU I ≫ (cechComplex V U hU I).pOpcycles 0
```

**`Stacks.Cohomology.isZero_homology_cechComplex_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/CechModulesInjective.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/CechModulesInjective.lean#L187). The attribute's comment: “positive degrees”.

> **Stacks Project, Tag 01EP, positive degrees.** The cohomology of the module-valued Čech
> complex of an injective sheaf of modules, for a covering of an open subset `V` by a family
> `U`, vanishes in every positive degree.
>
> An injective sheaf of modules is injective as a presheaf of modules, so it splits off its
> global cofree hull; the restriction of that hull to the opens over `V` is a product of cofree
> presheaves of `R(V)`-modules and of zero presheaves, whose positive-degree Čech cohomology
> vanishes.

```lean
theorem isZero_homology_cechComplex_of_injective (V : Opens X) (U : ι → Opens X)
    (hU : V = ⨆ i, U i) (I : SheafOfModules.{uM} R) [Injective I] (n : ℕ) (hn : 0 < n) :
    IsZero ((cechComplex V U hU I).homology n)
```

**`Stacks.Cohomology.CechSheaf.existsUnique_cechRestrictionHomologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfSheavesOfModules/DegreeZeroUniqueIsomorphism.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechOfSheavesOfModules/DegreeZeroUniqueIsomorphism.lean#L150). The attribute's comment: “degree zero”.

> **The degree-zero clause of [Stacks, Tag 01EP].**  There is a unique `R(V)`-linear map from
> the sections of `ℱ` on the covered open to degree-zero Čech cohomology whose composite with the
> inclusion of homology into the degree-zero opcycles is the restriction map to the cover, and
> that map is an isomorphism.
>
> Existence is `homologyZeroIso`, which is the sheaf condition for the cover: the augmentation
> is a kernel of the first Čech differential.  Uniqueness is the monomorphy of
> `HomologicalComplex.homologyι`.

```lean
theorem existsUnique_cechRestrictionHomologyMap :
    ∃! f : (SheafOfModules.evaluation.{uM} R (op V)).obj I ⟶ (cechComplex V U hU I).homology 0,
      IsIso f ∧
        f ≫ (cechComplex V U hU I).homologyι 0 =
          cechDegreeZeroRestriction V U hU I ≫ (cechComplex V U hU I).pOpcycles 0
```

**`Stacks.Cohomology.CechSheaf.isZero_cechComplex_homology_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfSheavesOfModules/InjectiveVanishing.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechOfSheavesOfModules/InjectiveVanishing.lean#L400). The attribute's comment: “positive degrees”.

> **Stacks 01EP, positive degrees.** The positive-degree module-valued Čech cohomology of an
> injective sheaf of modules vanishes.

```lean
public theorem isZero_cechComplex_homology_of_injective
    (V : Opens X) (U : ι → Opens X) (hU : V = ⨆ i, U i)
    (I : SheafOfModules.{uM} R) [Injective I] (p : ℕ) (hp : 0 < p) :
    IsZero ((cechComplex V U hU I).homology p)
```

## Tag 01EQ, a lemma

[Tag 01EQ](https://stacks.math.columbia.edu/tag/01EQ) in the Stacks Project.

**`Stacks.Cohomology.CechDerived.cechToDerivedGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/ComparisonToDerivedSections.lean, line 763](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/ComparisonToDerivedSections.lean#L763). The attribute's comment: “the derived transformation”. References: EGA 0 (12.1.2), “A-linear Č^p → H^p maps”.

> **The canonical natural transformation from the Čech complex of an open cover to derived
> global sections on the covered open.**
>
> It is built at an injective resolution chosen for each sheaf of modules; it is natural because
> the two augmentations and the identification of the sections of a resolution with derived
> sections are each natural in the resolution.

```lean
def cechToDerivedGlobalSections :
    cechComplexPlusFunctor O U Ui hU ⋙ DerivedCategory.Plus.Q ⟶
      derivedGlobalSectionsFunctor O U
```

**`Stacks.Cohomology.CechDerived.cechCohomologyToCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/ComparisonToDerivedSections.lean, line 774](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/ComparisonToDerivedSections.lean#L774). The attribute's comment: “the induced cohomology maps”. References: EGA 0 (12.1.2), “A-linear Ȟ^p → H^p”.

> **The canonical maps from Čech cohomology to sheaf cohomology**, natural in the sheaf of
> modules.

```lean
def cechCohomologyToCohomology (p : ℤ) :
    (cechComplexPlusFunctor O U Ui hU ⋙ DerivedCategory.Plus.Q ⋙
        DerivedCategory.Plus.homologyFunctor _ p) ⟶
      (derivedGlobalSectionsFunctor O U ⋙
        DerivedCategory.Plus.homologyFunctor _ p)
```

**`Stacks.Cohomology.CechDerived.nonempty_cechResolutionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/ComparisonToDerivedSections.lean, line 785](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/ComparisonToDerivedSections.lean#L785). The attribute's comment: “the injective-resolution specification”.

> **For every injective resolution, the canonical comparison is the map prescribed by the
> total Čech complex construction.**  In particular it is independent of the resolution.

```lean
theorem nonempty_cechResolutionComparison (F : SheafOfModules.{u} O)
    (J : InjectiveResolution F) :
    Nonempty (CechResolutionComparison O U Ui hU
      (cechToDerivedGlobalSections O U Ui hU) F J)
```

**`Stacks.Cohomology.CechOne.cechH1ToRightDerivedSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/DegreeOneComparison.lean, line 852](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/DegreeOneComparison.lean#L852). The attribute's comment: “the additive-sheaf degree-one comparison”.

> The canonical additive comparison from the Čech quotient to the first
> right-derived functor of sections, for an arbitrary abelian sheaf.

```lean
noncomputable def cechH1ToRightDerivedSections
    {I : Type w}
    (U : Opens X) (Ui : I → Opens X) (hUi : U = ⨆ i, Ui i)
    (H : TopCat.Sheaf AddCommGrpCat.{max uX v} X) :
    CechCochains.CechH1 Ui H.presheaf →+
      (((sheafSections (Opens.grothendieckTopology X) AddCommGrpCat.{max uX v}).obj
        (op U)).rightDerived 1).obj H
```

**`Stacks.Cohomology.CechOne.exists_cechOneResolutionRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/DegreeOneComparison.lean, line 874](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/DegreeOneComparison.lean#L874). The attribute's comment: “the additive-sheaf injective-resolution specification”.

> Every Čech cocycle admits the representative prescribed by the total-complex
> construction, in every injective resolution, and its class is the comparison image.

```lean
theorem exists_cechOneResolutionRepresentative
    {I : Type w}
    (U : Opens X) (Ui : I → Opens X) (hUi : U = ⨆ i, Ui i)
    (H : TopCat.Sheaf AddCommGrpCat.{max uX v} X) (J : InjectiveResolution H)
    (z : CechCochains.cocycles1 Ui H.presheaf) :
    ∃ r : CechOneResolutionRepresentative X U Ui hUi H J z,
      cechH1ToRightDerivedSections X U Ui hUi H (CechCochains.cls Ui H.presheaf z) =
        (@InjectiveResolution.isoRightDerivedObj _ _ AddCommGrpCat.{max uX v} _ _ _ _ H J
          ((sheafSections (Opens.grothendieckTopology X) AddCommGrpCat.{max uX v}).obj
            (op U)) (inferInstanceAs
              (sheafToPresheaf (Opens.grothendieckTopology X) AddCommGrpCat.{max uX v} ⋙
                (evaluation (Opens X)ᵒᵖ AddCommGrpCat.{max uX v}).obj (op U)).Additive) 1).inv
          ((abelianResolutionSections X U J).homologyπ 1 r.cycle)
```

**`Stacks.Cohomology.CechOne.cechH1ToRightDerivedSections_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/DegreeOneComparison.lean, line 895](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/DegreeOneComparison.lean#L895). The attribute's comment: “calculation of the additive-sheaf comparison”.

> Any injective-resolution representative computes the canonical comparison;
> neither the chosen zero-cochain nor the chosen resolution changes its value.

```lean
theorem cechH1ToRightDerivedSections_apply
    {I : Type w} (U : Opens X) (Ui : I → Opens X) (hUi : U = ⨆ i, Ui i)
    (H : TopCat.Sheaf AddCommGrpCat.{max uX v} X) (J : InjectiveResolution H)
    (z : CechCochains.cocycles1 Ui H.presheaf)
    (r : CechOneResolutionRepresentative X U Ui hUi H J z) :
    cechH1ToRightDerivedSections X U Ui hUi H (CechCochains.cls Ui H.presheaf z) =
      (@InjectiveResolution.isoRightDerivedObj _ _ AddCommGrpCat.{max uX v} _ _ _ _ H J
        ((sheafSections (Opens.grothendieckTopology X) AddCommGrpCat.{max uX v}).obj
          (op U)) (inferInstanceAs
              (sheafToPresheaf (Opens.grothendieckTopology X) AddCommGrpCat.{max uX v} ⋙
                (evaluation (Opens X)ᵒᵖ AddCommGrpCat.{max uX v}).obj (op U)).Additive) 1).inv
        ((abelianResolutionSections X U J).homologyπ 1 r.cycle)
```

**`Stacks.Cohomology.CechOne.cechH1ToRightDerivedSections_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/DegreeOneComparison.lean, line 912](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/DegreeOneComparison.lean#L912). The attribute's comment: “naturality of the additive-sheaf degree-one comparison”.

> Naturality of the additive-sheaf comparison, expressed on Čech cocycles.

```lean
theorem cechH1ToRightDerivedSections_naturality
    {I : Type w}
    (U : Opens X) (Ui : I → Opens X) (hUi : U = ⨆ i, Ui i)
    {H G : TopCat.Sheaf AddCommGrpCat.{max uX v} X} (f : H ⟶ G)
    (z : CechCochains.cocycles1 Ui H.presheaf) (z' : CechCochains.cocycles1 Ui G.presheaf)
    (hz : ∀ i : Fin 2 → I,
      z'.val i = (f.hom.app (op (CechCochains.inter Ui i))) (z.val i)) :
    (((sheafSections (Opens.grothendieckTopology X) AddCommGrpCat.{max uX v}).obj
      (op U)).rightDerived 1).map f
        (cechH1ToRightDerivedSections X U Ui hUi H (CechCochains.cls Ui H.presheaf z)) =
      cechH1ToRightDerivedSections X U Ui hUi G (CechCochains.cls Ui G.presheaf z')
```

## Tag 0B8R, a lemma

[Tag 0B8R](https://stacks.math.columbia.edu/tag/0B8R) in the Stacks Project.

**`Stacks.Cohomology.SheafTorsor.cechH1EquivLocallyTrivialTorsorClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/LocalTriviality.lean, line 737](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/LocalTriviality.lean#L737). The attribute's comment: “identification with locally trivial torsors”. References: EGA IV (16.5.15), “partial”; SGA 4½ Cycle (1.1.2), “cocycle ↔ torsor class”.

> **Stacks Project, Tag 0B8R.** First Čech cohomology of an open covering is in canonical
> bijection with the set of isomorphism classes of torsors which are trivial on every member of
> the covering.

```lean
def cechH1EquivLocallyTrivialTorsorClass :
    CechCochains.CechH1 Ui H.presheaf ≃ {c : TorsorClass X H // IsLocallyTrivialOn H Ui c}
```

**`Stacks.Cohomology.SheafTorsor.torsorClassEquivSheafCohomologyOne_cechH1Equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/LocalTriviality.lean, line 748](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/LocalTriviality.lean#L748). The attribute's comment: “identification with locally trivial torsors”.

> **Stacks Project, Tag 0B8R.** The bijection of
> `cechH1EquivLocallyTrivialTorsorClass` is the one induced by the canonical comparison to first
> sheaf cohomology and the classification of torsors of Tag 02FQ.

```lean
theorem torsorClassEquivSheafCohomologyOne_cechH1Equiv (z : CechCochains.CechH1 Ui H.presheaf) :
    torsorClassEquivSheafCohomologyOne X H
        (cechH1EquivLocallyTrivialTorsorClass H Ui hUi z).1 =
      CechOne.cechH1ToRightDerivedSections X ⊤ Ui hUi H z
```

**`Stacks.Cohomology.SheafTorsor.cechH1ToRightDerivedSections_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/LocalTriviality.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/LocalTriviality.lean#L757). The attribute's comment: “injectivity”.

> **Stacks Project, Tag 0B8R.** The canonical additive comparison from first Čech cohomology
> of an open covering to first sheaf cohomology is injective.

```lean
theorem cechH1ToRightDerivedSections_injective :
    Function.Injective (CechOne.cechH1ToRightDerivedSections X ⊤ Ui hUi H)
```

Declarations registered for the tag:

- [`Stacks.Cohomology.CechOne.cechH1ToRightDerivedSections`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/DegreeOneComparison.lean#L852), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/LocalTriviality.lean, line 768](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/LocalTriviality.lean#L768) (StacksFrontier): “the canonical comparison map”.

## Tag 01ER, a lemma

[Tag 01ER](https://stacks.math.columbia.edu/tag/01ER) in the Stacks Project.

**`Stacks.Cohomology.DerivedForget.rightDerivedForgetEvaluationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/ForgetfulInclusionCohomologyPresheaf.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/ForgetfulInclusionCohomologyPresheaf.lean#L110). The attribute's comment: “right derived functors”.

> **Stacks 01ER.** The value on `U` of the `p`-th right derived functor of the inclusion
> `Mod(O) ⟶ PMod(O)` is canonically the `p`-th right derived functor of sections on `U`. The
> isomorphism is natural in the coefficient sheaf.

```lean
noncomputable def rightDerivedForgetEvaluationIso (U : Opens X) (p : ℕ) :
    (SheafOfModules.forget O).rightDerived p ⋙
        PresheafOfModules.evaluation O.obj (op U) ≅
      (SheafOfModules.evaluation O (op U)).rightDerived p
```

**`Stacks.Cohomology.DerivedForget.rightDerivedForgetCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/ForgetfulInclusionCohomologyPresheaf.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/ForgetfulInclusionCohomologyPresheaf.lean#L122). The attribute's comment: “cohomology presheaf”.

> **Stacks 01ER.** After forgetting the module structure, the value on `U` of the `p`-th
> right derived functor of `Mod(O) ⟶ PMod(O)` is canonically `H^p(U, -)`. This is an isomorphism
> of functors in the coefficient sheaf.

```lean
noncomputable def rightDerivedForgetCohomologyIso (U : Opens X) (p : ℕ) :
    (SheafOfModules.forget O).rightDerived p ⋙
        PresheafOfModules.toPresheaf O.obj ⋙
        (evaluation (Opens X)ᵒᵖ AddCommGrpCat).obj (op U) ≅
      Hfunctor O U p
```

**`Stacks.Cohomology.DerivedForget.rightDerivedForgetCohomologyIso_naturality_open`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/ForgetfulInclusionCohomologyPresheaf.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/ForgetfulInclusionCohomologyPresheaf.lean#L137). The attribute's comment: “compatibility with restriction”.

> **Stacks 01ER.** The canonical identification of the derived presheaf with
> `U ↦ H^p(U, -)` commutes with restriction from an open subset `V` to an open subset `U`.

```lean
lemma rightDerivedForgetCohomologyIso_naturality_open
    {U V : Opens X} (h : U ≤ V) (p : ℕ) (F : SheafOfModules O) :
    ((PresheafOfModules.toPresheaf O.obj).obj
          (((SheafOfModules.forget O).rightDerived p).obj F)).map (homOfLE h).op ≫
        (rightDerivedForgetCohomologyIso O U p).hom.app F =
      (rightDerivedForgetCohomologyIso O V p).hom.app F ≫ Hrestrict O h p F
```

Declarations registered for the tag:

- [`SheafOfModules.Finite.forgetPreservesFiniteLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.Finite.forgetPreservesFiniteLimits#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/ForgetfulInclusionCohomologyPresheaf.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/ForgetfulInclusionCohomologyPresheaf.lean#L67) (StacksFrontier): “left exact”.

## Tag 01ES, a lemma

[Tag 01ES](https://stacks.math.columbia.edu/tag/01ES) in the Stacks Project.

**`Stacks.Cohomology.CechSpectral.cechSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechSpectralSequence/Assembled.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechSpectralSequence/Assembled.lean#L124). References: SGA 4 V (3.2), “ringed space, open cover”.

> **The functorial Čech spectral sequence of an open covering**, with second page
> `Ȟ^p(𝒰, H^q(ℱ))` and abutment `H^{p+q}(U, ℱ)`.
>
> This is [Stacks, Tag 01ES]: the four fields are `SheafOfModules.enoughInjectives_opens`,
> `cechSpectralSequenceFunctor`, `cechPageTwoIso` and `cechAbutment`.

```lean
def cechSpectralSequence : CechSpectralSequenceData.{u, r, v, w} O 𝒰
```

## Tag 01ET, a lemma

[Tag 01ET](https://stacks.math.columbia.edu/tag/01ET) in the Stacks Project.

**`Stacks.Cohomology.CechAcyclic.isIso_cechCohomologyToCohomology_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/AcyclicCovering.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/AcyclicCovering.lean#L503). The attribute's comment: “the comparison of Tag 01EQ is an isomorphism in every degree”.

> An open covering whose nonempty finite intersections are acyclic for a module sheaf
> computes the cohomology of that sheaf by its Čech complex.
>
> This is the whole of [Stacks, Tag 01ET]: the source's equality `Ȟᵖ(𝒰, ℱ) = Hᵖ(U, ℱ)` of
> `𝒪_X(U)`-modules is read here as the canonical comparison of [Stacks, Tag 01EQ] being an
> isomorphism, both sides living in the derived category of `𝒪_X(U)`-modules.  `hacyclic` is the
> acyclicity of `ℱ` on the intersections `U_{i₀ … i_r}`, and the two instance binders are
> synthesizable for any topological space.

```lean
theorem isIso_cechCohomologyToCohomology_app
    [HasSheafify (Opens.grothendieckTopology X) AddCommGrpCat.{u}]
    [(Opens.grothendieckTopology X).WEqualsLocallyBijective AddCommGrpCat.{u}]
    (F : SheafOfModules.{u} O)
    (hacyclic : ∀ (r : ℕ) (s : Fin (r + 1) → I) (q : ℕ), 0 < q →
      IsZero (((SheafOfModules.evaluation.{u} O (op (⨅ k, Ui (s k)))).rightDerived q).obj F))
    (p : ℕ) :
    IsIso ((cechCohomologyToCohomology O U Ui hU (p : ℤ)).app F)
```

## Tag 01EU, a lemma

[Tag 01EU](https://stacks.math.columbia.edu/tag/01EU) in the Stacks Project.

**`Stacks.Cohomology.CechDegreeOneVanishing.cech_h1_vanishing_implies_surjective_on_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/DegreeOneVanishingGluesSections.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/DegreeOneVanishingGluesSections.lean#L412).

> **Theorem (Stacks project, Tag 01EU; Lemma 20.11.7).** Let `X` be a (ringed) space and
> `0 → F → G → H → 0` a short exact sequence of abelian sheaves on `X` (the underlying short exact
> sequence of the given short exact sequence of `O_X`-modules), encoded as a short exact
> `ShortComplex` `S` with `S.X₁ = F`, `S.X₂ = G`, `S.X₃ = H`, `S.f = a`, `S.g = b`. Let `U ⊆ X` be
> open and suppose there is a cofinal system `𝒮` of open coverings of `U` with `Ȟ¹(𝒰, F) = 0` for
> every `𝒰 ∈ 𝒮`. Then the map on sections over `U` induced by `b`, `b_U : G(U) → H(U)`, is
> surjective.

```lean
theorem cech_h1_vanishing_implies_surjective_on_sections
    (S : ShortComplex (TopCat.Sheaf AddCommGrpCat X)) (hS : S.ShortExact)
    (U : Opens X)
    (𝒮 : Set (OpenCovering U)) (hcof : CofinalCoveringSystem 𝒮)
    (hH1 : ∀ 𝒰 ∈ 𝒮, CechH1IsZero (S.X₁.1) 𝒰) :
    Function.Surjective
      (((TopCat.Sheaf.forget AddCommGrpCat X).map S.g).app (op U))
```

## Tag 01EV, a lemma

[Tag 01EV](https://stacks.math.columbia.edu/tag/01EV) in the Stacks Project.

**`Stacks.Cohomology.CechVanishing.isZero_rightDerived_sections_of_isZero_cechHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechVanishingCriteria/FromCechVanishing.lean, line 794](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechVanishingCriteria/FromCechVanishing.lean#L794).

> **Stacks Project, Tag 01EV.** If all positive-degree Čech cohomology of a sheaf
> of modules vanishes, then every positive right-derived functor of sections vanishes.

```lean
public theorem isZero_rightDerived_sections_of_isZero_cechHomology
    {X : Type u} [TopologicalSpace X] [UnivLE.{u, v}]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{v})
    (F : SheafOfModules.{v} R)
    (hF : ∀ {I : Type (max u v)} (U : I → Opens X) (p : ℕ), 0 < p →
      IsZero (((cechComplexFunctor U).obj
        (F.val.presheaf ⋙ AddCommGrpCat.uliftFunctor.{u, v})).homology p)) :
    ∀ (U : Opens X) (p : ℕ), 0 < p →
      IsZero ((((SheafOfModules.toSheaf R ⋙
        (sheafSections (Opens.grothendieckTopology X) AddCommGrpCat.{v}).obj
          (op U)).rightDerived p).obj F))
```

## Tag 01EW, a lemma

[Tag 01EW](https://stacks.math.columbia.edu/tag/01EW) in the Stacks Project.

**`Stacks.Cohomology.BasisCycles.isZero_hgroup_of_cech_isZero_on_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechVanishingCriteria/OnABasis.lean, line 751](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechVanishingCriteria/OnABasis.lean#L751).

> **Stacks Tag 01EW.** Let `B` be a basis of open subsets of a ringed space and let `Cov` be a
> collection of open covers by members of `B` whose finite intersections also lie in `B`.  If every
> open cover of a member of `B` is refined by a member of `Cov` covering it, and the positive-degree
> Čech cohomology of `F` vanishes for every cover in `Cov`, then the higher cohomology of `F`
> vanishes over every member of `B`.
>
> This is the case `T = SheafOfModules.toSheaf R` of `isZero_Hobj_of_cech_isZero_on_basis`: the
> Čech acyclicity of the injective objects is `cechAcyclicInjectives_toSheaf`, Stacks 01EA followed
> by Stacks 09SZ.
>
> The hypothesis that `B` is a basis is not needed: the cofinality hypothesis `hCovCofinal` already
> provides all the covers the proof uses.  It is kept because it is part of the statement of the
> tag.

```lean
theorem isZero_hgroup_of_cech_isZero_on_basis (F : SheafOfModules.{max u w} R)
    (B : Set (Opens X)) (_hB : Opens.IsBasis B) (Cov : Set (OpenCover X))
    (hCovBasis : ∀ U ∈ Cov, U.carrier ∈ B ∧ (∀ i, U.obj i ∈ B) ∧
      ∀ (p : ℕ) (s : Fin (p + 1) → U.ι), (⨅ k, U.obj (s k)) ∈ B)
    (hCovCofinal : ∀ U ∈ B, ∀ V : OpenCover X, V.carrier = U →
      ∃ W ∈ Cov, W.carrier = U ∧ W.Refines V)
    (hCech : ∀ U ∈ Cov, ∀ n : ℕ, 0 < n → CechCohomologyIsZero R F U n)
    (U : Opens X) (hU : U ∈ B) (n : ℕ) (hn : 0 < n) :
    IsZero (Hgroup R U n F)
```

## Tag 01EX, a lemma

[Tag 01EX](https://stacks.math.columbia.edu/tag/01EX) in the Stacks Project.

**`Stacks.Cohomology.PushforwardAcyclic.pushforward_injective_rightAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/PushforwardOfAnInjective.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/PushforwardOfAnInjective.lean#L95). The attribute's comment: “part (2)”.

> **Stacks 01EX, part (2).** The pushforward of an injective module is right acyclic for
> the sections functor on every open subset.

```lean
public theorem pushforward_injective_rightAcyclic
    {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (I : SheafOfModules.{u} (structureSheafRing X)) [Injective I]
    (V : Opens Y.carrier) :
    (SheafOfModules.evaluation (structureSheafRing Y) (op V)).rightAcyclic
      ((RingedSpaceModuleAdjunction.modulePushforward f).obj I)
```

**`Stacks.Cohomology.PushforwardAcyclic.pushforward_injective_cechCohomology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/PushforwardOfAnInjectiveCechVanishing.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/PushforwardOfAnInjectiveCechVanishing.lean#L53). The attribute's comment: “part (1)”.

> **Stacks 01EX, part (1).** The positive-degree Čech cohomology of the pushforward of an
> injective module vanishes for every family of opens, and hence for every open covering.

```lean
public theorem pushforward_injective_cechCohomology_isZero
    {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (I : SheafOfModules.{u} (structureSheafRing X)) [Injective I]
    {J : Type u} (U : J → Opens Y.carrier) (p : ℕ) (hp : 0 < p) :
    IsZero (((cechComplexFunctor U).obj
      ((RingedSpaceModuleAdjunction.modulePushforward f).obj I).val.presheaf).homology p)
```

## Tag 02N5, a lemma

[Tag 02N5](https://stacks.math.columbia.edu/tag/02N5) in the Stacks Project.

**`RingedSpaceModuleAdjunction.modulePushforward_preservesInjectiveObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/FlatPullback.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/FlatPullback.lean#L102).

> **Pushforward along a flat morphism of ringed spaces preserves injective modules.** The left
> adjoint `f^*` of `f_*` is exact, and a functor with an exact left adjoint preserves injective
> objects.

```lean
theorem modulePushforward_preservesInjectiveObjects (hf : AlgebraicGeometry.IsFlat f) :
    (modulePushforward f).PreservesInjectiveObjects
```

## Tag 0D0A, a lemma

[Tag 0D0A](https://stacks.math.columbia.edu/tag/0D0A) in the Stacks Project.

**`Stacks.Cohomology.ModuleComparison.isIso_piComparison_rightDerivedPlus_evaluation_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/CohomologyOfAProduct.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/CohomologyOfAProduct.lean#L274). The attribute's comment: “degree zero”.

> **Degree-zero cohomology of modules on a ringed space commutes with arbitrary products**:
> the canonical map from the degree-zero cohomology over an open `U` of a product of sheaves of
> modules to the product of their degree-zero cohomologies is an isomorphism.

```lean
theorem isIso_piComparison_rightDerivedPlus_evaluation_zero
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (U : Opens X)
    {I : Type u} (F : I → SheafOfModules.{u} O) :
    IsIso (piComparison ((SheafOfModules.evaluation O (op U)).rightDerivedPlus 0) F)
```

**`Stacks.Cohomology.ModuleComparison.mono_piComparison_rightDerivedPlus_evaluation_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/CohomologyOfAProduct.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/CohomologyOfAProduct.lean#L284). The attribute's comment: “degree one”.

> **Degree-one cohomology of modules on a ringed space injects into the product**: the
> canonical map from the degree-one cohomology over an open `U` of a product of sheaves of
> modules to the product of their degree-one cohomologies is a monomorphism.

```lean
theorem mono_piComparison_rightDerivedPlus_evaluation_one
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (U : Opens X)
    {I : Type u} (F : I → SheafOfModules.{u} O) :
    Mono (piComparison ((SheafOfModules.evaluation O (op U)).rightDerivedPlus 1) F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.11, Tag 01EO](https://stacks.math.columbia.edu/tag/01EO)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
