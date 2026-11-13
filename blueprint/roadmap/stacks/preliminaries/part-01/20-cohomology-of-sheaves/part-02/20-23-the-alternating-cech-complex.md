---
declaration: section
origin: cited
lean: CechCochains.alternatingSubgroup, CechCochains.cechD_mem_alternating, Stacks.Cech.alternatingCechComplex, Stacks.Cech.alternatingCechInclusion, Stacks.Cech.orderedCechComplex, CechCochains.cAddEquiv, CechCochains.c_chainMap, Stacks.Cech.orderedIsoAlternatingCechComplex
statement: formalized
proof: formalized
---

# 20.23 The alternating Čech complex

Section 20.23 of the Stacks Project, [Tag 01FG](https://stacks.math.columbia.edu/tag/01FG). 7 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01FG, the section

[Tag 01FG](https://stacks.math.columbia.edu/tag/01FG) in the Stacks Project.

**`CechCochains.alternatingSubgroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingCochainGroups.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingCochainGroups.lean#L193). The attribute's comment: “the group `Č_alt^p(𝒰, ℱ)` of alternating cochains”.

> The alternating cochains form a subgroup `Č_alt^p ⊆ Č^p`.

```lean
def alternatingSubgroup (p : ℕ) : AddSubgroup (Cochain U ℱ p)
```

**`CechCochains.cechD_mem_alternating`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingCochainGroups.lean, line 687](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingCochainGroups.lean#L687). The attribute's comment: “`d` maps `Č_alt^p` into `Č_alt^{p+1}`, the verification the source omits”.

> The differential `cechD` preserves the alternating subgroup, so the latter is a
> subcomplex of the full Čech complex.

```lean
theorem cechD_mem_alternating (p : ℕ) (s : Cochain U ℱ p) (hs : IsAlternating U ℱ s) :
    IsAlternating U ℱ (cechD U ℱ p s)
```

## Tag 01FH, a definition

[Tag 01FH](https://stacks.math.columbia.edu/tag/01FH) in the Stacks Project.

**`Stacks.Cech.alternatingCechComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingComplex.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingComplex.lean#L129). References: EGA 0 (12.1.2), “alternating Čech complex”.

> **Stacks 01FH.** The alternating Čech complex associated to an abelian presheaf and an
> indexed family of open subsets.

```lean
noncomputable def alternatingCechComplex : CochainComplex Ab ℕ
```

**`Stacks.Cech.alternatingCechInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingComplex.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingComplex.lean#L153). The attribute's comment: “the canonical inclusion”.

> **Stacks 01FH.** The canonical inclusion of the alternating Čech complex into the usual
> Čech complex: in each degree it is the inclusion of the subgroup of alternating cochains.

```lean
noncomputable def alternatingCechInclusion :
    alternatingCechComplex U ℱ ⟶ cechComplex U ℱ
```

## Tag 01FI, a definition

[Tag 01FI](https://stacks.math.columbia.edu/tag/01FI) in the Stacks Project.

**`Stacks.Cech.orderedCechComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/OrderedComplex.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/OrderedComplex.lean#L57).

> The ordered Čech cochain complex of an abelian presheaf with respect to a linearly
> ordered family of open subsets.

```lean
noncomputable def orderedCechComplex (U : I → Opens X)
    (ℱ : TopCat.Presheaf AddCommGrpCat.{w} X) :
    CochainComplex AddCommGrpCat.{max v w} ℕ
```

## Tag 01FJ, a lemma

[Tag 01FJ](https://stacks.math.columbia.edu/tag/01FJ) in the Stacks Project.

**`CechCochains.cAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingCochainGroups.lean, line 498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingCochainGroups.lean#L498). The attribute's comment: “the degreewise isomorphism”.

> (3) **[Stacks, Tag 01FJ], the degreewise clause.** In every degree, `c` corestricted to the
> alternating subgroup is an isomorphism of abelian groups `Č_ord^p ≃+ Č_alt^p`, with inverse the
> projection `π`.
>
> This is the degreewise statement only: it says nothing about the differentials.  That `c`
> commutes with them is `c_chainMap`, and the two clauses are assembled into the isomorphism of
> cochain complexes the source asserts by `Stacks.Cech.orderedIsoAlternatingCechComplex`.

```lean
noncomputable def cAddEquiv (p : ℕ) : OrdCochain U ℱ p ≃+ alternatingSubgroup U ℱ p
```

**`CechCochains.c_chainMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingCochainGroups.lean, line 803](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingCochainGroups.lean#L803). The attribute's comment: “c is a morphism of complexes”.

> (1) **[Stacks, Tag 01FJ], the chain-map clause.** `c` is a chain map: `c ∘ d = d ∘ c`.
>
> This is the first half of what the source asserts about `c`; the degreewise bijectivity is
> `cAddEquiv`, and `Stacks.Cech.orderedIsoAlternatingCechComplex` assembles the two into the
> isomorphism of cochain complexes `Č_ord^• → Č_alt^•`.

```lean
theorem c_chainMap (p : ℕ) (s : OrdCochain U ℱ p) :
    c U ℱ (p + 1) (ordD U ℱ p s) = cechD U ℱ p (c U ℱ p s)
```

**`Stacks.Cech.orderedIsoAlternatingCechComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/OrderedAlternatingComparison.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/OrderedAlternatingComparison.lean#L91). The attribute's comment: “the induced isomorphism of complexes”.

> **The ordered Čech complex is the alternating Čech complex.** The degreewise comparison of
> Stacks 01FJ is an isomorphism of cochain complexes, because `CechCochains.c` is a chain map.
>
> This is the second assertion of the source: the degreewise isomorphism `CechCochains.cAddEquiv`
> and the chain-map property `CechCochains.c_chainMap` together induce an isomorphism of the
> complexes themselves.

```lean
def orderedIsoAlternatingCechComplex :
    orderedCechComplex U ℱ ≅ alternatingCechComplex U ℱ
```

## Tag 01FK, a lemma

[Tag 01FK](https://stacks.math.columbia.edu/tag/01FK) in the Stacks Project.

**`Stacks.CategoryTheory.CechComplex.Alternating.cechProj_comp_cechDiff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechComplexAlternating.lean, line 579](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexAlternating.lean#L579). The attribute's comment: “(1)”.

> The projection `π : C^• → C^•_ord` is a morphism of complexes: it commutes with the
> differentials, `π ∘ d = d ∘ π`.

```lean
theorem cechProj_comp_cechDiff (P : Cᵒᵖ ⥤ AddCommGrpCat.{w'}) (U : ι → C) (p : ℕ) :
    (Alternating.cechProj P U (p+1)).comp (Alternating.cechDiff P U p)
      = (Alternating.cechDiffOrd P U p).comp (Alternating.cechProj P U p)
```

**`Stacks.CategoryTheory.CechComplex.Alternating.cechProj_comp_cechComp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechComplexAlternating.lean, line 587](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexAlternating.lean#L587). The attribute's comment: “(3)”.

> `π` is a left inverse to the comparison map `c`: `π ∘ c = id` on the ordered cochains.

```lean
theorem cechProj_comp_cechComp (P : Cᵒᵖ ⥤ AddCommGrpCat.{w'}) (U : ι → C) (p : ℕ) :
    (Alternating.cechProj P U p).comp (Alternating.cechComp P U p) =
      AddMonoidHom.id (Alternating.CechCochainOrd P U p)
```

**`Stacks.CategoryTheory.CechComplex.Alternating.cechProjAltEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechComplexAlternating.lean, line 626](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexAlternating.lean#L626). The attribute's comment: “(2)”.

> The restriction of the projection to the alternating cochains, `π : C^•_alt → C^•_ord`,
> is an *isomorphism* of abelian groups in each degree, with inverse the comparison map `c`.

```lean
noncomputable def cechProjAltEquiv (P : Cᵒᵖ ⥤ AddCommGrpCat.{w'}) (U : ι → C) (p : ℕ) :
    Alternating.CechCochainAlt P U p ≃+ Alternating.CechCochainOrd P U p
```

**`Stacks.CategoryTheory.CechComplex.Alternating.cechProjAlt_comp_cechDiffAlt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechComplexAlternating.lean, line 639](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexAlternating.lean#L639). The attribute's comment: “(2)”.

> The isomorphism `π : C^•_alt → C^•_ord`
> commutes with the differentials, hence is an isomorphism of complexes.  Equivalently, the
> comparison map `c : C^•_ord → C^•_alt` is a morphism of complexes (`c ∘ d_ord = d_alt ∘ c`),
> exhibiting `c` as the inverse morphism of complexes.

```lean
theorem cechProjAlt_comp_cechDiffAlt (P : Cᵒᵖ ⥤ AddCommGrpCat.{w'}) (U : ι → C)
    (hU : ∀ i, IsSubterminal (U i)) (p : ℕ) :
    (Alternating.cechProjAlt P U (p+1)).comp (Alternating.cechDiffAlt P U hU p)
      = (Alternating.cechDiffOrd P U p).comp (Alternating.cechProjAlt P U p)
```

**`Stacks.CategoryTheory.CechComplex.Alternating.cechProjAltComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingHomotopy.lean, line 826](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingHomotopy.lean#L826). The attribute's comment: “(2) as an isomorphism of complexes”.

> **[Stacks, Tag 01FK] (2) as an isomorphism of complexes.**  The projection `π` from the
> alternating to the ordered Čech cochains is an isomorphism of complexes.

```lean
def cechProjAltComplexIso (hU : ∀ i, IsSubterminal (U i)) :
    cechCochainComplexAlt P U hU ≅ cechCochainComplexOrd P U
```

**`cechProj_comp_cechDiff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingProjection.lean, line 665](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingProjection.lean#L665). The attribute's comment: “(1)”.

> **Statement 1.** The projection `π : C^• → C^•_ord` is a morphism of complexes: each
> `π` in degree `p` is a homomorphism of abelian groups (built into `cechProj`) and it
> commutes with the differentials, `π ∘ d = d ∘ π`.

```lean
theorem cechProj_comp_cechDiff (F : AbelianPresheaf X) (U : I → Opens X) (p : ℕ) :
    (cechProj F U (p+1)).comp (cechDiff F U p)
      = (cechDiffOrd F U p).comp (cechProj F U p)
```

**`cechProj_comp_cechComp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingProjection.lean, line 675](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingProjection.lean#L675). The attribute's comment: “(3)”.

> **Statement 3 (left inverse).** `π` is a left inverse to the comparison map `c`:
> `π ∘ c = id` on the ordered complex.  (For a strictly increasing tuple the sorting
> permutation is the identity, so `c(s)` agrees with `s` there.)

```lean
theorem cechProj_comp_cechComp (F : AbelianPresheaf X) (U : I → Opens X) (p : ℕ) :
    (cechProj F U p).comp (cechComp F U p) = AddMonoidHom.id (CechCochainOrd F U p)
```

**`cechProjAltEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingProjection.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingProjection.lean#L716). The attribute's comment: “(2)”.

> **Statement 2.** The restriction of the projection to the alternating subcomplex,
> `π : C^•_alt → C^•_ord`, is an *isomorphism* of abelian groups in each degree, with inverse
> the comparison map `c`.  (Together with Statement 2 below — that this isomorphism commutes
> with the differentials — this is the asserted isomorphism of complexes.)

```lean
noncomputable def cechProjAltEquiv (F : AbelianPresheaf X) (U : I → Opens X) (p : ℕ) :
    CechCochainAlt F U p ≃+ CechCochainOrd F U p
```

**`cechProjAlt_comp_cechDiffAlt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingProjection.lean, line 729](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingProjection.lean#L729). The attribute's comment: “(2)”.

> **Statement 2 (isomorphism of complexes).** The isomorphism `π : C^•_alt → C^•_ord`
> commutes with the differentials, hence is an isomorphism of complexes.  Equivalently, the
> comparison map `c : C^•_ord → C^•_alt` is a morphism of complexes (`c ∘ d_ord = d_alt ∘ c`),
> exhibiting `c` as the inverse morphism of complexes.

```lean
theorem cechProjAlt_comp_cechDiffAlt (F : AbelianPresheaf X) (U : I → Opens X) (p : ℕ) :
    (cechProjAlt F U (p+1)).comp (cechDiffAlt F U p)
      = (cechDiffOrd F U p).comp (cechProjAlt F U p)
```

## Tag 01FM, a lemma

[Tag 01FM](https://stacks.math.columbia.edu/tag/01FM) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.CrystallineThickening.restrictCechAltInclusionHomotopyEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/OrdCechRestrictCover.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/OrdCechRestrictCover.lean#L221). The attribute's comment: “for a restriction cover of an object of the small crystalline site”.

> **[Stacks, Tag 01FM] for a restriction cover of an object of `Cris(X/S)`.**  The canonical
> inclusion of the alternating Čech cochain complex of the cover into the full Čech cochain
> complex is a homotopy equivalence; signed sorting is a homotopy inverse.
>
> The family of opens is arbitrary: it need not cover the ambient scheme, exactly as at the space
> level.  The hypothesis of the lifted theory is discharged by `isSubterminal_ambientOpen` and
> nothing is assumed here.

```lean
def restrictCechAltInclusionHomotopyEquiv :
    HomotopyEquiv (restrictCechComplexAlt A V F) (restrictCechComplex A V F)
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.CrystallineThickening.restrictCechAltInclusion_homotopyEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/OrdCechRestrictCover.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/OrdCechRestrictCover.lean#L229). The attribute's comment: “a restriction cover's alternating inclusion lies in homotopyEquivalences”.

> **[Stacks, Tag 01FM] for a restriction cover of an object of `Cris(X/S)`**, in the
> `homotopyEquivalences` morphism-property spelling.

```lean
theorem restrictCechAltInclusion_homotopyEquivalence :
    (HomologicalComplex.homotopyEquivalences AddCommGrpCat.{max w w'} (ComplexShape.up ℕ))
      (restrictCechAltInclusion A V F)
```

**`Stacks.CategoryTheory.CechComplex.Alternating.cechAltHomotopyEquivCechComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingComparison.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingComparison.lean#L160). The attribute's comment: “in the cechComplexFunctor model”.

> **[Stacks, Tag 01FM] in the `cechComplexFunctor` model.** The alternating Čech cochain
> complex of a family of subterminal objects is homotopy equivalent to the Čech complex of the
> family.

```lean
def cechAltHomotopyEquivCechComplex (hU : ∀ i, IsSubterminal (U i)) :
    HomotopyEquiv (cechCochainComplexAlt P U hU) ((cechComplexFunctor U).obj P)
```

**`Stacks.CategoryTheory.CechComplex.Alternating.cechComparisonProjectionHomotopy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingHomotopy.lean, line 725](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingHomotopy.lean#L725). The attribute's comment: “c after projection is homotopic to the identity”.

> **[Stacks, Tag 01FM] for a family in an arbitrary category, chain-level form.**  An
> explicit homotopy from the endomorphism `c ∘ π` to the identity of the full Čech cochain
> complex.  Its component from degree `j + 1` to degree `j` is `cochainHomotopy`.

```lean
def cechComparisonProjectionHomotopy (hU : ∀ i, IsSubterminal (U i)) :
    Homotopy (cechComparisonProjection P U hU) (𝟙 (cechCochainComplex P U))
```

**`Stacks.CategoryTheory.CechComplex.Alternating.cechAltInclusionHomotopyEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingHomotopy.lean, line 756](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingHomotopy.lean#L756). The attribute's comment: “the canonical inclusion is a homotopy equivalence”. References: EGA 0 (11.8.7), “more general”.

> **[Stacks, Tag 01FM] for a family in an arbitrary category.**  The canonical inclusion
> of the alternating Čech cochain complex into the full Čech cochain complex is a homotopy
> equivalence; signed sorting `c ∘ π`, corestricted to the alternating cochains, is a homotopy
> inverse.  The family need not cover anything.

```lean
def cechAltInclusionHomotopyEquiv (hU : ∀ i, IsSubterminal (U i)) :
    HomotopyEquiv (cechCochainComplexAlt P U hU) (cechCochainComplex P U)
```

**`Stacks.CategoryTheory.CechComplex.Alternating.cechAltInclusion_homotopyEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingHomotopy.lean, line 790](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechComplexAlternatingHomotopy.lean#L790). The attribute's comment: “the canonical inclusion lies in homotopyEquivalences”.

> **[Stacks, Tag 01FM] for a family in an arbitrary category**, in the `homotopyEquivalences`
> morphism-property spelling.

```lean
theorem cechAltInclusion_homotopyEquivalence (hU : ∀ i, IsSubterminal (U i)) :
    (HomologicalComplex.homotopyEquivalences AddCommGrpCat.{max w w'} (ComplexShape.up ℕ))
      (cechAltInclusion P U hU)
```

**`Stacks.Cech.cechComparisonProjection_homotopic_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingHomotopyEquivalence.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingHomotopyEquivalence.lean#L110). The attribute's comment: “c after projection is homotopic to the identity”.

> The endomorphism `c ∘ π` is homotopic to the identity on the usual Čech
> complex.

```lean
theorem cechComparisonProjection_homotopic_id :
    Nonempty (Homotopy (cechComparisonProjection U F)
      (𝟙 (cechComplex U F)))
```

**`Stacks.Cech.alternatingCechInclusion_homotopyEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingHomotopyEquivalence.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AlternatingHomotopyEquivalence.lean#L143). The attribute's comment: “the canonical inclusion is a homotopy equivalence”.

> The canonical inclusion of alternating Čech cochains into the usual Čech complex is a
> homotopy equivalence: the signed-sorting projection is a homotopy inverse.

```lean
theorem alternatingCechInclusion_homotopyEquivalence
    (G : TopCat.Presheaf Ab.{max v w} X) :
    (HomologicalComplex.homotopyEquivalences AddCommGrpCat (ComplexShape.up ℕ))
      (alternatingCechInclusion U G)
```

## Tag 0G6T, a lemma

[Tag 0G6T](https://stacks.math.columbia.edu/tag/0G6T) in the Stacks Project.

**`Stacks.Cech.alternatingCechComplex_augment_homotopyEquiv_zero_of_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AugmentationContractible.lean, line 652](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AugmentationContractible.lean#L652). The attribute's comment: “alternating complex”.

> If a family of opens contained in `U` contains `U`, its extended alternating Čech complex is
> homotopy equivalent to zero.

```lean
lemma alternatingCechComplex_augment_homotopyEquiv_zero_of_eq
    (X : TopCat.{u}) (F : TopCat.Presheaf Ab.{w} X)
    {I : Type v} {U : Opens X} (V : I → Opens X) (hV : ∀ i, V i ≤ U)
    (i : I) (hi : V i = U) :
    ∃ (w : alternatingCechAugmentation X F V hV ≫
        (alternatingCechComplex V F).d 0 1 = 0),
      Nonempty (HomotopyEquiv
        ((alternatingCechComplex V F).augment
          (alternatingCechAugmentation X F V hV) w)
        (HomologicalComplex.zero : CochainComplex Ab.{max v w} ℕ))
```

**`Stacks.Cech.orderedCechComplex_augment_homotopyEquiv_zero_of_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/AugmentationContractible.lean, line 681](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Cech/AugmentationContractible.lean#L681). The attribute's comment: “ordered complex”.

> For any ordering, if a family of opens contained in `U` contains `U`, its extended ordered
> Čech complex is homotopy equivalent to zero.

```lean
lemma orderedCechComplex_augment_homotopyEquiv_zero_of_eq
    (X : TopCat.{u}) (F : TopCat.Presheaf Ab.{w} X)
    {I : Type v} [LinearOrder I] {U : Opens X} (V : I → Opens X) (hV : ∀ i, V i ≤ U)
    (i : I) (hi : V i = U) :
    ∃ (w : orderedCechAugmentation X F V hV ≫
        (orderedCechComplex V F).d 0 1 = 0),
      Nonempty (HomotopyEquiv
        ((orderedCechComplex V F).augment
          (orderedCechAugmentation X F V hV) w)
        (HomologicalComplex.zero : CochainComplex Ab.{max v w} ℕ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.23, Tag 01FG](https://stacks.math.columbia.edu/tag/01FG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
