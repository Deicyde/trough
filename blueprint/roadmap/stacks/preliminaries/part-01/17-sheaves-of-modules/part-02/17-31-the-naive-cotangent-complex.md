---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.presentationNaiveCotangentDerivedIso, Stacks.Sheaves.PolynomialAlgebra.polynomialAlgebraSheaf, Stacks.Sheaves.PolynomialAlgebra.canonicalPolynomialPresentation, Stacks.Sheaves.PolynomialAlgebra.canonicalPolynomialPresentation_surjective, Stacks.SheafOfModules.naiveCotangentComplex, Stacks.SheafOfModules.presentationNaiveCotangentComplex, Stacks.SheafOfModules.spaceNaiveCotangentComplexMapOfSquare, Stacks.SheafOfModules.spaceNaiveCotangentComplexMapOfSquare_comp
statement: formalized
proof: formalized
---

# 17.31 The naive cotangent complex

Section 17.31 of the Stacks Project, [Tag 08TG](https://stacks.math.columbia.edu/tag/08TG). 11 tags here are carried by 34 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08TG, the section

[Tag 08TG](https://stacks.math.columbia.edu/tag/08TG) in the Stacks Project.

**`Stacks.SheafOfModules.presentationNaiveCotangentDerivedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L49). The attribute's comment: “the presentation-independence assertion”.

> For a presentation `α : ℰ ⟶ ℬ` of `ℬ` as a quotient of a polynomial algebra over `𝒜`, the
> isomorphism `𝖭𝖫(α) ≅ 𝖭𝖫_{ℬ/𝒜}` in `D(ℬ)` given by the comparison quasi-isomorphism
> `𝖭𝖫(α) ⟶ 𝖭𝖫_{ℬ/𝒜}`.

```lean
def presentationNaiveCotangentDerivedIso :
    DerivedCategory.Q.obj (presentationNaiveCotangentComplex.{u, u, u, u}
        (Opens.grothendieckTopology Z) A B a E α) ≅
      DerivedCategory.Q.obj (naiveCotangentComplex.{u, u, u, u}
        (Opens.grothendieckTopology Z) A B a)
```

Declarations registered for the tag:

- [`Stacks.Sheaves.PolynomialAlgebra.polynomialAlgebraSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean#L105), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L65) (StacksFrontier): “the polynomial algebra sheaf 𝒜[ℰ] of the section's notation”.
- [`Stacks.Sheaves.PolynomialAlgebra.canonicalPolynomialPresentation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean#L122), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L68) (StacksFrontier): “the canonical surjection 𝒜[ℬ] ⟶ ℬ, [b] ↦ b”.
- [`Stacks.Sheaves.PolynomialAlgebra.canonicalPolynomialPresentation_surjective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean#L144), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L71) (StacksFrontier): “surjectivity of 𝒜[ℬ] ⟶ ℬ”.
- [`Stacks.SheafOfModules.naiveCotangentComplex`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L74) (StacksFrontier): “the naive cotangent complex 𝖭𝖫_{ℬ/𝒜} of the section's definition, with ℐ/ℐ² in degree -1 and Ω_{𝒜[ℬ]/𝒜} ⊗ ℬ in degree 0”.
- [`Stacks.SheafOfModules.presentationNaiveCotangentComplex`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L224), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L78) (StacksFrontier): “the complex 𝖭𝖫(α) attached to a presentation α : ℰ ⟶ ℬ”.
- [`Stacks.SheafOfModules.spaceNaiveCotangentComplexMapOfSquare`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentSquare.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L81) (StacksFrontier): “the canonical ℬ-linear map of complexes 𝖭𝖫_{ℬ/𝒜} ⟶ 𝖭𝖫_{ℬ'/𝒜'} attached to a commutative square of sheaves of rings”.
- [`Stacks.SheafOfModules.spaceNaiveCotangentComplexMapOfSquare_comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentSquare.lean#L129), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L85) (StacksFrontier): “compatibility of that canonical map of complexes with compositions”.
- [`Stacks.SheafOfModules.quasiIso_naiveCotangentComplexComparison`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationQuasiIso.lean#L858), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L88) (StacksFrontier): “the canonical comparison 𝖭𝖫(α) ⟶ 𝖭𝖫_{ℬ/𝒜} and its quasi-isomorphy”.
- [`Stacks.SheafOfModules.naiveCotangentComplexInverseImageIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentInverseImage.lean#L1916), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L91) (StacksFrontier): “compatibility with inverse images, f⁻¹𝖭𝖫_{ℬ/𝒜} ≅ 𝖭𝖫_{f⁻¹ℬ/f⁻¹𝒜}”.

## Tag 08TH, an equation

[Tag 08TH](https://stacks.math.columbia.edu/tag/08TH) in the Stacks Project.

**`Stacks.Sheaves.PolynomialAlgebra.polynomialAlgebraSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean#L105). The attribute's comment: “the polynomial algebra sheaf”.

> The sheaf `A[B]`: the sheafification of `U ↦ A(U)[B(U)]`.

```lean
noncomputable def polynomialAlgebraSheaf
    (A B : Sheaf (Opens.grothendieckTopology X) CommRingCat.{u}) :
    Sheaf (Opens.grothendieckTopology X) CommRingCat.{u}
```

**`Stacks.Sheaves.PolynomialAlgebra.polynomialAlgebraMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean#L114). The attribute's comment: “the coefficient map”.

> The structural morphism `A ⟶ A[B]`, obtained from the coefficient inclusions and the
> sheafification unit.

```lean
noncomputable def polynomialAlgebraMap
    (A B : Sheaf (Opens.grothendieckTopology X) CommRingCat.{u}) :
    A ⟶ polynomialAlgebraSheaf A B
```

**`Stacks.Sheaves.PolynomialAlgebra.canonicalPolynomialPresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean#L122). The attribute's comment: “the canonical map”.

> The canonical presentation `A[B] ⟶ B`, induced by `[b] ↦ b`.

```lean
noncomputable def canonicalPolynomialPresentation
    {A B : Sheaf (Opens.grothendieckTopology X) CommRingCat.{u}} (f : A ⟶ B) :
    polynomialAlgebraSheaf A B ⟶ B
```

**`Stacks.Sheaves.PolynomialAlgebra.polynomialAlgebraMap_comp_canonicalPolynomialPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean#L130). The attribute's comment: “compatibility with coefficients”.

> Evaluation `A[B] ⟶ B` is compatible with the structural maps from `A`, hence is a morphism
> of `A`-algebras.

```lean
theorem polynomialAlgebraMap_comp_canonicalPolynomialPresentation
    {A B : Sheaf (Opens.grothendieckTopology X) CommRingCat.{u}} (f : A ⟶ B) :
    polynomialAlgebraMap A B ≫ canonicalPolynomialPresentation f = f
```

**`Stacks.Sheaves.PolynomialAlgebra.canonicalPolynomialPresentation_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/PolynomialAlgebra.lean#L144). The attribute's comment: “surjectivity”.

> The canonical polynomial presentation `A[B] ⟶ B` is locally surjective on underlying
> sets.

```lean
theorem canonicalPolynomialPresentation_surjective
    {A B : Sheaf (Opens.grothendieckTopology X) CommRingCat.{u}} (f : A ⟶ B) :
    Presheaf.IsLocallySurjective (Opens.grothendieckTopology X)
      (Functor.whiskerRight (canonicalPolynomialPresentation f).hom
        (forget CommRingCat))
```

## Tag 08TI, an equation

[Tag 08TI](https://stacks.math.columbia.edu/tag/08TI) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.SheafOfModules.naiveCotangentComplex`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean, line 864](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L864) (StacksFrontier): “the displayed two-term complex `I/I² ⟶ Ω_{A[B]/A} ⊗_{A[B]} B`”.

## Tag 08TJ, a definition

[Tag 08TJ](https://stacks.math.columbia.edu/tag/08TJ) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.SheafOfModules.naiveCotangentComplex`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean, line 863](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L863) (StacksFrontier).

## Tag 08TK, an equation

[Tag 08TK](https://stacks.math.columbia.edu/tag/08TK) in the Stacks Project.

**`Stacks.SheafOfModules.spaceNaiveCotangentComplexMapOfSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentSquare.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentSquare.lean#L72). The attribute's comment: “the canonical B-linear map of complexes NL_{B/A} ⟶ NL_{B'/A'}”.

> **Stacks 08TK.** The canonical `B`-linear chain map `NL_{B/A} ⟶ NL_{B'/A'}` attached to a
> commutative square of sheaves of commutative rings on a topological space.

```lean
noncomputable def spaceNaiveCotangentComplexMapOfSquare :
    naiveCotangentComplex.{u, u, u, u} (Opens.grothendieckTopology X) A B a ⟶
      ((_root_.SheafOfModules.restrictScalars.{u, u, u, u} (underlyingRingHomOfSite.{u, u, u} β)
        ).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (naiveCotangentComplex.{u, u, u, u} (Opens.grothendieckTopology X) A' B' a')
```

**`Stacks.SheafOfModules.spaceNaiveCotangentComplexMapOfSquare_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentSquare.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentSquare.lean#L129). The attribute's comment: “compatibility of the canonical map of complexes with compositions”.

> **Stacks 08TK.** The canonical chain map attached to a commutative square of sheaves of
> commutative rings on a topological space is compatible with compositions: given a commutative
> diagram
> ```
> B ──β──▸ B' ──β'──▸ B''
> ▲         ▲          ▲
> a         a'         a''
> │         │          │
> A ──f──▸ A' ──f'──▸ A''
> ```
> the composition `NL_{B/A} ⟶ NL_{B'/A'} ⟶ NL_{B''/A''}` is the map attached to the outer
> rectangle.

```lean
theorem spaceNaiveCotangentComplexMapOfSquare_comp :
    spaceNaiveCotangentComplexMapOfSquare A A' B B' a a' f β hsq ≫
        ((_root_.SheafOfModules.restrictScalars.{u, u, u, u}
            (underlyingRingHomOfSite.{u, u, u} β)).mapHomologicalComplex
            (ComplexShape.up ℤ)).map
          (spaceNaiveCotangentComplexMapOfSquare A' A'' B' B'' a' a'' f' β' hsq') =
      spaceNaiveCotangentComplexMapOfSquare A A'' B B'' a a'' (f ≫ f') (β ≫ β')
        (square_comp hsq hsq')
```

## Tag 08TL, a lemma

[Tag 08TL](https://stacks.math.columbia.edu/tag/08TL) in the Stacks Project.

**`Stacks.SheafOfModules.naiveCotangentComplexComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L512). The attribute's comment: “the canonical map”.

> The canonical comparison chain map `NL(α) ⟶ NL_{B/A}` from the naive cotangent complex of
> an arbitrary polynomial presentation `α : E ⟶ B` to the one of the canonical presentation. It
> is the map of the morphism of presentations `α : (E, α) ⟶ (B, id)`.

```lean
noncomputable def naiveCotangentComplexComparison :
    presentationNaiveCotangentComplex.{v, u, w, z} J A B a E α ⟶
      naiveCotangentComplex.{v, u, w, z} J A B a
```

**`Stacks.SheafOfModules.presentationNaiveCotangentDerivedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationInvariance.lean#L49). The attribute's comment: “the isomorphism in D(ℬ)”.

> For a presentation `α : ℰ ⟶ ℬ` of `ℬ` as a quotient of a polynomial algebra over `𝒜`, the
> isomorphism `𝖭𝖫(α) ≅ 𝖭𝖫_{ℬ/𝒜}` in `D(ℬ)` given by the comparison quasi-isomorphism
> `𝖭𝖫(α) ⟶ 𝖭𝖫_{ℬ/𝒜}`.

```lean
def presentationNaiveCotangentDerivedIso :
    DerivedCategory.Q.obj (presentationNaiveCotangentComplex.{u, u, u, u}
        (Opens.grothendieckTopology Z) A B a E α) ≅
      DerivedCategory.Q.obj (naiveCotangentComplex.{u, u, u, u}
        (Opens.grothendieckTopology Z) A B a)
```

**`Stacks.SheafOfModules.quasiIso_naiveCotangentComplexComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationQuasiIso.lean, line 858](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentPresentationQuasiIso.lean#L858).

> For a morphism `a : A ⟶ B` of sheaves of commutative rings on a topological space and a
> family of generators `α : E ⟶ B` presenting `B`, the canonical comparison map
> `NL(α) ⟶ NL_{B/A}` is a quasi-isomorphism.

```lean
theorem quasiIso_naiveCotangentComplexComparison :
    QuasiIso (naiveCotangentComplexComparison.{u, u, u, u}
      (Opens.grothendieckTopology X) A B a E α)
```

**`Stacks.SheafOfModules.quasiIso_trivialNaiveCotangentComplexComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentTrivialPresentation.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentTrivialPresentation.lean#L439). The attribute's comment: “NL(α) ⟶ NL_{B/A} for the trivial presentation α = a : A ⟶ B of B over A”.

> **Stacks 08TL for the trivial presentation.**  For a locally surjective morphism
> `a : A ⟶ B` of sheaves of commutative rings on a topological space, the comparison map
> `NL(a) ⟶ NL_{B/A}` from the naive cotangent complex of the trivial presentation of `B` over `A`
> — that is, of `a` itself, presenting `B` as a quotient of the `A`-algebra `A` — to the naive
> cotangent complex of the canonical polynomial presentation is a quasi-isomorphism.
>
> Quasi-isomorphy is a stalkwise condition, and at every point `x` the two stalk complexes are
> the naive cotangent complexes of two extensions of `Bₓ` over `Aₓ` between which morphisms exist
> in both directions: the stalk of the coefficient inclusion `A ⟶ A[B]` one way, and evaluation
> of a polynomial at a set-theoretic section of `Aₓ → Bₓ` the other way.  So the comparison is a
> homotopy equivalence on stalks.

```lean
theorem quasiIso_trivialNaiveCotangentComplexComparison :
    QuasiIso (trivialNaiveCotangentComplexComparison A B a)
```

## Tag 08TM, a lemma

[Tag 08TM](https://stacks.math.columbia.edu/tag/08TM) in the Stacks Project.

**`Stacks.SheafOfModules.isIso_naiveCotangentComplexInverseImageMap`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentInverseImage.lean, line 1895](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentInverseImage.lean#L1895). The attribute's comment: “invertibility of the canonical map”.

> **The comparison chain map `f⁻¹ NL_{B/A} ⟶ NL_{f⁻¹B/f⁻¹A}` is an isomorphism.** Both
> complexes vanish outside the degrees `-1` and `0`, where the comparison is the isomorphism of
> conormal sheaves and the isomorphism of the scalar extensions of the differentials.

```lean
instance isIso_naiveCotangentComplexInverseImageMap :
    IsIso (naiveCotangentComplexInverseImageMap f A B a)
```

**`Stacks.SheafOfModules.naiveCotangentComplexInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentInverseImage.lean, line 1916](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentInverseImage.lean#L1916).

> **The inverse image of the naive cotangent complex is the naive cotangent complex of the
> inverse image**: `f⁻¹ NL_{B/A} ≅ NL_{f⁻¹B/f⁻¹A}`.

```lean
noncomputable def naiveCotangentComplexInverseImageIso :
    ((_root_.SheafOfModules.pullback.{u} (inverseImageRingHom f B)).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj
        (naiveCotangentComplex.{u, u, u, u} (Opens.grothendieckTopology X) A B a) ≅
      naiveCotangentComplex.{u, u, u, u} (Opens.grothendieckTopology Y)
        ((TopCat.Sheaf.pullback CommRingCat.{u} f).obj A)
        ((TopCat.Sheaf.pullback CommRingCat.{u} f).obj B)
        ((TopCat.Sheaf.pullback CommRingCat.{u} f).map a)
```

## Tag 0D09, a lemma

[Tag 0D09](https://stacks.math.columbia.edu/tag/0D09) in the Stacks Project.

**`Stacks.SheafOfModules.naiveCotangentStalk_eq_naiveCotangentComplexStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentStalk.lean, line 587](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentStalk.lean#L587).

> `NL_{𝓑/𝓐, x} = NL_{𝓑ₓ/𝓐ₓ}`: the stalk at `x` of the naive cotangent complex of `B` over `A`
> is the naive cotangent complex of `Bₓ` over `Aₓ`.
>
> The underlying additive bijections of the two terms are
> `Stacks.SheafOfModules.naiveCotangentStalkCotangentEquiv` in degree `-1` and
> `Stacks.SheafOfModules.naiveCotangentStalkCotangentSpaceEquiv` in degree `0`; the three clauses
> say that both are semilinear over the stalk `(A[B])ₓ → Bₓ` of the canonical presentation, which
> is surjective, so they are `Bₓ`-linear, and that they commute with the differentials.

```lean
theorem naiveCotangentStalk_eq_naiveCotangentComplexStalk :
    letI := algebraStalk a.hom x
    (∀ (r : ToType (TopCat.Presheaf.stalk (freeAlgebraSheaf (Opens.grothendieckTopology X) A
          (underlyingPresheaf (Opens.grothendieckTopology X) B)).obj x)) ξ,
        naiveCotangentStalkCotangentEquiv A B a x (r • ξ) =
          (show ToType (TopCat.Presheaf.stalk B.obj x) from
              ((TopCat.Presheaf.stalkFunctor CommRingCat.{u} x).map
                (presentation (Opens.grothendieckTopology X) A B a
                  (underlyingPresheaf (Opens.grothendieckTopology X) B) (𝟙 _)).hom).hom r) •
            naiveCotangentStalkCotangentEquiv A B a x ξ) ∧
      (∀ (r : ToType (TopCat.Presheaf.stalk (freeAlgebraSheaf (Opens.grothendieckTopology X) A
          (underlyingPresheaf (Opens.grothendieckTopology X) B)).obj x)) ξ,
        naiveCotangentStalkCotangentSpaceEquiv A B a x (r • ξ) =
          (show ToType (TopCat.Presheaf.stalk B.obj x) from
              ((TopCat.Presheaf.stalkFunctor CommRingCat.{u} x).map
                (presentation (Opens.grothendieckTopology X) A B a
                  (underlyingPresheaf (Opens.grothendieckTopology X) B) (𝟙 _)).hom).hom r) •
            naiveCotangentStalkCotangentSpaceEquiv A B a x ξ) ∧
      ∀ ξ, naiveCotangentStalkCotangentSpaceEquiv A B a x
            (conormalSequenceStalkMapF A (freeAlgebraSheaf (Opens.grothendieckTopology X) A
              (underlyingPresheaf (Opens.grothendieckTopology X) B)) B
              (freeAlgebraSheafCoefficientMap (Opens.grothendieckTopology X) A
                (underlyingPresheaf (Opens.grothendieckTopology X) B))
              (presentation (Opens.grothendieckTopology X) A B a
                (underlyingPresheaf (Opens.grothendieckTopology X) B) (𝟙 _)) x ξ) =
          (Algebra.Generators.self (ToType (TopCat.Presheaf.stalk A.obj x))
              (ToType (TopCat.Presheaf.stalk B.obj x))).toExtension.cotangentComplex
            (naiveCotangentStalkCotangentEquiv A B a x ξ)
```

## Tag 0E1Y, a lemma

[Tag 0E1Y](https://stacks.math.columbia.edu/tag/0E1Y) in the Stacks Project.

**`Stacks.SheafOfModules.exact_spaceJacobiZariskiHomologySequence_negOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean#L269). The attribute's comment: “exactness of the six-term sequence of cohomology sheaves at the node H^{-1}(NL_{C/A}), for the maps induced by the two canonical maps c_1 and g”.

> **Stacks 0E1Y, exactness at `H^{-1}(NL_{C/A})`.**  For morphisms `A ⟶ B ⟶ C` of sheaves of
> commutative rings on a topological space the sequence
>
> `H^{-1}(NL_{B/A} ⊗_B C) ⟶ H^{-1}(NL_{C/A}) ⟶ H^{-1}(NL_{C/B})`
>
> of cohomology sheaves is exact at the middle term.

```lean
theorem exact_spaceJacobiZariskiHomologySequence_negOne :
    (spaceJacobiZariskiHomologySequence A B C a b (-1)).Exact
```

**`Stacks.SheafOfModules.exact_spaceJacobiZariskiHomologySequence_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean#L297). The attribute's comment: “exactness of the six-term sequence of cohomology sheaves at the node H^0(NL_{C/A}), for the maps induced by the two canonical maps c_1 and g”.

> **Stacks 0E1Y, exactness at `H⁰(NL_{C/A})`.**  For morphisms `A ⟶ B ⟶ C` of sheaves of
> commutative rings on a topological space the sequence
>
> `H⁰(NL_{B/A} ⊗_B C) ⟶ H⁰(NL_{C/A}) ⟶ H⁰(NL_{C/B})`
>
> of cohomology sheaves is exact at the middle term.

```lean
theorem exact_spaceJacobiZariskiHomologySequence_zero :
    (spaceJacobiZariskiHomologySequence A B C a b 0).Exact
```

**`Stacks.SheafOfModules.epi_homologyMap_spaceRelativeNaiveCotangentComplexMap_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean#L369). The attribute's comment: “the final `-> 0` of the six-term sequence of cohomology sheaves, that is, its exactness at H^0(NL_{C/B}): the map induced by the canonical map g is surjective”.

> **Stacks 0E1Y, the final `⟶ 0` of the six-term sequence**: the canonical map
> `g : NL_{C/A} ⟶ NL_{C/B}` is surjective on `H⁰`, that is, the sequence of cohomology sheaves is
> exact at `H⁰(NL_{C/B})`.
>
> Epimorphy is stalkwise, and at a stalk this is the surjectivity clause of Algebra, Lemma 00S2
> over the canonical presentations of the stalk rings.

```lean
theorem epi_homologyMap_spaceRelativeNaiveCotangentComplexMap_zero :
    Epi (HomologicalComplex.homologyMap (spaceRelativeNaiveCotangentComplexMap A B C a b) 0)
```

**`Stacks.SheafOfModules.spaceJacobiZariskiConnecting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean#L103). The attribute's comment: “the connecting morphism H^{-1}(NL_{C/B}) -> H^0(NL_{B/A} ⊗_B C)”.

> **Stacks 0E1Y, the connecting morphism of the six-term sequence**
> `∂ : H^{-1}(NL_{C/B}) ⟶ H⁰(NL_{B/A} ⊗_B C)`, for morphisms `A ⟶ B ⟶ C` of sheaves of
> commutative rings on a topological space.
>
> It is the connecting morphism of the long exact sequence of the cone of
> `g : NL_{C/A} ⟶ NL_{C/B}`, whose target `H⁰(C(g)[-1])` is identified with
> `H⁰(NL_{B/A} ⊗_B C)` by the canonical map `c` of Stacks 0E1Y, an isomorphism on `H⁰` by
> `Stacks.SheafOfModules.isIso_homologyMap_spaceNaiveCotangentConeMap_zero`.

```lean
noncomputable def spaceJacobiZariskiConnecting
```

**`Stacks.SheafOfModules.exact_spaceJacobiZariskiSixTerm_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean#L191). The attribute's comment: “exactness of the six-term sequence at H^0(NL_{B/A} ⊗_B C)”.

> **Stacks 0E1Y, exactness at `H⁰(NL_{B/A} ⊗_B C)`.**  For morphisms `A ⟶ B ⟶ C` of sheaves of
> commutative rings on a topological space the sequence
>
> `H^{-1}(NL_{C/B}) --∂--> H⁰(NL_{B/A} ⊗_B C) ⟶ H⁰(NL_{C/A})`
>
> of cohomology sheaves is exact at the middle term.
>
> This is the exactness of the long exact sequence of the cone at `H⁰(C(g)[-1])`
> (`Stacks.SheafOfModules.spaceNaiveCotangentCone_homology_exact_cone`), transported along the
> isomorphism `H⁰(c)` of
> `Stacks.SheafOfModules.isIso_homologyMap_spaceNaiveCotangentConeMap_zero`.

```lean
theorem exact_spaceJacobiZariskiSixTerm_zero :
    (ShortComplex.mk (spaceJacobiZariskiConnecting A B C a b)
      (HomologicalComplex.homologyMap (spaceBaseChangeNaiveCotangentMap A B C a b) 0)
      (spaceJacobiZariskiConnecting_comp_homologyMap A B C a b)).Exact
```

**`Stacks.SheafOfModules.exact_spaceJacobiZariskiSixTerm_negOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean#L209). The attribute's comment: “exactness of the six-term sequence at H^{-1}(NL_{C/B})”.

> **Stacks 0E1Y, exactness at `H^{-1}(NL_{C/B})`.**  For morphisms `A ⟶ B ⟶ C` of sheaves of
> commutative rings on a topological space the sequence
>
> `H^{-1}(NL_{C/A}) ⟶ H^{-1}(NL_{C/B}) --∂--> H⁰(NL_{B/A} ⊗_B C)`
>
> of cohomology sheaves is exact at the middle term.
>
> This is the exactness of the long exact sequence of the cone at `H^{-1}(NL_{C/B})`
> (`Stacks.SheafOfModules.spaceNaiveCotangentCone_homology_exact_target`), transported along the
> isomorphism `H⁰(c)`.

```lean
theorem exact_spaceJacobiZariskiSixTerm_negOne :
    (ShortComplex.mk
      (HomologicalComplex.homologyMap (spaceRelativeNaiveCotangentComplexMap A B C a b) (-1))
      (spaceJacobiZariskiConnecting A B C a b)
      (homologyMap_comp_spaceJacobiZariskiConnecting A B C a b)).Exact
```

**`Stacks.SheafOfModules.spaceNaiveCotangentConeMap`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean#L390). The attribute's comment: “the canonical map NL_{B/A} ⊗ C -> C(g)[-1] to the shifted cone”.

> **Stacks 0E1Y, the canonical map.**  For morphisms `A ⟶ B ⟶ C` of sheaves of commutative
> rings on a topological space, the canonical map
>
> `c : NL_{B/A} ⊗_B C ⟶ C(NL_{C/A} ⟶ NL_{C/B})[-1]`
>
> of complexes of sheaves of `C`-modules, lifting the canonical map
> `c₁ : NL_{B/A} ⊗_B C ⟶ NL_{C/A}` through the projection of the shifted cone.
>
> All six assertions of the six-term exact sequence of cohomology sheaves are covered: exactness
> at `H^{-1}(NL_{C/A})`, at `H^0(NL_{C/A})` and at `H^0(NL_{C/B})` (the final `→ 0`) by
> `Stacks.SheafOfModules.exact_spaceJacobiZariskiHomologySequence_negOne`, `_zero` and
> `Stacks.SheafOfModules.epi_homologyMap_spaceRelativeNaiveCotangentComplexMap_zero`; exactness at
> `H^{-1}(NL_{C/B})` and at `H^0(NL_{B/A} ⊗ C)`, and the connecting map, by
> `Stacks.SheafOfModules.exact_spaceJacobiZariskiSixTerm_negOne`, `_zero` and
> `Stacks.SheafOfModules.spaceJacobiZariskiConnecting`, which rest on
> `Stacks.SheafOfModules.isIso_homologyMap_spaceNaiveCotangentConeMap_zero`.

```lean
noncomputable abbrev spaceNaiveCotangentConeMap
```

**`Stacks.SheafOfModules.spaceNaiveCotangentConeMap_comp_pShift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean#L401). The attribute's comment: “the defining property of the canonical map: composed with the cone projection it is c_1”.

> **Stacks 0E1Y, the defining property of the canonical map.**  The canonical map `c`
> composed with the projection `C(g)[-1] ⟶ NL_{C/A}` of the shifted cone is the canonical map
> `c₁ : NL_{B/A} ⊗_B C ⟶ NL_{C/A}`.
>
> The six assertions of the six-term exact sequence drawn from this map are all covered; see the
> docstring of `Stacks.SheafOfModules.spaceNaiveCotangentConeMap` for where each one is.

```lean
theorem spaceNaiveCotangentConeMap_comp_pShift :
    spaceNaiveCotangentConeMap A B C a b ≫
        pShift (spaceRelativeNaiveCotangentComplexMap A B C a b) =
      spaceBaseChangeNaiveCotangentMap A B C a b
```

**`Stacks.SheafOfModules.spaceNaiveCotangentConeMap_comp_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean#L422). The attribute's comment: “the second defining property of the canonical map: its degree -1 component is the explicit homotopy”.

> **Stacks 0E1Y, the canonical map.**  The canonical map `c` composed with the degree `-1`
> projection `C(g)[-1] ⟶ NL_{C/B}` of the shifted cone is the explicit null homotopy of
> `c₁ ≫ g`.  This is the second of the two components out of which Stacks 08RI (2) builds `c`,
> and together with `spaceNaiveCotangentConeMap_comp_pShift` it determines `c`.
>
> The six assertions of the six-term exact sequence drawn from this map are all covered; see the
> docstring of `Stacks.SheafOfModules.spaceNaiveCotangentConeMap` for where each one is.

```lean
theorem spaceNaiveCotangentConeMap_comp_snd :
    (CochainComplex.HomComplex.Cochain.ofHom
          (spaceNaiveCotangentConeMap A B C a b)).comp
        ((CochainComplex.mappingCone.snd
            (spaceRelativeNaiveCotangentComplexMap A B C a b)).leftShift (-1) (-1)
          (by omega)) (by omega) =
      CochainComplex.HomComplex.Cochain.ofHomotopy
        (spaceBaseChangeRelativeNullHomotopy A B C a b)
```

## Tag 08TN, a definition

[Tag 08TN](https://stacks.math.columbia.edu/tag/08TN) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.naiveCotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RingedSpace/NaiveCotangentComplex.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RingedSpace/NaiveCotangentComplex.lean#L57).

> The naive cotangent complex `NL_f = NL_{X/Y}` of a morphism of ringed spaces
> `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)`: the naive cotangent complex of the homomorphism of sheaves of rings
> `f^{-1}𝒪_Y ⟶ 𝒪_X` on `X`.

```lean
noncomputable def naiveCotangentComplex :
    CochainComplex (_root_.SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (J := Opens.grothendieckTopology X.carrier) X.sheaf)) ℤ
```

## Tag 0E1Z, a lemma

[Tag 0E1Z](https://stacks.math.columbia.edu/tag/0E1Z) in the Stacks Project.

**`Stacks.SheafOfModules.exact_ringedSpaceJacobiZariskiHomologySequence_negOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean#L469). The attribute's comment: “exactness of the six-term sequence of cohomology sheaves at the node H^{-1}(NL_{X/Z}), for the maps induced by the canonical maps f^*NL_{Y/Z} -> NL_{X/Z} and NL_{X/Z} -> NL_{X/Y}”.

> **Stacks 0E1Z, exactness at `H^{-1}(NL_{X/Z})`.**  For composable morphisms of ringed spaces
> `f : X ⟶ Y` and `g : Y ⟶ Z` the sequence
>
> `H^{-1}(f^*NL_{Y/Z}) ⟶ H^{-1}(NL_{X/Z}) ⟶ H^{-1}(NL_{X/Y})`
>
> of cohomology sheaves is exact at the middle term.

```lean
theorem exact_ringedSpaceJacobiZariskiHomologySequence_negOne :
    (ringedSpaceJacobiZariskiHomologySequence f g (-1)).Exact
```

**`Stacks.SheafOfModules.exact_ringedSpaceJacobiZariskiHomologySequence_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean#L485). The attribute's comment: “exactness of the six-term sequence of cohomology sheaves at the node H^0(NL_{X/Z}), for the maps induced by the canonical maps f^*NL_{Y/Z} -> NL_{X/Z} and NL_{X/Z} -> NL_{X/Y}”.

> **Stacks 0E1Z, exactness at `H⁰(NL_{X/Z})`.**  For composable morphisms of ringed spaces
> `f : X ⟶ Y` and `g : Y ⟶ Z` the sequence
>
> `H⁰(f^*NL_{Y/Z}) ⟶ H⁰(NL_{X/Z}) ⟶ H⁰(NL_{X/Y})`
>
> of cohomology sheaves is exact at the middle term.

```lean
theorem exact_ringedSpaceJacobiZariskiHomologySequence_zero :
    (ringedSpaceJacobiZariskiHomologySequence f g 0).Exact
```

**`Stacks.SheafOfModules.epi_homologyMap_ringedSpaceRelativeNaiveCotangentComplexMap_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSheaves.lean#L516). The attribute's comment: “the final `-> 0` of the six-term sequence of cohomology sheaves, that is, its exactness at H^0(NL_{X/Y}): the map induced by the canonical map NL_{X/Z} -> NL_{X/Y} is surjective”.

> **Stacks 0E1Z, the final `⟶ 0` of the six-term sequence**: the canonical map
> `NL_{X/Z} ⟶ NL_{X/Y}` is surjective on `H⁰`, that is, the sequence of cohomology sheaves is exact
> at `H⁰(NL_{X/Y})`.  This is the statement of Stacks 0E1Y for the tower
> `(g ∘ f)⁻¹O_Z ⟶ f⁻¹O_Y ⟶ O_X`.

```lean
theorem epi_homologyMap_ringedSpaceRelativeNaiveCotangentComplexMap_zero :
    Epi (HomologicalComplex.homologyMap (spaceRelativeNaiveCotangentComplexMap
      (inverseImageBaseRing f g) (inverseImageMiddleRing f) X.sheaf
      (inverseImageFirstRingMap f g) (ringedSpaceStructureMap f)) 0)
```

**`Stacks.SheafOfModules.ringedSpaceJacobiZariskiConnecting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean#L245). The attribute's comment: “the connecting morphism H^{-1}(NL_{X/Y}) -> H^0(f^*NL_{Y/Z})”.

> **Stacks 0E1Z, the connecting morphism of the six-term sequence**
> `∂ : H^{-1}(NL_{X/Y}) ⟶ H⁰(f^*NL_{Y/Z})`, for composable morphisms of ringed spaces.

```lean
noncomputable def ringedSpaceJacobiZariskiConnecting
```

**`Stacks.SheafOfModules.exact_ringedSpaceJacobiZariskiSixTerm_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean#L354). The attribute's comment: “exactness of the six-term sequence at H^0(f^*NL_{Y/Z})”.

> **Stacks 0E1Z, exactness at `H⁰(f^*NL_{Y/Z})`.**  For composable morphisms of ringed spaces
> `f : X ⟶ Y` and `g : Y ⟶ Z` the sequence
>
> `H^{-1}(NL_{X/Y}) --∂--> H⁰(f^*NL_{Y/Z}) ⟶ H⁰(NL_{X/Z})`
>
> of cohomology sheaves is exact at the middle term.

```lean
theorem exact_ringedSpaceJacobiZariskiSixTerm_zero :
    (ShortComplex.mk (ringedSpaceJacobiZariskiConnecting f g)
      (HomologicalComplex.homologyMap ((pulledNaiveCotangentComparison f g).hom ≫
        spaceBaseChangeNaiveCotangentMap (inverseImageBaseRing f g)
          (inverseImageMiddleRing f) X.sheaf (inverseImageFirstRingMap f g)
          (ringedSpaceStructureMap f)) 0)
      (ringedSpaceJacobiZariskiConnecting_comp_homologyMap f g)).Exact
```

**`Stacks.SheafOfModules.exact_ringedSpaceJacobiZariskiSixTerm_negOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentJacobiZariskiSixTerm.lean#L371). The attribute's comment: “exactness of the six-term sequence at H^{-1}(NL_{X/Y})”.

> **Stacks 0E1Z, exactness at `H^{-1}(NL_{X/Y})`.**  For composable morphisms of ringed spaces
> `f : X ⟶ Y` and `g : Y ⟶ Z` the sequence
>
> `H^{-1}(NL_{X/Z}) ⟶ H^{-1}(NL_{X/Y}) --∂--> H⁰(f^*NL_{Y/Z})`
>
> of cohomology sheaves is exact at the middle term.

```lean
theorem exact_ringedSpaceJacobiZariskiSixTerm_negOne :
    (ShortComplex.mk
      (HomologicalComplex.homologyMap (spaceRelativeNaiveCotangentComplexMap
        (inverseImageBaseRing f g) (inverseImageMiddleRing f) X.sheaf
        (inverseImageFirstRingMap f g) (ringedSpaceStructureMap f)) (-1))
      (ringedSpaceJacobiZariskiConnecting f g)
      (homologyMap_comp_ringedSpaceJacobiZariskiConnecting f g)).Exact
```

**`Stacks.SheafOfModules.ringedSpaceNaiveCotangentConeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean#L598). The attribute's comment: “the canonical map f^*NL_{Y/Z} -> C(NL_{X/Z} -> NL_{X/Y})[-1] to the shifted cone”.

> **Stacks 0E1Z, the canonical map.**  For composable morphisms of ringed spaces
> `f : X ⟶ Y` and `g : Y ⟶ Z`, the canonical map
>
> `f^*NL_{Y/Z} ⟶ C(NL_{X/Z} ⟶ NL_{X/Y})[-1]`
>
> of complexes of `O_X`-modules: the canonical map of Stacks 0E1Y for the sheaves of rings
> `(g ∘ f)⁻¹O_Z ⟶ f⁻¹O_Y ⟶ O_X` on `X`, precomposed with the identification of `f^*NL_{Y/Z}`
> with the base change of `NL_{f⁻¹O_Y/(g ∘ f)⁻¹O_Z}`.
>
> All six assertions of the six-term exact sequence of cohomology sheaves are covered: exactness
> at `H^{-1}(NL_{X/Z})`, at `H^0(NL_{X/Z})` and at `H^0(NL_{X/Y})` (the final `→ 0`) by
> `Stacks.SheafOfModules.exact_ringedSpaceJacobiZariskiHomologySequence_negOne`, `_zero` and
> `Stacks.SheafOfModules.epi_homologyMap_ringedSpaceRelativeNaiveCotangentComplexMap_zero`;
> exactness at `H^{-1}(NL_{X/Y})` and at `H^0(f^*NL_{Y/Z})`, and the connecting map, by
> `Stacks.SheafOfModules.exact_ringedSpaceJacobiZariskiSixTerm_negOne`, `_zero` and
> `Stacks.SheafOfModules.ringedSpaceJacobiZariskiConnecting`, which rest on
> `Stacks.SheafOfModules.isIso_homologyMap_ringedSpaceNaiveCotangentConeMap_zero`.

```lean
noncomputable def ringedSpaceNaiveCotangentConeMap :
    pulledNaiveCotangentComplex f g ⟶
      (CategoryTheory.shiftFunctor
          (CochainComplex (_root_.SheafOfModules.{u}
            (Stacks.SheafOfModules.Tensor.ringSheaf (J := Opens.grothendieckTopology (X : TopCat))
              X.sheaf)) ℤ) (-1 : ℤ)).obj
        (CochainComplex.mappingCone (spaceRelativeNaiveCotangentComplexMap
          (inverseImageBaseRing f g) (inverseImageMiddleRing f) X.sheaf
          (inverseImageFirstRingMap f g) (ringedSpaceStructureMap f)))
```

**`Stacks.SheafOfModules.ringedSpaceNaiveCotangentConeMap_comp_pShift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean#L619). The attribute's comment: “the defining property of the canonical map: composed with the cone projection it is the map f^*NL_{Y/Z} -> NL_{X/Z}”.

> **Stacks 0E1Z, the canonical map.**  The canonical map
> `f^*NL_{Y/Z} ⟶ C(NL_{X/Z} ⟶ NL_{X/Y})[-1]`, composed with the projection of the shifted cone
> onto `NL_{X/Z}`, is the canonical map `f^*NL_{Y/Z} ⟶ NL_{X/Z}`.
>
> The six assertions of the six-term exact sequence drawn from this map are all covered; see the
> docstring of `Stacks.SheafOfModules.ringedSpaceNaiveCotangentConeMap` for where each one is.

```lean
theorem ringedSpaceNaiveCotangentConeMap_comp_pShift :
    ringedSpaceNaiveCotangentConeMap f g ≫
        pShift (spaceRelativeNaiveCotangentComplexMap (inverseImageBaseRing f g)
          (inverseImageMiddleRing f) X.sheaf (inverseImageFirstRingMap f g)
          (ringedSpaceStructureMap f)) =
      (pulledNaiveCotangentComparison f g).hom ≫
        spaceBaseChangeNaiveCotangentMap (inverseImageBaseRing f g)
          (inverseImageMiddleRing f) X.sheaf (inverseImageFirstRingMap f g)
          (ringedSpaceStructureMap f)
```

**`Stacks.SheafOfModules.ringedSpaceNaiveCotangentConeMap_comp_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean, line 651](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExactSequence.lean#L651). The attribute's comment: “the second defining property of the canonical map: its degree -1 component is the explicit homotopy”.

> **Stacks 0E1Z, the canonical map.**  The canonical map
> `f^*NL_{Y/Z} ⟶ C(NL_{X/Z} ⟶ NL_{X/Y})[-1]`, composed with the degree `-1` projection of the
> shifted cone onto `NL_{X/Y}`, is the identification `f^*NL_{Y/Z} ≅ NL_{f⁻¹O_Y/(g ∘ f)⁻¹O_Z} ⊗ O_X`
> followed by the explicit null homotopy of the proof of Stacks 0E1Y for the tower
> `(g ∘ f)⁻¹O_Z ⟶ f⁻¹O_Y ⟶ O_X`.  Together with
> `ringedSpaceNaiveCotangentConeMap_comp_pShift` this determines the canonical map.
>
> The six assertions of the six-term exact sequence drawn from this map are all covered; see the
> docstring of `Stacks.SheafOfModules.ringedSpaceNaiveCotangentConeMap` for where each one is.

```lean
theorem ringedSpaceNaiveCotangentConeMap_comp_snd :
    (CochainComplex.HomComplex.Cochain.ofHom
          (ringedSpaceNaiveCotangentConeMap f g)).comp
        ((CochainComplex.mappingCone.snd
            (spaceRelativeNaiveCotangentComplexMap (inverseImageBaseRing f g)
              (inverseImageMiddleRing f) X.sheaf (inverseImageFirstRingMap f g)
              (ringedSpaceStructureMap f))).leftShift (-1) (-1) (by omega)) (by omega) =
      (CochainComplex.HomComplex.Cochain.ofHom
            (pulledNaiveCotangentComparison f g).hom).comp
        (CochainComplex.HomComplex.Cochain.ofHomotopy
          (ringedSpaceBaseChangeRelativeNullHomotopy f g)) (zero_add (-1))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.31, Tag 08TG](https://stacks.math.columbia.edu/tag/08TG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
