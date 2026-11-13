---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_inertiaPullbackComparison_isEquivalence, AlgebraicGeometry.Stack.HigherDiagonal.prop_isomMap_of_prop_relativeDiagonal, AlgebraicGeometry.Stack.inertiaPullbackComparison_isEquivalenceOver_iff_inducesIsomorphismAt, AlgebraicGeometry.Stack.exists_openSubstack_isStabilizerPreserving, AlgebraicGeometry.Stack.inducesIsomorphismAt_baseChange, AlgebraicGeometry.Stack.nonempty_inertiaPullbackComparison_isEquivalenceOver_baseChange, AlgebraicGeometry.Stack.isoClassMk_eq_of_isoClassMk_eq_components, AlgebraicGeometry.Stack.isEquivalence_of_isEtale_of_inducesIsomorphismAt
statement: formalized
proof: formalized
---

# 101.45 Stabilizer preserving morphisms

Section 101.45 of the Stacks Project, [Tag 0DU6](https://stacks.math.columbia.edu/tag/0DU6). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DU7, a lemma

[Tag 0DU7](https://stacks.math.columbia.edu/tag/0DU7) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_inertiaPullbackComparison_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StabilizerPreservingRepresentable.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StabilizerPreservingRepresentable.lean#L192).

> **Stacks 0DU7.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. If the
> canonical comparison `ℐ_𝒳 ⟶ 𝒳 ×_𝒴 ℐ_𝒴` of Stacks 06R5 is an isomorphism, then `f` is
> representable by algebraic spaces.
>
> The comparison makes `f` faithful
> (`AlgebraicGeometry.Stack.faithful_homFunctor_of_inertiaPullbackComparison_full`, condition (4)
> of Stacks 04YY), and a faithful 1-morphism of algebraic stacks is representable by algebraic
> spaces (Stacks 04Y5, the implication (2) ⟹ (3)).

```lean
theorem isRepresentableByAlgebraicSpaces_of_inertiaPullbackComparison_isEquivalence
    (f : 𝒳 ⟶ 𝒴)
    (hf : (CategoryTheory.inertiaPullbackComparison 𝒳.val.val.p 𝒴.val.val.p
      (CatFiberedInGroupoids.homFunctor f.hom)
      (CatFiberedInGroupoids.homFunctor_comp_p f.hom)).IsEquivalence) :
    IsRepresentableByAlgebraicSpaces B S hS f.hom.hom
```

## Tag 0DU8, a remark

[Tag 0DU8](https://stacks.math.columbia.edu/tag/0DU8) in the Stacks Project.

**`AlgebraicGeometry.Stack.HigherDiagonal.prop_isomMap_of_prop_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparatedIsomPullback.lean#L511).

> **Stacks 0DU8.** Let `x : T ⟶ 𝒳` have an algebraic space as source, and let `G ⟶ H` be the
> pullback to `T` of the stabilizer comparison `ℐ_𝒳 ⟶ 𝒳 ×_𝒴 ℐ_𝒴`, that is, the map
> `G = Isom_𝒳(x, x) ⟶ Isom_𝒴(f ∘ x, f ∘ x) = H` on automorphism spaces. Then `G ⟶ H` satisfies a
> condition of Stacks 04XB as soon as the relative diagonal `Δ_f` does, for an arbitrary property
> `P` of morphisms of algebraic spaces over `S`: if `Δ_f` is unramified, étale, proper, … then so
> is `G ⟶ H`.
>
> The square `T ×_𝒳 T ⟶ 𝒳`, `T ×_𝒴 T ⟶ 𝒳 ×_𝒴 𝒳` over `Δ_f` is 2-cartesian, so `T ×_𝒳 T ⟶ T ×_𝒴 T`
> is a base change of `Δ_f` (Stacks 050H), and `G ⟶ H` is a base change of that along the diagonal
> of `T` (Stacks 0CPL, part (2)).

```lean
theorem prop_isomMap_of_prop_relativeDiagonal
    (x : algebraicSpaceStack.{u, w} B S hS T hT ⟶ 𝒳)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    (hP : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤
        (AlgebraicStacks.twoFibreProduct B S hS f f).val.val.obj)
      (_hy : y ⋙ (AlgebraicStacks.twoFibreProduct B S hS f f).val.val.p = Over.map U.hom)
      (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.val.p
            (AlgebraicStacks.twoFibreProduct B S hS f f).val.val.p y
            (CatFiberedInGroupoids.homFunctor
              (Stack.relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom)))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        P (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩))) :
    ∀ (U : BigFppfOver B S hS)
      (z : BigFppfOver B U.left.1 U.left.2 ⥤
        (isomStack B S hS T hT (x ≫ f) (x ≫ f)).val.obj)
      (_hz : z ⋙ (isomStack B S hS T hT (x ≫ f) (x ≫ f)).val.p = Over.map U.hom)
      (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (isomStack B S hS T hT x x).val.p
            (isomStack B S hS T hT (x ≫ f) (x ≫ f)).val.p z
            (CatFiberedInGroupoids.homFunctor (isomMap B S hS f T hT x x)))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        P (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩))
