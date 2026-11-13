---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsUnramified, AlgebraicGeometry.Space.IsGUnramified, AlgebraicGeometry.Space.IsUnramifiedAt, AlgebraicGeometry.Space.IsGUnramifiedAt, AlgebraicGeometry.Space.isGUnramified_iff_isUnramified_and_isLocallyOfFinitePresentation, AlgebraicGeometry.Space.isUnramified_comp, AlgebraicGeometry.Space.isUnramified_isStableUnderBaseChange, AlgebraicGeometry.Space.isUnramified_tfae
statement: formalized
proof: formalized
---

# 67.38 Unramified morphisms

Section 67.38 of the Stacks Project, [Tag 03ZG](https://stacks.math.columbia.edu/tag/03ZG). 11 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03ZH, a definition

[Tag 03ZH](https://stacks.math.columbia.edu/tag/03ZH) in the Stacks Project.

**`AlgebraicGeometry.Space.IsUnramified`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean#L124). The attribute's comment: “part (1): unramified morphisms”.

> **Stacks 03ZH, part (1).** A morphism of algebraic spaces over `S` is *unramified* when the
> scheme morphism in every commuting square of étale scheme charts is unramified.

```lean
abbrev IsUnramified (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsGUnramified`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean#L131). The attribute's comment: “part (3): G-unramified morphisms”.

> **Stacks 03ZH, part (3).** A morphism of algebraic spaces over `S` is *G-unramified* when the
> scheme morphism in every commuting square of étale scheme charts is G-unramified.

```lean
abbrev IsGUnramified (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsUnramifiedAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean#L139). The attribute's comment: “part (2): unramified at a point”.

> **Stacks 03ZH, part (2).** A morphism of algebraic spaces over `S` is *unramified at* a point
> `x` of its source when it is unramified on some open subspace of the source having a point
> over `x`.

```lean
abbrev IsUnramifiedAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

**`AlgebraicGeometry.Space.IsGUnramifiedAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean#L148). The attribute's comment: “part (4): G-unramified at a point”.

> **Stacks 03ZH, part (4).** A morphism of algebraic spaces over `S` is *G-unramified at* a
> point `x` of its source when it is G-unramified on some open subspace of the source having a
> point over `x`.

```lean
abbrev IsGUnramifiedAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

## Tag 04G1, a lemma

[Tag 04G1](https://stacks.math.columbia.edu/tag/04G1) in the Stacks Project.

**`AlgebraicGeometry.Space.isGUnramified_iff_isUnramified_and_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L274).

> **Stacks 04G1.** A morphism of algebraic spaces over `S` is G-unramified exactly when it
> is unramified and locally of finite presentation.
>
> All three properties are conditions on every commuting square of étale charts, so the
> statement is the scheme-level equivalence
> `AlgebraicGeometry.gUnramified_iff_unramified_and_locallyOfFinitePresentation` quantified over
> the charts, together with the distribution of a universal quantifier over a conjunction.

```lean
theorem isGUnramified_iff_isUnramified_and_isLocallyOfFinitePresentation (f : X ⟶ Y) :
    IsGUnramified B S hS f ↔
      (IsUnramified B S hS f ∧ IsLocallyOfFinitePresentation B S hS f)
```

## Tag 03ZI, a lemma

[Tag 03ZI](https://stacks.math.columbia.edu/tag/03ZI) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L165).

> **Stacks 03ZI.** The composite of two unramified morphisms of algebraic spaces over `S`
> is unramified.
>
> Unramifiedness of scheme morphisms is étale local on the source and target and stable under
> composition, so this is the instance of [Stacks Project, Tag 0AML] at that property.

```lean
theorem isUnramified_comp (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsUnramified B S hS f) (hg : IsUnramified B S hS g) :
    IsUnramified B S hS (f ≫ g)
```

## Tag 03ZJ, a lemma

[Tag 03ZJ](https://stacks.math.columbia.edu/tag/03ZJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L188). References: SGA 1 I (3.5), “(iii)”.

> **Stacks 03ZJ.** Unramified morphisms of algebraic spaces over `S` are stable under base
> change.
>
> Unramifiedness of scheme morphisms is étale local on the source and target and stable under
> base change, so this is the instance of [Stacks Project, Tag 0AMM] at that property.

```lean
theorem isUnramified_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsUnramified B S hS f.hom)
```

## Tag 03ZK, a lemma

[Tag 03ZK](https://stacks.math.columbia.edu/tag/03ZK) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L578).

> **Stacks 03ZK.** Nine criteria for a morphism of algebraic spaces over `S` to be
> unramified: pointwise unramifiedness, unramifiedness of every base change to a scheme or to an
> affine scheme or to one surjective étale chart of the target, unramifiedness of the composite
> with one surjective étale chart of the source, unramifiedness of the morphism of schemes in
> every — or in one surjective — commuting square of étale charts, or over a pair of Zariski
> coverings.
>
> Unramifiedness of morphisms of schemes is étale local on the source and target
> ([Stacks Project, Tag 04R3]), stable under composition ([Stacks Project, Tag 02G9]) and under
> base change ([Stacks Project, Tag 02GA]), and implied by étaleness, so this is the instance of
> `AlgebraicGeometry.Space.holdsOnEveryEtaleChart_tfae` — Stacks 03MM for an arbitrary such
> property — at that property. Condition (2) is `AlgebraicGeometry.Space.IsUnramifiedAt`, which
> is by definition condition (2) of that theorem.

```lean
theorem isUnramified_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE [
      IsUnramified B S hS f,
      ∀ x : points B S hS X, IsUnramifiedAt B S hS f x,
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsUnramified B S hS (pullback.fst g f),
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) → IsUnramified B S hS (pullback.fst g f),
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧ IsEtale B S hS g ∧ IsUnramified B S hS (pullback.fst g f),
      ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X),
        IsSurjective B S hS p ∧ IsEtale B S hS p ∧ IsUnramified B S hS (p ≫ f),
      ∀ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p → IsEtale B S hS q → p ≫ f = yoneda.map a ≫ q →
          IsUnramified B S hS (yoneda.map a),
      ∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p ∧ IsEtale B S hS q ∧ IsSurjective B S hS p ∧
          p ≫ f = yoneda.map a ≫ q ∧ IsUnramified B S hS (yoneda.map a),
      ∃ (I : Type u) (Yopen : I → Subfunctor Y) (J : I → Type u)
        (Xopen : ∀ i, J i → Subfunctor (pullback f (Yopen i).ι)),
        IsZariskiCover B S hS I Yopen ∧ (∀ i, IsZariskiCover B S hS (J i) (Xopen i)) ∧
          ∀ i j, IsUnramified B S hS ((Xopen i j).ι ≫ pullback.snd f (Yopen i).ι)
    ]
