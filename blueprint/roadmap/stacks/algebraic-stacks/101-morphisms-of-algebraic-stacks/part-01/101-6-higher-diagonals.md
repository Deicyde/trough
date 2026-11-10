---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isRelativelyUnramified_relativeInertiaProjection_iff_isDM_unconditional, AlgebraicGeometry.Stack.isLocallyQuasiFinite_relativeInertiaProjection_iff_isQuasiDM_unconditional, AlgebraicGeometry.Stack.isLocallySeparated_relativeInertiaProjection_iff_relativeDiagonal, AlgebraicGeometry.Stack.isLocallySeparated_relativeDiagonal_iff_isImmersion_neutralSection, AlgebraicGeometry.Stack.isSeparated_relativeInertiaProjection_iff_relativeDiagonal, AlgebraicGeometry.Stack.isQuasiSeparated_relativeInertiaProjection_iff_relativeDiagonal, AlgebraicGeometry.Stack.isSeparated_relativeDiagonal_iff_isClosedImmersion_neutralSection, AlgebraicGeometry.Stack.isQuasiSeparated_relativeDiagonal_iff_isQuasiCompact_neutralSection
statement: formalized
proof: formalized
---

# 101.6 Higher diagonals

Section 101.6 of the Stacks Project, [Tag 04YX](https://stacks.math.columbia.edu/tag/04YX). 6 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CL0, a lemma

[Tag 0CL0](https://stacks.math.columbia.edu/tag/0CL0) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRelativelyUnramified_relativeInertiaProjection_iff_isDM_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordRelativeInertiaConverse.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordRelativeInertiaConverse.lean#L356). The attribute's comment: “part (4): the relative inertia projection is unramified iff f is DM, both directions and with no hypothesis. The direction (b) implies (a) is Stacks 0457 and 045C at the packaged unramified property; the converse needs no pseudo-torsor, being an instance of isUnramified\_of\_isUnramified\_pullbackSnd, because the shear identifies the self-fibre-product of a fibre of the relative diagonal with the base change of the relative automorphism presheaf the inertia projection is tested on”.

> **Stacks 0CL0, part (4).** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S`, the
> relative inertia projection `π : I_{𝒳/𝒴} ⟶ 𝒳` is unramified, in the relative sense of
> Properties of Stacks, Section 04XB, exactly when `f` is DM.
>
> The direction (b) ⇒ (a) is
> `AlgebraicGeometry.Stack.isRelativelyUnramified_relativeInertiaProjection_of_isDM` and (a) ⇒ (b)
> is `AlgebraicGeometry.Stack.isDM_of_isRelativelyUnramified_relativeInertiaProjection`; neither
> places any hypothesis on `f`.

```lean
theorem isRelativelyUnramified_relativeInertiaProjection_iff_isDM_unconditional
    (f : 𝒳 ⟶ 𝒴) :
    IsRelativelyUnramified B S hS (relativeInertiaProjection B S hS f).hom ↔ IsDM B S hS f
```

**`AlgebraicGeometry.Stack.isLocallyQuasiFinite_relativeInertiaProjection_iff_isQuasiDM_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordRelativeInertiaConverse.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordRelativeInertiaConverse.lean#L376). The attribute's comment: “part (5): the relative inertia projection is locally quasi-finite iff f is quasi-DM, both directions and with no hypothesis. The direction (b) implies (a) is Stacks 0457 and 045C at the packaged locally-quasi-finite property; the converse is an instance of isLocallyQuasiFinite\_of\_isLocallyQuasiFinite\_pullbackSnd, the generic half of Stacks 0DSK, fed by the shear identification rather than by a pseudo-torsor”.

> **Stacks 0CL0, part (5).** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S`, the
> relative inertia projection `π : I_{𝒳/𝒴} ⟶ 𝒳` is locally quasi-finite, in the relative sense of
> Properties of Stacks, Section 04XB, exactly when `f` is quasi-DM.
>
> The direction (b) ⇒ (a) is
> `AlgebraicGeometry.Stack.isLocallyQuasiFinite_relativeInertiaProjection_of_isQuasiDM` and
> (a) ⇒ (b) is
> `AlgebraicGeometry.Stack.isQuasiDM_of_isLocallyQuasiFinite_relativeInertiaProjection`; neither
> places any hypothesis on `f`. This is the part the proof of **Stacks 0DSN** cites.

```lean
theorem isLocallyQuasiFinite_relativeInertiaProjection_iff_isQuasiDM_unconditional
    (f : 𝒳 ⟶ 𝒴) :
    IsLocallyQuasiFinite B S hS (relativeInertiaProjection B S hS f).hom ↔
      AlgebraicStacks.IsQuasiDM B S hS f
```

**`AlgebraicGeometry.Stack.isLocallySeparated_relativeInertiaProjection_iff_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSeparatednessRelativeInertia.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSeparatednessRelativeInertia.lean#L172). The attribute's comment: “part (3), conditions (a) and (b): the relative diagonal is locally separated exactly when the first projection of the relative inertia is”.

> For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S`, the relative inertia projection
> `π : I_{𝒳/𝒴} ⟶ 𝒳` is locally separated, in the relative sense of Properties of Stacks,
> Section 04XB, exactly when the first relative diagonal `Δ_{f, 1} = Δ_f : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳`
> is.

```lean
theorem isLocallySeparated_relativeInertiaProjection_iff_relativeDiagonal (f : 𝒳 ⟶ 𝒴) :
    IsLocallySeparated B S hS (relativeInertiaProjection B S hS f).hom ↔
      IsLocallySeparated B S hS
        (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom)
```

**`AlgebraicGeometry.Stack.isLocallySeparated_relativeDiagonal_iff_isImmersion_neutralSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SecondRelativeDiagonalInertia.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SecondRelativeDiagonalInertia.lean#L406). The attribute's comment: “part (3), conditions (b) and (c): the relative diagonal is locally separated exactly when the neutral section of the relative inertia is an immersion”.

> For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S`, the relative diagonal
> `Δ_{f, 1} = Δ_f` is locally separated in the sense of Stacks 04XB exactly when
> `Δ_{f, 2} = e : 𝒳 ⟶ I_{𝒳/𝒴}`, the neutral section of the relative inertia, is an immersion of
> algebraic stacks in the sense of part (3) of Stacks 04YL.
>
> This is Stacks 04YU read at `Δ_f` instead of at `f` — whose representability hypothesis is
> automatic there by part (1) of Stacks 04XS — composed with the identification of `Δ_{f, 2}` with
> the neutral section, which is what the source means by "since `Δ_{f, 2}` is the diagonal of
> `Δ_f` we have (b) ⇔ (c) by definition". The transports of the two conjuncts of part (3) of
> Stacks 04YL are `isRepresentableByAlgebraicSpaces_secondRelativeDiagonal_iff_neutralSection`
> and `isImmersion_secondRelativeDiagonal_iff_neutralSection`.

```lean
theorem isLocallySeparated_relativeDiagonal_iff_isImmersion_neutralSection (f : 𝒳 ⟶ 𝒴) :
    IsLocallySeparated B S hS
        (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom) ↔
      AlgebraicStacks.IsImmersion B S hS (relativeInertiaStackNeutralSection B S hS f)
```

**`AlgebraicGeometry.Stack.isSeparated_relativeInertiaProjection_iff_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationRelativeInertia.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparationRelativeInertia.lean#L370). The attribute's comment: “part (1), conditions (a) and (b): the relative inertia projection is separated exactly when the first relative diagonal is”.

> **Stacks 0CL0, part (1), conditions (a) and (b).** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S`, the relative inertia projection `π : I_{𝒳/𝒴} ⟶ 𝒳` is separated, in
> the relative sense of Properties of Stacks, Section 04XB, exactly when the first relative
> diagonal `Δ_{f, 1} = Δ_f : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` is.
>
> Both conditions are first read at the first projection `pr₁` of the 2-fibre product of `Δ_f`
> with itself, by
> `AlgebraicGeometry.Stack.isSeparated_relativeInertiaProjection_iff_twoFibreProductFst`. Then:
>
> * (b) ⇒ (a) is Stacks 045C: `pr₁` is a base change of `Δ_f`, so it inherits separatedness, and
>   no hypothesis on the property is needed.
> * (a) ⇒ (b) is the section argument. `Δ_{f, 2} ≫ pr₁ = 𝟙 𝒳`, so `Δ_{f, 2}` is a section of
>   `pr₁`, and `AlgebraicGeometry.Stack.isClosedImmersion_section_of_isSeparated` — Stacks 04YS at
>   `pr₁`, which is representable by
>   `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_twoFibreProductFst_relativeDiagonal`,
>   followed by the three hypothesis-free transfers — makes `Δ_{f, 2}` a closed immersion.
>   Stacks 04YS read at `Δ_f` instead of at `pr₁` turns that back into separatedness of `Δ_f`.
>
> **Neither direction uses the group law of the relative inertia**, so Groupoids in Spaces,
> Lemma 06P6 — the source's route, and Chapter 78 — is not needed; see the module docstring.
>
> This theorem and
> `AlgebraicGeometry.Stack.isSeparated_relativeDiagonal_iff_isClosedImmersion_neutralSection`,
> which is (b) ⇔ (c), are together the covering set of part (1) of Stacks 0CL0, and both carry
> it.

```lean
theorem isSeparated_relativeInertiaProjection_iff_relativeDiagonal (f : 𝒳 ⟶ 𝒴) :
    IsSeparated B S hS (relativeInertiaProjection B S hS f).hom ↔
      IsSeparated B S hS
        (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom)
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_relativeInertiaProjection_iff_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationRelativeInertia.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparationRelativeInertia.lean#L406). The attribute's comment: “part (2), conditions (a) and (b): the relative inertia projection is quasi-separated exactly when the first relative diagonal is”.

> **Stacks 0CL0, part (2), conditions (a) and (b).** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S`, the relative inertia projection `π : I_{𝒳/𝒴} ⟶ 𝒳` is
> quasi-separated, in the relative sense of Properties of Stacks, Section 04XB, exactly when the
> first relative diagonal `Δ_{f, 1} = Δ_f` is.
>
> The argument is that of
> `AlgebraicGeometry.Stack.isSeparated_relativeInertiaProjection_iff_relativeDiagonal` one step
> down the scale: (b) ⇒ (a) is Stacks 045C at quasi-separatedness, and (a) ⇒ (b) is Stacks 04YT
> at `pr₁` — making the section `Δ_{f, 2}` quasi-compact through
> `AlgebraicGeometry.Stack.isRelativelyQuasiCompact_section_of_isQuasiSeparated` — followed by
> Stacks 04YT read at `Δ_f`.
>
> This theorem and
> `AlgebraicGeometry.Stack.isQuasiSeparated_relativeDiagonal_iff_isQuasiCompact_neutralSection`,
> which is (b) ⇔ (c), are together the covering set of part (2) of Stacks 0CL0, and both carry
> it.

```lean
theorem isQuasiSeparated_relativeInertiaProjection_iff_relativeDiagonal (f : 𝒳 ⟶ 𝒴) :
    IsQuasiSeparated B S hS (relativeInertiaProjection B S hS f).hom ↔
      IsQuasiSeparated B S hS
        (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom)
```

**`AlgebraicGeometry.Stack.isSeparated_relativeDiagonal_iff_isClosedImmersion_neutralSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationRelativeInertia.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparationRelativeInertia.lean#L437). The attribute's comment: “part (1), conditions (b) and (c): the relative diagonal is separated exactly when the neutral section of the relative inertia is a closed immersion”.

> **Stacks 0CL0, part (1), conditions (b) and (c).** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S`, the relative diagonal `Δ_{f, 1} = Δ_f` is separated in the sense of
> Stacks 04XB exactly when `Δ_{f, 2} = e : 𝒳 ⟶ I_{𝒳/𝒴}`, the neutral section of the relative
> inertia, is a closed immersion of algebraic stacks in the sense of part (2) of Stacks 04YL.
>
> This is part (1) of Stacks 04YZ — Stacks 04YS read at `Δ_f`, whose representability hypothesis
> is automatic by part (1) of Stacks 04XS — composed with the identification of `Δ_{f, 2}` with
> the neutral section, which is what the source means by "since `Δ_{f, 2}` is the diagonal of
> `Δ_f` we have (b) ⇔ (c) by definition". The transports of the two conjuncts of part (2) of
> Stacks 04YL are `Stack.isRepresentableByAlgebraicSpaces_secondRelativeDiagonal_iff_neutralSection`
> and `Stack.isClosedImmersion_secondRelativeDiagonal_iff_neutralSection`.

```lean
theorem isSeparated_relativeDiagonal_iff_isClosedImmersion_neutralSection (f : 𝒳 ⟶ 𝒴) :
    IsSeparated B S hS
        (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom) ↔
      AlgebraicStacks.IsClosedImmersion B S hS (relativeInertiaStackNeutralSection B S hS f)
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_relativeDiagonal_iff_isQuasiCompact_neutralSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationRelativeInertia.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparationRelativeInertia.lean#L458). The attribute's comment: “part (2), conditions (b) and (c): the relative diagonal is quasi-separated exactly when the neutral section of the relative inertia is quasi-compact”.

> **Stacks 0CL0, part (2), conditions (b) and (c).** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S`, the relative diagonal `Δ_{f, 1} = Δ_f` is quasi-separated in the
> sense of Stacks 04XB exactly when `Δ_{f, 2} = e : 𝒳 ⟶ I_{𝒳/𝒴}`, the neutral section of the
> relative inertia, is quasi-compact in that sense.
>
> This is part (2) of Stacks 04YZ — Stacks 04YT read at `Δ_f` — composed with
> `AlgebraicGeometry.Stack.isQuasiCompact_secondRelativeDiagonal_iff_neutralSection`. Being
> quasi-compact is not one of the three parts of Stacks 04YL, so unlike condition (1)(c) there is
> no representability conjunct to transport alongside.

```lean
theorem isQuasiSeparated_relativeDiagonal_iff_isQuasiCompact_neutralSection (f : 𝒳 ⟶ 𝒴) :
    IsQuasiSeparated B S hS
        (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom) ↔
      IsQuasiCompact B S hS (relativeInertiaStackNeutralSection B S hS f).hom
```

## Tag 04YY, a lemma

[Tag 04YY](https://stacks.math.columbia.edu/tag/04YY) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_isEquivalence_secondRelativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentableUnconditional.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FaithfulRepresentableUnconditional.lean#L98). The attribute's comment: “the implication (2) ⟹ (1)”.

> **Stacks 04YY, the implication (2) ⟹ (1).** A 1-morphism of algebraic stacks over `S` whose
> second diagonal `Δ_{f, 2}` is an isomorphism is representable by algebraic spaces: the second
> diagonal is an isomorphism exactly when `f` is faithful (Stacks 04Z7), and a faithful 1-morphism
> of algebraic stacks is representable by algebraic spaces (Stacks 04Y5).

```lean
theorem isRepresentableByAlgebraicSpaces_of_isEquivalence_secondRelativeDiagonal (f : 𝒳 ⟶ 𝒴)
    (hf : Functor.IsEquivalence (secondRelativeDiagonal B S hS f.hom).hom.toFunctor) :
    IsRepresentableByAlgebraicSpaces B S hS f.hom.hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableSecondDiagonalTFAE.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableSecondDiagonalTFAE.lean#L54).

> **Stacks 04YY.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following are
> equivalent:
>
> 1. `f` is representable by algebraic spaces;
> 2. the second diagonal `Δ_{f, 2}` is an isomorphism;
> 3. the relative inertia `I_{𝒳/𝒴}` is trivial over `𝒳`, that is, its neutral section
>    `e : 𝒳 ⟶ I_{𝒳/𝒴}` is an isomorphism;
> 4. for every scheme `T` and every `x : T ⟶ 𝒳` the kernel of
>    `Isom_𝒳(x, x) ⟶ Isom_𝒴(f ∘ x, f ∘ x)` is trivial — stated as: every endomorphism of an object
>    of `𝒳` which `f` sends to an identity is an identity.

```lean
theorem isRepresentableByAlgebraicSpaces_tfae (f : 𝒳 ⟶ 𝒴) :
    List.TFAE
      [IsRepresentableByAlgebraicSpaces B S hS f.hom.hom,
        Functor.IsEquivalence (secondRelativeDiagonal B S hS f.hom).hom.toFunctor,
        Functor.IsEquivalence
          (relativeInertiaStackNeutralSection B S hS f).hom.hom.toFunctor,
        ∀ (x : 𝒳.val.val.obj) (a : x ⟶ x),
          (CatFiberedInGroupoids.homFunctor f.hom).map a = 𝟙 _ → a = 𝟙 x]
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEquivalence_secondRelativeDiagonal_iff_relativeInertiaTrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalRepresentable.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalRepresentable.lean#L239). The attribute's comment: “the equivalence of parts (2) and (3)”.

> **Stacks 04YY, the equivalence of parts (2) and (3).** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S`, the second diagonal `Δ_{f, 2}` is an isomorphism exactly when the
> relative inertia group stack `I_{𝒳/𝒴}` is trivial over `𝒳`, that is, exactly when its neutral
> section `e : 𝒳 ⟶ I_{𝒳/𝒴}` is an isomorphism.

```lean
theorem isEquivalence_secondRelativeDiagonal_iff_relativeInertiaTrivial (f : 𝒳 ⟶ 𝒴) :
    Functor.IsEquivalence (secondRelativeDiagonal B S hS f.hom).hom.toFunctor ↔
      Functor.IsEquivalence
        (relativeInertiaStackNeutralSection B S hS f).hom.hom.toFunctor
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.relativeInertiaTrivial_iff_isomKernel_trivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalRepresentable.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalRepresentable.lean#L250). The attribute's comment: “the equivalence of parts (3) and (4)”.

> **Stacks 04YY, the equivalence of parts (3) and (4).** The relative inertia `I_{𝒳/𝒴}` of a
> 1-morphism of algebraic stacks is trivial over `𝒳` exactly when, for every scheme `T` and every
> `x : T ⟶ 𝒳`, the kernel of `Isom_𝒳(x, x) ⟶ Isom_𝒴(f ∘ x, f ∘ x)` is trivial — stated as: every
> endomorphism of an object of `𝒳` which `f` sends to an identity is an identity.

```lean
theorem relativeInertiaTrivial_iff_isomKernel_trivial (f : 𝒳 ⟶ 𝒴) :
    Functor.IsEquivalence
        (relativeInertiaStackNeutralSection B S hS f).hom.hom.toFunctor ↔
      ∀ (x : 𝒳.val.val.obj) (a : x ⟶ x),
        (CatFiberedInGroupoids.homFunctor f.hom).map a = 𝟙 _ → a = 𝟙 x
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.secondRelativeDiagonal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalRepresentable.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalRepresentable.lean#L262). The attribute's comment: “the equivalence of parts (2), (3) and (4)”.

> **Stacks 04YY, the equivalence of parts (2), (3) and (4).** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S` the following are equivalent: the second diagonal `Δ_{f, 2}` is an
> isomorphism; the relative inertia `I_{𝒳/𝒴}` is trivial over `𝒳`; the kernel of the map on
> `Isom` sheaves attached to any object of `𝒳` over a scheme is trivial.

```lean
theorem secondRelativeDiagonal_tfae (f : 𝒳 ⟶ 𝒴) :
    List.TFAE
      [Functor.IsEquivalence (secondRelativeDiagonal B S hS f.hom).hom.toFunctor,
        Functor.IsEquivalence
          (relativeInertiaStackNeutralSection B S hS f).hom.hom.toFunctor,
        ∀ (x : 𝒳.val.val.obj) (a : x ⟶ x),
          (CatFiberedInGroupoids.homFunctor f.hom).map a = 𝟙 _ → a = 𝟙 x]
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEquivalence_secondRelativeDiagonal_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalRepresentable.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SecondDiagonalRepresentable.lean#L280). The attribute's comment: “the implication (1) ⟹ (2)”.

> **Stacks 04YY, the implication (1) ⟹ (2).** If a 1-morphism of algebraic stacks over `S` is
> representable by algebraic spaces then its second diagonal `Δ_{f, 2}` is an isomorphism.
>
> By Stacks 04Y5 representability by algebraic spaces makes the underlying functor faithful, and by
> Stacks 04Z7 that is exactly the second diagonal being an isomorphism.

```lean
theorem isEquivalence_secondRelativeDiagonal_of_isRepresentableByAlgebraicSpaces (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    Functor.IsEquivalence (secondRelativeDiagonal B S hS f.hom).hom.toFunctor
```

## Tag 0AHJ, a lemma

[Tag 0AHJ](https://stacks.math.columbia.edu/tag/0AHJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_iff_isEquivalence_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalMonomorphism.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalMonomorphism.lean#L140). The attribute's comment: “part (1)”.

> **Stacks 0AHJ, part (1).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is a
> monomorphism (Stacks 04ZW) if and only if its first relative diagonal `Δ_{f,1}` is an isomorphism,
> i.e. has underlying functor an equivalence of categories.
>
> Both directions pass through full faithfulness of `f`: Stacks 04Z7 says `Δ_{f,1}` is an
> equivalence exactly when `f` is fully faithful, Stacks 05UK turns the monomorphy clause into full
> faithfulness, and Stacks 04ZZ turns full faithfulness back into the monomorphy clause.
>
> The representability conjunct of `AlgebraicGeometry.Stack.AlgebraicStacks.IsMonomorphism` in
> the "if" direction is the implication (2) ⟹ (3) of **Stacks 04Y5** at `f`.

```lean
theorem isMonomorphism_iff_isEquivalence_relativeDiagonal (f : 𝒳 ⟶ 𝒴) :
    IsMonomorphism B S hS f ↔
      Functor.IsEquivalence
        (CatFiberedInGroupoids.homFunctor (relativeDiagonalAlgebraicStacks B S hS f).hom)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_iff_isMonomorphism_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalMonomorphism.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalMonomorphism.lean#L162). The attribute's comment: “part (2)”.

> **Stacks 0AHJ, part (2).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is
> representable by algebraic spaces if and only if its first relative diagonal `Δ_{f,1}` is a
> monomorphism (Stacks 04ZW).
>
> The "only if" direction is part (3) of Stacks 04YQ. For the converse, Stacks 05UK makes `Δ_{f,1}`
> full, which by Stacks 04Z7 — the content clause (2) of Stacks 04YY reads as `Δ_{f,2}` being an
> isomorphism — makes `f` faithful, and faithfulness is representability by Stacks 04Y5.
>
> That last step, the implication (2) ⟹ (3) of **Stacks 04Y5** at `f`, is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_faithful`.

```lean
theorem isRepresentableByAlgebraicSpaces_iff_isMonomorphism_relativeDiagonal (f : 𝒳 ⟶ 𝒴) :
    IsRepresentableByAlgebraicSpaces B S hS f.hom.hom ↔
      IsMonomorphism B S hS (relativeDiagonalAlgebraicStacks B S hS f)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_secondRelativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalMonomorphism.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalMonomorphism.lean#L178). The attribute's comment: “the second diagonal is always a monomorphism”.

> **Stacks 0AHJ, the final assertion.** The second relative diagonal `Δ_{f,2}` of any
> 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is a monomorphism (Stacks 04ZW). No
> hypothesis on `f` is needed.
>
> This is the "only if" direction of part (2) applied to `Δ_{f,1}`, which is representable by
> algebraic spaces unconditionally by part (1) of Stacks 04XS.

```lean
theorem isMonomorphism_secondRelativeDiagonal (f : 𝒳 ⟶ 𝒴) :
    IsMonomorphism B S hS
      (relativeDiagonalAlgebraicStacks B S hS (relativeDiagonalAlgebraicStacks B S hS f))
```

## Tag 04YZ, a lemma

[Tag 04YZ](https://stacks.math.columbia.edu/tag/04YZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSeparated_firstRelativeDiagonal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalSeparation.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalSeparation.lean#L67). The attribute's comment: “part (1)”.

> For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the
> following are equivalent: the first relative diagonal `Δ_{f,1}` is separated; the second relative
> diagonal `Δ_{f,2}` is a closed immersion, part (2) of Stacks 04YL; `Δ_{f,2}` is proper;
> `Δ_{f,2}` is universally closed — the last two, and the first, in the relative sense of
> Stacks 04XB.

```lean
theorem isSeparated_firstRelativeDiagonal_tfae (f : 𝒳 ⟶ 𝒴) :
    List.TFAE
      [IsSeparated B S hS (relativeDiagonalAlgebraicStacks B S hS f).hom,
       AlgebraicStacks.IsClosedImmersion B S hS
         (relativeDiagonalAlgebraicStacks B S hS (relativeDiagonalAlgebraicStacks B S hS f)),
       IsProper B S hS
         (relativeDiagonalAlgebraicStacks B S hS
           (relativeDiagonalAlgebraicStacks B S hS f)).hom,
       UniversallyClosed B S hS
         (relativeDiagonalAlgebraicStacks B S hS
           (relativeDiagonalAlgebraicStacks B S hS f)).hom]
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_firstRelativeDiagonal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalSeparation.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalSeparation.lean#L86). The attribute's comment: “part (2)”.

> For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the
> following are equivalent: the first relative diagonal `Δ_{f,1}` is quasi-separated; the second
> relative diagonal `Δ_{f,2}` is of finite type; `Δ_{f,2}` is quasi-compact — all three in the
> relative sense of Stacks 04XB.

```lean
theorem isQuasiSeparated_firstRelativeDiagonal_tfae (f : 𝒳 ⟶ 𝒴) :
    List.TFAE
      [IsQuasiSeparated B S hS (relativeDiagonalAlgebraicStacks B S hS f).hom,
       IsFiniteType B S hS
         (relativeDiagonalAlgebraicStacks B S hS
           (relativeDiagonalAlgebraicStacks B S hS f)).hom,
       IsQuasiCompact B S hS
         (relativeDiagonalAlgebraicStacks B S hS
           (relativeDiagonalAlgebraicStacks B S hS f)).hom]
```

**`AlgebraicGeometry.Stack.isLocallySeparated_firstRelativeDiagonal_iff_isImmersion_second`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalSeparation.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/HigherDiagonalSeparation.lean#L111). The attribute's comment: “part (3)”.

> The first relative diagonal `Δ_{f,1}` of a 1-morphism
> `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is locally separated, in the relative sense of
> Stacks 04XB, if and only if the second relative diagonal `Δ_{f,2}` is an immersion, part (3) of
> Stacks 04YL.

```lean
theorem isLocallySeparated_firstRelativeDiagonal_iff_isImmersion_second (f : 𝒳 ⟶ 𝒴) :
    IsLocallySeparated B S hS (relativeDiagonalAlgebraicStacks B S hS f).hom ↔
      AlgebraicStacks.IsImmersion B S hS
        (relativeDiagonalAlgebraicStacks B S hS (relativeDiagonalAlgebraicStacks B S hS f))
```

## Tag 04Z0, a lemma

[Tag 04Z0](https://stacks.math.columbia.edu/tag/04Z0) in the Stacks Project.

**`AlgebraicGeometry.Stack.isDM_iff_isUnramifiedRelative_diagonals`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DMSecondDiagonal.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DMSecondDiagonal.lean#L149). The attribute's comment: “dm”.

> **Stacks 04Z0, part (4).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` — with no
> representability hypothesis — is DM, in the sense of Definition 04YW, if and only if its first
> relative diagonal `Δ_{f,1} : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` and its second relative diagonal `Δ_{f,2}`,
> the relative diagonal of `Δ_{f,1}`, are both unramified in the relative sense of Properties of
> Stacks, Section 04XB.
>
> Definition 04YW is representability of `Δ_{f,1}` by algebraic spaces together with Section 04XB
> unramifiedness of it; the representability clause is a theorem for a 1-morphism of *algebraic*
> stacks — part (1) of Stacks 04XS — so the condition carried here is the Section 04XB clause alone
> and the left-hand side is the first conjunct on the right. The second conjunct is unconditionally
> true, which is the source's own proof: `Δ_{f,2}` is the relative diagonal of `Δ_{f,1}`, which is
> representable by algebraic spaces, so part (3) of Stacks 050E — Stacks 05W6 applied at a diagonal
> which is locally of finite type and a monomorphism by parts (2) and (3) of Stacks 04YQ — makes it
> unramified with no hypothesis on `f`.

```lean
theorem isDM_iff_isUnramifiedRelative_diagonals (f : 𝒳 ⟶ 𝒴) :
    IsDM B S hS f ↔
      (IsUnramifiedRelative B S hS (relativeDiagonalAlgebraicStacks B S hS f).hom ∧
        IsUnramifiedRelative B S hS (relativeDiagonalAlgebraicStacks B S hS
          (relativeDiagonalAlgebraicStacks B S hS f)).hom)
```

**`AlgebraicGeometry.Stack.isQuasiDM_iff_isLocallyQuasiFinite_diagonals`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMSecondDiagonal.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiDMSecondDiagonal.lean#L54). The attribute's comment: “quasi\_dm”.

> A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` — with no representability
> hypothesis — is quasi-DM, in the sense of Definition 04YW, if and only if its first relative
> diagonal `Δ_{f,1} : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` and its second relative diagonal `Δ_{f,2}`, the
> relative diagonal of `Δ_{f,1}`, are both locally quasi-finite in the relative sense of Properties
> of Stacks, Section 04XB.

```lean
theorem isQuasiDM_iff_isLocallyQuasiFinite_diagonals (f : 𝒳 ⟶ 𝒴) :
    AlgebraicStacks.IsQuasiDM B S hS f ↔
      (IsLocallyQuasiFinite B S hS (relativeDiagonalAlgebraicStacks B S hS f).hom ∧
        IsLocallyQuasiFinite B S hS (relativeDiagonalAlgebraicStacks B S hS
          (relativeDiagonalAlgebraicStacks B S hS f)).hom)
```

**`AlgebraicGeometry.Stack.isQuasiSeparated_iff_isQuasiCompactMorphism_diagonals`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedSecondDiagonal.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedSecondDiagonal.lean#L323). The attribute's comment: “quasi\_separated”.

> **Stacks 04Z0, part (2).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` — with no
> representability hypothesis — is quasi-separated, in the sense of Definition 04YW, if and only if
> its first relative diagonal `Δ_{f,1} : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` and its second relative diagonal
> `Δ_{f,2}`, the relative diagonal of `Δ_{f,1}`, are both quasi-compact in the sense of
> Definition 050U.
>
> Definition 04YW is the conjunction, at every algebraic space representing a base change of
> `Δ_{f,1}` along a scheme-valued point, of quasi-compactness and quasi-separatedness of the
> structural morphism, so the left-hand side splits as Section 04XB quasi-compactness of `Δ_{f,1}`
> together with Section 04XB quasi-separatedness of `Δ_{f,1}`. Part (2) of Stacks 04YZ, which is
> `AlgebraicGeometry.Stack.isQuasiCompact_relativeDiagonal_iff_isQuasiSeparated` applied to
> `Δ_{f,1}`, replaces the second of those by Section 04XB quasi-compactness of `Δ_{f,2}`; and
> Stacks 050T, `AlgebraicGeometry.Stack.isQuasiCompact_iff_baseChange_quasiCompact`, replaces
> Section 04XB quasi-compactness of each diagonal by Definition 050U quasi-compactness, which is the
> form the statement asks for. Both diagonals are representable by algebraic spaces by part (1) of
> Stacks 04XS, so neither application needs a hypothesis.

```lean
theorem isQuasiSeparated_iff_isQuasiCompactMorphism_diagonals (f : 𝒳 ⟶ 𝒴) :
    AlgebraicStacks.IsQuasiSeparated B S hS f ↔
      (IsQuasiCompactMorphism B S hS (relativeDiagonalAlgebraicStacks B S hS f) ∧
        IsQuasiCompactMorphism B S hS (relativeDiagonalAlgebraicStacks B S hS
          (relativeDiagonalAlgebraicStacks B S hS f)))
```

**`AlgebraicGeometry.Stack.isSeparated_iff_universallyClosed_diagonals`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedSecondDiagonal.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedSecondDiagonal.lean#L117). The attribute's comment: “separated”.

> **Stacks 04Z0, part (1).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` — with no
> representability hypothesis — is separated, in the sense of Definition 04YW, if and only if its
> first relative diagonal `Δ_{f,1} : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` and its second relative diagonal
> `Δ_{f,2}`, the relative diagonal of `Δ_{f,1}`, are both universally closed in the relative sense
> of Properties of Stacks, Section 04XB.
>
> Definition 04YW is properness of `Δ_{f,1}`, and properness of a morphism of algebraic spaces is
> separatedness, finite type and universal closedness. Universal closedness of `Δ_{f,1}` is the
> first conjunct on the right; its separatedness is universal closedness of `Δ_{f,2}` by part (1)
> of Stacks 04YZ; it is unconditionally locally of finite type by part (2) of Stacks 04XS; and it
> is quasi-compact because it is universally closed, by Stacks 04XW.

```lean
theorem isSeparated_iff_universallyClosed_diagonals (f : 𝒳 ⟶ 𝒴) :
    AlgebraicStacks.IsSeparated B S hS f ↔
      (UniversallyClosed B S hS (relativeDiagonalAlgebraicStacks B S hS f).hom ∧
        UniversallyClosed B S hS (relativeDiagonalAlgebraicStacks B S hS
          (relativeDiagonalAlgebraicStacks B S hS f)).hom)
```

## Tag 0CPL, a lemma

[Tag 0CPL](https://stacks.math.columbia.edu/tag/0CPL) in the Stacks Project.

**`AlgebraicGeometry.Stack.HigherDiagonal.isProper_mapBase_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean#L235). The attribute's comment: “part (1): proper”.

> **Stacks 0CPL, part (1), the separated case.** If `f : 𝒳 ⟶ 𝒴` is separated then the
> comparison `T₁ ×_{x₁, 𝒳, x₂} T₂ ⟶ T₁ ×_{y₁, 𝒴, y₂} T₂` of algebraic-space-valued points of `𝒳`
> is proper, in the sense of Stacks 04XB.
>
> This is Stacks 050H part (6) at a cospan whose two sources are algebraic spaces.

```lean
theorem isProper_mapBase_of_isSeparated (hf : AlgebraicStacks.IsSeparated B S hS f) :
    Stack.IsProper.{u, u, u + 1} B S hS (AlgebraicStacks.mapBase B S hS x₁ x₂ f).hom
```

**`AlgebraicGeometry.Stack.HigherDiagonal.isQuasiCompactAndQuasiSeparated_mapBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean#L245). The attribute's comment: “part (1): quasi-compact and quasi-separated”.

> **Stacks 0CPL, part (1), the quasi-separated case.** If `f : 𝒳 ⟶ 𝒴` is quasi-separated then
> the comparison `T₁ ×_{x₁, 𝒳, x₂} T₂ ⟶ T₁ ×_{y₁, 𝒴, y₂} T₂` of algebraic-space-valued points of
> `𝒳` is quasi-compact and quasi-separated, in the sense of Stacks 04XB.
>
> This is Stacks 050H part (7) at a cospan whose two sources are algebraic spaces.

```lean
theorem isQuasiCompactAndQuasiSeparated_mapBase
    (hf : AlgebraicStacks.IsQuasiSeparated B S hS f) :
    Stack.IsQuasiCompact.{u, u, u + 1} B S hS
        (AlgebraicStacks.mapBase B S hS x₁ x₂ f).hom ∧
      Stack.IsQuasiSeparated.{u, u, u + 1} B S hS
        (AlgebraicStacks.mapBase B S hS x₁ x₂ f).hom
```

**`AlgebraicGeometry.Stack.HigherDiagonal.isLocallyQuasiFinite_mapBase_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean#L259). The attribute's comment: “part (1): locally quasi-finite”.

> **Stacks 0CPL, part (1), the quasi-DM case.** If `f : 𝒳 ⟶ 𝒴` is quasi-DM then the comparison
> `T₁ ×_{x₁, 𝒳, x₂} T₂ ⟶ T₁ ×_{y₁, 𝒴, y₂} T₂` of algebraic-space-valued points of `𝒳` is locally
> quasi-finite, in the sense of Stacks 04XB.
>
> This is Stacks 050H part (5) at a cospan whose two sources are algebraic spaces.

```lean
theorem isLocallyQuasiFinite_mapBase_of_isQuasiDM
    (hf : AlgebraicStacks.IsQuasiDM B S hS f) :
    Stack.IsLocallyQuasiFinite.{u, u, u + 1} B S hS
      (AlgebraicStacks.mapBase B S hS x₁ x₂ f).hom
```

**`AlgebraicGeometry.Stack.HigherDiagonal.isUnramified_mapBase_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean#L271). The attribute's comment: “part (1): unramified”.

> **Stacks 0CPL, part (1), the Deligne–Mumford case.** If `f : 𝒳 ⟶ 𝒴` is Deligne–Mumford then
> the comparison `T₁ ×_{x₁, 𝒳, x₂} T₂ ⟶ T₁ ×_{y₁, 𝒴, y₂} T₂` of algebraic-space-valued points of
> `𝒳` is unramified, in the sense of Stacks 04XB.
>
> This is Stacks 050H part (4) at a cospan whose two sources are algebraic spaces.

```lean
theorem isUnramified_mapBase_of_isDM (hf : Stack.IsDM B S hS f) :
    ∀ (U : BigFppfOver B S hS)
      (z : BigFppfOver B U.left.1 U.left.2 ⥤
        (AlgebraicStacks.twoFibreProduct B S hS (x₁ ≫ f) (x₂ ≫ f)).val.val.obj)
      (_hz : z ⋙ (AlgebraicStacks.twoFibreProduct B S hS (x₁ ≫ f) (x₂ ≫ f)).val.val.p =
        Over.map U.hom)
      (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (AlgebraicStacks.twoFibreProduct B S hS x₁ x₂).val.val.p
            (AlgebraicStacks.twoFibreProduct B S hS (x₁ ≫ f) (x₂ ≫ f)).val.val.p z
            (CatFiberedInGroupoids.homFunctor (AlgebraicStacks.mapBase B S hS x₁ x₂ f).hom))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.IsUnramified B S hS
          (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

**`AlgebraicGeometry.Stack.HigherDiagonal.isProper_isomMap_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean#L445). The attribute's comment: “part (2): proper”.

> **Stacks 0CPL, part (2), the separated case.** If `f : 𝒳 ⟶ 𝒴` is separated then the induced
> map `Isom_𝒳(x₁, x₂) ⟶ Isom_𝒴(y₁, y₂)` is proper, in the sense of Stacks 04XB.

```lean
theorem isProper_isomMap_of_isSeparated (hf : AlgebraicStacks.IsSeparated B S hS f) :
    Stack.IsProper.{u, u, u + 1} B S hS (isomMap B S hS f T hT x₁ x₂)
```

**`AlgebraicGeometry.Stack.HigherDiagonal.isQuasiCompactAndQuasiSeparated_isomMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean#L455). The attribute's comment: “part (2): quasi-compact and quasi-separated”.

> **Stacks 0CPL, part (2), the quasi-separated case.** If `f : 𝒳 ⟶ 𝒴` is quasi-separated then
> the induced map `Isom_𝒳(x₁, x₂) ⟶ Isom_𝒴(y₁, y₂)` is quasi-compact and quasi-separated, in the
> sense of Stacks 04XB.

```lean
theorem isQuasiCompactAndQuasiSeparated_isomMap
    (hf : AlgebraicStacks.IsQuasiSeparated B S hS f) :
    Stack.IsQuasiCompact.{u, u, u + 1} B S hS (isomMap B S hS f T hT x₁ x₂) ∧
      Stack.IsQuasiSeparated.{u, u, u + 1} B S hS (isomMap B S hS f T hT x₁ x₂)
```

**`AlgebraicGeometry.Stack.HigherDiagonal.isLocallyQuasiFinite_isomMap_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean#L469). The attribute's comment: “part (2): locally quasi-finite”.

> **Stacks 0CPL, part (2), the quasi-DM case.** If `f : 𝒳 ⟶ 𝒴` is quasi-DM then the induced
> map `Isom_𝒳(x₁, x₂) ⟶ Isom_𝒴(y₁, y₂)` is locally quasi-finite, in the sense of Stacks 04XB.

```lean
theorem isLocallyQuasiFinite_isomMap_of_isQuasiDM
    (hf : AlgebraicStacks.IsQuasiDM B S hS f) :
    Stack.IsLocallyQuasiFinite.{u, u, u + 1} B S hS (isomMap B S hS f T hT x₁ x₂)
```

**`AlgebraicGeometry.Stack.HigherDiagonal.isUnramified_isomMap_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean#L480). The attribute's comment: “part (2): unramified”.

> **Stacks 0CPL, part (2), the Deligne–Mumford case.** If `f : 𝒳 ⟶ 𝒴` is Deligne–Mumford then
> the induced map `Isom_𝒳(x₁, x₂) ⟶ Isom_𝒴(y₁, y₂)` is unramified, in the sense of
> Stacks 04XB.

```lean
theorem isUnramified_isomMap_of_isDM (hf : Stack.IsDM B S hS f) :
    ∀ (U : BigFppfOver B S hS)
      (z : BigFppfOver B U.left.1 U.left.2 ⥤
        (isomStack B S hS T hT (x₁ ≫ f) (x₂ ≫ f)).val.obj)
      (_hz : z ⋙ (isomStack B S hS T hT (x₁ ≫ f) (x₂ ≫ f)).val.p = Over.map U.hom)
      (G : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hG : IsAlgebraicSpace B U.left.1 U.left.2 G),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (isomStack B S hS T hT x₁ x₂).val.p
            (isomStack B S hS T hT (x₁ ≫ f) (x₂ ≫ f)).val.p z
            (CatFiberedInGroupoids.homFunctor (isomMap B S hS f T hT x₁ x₂)))
          (presheafOfCategories (G ⋙ typeToCat)).p) →
        Space.IsUnramified B S hS
          (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨G, hG⟩)).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.6, Tag 04YX](https://stacks.math.columbia.edu/tag/04YX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
