---
declaration: section
origin: cited
lean: AlgebraicGeometry.firstStructureSheafCohomologyVanishes_of_isModification, AlgebraicGeometry.SemistableReduction.TwoModifications.exists_shortExact_firstCohomology, AlgebraicGeometry.SemistableReduction.TwoModifications.topologicalKrullDim_supp_rightDerived_one_pushforward_le_zero, AlgebraicGeometry.SemistableReduction.TwoModifications.nonempty_generatingSections_rightDerived_one_pushforward, AlgebraicGeometry.exists_bound_length_quotient_baseToZeroSchemeSections, AlgebraicGeometry.exists_uniform_bound_length_quotient_baseToZeroSchemeSections, AlgebraicGeometry.nonempty_quotient_baseToZeroSchemeSections_equiv_torsionBy, AlgebraicGeometry.DefinesRationalSingularity
statement: formalized
proof: formalized
---

# 54.8 Boundedness

Section 54.8 of the Stacks Project, [Tag 0AXE](https://stacks.math.columbia.edu/tag/0AXE). 11 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AXF, a lemma

[Tag 0AXF](https://stacks.math.columbia.edu/tag/0AXF) in the Stacks Project.

**`AlgebraicGeometry.firstStructureSheafCohomologyVanishes_of_isModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/FirstCohomologyModificationTransfer.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/FirstCohomologyModificationTransfer.lean#L158). The attribute's comment: “first conclusion, injectivity only: the map H¹(X, 𝒪\_X) ⟶ H¹(X', 𝒪\_\{X'}) of the source's short exact sequence is injective, so a vanishing H¹ upstairs forces one downstairs. Generalized: the base is an arbitrary normal integral scheme, not the spectrum of a two-dimensional normal local domain. NOT proved, and not asserted by this entry: the surjectivity onto H⁰(X, R¹g\_*𝒪\_\{X'}), which rests on Tag 02V7 in fibre dimension one. The tag's second and third conclusions are carried separately in AlgebraicGeometry.SemistableReduction.TwoModifications”.

> **Stacks Project, Tag 0AXF, the injectivity in the first conclusion.** For a modification
> `q : Z ⟶ Y` of a normal integral scheme `Y`, the vanishing of `H¹(Z, 𝒪_Z)` implies the vanishing
> of `H¹(Y, 𝒪_Y)`.
>
> The source states this for modifications of the spectrum of a two-dimensional normal local
> domain; neither the dimension nor the locality nor the affineness of the base is used, so it is
> proved here for an arbitrary normal integral target. Only the injectivity half of the source's
> exact sequence is proved: see the module docstring.

```lean
public theorem firstStructureSheafCohomologyVanishes_of_isModification {Z Y : Scheme.{u}}
    [IsIntegral Y] [IsNormal Y] {q : Z ⟶ Y} (hq : IsModification q)
    (h : FirstStructureSheafCohomologyVanishes Z) :
    FirstStructureSheafCohomologyVanishes Y
```

**`AlgebraicGeometry.SemistableReduction.TwoModifications.exists_shortExact_firstCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LerayShortExactSequenceDimTwo.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LerayShortExactSequenceDimTwo.lean#L371). The attribute's comment: “the short exact sequence 0 → H¹(X, 𝒪\_X) → H¹(X', 𝒪\_\{X'}) → H⁰(X, R¹g\_*𝒪\_\{X'}) → 0”.

> **[Stacks, Tag 0AXF], first conclusion.**  There is a short exact sequence
>
>   `0 ⟶ H¹(X, 𝒪_X) ⟶ H¹(X', 𝒪_{X'}) ⟶ H⁰(X, R¹g_*𝒪_{X'}) ⟶ 0`
>
> of modules over `Γ(X, 𝒪_X)`: the first map is injective and semilinear along `g^♯`, its image is
> the kernel of the second, and the second is surjective and carries the `g^♯`-twisted action to
> the action of `Γ(X, 𝒪_X)`.

```lean
theorem exists_shortExact_firstCohomology :
    ∃ (θ : ((Scheme.sectionsFunctor S.X).rightDerived 1).obj
            (SheafOfModules.unit S.X.ringCatSheaf)
          →ₛₗ[SeparableGoUp.sectionsRingHom S.g]
        ((Scheme.sectionsFunctor S.X').rightDerived 1).obj
          (SheafOfModules.unit S.X'.ringCatSheaf))
      (ψ : (((Scheme.sectionsFunctor S.X').rightDerived 1).obj
            (SheafOfModules.unit S.X'.ringCatSheaf)) →+
        (Scheme.sectionsFunctor S.X).obj (((Scheme.Modules.pushforward S.g).rightDerived 1).obj
          (SheafOfModules.unit S.X'.ringCatSheaf))),
      Function.Injective θ ∧
        (∀ (r : Scheme.sectionsRing S.X) y,
          ψ (SeparableGoUp.sectionsRingHom S.g r • y) = r • ψ y) ∧
        (∀ y, ψ y = 0 ↔ ∃ x, θ x = y) ∧
        Function.Surjective ψ
```

**`AlgebraicGeometry.SemistableReduction.TwoModifications.topologicalKrullDim_supp_rightDerived_one_pushforward_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/HigherDirectImageBoundedness.lean, line 719](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/HigherDirectImageBoundedness.lean#L719). The attribute's comment: “dim(Supp(R¹g\_*𝒪\_\{X'})) = 0, read as dimension at most zero”.

> **[Stacks, Tag 0AXF], second conclusion.**  The support of `R¹g_*𝒪_{X'}` has dimension zero:
> it is a finite set of closed points of `X`.  As everywhere in this development the source's
> `dim = 0` is read as `≤ 0`, the support being allowed to be empty.

```lean
theorem topologicalKrullDim_supp_rightDerived_one_pushforward_le_zero :
    topologicalKrullDim (SheafOfModules.supp
      (((Scheme.Modules.pushforward S.g).rightDerived 1).obj
        (SheafOfModules.unit S.X'.ringCatSheaf))) ≤ 0
```

**`AlgebraicGeometry.SemistableReduction.TwoModifications.nonempty_generatingSections_rightDerived_one_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/HigherDirectImageBoundedness.lean, line 732](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/HigherDirectImageBoundedness.lean#L732). The attribute's comment: “R¹g\_*𝒪\_\{X'} is generated by global sections”.

> **[Stacks, Tag 0AXF], third conclusion.**  `R¹g_*𝒪_{X'}` is generated by global sections.
> Its support is a finite set of closed points, so a germ at any of them extends by zero to a
> global section.

```lean
theorem nonempty_generatingSections_rightDerived_one_pushforward :
    Nonempty ((((Scheme.Modules.pushforward S.g).rightDerived 1).obj
      (SheafOfModules.unit S.X'.ringCatSheaf)).GeneratingSections)
```

## Tag 0AXJ, a lemma

[Tag 0AXJ](https://stacks.math.columbia.edu/tag/0AXJ) in the Stacks Project.

**`AlgebraicGeometry.exists_bound_length_quotient_baseToZeroSchemeSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ZeroSchemeSectionsBound.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ZeroSchemeSectionsBound.lean#L159). The attribute's comment: “`hsub` carries the subquotient step: `M_{X,c}` embeds into `B / (A ⧸ cA)` because the closure of `Z ∩ f⁻¹(U)` is a spectrum between them (Stacks 0AB7) and `H⁰(Z, 𝒪_Z)` injects on it (Stacks 0AXB, absent from this library)”.

> **Stacks Project, Tag 0AXJ.** Let `(A, 𝔪, κ)` be a local normal Nagata domain of dimension
> two and let `a ∈ A` be nonzero. There is an integer `N` such that for every modification
> `f : X ⟶ Spec A` with `X` normal the `A`-module
>
>   `M_{X,a} = Coker(A ⟶ H⁰(Z, 𝒪_Z))`,
>
> for `Z ⊂ X` the closed subscheme cut out by `a`, has length at most `N`.
>
> A unit `a` cuts out the empty subscheme, so the cokernel vanishes. Otherwise `a` is replaced by
> an element with reduced principal quotient: the cokernel is the `a`-torsion submodule of
> `H¹(X, 𝒪_X)`, which is monotone in divisibility and whose length grows at most linearly along
> powers, and `a` divides a power of a nonzero `c ∈ 𝔪` with `A ⧸ cA` reduced. For such a `c` the
> bound is the length of the cokernel `B / (A ⧸ cA)` of the integral closure `B` of `A ⧸ cA` in
> its total ring of fractions, and the hypothesis `hsub` converts a bound on that cokernel into
> one on `M_{X,c}`.

```lean
theorem exists_bound_length_quotient_baseToZeroSchemeSections {A : Type u} [CommRing A]
    [IsLocalRing A] [IsNormalDomain A] [IsNagataRing A] (hdim : ringKrullDim A = 2) {a : A}
    (ha : a ≠ 0)
    (hsub : ∀ c : A, c ≠ 0 → c ∈ IsLocalRing.maximalIdeal A →
        _root_.IsReduced (A ⧸ Ideal.span {c}) → ∀ N : ℕ,
      Module.length (A ⧸ Ideal.span {c}) (normalizationCokernel (A ⧸ Ideal.span {c})) ≤ N →
        ∀ (X : Scheme.{u}) [IsNormal X] (f : X ⟶ Spec (.of A)), IsModification f →
          Module.length A (globalSectionsAsBaseModule X f (zeroSchemeStructureSheaf X f c) ⧸
            LinearMap.range (baseToZeroSchemeSections X f c)) ≤ N) :
    ∃ N : ℕ, ∀ (X : Scheme.{u}) [IsNormal X] (f : X ⟶ Spec (.of A)), IsModification f →
      Module.length A (globalSectionsAsBaseModule X f (zeroSchemeStructureSheaf X f a) ⧸
        LinearMap.range (baseToZeroSchemeSections X f a)) ≤ N
```

**`AlgebraicGeometry.exists_uniform_bound_length_quotient_baseToZeroSchemeSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ZeroSchemeSectionsNormalization.lean, line 725](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ZeroSchemeSectionsNormalization.lean#L725).

> Let `(A, 𝔪, κ)` be a local normal Nagata domain of dimension two and let `a ∈ A` be nonzero.
> There is an integer `N` such that for every modification `f : X ⟶ Spec A` with `X` normal the
> `A`-module
>
>   `M_{X,a} = Coker(A ⟶ H⁰(Z, 𝒪_Z))`,
>
> for `Z ⊂ X` the closed subscheme cut out by `a`, has length at most `N`.

```lean
theorem exists_uniform_bound_length_quotient_baseToZeroSchemeSections {A : Type u} [CommRing A]
    [IsLocalRing A] [IsNormalDomain A] [IsNagataRing A] (hdim : ringKrullDim A = 2) {a : A}
    (ha : a ≠ 0) :
    ∃ N : ℕ, ∀ (X : Scheme.{u}) [IsNormal X] (f : X ⟶ Spec (.of A)), IsModification f →
      Module.length A (globalSectionsAsBaseModule X f (zeroSchemeStructureSheaf X f a) ⧸
        LinearMap.range (baseToZeroSchemeSections X f a)) ≤ N
```

## Tag 0AXK, an equation

[Tag 0AXK](https://stacks.math.columbia.edu/tag/0AXK) in the Stacks Project.

**`AlgebraicGeometry.nonempty_quotient_baseToZeroSchemeSections_equiv_torsionBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ModificationATorsion.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ModificationATorsion.lean#L167).

> **Stacks Project, Tag 0AXK.** For a nonzero element `a` of a normal domain `A` and a
> modification `f : X ⟶ Spec A`, the cokernel of `A ⟶ H⁰(Z, 𝒪_Z)`, for `Z ⊂ X` cut out by `a`, is
> the `a`-torsion submodule of `H¹(X, 𝒪_X)`.

```lean
theorem nonempty_quotient_baseToZeroSchemeSections_equiv_torsionBy [IsNormalDomain A]
    (hf : IsModification f) {a : A} (ha : a ≠ 0) :
    Nonempty ((globalSectionsAsBaseModule X f (zeroSchemeStructureSheaf X f a) ⧸
        LinearMap.range (baseToZeroSchemeSections X f a)) ≃ₗ[A]
      Submodule.torsionBy A (firstCohomologyAsBaseModule X f) a)
```

## Tag 0B4N, a definition

[Tag 0B4N](https://stacks.math.columbia.edu/tag/0B4N) in the Stacks Project.

**`AlgebraicGeometry.DefinesRationalSingularity`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RationalSingularity.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RationalSingularity.lean#L49). The attribute's comment: “defines\_rational\_singularity”.

> An integral domain `A` **defines a rational singularity** if the first cohomology of the
> structure sheaf of every normal modification of `Spec A` vanishes.

```lean
noncomputable abbrev DefinesRationalSingularity
    (A : Type u) [CommRing A] [IsDomain A] : Prop
```

**`AlgebraicGeometry.IsReductionToRationalSingularitiesPossible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/Reduction.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/Reduction.lean#L50). The attribute's comment: “reduction\_to\_rational\_singularities\_possible”.

> Reduction to rational singularities is possible for `A` if the `A`-module lengths of
> `H¹(X, 𝒪_X)` have a common finite bound over all normal modifications `X ⟶ Spec A`.

```lean
abbrev IsReductionToRationalSingularitiesPossible (A : Type u) [CommRing A] [IsDomain A] :
    Prop
```

## Tag 0BG0, a lemma

[Tag 0BG0](https://stacks.math.columbia.edu/tag/0BG0) in the Stacks Project.

**`AlgebraicGeometry.definesRationalSingularity_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LocalBirationalExtensionsRational.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LocalBirationalExtensionsRational.lean#L92). The attribute's comment: “a local extension A ⊂ B of domains with the same fraction field, essentially of finite type, A a 2-dimensional local normal Nagata domain defining a rational singularity, B normal of dimension 2: B defines a rational singularity”.

> **Stacks Project, Tag 0BG0.** Let `(A, 𝔪)` be a two-dimensional local normal Nagata domain
> defining a rational singularity, and let `A ⟶ B` be a local extension of normal local domains
> with the same fraction field `K`, essentially of finite type, with `dim B = 2`. Then `B` defines
> a rational singularity.

```lean
theorem definesRationalSingularity_of_essFiniteType (A B : Type u) [CommRing A] [IsLocalRing A]
    [IsNormalDomain A] [CommRing B] [IsLocalRing B] [IsNormalDomain B] [Algebra A B]
    [IsLocalHom (algebraMap A B)] (K : Type u) [Field K] [Algebra A K] [Algebra B K]
    [IsScalarTower A B K] [IsFractionRing A K] [IsFractionRing B K] (hN : IsNagataRing A)
    (hA : ringKrullDim A = 2) (hB : ringKrullDim B = 2) (hft : Algebra.EssFiniteType A B)
    (hrat : DefinesRationalSingularity A) : DefinesRationalSingularity B
```

## Tag 0B4P, a lemma

[Tag 0B4P](https://stacks.math.columbia.edu/tag/0B4P) in the Stacks Project.

**`AlgebraicGeometry.exists_normalizedBlowUpSeq_definesRationalSingularity_stalk_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedPointBlowupRationalSingularity.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedPointBlowupRationalSingularity.lean#L101). The attribute's comment: “Complete, under exactly the source's hypotheses, with every clause of the source.”.

> **[Stacks, Tag 0B4P].** For a local normal Nagata domain `A` of dimension two for which
> reduction to rational singularities is possible, there is a finite sequence of normalized blowups
> at closed points `X = Xₙ ⟶ ⋯ ⟶ X₁ ⟶ X₀ = Spec A` with `X` normal, the structure morphism a
> projective modification, and the local ring of `X` at every closed point defining a rational
> singularity.

```lean
theorem exists_normalizedBlowUpSeq_definesRationalSingularity_stalk_unconditional
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNormalDomain A]
    (hNagata : IsNagataRing A) (hdim : ringKrullDim A = 2)
    (hReduction : IsReductionToRationalSingularitiesPossible A) :
    ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) (hX : IsNormal X),
      letI := hX
      NormalizedBlowUpSeq (Spec (.of A)) X f ∧ IsModification f ∧ IsProjectiveMorphism f ∧
        ∀ x : X, IsClosed ({x} : Set X) →
          DefinesRationalSingularity (X.presheaf.stalk x)
```

## Tag 0AXL, a lemma

[Tag 0AXL](https://stacks.math.columbia.edu/tag/0AXL) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.isReductionToRationalSingularitiesPossible_of_finite_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/FiniteSeparableExtension.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/FiniteSeparableExtension.lean#L67).

> Let `A ⟶ B` be a finite injective local map of local normal
> Nagata domains of dimension two, let `K` and `L` be their fraction fields and assume `L/K`
> separable. If reduction to rational singularities is possible for `A`, it is possible for `B`.

```lean
theorem isReductionToRationalSingularitiesPossible_of_finite_of_isSeparable
    {A B : Type u} [CommRing A] [IsLocalRing A] [IsNormalDomain A] [IsNagataRing A]
    [CommRing B] [IsLocalRing B] [IsNormalDomain B] [IsNagataRing B]
    [Algebra A B] [Module.Finite A B] [IsLocalHom (algebraMap A B)]
    (K L : Type u) [Field K] [Field L]
    [Algebra A K] [IsFractionRing A K] [Algebra B L] [IsFractionRing B L]
    [Algebra K L] [Algebra A L] [IsScalarTower A K L] [IsScalarTower A B L]
    [Algebra.IsSeparable K L]
    (hdimA : ringKrullDim A = 2) (hdimB : ringKrullDim B = 2)
    (hinj : Function.Injective (algebraMap A B))
    (hA : IsReductionToRationalSingularitiesPossible A) :
    IsReductionToRationalSingularitiesPossible B
```

**`AlgebraicGeometry.SeparableGoUp.isReductionToRationalSingularitiesPossible_of_finite_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/SeparableGoUpTransfer.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/SeparableGoUpTransfer.lean#L103).

> **Stacks Project, Tag 0AXL.** Let `A → B` be a finite injective local ring map of local normal
> Nagata domains of dimension two such that the induced extension of fraction fields is separable.
> If reduction to rational singularities is possible for `A`, then it is possible for `B`.

```lean
theorem isReductionToRationalSingularitiesPossible_of_finite_of_isSeparable (A B : Type u)
    [CommRing A] [IsLocalRing A] [IsNormalDomain A] [IsNagataRing A] [CommRing B]
    [IsLocalRing B] [IsNormalDomain B] [IsNagataRing B] [Algebra A B] [Module.Finite A B]
    [FaithfulSMul A B] [IsLocalHom (algebraMap A B)] (_hdimA : ringKrullDim A = 2)
    (hdimB : ringKrullDim B = 2)
    (hsep : letI := FractionRing.liftAlgebra A (FractionRing B)
      Algebra.IsSeparable (FractionRing A) (FractionRing B))
    (hA : IsReductionToRationalSingularitiesPossible A) :
    IsReductionToRationalSingularitiesPossible B
```

## Tag 0B4Q, a lemma

[Tag 0B4Q](https://stacks.math.columbia.edu/tag/0B4Q) in the Stacks Project.

**`AlgebraicGeometry.definesRationalSingularity_of_isRegularLocalRing_of_ringKrullDim_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRingDefinesRational.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRingDefinesRational.lean#L148).

> **Stacks Project, Tag 0B4Q.** A Nagata regular local ring of dimension two defines a rational
> singularity.

```lean
theorem definesRationalSingularity_of_isRegularLocalRing_of_ringKrullDim_eq_two (A : Type u)
    [CommRing A] [IsRegularLocalRing A] [IsNagataRing A] (hdim : ringKrullDim A = 2) :
    letI := IsRegularLocalRing.isDomain A; DefinesRationalSingularity A
```

**`AlgebraicGeometry.definesRationalSingularity_of_isRegularLocalRing_of_isNagataRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRingRational.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRingRational.lean#L314).

> **Stacks Project, Tag 0B4Q.** A Nagata regular local ring `A` of dimension two defines a
> rational singularity: `H¹(X, 𝒪_X) = 0` for every modification `X ⟶ Spec(A)` with `X` normal.
> (A regular local ring is a domain, which `DefinesRationalSingularity` needs as an instance; it is
> supplied by `IsRegularLocalRing.isDomain`.)
>
> The modification is dominated by a chain of normalized blowups at closed points
> ([Stacks, Tag 0BBT], which uses the Nagata hypothesis); along the chain every scheme is regular
> with two-dimensional local rings at its closed points and has `H¹(𝒪) = 0`
> (`AlgebraicGeometry.normalizedBlowUpChain_invariant`), and `H¹(X, 𝒪_X)` embeds into the
> cohomology of the dominating scheme ([Stacks, Tag 0AXF]). Nothing beyond the source's
> hypotheses is assumed; the conditional forms of the argument, which carry Tags 0AHI, 0AXF and
> 0AGS as hypotheses, are listed in the module docstring.

```lean
theorem definesRationalSingularity_of_isRegularLocalRing_of_isNagataRing (A : Type u)
    [CommRing A] [IsRegularLocalRing A] [IsNagataRing A] (hdim : ringKrullDim A = 2) :
    @DefinesRationalSingularity A _ (IsRegularLocalRing.isDomain A)
```

## Tag 0B4S, a lemma

[Tag 0B4S](https://stacks.math.columbia.edu/tag/0B4S) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.isReductionToRationalSingularitiesPossible_of_smul_baseTraceCokernel_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/TraceCokernelImageLift.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/TraceCokernelImageLift.lean#L363). The attribute's comment: “reduction to rational singularities for a two-dimensional local normal Nagata domain with a normalized dualizing complex, from a nonzero element annihilating the cokernel of the trace map of every normal modification; the trace is Stacks.Duality.baseTrace, the trace of Tag 0AWG over the affine base, read on H^\{-2}, whose source is the global sections of the normalized dualizing module of X by homologyNegTwoDerivedGlobalSectionsIso and whose target is the dualizing module of A by dualizingModule\_eq\_homologyFunctor\_negTwo\_obj; Grauert-Riemenschneider vanishing (Tag 0AXD) is discharged in TraceCokernelVanishingHom.lean and the uniform length bound of Tags 0AXJ and 0AXK upstream”.

> Let `(A, 𝔪, κ)` be a local normal Nagata domain of dimension two with a normalized
> dualizing complex `ω_A^•`. If some nonzero `d ∈ A` annihilates the cokernel of the
> trace map `Γ(X, ω_X) ⟶ ω_A` for every modification `f : X ⟶ Spec(A)` with `X` normal — `ω_X`
> being the dualizing module of `X` normalized relative to `ω_A^•` — then reduction to rational
> singularities is possible for `A`: the `A`-module lengths of `H¹(X, 𝒪_X)` admit a common finite
> bound over all such `X`.
>
> The trace is the trace of [Stacks, Tag 0AWG] over the affine base
> (`Stacks.Duality.baseTrace`) read on degree `-2` cohomology. Its source is `Γ(X, ω_X)` by
> `AlgebraicGeometry.homologyNegTwoDerivedGlobalSectionsIso`, and its target is `ω_A` by
> `Dualizing.dualizingModule_eq_homologyFunctor_negTwo_obj`: the dualizing module of a
> two-dimensional Noetherian local ring is `H^{-2}` of its dualizing complex, which is the source's
> own reading `ω_A^• = ω_A[2]`.
>
> Duality turns the annihilation into the factorisation hypothesis of
> `isReductionToRationalSingularitiesPossible_of_exists_comp_baseTrace_eq`: `A[-2]` corepresents
> `H^{-2}` on `D(A)` (`Dualizing.homologyLinearEquiv`), naturally in its argument
> (`Dualizing.homologyLinearEquiv_symm_comp`), so a morphism `q : A[-2] ⟶ ω_A^•` is an element of
> `ω_A`, and `d · q` lying in the image of the trace is exactly that factorisation.
>
> The source assumes only that `A` *has* a dualizing complex. Asking for a normalized one costs
> nothing: the normalizing shift of [Stacks, Tag 0AX1]
> (`Dualizing.exists_isNormalizedDualizingComplex_shift`) produces one from any dualizing complex,
> and it is the normalized complex whose `H^{-2}` is the dualizing module `ω_A` that the source's
> hypothesis is about. The complex has to be named in the statement because the hypothesis on `d`
> mentions it.

```lean
theorem isReductionToRationalSingularitiesPossible_of_smul_baseTraceCokernel_eq_zero
    [IsLocalRing A] [IsNormalDomain A] [IsNagataRing A] (hdim : ringKrullDim A = 2)
    (ωA : DerivedCategory (ModuleCat.{u} A))
    (hωA : Dualizing.IsNormalizedDualizingComplex.{u, u} ωA) (d : A) (hd : d ≠ 0)
    (hcoker : ∀ (X : Scheme.{u}) [IsNormal X] (f : X ⟶ Spec (.of A)) (hf : IsModification f),
      letI : IsProper f := hf.isProper
      letI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
      letI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
      ∀ z : ↥((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-2)).obj ωA) ⧸
          LinearMap.range ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-2)).map
            (baseTrace f ωA)).hom,
        d • z = 0) :
    IsReductionToRationalSingularitiesPossible A
```

## Tag 0B4T, a lemma

[Tag 0B4T](https://stacks.math.columbia.edu/tag/0B4T) in the Stacks Project.

**`Stacks.BlowupTwistUnit.exists_topFormsTrace_eq_baseIsoOfTopForms_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BlowupTwistUnit/TopFormsTraceRegularLocal.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BlowupTwistUnit/TopFormsTraceRegularLocal.lean#L200). The attribute's comment: “the map phi\_X from the reflexive hull of the top relative differential forms of X over A\_0 to the dualizing module omega\_X normalized relative to omega\_A = Omega^r\_\{A/A\_0}, for every sequence of blowups in closed points of a regular local base of dimension two, extending the given identification: pulling the top forms back to X, applying phi\_X and taking the trace of omega\_X back to Spec A gives the identification omega\_A = Omega^r\_\{A/A\_0}. The family omega\_X, the identification and the normalization are constructed from the hypotheses of the tag, and at each blowup the automorphism by which the direct-image comparison differs from the canonical map is proved invertible”.

> **Stacks Project, Tag 0B4T.** Let `A` be a regular local ring of dimension two and `A₀ ⊆ A` a
> subring with `Ω_{A/A₀}` free of rank `r`, and set `ω_A = Ω^r_{A/A₀}`. If `f : X ⟶ Spec A` is the
> result of a sequence of blowups in closed points then there is a map
>
> `φ_X : (Ω^r_{X/A₀})^{**} ⟶ ω_X`
>
> extending the given identification, `ω_X` being the dualizing module of `X` normalized relative
> to `ω_A`.
>
> *Extending the identification* is the equation
>
> `(ChainTopFormData.ofTopForms hS T p r hdimA).topFormsTrace hf φ =
>   (baseIsoOfTopForms hS T p r).inv`:
>
> the composite
>
> `Ω^r_{A/A₀} ⟶ f_*((Ω^r_{X/A₀})^{**}) ⟶ Rf_*((Ω^r_{X/A₀})^{**}[0]) ⟶ Rf_*(ω_X[0]) ⟶ ω_A`
>
> — the pullback of top forms into the reflexive hull, then `Rf_*φ_X`, then the trace of `f`, the
> counit of `Rf_* ⊣ f^×` at the normalization `ω_X[0] ≅ f^×(ω_A[0])` — is the identification
> `ω_A ≅ Ω^r_{A/A₀}`. Over the open `U` of `Spec A` over which `f` is an isomorphism, which contains
> the generic point, the pullback of forms is the isomorphism `Ω^r_{U/A₀} ≅ f_*Ω^r_{f⁻¹U/A₀}` and the
> trace is the identification of `f_*ω_X` with `ω_A` that `f` induces, so the equation says that
> `φ_X` restricted to `f⁻¹U` is the given identification transported along `f`. The equation is about
> `φ_X` itself, not about a map built from it up to a unit: the right-hand side is the identification
> of `ω_A` with `Ω^r_{A/A₀}`, on the nose.
>
> The hypotheses are the tag's: `S` is an integral regular surface whose ring of global sections is
> a regular local ring of dimension two, and `Ω_{S/S₀}` is coherent and free of rank `r`. The family
> `ω_X` is `chainDualizingModuleOfTopForms`, constructed; the identification is
> `baseIsoOfTopForms`, proved; the normalization is `normalizedChainDualizingModule`, proved.
>
> The proof is the induction of the source (`ChainTopFormData.exists_topFormsTrace_eq`). At each
> blowup the comparison `Rb_*((Ω^r_{X'})^{**}[0]) ⟶ (Ω^r_X)^{**}[0]` is built from the dichotomy of
> [Stacks, Tag 0B3T], and the automorphism of `(Ω^r_X)^{**}` it differs by from the canonical map is
> proved invertible and cancelled (`exists_isIso_comparison_blowUp`); the isomorphism
> `Rb_*((Ω^r_{X'})^{**}) ≅ (Ω^r_X)^{**}` the source's proof asserts is not used.

```lean
theorem exists_topFormsTrace_eq_baseIsoOfTopForms_inv
    (hS : IsIntegralRegularSurface S) (T : Set S) (p : S ⟶ S₀) (r : ℕ)
    [(Scheme.Hom.relativeDifferentials p).IsCoherent]
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (Scheme.Hom.relativeDifferentials p) r]
    (hdimA : ringKrullDim Γ(S, ⊤) = 2)
    {X : Scheme.{u}} {f : X ⟶ S} (hf : PointBlowupChain S T X f) :
    ∃ φ : hullForms p (r : ℤ) f ⟶ chainDualizingModuleOfTopForms hS T p r X f,
      (ChainTopFormData.ofTopForms hS T p r hdimA).topFormsTrace hf φ =
        (baseIsoOfTopForms hS T p r).inv
```

## Tag 0B4U, a lemma

[Tag 0B4U](https://stacks.math.columbia.edu/tag/0B4U) in the Stacks Project.

**`AlgebraicGeometry.SeparableGoUp.isReductionToRationalSingularitiesPossible_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/InseparableReductionAssembly.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/InseparableReductionAssembly.lean#L43).

> **Stacks Project, Tag 0B4U.** Let `p` be a prime number, `A` a complete regular local ring of
> dimension two and characteristic `p`, `L/K` an inseparable extension of degree `p` of the
> fraction field `K` of `A`, and `B ⊆ L` the integral closure of `A`. Then reduction to rational
> singularities is possible for `B`.

```lean
theorem isReductionToRationalSingularitiesPossible_integralClosure (p : ℕ)
    (hp : p.Prime) (A : Type u) [CommRing A] [IsRegularLocalRing A]
    [IsAdicComplete (IsLocalRing.maximalIdeal A) A] [CharP A p] (hdim : ringKrullDim A = 2)
    (K L : Type u) [Field K] [Field L] [Algebra A K] [IsFractionRing A K] [Algebra K L]
    [Algebra A L] [IsScalarTower A K L] (hdeg : Module.finrank K L = p)
    (hinsep : ¬ Algebra.IsSeparable K L) :
    IsReductionToRationalSingularitiesPossible (integralClosure A L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.8, Tag 0AXE](https://stacks.math.columbia.edu/tag/0AXE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