```

## Tag 05VZ, a lemma

[Tag 05VZ](https://stacks.math.columbia.edu/tag/05VZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Unramified.lean#L194).

> **Stacks 05VZ.** An unramified morphism of algebraic spaces is locally of finite type. In
> every étale chart the underlying scheme morphism is unramified, hence locally of finite type by
> `AlgebraicGeometry.locallyOfFiniteType_of_unramified`.
>
> This is also the local-finite-type half of the implication (1) ⇒ (3) of
> [Stacks Project, Tag 05W6].

```lean
theorem isLocallyOfFiniteType_of_isUnramified {f : X ⟶ Y} (hf : IsUnramified B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 05W0, a lemma

[Tag 05W0](https://stacks.math.columbia.edu/tag/05W0) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiFiniteAt_of_isUnramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L295). The attribute's comment: “pointwise statement”.

> **Stacks 05W0**, the pointwise statement: a morphism of algebraic spaces over `S` which is
> unramified at a point of its source is quasi-finite at that point.
>
> The open subspace witnessing unramifiedness at the point witnesses quasi-finiteness there, by
> the global statement applied to the restriction of the morphism.

```lean
theorem isQuasiFiniteAt_of_isUnramifiedAt {f : X ⟶ Y} {x : points B S hS X}
    (hf : IsUnramifiedAt B S hS f x) : IsQuasiFiniteAt B S hS f x
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedQuasiFinite.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedQuasiFinite.lean#L68). The attribute's comment: “global consequence”. References: EGA IV (17.4.3).

> **Stacks 05W0, the global consequence.** An unramified morphism of algebraic spaces over `S`
> is locally quasi-finite: on every commuting square of étale scheme charts the induced scheme
> morphism is unramified, hence locally of finite type and locally quasi-finite.

```lean
theorem isLocallyQuasiFinite_of_isUnramified {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (h : IsUnramified B S hS f) :
    IsLocallyQuasiFinite B S hS f
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedQuasiFinite.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedQuasiFinite.lean#L68). The attribute's comment: “an unramified morphism is locally quasi-finite”. References: EGA IV (17.4.3).

> **Stacks 05W0, the global consequence.** An unramified morphism of algebraic spaces over `S`
> is locally quasi-finite: on every commuting square of étale scheme charts the induced scheme
> morphism is unramified, hence locally of finite type and locally quasi-finite.

```lean
theorem isLocallyQuasiFinite_of_isUnramified {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (h : IsUnramified B S hS f) :
    IsLocallyQuasiFinite B S hS f
```

## Tag 06CQ, a lemma

[Tag 06CQ](https://stacks.math.columbia.edu/tag/06CQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L232).

> **Stacks 06CQ.** An immersion of algebraic spaces over `S` is unramified.
>
> An immersion is representable, so an atlas `b` of the target pulls back to a surjective étale
> chart `a` of the source over an immersion `α` of schemes; `α` is unramified, and that one
> surjective étale square suffices by [Stacks Project, Tag 03MJ].

```lean
theorem isUnramified_of_isImmersion (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y} (hf : IsImmersion B S hS f) :
    IsUnramified B S hS f
```

## Tag 05W1, a lemma

[Tag 05W1](https://stacks.math.columbia.edu/tag/05W1) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_of_isOpenImmersion_pullbackDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L515). The attribute's comment: “part (2)”.

> **Stacks 05W1, part (2).** A morphism of algebraic spaces over `S` which is locally of
> finite type and whose relative diagonal is an open immersion is unramified.
>
> On a commuting square of surjective étale charts the relative diagonal of the morphism `α` of
> the site sits over the relative diagonal of `f`, which is étale after every represented base
> change because it is an open immersion after every such base change. Both legs of that square
> are therefore étale, so the relative diagonal of `α` is étale by
> [Stacks Project, Tag 03FV]; it is also a split monomorphism, hence universally injective, so
> it is an open immersion by [Stacks Project, Tag 02LC]. Now `α` is unramified by
> [Stacks Project, Tag 02GE], and one surjective étale square suffices by
> [Stacks Project, Tag 03MJ].

```lean
theorem isUnramified_of_isOpenImmersion_pullbackDiagonal (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hft : IsLocallyOfFiniteType B S hS f)
    (hdiag : IsOpenImmersion B S hS (pullback.diagonal f)) :
    IsUnramified B S hS f
```

**`AlgebraicGeometry.Space.isOpenImmersion_diagonal_of_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean#L487). The attribute's comment: “part (1)”. References: EGA IV (17.4.2), “a) ⇒ b)”; SGA 1 I (3.4), “diagonal case (g = id)”; SGA 3 XI (1.3), “more general”.

> **Stacks 05W1, part (1).** The relative diagonal of an unramified morphism of algebraic
> spaces over `S` is an open immersion.
>
> Each represented base change of the relative diagonal is a monomorphism of schemes, because
> the relative diagonal is a base change of the absolute diagonal of the source
> (`AlgebraicGeometry.isPullback_pullbackDiagonal_diag`) and the absolute diagonal of an algebraic
> space is a monomorphism after every represented base change
> (`AlgebraicGeometry.Space.monomorphisms_diag_of_representable`, part (2) of
> [Stacks Project, Tag 02X4]). It is moreover étale, which is
> `AlgebraicGeometry.Space.presheaf_etale_diagonal_of_isUnramified`. A morphism of schemes which
> is étale and universally injective — in particular one which is étale and a monomorphism — is
> an open immersion by [Stacks Project, Tag 025G].

```lean
theorem isOpenImmersion_diagonal_of_isUnramified
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsUnramified B S hS f) :
    IsOpenImmersion B S hS (pullback.diagonal f)
```

**`AlgebraicGeometry.Space.isUnramified_of_isOpenImmersion_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean#L524). The attribute's comment: “part (2)”. References: EGA IV (17.4.2), “b) ⇒ a)”; SGA 3 XI (1.3), “more general”.

> **Stacks 05W1, part (2).** A morphism of algebraic spaces over `S` which is locally of
> finite type and whose relative diagonal is an open immersion is unramified.
>
> Let `a : h_U ⟶ X`, `b : h_V ⟶ Y` be étale charts over `h : U ⟶ V`, and let
> `p : h_U ⟶ X ×_Y h_V` be the induced morphism. The morphism `p` is representable, because
> `p` composed with the base change `X ×_Y h_V ⟶ X` of `b` is the representable `a` and
> representability cancels (`CategoryTheory.Functor.relativelyRepresentable.hasOfPostcompProperty`,
> [Stacks Project, Tag 05L9]). Its kernel pair `R` is, by
> `CategoryTheory.Limits.isPullback_kernelPair_diagonal`, a base change of the relative diagonal
> of `f`, so `R ⟶ U ×_V U` is an open immersion by hypothesis.
>
> The relative diagonal `U ⟶ U ×_V U` factors through `R` by a section `σ` of its first
> projection, and it remains to see that `σ` is an open immersion. The relative diagonal
> `d : U ⟶ R_a` of `p` over the kernel pair `R_a` of `a` *is* one: it is a section of the étale
> first projection of `R_a`, hence étale by `AlgebraicGeometry.Etale.of_comp`, and a split
> monomorphism, hence an open immersion by [Stacks Project, Tag 025G]. The comparison
> `e : R ⟶ R_a` is a monomorphism because the two projections of `R` are jointly monic, and
> `σ` is the base change of `d` along `e` — the square `𝟙, σ, d, e` is cartesian because `e` is a
> monomorphism. Composing the two open immersions and transporting along the comparison of the
> fibre product of `h` with itself in the site and in schemes gives that the diagonal of the
> scheme morphism is an open immersion, and part (2) of [Stacks Project, Tag 02GE] concludes.

```lean
theorem isUnramified_of_isOpenImmersion_diagonal (f : X ⟶ Y)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hoi : IsOpenImmersion B S hS (pullback.diagonal f)) :
    IsUnramified B S hS f
```

## Tag 05W2, a lemma

[Tag 05W2](https://stacks.math.columbia.edu/tag/05W2) in the Stacks Project.

**`AlgebraicGeometry.Space.unramifiedLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 644](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L644). The attribute's comment: “part (1): the open unramified locus”.

> **Stacks 05W2, part (1).** The open subspace of the source of a morphism of algebraic
> spaces over `S` cut out by the points at which the morphism is unramified.
>
> Openness of that set of points is `AlgebraicGeometry.Space.isOpen_setOf_isUnramifiedAt`, and
> the open subspace realizing it is produced by the correspondence of part (1) of
> [Stacks Project, Tag 03BZ] between the open subspaces of an algebraic space and the open
> subsets of its point space. No finiteness hypothesis is needed, because unramifiedness at a
> point is stated as the existence of an open subspace on which the morphism is unramified; the
> source's local-finite-type assumption is only used for its part (2).

```lean
noncomputable def unramifiedLocus (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y) :
    {U : Subfunctor X // IsOpenSubspace B S hS U}
```

**`AlgebraicGeometry.Space.range_pointsMap_unramifiedLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 652](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L652). The attribute's comment: “part (1): the points of the open unramified locus”.

> **Stacks 05W2, part (1).** The points of `AlgebraicGeometry.Space.unramifiedLocus` are
> exactly the points at which the morphism is unramified.

```lean
theorem range_pointsMap_unramifiedLocus (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y) :
    Set.range (pointsMap B S hS (unramifiedLocus B S hS hX f).1.toFunctor
        (unramifiedLocus B S hS hX f).1.ι) =
      {x : points B S hS X | IsUnramifiedAt B S hS f x}
```

**`AlgebraicGeometry.Space.isUnramifiedAt_iff_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UnramifiedLocusOnBase.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UnramifiedLocusOnBase.lean#L212). The attribute's comment: “part (2): base-change invariance of the unramified locus, pointwise”.

> **Part (2) of Stacks 05W2, read at a point.** In a cartesian square of algebraic spaces over
> `S` whose right vertical arrow `f` is locally of finite type, the base change `f'` is unramified
> at a point `x'` of its source exactly when `f` is unramified at the image of `x'`; that is,
> forming the unramified locus commutes with base change.
>
> Read on the compatible pointed charts of
> `AlgebraicGeometry.Space.exists_etaleChartAtPoint_pair_of_isPullback`, each side is
> unramifiedness of a morphism of schemes at corresponding points of a cartesian square of
> schemes whose right vertical arrow is locally of finite type.
>
> The source assumes all four corners of the square algebraic; only the three producing the charts
> and the source of the base change are needed, the latter merely to read unramifiedness at a
> point of it off a single chart.

```lean
theorem isUnramifiedAt_iff_of_isPullback {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) (x' : points B S hS X') :
    IsUnramifiedAt B S hS f (pointsMap B S hS X' g' x') ↔ IsUnramifiedAt B S hS f' x'
```

## Tag 06G6, a lemma

[Tag 06G6](https://stacks.math.columbia.edu/tag/06G6) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Unramified.lean#L203).

> **Stacks 06G6.** If a composite of morphisms of algebraic spaces over `S` is unramified,
> then so is its first factor.
>
> Lift a surjective étale atlas of `Z` through `g` and the resulting chart of `Y` through `f`,
> by [Stacks Project, Tag 02X1]. The scheme morphism on top of the outer square is unramified
> by hypothesis, hence so is its first factor by [Stacks Project, Tag 02GG]; that is one
> surjective étale square for `f`, which suffices by [Stacks Project, Tag 03MJ].

```lean
theorem isUnramified_of_comp (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : IsUnramified B S hS (f ≫ g)) : IsUnramified B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.38, Tag 03ZG](https://stacks.math.columbia.edu/tag/03ZG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
