---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.exists_colimit_presentation_of_isAffineFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.exists_colimit_presentation_of_quasiCompact_quasiSeparated, AlgebraicGeometry.LocallyTopologicallyRingedSpace.exists_subfamily_isFundamentalSystemOfIdealsOfDefinitionOn_of_isFormalScheme, AlgebraicGeometry.exists_isFundamentalSystemOfIdealsOfDefinitionOn_of_isFormalScheme, AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_iff_isAffine_reduction
statement: formalized
proof: formalized
---

# 87.18 Quasi-compact and quasi-separated formal algebraic spaces

Section 87.18 of the Stacks Project, [Tag 0AJD](https://stacks.math.columbia.edu/tag/0AJD). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AJE, a lemma

[Tag 0AJE](https://stacks.math.columbia.edu/tag/0AJE) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_colimit_presentation_of_isAffineFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactQuasiSeparatedPresentation.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactQuasiSeparatedPresentation.lean#L114). The attribute's comment: “the conclusion for an AFFINE formal algebraic space only; the general quasi-compact quasi-separated case is not proved here, see the implementation notes”.

> An affine formal algebraic space over `S` is a directed colimit of algebraic spaces over `S`
> along thickenings.

```lean
public theorem exists_colimit_presentation_of_isAffineFormalAlgebraicSpace
    (X : FppfSheaf B S hS) (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) := Sheaf.instHasColimitsOfSize
    ∃ (Λ : Type (u + 1)) (pre : Preorder Λ),
      letI : Preorder Λ := pre
      Nonempty Λ ∧ IsDirected Λ (· ≤ ·) ∧
        ∃ D : Λ ⥤ AlgebraicSpaces B S hS,
          (∀ ⦃i j : Λ⦄ (f : i ⟶ j), Space.IsThickeningHom B S hS (D.map f)) ∧
          Nonempty (X ≅ colimit (D ⋙ liftSheafFunctor B S hS))
```

**`AlgebraicGeometry.FormalSpace.exists_colimit_presentation_of_quasiCompact_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactQuasiSeparatedPresentation.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiCompactQuasiSeparatedPresentation.lean#L205).

> Let `S` be a scheme contained in a big fppf site `B` and let `X` be a formal algebraic space
> over `S` which is quasi-compact and quasi-separated. Then `X` is a directed colimit of algebraic
> spaces over `S` all of whose transition morphisms are thickenings.

```lean
theorem exists_colimit_presentation_of_quasiCompact_quasiSeparated
    (X : FppfSheaf B S hS) (_hX : IsFormalAlgebraicSpace B S hS X)
    (hqc : IsQuasiCompactSpace B S hS X) (hqs : IsQuasiSeparated B S hS X) :
    letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) := Sheaf.instHasColimitsOfSize
    ∃ (Λ : Type (u + 1)) (pre : Preorder Λ),
      letI : Preorder Λ := pre
      Nonempty Λ ∧ IsDirected Λ (· ≤ ·) ∧
        ∃ D : Λ ⥤ AlgebraicSpaces B S hS,
          (∀ ⦃i j : Λ⦄ (f : i ⟶ j), Space.IsThickeningHom B S hS (D.map f)) ∧
          Nonempty (X ≅ colimit (D ⋙ liftSheafFunctor B S hS))
```

## Tag 0AJF, a remark

[Tag 0AJF](https://stacks.math.columbia.edu/tag/0AJF) in the Stacks Project.

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.exists_subfamily_isFundamentalSystemOfIdealsOfDefinitionOn_of_isFormalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FundamentalSystemOfIdealsOfDefinition.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FundamentalSystemOfIdealsOfDefinition.lean#L147). The attribute's comment: “the shrinking of a fundamental system of WEAK ideals of definition to one of ideals of definition; the weak system is a hypothesis, see the implementation notes”.

> **Stacks 0AJF.** A quasi-compact formal scheme à la EGA carrying a fundamental system of weak
> ideals of definition carries a fundamental system of genuine ideals of definition, over a finite
> covering by affine formal open subschemes.
>
> This is the remark's conclusion. Its hypothesis — the fundamental system of weak ideals of
> definition — is what the translation of Stacks 0AJE supplies, and that *translation* is not
> carried by this library, although Stacks 0AJE itself is; see the implementation notes of this
> file. Here the class of opens is the class of
> affine formal open subschemes, so the two geometric inputs of
> `exists_subfamily_isFundamentalSystemOfIdealsOfDefinitionOn`
> are discharged: the affine formal opens cover `X` because `X` is a formal scheme, and the ring of
> sections over one of them is pre-admissible by Stacks 0AHY.

```lean
public theorem exists_subfamily_isFundamentalSystemOfIdealsOfDefinitionOn_of_isFormalScheme
    {X : LTRS.{u}} [CompactSpace ↥X] (hX : IsFormalScheme X) (𝒮 : Set (IdealSheaf X))
    (hne : 𝒮.Nonempty)
    (hdir : ∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
      K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W)
    (hfund : IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X)) :
    ∃ 𝒰 : Set (Opens X), 𝒰.Finite ∧ (∀ V ∈ 𝒰, IsAffineFormalOpen X V) ∧ sSup 𝒰 = ⊤ ∧
      ∃ 𝒮' : Set (IdealSheaf X), 𝒮' ⊆ 𝒮 ∧ 𝒮'.Nonempty ∧
        IsFundamentalSystemOfIdealsOfDefinitionOn 𝒮' (· ∈ 𝒰)
