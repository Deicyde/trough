---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_affine_locallyFinitePresentation_separation, AlgebraicGeometry.universallyClosed_tfae, AlgebraicGeometry.isProper_tfae, AlgebraicGeometry.exists_surjective_isClosedImmersion_projectiveSpace_of_isProper, AlgebraicGeometry.exists_projectiveSpace_square_isProper_iff_isClosedImmersion, AlgebraicGeometry.HasChowModification
statement: formalized
proof: formalized
---

# 32.14 Universally closed morphisms

Section 32.14 of the Stacks Project, [Tag 05JW](https://stacks.math.columbia.edu/tag/05JW). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05BD, a lemma

[Tag 05BD](https://stacks.math.columbia.edu/tag/05BD) in the Stacks Project.

**`AlgebraicGeometry.exists_affine_locallyFinitePresentation_separation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreSeparation/Basic.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FibreSeparation/Basic.lean#L64).

> **Stacks Project, Tag 05BD.** A closed subscheme of a base change `X ×_S T` avoiding the
> fibre of `X ×_S T ⟶ T` over a point `t`, for `f : X ⟶ S` quasi-compact, can be separated from
> that fibre already over an affine base locally of finite presentation over `S`: there is an
> affine open `V ∋ t`, an affine `T'` locally of finite presentation over `S` with a factorization
> of `V ⟶ T` through it, and a closed subscheme of `X ×_S T'` containing the restriction of the
> given one and still avoiding the fibre over the image of `t`.

```lean
theorem exists_affine_locallyFinitePresentation_separation
    {X S T : Scheme.{u}} (f : X ⟶ S) [QuasiCompact f] (g : T ⟶ S)
    (t : T) (I : (pullback f g).IdealSheafData)
    (ht : t ∉ Set.image (pullback.snd f g) I.support.1) :
    ∃ (V : T.affineOpens) (htV : t ∈ V.1)
      (T' : Scheme.{u}) (_ : IsAffine T') (b : T' ⟶ S)
      (_ : LocallyOfFinitePresentation b) (a : V.1.toScheme ⟶ T')
      (_ : V.1.ι ≫ g = a ≫ b)
      (I' : (pullback f b).IdealSheafData)
      (p : pullback f (V.1.ι ≫ g) ⟶ pullback f g)
      (q : pullback f (V.1.ι ≫ g) ⟶ pullback f b),
      (p ≫ pullback.fst f g = pullback.fst f (V.1.ι ≫ g)) ∧
      (p ≫ pullback.snd f g = pullback.snd f (V.1.ι ≫ g) ≫ V.1.ι) ∧
      (q ≫ pullback.fst f b = pullback.fst f (V.1.ι ≫ g)) ∧
      (q ≫ pullback.snd f b = pullback.snd f (V.1.ι ≫ g) ≫ a) ∧
      (a ⟨t, htV⟩ ∉ Set.image (pullback.snd f b) I'.support.1) ∧
      (I'.comap q ≤ I.comap p)
```

## Tag 05JX, a lemma

[Tag 05JX](https://stacks.math.columbia.edu/tag/05JX) in the Stacks Project.

**`AlgebraicGeometry.universallyClosed_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/UniversallyClosedTest.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/UniversallyClosedTest.lean#L62).

> **Stacks 05JX.** A quasi-compact morphism is universally closed precisely when all of its
> locally finitely presented base changes are closed, or equivalently when its
> base changes to all finite-dimensional affine spaces are closed.

```lean
theorem universallyClosed_tfae {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] :
    List.TFAE
      [UniversallyClosed f,
       ∀ (S' : Scheme.{u}) (g : S' ⟶ S),
         LocallyOfFinitePresentation g → IsClosedMap (pullback.snd f g),
       ∀ n : ℕ, IsClosedMap (AffineSpace.map (ULift.{u} (Fin n)) f)]
```

## Tag 0205, a lemma

[Tag 0205](https://stacks.math.columbia.edu/tag/0205) in the Stacks Project.

**`AlgebraicGeometry.isProper_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ProperTest.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/ProperTest.lean#L42).

> A separated morphism of finite type is proper precisely when all of its base changes along
> morphisms locally of finite type are closed, or equivalently when its base changes to all
> finite-dimensional affine spaces are closed.
>
> The second condition is the hypothesis that `X ×_S S' ⟶ S'` is a closed map for every `S' ⟶ S`
> locally of finite type, and the third that `𝔸(n; X) ⟶ 𝔸(n; S)`, the base change of `f` along
> `𝔸(n; S) ↘ S`, is a closed map for every `n`.

```lean
theorem isProper_tfae {X S : Scheme.{u}} (f : X ⟶ S)
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f] :
    List.TFAE
      [IsProper f,
       ∀ (S' : Scheme.{u}) (g : S' ⟶ S),
         LocallyOfFiniteType g → IsClosedMap (pullback.snd f g),
       ∀ n : ℕ, IsClosedMap (AffineSpace.map (ULift.{u} (Fin n)) f)]
```

## Tag 05LZ, an equation

[Tag 05LZ](https://stacks.math.columbia.edu/tag/05LZ) in the Stacks Project.

**`AlgebraicGeometry.exists_surjective_isClosedImmersion_projectiveSpace_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ProperCheckSquare.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/ProperCheckSquare.lean#L139).

> **The square of [Stacks, Tag 05LZ].** Let `f : X ⟶ S` be proper and admit a Chow
> modification. Then there are an `n`, a scheme `X'`, a proper **surjective** morphism
> `π : X' ⟶ X` and a **closed immersion** `i : X' ⟶ ℙⁿ_S` with
> `π ≫ f = i ≫ (ℙⁿ_S ↘ S)`, that is, a commutative square
>
> ```
> X' ---i---> ℙⁿ_S
> |            |
> π            |
> v            v
> X ----f----> S
> ```
>
> over `S` whose left vertical morphism is surjective and whose top morphism is a closed immersion
> into projective space over `S`.
>
> Chow's lemma supplies the square with `i` merely an immersion; properness of `f` upgrades it to a
> closed immersion.

```lean
theorem exists_surjective_isClosedImmersion_projectiveSpace_of_isProper (f : X ⟶ S) [IsProper f]
    (hf : HasChowModification f) :
    ∃ (n : ℕ) (X' : Scheme.{u}) (π : X' ⟶ X) (i : X' ⟶ ProjectiveSpace n S),
      IsProper π ∧ Surjective π ∧ IsClosedImmersion i ∧
        π ≫ f = i ≫ (ProjectiveSpace n S ↘ S)
```

**`AlgebraicGeometry.exists_projectiveSpace_square_isProper_iff_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ProperCheckSquareChow.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/ProperCheckSquareChow.lean#L50).

> Let `S` be quasi-compact and quasi-separated and let `f : X ⟶ S` be separated and of finite
> type. Then there are an `n`, a scheme `X'`, a proper surjective morphism `π : X' ⟶ X` and an
> immersion `i : X' ⟶ ℙⁿ_S` with `π ≫ f = i ≫ (ℙⁿ_S ↘ S)`. Moreover `f` is proper if and only if
> `i` is a closed immersion.

```lean
theorem exists_projectiveSpace_square_isProper_iff_isClosedImmersion {X S : Scheme.{u}}
    (f : X ⟶ S) [CompactSpace S] [QuasiSeparatedSpace S] [IsSeparated f] [LocallyOfFiniteType f]
    [QuasiCompact f] :
    ∃ (n : ℕ) (X' : Scheme.{u}) (π : X' ⟶ X) (i : X' ⟶ ProjectiveSpace n S),
      IsProper π ∧ Surjective π ∧ IsImmersion i ∧ π ≫ f = i ≫ (ProjectiveSpace n S ↘ S) ∧
        (IsProper f ↔ IsClosedImmersion i)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.HasChowModification`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/ChowLemma.lean#L96), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ChowFiniteType/Basic.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ChowFiniteType/Basic.lean#L92) (StacksFrontier): “the displayed diagram, as the predicate HasChowModification”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.14, Tag 05JW](https://stacks.math.columbia.edu/tag/05JW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