```

## Tag 0DU9, a lemma

[Tag 0DU9](https://stacks.math.columbia.edu/tag/0DU9) in the Stacks Project.

**`AlgebraicGeometry.Stack.inertiaPullbackComparison_isEquivalenceOver_iff_inducesIsomorphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StabilizerPreservingUnramified.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StabilizerPreservingUnramified.lean#L187).

> **Stacks 0DU9.** Let `f : 𝒳 ⟶ 𝒴` be an unramified 1-morphism of algebraic stacks over `S`.
> Then the canonical comparison `ℐ_𝒳 ⟶ 𝒳 ×_𝒴 ℐ_𝒴` of Stacks 06R5 is an isomorphism (an
> equivalence over the big fppf site) if and only if `f` induces an isomorphism between the
> automorphism groups at `x` and at `f(x)` (Stacks 0DTW) for every `x ∈ |𝒳|`.

```lean
theorem inertiaPullbackComparison_isEquivalenceOver_iff_inducesIsomorphismAt
    (f : 𝒳 ⟶ 𝒴) (hu : IsUnramified B S hS f) :
    Nonempty (IsEquivalenceOver
      (RelativeInertia.toBase 𝒳.val.val.p)
      (TwoFibreProductOver.structureFunctor (RelativeInertia.toBase 𝒴.val.val.p)
        𝒳.val.val.p 𝒴.val.val.p (RelativeInertia.π 𝒴.val.val.p)
        (CatFiberedInGroupoids.homFunctor f.hom))
      (inertiaPullbackComparison 𝒳.val.val.p 𝒴.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom)
        (CatFiberedInGroupoids.homFunctor_comp_p f.hom))) ↔
      ∀ q : points B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids,
        InducesIsomorphismAt B S hS f q
```

## Tag 0DUA, a lemma

[Tag 0DUA](https://stacks.math.columbia.edu/tag/0DUA) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_openSubstack_isStabilizerPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StabilizerPreservingLocus.lean, line 694](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StabilizerPreservingLocus.lean#L694).

> **Stacks 0DUA.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` which is
> representable by algebraic spaces and unramified, and assume the inertia `ℐ_𝒴 ⟶ 𝒴` is proper.
> Then the set of `x ∈ |𝒳|` at which `f` induces an isomorphism between the automorphism groups
> at `x` and at `f(x)` (**Stacks 0DTW**) is open; there is an open substack `𝒰 ⊆ 𝒳` with that set
> of points (**Stacks 06FJ**); and for every open substack `𝒰 ⊆ 𝒳` with that set of points, the
> canonical comparison `ℐ_𝒰 ⟶ 𝒰 ×_𝒴 ℐ_𝒴` of **Stacks 06R5** is an isomorphism.

```lean
theorem exists_openSubstack_isStabilizerPreserving
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) (hu : IsUnramified B S hS f)
    (hI : AlgebraicStacks.IsProper B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒴)) :
    @IsOpen _ (pointTopology B S hS 𝒳.val) (stabilizerPreservingLocus B S hS f) ∧
      (∃ U : OpenSubstack 𝒳, U.pointSet B S hS = stabilizerPreservingLocus B S hS f) ∧
        ∀ U : OpenSubstack 𝒳, U.pointSet B S hS = stabilizerPreservingLocus B S hS f →
          IsStabilizerPreserving B S hS (U.inclusion ≫ f)
