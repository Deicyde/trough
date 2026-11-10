---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.existsFiniteSurjectiveSchemeCover_and_refining, AlgebraicGeometry.Space.exists_isLimit_finite_finitePresentation_fixedOnOpen, AlgebraicGeometry.Space.exists_finiteSchemeCover_finiteEtaleOverDenseOpen_and_refining, AlgebraicGeometry.Space.exists_finiteEtaleCoverStratification
statement: formalized
proof: formalized
---

# 70.16 Finite cover by a scheme

Section 70.16 of the Stacks Project, [Tag 0ACX](https://stacks.math.columbia.edu/tag/0ACX). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09YC, a proposition

[Tag 09YC](https://stacks.math.columbia.edu/tag/09YC) in the Stacks Project.

**`AlgebraicGeometry.Space.existsFiniteSurjectiveSchemeCover_and_refining`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFpSchemeCoverExistence.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFpSchemeCoverExistence.lean#L97).

> **Stacks Project, Tag 09YC.** Let `X` be a quasi-compact and quasi-separated algebraic space
> over a scheme `S`. Then
>
> 1. there is a surjective finite morphism of finite presentation to `X` from the presheaf
>    represented by an object of the big fppf site — a scheme over `S` — and
> 2. given a surjective étale morphism `p : U ⟶ X` from an algebraic space, such a cover can be
>    chosen so that it factors through `p` on a representable open subspace neighbourhood of every
>    one of its points.
>
> Clause (1) is a finite surjective scheme cover refined through an affine étale chart by Stacks
> 0CP0 and embedded in a finite cover of finite presentation; clause (2) is clause (1) refined by
> Stacks 0CP0.

```lean
theorem existsFiniteSurjectiveSchemeCover_and_refining
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (hXqc : IsQuasiCompactSpace B S hS X)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X) :
    (∃ (Y : BigFppfOver B S hS) (f : yoneda.obj Y ⟶ X),
        IsSurjective B S hS f ∧ IsFinite B S hS f ∧ IsFinitePresentation B S hS f) ∧
      ∀ (U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS U →
        ∀ p : U ⟶ X, IsSurjective B S hS p → IsEtale B S hS p →
          ∃ (Y : BigFppfOver B S hS) (f : yoneda.obj Y ⟶ X),
            IsSurjective B S hS f ∧ IsFinite B S hS f ∧ IsFinitePresentation B S hS f ∧
              FactorsZariskiLocallyThrough B S hS p Y f
```

## Tag 0GUM, a lemma

[Tag 0GUM](https://stacks.math.columbia.edu/tag/0GUM) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isLimit_finite_finitePresentation_fixedOnOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralLimitFinitePresentationFixedOnOpen.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/IntegralLimitFinitePresentationFixedOnOpen.lean#L83).

> An integral morphism `f : X ⟶ Y` of algebraic spaces over `S`, with `Y` quasi-compact and
> quasi-separated, which is finite and of finite presentation over a quasi-compact open subspace `V`
> of `Y` (that is, `f⁻¹(V) = X ×_Y V ⟶ V` is), is the limit of a directed inverse system, indexed by
> a nonempty directed preorder in the universe of the schemes, of algebraic spaces `D i` with
> morphisms `t i : D i ⟶ Y` finite and of finite presentation, the limiting cone `p` having vertex
> `X` and lying over `Y`; and for every `i` the square formed by `X ×_Y V ⟶ X ⟶ D i`, `X ×_Y V ⟶ V`,
> `t i` and `V ⟶ Y` is cartesian, that is `f⁻¹(V) ⟶ f_i⁻¹(V)` is an isomorphism.

```lean
theorem exists_isLimit_finite_finitePresentation_fixedOnOpen
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsIntegralHom B S hS f)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    (V : Subfunctor Y) (hV : IsOpenSubspace B S hS V)
    (hVqc : IsQuasiCompactSpace B S hS V.toFunctor)
    (hfVfinite : IsFinite B S hS (pullback.snd f V.ι))
    (hfVfp : IsFinitePresentation B S hS (pullback.snd f V.ι)) :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirectedOrder I)
      (D : Iᵒᵖ ⥤ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
      (p : (Functor.const Iᵒᵖ).obj X ⟶ D) (t : D ⟶ (Functor.const Iᵒᵖ).obj Y),
      (∀ i, IsAlgebraicSpace B S hS (D.obj i)) ∧
      (∀ i, IsFinite B S hS (t.app i)) ∧
      (∀ i, IsFinitePresentation B S hS (t.app i)) ∧
      (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
      Nonempty (IsLimit (Cone.mk X p)) ∧
      (∀ i, IsPullback (pullback.fst f V.ι ≫ p.app i) (pullback.snd f V.ι) (t.app i) V.ι)
```

## Tag 0GUN, a lemma

[Tag 0GUN](https://stacks.math.columbia.edu/tag/0GUN) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finiteSchemeCover_finiteEtaleOverDenseOpen_and_refining`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteSchemeCoverExistence.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteSchemeCoverExistence.lean#L156).

> **Stacks Project, Tag 0GUN.** Let `X` be a quasi-compact and quasi-separated algebraic
> space over a scheme `S` such that `|X|` has finitely many irreducible components. Then
>
> 1. there is a surjective, finite and finitely presented morphism `f : h_Y ⟶ X` from the
>    presheaf represented by an object `Y` of the big fppf site — a scheme over `S` — and a
>    quasi-compact open subspace `U ⊆ X` with dense point set over which `f` is finite étale, and
> 2. given a surjective étale morphism `p : V ⟶ X` from an algebraic space, such a cover can be
>    chosen so that it factors through `p` on a representable open subspace neighbourhood of
>    every one of its points.
>
> Clause (2) for `p` is reduced to an affine chart `h_A ⟶ V`, where it is
> `AlgebraicGeometry.Space.exists_finiteSchemeCover_refining_of_isAffine`; clause (1) is clause (2)
> at the identity of `X`.

```lean
theorem exists_finiteSchemeCover_finiteEtaleOverDenseOpen_and_refining
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hXqc : IsQuasiCompactSpace B S hS X) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (hcomp : (irreducibleComponents (points B S hS X)).Finite) :
    (∃ (Y : BigFppfOver B S hS) (f : yoneda.obj Y ⟶ X) (U : Subfunctor X),
      IsFiniteSchemeCoverFiniteEtaleOverDenseOpen B S hS Y f U) ∧
    ∀ (V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS V →
      ∀ p : V ⟶ X, IsSurjective B S hS p → IsEtale B S hS p →
        ∃ (Y : BigFppfOver B S hS) (f : yoneda.obj Y ⟶ X) (U : Subfunctor X),
          IsFiniteSchemeCoverFiniteEtaleOverDenseOpen B S hS Y f U ∧
            FactorsZariskiLocallyThrough B S hS p Y f
```

## Tag 0GUP, a lemma

[Tag 0GUP](https://stacks.math.columbia.edu/tag/0GUP) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finiteEtaleCoverStratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteEtaleCoverStratification.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteEtaleCoverStratification.lean#L57).

> **Stacks 0GUP.** Let `X` be a quasi-compact and quasi-separated algebraic space. There are
> `t ≥ 0` and closed subspaces `X ⊇ Z₀ ⊇ Z₁ ⊇ ⋯ ⊇ Z_t = ∅` with each `Z_i ⟶ X` of finite
> presentation and `Z₀ ⊆ X` a thickening, such that for each `i < t` there is a scheme `Y_i` and a
> surjective, finite and finitely presented morphism `Y_i ⟶ Z_i` which is finite étale over the
> open subspace `Z_i ∖ Z_{i+1}` (`AlgebraicGeometry.Space.IsFiniteEtaleCoverStep`).

```lean
theorem exists_finiteEtaleCoverStratification (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hXqc : IsQuasiCompactSpace B S hS X) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X) :
    ∃ (t : ℕ) (Z : ℕ → Subfunctor X),
      (∀ i, IsClosedSubspace B S hS (Z i)) ∧ (∀ i, IsFinitePresentation B S hS (Z i).ι) ∧
      (∀ i, Z (i + 1) ≤ Z i) ∧ IsThickening B S hS ⟨X, hX⟩ (Z 0) ∧
      IsEmpty (points B S hS (Z t).toFunctor) ∧
      ∀ i < t, IsFiniteEtaleCoverStep B S hS (Z i) (Z (i + 1))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.16, Tag 0ACX](https://stacks.math.columbia.edu/tag/0ACX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
