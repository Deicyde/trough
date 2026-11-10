---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.hasPropertyOnAffineChartMap_adicStar_iff, Rig.adicFiniteType_tfae, TopologicalRing.adicTopologicallyFiniteType_isLocal, TopologicalRing.adicTopologicallyFiniteType_isomorphismInvariant, TopologicalRing.adicTopologicallyFiniteType_isLocal', Rig.nonempty_restrictedNaiveCotangentComplex, Rig.nonempty_restrictedPowerSeriesPresentation, Rig.exists_noetherianPresentationComparison
statement: formalized
proof: formalized
---

# 88.11 Finite type morphisms

Section 88.11 of the Stacks Project, [Tag 0GBV](https://stacks.math.columbia.edu/tag/0GBV). 5 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GBW, a lemma

[Tag 0GBW](https://stacks.math.columbia.edu/tag/0GBW) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyOnAffineChartMap_adicStar_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicFiniteTypeCharacterization.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicFiniteTypeCharacterization.lean#L223). The attribute's comment: “the equivalence of conditions (1) and (2), read on a map of affine formal algebraic spaces whose presenting rings are all adic*”.

> **The equivalence of conditions (1) and (2) of Stacks 0GBW, read on charts.** Let
> `t : U ⟶ V` be a map of affine formal algebraic spaces over `S` all of whose presenting
> topological rings are adic\*. Then `t` corresponds to an adic, topologically of finite type
> arrow of `WAdm^{adic*}` exactly when it corresponds to a taut, topologically of finite type
> arrow of `WAdm^{count}`.
>
> The two conditions quantify over different classes of presentations, so neither inclusion is
> formal: the condition for countably indexed weakly admissible rings quantifies over strictly
> more presentations, since an adic\* ring is countably indexed weakly admissible, and the
> hypotheses `hU` and `hV` are what make the two ranges of quantification agree. On a single
> presentation the two properties of the arrow are identified by Stacks 0GBW.

```lean
theorem hasPropertyOnAffineChartMap_adicStar_iff {U V : FppfSheaf B S hS} (t : U ⟶ V)
    (hU : ∀ (R : Type u) [CommRing R] [TopologicalSpace R] [IsTopologicalRing R]
      [IsLinearTopology R R] (E : QuotientSystem B S hS R), (U ≅ formalSpectrum E) →
      TopologicalRing.IsAdicStar R)
    (hV : ∀ (A : Type u) [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
      [IsLinearTopology A A] (D : QuotientSystem B S hS A), (V ≅ formalSpectrum D) →
      TopologicalRing.IsAdicStar A) :
    HasPropertyOnAffineChartMap B S hS TopologicalRing.IsAdicStar
        TopologicalRing.IsAdicTopologicallyOfFiniteTypeHom t ↔
      HasPropertyOnAffineChartMap B S hS TopologicalRing.IsCountablyWeaklyAdmissible
        TopologicalRing.IsTautTopologicallyOfFiniteTypeHom t
```

**`Rig.adicFiniteType_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FiniteType.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/FiniteType.lean#L719). The attribute's comment: “equivalent_conditions”. References: EGA I (10.13.4); EGA I (10.13.1), “affine case”; EGA 0 (7.5.5), “(a) <=> (c)”.

> The eight characterizations of an adic morphism of topologically finite type.

```lean
public theorem adicFiniteType_tfae (φ : A →+* B) (hφ : Continuous φ)
    (hA : TopologicalRing.IsAdic A) (hB : TopologicalRing.IsAdic B)
    (hAfg : ∃ I : Ideal A, TopologicalRing.IsIdealOfDefinition I ∧ I.FG)
    (hBfg : ∃ J : Ideal B, TopologicalRing.IsIdealOfDefinition J ∧ J.FG) :
    List.TFAE [
      RingHom.IsAdic φ ∧ TopologicalRing.IsTopologicallyOfFiniteType φ,
      RingHom.IsTaut φ ∧ TopologicalRing.IsTopologicallyOfFiniteType φ,
      FiniteTypeModuloSomeIdealOfDefinition φ,
      FiniteTypeModuloEveryIdealOfDefinition φ,
      FiniteTypeAdicAlgebraForSomeIdeal φ,
      FiniteTypeAdicAlgebraForEveryIdeal φ,
    TopologicalRing.HasRestrictedPowerSeriesPresentation φ,
      HasCompletedPolynomialPresentation φ]
```

**`TopologicalRing.adicTopologicallyFiniteType_isLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocal.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocal.lean#L111). The attribute's comment: “local_property”.

> **Stacks 0GBW.** Being adic and topologically of finite type is a local property of
> morphisms of weakly admissible adic-star rings: it ascends along completed étale localization
> diagrams, descends along faithfully flat ones, and is preserved by finite products of
> targets.

```lean
public theorem adicTopologicallyFiniteType_isLocal :
    AdicStarPropertyIsLocal.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsAdic φ ∧ IsTopologicallyOfFiniteType φ)
```

**`TopologicalRing.adicTopologicallyFiniteType_isomorphismInvariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocalRefined.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocalRefined.lean#L58). The attribute's comment: “local_property”.

> Being adic and topologically of finite type is independent of the presentations of the source
> and the target.

```lean
public theorem adicTopologicallyFiniteType_isomorphismInvariant :
    IsomorphismInvariant.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsAdic φ ∧ IsTopologicallyOfFiniteType φ)
      (fun R ↦ ∃ I : Ideal R, I.FG ∧ _root_.IsAdic I)
```

**`TopologicalRing.adicTopologicallyFiniteType_isLocal'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocalRefined.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocalRefined.lean#L74). The attribute's comment: “local_property”.

> Being adic and topologically of finite type is a local property of morphisms of weakly
> admissible adic-star rings: it is independent of the presentations of the source and the target,
> ascends along completed étale localization diagrams, descends along faithfully flat ones, and is
> preserved by finite products of targets.

```lean
public theorem adicTopologicallyFiniteType_isLocal' :
    AdicStarPropertyIsLocal'.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsAdic φ ∧ IsTopologicallyOfFiniteType φ)
```

## Tag 0GBX, a remark

[Tag 0GBX](https://stacks.math.columbia.edu/tag/0GBX) in the Stacks Project.

**`Rig.nonempty_restrictedNaiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/Construction.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/Construction.lean#L476).

> **Stacks Project, Remark 88.14.3 (Tag 0GBX).** For a presentation
> `B = A{x₁, …, x_r} / J` of `B` as a topological `A`-algebra, the completed naive cotangent
> complex `NL^∧_{B/A} = (J / J² → ⨁ i, B dxᵢ)` exists: the formal partial derivatives of
> `A{x₁, …, x_r}` exist, and the differential sending the class of a restricted power series
> `g ∈ J` to the tuple of its formal partial derivatives is well defined. Since
> `RestrictedNaiveCotangentComplex P` is a subsingleton, this determines the complex.

```lean
public theorem nonempty_restrictedNaiveCotangentComplex
    (P : RestrictedPowerSeriesPresentation A B) :
    Nonempty (RestrictedNaiveCotangentComplex P)
```

**`Rig.nonempty_restrictedPowerSeriesPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/Construction.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/Construction.lean#L536). The attribute's comment: “every adic, topologically finite type arrow has a presentation”.

> **Stacks Project, Tag 0GBX.** An arrow of `WAdm^{adic*}` which is adic and topologically
> of finite type can be written as `B = A{x₁, …, x_r} / J`, so that the construction applies to
> it. This is condition (7) of Lemma 0GBW.

```lean
public theorem nonempty_restrictedPowerSeriesPresentation
    (hcont : Continuous (algebraMap A B))
    (hA : TopologicalRing.IsAdic A) (hB : TopologicalRing.IsAdic B)
    (hAfg : ∃ I : Ideal A, TopologicalRing.IsIdealOfDefinition I ∧ I.FG)
    (hBfg : ∃ J : Ideal B, TopologicalRing.IsIdealOfDefinition J ∧ J.FG)
    (hadic : _root_.RingHom.IsAdic (algebraMap A B))
    (hft : TopologicalRing.IsTopologicallyOfFiniteType (algebraMap A B)) :
    Nonempty (RestrictedPowerSeriesPresentation A B)
```

**`Rig.exists_noetherianPresentationComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/NoetherianComparison.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/NoetherianComparison.lean#L569). The attribute's comment: “agreement with Equation 0AJR”.

> **Stacks Project, Tag 0GBX.** When `A` is Noetherian and `I` is an ideal of definition for
> its topology, the complex of Tag 0GBX reproduces the completed naive cotangent complex of
> `B` over `(A, I)` defined by Equation 0AJR.

```lean
public theorem exists_noetherianPresentationComparison
    {I : Ideal A} (_hI : TopologicalRing.IsIdealOfDefinition I) (hIadic : _root_.IsAdic I)
    {C : Type v} [CommRing C] [Algebra A C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C]
    (hc : IsAdicComplete (I.map (algebraMap A C)) C)
    [Algebra.FiniteType (A ⧸ I) (C ⧸ I.map (algebraMap A C))]
    (P : RestrictedPowerSeriesPresentation A C) :
    ∃ Q : CompletedPolynomialPresentation I (AdicFiniteTypeAlgebra.of C hc),
      Nonempty (NoetherianPresentationComparison (restrictedNaiveCotangentComplex P) hc Q)
```

**`Rig.nonempty_homotopyEquiv_of_idealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/NoetherianComparison.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/NoetherianComparison.lean#L672). The attribute's comment: “independence of the ideal of definition”. References: SGA 6 0 (4.4), “partial”.

> **Stacks Project, Tag 0GBX.** For `A` an adic Noetherian topological ring, the completed
> naive cotangent complex of Equation 0AJR is independent of the choice of the ideal of
> definition `I ⊆ A`: both are the complex of Tag 0GBX, which is built from the topology of `A`
> alone.

```lean
public theorem nonempty_homotopyEquiv_of_idealOfDefinition
    {I I' : Ideal A}
    (hI : TopologicalRing.IsIdealOfDefinition I) (hIadic : _root_.IsAdic I)
    (hI' : TopologicalRing.IsIdealOfDefinition I') (hIadic' : _root_.IsAdic I')
    {C : Type v} [CommRing C] [Algebra A C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C]
    (hc : IsAdicComplete (I.map (algebraMap A C)) C)
    [Algebra.FiniteType (A ⧸ I) (C ⧸ I.map (algebraMap A C))]
    (hc' : IsAdicComplete (I'.map (algebraMap A C)) C)
    [Algebra.FiniteType (A ⧸ I') (C ⧸ I'.map (algebraMap A C))]
    (P : RestrictedPowerSeriesPresentation A C)
    (Q : CompletedPolynomialPresentation I (AdicFiniteTypeAlgebra.of C hc))
    (Q' : CompletedPolynomialPresentation I' (AdicFiniteTypeAlgebra.of C hc')) :
    Nonempty (HomotopyEquiv
      (Rig.completedNaiveCotangentComplex (AdicFiniteTypeAlgebra.of C hc) Q).cochainComplex
      (Rig.completedNaiveCotangentComplex
        (AdicFiniteTypeAlgebra.of C hc') Q').cochainComplex)
```

**`Rig.exists_restrictedPresentationComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/PresentationComparison.lean, line 732](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/PresentationComparison.lean#L732). The attribute's comment: “well defined in K(B)”.

> **Stacks Project, Tag 0GBX.** Any two presentations of `B` are related by a morphism of
> presentations, and the map of complexes it induces is a homotopy equivalence. This is the
> existence half of "the complex is well defined in `K(B)`".

```lean
public theorem exists_restrictedPresentationComparison :
    Nonempty (RestrictedPresentationComparison K L)
```

**`Rig.homotopy_of_restrictedPresentationComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/PresentationComparison.lean, line 773](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/NaiveCotangent/RestrictedPresentation/PresentationComparison.lean#L773). The attribute's comment: “unique isomorphism in K(B)”.

> **Stacks Project, Tag 0GBX.** The isomorphism in `K(B)` is *unique*: any two morphisms of
> presentations induce homotopic maps of complexes. This is Step 2 of the proof of Lemma
> 0GAE.

```lean
public theorem homotopy_of_restrictedPresentationComparison
    (e e' : RestrictedPresentationComparison K L) :
    Nonempty (Homotopy e.equiv.hom e'.equiv.hom)
```

## Tag 0GBY, a lemma

[Tag 0GBY](https://stacks.math.columbia.edu/tag/0GBY) in the Stacks Project.

**`TopologicalRing.adicAndFiniteType_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FiniteTypeBaseChange.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FiniteTypeBaseChange.lean#L221).

> Adic morphisms of topologically finite type in the category of weakly admissible adic-star
> rings form a local property which is stable under completed tensor-product base change.

```lean
public theorem adicAndFiniteType_isStableUnderBaseChange :
    TopologicalRing.AdicStarPropertyIsStableUnderBaseChange.{u}
      (fun φ => RingHom.IsAdic φ ∧ TopologicalRing.IsTopologicallyOfFiniteType φ)
```

## Tag 0GBZ, a lemma

[Tag 0GBZ](https://stacks.math.columbia.edu/tag/0GBZ) in the Stacks Project.

**`TopologicalRing.adicTopologicallyFiniteType_isStableUnderComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocal.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocal.lean#L156).

> **Stacks 0GBZ.** The local property of Stacks 0GBW — being adic and topologically of finite
> type — is stable under composition on weakly admissible adic-star rings.

```lean
public theorem adicTopologicallyFiniteType_isStableUnderComposition :
    AdicStarPropertyIsStableUnderComposition.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsAdic φ ∧ IsTopologicallyOfFiniteType φ)
```

**`TopologicalRing.adicTopologicallyFiniteType_isStableUnderComposition'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocalRefined.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicFiniteTypeIsLocalRefined.lean#L87).

> Being adic and topologically of finite type is stable under composition on weakly admissible
> adic-star rings.

```lean
public theorem adicTopologicallyFiniteType_isStableUnderComposition' :
    AdicStarPropertyIsStableUnderComposition'.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsAdic φ ∧ IsTopologicallyOfFiniteType φ)
```

## Tag 0GC0, a lemma

[Tag 0GC0](https://stacks.math.columbia.edu/tag/0GC0) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_adicStar_tfae'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicFiniteTypeCharacterizationRefined.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicFiniteTypeCharacterizationRefined.lean#L59). The attribute's comment: “all four conditions, with all six equivalences proved, from one named hypothesis this library does not have: Stacks 0AKX in the adic* form of Stacks 0AKT together with Stacks 0AIC as `hchart`. The library's Stacks 0ANW is unconditional, so nothing is forwarded from it; the covering refinement of Stacks 0AJ2 and the implication (2) implies (1) of Stacks 0AKX, which used to be forwarded as `href` and `h0AKX`, are theorems. Stacks 0AJ3, the implication (4) implies (1) of Stacks 0ANL and Stacks 0ANV on countably indexed charts are no longer among them: Stacks 0AJ3 is proved for a base which is a formal algebraic space, (4) implies (1) is obtained as (4) implies (5) implies (1), and Stacks 0ANV on countably indexed charts is proved. Neither are the locality axioms of Situation 0CBA for tautness with topological finite type: they follow from the locality of Stacks 0ANU”.

> For a morphism `f : X ⟶ Y` of locally adic\* formal algebraic spaces over `S`, the condition
> that every affine representable étale square over `f` carry an adic, topologically of finite type
> arrow of `WAdm^{adic*}`, the existence of an affine étale covering of `Y` together with affine
> étale coverings of the fibre products of its members with `X` on which that condition holds, the
> existence of an affine étale covering of `X` whose members factor through affine representable
> étale charts of `Y` by such arrows, and `f` being locally of finite type, are all equivalent,
> provided chart presentations are adic\*.

```lean
theorem isLocallyOfFiniteType_adicStar_tfae' {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyAdicStar B S hS X) (hY : IsLocallyAdicStar B S hS Y)
    (hchart : ChartPresentationIsAdicStar B S hS) :
    List.TFAE
      [HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar
          TopologicalRing.IsAdicTopologicallyOfFiniteTypeHom f,
        HasPropertyAfterTargetCover B S hS TopologicalRing.IsAdicStar
          TopologicalRing.IsAdicTopologicallyOfFiniteTypeHom f,
        HasPropertyAfterSourceCover B S hS TopologicalRing.IsAdicStar
          TopologicalRing.IsAdicTopologicallyOfFiniteTypeHom f,
        IsLocallyOfFiniteType B S hS f]
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_tfae_of_isLocallyAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicFiniteTypeCharacterizationUnconditional.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicFiniteTypeCharacterizationUnconditional.lean#L89).

> **Stacks 0GC0.** Let `f : X ⟶ Y` be a morphism of locally adic\* formal algebraic spaces
> over `S`. The following are equivalent:
>
> 1. for every commutative square with `U`, `V` affine formal algebraic spaces and `U ⟶ X`,
>    `V ⟶ Y` representable by algebraic spaces and étale, the morphism `U ⟶ V` corresponds to an
>    arrow of `WAdm^{adic*}` which is adic and topologically of finite type;
> 2. there are a covering `{Yⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Xⱼᵢ ⟶ Yⱼ ×_Y X}` as in Definition 0AIM such that each `Xⱼᵢ ⟶ Yⱼ` corresponds to an arrow
>    of `WAdm^{adic*}` which is adic and topologically of finite type;
> 3. there are a covering `{Xᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Xᵢ ⟶ Yᵢ ⟶ Y` where `Yᵢ` is an affine formal algebraic space, `Yᵢ ⟶ Y` is representable by
>    algebraic spaces and étale, and `Xᵢ ⟶ Yᵢ` corresponds to an arrow of `WAdm^{adic*}` which
>    is adic and topologically of finite type;
> 4. `f` is locally of finite type.
>
> This is the source's proof. By Stacks 0AKX for the adic\* property together with Stacks 0AIC
> (`chartPresentationIsAdicStarOfWeaklyAdmissible`) every weakly admissible ring presenting an
> affine chart of `X` or `Y` is adic\*, so on each chart the adic, topologically of finite type
> condition and the taut, topologically of finite type condition agree by Stacks 0GBW
> (`hasPropertyOnAffineChartMap_adicStar_iff_of_isWeaklyAdmissible`); and Stacks 0ANW
> (`isLocallyOfFiniteType_tfae'`), for the locally countably indexed spaces `X` and `Y`,
> identifies the three resulting conditions with `f` being locally of finite type.

```lean
theorem isLocallyOfFiniteType_tfae_of_isLocallyAdicStar {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsLocallyAdicStar B S hS X) (hY : IsLocallyAdicStar B S hS Y) :
    List.TFAE
      [HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar
          TopologicalRing.IsAdicTopologicallyOfFiniteTypeHom f,
        HasPropertyAfterTargetCover B S hS TopologicalRing.IsAdicStar
          TopologicalRing.IsAdicTopologicallyOfFiniteTypeHom f,
        HasPropertyAfterSourceCover B S hS TopologicalRing.IsAdicStar
          TopologicalRing.IsAdicTopologicallyOfFiniteTypeHom f,
        IsLocallyOfFiniteType B S hS f]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.11, Tag 0GBV](https://stacks.math.columbia.edu/tag/0GBV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