```

## Tag 0DUB, a lemma

[Tag 0DUB](https://stacks.math.columbia.edu/tag/0DUB) in the Stacks Project.

**`AlgebraicGeometry.Stack.inducesIsomorphismAt_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupBaseChange.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupBaseChange.lean#L311). The attribute's comment: “the automorphism groups at a point of a base change”.

> **Stacks 0DUB, part (1).** In a 2-cartesian square of algebraic stacks with apex `𝒳'`,
> first projection `f' : 𝒳' ⟶ 𝒴'` and second projection `𝒳' ⟶ 𝒳`, if `f` induces an isomorphism
> between automorphism groups at the image `x` of a point `x'` of `|𝒳'|`, then `f'` induces an
> isomorphism between automorphism groups at `x'`.
>
> The hypothesis is the isomorphism at the single point `x` and nothing else; in particular `f` is
> not assumed stabilizer preserving, which is the hypothesis of part (2).

```lean
theorem inducesIsomorphismAt_baseChange (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (x' : points B S hS P.pt.val.val P.pt.val.isFiberedInGroupoids)
    (hx : InducesIsomorphismAt B S hS f
      (pointsMap B S hS P.pt.val.val P.pt.val.isFiberedInGroupoids
        𝒳.val.isFiberedInGroupoids P.snd.hom.hom x')) :
    InducesIsomorphismAt B S hS P.fst x'
```

**`AlgebraicGeometry.Stack.nonempty_inertiaPullbackComparison_isEquivalenceOver_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StabilizerPreserving.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StabilizerPreserving.lean#L79). The attribute's comment: “the inertia map of a base change”.

> **Stacks 0DUB, part (2).** In a cartesian square of algebraic stacks, if the canonical
> comparison from the inertia of `𝒳` to `𝒳 ×_𝒴 ℐ_𝒴` is an equivalence, then so is the
> corresponding comparison for the base change of `f` along `g`.
>
> The base change of `f : 𝒳 ⟶ 𝒴` along `g : 𝒴' ⟶ 𝒴` is the first projection of a 2-fibre product
> `P` of the cospan `(g, f)`.

```lean
theorem nonempty_inertiaPullbackComparison_isEquivalenceOver_baseChange
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hf : (CategoryTheory.inertiaPullbackComparison 𝒳.val.val.p 𝒴.val.val.p
      (CatFiberedInGroupoids.homFunctor f.hom)
      (CatFiberedInGroupoids.homFunctor_comp_p f.hom)).IsEquivalence) :
    Nonempty (CategoryTheory.IsEquivalenceOver
      (RelativeInertia.toBase P.pt.val.val.p)
      (TwoFibreProductOver.structureFunctor (RelativeInertia.toBase 𝒴'.val.val.p)
        P.pt.val.val.p 𝒴'.val.val.p (RelativeInertia.π 𝒴'.val.val.p)
        (CatFiberedInGroupoids.homFunctor P.fst.hom))
      (CategoryTheory.inertiaPullbackComparison P.pt.val.val.p 𝒴'.val.val.p
        (CatFiberedInGroupoids.homFunctor P.fst.hom)
        (CatFiberedInGroupoids.homFunctor_comp_p P.fst.hom)))
```

## Tag 0DUC, a lemma

