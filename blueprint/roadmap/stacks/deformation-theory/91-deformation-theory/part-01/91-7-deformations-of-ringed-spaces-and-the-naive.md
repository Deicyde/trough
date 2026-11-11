---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpaceThickening.DeformationSolution, Stacks.SheafOfModules.presentationNaiveCotangentExtZeroAddEquiv, AlgebraicGeometry.RingedSpaceThickening.DeformationIdealDiagram.lifting_obstruction_and_torsor, AlgebraicGeometry.RingedSpaceThickening.liftingObstruction_eq_zero_iff, AlgebraicGeometry.RingedSpaceThickening.liftTranslate_zero, AlgebraicGeometry.RingedSpaceThickening.liftTranslate_add, AlgebraicGeometry.RingedSpaceThickening.existsUnique_liftTranslate, AlgebraicGeometry.RingedSpaceThickening.DeformationCube
statement: formalized
proof: formalized
---

# 91.7 Deformations of ringed spaces and the naive cotangent complex

Section 91.7 of the Stacks Project, [Tag 08U6](https://stacks.math.columbia.edu/tag/08U6). 12 tags here are carried by 57 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08U7, an equation

[Tag 08U7](https://stacks.math.columbia.edu/tag/08U7) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.DeformationSolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DeformationDiagram.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DeformationDiagram.lean#L60). The attribute's comment: “the deformation problem to solve”.

> A solution of the first order deformation problem for a fixed
> first order thickening `t : S ⟶ S'`, morphism `f : X ⟶ S`, `𝒪_X`-module `𝒢` and prescribed map
> `c : f^* t^* 𝒥 ⟶ 𝒢`: a first order thickening `i : X ⟶ X'` and a morphism `f' : X' ⟶ S'` over
> `t`, together with an identification of the ideal of `i` with `𝒢` under which the vertical map
> on ideals induced by `f'` is exactly `c`.

```lean
structure DeformationSolution {X S S' : RingedSpace.{u, u}} (t : S ⟶ S')
    (ht : IsFirstOrderThickening t) (f : X ⟶ S)
    (G : SheafOfModules.{u} (structureSheafRing X))
    (c : (modulePullback f).obj
      ((modulePullback t).obj (AlgebraicGeometry.SheafOfModules.idealSheaf t)) ⟶ G)
```

## Tag 08U8, a lemma

[Tag 08U8](https://stacks.math.columbia.edu/tag/08U8) in the Stacks Project.

**`Stacks.SheafOfModules.presentationNaiveCotangentExtZeroAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentExtZero.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentExtZero.lean#L120). The attribute's comment: “clause (2): the identification of the acting group Hom(H^0(NL(α)), G) = Hom(Omega\_\{B/A}, G) with Ext^0(NL(α), G), for NL(α) the naive cotangent complex of a polynomial presentation of a homomorphism of sheaves of rings on a site — the form the source's diagram takes after its own reduction to sheaves on one space. No hypothesis beyond the source. The remaining two links of the source's display, the adjunction Hom(Omega\_\{X\_1/S\_1}, g\_* G\_2) = Hom(g^* Omega\_\{X\_1/S\_1}, G\_2) and the passage from NL(α) to Lg^* NL\_\{X\_1/S\_1}, are not proved here; clause (1) and the principal homogeneous space structure itself are elsewhere”.

> The identification of `Ext⁰_B(NL(α), 𝒢)` with `Hom_B(Ω_{B/A}, 𝒢)`, for `NL(α)` the naive
> cotangent complex of a polynomial presentation of `B` over `A`.

```lean
noncomputable def presentationNaiveCotangentExtZeroAddEquiv :
    presentationNaiveCotangentExt.{v, u, w, z, t} J A B a E α G 0 ≃+
      (moduleOfDifferentialsOfSite.{v, u, w, z} A B a ⟶ G)
```

**`AlgebraicGeometry.RingedSpaceThickening.DeformationIdealDiagram.lifting_obstruction_and_torsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DeformationLiftingObstruction.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DeformationLiftingObstruction.lean#L273). References: EGA 0 (20.1.3), “more general”; EGA IV (16.5.14), “more general”.

> **Stacks Project, Tag 08U8.** In the situation of **Stacks 08U9** — a commutative cube of
> ringed spaces whose horizontal arrows are first order thickenings, with `𝒢_j = Ker(i_j^♯)`, a
> `g`-map `ν : 𝒢₁ ⟶ 𝒢₂`, and front and back solutions of **Stacks 08U7** making the diagram of
> ideal rows of **Stacks 08UA** commute (`D : DeformationIdealDiagram`):
>
> 1. the canonical element `D.obstructionClass` of `Ext¹_{𝒪_{X₂}}(Lg^*NL_{X₁/S₁}, 𝒢₂)` vanishes
>    if and only if there is a morphism of ringed spaces `X'₂ ⟶ X'₁` fitting into (08U9)
>    compatibly with `ν`;
> 2. if there is such a morphism, the set of all of them is a principal homogeneous space under
>    `Hom_{𝒪_{X₁}}(Ω_{X₁/S₁}, g_*𝒢₂)`: the action `liftAct` (given by the source's formula,
>    `liftAct_spec`) is trivial at `0`, additive, and simply transitive, and is the action of an
>    `AddTorsor` structure on the set.
>
> The other two spellings of the acting group in the source's display are identified with this
> one by `actingGroupPullbackAddEquiv` (`Hom_{𝒪_{X₂}}(g^*Ω_{X₁/S₁}, 𝒢₂)`) and
> `extZeroDerivedPullbackNaiveCotangentAddEquiv` (`Ext⁰_{𝒪_{X₂}}(Lg^*NL_{X₁/S₁}, 𝒢₂)`).

```lean
theorem lifting_obstruction_and_torsor :
    (D.obstructionClass = 0 ↔ Nonempty D.Lifts) ∧
      (∀ φ : D.Lifts, D.liftAct 0 φ = φ) ∧
      (∀ (φ : D.Lifts) (θ θ' : D.ActingGroup),
        D.liftAct θ' (D.liftAct θ φ) = D.liftAct (θ + θ') φ) ∧
      (∀ φ ψ : D.Lifts, ∃! θ : D.ActingGroup, D.liftAct θ φ = ψ) ∧
      (∀ _φ₀ : D.Lifts, ∃ T : AddTorsor D.ActingGroup D.Lifts,
        ∀ (θ : D.ActingGroup) (φ ψ : D.Lifts), T.vadd θ φ = ψ ↔ D.liftAct θ φ = ψ)
```

**`AlgebraicGeometry.RingedSpaceThickening.liftingObstruction_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentLiftingObstruction.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentLiftingObstruction.lean#L245). The attribute's comment: “clause (1): the class of Step 1 of the source's proof and its vanishing criterion, with the underlying spaces of the diagram identified as in the source's reduction, the two-term structure of NL(α) supplied as the distinguished triangle of `NaiveCotangentTwoTerm`, and the content of Steps 1 to 3 — the bijection between morphisms X'₂ ⟶ X'₁ fitting into the diagram and factorizations of the difference map through the degree 0 term — carried as the hypothesis `e`”.

> **Stacks Project, Tag 08U8**, clause (1). In the situation of the source's diagram, reduced
> as in its proof to sheaves of rings on one space, the class in `Ext¹(NL(α), 𝒢₂)` of the
> difference homomorphism `ξ` of Step 1 vanishes if and only if there is a morphism
> `X'₂ ⟶ X'₁` fitting into the diagram compatibly with `ν`.

```lean
theorem liftingObstruction_eq_zero_iff (P : NaiveCotangentTwoTerm single) (G : M)
    (ξ : P.conormal ⟶ G) {Lift : Type*} (e : Lift ≃ {θ : P.base ⟶ G // P.d ≫ θ = ξ}) :
    liftingObstruction P G ξ = 0 ↔ Nonempty Lift
```

**`AlgebraicGeometry.RingedSpaceThickening.liftTranslate_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentLiftingObstruction.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentLiftingObstruction.lean#L290). The attribute's comment: “clause (2): triviality of the action of 0 in the principal homogeneous space structure under Hom(H⁰(NL(α)), 𝒢₂)”.

> **Stacks Project, Tag 08U8**, clause (2). The zero homomorphism acts trivially on the
> morphisms `X'₂ ⟶ X'₁` fitting into the source's diagram.

```lean
theorem liftTranslate_zero (p : Lift) : liftTranslate P G ξ e 0 p = p
```

**`AlgebraicGeometry.RingedSpaceThickening.liftTranslate_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentLiftingObstruction.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentLiftingObstruction.lean#L297). The attribute's comment: “clause (2): additivity of the action in the principal homogeneous space structure under Hom(H⁰(NL(α)), 𝒢₂)”.

> **Stacks Project, Tag 08U8**, clause (2). Translation of the morphisms `X'₂ ⟶ X'₁` fitting
> into the source's diagram is additive in the translating homomorphism.

```lean
theorem liftTranslate_add (a b : cokernel P.d ⟶ G) (p : Lift) :
    liftTranslate P G ξ e a (liftTranslate P G ξ e b p) = liftTranslate P G ξ e (a + b) p
```

**`AlgebraicGeometry.RingedSpaceThickening.existsUnique_liftTranslate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentLiftingObstruction.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentLiftingObstruction.lean#L311). The attribute's comment: “clause (2): the morphisms X'₂ ⟶ X'₁ fitting into the diagram are a principal homogeneous space under Hom(H⁰(NL(α)), 𝒢₂), the acting group being written as the Hom out of the cokernel of the differential of NL(α); its further identification with Hom(g^*Ω\_\{X₁/S₁}, 𝒢₂) and with Ext⁰(Lg^*NL\_\{X₁/S₁}, 𝒢₂) is not proved here”.

> **Stacks Project, Tag 08U8**, clause (2). The morphisms `X'₂ ⟶ X'₁` fitting into the
> source's diagram compatibly with `ν` form a principal homogeneous space under
> `Hom(H⁰(NL(α)), 𝒢₂) = Hom(Ω_{X₁/S₁}, 𝒢₂)`: any one of them is carried to any other by exactly
> one homomorphism.

```lean
theorem existsUnique_liftTranslate (p q : Lift) :
    ∃! a : cokernel P.d ⟶ G, liftTranslate P G ξ e a p = q
```

## Tag 08U9, an equation

[Tag 08U9](https://stacks.math.columbia.edu/tag/08U9) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.DeformationCube`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DeformationDiagram.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DeformationDiagram.lean#L110). The attribute's comment: “the displayed commutative diagram of ringed spaces”.

> The commutative diagram of morphisms of ringed spaces
> comparing two deformation situations: a square `i₂ : X₂ ⟶ X₂'` over `t₂ : S₂ ⟶ S₂'` at the
> back, a square `i₁ : X₁ ⟶ X₁'` over `t₁ : S₁ ⟶ S₁'` at the front, and comparison morphisms
> `g : X₂ ⟶ X₁`, `h : S₂ ⟶ S₁`, `h' : S₂' ⟶ S₁'` making the four closed faces commute. There
> is no comparison `X₂' ⟶ X₁'`.

```lean
structure DeformationCube
```

## Tag 08UA, an equation

[Tag 08UA](https://stacks.math.columbia.edu/tag/08UA) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.DeformationIdealDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DeformationDiagram.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DeformationDiagram.lean#L216). The attribute's comment: “the displayed commutative diagram of the four ideal rows”.

> The commutative diagram of the four short exact ideal rows attached to a deformation cube
> whose horizontal arrows are first order thickenings: modules `𝒢₁`, `𝒢₂` identifying the ideals
> of `i₁` and `i₂`, prescribed maps `c₁`, `c₂` making front and back solutions of the deformation
> problem, and a `g`-map `ν : 𝒢₁ ⟶ 𝒢₂` compatible with the
> comparison `DeformationCube.baseIdealMap` of the ideals of `t₁` and `t₂`.

```lean
structure DeformationIdealDiagram
```

## Tag 08UB, a lemma

[Tag 08UB](https://stacks.math.columbia.edu/tag/08UB) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.exists_conormalRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentConormalRepresentation.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentConormalRepresentation.lean#L197). The attribute's comment: “over a ringed space, in the two-term idiom of NaiveCotangentTwoTerm: the class of a conormal homomorphism of a family of generators produced with it, transported to 𝖭𝖫\_\{X/S}”.

> **Stacks Project, Tag 08UB.** Every class of `Ext¹_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢)` is the class of a
> homomorphism `δ : 𝒥/𝒥² ⟶ 𝒢` out of the conormal sheaf of a suitable family of generators
> `α : ℰ ⟶ 𝒪_X` of `𝒪_X` over `f⁻¹𝒪_S`, transported to `𝖭𝖫_{X/S}` through the quasi-isomorphism
> of **Stacks 08TL**.
>
> The family of generators comes with the class and is not a refinement of a prescribed one; that
> is all the source gives, and it is all that is needed where the acting group of the torsor of
> **Stacks 08UC** is the presentation-free `Ext¹_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢)`.

```lean
theorem exists_conormalRepresentative (ξ : relativeObj f ⟶ shiftedSingleObj G) :
    ∃ (E : Functor (Opens X.carrier)ᵒᵖ (Type u))
      (α : E ⟶ underlyingPresheaf (Opens.grothendieckTopology X.carrier) X.sheaf)
      (hsurj : Presheaf.IsLocallySurjective (Opens.grothendieckTopology X.carrier)
        (generatorsPresentation f E α).hom),
      letI : Presheaf.IsLocallySurjective (Opens.grothendieckTopology X.carrier)
        (generatorsPresentation f E α).hom := hsurj
      ∃ δ : (twoTerm f E α).conormal ⟶ G,
        (naiveCotangentIso f E α).inv ≫ (twoTerm f E α).conormalExtClass G δ = ξ
```

**`Stacks.SheafOfModules.ConormalRepresentative.exists_enlargement_conormalExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExtClassRepresentation.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/NaiveCotangentExtClassRepresentation.lean#L44). The attribute's comment: “on the site of open sets of a topological space, the setting of the statement; the family of generators and the homomorphism are produced by the proof”.

> **Stacks Project, Tag 08UB.** Let `𝒜 ⟶ ℬ` be a homomorphism of sheaves of commutative
> rings on a topological space, let `𝒢` be a `ℬ`-module and let `ξ` be a first Ext class of
> `NL_{ℬ/𝒜}` with values in `𝒢`. There is a family of generators `α : ℰ ⟶ ℬ` presenting `ℬ` over
> `𝒜` for which `ξ`, restricted along the canonical comparison map `NL(α) ⟶ NL_{ℬ/𝒜}`, is the
> class of a homomorphism `ℐ/ℐ² ⟶ 𝒢` out of the conormal sheaf.

```lean
theorem exists_enlargement_conormalExtClass
    [HasWeakSheafify (Opens.grothendieckTopology X) CommRingCat.{max w u}]
    [(Opens.grothendieckTopology X).HasSheafCompose
      (forget₂ CommRingCat.{max w u} RingCat.{max w u})]
    (A B : Sheaf (Opens.grothendieckTopology X) CommRingCat.{max w u}) (a : A ⟶ B)
    [HasSheafify (Opens.grothendieckTopology X) AddCommGrpCat.{max w u}]
    [(Opens.grothendieckTopology X).WEqualsLocallyBijective AddCommGrpCat.{max w u}]
    [HasDerivedCategory.{w} (SheafOfModules.{max w u} (Stacks.SheafOfModules.Tensor.ringSheaf B))]
    (G : SheafOfModules.{max w u} (Stacks.SheafOfModules.Tensor.ringSheaf B))
    (ξ : DerivedCategory.Ext (DerivedCategory.Q.obj
        (Stacks.SheafOfModules.naiveCotangentComplex.{u, u, max w u, w}
          (Opens.grothendieckTopology X) A B a))
      ((DerivedCategory.singleFunctor _ 0).obj G) 1) :
    ∃ (E : Sheaf (Opens.grothendieckTopology X) (Type (max w u)))
      (α : E.obj ⟶ underlyingPresheaf (Opens.grothendieckTopology X) B)
      (hsurj : Presheaf.IsLocallySurjective (Opens.grothendieckTopology X)
        (Stacks.SheafOfModules.presentation (Opens.grothendieckTopology X) A B a E.obj α).hom),
      letI : Presheaf.IsLocallySurjective (Opens.grothendieckTopology X)
        (Stacks.SheafOfModules.presentation (Opens.grothendieckTopology X) A B a E.obj α).hom :=
        hsurj
      ∃ f : (Stacks.SheafOfModules.presentationConormalSequence.{u, u, max w u, w}
          (Opens.grothendieckTopology X) A B a E.obj α).X₁ ⟶ G,
        DerivedCategory.Q.map
            (Stacks.SheafOfModules.naiveCotangentComplexComparison.{u, u, max w u, w}
              (Opens.grothendieckTopology X) A B a E.obj α) ≫ ξ =
          Stacks.SheafOfModules.presentationConormalExtClass.{u, u, w, w}
            (Opens.grothendieckTopology X) A B a E.obj α G f
```

## Tag 08UC, a lemma

[Tag 08UC](https://stacks.math.columbia.edu/tag/08UC) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.exists_addTorsor_solutionClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/SolutionClassesPrincipalHomogeneous.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/SolutionClassesPrincipalHomogeneous.lean#L171). The attribute's comment: “at any model of D(𝒪\_X), with the canonical Ext¹(NL\_\{X/S}, 𝒢); the separating element of two classes is their difference class and ξ acts on [X'] by [X'\_ξ]”.

> **Stacks Project, Tag 08UC.** If there exists a solution to the deformation problem
> (91.7.0.1) of **Stacks 08U7**, then the set of isomorphism classes of solutions is principal
> homogeneous under `Ext¹_{𝒪_X}(NL_{X/S}, 𝒢)`.
>
> The statement holds at every model `H` of the derived category `D(𝒪_X)`, with the canonical group
> `Stacks.SheafOfModules.naiveCotangentExt` of the homomorphism `f⁻¹𝒪_S ⟶ 𝒪_X` in degree one. The
> set of isomorphism classes is `SolutionClasses t ht f G c`, the quotient of the solutions by
> `Isomorphic` (some morphism of solutions — a morphism of the deformed spaces under `X`, over
> `S'`, and the identity on `𝒢` — is an isomorphism). "Principal homogeneous" is Mathlib's
> `AddTorsor`: an action of the group which is free and transitive, the unique element carrying
> one class to another being `-ᵥ`. The structure is not an arbitrary one: the element separating
> the classes of `X'₁` and `X'₂` is the difference class `o(X'₁, X'₂)` of the two solutions (the
> class of the square-zero extension of `f⁻¹𝒪_S`-algebras which is their difference, read in the
> model `H`), and `ξ` acts on the class of `X'` by the class of the solution `X'_ξ` of the
> source's proof.

```lean
theorem exists_addTorsor_solutionClasses (h : Nonempty (DeformationSolution t ht f G c)) :
    ∃ T : AddTorsor (modelExtOneNaiveCotangent H f G) (SolutionClasses t ht f G c),
      letI := T
      (∀ Q₁ Q₂ : DeformationSolution t ht f G c,
        ((⟦Q₁⟧ : SolutionClasses t ht f G c) -ᵥ ⟦Q₂⟧) =
          extOneNaiveCotangentModelAddEquiv f G (differenceClass Q₁ Q₂)) ∧
      ∀ (ξ : modelExtOneNaiveCotangent H f G) (Q : DeformationSolution t ht f G c),
        ξ +ᵥ (⟦Q⟧ : SolutionClasses t ht f G c) =
          ⟦solutionTwist Q ((extOneNaiveCotangentModelAddEquiv f G).symm ξ)⟧
```

**`AlgebraicGeometry.RingedSpaceThickening.isomorphic_iff_nonempty_solutionHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/SolutionIsomorphism.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/SolutionIsomorphism.lean#L405). The attribute's comment: “the step of the proof that the obstruction to a morphism of solutions is the obstruction to an isomorphism; the full statement is exists\_addTorsor\_solutionClasses”.

> **Stacks Project, Tag 08UC**, the half asserting that the obstruction separates isomorphism
> classes. Two solutions of the deformation problem of Tag 08U7 are isomorphic exactly when there
> is a morphism of solutions between them: by `SolutionHom.isIso_hom` every morphism of solutions
> is already invertible. This is the source's "clearly, this element is the obstruction to the
> existence of an isomorphism, hence separates the isomorphism classes" — the obstruction class of
> Tag 08U8, which obstructs a *morphism* of solutions, thereby obstructs an isomorphism.
>
> The other half of the tag — that the isomorphism classes form a principal homogeneous space
> under `Ext¹_{𝒪_X}(NL_{X/S}, 𝒢)` — is not claimed here; the full statement of the tag is
> `exists_addTorsor_solutionClasses` in
> `StacksFrontier/Deformation/RingedSpaceThickening/SolutionClassesPrincipalHomogeneous.lean`.

```lean
theorem isomorphic_iff_nonempty_solutionHom (Q₁ Q₂ : DeformationSolution t ht f G c) :
    Isomorphic Q₁ Q₂ ↔ Nonempty (SolutionHom Q₁ Q₂)
```

## Tag 0GPZ, a lemma

[Tag 0GPZ](https://stacks.math.columbia.edu/tag/0GPZ) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.SquareZeroAlgebraExtension.isomorphismClassesEquivExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroAlgebraExtensionClassification.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroAlgebraExtensionClassification.lean#L340).

> Let `f : (X, 𝒪_X) ⟶ (S, 𝒪_S)` be a morphism of ringed spaces and `𝒢` an `𝒪_X`-module. The set
> of isomorphism classes of extensions `0 ⟶ 𝒢 ⟶ 𝒪_{X'} ⟶ 𝒪_X ⟶ 0` of `f⁻¹𝒪_S`-algebras with `𝒢` an
> ideal of square zero is canonically bijective to `Ext¹_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢)`.
>
> The bijection is the class map of **Stacks 0GQ0**: an extension goes to the class of the
> homomorphism `𝒥/𝒥² ⟶ 𝒢` of the presentation of `𝒪_X` by the sheaf of sets underlying
> `𝒪_{X'}`, read through the quasi-isomorphism of **Stacks 08TL**
> (`isomorphismClassesEquivExt_apply`).

```lean
def isomorphismClassesEquivExt : IsomorphismClasses f G ≃ extOneNaiveCotangent f G
```

**`AlgebraicGeometry.RingedSpaceThickening.trivialSolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroExtensionClasses.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroExtensionClasses.lean#L172). The attribute's comment: “the existence of a solution: the trivial extension 𝒪\_X ⋉ 𝒢; not the bijection with Ext¹, which needs the torsor statement of 08UC”.

> **The trivial square-zero extension is a solution of the problem of Stacks 08U7** over the
> identity thickening of the base: `X' = (X, 𝒪_X ⋉ 𝒢)` is a first order thickening of `X` over
> `S` whose ideal is `𝒢`. This is the base point the torsor of **Stacks 08UC** needs.

```lean
def trivialSolution (ht : IsFirstOrderThickening (𝟙 S)) (f : X ⟶ S)
    (G : SheafOfModules.{u} (structureSheafRing X)) :
    DeformationSolution (𝟙 S) ht f G 0
```

**`AlgebraicGeometry.RingedSpaceThickening.nonempty_deformationSolution`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroExtensionClasses.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroExtensionClasses.lean#L192). The attribute's comment: “the existence of a solution, which is what the torsor of 08UC requires of the type of solutions; not the bijection with Ext¹”.

> **The deformation problem of Stacks 08U7 over the identity thickening of the base has a
> solution**, namely the trivial square-zero extension. This is the source's "there exists a
> solution", i.e. what `[Nonempty Sol]` asks of `SolutionObstruction.addTorsor`.

```lean
instance nonempty_deformationSolution {ht : IsFirstOrderThickening (𝟙 S)} {f : X ⟶ S}
    {G : SheafOfModules.{u} (structureSheafRing X)} :
    Nonempty (DeformationSolution (𝟙 S) ht f G 0)
```

**`AlgebraicGeometry.RingedSpaceThickening.classesEquivExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroExtensionClasses.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroExtensionClasses.lean#L232). The attribute's comment: “the bijection, subject to four conditions on the type of solutions that remain inputs — the fields of SolutionObstruction: the difference cocycle xi of two solutions, its additivity hxi, the pushout construction realizing every class as a difference, and the representation rep of every class by a conormal homomorphism (08UB, whose change of presentation is 08TL). The two-term complex P is arbitrary, so the acting group is the Ext¹ of P — for P the complex of a fixed presentation α, that of α rather than Ext¹(NL\_\{X/S}, 𝒢), whose identification is 08TL”.

> **Stacks Project, Tag 0GPZ.** The isomorphism classes of square-zero extensions
> `0 ⟶ 𝒢 ⟶ 𝒪_{X'} ⟶ 𝒪_X ⟶ 0` of `f⁻¹𝒪_S`-algebras — equivalently, of first order thickenings
> `i : X ⟶ X'` over `S` with `Ker(i^♯) ≅ 𝒢`, i.e. of solutions of the problem of **Stacks 08U7**
> over the identity thickening of the base — are in bijection with `Ext¹(NL(α), 𝒢)`.
>
> The bijection is the torsor of **Stacks 08UC** evaluated at the base point supplied by the
> trivial extension `𝒪_X ⋉ 𝒢`: a class `q` goes to the obstruction class separating it from the
> class of `𝒪_X ⋉ 𝒢`, and a class `ξ` of `Ext¹` goes to the class of the solution obtained from
> `𝒪_X ⋉ 𝒢` by twisting with `ξ`. The four fields of `SolutionObstruction` remain inputs; see
> the implementation notes of this file and of
> `StacksFrontier/Deformation/RingedSpaceThickening/SolutionTorsor.lean`.

```lean
def classesEquivExt (P : NaiveCotangentTwoTerm single)
    (xi : DeformationSolution (𝟙 S) ht f G 0 → DeformationSolution (𝟙 S) ht f G 0 →
      (P.conormal ⟶ G))
    (hxi : ∀ Q₁ Q₂ Q₃ : DeformationSolution (𝟙 S) ht f G 0, xi Q₁ Q₂ + xi Q₂ Q₃ = xi Q₁ Q₃)
    (rep : ∀ ξ : P.obj ⟶ (single.obj G)⟦(1 : ℤ)⟧,
      { δ : P.conormal ⟶ G // liftingObstruction P G δ = ξ })
    (pushout : ∀ (Q : DeformationSolution (𝟙 S) ht f G 0) (δ : P.conormal ⟶ G),
      { Q' : DeformationSolution (𝟙 S) ht f G 0 // xi Q Q' = δ }) :
    (liftingObstructionSolution P G xi hxi rep pushout).IsomorphismClasses ≃
      (P.obj ⟶ (single.obj G)⟦(1 : ℤ)⟧)
```

**`AlgebraicGeometry.RingedSpaceThickening.classesEquivExtRelative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroExtensionClassesRelative.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/SquareZeroExtensionClassesRelative.lean#L102). The attribute's comment: “the bijection, unconditional, with the acting group of the tag: Ext¹(𝖭𝖫\_\{X/S}, 𝒢) itself. The set counted is the classes of square-zero extensions of f⁻¹𝒪\_S-algebras under equality of their class in that group; a morphism of extensions forces that equality by extClass\_eq\_extClass\_of\_hom, and that the converse holds too — so that the relation is isomorphism of extensions — is clause (1) of 08U8, a separate tag, not reproved here”.

> **Stacks Project, Tag 0GPZ.** The classes of square-zero extensions
> `0 ⟶ 𝒢 ⟶ 𝒪_{X'} ⟶ 𝒪_X ⟶ 0` of `f⁻¹𝒪_S`-algebras are in bijection with
> `Ext¹_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢)`, by sending an extension to its class.
>
> Both halves are proved. Injectivity is by construction: the classes are the quotient of the
> type of extensions by equality of their class in `Ext¹_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢)`, a relation which a
> morphism of extensions forces by
> `AlgebraicGeometry.RingedSpaceThickening.extClassDiff_eq_zero_of_hom` and which is read as the
> vanishing of an obstruction class over a common refinement by
> `...extClassDiff_eq_zero_iff_pairRefinement`. Surjectivity is
> `...exists_extension_extClass_eq`: the square-zero pushout of a presentation along a conormal
> homomorphism representing the class, which exists by **Stacks 08UB**.
>
> The acting group is the group of the tag, and the bijection is the one of the torsor
> `addTorsorExtensionClasses` read at a base point.

```lean
def classesEquivExtRelative :
    ExtensionClasses (realizeExtClassDiff (f := f) (G := G)) ≃
      (PresentedSquareZeroExtension.relativeObj f ⟶
        PresentedSquareZeroExtension.shiftedSingleObj G)
```

**`Stacks.Deformation.TrivialSqZero.isFirstOrderThickening_thickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialSquareZeroThickening.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialSquareZeroThickening.lean#L165). The attribute's comment: “the solution 𝒢 ⊕ 𝒪\_X of the proof: it is a first order thickening of X; not the bijection with Ext¹, which needs the torsor statement of 08UC”.

> **`i : X ⟶ X'` is a first order thickening**: the square of the kernel ideal of `i^♯`
> over an open is generated by products of sections killed by `i^♯`, all of which vanish.

```lean
theorem isFirstOrderThickening_thickening : IsFirstOrderThickening (thickening X G)
```

**`Stacks.Deformation.TrivialSqZero.idealSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialSquareZeroThickening.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialSquareZeroThickening.lean#L371). The attribute's comment: “the solution 𝒢 ⊕ 𝒪\_X of the proof: the identification of 𝒢 with Ker(i^♯); not the bijection with Ext¹, which needs the torsor statement of 08UC”.

> **The ideal of the trivial square-zero thickening is `𝒢`**: the canonical isomorphism
> `Ker(i^♯) ≅ i_* 𝒢` of `𝒪_{X'}`-modules coming from the kernel property of the inclusion.

```lean
def idealSheafIso :
    AlgebraicGeometry.SheafOfModules.idealSheaf (thickening X G) ≅
      (modulePushforward (thickening X G)).obj G
```

**`Stacks.Deformation.TrivialSqZero.thickening_comp_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialSquareZeroThickening.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialSquareZeroThickening.lean#L395). The attribute's comment: “the solution 𝒢 ⊕ 𝒪\_X of the proof: the thickening is a thickening over S; not the bijection with Ext¹, which needs the torsor statement of 08UC”.

> `i : X ⟶ X'` is a morphism over `S`.

```lean
theorem thickening_comp_over (f : X ⟶ S) : thickening X G ≫ over (G := G) f = f
```

## Tag 0GQ0, a remark

[Tag 0GQ0](https://stacks.math.columbia.edu/tag/0GQ0) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.AlgebraSquareZeroExtension.lift_comp_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentation.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentation.lean#L351). The attribute's comment: “the commutative diagram over 𝒪\_\{X'} ⟶ 𝒪\_X for the choice of sheaf of sets ℰ that the source gives, namely the one underlying 𝒪\_\{X'} with α' the identity”.

> The map determined by `α'` followed by the reduction `𝒪_{X'} ⟶ 𝒪_X` is the presentation
> attached to `α`.

```lean
theorem lift_comp_reduction : P.lift ≫ P.reduction = P.presentation
```

**`AlgebraicGeometry.RingedSpaceThickening.AlgebraSquareZeroExtension.presentation_isLocallySurjective`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentation.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentation.lean#L356). The attribute's comment: “surjectivity of f⁻¹𝒪\_S[ℰ] ⟶ 𝒪\_X, which is what makes 𝖭𝖫(α) defined”.

> The presentation `f⁻¹𝒪_S[ℰ] ⟶ 𝒪_X` is surjective.

```lean
instance presentation_isLocallySurjective :
    Presheaf.IsLocallySurjective (Opens.grothendieckTopology X.carrier) P.presentation.hom
```

**`AlgebraicGeometry.RingedSpaceThickening.AlgebraSquareZeroExtension.conormalToIdeal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentation.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentation.lean#L377). The attribute's comment: “the map 𝒥/𝒥² ⟶ 𝒢 determined by α'; not the resulting element of Ext¹\_\{𝒪\_X}(𝖭𝖫(α), 𝒢), whose agreement with the class of 𝒪\_\{X'} under the bijection of 0GPZ is not proved here”.

> The map `𝒥/𝒥² ⟶ 𝒢` determined by `α'`.

```lean
abbrev conormalToIdeal :
    conormalSheaf.{u, u, u, u} (Opens.grothendieckTopology X.carrier)
      (freeAlgebraSheaf (Opens.grothendieckTopology X.carrier) (inverseImageBaseRing f)
        P.generators) X.sheaf P.presentation ⟶ G
```

**`AlgebraicGeometry.RingedSpaceThickening.AlgebraSquareZeroExtension.naiveCotangentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentation.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentation.lean#L405). The attribute's comment: “the identification 𝖭𝖫\_\{X/S} ≅ 𝖭𝖫(α) in D(𝒪\_X) for the chosen ℰ, by 08TL”.

> The identification `𝖭𝖫(α) ≅ 𝖭𝖫_{X/S}` in `D(𝒪_X)` given by the canonical comparison map.

```lean
def naiveCotangentIso :
    DerivedCategory.Q.obj P.naiveCotangentComplex ≅
      DerivedCategory.Q.obj (Stacks.SheafOfModules.naiveCotangentComplex.{u, u, u, u}
        (Opens.grothendieckTopology X.carrier) (inverseImageBaseRing f) X.sheaf
        (structureRingMap f))
```

**`AlgebraicGeometry.RingedSpaceThickening.SquareZeroAlgebraExtension.isomorphismClassesEquivExt_mk_eq_presented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentationRemark.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPresentationRemark.lean#L108).

> **Stacks Project, Tag 0GQ0.** Let `0 ⟶ 𝒢 ⟶ 𝒪_{X'} ⟶ 𝒪_X ⟶ 0` be an extension of
> `f⁻¹𝒪_S`-algebras with `𝒢` an ideal of square zero, and let `ℰ` be any (pre)sheaf of sets with a
> commutative diagram `α' : ℰ ⟶ 𝒪_{X'}`, `α : ℰ ⟶ 𝒪_X` over the reduction (`hα`) such that
> `f⁻¹𝒪_S[ℰ] ⟶ 𝒪_X` is surjective, with kernel `𝒥`. The map `f⁻¹𝒪_S[ℰ] ⟶ 𝒪_{X'}` determined by
> `α'` induces `𝒥/𝒥² ⟶ 𝒢` (`conormalToIdeal`); its class in `Ext¹_{𝒪_X}(𝖭𝖫(α), 𝒢)`
> (`conormalExtClass` on `𝖭𝖫(α) = (𝒥/𝒥² ⟶ Ω ⊗ 𝒪_X)`), carried to `Ext¹_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢)` along
> the identification `𝖭𝖫(α) ≅ 𝖭𝖫_{X/S}` of **Stacks 08TL** (`naiveCotangentIso`), is the element
> the canonical bijection of **Stacks 0GPZ** attaches to the class of `𝒪_{X'}`.

```lean
theorem isomorphismClassesEquivExt_mk_eq_presented (P : SquareZeroAlgebraExtension f G)
    (E : Functor (Opens X.carrier)ᵒᵖ (Type u))
    (α : E ⟶ underlyingPresheaf (Opens.grothendieckTopology X.carrier) X.sheaf)
    (α' : E ⟶ underlyingPresheaf (Opens.grothendieckTopology X.carrier) P.sheaf)
    (hα : α' ≫ P.generatorsMap = α)
    [Presheaf.IsLocallySurjective (Opens.grothendieckTopology X.carrier)
      (generatorsPresentation f E α).hom] :
    (PresentedSquareZeroExtension.naiveCotangentIso f E α).inv ≫
        (PresentedSquareZeroExtension.twoTerm f E α).conormalExtClass G
          (P.withGenerators E α α' hα).conormalToIdeal =
      isomorphismClassesEquivExt f G ⟦P⟧
```

## Tag 0GQ1, a lemma

[Tag 0GQ1](https://stacks.math.columbia.edu/tag/0GQ1) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.nonempty_compatibleMorphism_iff_pullbackExtClass_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/CompatibleMorphismExtClass.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/CompatibleMorphismExtClass.lean#L363).

> **Stacks Project, Tag 0GQ1.** Let `f : (X, 𝒪_X) ⟶ (S, 𝒪_S)` and `g : (Y, 𝒪_Y) ⟶ (X, 𝒪_X)` be
> morphisms of ringed spaces, `ℱ` an `𝒪_X`-module, `𝒢` an `𝒪_Y`-module and `c : ℱ ⟶ g_*𝒢` a
> `g`-map. Let `P : 0 ⟶ ℱ ⟶ 𝒪_{X'} ⟶ 𝒪_X ⟶ 0` be an extension of `f⁻¹𝒪_S`-algebras corresponding to
> `ξ ∈ Ext¹_{𝒪_X}(𝖭𝖫_{X/S}, ℱ)` and `Q : 0 ⟶ 𝒢 ⟶ 𝒪_{Y'} ⟶ 𝒪_Y ⟶ 0` an extension of
> `g⁻¹f⁻¹𝒪_S`-algebras corresponding to `ζ ∈ Ext¹_{𝒪_Y}(𝖭𝖫_{Y/S}, 𝒢)` under the bijections of
> Stacks 0GPZ. Then there is an `S`-morphism `g' : Y' ⟶ X'` compatible with `g` and `c` if and
> only if `ξ` and `ζ` map to the same element of `Ext¹_{𝒪_Y}(Lg^*𝖭𝖫_{X/S}, 𝒢)`: `ξ` through `Lg^*`
> and the coefficient map `Lg^*ℱ ⟶ g^*ℱ ⟶ 𝒢` (the last map the adjoint of `c`), and `ζ` through
> the canonical map `Lg^*𝖭𝖫_{X/S} ⟶ 𝖭𝖫_{Y/S}`.

```lean
theorem nonempty_compatibleMorphism_iff_pullbackExtClass_eq (P : SquareZeroAlgebraExtension f F)
    (Q : SquareZeroAlgebraExtension (g ≫ f) G) (c : F ⟶ (modulePushforward g).obj G) :
    Nonempty (CompatibleMorphism P Q c) ↔
      pullbackExtClass g f (((modulePullbackPushforwardAdjunction g).homEquiv _ _).symm c)
          (isomorphismClassesEquivExt f F (Quotient.mk _ P)) =
        restrictDerivedExtClass (derivedPullbackNaiveCotangentMap g f)
          (isomorphismClassesEquivExt (g ≫ f) G (Quotient.mk _ Q))
```

**`AlgebraicGeometry.RingedSpaceThickening.exists_compatibleLift_iff_eq_pullbackExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DerivedExtensionClassCriterion.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DerivedExtensionClassCriterion.lean#L92). The attribute's comment: “the criterion for the DERIVED pullback Lf^*𝖭𝖫\_\{S/S'} of the source's statement, with the image of ξ the constructed map pullbackExtClass. Carried, exactly as in the degreewise form: the two-term structure P with hP, the bijection e of Steps 1 to 3 of 08U8, and hcompat, the 0GPZ/08U8 compatibility whose statement and proof the source omits”.

> For the derived pullback `Lf^*𝖭𝖫_{S/S'}`: a lift compatible with `f` and the prescribed map `c`
> exists if and only if the class of the extension `𝒪_{X'}`, restricted along a comparison
> `q : Lf^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'}`, agrees with the image `pullbackExtClass f t c xi` of
> `ξ ∈ Ext¹_{𝒪_S}(𝖭𝖫_{S/S'}, 𝒥)` in `Ext¹_{𝒪_X}(Lf^*𝖭𝖫_{S/S'}, 𝒢)`.  The compatible lifts are the
> type `Lift`, identified by `e` with the factorizations of the difference homomorphism `δ` through
> the degree `0` term, and `hcompat` says that the difference of the two classes is the
> obstruction class.

```lean
theorem exists_compatibleLift_iff_eq_pullbackExtClass {f : X ⟶ S} {t : S ⟶ S'}
    {J : SheafOfModules.{u} (structureSheafRing S)} {G : SheafOfModules.{u} (structureSheafRing X)}
    (c : (modulePullback f).obj J ⟶ G)
    (q : derivedPullbackNaiveCotangent f t ⟶ relativeNaiveCotangentObj (f ≫ t))
    (P : NaiveCotangentTwoTerm
      (DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0))
    (hP : P.obj = derivedPullbackNaiveCotangent f t)
    (δ : P.conormal ⟶ G) {Lift : Type*}
    (e : Lift ≃ {θ : P.base ⟶ G // P.d ≫ θ = δ})
    (xi : extOneNaiveCotangent t J) (ζ : extOneNaiveCotangent (f ≫ t) G)
    (hcompat : eqToHom hP ≫ (pullbackExtClass f t c xi - restrictDerivedExtClass q ζ) =
      P.conormalExtClass G δ) :
    Nonempty Lift ↔ pullbackExtClass f t c xi = restrictDerivedExtClass q ζ
```

**`AlgebraicGeometry.RingedSpaceThickening.isSolutionClass_iff_eq_pullbackExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DerivedExtensionClassCriterion.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DerivedExtensionClassCriterion.lean#L141). The attribute's comment: “the criterion for the DERIVED pullback, read on isomorphism classes of extensions: this is the hcrit hypothesis of solutionsEquivExtFibre, proved rather than assumed. Carried are the two-term structure P with hP, the per-class bijections e of Steps 1 to 3 of 08U8, the per-class 0GPZ/08U8 compatibilities, and the 0GPZ bijection E”.

> Read on isomorphism classes: a class of square-zero extensions of `f^{-1}𝒪_{S'}`-algebras is
> a class of solutions of **Stacks 08U7** exactly when its image under `E` restricts, along a
> comparison `q : Lf^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'}`, to the image of `ξ` in
> `Ext¹_{𝒪_X}(Lf^*𝖭𝖫_{S/S'}, 𝒢)`.  Here `P` with `hP` is a two-term structure of
> `Lf^*𝖭𝖫_{S/S'}`, `e` and `hcompat` are the per-class bijections and compatibilities of
> `exists_compatibleLift_iff_eq_pullbackExtClass`, and `E` is the bijection of **Stacks 0GPZ**.

```lean
theorem isSolutionClass_iff_eq_pullbackExtClass
    (E : Quotient r ≃ extOneNaiveCotangent (f ≫ t) G)
    (q : derivedPullbackNaiveCotangent f t ⟶ relativeNaiveCotangentObj (f ≫ t))
    (xi : extOneNaiveCotangent t (baseIdealOnReduction t))
    (P : NaiveCotangentTwoTerm
      (DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0))
    (hP : P.obj = derivedPullbackNaiveCotangent f t)
    (δ : Quotient r → (P.conormal ⟶ G))
    (e : ∀ p : Quotient r, SolutionInClass ht c r p ≃
      {θ : P.base ⟶ G // P.d ≫ θ = δ p})
    (hcompat : ∀ p : Quotient r, eqToHom hP ≫
      (pullbackExtClass f t c xi - restrictDerivedExtClass q (E p)) =
        P.conormalExtClass G (δ p))
    (p : Quotient r) :
    ExtensionOverBase.IsSolutionClass ht c r p ↔
      restrictDerivedExtClass q (E p) = pullbackExtClass f t c xi
```

**`AlgebraicGeometry.RingedSpaceThickening.pulledNaiveCotangentComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassComparison.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassComparison.lean#L76). The attribute's comment: “the canonical comparison g^*𝖭𝖫\_\{X/S} ⟶ 𝖭𝖫\_\{Y/S} along which ζ is read, for the degreewise pullback; the derived pullback Lg^*𝖭𝖫\_\{X/S} of the source's statement is not used”.

> The canonical comparison `g^*𝖭𝖫_{X/S} ⟶ 𝖭𝖫_{Y/S}`: the identification of `g^*𝖭𝖫_{X/S}` with the
> base change of `𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}`, followed by the canonical base-change map for
> `g⁻¹f⁻¹𝒪_S ⟶ g⁻¹𝒪_X ⟶ 𝒪_Y`.

```lean
def pulledNaiveCotangentComparison (g : Y ⟶ X) (f : X ⟶ S) :
    pulledNaiveCotangentComplex.{u} g f ⟶ relativeNaiveCotangentComplex g f
```

**`AlgebraicGeometry.RingedSpaceThickening.restrictExtClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassComparison.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassComparison.lean#L105). The attribute's comment: “the map Ext¹(𝖭𝖫\_\{Y/S}, 𝒢) ⟶ Ext¹(g^*𝖭𝖫\_\{X/S}, 𝒢) in which ζ is read, the second of the two maps the source's proof constructs; the first, which goes through the derived pullback of 06YJ and the g-map c, is not constructed here”.

> The map `Ext¹_{𝒪_Y}(𝖭𝖫_{Y/S}, 𝒢) ⟶ Ext¹_{𝒪_Y}(g^*𝖭𝖫_{X/S}, 𝒢)`: precomposition with the
> canonical comparison of the naive cotangent complexes.

```lean
def restrictExtClass (ζ : relativeExtGroup g f G) : pulledExtGroup g f G
```

**`AlgebraicGeometry.RingedSpaceThickening.exists_compatibleLift_iff_eq_restrictExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassComparison.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassComparison.lean#L124). The attribute's comment: “the equivalence, deduced from clause (1) of 08U8: the two Ext¹ classes agree exactly when a compatible S-morphism exists. The two-term structure of g^*𝖭𝖫\_\{X/S} is now constructed rather than assumed, by pulledNaiveCotangentTwoTerm. Two conditions remain inputs: (i) the bijection e between the compatible S-morphisms and the factorizations of the difference homomorphism — Steps 1 to 3 of 08U8, an input there too — and (ii) hcompat, the compatibility between the constructions in the proofs of 0GPZ and 08U8 whose statement and proof the source omits. The class read off from ξ is taken as its image in Ext¹(g^*𝖭𝖫\_\{X/S}, 𝒢); the first of the source's two maps is not constructed here”.

> An `S`-morphism `Y' ⟶ X'` compatible with `g` and the `g`-map `c` exists if and only if
> `ξ = restrictExtClass g f G ζ` in `Ext¹_{𝒪_Y}(g^*𝖭𝖫_{X/S}, 𝒢)`.
>
> Here `δ : g^*(𝒥/𝒥²) ⟶ 𝒢` is a homomorphism out of the conormal term of the two-term structure
> `AlgebraicGeometry.RingedSpaceThickening.pulledNaiveCotangentTwoTerm g f`. The theorem takes as
> hypotheses a bijection `e` between the type `Lift` of compatible morphisms and the factorizations
> of `δ` through the degree `0` term `g^*Ω`, and the identity `hcompat`: the difference
> `ξ - restrictExtClass g f G ζ` is the obstruction class of `δ`.

```lean
theorem exists_compatibleLift_iff_eq_restrictExtClass
    (δ : (pulledNaiveCotangentTwoTerm g f).conormal ⟶ G) {Lift : Type*}
    (e : Lift ≃ {θ : (pulledNaiveCotangentTwoTerm g f).base ⟶ G //
      (pulledNaiveCotangentTwoTerm g f).d ≫ θ = δ})
    (ξ : pulledExtGroup g f G) (ζ : relativeExtGroup g f G)
    (hcompat : ξ - restrictExtClass g f G ζ =
      (pulledNaiveCotangentTwoTerm g f).conormalExtClass G δ) :
    Nonempty Lift ↔ ξ = restrictExtClass g f G ζ
```

**`AlgebraicGeometry.RingedSpaceThickening.eq_restrictExtClass_iff_exists_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassComparisonUnconditional.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassComparisonUnconditional.lean#L149). The attribute's comment: “the equivalence with every input removed: the two Ext¹ classes agree exactly when their difference is the class of a homomorphism δ out of the conormal term of g^*𝖭𝖫\_\{X/S} which factors through the degree 0 term. The binders are g, f, 𝒢 and the two classes alone — there is no type of compatible morphisms, no bijection e and no compatibility hcompat — and this implies exists\_compatibleLift\_iff\_eq\_restrictExtClass of ExtensionClassComparison.lean for every choice of those four. The right hand side is the condition that Steps 1 to 3 of the proof of 08U8 identify with the existence of a compatible S-morphism Y' ⟶ X'; that identification is a separate result of the source, so the left hand side of the source's own equivalence is read here through it. The comparison group is the Ext¹ of the DEGREEWISE pullback g^*𝖭𝖫\_\{X/S} rather than of the derived pullback Lg^*𝖭𝖫\_\{X/S} of the source's statement, and ξ is a FREE ELEMENT of that group rather than the image of the class of the extension of 𝒪\_X: the first of the source's two maps, which would carry that class in, is absent here”.

> **Stacks Project, Tag 0GQ1**, with every input removed.  The two classes agree in
> `Ext¹_{𝒪_Y}(g^*𝖭𝖫_{X/S}, 𝒢)` if and only if their difference is the class of a homomorphism `δ`
> out of the conormal term of `g^*𝖭𝖫_{X/S}` which factors through the degree `0` term.
>
> The right hand side is the condition that Steps 1 to 3 of the proof of **Stacks 08U8** identify
> with the existence of a compatible `S`-morphism `Y' ⟶ X'`.  Compared with
> `exists_compatibleLift_iff_eq_restrictExtClass` the homomorphism `δ`, the type `Lift`, the
> bijection `e` and the compatibility `hcompat` are all gone: the only binders are `g`, `f`, `𝒢`
> and the two classes.  That statement follows from this one for every choice of them.

```lean
theorem eq_restrictExtClass_iff_exists_factorization
    (ξ : pulledExtGroup g f G) (ζ : relativeExtGroup g f G) :
    ξ = restrictExtClass g f G ζ ↔
      ∃ δ : (pulledNaiveCotangentTwoTerm g f).conormal ⟶ G,
        ξ - restrictExtClass g f G ζ =
            (pulledNaiveCotangentTwoTerm g f).conormalExtClass G δ ∧
          Nonempty { θ : (pulledNaiveCotangentTwoTerm g f).base ⟶ G //
            (pulledNaiveCotangentTwoTerm g f).d ≫ θ = δ }
```

## Tag 0GQ2, a remark

[Tag 0GQ2](https://stacks.math.columbia.edu/tag/0GQ2) in the Stacks Project.

**`Stacks.Deformation.InverseImageExtension.Data.pullbackExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageExtensionComparison.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageExtensionComparison.lean#L231). The attribute's comment: “the pullback extension 𝒪'₂ = 𝒪\_\{Y'} ×\_\{𝒪\_Y} g⁻¹𝒪\_X, with the second displayed diagram its projections. Carried: that g⁻¹𝒪\_\{X'} is an extension of g⁻¹𝒪\_X by g⁻¹ℱ, and that 𝒢 is the square-zero ideal of 𝒪\_\{Y'} with its 𝒪\_Y-action”.

> **Stacks 0GQ2**, the second construction: pulling the extension
> `0 ⟶ 𝒢 ⟶ 𝒪_{Y'} ⟶ 𝒪_Y ⟶ 0` back along `g^♯ : g^{-1}𝒪_X ⟶ 𝒪_Y` gives an extension
> `0 ⟶ 𝒢 ⟶ 𝒪'₂ ⟶ g^{-1}𝒪_X ⟶ 0` of `g^{-1}f^{-1}𝒪_S`-algebras, with
> `𝒪'₂ = 𝒪_{Y'} ×_{𝒪_Y} g^{-1}𝒪_X` the fibre product of sheaves of rings and the remark's second
> displayed diagram its two projections.

```lean
def pullbackExtension : AlgebraExtension S A (d.u ≫ d.π) d.N.val.presheaf
```

**`Stacks.Deformation.InverseImageExtension.Data.pushoutExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageExtensionComparison.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageExtensionComparison.lean#L325). The attribute's comment: “the pushout extension 𝒪'₁ of g⁻¹𝒪\_\{X'} along c, with the first displayed diagram its comparison with g⁻¹𝒪\_\{X'}. Carried: that g⁻¹𝒪\_\{X'} is an extension of g⁻¹𝒪\_X by g⁻¹ℱ, the ideal being Ker π”.

> **Stacks 0GQ2**, the first construction: pushing the extension
> `0 ⟶ g^{-1}ℱ ⟶ g^{-1}𝒪_{X'} ⟶ g^{-1}𝒪_X ⟶ 0` out along `c : g^{-1}ℱ ⟶ 𝒢` gives an extension
> `0 ⟶ 𝒢 ⟶ 𝒪'₁ ⟶ g^{-1}𝒪_X ⟶ 0` of `g^{-1}f^{-1}𝒪_S`-algebras, with the remark's first
> displayed diagram its comparison with `g^{-1}𝒪_{X'}`.

```lean
def pushoutExtension [K.WEqualsLocallyBijective CommRingCat.{u}] :
    AlgebraExtension S A (d.u ≫ d.π) d.N.val.presheaf
```

**`Stacks.Deformation.InverseImageExtension.Data.nonempty_compatibleHom_iff_isomorphic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageExtensionComparison.lean, line 661](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageExtensionComparison.lean#L661). The attribute's comment: “the diagram chase: a compatible S-morphism Y' → X' exists iff 𝒪'₁ ≅ 𝒪'₂ as g⁻¹f⁻¹𝒪\_S-algebra extensions of g⁻¹𝒪\_X by 𝒢. Carried: that g⁻¹𝒪\_\{X'} is an extension of g⁻¹𝒪\_X by g⁻¹ℱ, and that 𝒢 is the square-zero ideal of 𝒪\_\{Y'} with its 𝒪\_Y-action”.

> **Stacks 0GQ2**, the criterion.  An `S`-morphism `Y' → X'` compatible with `g` and `c`
> exists if and only if the pushout `𝒪'₁` and the pullback `𝒪'₂` are isomorphic as
> `g^{-1}f^{-1}𝒪_S`-algebra extensions of `g^{-1}𝒪_X` by `𝒢`.

```lean
theorem nonempty_compatibleHom_iff_isomorphic :
    Nonempty d.CompatibleHom ↔
      AlgebraExtension.Isomorphic d.pushoutExtension d.pullbackExtension
```

**`AlgebraicGeometry.RingedSpaceThickening.inverseImageNaiveCotangentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageNaiveCotangentIso.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageNaiveCotangentIso.lean#L592).

> The identification `g⁻¹𝖭𝖫_{X/S} = 𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}`: the canonical map
> `π^*𝖭𝖫_{X/S} ⟶ 𝖭𝖫_{g⁻¹𝒪_X/(g ∘ f)⁻¹𝒪_S}` of naive cotangent complexes, as an isomorphism of
> complexes of `g⁻¹𝒪_X`-modules.

```lean
def inverseImageNaiveCotangentIso :
    ((modulePullback (inverseImageProj g)).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (show CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ from
          PresentedSquareZeroExtension.relativeComplex f) ≅
      (show CochainComplex
            (SheafOfModules.{u} (structureSheafRing (inverseImageRingedSpace g))) ℤ from
          PresentedSquareZeroExtension.relativeComplex (inverseImageProj g ≫ f))
```

**`AlgebraicGeometry.RingedSpaceThickening.isomorphismClassesEquivExt_inverseImagePushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageNaiveCotangentIso.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageNaiveCotangentIso.lean#L635).

> The class, under the bijection of **Stacks 0GPZ** for the ringed space `(Y, g⁻¹𝒪_X)` over `S`,
> of the pushout `𝒪'₁` of `0 ⟶ g⁻¹ℱ ⟶ g⁻¹𝒪_{X'} ⟶ g⁻¹𝒪_X ⟶ 0` along `c : g⁻¹ℱ ⟶ 𝒢` is the image
> of the class `ξ` of `𝒪_{X'}` (under the bijection of **Stacks 0GPZ** for `X` over `S`): `g⁻¹ξ`
> pushed along `c^♭ : g⁻¹ℱ ⟶ 𝒢`, read in `Ext¹_{g⁻¹𝒪_X}(𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}, 𝒢)` through the
> identification `𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S} = g⁻¹𝖭𝖫_{X/S}` of **Stacks 08TM**.

```lean
theorem isomorphismClassesEquivExt_inverseImagePushout (P : SquareZeroAlgebraExtension f F)
    (c : F ⟶ (modulePushforward g).obj G) :
    SquareZeroAlgebraExtension.isomorphismClassesEquivExt (inverseImageSpaceHom f g)
        (restrictedModule g G) (Quotient.mk _ (inverseImagePushout G P c)) =
      inverseImageXiMap c
        (SquareZeroAlgebraExtension.isomorphismClassesEquivExt f F (Quotient.mk _ P))
```

**`AlgebraicGeometry.RingedSpaceThickening.isomorphismClassesEquivExt_inverseImagePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningClasses.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningClasses.lean#L431).

> **The class of `𝒪'₂`.** The class, under the bijection of **Stacks 0GPZ** for the ringed
> space `(Y, g⁻¹𝒪_X)` over `S`, of the pullback `𝒪'₂ = 𝒪_{Y'} ×_{𝒪_Y} g⁻¹𝒪_X` is the image of the
> class `ζ` of `𝒪_{Y'}` (under the bijection of **Stacks 0GPZ** for `Y` over `S`) by the canonical
> map `Ext¹_{𝒪_Y}(𝖭𝖫_{Y/S}, 𝒢) ⟶ Ext¹_{g⁻¹𝒪_X}(𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}, 𝒢)`.

```lean
theorem isomorphismClassesEquivExt_inverseImagePullback
    {G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (J := Opens.grothendieckTopology Y.carrier) Y.sheaf)}
    (Q : SquareZeroAlgebraExtension (g ≫ f) G) :
    SquareZeroAlgebraExtension.isomorphismClassesEquivExt (inverseImageSpaceHom f g)
        (restrictedModule g G) (Quotient.mk _ (inverseImagePullback Q)) =
      inverseImageExtMap
        (SquareZeroAlgebraExtension.isomorphismClassesEquivExt (g ≫ f) G (Quotient.mk _ Q))
```

**`AlgebraicGeometry.RingedSpaceThickening.inverseImageExtEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean, line 628](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean#L628).

> **The identification `Ext¹_{𝒪_Y}(Lg^*𝖭𝖫_{X/S}, 𝒢) = Ext¹_{g⁻¹𝒪_X}(𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}, 𝒢)` of
> Stacks 0GQ2.** Through `Lg^* = Lι^* ∘ π^*` along `g = π ∘ ι`, the tensor–hom adjunction
> `Lι^* ⊣ Rι_* = ι_*` (restriction of scalars along `g^♯ : g⁻¹𝒪_X ⟶ 𝒪_Y`), and the identification
> `g⁻¹𝖭𝖫_{X/S} = 𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}` (`inverseImageNaiveCotangentIso`).

```lean
def inverseImageExtEquiv :
    extOnePulledNaiveCotangent g f G ≃
      extOneNaiveCotangent (inverseImageSpaceHom f g) (restrictedModule g G)
```

**`AlgebraicGeometry.RingedSpaceThickening.inverseImageExtEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean, line 640](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean#L640).

> **The identification `inverseImageExtEquiv` is the explicit composite**: the transposition
> `liftProjTransport` along the adjunction `Lι^* ⊣ ι_*`, preceded by
> `g⁻¹𝖭𝖫_{X/S} = 𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}` and followed by `ι_*(𝒢[1]) = (ι_*𝒢)[1]`.

```lean
theorem inverseImageExtEquiv_apply (z : extOnePulledNaiveCotangent g f G) :
    inverseImageExtEquiv f g G z =
      (DerivedCategory.Q.mapIso (inverseImageNaiveCotangentIso f g)).inv ≫
        liftProjTransport g (PresentedSquareZeroExtension.relativeComplex f) z ≫
        liftShiftSingleIso.hom
```

**`AlgebraicGeometry.RingedSpaceThickening.inverseImageExtEquiv_restrictDerivedExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean, line 661](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean#L661).

> **The image of `ζ` through `Ext¹_{𝒪_Y}(Lg^*𝖭𝖫_{X/S}, 𝒢)` is its image in
> `Ext¹_{g⁻¹𝒪_X}(𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}, 𝒢)`.**

```lean
theorem inverseImageExtEquiv_restrictDerivedExtClass (ζ : extOneNaiveCotangent (g ≫ f) G) :
    inverseImageExtEquiv f g G
        (restrictDerivedExtClass (derivedPullbackNaiveCotangentMap g f) ζ) =
      inverseImageExtMap ζ
```

**`AlgebraicGeometry.RingedSpaceThickening.inverseImageExtEquiv_pullbackExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean, line 959](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean#L959).

> **The image of `ξ` through `Ext¹_{𝒪_Y}(Lg^*𝖭𝖫_{X/S}, 𝒢)` is its image in
> `Ext¹_{g⁻¹𝒪_X}(𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}, 𝒢)`.**

```lean
theorem inverseImageExtEquiv_pullbackExtClass (P : SquareZeroAlgebraExtension f F)
    (c : F ⟶ (modulePushforward g).obj G) :
    inverseImageExtEquiv f g G (pullbackExtClass g f (LiftGluing.cAdj g c) P.extClass) =
      inverseImageXiMap c P.extClass
```

**`AlgebraicGeometry.RingedSpaceThickening.nonempty_compatibleMorphism_iff_isomorphismClassesEquivExt_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean, line 972](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean#L972).

> **Stacks 0GQ2, the classification.** By the diagram chase and the bijection of Stacks 0GPZ for
> the ringed space `(Y, g⁻¹𝒪_X)` over `S`, an `S`-morphism `Y' ⟶ X'` compatible with `g` and `c`
> exists if and only if the extensions `𝒪'₁` and `𝒪'₂` have the same class in
> `Ext¹_{g⁻¹𝒪_X}(𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}, 𝒢)`.

```lean
theorem nonempty_compatibleMorphism_iff_isomorphismClassesEquivExt_eq
    (P : SquareZeroAlgebraExtension f F) (Q : SquareZeroAlgebraExtension (g ≫ f) G)
    (c : F ⟶ (modulePushforward g).obj G) :
    Nonempty (CompatibleMorphism P Q c) ↔
      SquareZeroAlgebraExtension.isomorphismClassesEquivExt (inverseImageSpaceHom f g)
          (restrictedModule g G) (Quotient.mk _ (inverseImagePushout G P c)) =
        SquareZeroAlgebraExtension.isomorphismClassesEquivExt (inverseImageSpaceHom f g)
          (restrictedModule g G) (Quotient.mk _ (inverseImagePullback Q))
```

**`AlgebraicGeometry.RingedSpaceThickening.nonempty_compatibleMorphism_iff_images_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean, line 989](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningExtIdentification.lean#L989).

> **Stacks 0GQ2, the final deduction.** An `S`-morphism `Y' ⟶ X'` compatible with `g` and `c`
> exists if and only if `ξ` and `ζ` have the same image in `Ext¹_{𝒪_Y}(Lg^*𝖭𝖫_{X/S}, 𝒢)`: through the
> identification `Ext¹_{g⁻¹𝒪_X}(𝖭𝖫_{g⁻¹𝒪_X/g⁻¹f⁻¹𝒪_S}, 𝒢) = Ext¹_{𝒪_Y}(Lg^*𝖭𝖫_{X/S}, 𝒢)`
> (`inverseImageExtEquiv`), the class of `𝒪'₁` is the image of `ξ` and the class of `𝒪'₂` is the
> image of `ζ`, so this is `nonempty_compatibleMorphism_iff_isomorphismClassesEquivExt_eq`.

```lean
theorem nonempty_compatibleMorphism_iff_images_eq
    (P : SquareZeroAlgebraExtension f F) (Q : SquareZeroAlgebraExtension (g ≫ f) G)
    (c : F ⟶ (modulePushforward g).obj G) :
    Nonempty (CompatibleMorphism P Q c) ↔
      pullbackExtClass g f (LiftGluing.cAdj g c)
          (SquareZeroAlgebraExtension.isomorphismClassesEquivExt f F (Quotient.mk _ P)) =
        restrictDerivedExtClass (derivedPullbackNaiveCotangentMap g f)
          (SquareZeroAlgebraExtension.isomorphismClassesEquivExt (g ≫ f) G (Quotient.mk _ Q))
```

**`AlgebraicGeometry.RingedSpaceThickening.inverseImagePushout`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningRemark.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningRemark.lean#L275).

> **The extension `𝒪'₁` of Stacks 0GQ2**: the pushout of
> `0 ⟶ g⁻¹ℱ ⟶ g⁻¹𝒪_{X'} ⟶ g⁻¹𝒪_X ⟶ 0` along `c : g⁻¹ℱ ⟶ 𝒢`, an extension
> `0 ⟶ 𝒢 ⟶ 𝒪'₁ ⟶ g⁻¹𝒪_X ⟶ 0` of `g⁻¹f⁻¹𝒪_S`-algebras, that is, a square-zero extension over the
> ringed space `(Y, g⁻¹𝒪_X)` and its morphism to `S`. Here `g⁻¹ℱ` is the kernel of the inverse
> image `g⁻¹𝒪_{X'} ⟶ g⁻¹𝒪_X` of the reduction, and `c` on it is `idealMap`.

```lean
def inverseImagePushout :
    SquareZeroAlgebraExtension (inverseImageSpaceHom f g) (restrictedModule g G)
```

**`AlgebraicGeometry.RingedSpaceThickening.inverseImagePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningRemark.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningRemark.lean#L335).

> **The extension `𝒪'₂` of Stacks 0GQ2**: the pullback of `0 ⟶ 𝒢 ⟶ 𝒪_{Y'} ⟶ 𝒪_Y ⟶ 0` along
> `g^♯ : g⁻¹𝒪_X ⟶ 𝒪_Y`, the extension `0 ⟶ 𝒢 ⟶ 𝒪_{Y'} ×_{𝒪_Y} g⁻¹𝒪_X ⟶ g⁻¹𝒪_X ⟶ 0` of
> `g⁻¹f⁻¹𝒪_S`-algebras; its two projections are the second displayed diagram.

```lean
def inverseImagePullback :
    SquareZeroAlgebraExtension (inverseImageSpaceHom f g) (restrictedModule g G)
```

**`AlgebraicGeometry.RingedSpaceThickening.nonempty_compatibleMorphism_iff_nonempty_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningRemark.lean, line 558](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/InverseImageThickeningRemark.lean#L558).

> **Stacks 0GQ2, the diagram chase.** An `S`-morphism `Y' ⟶ X'` compatible with `g` and `c`
> exists if and only if `𝒪'₁` and `𝒪'₂` are isomorphic as `g⁻¹f⁻¹𝒪_S`-algebra extensions of
> `g⁻¹𝒪_X` by `𝒢`.

```lean
theorem nonempty_compatibleMorphism_iff_nonempty_iso :
    Nonempty (CompatibleMorphism P Q c) ↔
      Nonempty (inverseImagePushout G P c ≅ inverseImagePullback Q)
```

## Tag 0GQ3, a lemma

[Tag 0GQ3](https://stacks.math.columbia.edu/tag/0GQ3) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.DeformationSolution.isomorphismClassesEquivExtFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DeformationSolutionExtFibre.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DeformationSolutionExtFibre.lean#L95).

> Let `t : (S, 𝒪_S) ⟶ (S', 𝒪_{S'})` be a first order thickening, `𝒥 = Ker(t^♯)`
> (`baseIdealModule`), `f : (X, 𝒪_X) ⟶ (S, 𝒪_S)`, `𝒢` an `𝒪_X`-module and `c : 𝒥 ⟶ 𝒢` as in (08U7):
> here `c` is given, as in `DeformationSolution`, by `c' : f^*t^*Ker(t^♯) ⟶ 𝒢`, and is
> `f^*𝒥 ≅ f^*t^*Ker(t^♯) ⟶ 𝒢` (`baseIdealIsoPullback`). Let `ξ ∈ Ext¹_{𝒪_S}(𝖭𝖫_{S/S'}, 𝒥)` be the
> element corresponding to the extension `𝒪_{S'}` of `𝒪_S` by `𝒥` via **Stacks 0GPZ** (`baseClass`).
> The set of isomorphism classes of solutions of (08U7) (first order thickenings `X ⟶ X'` with a
> morphism of thickenings to `S ⟶ S'`, `Ker ≅ 𝒢` and inducing `c`, up to the isomorphism `Isomorphic`
> of **Stacks 08UC**) is canonically bijective to the fibre of
>
> `Ext¹_{𝒪_X}(𝖭𝖫_{X/S'}, 𝒢) ⟶ Ext¹_{𝒪_X}(Lf^*𝖭𝖫_{S/S'}, 𝒢)`
>
> over the image of `ξ`: the map is precomposition with the canonical comparison
> `Lf^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'}` (through the derived pullback `Lf^*` of **Stacks 06YJ**), and the
> image of `ξ` is `Lf^*ξ` pushed along `Lf^*𝒥 ⟶ f^*𝒥 ⟶ 𝒢` (`pullbackExtClass`). The bijection sends
> a solution `X'` to the class, under **Stacks 0GPZ** for `X ⟶ S'`, of `𝒪_{X'}` read as an extension
> of `f⁻¹𝒪_{S'}`-algebras (`DeformationSolution.isomorphismClassesEquivExtFibre_mk`).

```lean
def DeformationSolution.isomorphismClassesEquivExtFibre :
    Quotient (DeformationSolution.isomorphicSetoid ht f G c') ≃
      {z : extOneNaiveCotangent (f ≫ t) G //
        restrictDerivedExtClass (derivedPullbackNaiveCotangentMap f t) z =
          pullbackExtClass f t ((modulePullback f).map (baseIdealIsoPullback ht).hom ≫ c')
            (baseClass ht)}
```

**`AlgebraicGeometry.RingedSpaceThickening.solutionsEquivDerivedExtFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DerivedExtensionClassCriterion.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DerivedExtensionClassCriterion.lean#L173). The attribute's comment: “the canonical bijection from isomorphism classes of solutions of 08U7 to the fibre of Ext¹(𝖭𝖫\_\{X/S'}, 𝒢) ⟶ Ext¹(Lf^*𝖭𝖫\_\{S/S'}, 𝒢) over the image of ξ, by the constructed map [X'] ↦ E [𝒪\_\{X'}]. Carried: the 0GPZ bijection E, the comparison q, and the inputs P, hP, δ, e, hcompat of the 0GQ1 criterion — which is proved here, not assumed”.

> In the situation of **Stacks 08U7**, with `ξ` the class of the extension `𝒪_{S'}` of `𝒪_S`
> by `𝒥`, the isomorphism classes of solutions are canonically bijective to the fibre of
>
> `Ext¹_{𝒪_X}(𝖭𝖫_{X/S'}, 𝒢) ⟶ Ext¹_{𝒪_X}(Lf^*𝖭𝖫_{S/S'}, 𝒢)`
>
> over the image of `ξ`, by the map `[X'] ↦ E [𝒪_{X'}]`.  Here `E` is the bijection of
> **Stacks 0GPZ**, `q` the comparison of naive cotangent complexes, and `P`, `hP`, `δ`, `e`,
> `hcompat` the inputs of `isSolutionClass_iff_eq_pullbackExtClass`.

```lean
def solutionsEquivDerivedExtFibre
    (E : Quotient r ≃ extOneNaiveCotangent (f ≫ t) G)
    (q : derivedPullbackNaiveCotangent f t ⟶ relativeNaiveCotangentObj (f ≫ t))
    (xi : extOneNaiveCotangent t (baseIdealOnReduction t))
    (P : NaiveCotangentTwoTerm
      (DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0))
    (hP : P.obj = derivedPullbackNaiveCotangent f t)
    (δ : Quotient r → (P.conormal ⟶ G))
    (e : ∀ p : Quotient r, SolutionInClass ht c r p ≃
      {θ : P.base ⟶ G // P.d ≫ θ = δ p})
    (hcompat : ∀ p : Quotient r, eqToHom hP ≫
      (pullbackExtClass f t c xi - restrictDerivedExtClass q (E p)) =
        P.conormalExtClass G (δ p)) :
    Quotient (solutionSetoid ht c r) ≃
      {z : extOneNaiveCotangent (f ≫ t) G //
        restrictDerivedExtClass q z = pullbackExtClass f t c xi}
```

**`AlgebraicGeometry.RingedSpaceThickening.solutionsEquivDerivedExtFibre_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DerivedExtensionClassCriterion.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DerivedExtensionClassCriterion.lean#L197). The attribute's comment: “the canonicity of the bijection: it is the constructed map [X'] ↦ E [𝒪\_\{X'}], sending the class of a solution to the class of its underlying extension read through the 0GPZ bijection, rather than an unspecified bijection of the two sides”.

> The bijection `solutionsEquivDerivedExtFibre` sends the class of a solution `X'` to
> `E [𝒪_{X'}]`.

```lean
theorem solutionsEquivDerivedExtFibre_apply
    (E : Quotient r ≃ extOneNaiveCotangent (f ≫ t) G)
    (q : derivedPullbackNaiveCotangent f t ⟶ relativeNaiveCotangentObj (f ≫ t))
    (xi : extOneNaiveCotangent t (baseIdealOnReduction t))
    (P : NaiveCotangentTwoTerm
      (DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0))
    (hP : P.obj = derivedPullbackNaiveCotangent f t)
    (δ : Quotient r → (P.conormal ⟶ G))
    (e : ∀ p : Quotient r, SolutionInClass ht c r p ≃
      {θ : P.base ⟶ G // P.d ≫ θ = δ p})
    (hcompat : ∀ p : Quotient r, eqToHom hP ≫
      (pullbackExtClass f t c xi - restrictDerivedExtClass q (E p)) =
        P.conormalExtClass G (δ p))
    (s : Quotient (solutionSetoid ht c r)) :
    (solutionsEquivDerivedExtFibre ht c r E q xi P hP δ e hcompat s).1 =
      solutionClassToExtClass ht c r E s
```

## Tag 0GQ4, a remark

[Tag 0GQ4](https://stacks.math.columbia.edu/tag/0GQ4) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.naiveCotangentRemarkArrows`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentRemarkConditional.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentRemarkConditional.lean#L69).

> The two maps `Lf^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'} ⟶ 𝖭𝖫_{X/S}` in `D(𝒪_X)`. The first is the canonical
> map of **Stacks 0GQ1** through the derived pullback of **Stacks 06YJ**, the second is induced by
> the tower `(f ≫ t)^{-1}𝒪_{S'} ⟶ f^{-1}𝒪_S ⟶ 𝒪_X`.

```lean
def naiveCotangentRemarkArrows (f : X ⟶ S) (t : S ⟶ S') :
    ComposableArrows (DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) 2
```

**`AlgebraicGeometry.RingedSpaceThickening.DeformationSolution.nonempty_iff_obstructionExtClass_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentRemarkConditional.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentRemarkConditional.lean#L135).

> In the situation of **Stacks 0GQ3** (a first order thickening `t : S ⟶ S'` with ideal `𝒥`,
> `f : X ⟶ S`, an `𝒪_X`-module `𝒢` and `c : f^*𝒥 ⟶ 𝒢`, here `f^*𝒥 ≅ f^*t^*Ker(t^♯) ⟶ 𝒢` with `c'`),
> let `ξ` be the class of the extension `𝒪_{S'}` of `𝒪_S` by `𝒥` under **Stacks 0GPZ** (`baseClass`).
> *If* the two maps `Lf^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'} ⟶ 𝖭𝖫_{X/S}` form a distinguished triangle with some
> connecting map `w`, then a solution of (08U7) exists if and only if the image of `ξ` in
> `Ext²_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢)` — the image of `ξ` in `Ext¹_{𝒪_X}(Lf^*𝖭𝖫_{S/S'}, 𝒢)`
> (`pullbackExtClass`) composed with `w` — vanishes.

```lean
theorem DeformationSolution.nonempty_iff_obstructionExtClass_eq_zero
    (w : relativeNaiveCotangentObj f ⟶ (derivedPullbackNaiveCotangent f t)⟦(1 : ℤ)⟧)
    (htri : Triangle.mk (derivedPullbackNaiveCotangentMap f t)
        (relativeNaiveCotangentObjMap f t) w ∈
      distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))) :
    Nonempty (DeformationSolution t ht f G c') ↔
      obstructionExtClass w (pullbackExtClass f t
        ((modulePullback f).map (baseIdealIsoPullback ht).hom ≫ c') (baseClass ht)) = 0
```

**`AlgebraicGeometry.RingedSpaceThickening.naiveCotangentRemark_closeToDistinguishedTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentRemarkTriangle.lean, line 1236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentRemarkTriangle.lean#L1236).

> **Stacks Project, Tag 0GQ4**, what the remark's two maps
> `Lf^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'} ⟶ 𝖭𝖫_{X/S}` satisfy: they are *close to* forming a distinguished
> triangle, by **Stacks 0E1Z**.  Precisely:
>
> * the composite `Lf^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'} ⟶ 𝖭𝖫_{X/S}` vanishes in `D(𝒪_X)`;
> * the first map factors as the comparison `Lf^*𝖭𝖫_{S/S'} ⟶ f^*𝖭𝖫_{S/S'}` of **Stacks 06YJ**
>   (an isomorphism on `H⁰`) followed by the canonical map `f^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'}`;
> * the second map sits in a distinguished triangle `C[-1] ⟶ 𝖭𝖫_{X/S'} ⟶ 𝖭𝖫_{X/S} ⟶ C`, with
>   `C` the cone of `𝖭𝖫_{X/S'} ⟶ 𝖭𝖫_{X/S}`;
> * the canonical map `f^*𝖭𝖫_{S/S'} ⟶ C[-1]` of **Stacks 0E1Z** lifts `f^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'}`
>   along `C[-1] ⟶ 𝖭𝖫_{X/S'}`, is an isomorphism on `H⁰` and is surjective on `H⁻¹`.
>
> So the maps form a distinguished triangle exactly when the comparison with the cone is an
> isomorphism; the remark only says they are close to one, and nothing more is claimed.

```lean
theorem naiveCotangentRemark_closeToDistinguishedTriangle :
    derivedPullbackNaiveCotangentMap f t ≫ relativeNaiveCotangentObjMap f t = 0 ∧
    remarkPullbackComparison f t ≫ remarkPulledMap f t = derivedPullbackNaiveCotangentMap f t ∧
    IsIso ((DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X)) 0).map
      (remarkPullbackComparison f t)) ∧
    remarkConeTriangle f t ∈ distTriang _ ∧
    (remarkConeTriangle f t).mor₂ = relativeNaiveCotangentObjMap f t ∧
    remarkConeMap f t ≫ (remarkConeTriangle f t).mor₁ = remarkPulledMap f t ∧
    IsIso ((DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X)) 0).map
      (remarkConeMap f t)) ∧
    Epi ((DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X)) (-1)).map
      (remarkConeMap f t))
```

**`AlgebraicGeometry.RingedSpaceThickening.naiveCotangentCompComplexMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentTriangleObstruction.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentTriangleObstruction.lean#L138). The attribute's comment: “the second map of complexes of the remark, 𝖭𝖫\_\{X/S'} ⟶ 𝖭𝖫\_\{X/S}”.

> The map of complexes `𝖭𝖫_{X/S'} ⟶ 𝖭𝖫_{X/S}`: the canonical map of a tower of sheaves of
> rings on `X`, taken at `(f ≫ t)^{-1}𝒪_{S'} ⟶ f^{-1}𝒪_S ⟶ 𝒪_X`.

```lean
public def naiveCotangentCompComplexMap (f : X ⟶ S) (t : S ⟶ S') :
    RingedSpace.naiveCotangentComplex (f ≫ t) ⟶ RingedSpace.naiveCotangentComplex f
```

**`AlgebraicGeometry.RingedSpaceThickening.derivedPullbackNaiveCotangentChain`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentTriangleObstruction.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentTriangleObstruction.lean#L154). The attribute's comment: “the remark's chain Lf^*𝖭𝖫\_\{S/S'} ⟶ 𝖭𝖫\_\{X/S'} ⟶ 𝖭𝖫\_\{X/S}, with q carried”.

> The chain `Lf^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'} ⟶ 𝖭𝖫_{X/S}`, composed in `D(𝒪_X)`: the first map
> is the given comparison `q`, the second is `relativeNaiveCotangentObjMap`.

```lean
public def derivedPullbackNaiveCotangentChain {f : X ⟶ S} {t : S ⟶ S'}
    (q : derivedPullbackNaiveCotangent f t ⟶ relativeNaiveCotangentObj (f ≫ t)) :
    derivedPullbackNaiveCotangent f t ⟶ relativeNaiveCotangentObj f
```

**`AlgebraicGeometry.RingedSpaceThickening.nonempty_deformationSolution_iff_obstruction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentTriangleObstruction.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/NaiveCotangentTriangleObstruction.lean#L216). The attribute's comment: “the conditional: given the triangle, ξ's image in Ext² obstructs 08U7”.

> In the situation of **Stacks 0GQ3**, *given* that the two maps
> `Lf^*𝖭𝖫_{S/S'} ⟶ 𝖭𝖫_{X/S'} ⟶ 𝖭𝖫_{X/S}` form a distinguished triangle with connecting morphism
> `w`, the deformation problem of **Stacks 08U7** has a solution exactly when the image of `ξ` in
> `Ext²_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢)` vanishes; that image is therefore the obstruction.
>
> The triangle is a hypothesis, not a claim: the source only says that the two maps are close to
> forming a distinguished triangle, and its conclusion is drawn under that assumption.  The
> remaining arguments are those of `solutionsEquivDerivedExtFibre`, which supplies the bijection
> of **Stacks 0GQ3** between isomorphism classes of solutions and the fibre over the image of
> `ξ`.

```lean
public theorem nonempty_deformationSolution_iff_obstruction_eq_zero
    (E : Quotient r ≃ extOneNaiveCotangent (f ≫ t) G)
    (q : derivedPullbackNaiveCotangent f t ⟶ relativeNaiveCotangentObj (f ≫ t))
    (xi : extOneNaiveCotangent t (baseIdealOnReduction t))
    (P : NaiveCotangentTwoTerm
      (DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0))
    (hP : P.obj = derivedPullbackNaiveCotangent f t)
    (δ : Quotient r → (P.conormal ⟶ G))
    (e : ∀ p : Quotient r, SolutionInClass ht c r p ≃
      {θ : P.base ⟶ G // P.d ≫ θ = δ p})
    (hcompat : ∀ p : Quotient r, eqToHom hP ≫
      (pullbackExtClass f t c xi - restrictDerivedExtClass q (E p)) =
        P.conormalExtClass G (δ p))
    (w : relativeNaiveCotangentObj f ⟶ (derivedPullbackNaiveCotangent f t)⟦(1 : ℤ)⟧)
    (htri : Triangle.mk q (relativeNaiveCotangentObjMap f t) w ∈
      distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))) :
    Nonempty (DeformationSolution t ht f G c) ↔
      obstructionExtClass w (pullbackExtClass f t c xi) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.7, Tag 08U6](https://stacks.math.columbia.edu/tag/08U6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
