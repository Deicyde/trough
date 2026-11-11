---
declaration: section
origin: cited
lean: AlgebraicGeometry.firstStructureSheafCohomologyVanishes_of_isModification, AlgebraicGeometry.SemistableReduction.TwoModifications.exists_shortExact_firstCohomology, AlgebraicGeometry.SemistableReduction.TwoModifications.topologicalKrullDim_supp_rightDerived_one_pushforward_le_zero, AlgebraicGeometry.SemistableReduction.TwoModifications.nonempty_generatingSections_rightDerived_one_pushforward, AlgebraicGeometry.exists_bound_length_quotient_baseToZeroSchemeSections, AlgebraicGeometry.exists_uniform_bound_length_quotient_baseToZeroSchemeSections, AlgebraicGeometry.nonempty_quotient_baseToZeroSchemeSections_equiv_torsionBy, AlgebraicGeometry.DefinesRationalSingularity
statement: formalized
proof: formalized
---

# 54.8 Boundedness

Section 54.8 of the Stacks Project, [Tag 0AXE](https://stacks.math.columbia.edu/tag/0AXE). 11 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AXF, a lemma

[Tag 0AXF](https://stacks.math.columbia.edu/tag/0AXF) in the Stacks Project.

**`AlgebraicGeometry.firstStructureSheafCohomologyVanishes_of_isModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/FirstCohomologyModificationTransfer.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/FirstCohomologyModificationTransfer.lean#L158). The attribute's comment: “first conclusion, injectivity only: the map H¹(X, 𝒪\_X) ⟶ H¹(X', 𝒪\_\{X'}) of the source's short exact sequence is injective, so a vanishing H¹ upstairs forces one downstairs. Generalized: the base is an arbitrary normal integral scheme, not the spectrum of a two-dimensional normal local domain. NOT proved, and not asserted by this entry: the surjectivity onto H⁰(X, R¹g\_*𝒪\_\{X'}), which rests on Tag 02V7 in fibre dimension one. The tag's second and third conclusions are carried separately in AlgebraicGeometry.SemistableReduction.TwoModifications”.

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

**`AlgebraicGeometry.SemistableReduction.TwoModifications.exists_shortExact_firstCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LerayShortExactSequenceDimTwo.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LerayShortExactSequenceDimTwo.lean#L371). The attribute's comment: “the short exact sequence 0 → H¹(X, 𝒪\_X) → H¹(X', 𝒪\_\{X'}) → H⁰(X, R¹g\_*𝒪\_\{X'}) → 0”.

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

**`AlgebraicGeometry.SemistableReduction.TwoModifications.topologicalKrullDim_supp_rightDerived_one_pushforward_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/HigherDirectImageBoundedness.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/HigherDirectImageBoundedness.lean#L719). The attribute's comment: “dim(Supp(R¹g\_*𝒪\_\{X'})) = 0, read as dimension at most zero”.

> **[Stacks, Tag 0AXF], second conclusion.**  The support of `R¹g_*𝒪_{X'}` has dimension zero:
> it is a finite set of closed points of `X`.  As everywhere in this development the source's
> `dim = 0` is read as `≤ 0`, the support being allowed to be empty.

```lean
theorem topologicalKrullDim_supp_rightDerived_one_pushforward_le_zero :
    topologicalKrullDim (SheafOfModules.supp
      (((Scheme.Modules.pushforward S.g).rightDerived 1).obj
        (SheafOfModules.unit S.X'.ringCatSheaf))) ≤ 0
```

**`AlgebraicGeometry.SemistableReduction.TwoModifications.nonempty_generatingSections_rightDerived_one_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/HigherDirectImageBoundedness.lean, line 732](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/HigherDirectImageBoundedness.lean#L732). The attribute's comment: “R¹g\_*𝒪\_\{X'} is generated by global sections”.

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

**`AlgebraicGeometry.exists_bound_length_quotient_baseToZeroSchemeSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ZeroSchemeSectionsBound.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ZeroSchemeSectionsBound.lean#L159). The attribute's comment: “`hsub` carries the subquotient step: `M_{X,c}` embeds into `B / (A ⧸ cA)` because the closure of `Z ∩ f⁻¹(U)` is a spectrum between them (Stacks 0AB7) and `H⁰(Z, 𝒪_Z)` injects on it (Stacks 0AXB, absent from this library)”.

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

**`AlgebraicGeometry.exists_uniform_bound_length_quotient_baseToZeroSchemeSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ZeroSchemeSectionsNormalization.lean, line 725](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ZeroSchemeSectionsNormalization.lean#L725).

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

**`AlgebraicGeometry.nonempty_quotient_baseToZeroSchemeSections_equiv_torsionBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ModificationATorsion.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/ModificationATorsion.lean#L167).

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

**`AlgebraicGeometry.DefinesRationalSingularity`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RationalSingularity.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RationalSingularity.lean#L49). The attribute's comment: “defines\_rational\_singularity”.

> An integral domain `A` **defines a rational singularity** if the first cohomology of the
> structure sheaf of every normal modification of `Spec A` vanishes.

```lean
noncomputable abbrev DefinesRationalSingularity
    (A : Type u) [CommRing A] [IsDomain A] : Prop
```

**`AlgebraicGeometry.IsReductionToRationalSingularitiesPossible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/Reduction.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/Reduction.lean#L50). The attribute's comment: “reduction\_to\_rational\_singularities\_possible”.

> Reduction to rational singularities is possible for `A` if the `A`-module lengths of
> `H¹(X, 𝒪_X)` have a common finite bound over all normal modifications `X ⟶ Spec A`.

```lean
abbrev IsReductionToRationalSingularitiesPossible (A : Type u) [CommRing A] [IsDomain A] :
    Prop
```

## Tag 0BG0, a lemma

[Tag 0BG0](https://stacks.math.columbia.edu/tag/0BG0) in the Stacks Project.

**`AlgebraicGeometry.definesRationalSingularity_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LocalBirationalExtensions.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LocalBirationalExtensions.lean#L257). The attribute's comment: “the local-ring form: `𝒪_{X, x}` defines a rational singularity for a closed point `x` of a normal scheme `X` over `Spec(A)`. Proved: the spreading out of a normal modification of `Spec 𝒪_{X, x}` to a proper modification of `X` (Tags 0B3X and 0BFN) and the application of the hypothesis on `A` to it. Carried as named hypotheses: `ModificationIsFinitePresentationAway` (a normal modification of a two-dimensional normal local ring is of finite presentation and an isomorphism over the punctured spectrum), `SpreadOutIsNormalModification` (Step 4 of the source's proof: the local rings of the spread-out scheme), and `SpreadOutVanishingDescends` (the first conclusion of Tag 0AXF, absent from this development, together with the identification of the stalk of `R¹g_*𝒪_{X'}` with `H¹(Y, 𝒪_Y)`). Not formalized: Steps 1 and 2, which realize a two-dimensional normal local domain essentially of finite type and birational over `A` as such an `𝒪_{X, x}` by taking the closure of `Spec(C) ⊆ 𝐀ⁿ_A` in `𝐏ⁿ_A` and normalizing”.

> **[Stacks, Tag 0BG0], local-ring form.**  Let `A` be a domain defining a rational
> singularity, `X` a normal scheme with a morphism `f : X ⟶ Spec(A)`, and `x ∈ X` a closed point
> whose open complement has quasi-compact inclusion.  Then the local ring `𝒪_{X, x}` defines a
> rational singularity.
>
> A normal modification of `Spec 𝒪_{X, x}` is spread out to a proper morphism `g : X' ⟶ X` which
> is an isomorphism over `X ∖ {x}` by [Stacks, Tag 0B3X] and [Stacks, Tag 0BFN]; the hypothesis on
> `A` applies to the modification `g ≫ f`, and the vanishing descends to the base change.

```lean
theorem definesRationalSingularity_stalk {A : Type u} [CommRing A] [IsDomain A]
    {X : Scheme.{u}} [IsNormal X] (f : X ⟶ Spec (.of A)) (x : X)
    (hx : IsClosed ({x} : Set X)) (hqc : QuasiCompact (puncturedOpen hx).ι)
    (hA : DefinesRationalSingularity A)
    (hfp : ModificationIsFinitePresentationAway x hx)
    (hnormal : SpreadOutIsNormalModification f x)
    (hdescend : SpreadOutVanishingDescends f x) :
    DefinesRationalSingularity ↥(X.presheaf.stalk x)
```

**`AlgebraicGeometry.definesRationalSingularity_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LocalBirationalExtensionsRational.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/LocalBirationalExtensionsRational.lean#L90).

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

**`AlgebraicGeometry.exists_normalizedBlowUpSeq_definesRationalSingularity_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedBlowUpRationalSingularity.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedBlowUpRationalSingularity.lean#L289). The attribute's comment: “the whole conclusion — the sequence, its normality, its being a modification, its H-projectivity, and the rational singularity of the local ring at every closed point — over five named hypotheses, none of them this tag. `LerayFirstCohomologyExact` is the first conclusion of Tag 0AXF, the Leray short exact sequence, absent from this development because its right-hand exactness rests on Tag 02V7 in fibre dimension one and hence on Tags 02OD and 02O5. `FlatBaseChangeFirstCohomologyVanishing` is Tag 02KH for the first higher direct image, carried here only in degree zero or as a vanishing criterion for projective space. `BlowUpIsQuasiProjective` is Tag 02NS, whose missing content is part (2), relative ampleness of the twist, carried here only over an unconstructed twist-transition datum, Tag 01NO. `NormalModificationIsIsoAwayFromClosedPoint` and `SpreadOutIsNormalModificationOverSpec` are the isomorphism halves of the hypotheses `ModificationIsFinitePresentationAway` and `SpreadOutIsNormalModification` of `definesRationalSingularity_stalk`, quantified over the base: Tag 0AB7 at the punctured spectrum of a two-dimensional normal local ring, and Step 4 of the source's proof of Tag 0BG0. Proved: Step 1, the domination of Tag 0BBT, the maximality transfer, the spreading out of Tag 0B3X, the third conclusion of Tag 0AXF, and the entire projectivity clause”.

> **Stacks Project, Tag 0B4P.**  Let `A` be a local normal Nagata domain of dimension two for
> which reduction to rational singularities is possible.  Then there is a finite sequence of
> normalized blowups at closed points `X = Xₙ → ⋯ → X₁ → X₀ = Spec(A)` whose total space `X` is
> normal, whose structure morphism is a projective modification, and such that the local ring of
> `X` at every closed point defines a rational singularity.
>
> What is proved here is the shape of the source's argument.  Step 1 is
> `AlgebraicGeometry.exists_maximal_length_normal_modification`; Step 2 replaces the maximal
> modification by a sequence of normalized blowups dominating it, which is Tag 0BBT in the form
> `AlgebraicGeometry.exists_normalizedBlowUpSeq_isModification_dominating`, and the replacement
> stays maximal because the first cohomology injects along the domination.  Step 3 fixes a closed
> point `x` of the sequence and a normal modification `Y ⟶ Spec 𝒪_{X, x}`, spreads it out to a
> proper `g : X' ⟶ X` which is an isomorphism away from `x` — Tag 0B3X, available unconditionally
> as `AlgebraicGeometry.exists_isPullback_fromSpecStalk_of_isProper` — and concludes from
> maximality that the Leray map `H¹(X, 𝒪_X) ⟶ H¹(X', 𝒪_{X'})` is onto, so that `R¹g_*𝒪_{X'}` has
> no global sections; being generated by global sections, by the third conclusion of Tag 0AXF, it
> vanishes, and flat base change carries the vanishing to `Y`.  The projectivity clause is proved
> in full from the carried Tag 02NS, through the H-forms of Tags 0BCL (2), 087S (2) and 01WE, all
> of which are unconditional here.

```lean
public theorem exists_normalizedBlowUpSeq_definesRationalSingularity_stalk
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNormalDomain A]
    (hNagata : IsNagataRing A) (hdim : ringKrullDim A = 2)
    (hReduction : IsReductionToRationalSingularitiesPossible A)
    (h0AXF : LerayFirstCohomologyExact A)
    (h02KH : FlatBaseChangeFirstCohomologyVanishing.{u})
    (h02NS : BlowUpIsQuasiProjective.{u})
    (h0AB7 : NormalModificationIsIsoAwayFromClosedPoint A)
    (hStep4 : SpreadOutIsNormalModificationOverSpec A) :
    ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) (hX : IsNormal X),
      letI := hX
      NormalizedBlowUpSeq (Spec (.of A)) X f ∧ IsModification f ∧
        IsProjectiveMorphism f ∧
        ∀ x : X, IsClosed ({x} : Set X) →
          DefinesRationalSingularity (X.presheaf.stalk x)
```

**`AlgebraicGeometry.exists_normalizedBlowUpSeq_definesRationalSingularity_stalk_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedPointBlowupRationalSingularity.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedPointBlowupRationalSingularity.lean#L99).

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

**`Stacks.ResolutionOfSurfaces.isReductionToRationalSingularitiesPossible_of_finite_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/FiniteSeparableExtension.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/FiniteSeparableExtension.lean#L67).

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

**`AlgebraicGeometry.SeparableGoUp.isReductionToRationalSingularitiesPossible_of_finite_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/SeparableGoUpTransfer.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/SeparableGoUpTransfer.lean#L103).

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

**`AlgebraicGeometry.definesRationalSingularity_of_isRegularLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRing.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRing.lean#L194). The attribute's comment: “granted Tag 0AHI with the regularity of Tag 0AGR and the normality of Tag 0567, carried as `dominate`; the exact sequence of Tag 0AXF, carried as `transfer`; and Tag 0AGS with that exact sequence, carried as `blowUpStep`”.

> **Stacks Project, Tag 0B4Q.** A Nagata regular local ring `A` of dimension two defines a
> rational singularity: the first cohomology of the structure sheaf vanishes on every modification
> of `Spec(A)` with normal source.
>
> Three inputs of the source's proof are carried as hypotheses. `dominate` is [Stacks, Tag 0AHI],
> that every such modification is dominated by a sequence of blowups at closed points over the
> closed point of `Spec(A)`, together with the regularity of the members of that sequence
> ([Stacks, Tag 0AGR]) and their consequent normality ([Stacks, Tag 0567]). `transfer` is the
> injectivity of `H¹(X, 𝒪_X) → H¹(X', 𝒪_{X'})` along a dominating normal modification, the first
> conclusion of [Stacks, Tag 0AXF]. `blowUpStep` is the survival of the vanishing across a single
> blowup at a closed point, which the source gets from [Stacks, Tag 0AGS] and the same exact
> sequence of Tag 0AXF.
>
> What is proved is the rest: the vanishing at the start of the sequence, its propagation along
> the whole sequence, and the descent of the vanishing from the dominating sequence to the given
> modification.

```lean
theorem definesRationalSingularity_of_isRegularLocalRing (A : Type u) [CommRing A] [IsDomain A]
    [IsRegularLocalRing A] [IsNagataRing A] (_hdim : ringKrullDim A = 2)
    (dominate : ∀ (X : Scheme.{u}), IsNormal X → ∀ f : X ⟶ Spec (.of A), IsModification f →
      ∃ (Y : Scheme.{u}) (p : Y ⟶ Spec (.of A)) (g : Y ⟶ X),
        PointBlowupChain (Spec (.of A)) {IsLocalRing.closedPoint A} Y p ∧
          IsNormal Y ∧ IsModification p ∧ g ≫ f = p)
    (transfer : ∀ (X Y : Scheme.{u}) (f : X ⟶ Spec (.of A)) (p : Y ⟶ Spec (.of A)) (g : Y ⟶ X),
      IsNormal X → IsNormal Y → IsModification f → IsModification p → g ≫ f = p →
        FirstStructureSheafCohomologyVanishes Y → FirstStructureSheafCohomologyVanishes X)
    (blowUpStep : ∀ (W : Scheme.{u}) (h : W ⟶ Spec (.of A)),
      PointBlowupChain (Spec (.of A)) {IsLocalRing.closedPoint A} W h →
      ∀ (w : W) (hw : IsClosed ({w} : Set W)),
        FirstStructureSheafCohomologyVanishes W →
        FirstStructureSheafCohomologyVanishes
          (blowUp (Scheme.IdealSheafData.vanishingIdeal ⟨{w}, hw⟩))) :
    DefinesRationalSingularity A
```

**`AlgebraicGeometry.definesRationalSingularity_of_isRegularLocalRing_of_ringKrullDim_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRingDefinesRational.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRingDefinesRational.lean#L148).

> **Stacks Project, Tag 0B4Q.** A Nagata regular local ring of dimension two defines a rational
> singularity.

```lean
theorem definesRationalSingularity_of_isRegularLocalRing_of_ringKrullDim_eq_two (A : Type u)
    [CommRing A] [IsRegularLocalRing A] [IsNagataRing A] (hdim : ringKrullDim A = 2) :
    letI := IsRegularLocalRing.isDomain A; DefinesRationalSingularity A
```

**`AlgebraicGeometry.definesRationalSingularity_of_isRegularLocalRing_of_isNagataRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRingRational.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/RegularLocalRingRational.lean#L289).

> **Stacks Project, Tag 0B4Q.** A Nagata regular local ring `A` of dimension two defines a
> rational singularity: `H¹(X, 𝒪_X) = 0` for every modification `X ⟶ Spec(A)` with `X` normal.
> (A regular local ring is a domain, which `DefinesRationalSingularity` needs as an instance; it is
> supplied by `IsRegularLocalRing.isDomain`.)
>
> The modification is dominated by a chain of normalized blowups at closed points
> ([Stacks, Tag 0BBT], which uses the Nagata hypothesis); along the chain every scheme is regular
> with two-dimensional local rings at its closed points and has `H¹(𝒪) = 0`
> (`AlgebraicGeometry.normalizedBlowUpChain_invariant`), and `H¹(X, 𝒪_X)` embeds into the
> cohomology of the dominating scheme ([Stacks, Tag 0AXF]).

```lean
theorem definesRationalSingularity_of_isRegularLocalRing_of_isNagataRing (A : Type u)
    [CommRing A] [IsRegularLocalRing A] [IsNagataRing A] (hdim : ringKrullDim A = 2) :
    @DefinesRationalSingularity A _ (IsRegularLocalRing.isDomain A)
```

## Tag 0B4S, a lemma

[Tag 0B4S](https://stacks.math.columbia.edu/tag/0B4S) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.isReductionToRationalSingularitiesPossible_of_smul_baseTraceCokernel_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/TraceCokernelImageLift.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/TraceCokernelImageLift.lean#L362). The attribute's comment: “reduction to rational singularities for a two-dimensional local normal Nagata domain with a normalized dualizing complex, from a nonzero element annihilating the cokernel of the trace map of every normal modification; the trace is Stacks.Duality.baseTrace, the trace of Tag 0AWG over the affine base, read on H^\{-2}, whose source is the global sections of the normalized dualizing module of X by homologyNegTwoDerivedGlobalSectionsIso and whose target is the dualizing module of A by dualizingModule\_eq\_homologyFunctor\_negTwo\_obj; Grauert-Riemenschneider vanishing (Tag 0AXD) is discharged in TraceCokernelVanishingHom.lean and the uniform length bound of Tags 0AXJ and 0AXK upstream”.

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

**`Stacks.ResolutionOfSurfaces.isReductionToRationalSingularitiesPossible_of_smul_traceCokernel_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/TraceCokernelReduction.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/TraceCokernelReduction.lean#L140). The attribute's comment: “reduction to rational singularities from a nonzero element annihilating the cokernel of the trace map of every normal modification; the identification of that cokernel with the Matlis dual of H¹(X, 𝒪\_X) — Grauert–Riemenschneider vanishing (Tag 0AXD) with duality (Tag 0AUE) and local duality (Tag 0AAK) — is the field matlisDualOfCokernel of the hypothesis D, and the uniform bound on the lengths of the cokernels of A ⟶ H⁰(Z, 𝒪\_Z) (Tag 0AXJ) is the hypothesis hbound”.

> **Stacks Project, Tag 0B4S.** Let `A` be a local normal Nagata domain of dimension two with a
> dualizing module `ω_A`. If some nonzero `d ∈ A` annihilates the cokernel of the trace map
> `Γ(X, ω_X) ⟶ ω_A` for every modification `f : X ⟶ Spec A` with `X` normal, then reduction to
> rational singularities is possible for `A`: the `A`-module lengths of `H¹(X, 𝒪_X)` admit a common
> finite bound over all such `X`.
>
> Duality presents the Matlis dual `Hom_A(H¹(X, 𝒪_X), E)` as a quotient of the cokernel of the
> trace — the field `TraceCokernelDuality.matlisDualOfCokernel` of `D` — so `d` annihilates that
> dual, and an injective hull of the residue field being a cogenerator, `d` then annihilates
> `H¹(X, 𝒪_X)` itself. Each `H¹(X, 𝒪_X)` is therefore its own `d`-torsion submodule, and the
> uniform bound `hbound` on the lengths of the cokernels of `A ⟶ H⁰(Z, 𝒪_Z)`, for `Z ⊂ X` cut out
> by `d`, bounds their lengths through the identification [Stacks, Tag 0AXK].

```lean
theorem isReductionToRationalSingularitiesPossible_of_smul_traceCokernel_eq_zero
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNormalDomain A] [IsNagataRing A]
    (_hdim : ringKrullDim A = 2)
    (E : ModuleCat.{u} A) (i : Dualizing.residueFieldModule.{u, u} A ⟶ E) [Mono i]
    (hi : Module.IsInjectiveHull i)
    (ωA : ModuleCat.{u} A) (_hωA : Stacks.Duality.IsDualizingRingModule A ωA)
    (D : TraceCokernelDuality A E ωA) (d : A) (hd : d ≠ 0)
    (hcoker : ∀ (X : Scheme.{u}) [IsNormal X] (f : X ⟶ Spec (.of A)), IsModification f →
      ∀ z : ↥ωA ⧸ LinearMap.range (D.trace X f).hom, d • z = 0)
    (hbound : ∃ N : ℕ, ∀ (X : Scheme.{u}) [IsNormal X] (f : X ⟶ Spec (.of A)),
      IsModification f →
      Module.length A (globalSectionsAsBaseModule X f (zeroSchemeStructureSheaf X f d) ⧸
        LinearMap.range (baseToZeroSchemeSections X f d)) ≤ N) :
    IsReductionToRationalSingularitiesPossible A
```

## Tag 0B4T, a lemma

[Tag 0B4T](https://stacks.math.columbia.edu/tag/0B4T) in the Stacks Project.

**`Stacks.BlowupTwistUnit.exists_extendsIdentification_hullForms_chainDualizingOfTopForms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BlowupTwistUnit/ChainTopFormDataRegularLocal.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BlowupTwistUnit/ChainTopFormDataRegularLocal.lean#L336). The attribute's comment: “the map phi\_X from the reflexive hull of the top relative differential forms to the dualizing module omega\_X normalized relative to omega\_A, extending the given identification at the generic point, for every sequence of blowups in closed points of a regular local base of dimension two. The family omega\_X is constructed, not a parameter: it is H^\{-2} of the twisted inverse image of the explicit complex Omega^r in degree -2, so the identification omega\_A = Omega^r\_\{A/A\_0} of the tag's definition of omega\_A is proved (baseIsoOfTopForms) from the invertibility of the top forms of a free module of rank r and the triviality of an invertible module on the spectrum of a local ring, and the normalization omega\_\{X'} = b^! omega\_X of Section 0AU3 is proved from the Gorenstein property of Tag 0AWX. The two-dimensionality of the local rings at the centres is derived too, from properness of the sequence over the local base. The direct-image computation of Tags 0AGS, 0B4L and 0B3T is derived, and as a morphism rather than the isomorphism the source's proof asserts, which is false”.

> **Stacks Project, Tag 0B4T.** Let `A` be a regular local ring of dimension two and `A₀ ⊆ A` a
> subring with `Ω_{A/A₀}` free of rank `r`, and set `ω_A = Ω^r_{A/A₀}`. If `X → Spec A` is the
> result of a sequence of blowups in closed points then there is a map
>
> `φ_X : (Ω^r_{X/Spec A₀})^{**} ⟶ ω_X`
>
> extending the given identification in the generic point, where `ω_X` is the dualizing module of
> `X` normalized relative to `ω_A`.
>
> Everything the symbol `ω_X` denotes is *constructed* here, not assumed. The family is
> `Stacks.BlowupTwistUnit.chainDualizingModuleOfTopForms`, that is `H^{-2}(f^!ω_S^•)` for the
> explicit complex `ω_S^• = Ω^r_{S/S₀}` in degree `-2`; the identification `ω_A = Ω^r_{A/A₀}` is
> `Stacks.BlowupTwistUnit.baseIsoOfTopForms`, proved from the invertibility of the top forms of a
> free module of rank `r` and the triviality of an invertible module on the spectrum of a local
> ring; and the normalization `ω_{X'} = b^!ω_X` of [Stacks, Section 0AU3] is
> `Stacks.BlowupTwistUnit.normalizedChainDualizingModule`, which consumes the fact that `A` being
> Gorenstein makes `ω_A` a dualizing module ([Stacks, Tag 0AWX]). So the hypotheses below are the
> tag's own: `S` is an integral regular surface whose ring of global sections is a regular local
> ring of dimension two and `Ω_{S/S₀}` is coherent and free of rank `r`. That the centres have
> two-dimensional local rings is *derived*, by
> `Stacks.BlowupTwistUnit.ringKrullDim_stalk_eq_two_of_pointBlowupChain`.
>
> The extension clause is `Stacks.BlowupTwistUnit.ChainTopFormData.ExtendsIdentification`, pinned
> rigidly by `Stacks.BlowupTwistUnit.ChainTopFormData.eq_baseHom_of_toReflexiveHull_comp` and
> `Stacks.BlowupTwistUnit.ChainTopFormData.eq_step_of_stepDualityEquiv`, and the direct-image
> comparison the induction consumes is the *morphism*
> `Stacks.BlowupTwistUnit.ChainTopFormData.pushforwardHom`, derived rather than assumed — the
> isomorphism the source's proof asserts there is false, an erratum to the Stacks Project.
>
> *The placeholder reading.* The dependency scan reports a placeholder constant for this
> declaration, inherited from upstream and not from anything written here. The chain runs
> `ChainTopFormData.ofTopForms` to `Stacks.BlowupTwistUnit.normalizedChainDualizingModule` to
> `Stacks.Duality.relativeDualizingComplexIsoShiftTwoOfIsNormalSurface` to
> `Stacks.Duality.hasTopCharts_relativeDualizingComplex` to `Stacks.Duality.upperShriek` to
> `Stacks.Duality.quasiCoherentDerivedPullback'` to `AlgebraicGeometry.affinePullbackComparison`,
> and stops at `AlgebraicGeometry.isLeftDerivedFunctor_extendScalarsTilde`
> (`StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePullbackComparison.lean:279`) and its
> sibling `AlgebraicGeometry.isLeftDerivedFunctor_tildeDerivedPullback` (same file, `:299`).
>
> Those two are where the constant enters, and it enters during elaboration: of the 7602
> declarations in the 499 library modules of that file's import closure, exactly four carry the
> reading and all four are declared in that one file, while every dependency they name is clean.
> The file checks with no errors and no warnings, so nothing is reported, and no file on the chain
> contains a placeholder at a code position. This repository documents the same silent taint of
> typeclass synthesis at
> `StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHomLeftExact.lean:456`,
> `StacksFrontier/Homology/Tor/Presentation.lean:372` and four other sites, the second with the
> instance pinned by hand to avoid it.
>
> The explanation is *not* the `import all` at `StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePullbackComparison.lean:9`: the `private`
> lemma it reaches, `CochainComplex.DerivedExtensionScalars.isLeftDerivedFunctor_of_isIso_on_kFlat`
> (`StacksFrontier/Homology/Tor/DerivedExtensionScalars.lean:893`), is clean, as are the other
> eighteen `private` declarations of that module; and
> `StacksFrontier/AlgebraicGeometry/Perfect/RelativeDescentStandardModel.lean` carries the same
> `import all`, names the same lemma in the same proof shape, and is clean. The two files differ in
> which derived-category model they read, which is where a fix should be looked for.

```lean
theorem exists_extendsIdentification_hullForms_chainDualizingOfTopForms
    (hS : IsIntegralRegularSurface S) (T : Set S) (p : S ⟶ S₀) (r : ℕ)
    [(Scheme.Hom.relativeDifferentials p).IsCoherent]
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (Scheme.Hom.relativeDifferentials p) r]
    (hdimA : ringKrullDim Γ(S, ⊤) = 2)
    {X : Scheme.{u}} {f : X ⟶ S} (hf : PointBlowupChain S T X f) :
    ∃ φ : hullForms p (r : ℤ) f ⟶ chainDualizingModuleOfTopForms hS T p r X f,
      (ChainTopFormData.ofTopForms hS T p r hdimA).ExtendsIdentification hf φ
```

**`Stacks.ResolutionOfSurfaces.exists_extendsIdentification_hom_reflexiveHull_dualizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/TopDifferentialsToDualizing.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/TopDifferentialsToDualizing.lean#L318). The attribute's comment: “the map extending the given identification at the generic point, by induction along the sequence of blowups; the invertible dualizing modules of Tags 0B4R and 0AGR and the Gorenstein property of Tag 0AWX enter as the parameter `ω` together with the field `baseIso`, the duality isomorphism `ω_{X'} = b^!ω_X` of Section 0AU3 as the field `dualityEquiv`, and the computation `b_*(Ω^r_{X'})^{**} = (Ω^r_X)^{**}` of Tags 0AGS, 0B4L and 0B3T as the field `pushforwardIso`, all of `BlowupDualizingData`”.

> **Stacks Project, Tag 0B4T.** Let `A` be a regular local ring of dimension two and `A₀ ⊆ A` a
> subring with `Ω_{A/A₀}` free of rank `r`, so that `ω_A = Ω^r_{A/A₀}` is invertible and, `A` being
> Gorenstein, dualizing. If `X → Spec A` is the result of a sequence of blowups in closed points
> then there is a map
>
> `φ_X : (Ω^r_{X/Spec A₀})^{**} ⟶ ω_X`
>
> extending the given identification in the generic point. The extension clause is
> `BlowupDualizingData.ExtendsIdentification`: `φ_X` descends along the sequence, by the duality
> isomorphism of each blowup and the direct-image identification of the top forms, to the map on
> `Spec A` restricting to `baseIso.inv` along `Ω^r_{A/A₀} ⟶ (Ω^r_{A/A₀})^{**}`. By
> `eq_baseHom_of_toReflexiveHull_comp` and `eq_step_of_dualityEquiv` that pins `φ_X` uniquely at
> every stage, so the conclusion is not inhabited by an arbitrary morphism.
>
> The proof is the induction of the source: the bottom stage is `baseHom`, anchored by
> `toReflexiveHull_comp_baseHom`, and one blowup is `step`, whose correspondence to the previous
> stage is `dualityEquiv_step`.

```lean
public theorem exists_extendsIdentification_hom_reflexiveHull_dualizing {S₀ S : Scheme.{u}}
    {p : S ⟶ S₀} {n : ℤ} {ω : (W : Scheme.{u}) → (W ⟶ S) → W.Modules}
    (D : BlowupDualizingData p n ω)
    {T : Set S} {X : Scheme.{u}} {f : X ⟶ S} (hf : PointBlowupChain S T X f) :
    ∃ φ : reflexiveHull (Scheme.Hom.relativeDifferentialForms (f ≫ p) n) ⟶ ω X f,
      D.ExtendsIdentification φ
```

## Tag 0B4U, a lemma

[Tag 0B4U](https://stacks.math.columbia.edu/tag/0B4U) in the Stacks Project.

**`AlgebraicGeometry.SeparableGoUp.isReductionToRationalSingularitiesPossible_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/InseparableReductionAssembly.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Boundedness/InseparableReductionAssembly.lean#L43).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