[Tag 0DUC](https://stacks.math.columbia.edu/tag/0DUC) in the Stacks Project.

**`AlgebraicGeometry.Stack.isoClassMk_eq_of_isoClassMk_eq_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FieldValuedPointsBaseChange.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FieldValuedPointsBaseChange.lean#L208). The attribute's comment: “field-valued points of a base change, injective on isomorphism classes”.

> **Stacks 0DUC.** Let `𝒳'` be the apex of a 2-cartesian square of algebraic stacks with
> `f' : 𝒳' ⟶ 𝒴'` its first projection, over `f : 𝒳 ⟶ 𝒴` and `g : 𝒴' ⟶ 𝒴`, and suppose `f`
> induces an isomorphism between automorphism groups at every point of `|𝒳|` (Stacks 0DTW). Then
> for every field `k` the map `Mor(Spec k, 𝒳') → Mor(Spec k, 𝒴') × Mor(Spec k, 𝒳)` is injective
> on isomorphism classes.
>
> A 1-morphism `Spec k ⟶ 𝒳'` is, by 2-Yoneda, an object of the fibre of `𝒳'` over an object `U`
> of the big site with underlying scheme `Spec k`, and its isomorphism class is
> `CategoryTheory.Functor.isoClassMk`; so this says that two such 1-morphisms with the same pair
> of classes in `𝒴'` and in `𝒳` have the same class in `𝒳'`.

```lean
theorem isoClassMk_eq_of_isoClassMk_eq_components (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hf : ∀ q : points B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids,
      InducesIsomorphismAt B S hS f q)
    (k : Type u) [Field k] (U : BigFppfOver B S hS)
    (hU : (BigFppfOver.toScheme B S hS).obj U ≅ Spec (.of k))
    (a b : P.pt.val.val.p.Fiber U)
    (hfst : Functor.isoClassMk 𝒴'.val.val.p
        ((Functor.fiberMap P.pt.val.val.p 𝒴'.val.val.p
          (CatFiberedInGroupoids.homFunctor P.fst.hom)
          (CatFiberedInGroupoids.homFunctor_comp_p P.fst.hom) U).obj a)
      = Functor.isoClassMk 𝒴'.val.val.p
        ((Functor.fiberMap P.pt.val.val.p 𝒴'.val.val.p
          (CatFiberedInGroupoids.homFunctor P.fst.hom)
          (CatFiberedInGroupoids.homFunctor_comp_p P.fst.hom) U).obj b))
    (hsnd : Functor.isoClassMk 𝒳.val.val.p
        ((Functor.fiberMap P.pt.val.val.p 𝒳.val.val.p
          (CatFiberedInGroupoids.homFunctor P.snd.hom)
          (CatFiberedInGroupoids.homFunctor_comp_p P.snd.hom) U).obj a)
      = Functor.isoClassMk 𝒳.val.val.p
        ((Functor.fiberMap P.pt.val.val.p 𝒳.val.val.p
          (CatFiberedInGroupoids.homFunctor P.snd.hom)
          (CatFiberedInGroupoids.homFunctor_comp_p P.snd.hom) U).obj b)) :
    Functor.isoClassMk P.pt.val.val.p a = Functor.isoClassMk P.pt.val.val.p b
```

## Tag 0DUD, a lemma

[Tag 0DUD](https://stacks.math.columbia.edu/tag/0DUD) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEquivalence_of_isEtale_of_inducesIsomorphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleStabilizerPreservingIsomorphism.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/EtaleStabilizerPreservingIsomorphism.lean#L295).

> **Stacks 0DUD.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. Assume `f`
> is étale, that `f` induces an isomorphism between the automorphism groups at `x` and at `f(x)`
> for every `x ∈ |𝒳|` (**Stacks 0DTW**), and that for every algebraically closed field `k` the
> functor `Mor(Spec k, 𝒳) ⟶ Mor(Spec k, 𝒴)` is an equivalence. Then `f` is an isomorphism.
>
> The proof is the source's. Fullness of the functors on geometric points is condition (3) of
> **Stacks 0CPN**, so `f` is universally injective. Étale implies unramified (**Stacks 0CIW**), so
> **Stacks 0DU9** makes `f` stabilizer preserving and **Stacks 0DU7** makes it representable by
> algebraic spaces. Essential surjectivity on geometric points makes `f` surjective, and
> **Stacks 05W5**, in the form
> `AlgebraicGeometry.Stack.isEquivalence_of_isEtale_of_universallyInjective_of_isSurjective`,
> concludes.

```lean
theorem isEquivalence_of_isEtale_of_inducesIsomorphismAt (f : 𝒳 ⟶ 𝒴)
    (he : IsEtale B S hS f)
    (hauto : ∀ x : AlgebraicStacks.points B S hS 𝒳, InducesIsomorphismAt B S hS f x)
    (hfibre : ∀ (k : Type u) [Field k] [IsAlgClosed k] (V : BigFppfOver B S hS),
      ((BigFppfOver.toScheme B S hS).obj V ≅ Spec (.of k)) →
        (geometricFibreFunctor B S hS f V).IsEquivalence) :
    (CatFiberedInGroupoids.homFunctor f.hom).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.45, Tag 0DU6](https://stacks.math.columbia.edu/tag/0DU6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