```

**`AlgebraicGeometry.exists_isFundamentalSystemOfIdealsOfDefinitionOn_of_isFormalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FundamentalSystemOfIdealsOfDefinitionExistence.lean, line 568](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FundamentalSystemOfIdealsOfDefinitionExistence.lean#L568).

> **Stacks 0AJF.** Every quasi-compact and quasi-separated formal scheme à la EGA has a
> fundamental system of ideals of definition: a nonempty family of ideal sheaves, sectionwise
> directed, each of which is an ideal of definition over every affine formal open subscheme, and
> whose ideals of sections over every affine formal open subscheme form a neighbourhood basis of
> zero.
>
> The members are the intersections `⋂ᵢ ker(Spec (Aᵢ/Jᵢ) ⟶ X)` over a finite covering by affine
> formal charts `Spf Aᵢ`, which is the ideal of the scheme-theoretic image that the source's
> induction produces; see the implementation notes. Quasi-separatedness is that of the underlying
> space, which for a formal scheme à la EGA is quasi-separatedness of the formal scheme.

```lean
theorem exists_isFundamentalSystemOfIdealsOfDefinitionOn_of_isFormalScheme
    {X : LTRS.{u}} [CompactSpace ↥X] [QuasiSeparatedSpace ↥X] (hX : IsFormalScheme X) :
    ∃ 𝒮 : Set (IdealSheaf X), 𝒮.Nonempty ∧
      (∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
        K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W) ∧
      IsFundamentalSystemOfIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X)
```

## Tag 0DE8, a lemma

[Tag 0DE8](https://stacks.math.columbia.edu/tag/0DE8) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_iff_isAffine_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineOfAffineReduction.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineOfAffineReduction.lean#L396). The attribute's comment: “affineness of the reduction rendered as its being the sheaf of an object of the site with affine underlying scheme, the shape Stacks 0AIN delivers in the affine case; stated for an arbitrary reduction i : X\_red -> X, which generalizes the source's canonical one”.

> **Stacks 0DE8.** Let `S` be a scheme contained in a big fppf site `B` and let `X` be a formal
> algebraic space over `S` with reduction `i : X_red ⟶ X` as in Stacks 0AIN. Then `X` is an affine
> formal algebraic space over `S` if and only if `X_red` is affine, that is, if and only if it is
> the sheaf of an object of the site with affine underlying scheme.
>
> Nothing is granted. The converse direction uses, for one stage of the presentation of Stacks 0AJE,
> that an algebraic space receiving a surjective closed immersion from an affine scheme of the site is
> affine: `AlgebraicGeometry.FormalSpace.isAffineOfSurjectiveClosedImmersion`, the closed-immersion
> case of Stacks 07VS, proved in
> `StacksFrontier.AlgebraicGeometry.Spaces.Thickenings.AffineOfAffineThickening`.

```lean
theorem isAffineFormalAlgebraicSpace_iff_isAffine_reduction
    {X Xred : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X)
    {i : Xred ⟶ X} (hi : IsReduction B S hS X Xred i) :
    IsAffineFormalAlgebraicSpace B S hS X ↔
      ∃ T : BigFppfOver B S hS, IsAffine ((BigFppfOver.toScheme B S hS).obj T) ∧
        Nonempty ((uliftYoneda.{u + 1}).obj T ≅ Xred.obj)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.18, Tag 0AJD](https://stacks.math.columbia.edu/tag/0AJD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
