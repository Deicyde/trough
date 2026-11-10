---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PolynomialChart, AlgebraicGeometry.Space.PolynomialChart.Hom, AlgebraicGeometry.Space.PolynomialChart.openFunctor, AlgebraicGeometry.Space.PolynomialChart.openFunctor_isFibered, AlgebraicGeometry.Space.PolynomialChart.piSpacesDiagram, AlgebraicGeometry.Space.PolynomialChart.standardResolutionChart_computes_derivedAbelianLowerShriek, AlgebraicGeometry.Space.PolynomialChart.derivedLowerShriekInverseImageDifferentialsIso, AlgebraicGeometry.Space.PolynomialChart.derivedLowerShriekPulledBackDifferentialsIso
statement: formalized
proof: formalized
---

# 92.27 The cotangent complex of an algebraic space over a ring

Section 92.27 of the Stacks Project, [Tag 08VH](https://stacks.math.columbia.edu/tag/08VH). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08VI, an equation

[Tag 08VI](https://stacks.math.columbia.edu/tag/08VI) in the Stacks Project.

**`AlgebraicGeometry.Space.PolynomialChart`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialChartSpace.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialChartSpace.lean#L77). The attribute's comment: “the objects of the category C\_\{X/Λ}”.

> A commutative square `U ⟶ A ⟶ Spec Λ`, `U ⟶ X ⟶ Spec Λ`, in which `U ⟶ X` is an object of
> the small étale site of the algebraic space `X` and `A` is an affine space over `Spec Λ`.

```lean
structure PolynomialChart (hX : IsAlgebraicSpace B (Spec (CommRingCat.of Λ)) hS X)
```

**`AlgebraicGeometry.Space.PolynomialChart.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialChartSpace.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialChartSpace.lean#L108). The attribute's comment: “the morphisms of the category C\_\{X/Λ}”.

> A morphism of polynomial charts is a commutative diagram over both the algebraic space `X`
> and `Spec Λ`.

```lean
structure Hom (P Q : PolynomialChart Λ B hS X hX)
```

**`AlgebraicGeometry.Space.PolynomialChart.openFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialChartSpace.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialChartSpace.lean#L147). The attribute's comment: “the forgetful functor to the small étale site”.

> The functor sending a polynomial chart `(U ⟶ A)` to the object `U ⟶ X` of the small étale
> site of `X`.

```lean
def openFunctor :
    PolynomialChart Λ B hS X hX ⥤ SmallEtale B (Spec (CommRingCat.of Λ)) hS X
```

## Tag 08VJ, a lemma

[Tag 08VJ](https://stacks.math.columbia.edu/tag/08VJ) in the Stacks Project.

**`AlgebraicGeometry.Space.PolynomialChart.openFunctor_isFibered`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartSpaceFibred.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartSpaceFibred.lean#L115).

> **Stacks 08VJ.** The category `C_{X/Λ}` of polynomial charts of an algebraic space `X` over
> `Λ` is fibred over the small étale site of `X`.

```lean
noncomputable instance openFunctor_isFibered (Λ : Type u) [CommRing Λ] (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (CommRingCat.of Λ)))
    (X : (BigFppfOver B (Spec (CommRingCat.of Λ)) hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (CommRingCat.of Λ)) hS X) :
    (openFunctor (Λ := Λ) (B := B) (hS := hS) (X := X) (hX := hX)).IsFibered
```

## Tag 08VK, an equation

[Tag 08VK](https://stacks.math.columbia.edu/tag/08VK) in the Stacks Project.

**`AlgebraicGeometry.Space.PolynomialChart.piSpacesDiagram`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartSpaceRingedTopoi.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartSpaceRingedTopoi.lean#L620).

> The diagram of ringed topoi of the polynomial charts of an algebraic space over a ring, with
> all of its arrows pinned to the canonical ones.

```lean
def piSpacesDiagram [HasWeakSheafify (topology Λ B hS X hX) CommRingCat.{u}] :
    PiSpacesDiagram Λ B hS X hX
```

## Tag 08VL, a remark

[Tag 08VL](https://stacks.math.columbia.edu/tag/08VL) in the Stacks Project.

**`AlgebraicGeometry.Space.PolynomialChart.standardResolutionChart_computes_derivedAbelianLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartSpaceStandardResolution.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/PolynomialChartSpaceStandardResolution.lean#L253).

> **Stacks 08VL.** Let `X` be an algebraic space over a ring `Λ`, let `C_{X/Λ}` be its category
> of polynomial charts, fibred over `X_étale`, and let `π : Sh(C_{X/Λ}) ⟶ Sh(X_étale)` be the
> induced morphism of topoi. For an object `U` of `X_étale` let `P_{•,U}` be the standard resolution
> of `𝒪_X(U)` over `Λ` and `𝐀_{•,U} = Spec(P_{•,U})` (`standardResolutionChart`). Then:
>
> * the fibre of `C_{X/Λ}` over `U` is the site `C_{𝒪_X(U)/Λ}`, and through this identification
>   `𝐀_{•,U}` is the cosimplicial object of `P_{•,U}`;
> * `𝐀_{•,U}` is a cosimplicial object of the fibre over `U`, functorially in `U`;
> * it is a cosimplicial object as in Cohomology on Sites, Lemma 08Q9: every simplicial set
>   `Mor(𝐀_{•,U}, W)` is homotopy equivalent to a singleton;
> * for every abelian sheaf `ℱ` on `C_{X/Λ}`, the homology at `U` of the complex of presheaves
>   `U ↦ ℱ(𝐀_{•,U})` is the homology `H_n(C_U, ℱ|_{C_U})` of `ℱ` on the fibre category;
> * its sheafified homology computes `L_nπ_!(ℱ)`;
> * the complex of sheaves whose term in degree `-n` is the sheafification of `U ↦ ℱ(𝐀_{n,U})`
>   computes `Lπ_!(ℱ)`.

```lean
theorem standardResolutionChart_computes_derivedAbelianLowerShriek :
    (∀ U : SmallEtale B (Spec (CommRingCat.of Λ)) hS X,
      ∃ e : (openFunctor (Λ := Λ) (B := B) (hS := hS) (X := X) (hX := hX)).Fiber U ≌
          CommAlgCat.polynomialSite Λ (sectionsAlgebra Λ B hS X U),
        Nonempty (standardChartCosimplicialObject Λ B hS X hX U ⋙ e.functor ≅
          CommAlgCat.resolutionCosimplicialObject
            (CommAlgCat.standardResolution.{u, u} Λ (sectionsAlgebra Λ B hS X U)).hom
            (CommAlgCat.standardResolution_isResolution.{u, u} Λ
              (sectionsAlgebra Λ B hS X U)).isPolynomialAlgebra)) ∧
    (standardResolutionChart Λ B hS X hX : (fibredCategorySituation Λ B hS X hX).base.C ⥤
        CosimplicialObject (fibredCategorySituation Λ B hS X hX).C) ⋙
      (Functor.whiskeringRight SimplexCategory (fibredCategorySituation Λ B hS X hX).C
        (fibredCategorySituation Λ B hS X hX).base.C).obj
          (fibredCategorySituation Λ B hS X hX).p =
      Functor.const SimplexCategory ∧
    (∀ (U : (fibredCategorySituation Λ B hS X hX).base.C)
      (W : (fibredCategorySituation Λ B hS X hX).p.Fiber U),
      ∃ f : (Functor.Fiber.inducedFunctor (Functor.congr_obj
            (standardResolutionChart_comp_whiskeringRight Λ B hS X hX) U)).op ⋙
            yoneda.obj W ⟶
          (Functor.const SimplexCategoryᵒᵖ).obj PUnit.{u + 1},
        SimplicialObject.homotopyEquivalences (Type u) f) ∧
    ∀ F : Sheaf (fibredCategorySituation Λ B hS X hX).topology AddCommGrpCat.{u + 1},
      (∀ (U : (fibredCategorySituation Λ B hS X hX).base.C) (n : ℕ),
        Nonempty (((((fibredCategorySituation Λ B hS X hX).pointMooreComplex
            (standardResolutionChart Λ B hS X hX)).obj F.obj).homology n).obj (op U) ≅
          Stacks.CategoryHomology.categoryHomology.{u + 1, u + 1}
            ((fibredCategorySituation Λ B hS X hX).smallFiberRestriction F.obj U) n)) ∧
      (∀ n : ℕ, Nonempty ((DerivedCategory.homologyFunctor _ (-(n : ℤ))).obj
          ((fibredCategorySituation Λ B hS X hX).derivedAbelianLowerShriek.obj
            ((DerivedCategory.singleFunctor _ 0).obj F)) ≅
        (presheafToSheaf (fibredCategorySituation Λ B hS X hX).base.J AddCommGrpCat.{u + 1}).obj
          ((((fibredCategorySituation Λ B hS X hX).pointMooreComplex
            (standardResolutionChart Λ B hS X hX)).obj F.obj).homology n))) ∧
      Nonempty ((fibredCategorySituation Λ B hS X hX).derivedAbelianLowerShriek.obj
          ((DerivedCategory.singleFunctor _ 0).obj F) ≅
        DerivedCategory.Q.obj ((fibredCategorySituation Λ B hS X hX).pointSheafComplex
          (standardResolutionChart Λ B hS X hX) F.obj))
```

## Tag 08VM, a lemma

[Tag 08VM](https://stacks.math.columbia.edu/tag/08VM) in the Stacks Project.

**`AlgebraicGeometry.Space.PolynomialChart.derivedLowerShriekInverseImageDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/SpaceCotangentChartSite.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Spaces/SpaceCotangentChartSite.lean#L193). The attribute's comment: “second isomorphism Lπ\_!(Li^*Ω\_\{𝒪/Λ̲}) = Lπ\_!(i^*Ω\_\{𝒪/Λ̲}) for an algebraic space X over Λ, induced by the canonical map Li^*Ω ⟶ i^*Ω, an isomorphism since Ω\_\{𝒪/Λ̲} is flat”.

> **Stacks Project, Tag 08VM, the second isomorphism**
> `Lπ_!(Li^*Ω_{𝒪/Λ̲}) ≅ Lπ_!(i^*Ω_{𝒪/Λ̲})`: `Lπ_!` applied to the canonical map
> `Li^*Ω_{𝒪/Λ̲} ⟶ i^*Ω_{𝒪/Λ̲}`, an isomorphism because `Ω_{𝒪/Λ̲}` is a flat `𝒪`-module
> (`derivedHorizontalInverseImageDifferentialsIso`).

```lean
def derivedLowerShriekInverseImageDifferentialsIso :
    (chartDerivedLowerShriek Λ B hS X hX).obj
        ((derivedHorizontalInverseImage Λ B hS X hX).obj
          ((DerivedCategory.singleFunctor _ 0).obj (chartDifferentials Λ B hS X hX))) ≅
      (chartDerivedLowerShriek Λ B hS X hX).obj
        ((DerivedCategory.singleFunctor _ 0).obj (pulledBackDifferentials Λ B hS X hX))
```

**`AlgebraicGeometry.Space.PolynomialChart.derivedLowerShriekPulledBackDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/SpaceCotangentChartSite.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Spaces/SpaceCotangentChartSite.lean#L208). The attribute's comment: “third isomorphism Lπ\_!(i^*Ω\_\{𝒪/Λ̲}) = Lπ\_!(Ω\_\{𝒪/Λ̲} ⊗\_𝒪 𝒪̲\_X) for an algebraic space X over Λ, induced by the canonical identification of i^* with extension of scalars along i♯”.

> **Stacks Project, Tag 08VM, the third isomorphism**
> `Lπ_!(i^*Ω_{𝒪/Λ̲}) ≅ Lπ_!(Ω_{𝒪/Λ̲} ⊗_𝒪 𝒪̲_X)`: `Lπ_!` applied to the canonical identification of
> the pullback `i^*Ω_{𝒪/Λ̲}` with the extension of scalars of `Ω_{𝒪/Λ̲}` along `i♯`
> (`pulledBackDifferentialsIsoBaseChange`).

```lean
def derivedLowerShriekPulledBackDifferentialsIso :
    (chartDerivedLowerShriek Λ B hS X hX).obj
        ((DerivedCategory.singleFunctor _ 0).obj (pulledBackDifferentials Λ B hS X hX)) ≅
      (chartDerivedLowerShriek Λ B hS X hX).obj
        ((DerivedCategory.singleFunctor _ 0).obj (chartDifferentialsBaseChange Λ B hS X hX))
```

**`AlgebraicGeometry.Space.PolynomialChart.cotangentComplexIsoDerivedLowerShriekInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/SpaceCotangentChartSite.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Spaces/SpaceCotangentChartSite.lean#L266). The attribute's comment: “first isomorphism L\_\{X/Λ} = Lπ\_!(Li^*Ω\_\{𝒪/Λ̲}) in D(𝒪\_X), for the site of polynomial charts of an algebraic space X over a ring Λ, with L\_\{X/Λ} the cotangent complex of X ⟶ Spec Λ (Tag 08VD, sections lifted to the universe of the site); built from the canonical maps of the proof: flatness of Ω, Tag 08VL, Tag 08SX and Tag 08VG”.

> **Stacks Project, Tag 08VM, the first isomorphism** `L_{X/Λ} ≅ Lπ_!(Li^*Ω_{𝒪/Λ̲})` in `D(𝒪_X)`,
> for the site of polynomial charts of Section 08VJ of an algebraic space `X` over a ring `Λ`. Here
> `L_{X/Λ} = L_{X/Spec Λ}` is the cotangent complex of the structure morphism
> (`AlgebraicGeometry.Space.cotangentComplexDerived`, Tag 08VD); `Ω_{𝒪/Λ̲}` is `chartDifferentials`;
> `Li^*` is `derivedHorizontalInverseImage`; and `Lπ_!` is `chartDerivedLowerShriek`.
>
> It is the composite of the canonical maps of the source's proof, read from right to left:
> `Li^*Ω ⟶ i^*Ω` (an isomorphism because `Ω_{𝒪/Λ̲}` is flat), `i^*Ω ≅ Ω ⊗_𝒪 𝒪̲_X`, the
> identification of `Lπ_!(Ω ⊗_𝒪 𝒪̲_X)` with the complex of the standard resolutions (Tag 08VL at
> module coefficients), the identification of that complex with the sheafification of
> `U ↦ L_{𝒪_X(U)/Λ}` and with `L_{𝒪_X/Λ̲}` (Tag 08SX), and the isomorphism
> `L_{𝒪_X/Λ̲} ≅ L_{X/Spec Λ}` of Tag 08VG for the canonical map `Λ̲ ⟶ 𝒪_X`, which restricts on
> sections to the structure maps of the étale charts (`toSheafify_comp_constantStructureMapOfSpace`).

```lean
def cotangentComplexIsoDerivedLowerShriekInverseImage :
    cotangentComplexDerived B (Spec (CommRingCat.of Λ)) hS (structureToSpec Λ B hS ⟨X, hX⟩) ≅
      (chartDerivedLowerShriek Λ B hS X hX).obj
        ((derivedHorizontalInverseImage Λ B hS X hX).obj
          ((DerivedCategory.singleFunctor _ 0).obj (chartDifferentials Λ B hS X hX)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.27, Tag 08VH](https://stacks.math.columbia.edu/tag/08VH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
