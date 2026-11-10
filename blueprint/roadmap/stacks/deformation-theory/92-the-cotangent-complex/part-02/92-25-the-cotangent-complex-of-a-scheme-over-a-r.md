---
declaration: section
origin: cited
lean: AlgebraicGeometry.PolynomialChart, AlgebraicGeometry.PolynomialChart.openFunctor_isFibered, AlgebraicGeometry.PolynomialChart.piSchemesDiagram, AlgebraicGeometry.PolynomialChart.standardResolutionChart_computes_derivedLowerShriek, AlgebraicGeometry.PolynomialChart.hasLeftDerivedFunctor_horizontalModuleInverseImage, AlgebraicGeometry.PolynomialChart.derivedLowerShriekInverseImageDifferentialsIso, AlgebraicGeometry.PolynomialChart.derivedLowerShriekPulledBackDifferentialsIso, AlgebraicGeometry.PolynomialChart.cotangentComplexIsoDerivedLowerShriekInverseImage
statement: formalized
proof: formalized
---

# 92.25 The cotangent complex of a scheme over a ring

Section 92.25 of the Stacks Project, [Tag 08V7](https://stacks.math.columbia.edu/tag/08V7). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08V8, an equation

[Tag 08V8](https://stacks.math.columbia.edu/tag/08V8) in the Stacks Project.

**`AlgebraicGeometry.PolynomialChart`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialChart.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialChart.lean#L50).

> A commutative diagram `U ⟶ A ⟶ Spec Λ`, `U ⟶ X ⟶ Spec Λ`, where `U` is an open subscheme of
> `X` and `A` is an affine space over `Spec Λ`.

```lean
structure PolynomialChart (Λ : Type u) [CommRing Λ] (X : Scheme.{u})
    (structureMap : X ⟶ Spec (CommRingCat.of Λ))
```

## Tag 08V9, a lemma

[Tag 08V9](https://stacks.math.columbia.edu/tag/08V9) in the Stacks Project.

**`AlgebraicGeometry.PolynomialChart.openFunctor_isFibered`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartFibred.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartFibred.lean#L101).

> **Stacks 08V9.** Polynomial charts over `X` form a category fibred over the Zariski
> category of `X`.

```lean
instance openFunctor_isFibered (Λ : Type u) [CommRing Λ] (X : Scheme.{u})
    (structureMap : X ⟶ Spec (CommRingCat.of Λ)) :
    (openFunctor (Λ := Λ) (X := X) (structureMap := structureMap)).IsFibered
```

## Tag 08VA, an equation

[Tag 08VA](https://stacks.math.columbia.edu/tag/08VA) in the Stacks Project.

**`AlgebraicGeometry.PolynomialChart.piSchemesDiagram`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartRingedTopoi.lean, line 694](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartRingedTopoi.lean#L694).

> **Stacks 08VA.** The diagram of ringed topoi of the polynomial charts of a scheme over a
> ring, with all of its arrows pinned to the canonical ones.

```lean
def piSchemesDiagram : PiSchemesDiagram.{u, w} Λ X structureMap
```

## Tag 08VB, a remark

[Tag 08VB](https://stacks.math.columbia.edu/tag/08VB) in the Stacks Project.

**`AlgebraicGeometry.PolynomialChart.standardResolutionChart_computes_derivedLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/StandardResolutionChartsLowerShriek.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/StandardResolutionChartsLowerShriek.lean#L85).

> **Stacks 08VB.** Let `X` be a scheme over a ring `Λ`, and for an open `U ⊆ X` let `P_{•,U}` be
> the standard resolution of `𝒪_X(U)` over `Λ` and `A_{•,U} = Spec(P_{•,U})`, the functorial
> cosimplicial charts `standardResolutionChart`. Then:
>
> 1. the fibre category of `C_{X/Λ}` over `U` is `C_{𝒪_X(U)/Λ}`, and `A_{•,U}` is a cosimplicial
>    object of it (`standardResolutionFibreChart`) which is as in Stacks 08Q9: every simplicial set
>    `Mor(A_{•,U}, W)` is homotopy equivalent to a point;
> 2. for every abelian sheaf `F` on `C_{X/Λ}` the cohomology groups of the complex of presheaves
>    `U ↦ F(A_{•,U})` compute the homology of `F` on the fibre category over `U`;
> 3. their sheafification computes `L_nπ_!(F)`;
> 4. the complex of sheaves whose term in degree `-n` is the sheafification of `U ↦ F(A_{n,U})`
>    computes `Lπ_!(F)`.

```lean
theorem standardResolutionChart_computes_derivedLowerShriek :
    (∀ U : X.Opens, Nonempty ((openFunctor (Λ := Λ) (X := X)
        (structureMap := structureMap)).Fiber U ≌
      CommAlgCat.polynomialSite Λ ((openAlgebra Λ X structureMap).obj (op U)))) ∧
    (∀ (U : X.Opens) (W : (openFunctor (Λ := Λ) (X := X) (structureMap := structureMap)).Fiber U),
      ∃ f : (standardResolutionFibreChart Λ X structureMap U).op ⋙ yoneda.obj W ⟶
          (Functor.const SimplexCategoryᵒᵖ).obj PUnit.{u + 1},
        SimplicialObject.homotopyEquivalences (Type u) f) ∧
    (∀ (F : Sheaf (fibredCategorySituation Λ X structureMap).topology AddCommGrpCat.{u + 1})
      (U : (fibredCategorySituation Λ X structureMap).base.C) (n : ℕ),
      Nonempty (((((fibredCategorySituation Λ X structureMap).pointMooreComplex
          (standardResolutionChart Λ X structureMap :
            (fibredCategorySituation Λ X structureMap).base.C ⥤
              CosimplicialObject (fibredCategorySituation Λ X structureMap).C)).obj
            F.obj).homology n).obj (op U) ≅
        Stacks.CategoryHomology.categoryHomology.{u + 1, u + 1}
          ((fibredCategorySituation Λ X structureMap).smallFiberRestriction F.obj U) n)) ∧
    (∀ (F : Sheaf (fibredCategorySituation Λ X structureMap).topology AddCommGrpCat.{u + 1})
      (n : ℕ),
      Nonempty ((DerivedCategory.homologyFunctor _ (-(n : ℤ))).obj
          ((fibredCategorySituation Λ X structureMap).derivedAbelianLowerShriek.obj
            ((DerivedCategory.singleFunctor _ 0).obj F)) ≅
        (presheafToSheaf (fibredCategorySituation Λ X structureMap).base.J
          AddCommGrpCat.{u + 1}).obj
          ((((fibredCategorySituation Λ X structureMap).pointMooreComplex
            (standardResolutionChart Λ X structureMap :
              (fibredCategorySituation Λ X structureMap).base.C ⥤
                CosimplicialObject (fibredCategorySituation Λ X structureMap).C)).obj
              F.obj).homology n))) ∧
    (∀ F : Sheaf (fibredCategorySituation Λ X structureMap).topology AddCommGrpCat.{u + 1},
      Nonempty ((fibredCategorySituation Λ X structureMap).derivedAbelianLowerShriek.obj
          ((DerivedCategory.singleFunctor _ 0).obj F) ≅
        DerivedCategory.Q.obj ((fibredCategorySituation Λ X structureMap).pointSheafComplex
          (standardResolutionChart Λ X structureMap :
            (fibredCategorySituation Λ X structureMap).base.C ⥤
              CosimplicialObject (fibredCategorySituation Λ X structureMap).C) F.obj)))
```

## Tag 08T9, a lemma

[Tag 08T9](https://stacks.math.columbia.edu/tag/08T9) in the Stacks Project.

**`AlgebraicGeometry.PolynomialChart.hasLeftDerivedFunctor_horizontalModuleInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ChartSiteHorizontalDerivedPullback.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ChartSiteHorizontalDerivedPullback.lean#L267). The attribute's comment: “the first link of the chain L\_\{X/Λ} = Lπ\_!(Li^*Ω\_\{𝒪/Λ̲}) = Lπ\_!(i^*Ω\_\{𝒪/Λ̲}) = Lπ\_!(Ω\_\{𝒪/Λ̲} ⊗\_𝒪 π⁻¹𝒪\_X): the existence of the total left derived functor Li^* of the module pullback along the horizontal arrow of the diagram of Tag 08VA, on the chart site itself”.

> **`Li^*` exists on the site of polynomial charts.** Degreewise `i^*` followed by
> localization to the derived category has a total left derived functor with respect to the
> quasi-isomorphisms of complexes of `𝒪`-modules.
>
> On the small model this is the derived pullback of Tag 06YY along a change of coefficient rings;
> the quasi-isomorphisms of the chart site are the inverse image of those of the small model, and
> total left derived functors are preserved by conjugation by equivalences.

```lean
theorem hasLeftDerivedFunctor_horizontalModuleInverseImage :
    ((horizontalModuleInverseImage.{u, u + 1} Λ X structureMap).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).HasLeftDerivedFunctor
      (HomotopyCategory.quasiIso (_root_.SheafOfModules.{u + 1}
        ((Stacks.SheafOfModules.Tensor.ringSheaf.{u + 1, u, u + 1}
            (J := (topology Λ X structureMap)))
          (affineSheaf.{u, u + 1} Λ X structureMap))) (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.PolynomialChart.derivedLowerShriekInverseImageDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SchemeCotangentChartSite.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SchemeCotangentChartSite.lean#L256). The attribute's comment: “second isomorphism Lπ\_!(Li^*Ω\_\{𝒪/Λ̲}) = Lπ\_!(i^*Ω\_\{𝒪/Λ̲}), induced by the canonical map Li^*Ω ⟶ i^*Ω, an isomorphism since Ω\_\{𝒪/Λ̲} is flat”.

> **Stacks Project, Tag 08T9, the second isomorphism** `Lπ_!(Li^*Ω_{𝒪/Λ̲}) ≅ Lπ_!(i^*Ω_{𝒪/Λ̲})`:
> `Lπ_!` applied to the canonical map `Li^*Ω_{𝒪/Λ̲} ⟶ i^*Ω_{𝒪/Λ̲}`, an isomorphism because
> `Ω_{𝒪/Λ̲}` is a flat `𝒪`-module (`derivedHorizontalInverseImageDifferentialsIso`).

```lean
def derivedLowerShriekInverseImageDifferentialsIso :
    (chartDerivedLowerShriek Λ X structureMap).obj
        ((derivedHorizontalInverseImage Λ X structureMap).obj
          ((DerivedCategory.singleFunctor _ 0).obj
            (chartDifferentials.{u, u + 1} Λ X structureMap))) ≅
      (chartDerivedLowerShriek Λ X structureMap).obj
        ((DerivedCategory.singleFunctor _ 0).obj
          (pulledBackDifferentials.{u, u + 1} Λ X structureMap))
```

**`AlgebraicGeometry.PolynomialChart.derivedLowerShriekPulledBackDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SchemeCotangentChartSite.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SchemeCotangentChartSite.lean#L273). The attribute's comment: “third isomorphism Lπ\_!(i^*Ω\_\{𝒪/Λ̲}) = Lπ\_!(Ω\_\{𝒪/Λ̲} ⊗\_𝒪 𝒪̲\_X), induced by the canonical identification of i^* with extension of scalars along i♯”.

> **Stacks Project, Tag 08T9, the third isomorphism**
> `Lπ_!(i^*Ω_{𝒪/Λ̲}) ≅ Lπ_!(Ω_{𝒪/Λ̲} ⊗_𝒪 𝒪̲_X)`: `Lπ_!` applied to the canonical identification of
> the pullback `i^*Ω_{𝒪/Λ̲}` with the extension of scalars of `Ω_{𝒪/Λ̲}` along `i♯`
> (`pulledBackDifferentialsIsoBaseChange`).

```lean
def derivedLowerShriekPulledBackDifferentialsIso :
    (chartDerivedLowerShriek Λ X structureMap).obj
        ((DerivedCategory.singleFunctor _ 0).obj
          (pulledBackDifferentials.{u, u + 1} Λ X structureMap)) ≅
      (chartDerivedLowerShriek Λ X structureMap).obj
        ((DerivedCategory.singleFunctor _ 0).obj
          (chartDifferentialsBaseChange Λ X structureMap))
```

**`AlgebraicGeometry.PolynomialChart.cotangentComplexIsoDerivedLowerShriekInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SchemeCotangentChartSite.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SchemeCotangentChartSite.lean#L301). The attribute's comment: “first isomorphism L\_\{X/Λ} = Lπ\_!(Li^*Ω\_\{𝒪/Λ̲}) in D(𝒪\_X), for the site of polynomial charts of a scheme X over a ring Λ, with L\_\{X/Λ} the cotangent complex of X ⟶ Spec Λ and D(𝒪\_X) taken in the coefficient universe of the chart topos; built from the canonical maps of the proof: flatness of Ω, Tag 08VB, Tag 08SX and the Tag 08V6 comparison”.

> **Stacks Project, Tag 08T9, the first isomorphism** `L_{X/Λ} ≅ Lπ_!(Li^*Ω_{𝒪/Λ̲})` in `D(𝒪_X)`,
> for the site of polynomial charts of Tag 08VA of a scheme `X` over a ring `Λ`. Here
> `L_{X/Λ} = L_{X/Spec Λ}` is the cotangent complex of the structure morphism
> (`SchemeOverRing.cotangentComplexRelative`, Tag 08UU), read in the coefficient universe of the
> chart topos through `chartBaseLift`; `Ω_{𝒪/Λ̲}` is `chartDifferentials`; `Li^*` is
> `derivedHorizontalInverseImage`; and `Lπ_!` is `chartDerivedLowerShriek`.
>
> It is the composite of the canonical maps of the source's proof, read from right to left:
> `Li^*Ω ⟶ i^*Ω` (an isomorphism because `Ω_{𝒪/Λ̲}` is flat), `i^*Ω ≅ Ω ⊗_𝒪 𝒪̲_X`, the
> identification of `Lπ_!(Ω ⊗_𝒪 𝒪̲_X)` with the complex of the standard resolutions (Tag 08VB at
> module coefficients), the identification of that complex with the sheafification of
> `U ↦ L_{𝒪_X(U)/Λ}` and with `L_{𝒪_X/Λ̲}` (Tag 08SX), and the comparison map
> `L_{𝒪_X/Λ̲} ⟶ L_{X/Spec Λ}`, a quasi-isomorphism by Tag 08V6.

```lean
def cotangentComplexIsoDerivedLowerShriekInverseImage :
    DerivedCategory.Q.obj (((chartBaseLift Λ X structureMap).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj (SchemeOverRing.cotangentComplexRelative Λ structureMap)) ≅
      (chartDerivedLowerShriek Λ X structureMap).obj
        ((derivedHorizontalInverseImage Λ X structureMap).obj
          ((DerivedCategory.singleFunctor _ 0).obj
            (chartDifferentials.{u, u + 1} Λ X structureMap)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.25, Tag 08V7](https://stacks.math.columbia.edu/tag/08V7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
