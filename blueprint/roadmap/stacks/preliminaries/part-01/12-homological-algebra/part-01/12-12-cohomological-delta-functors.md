---
declaration: section
origin: cited
lean: CategoryTheory.DeltaFunctor, CategoryTheory.DeltaFunctor.Hom, CategoryTheory.DeltaFunctor.IsUniversal, CategoryTheory.DeltaFunctor.isUniversal_of_effaceable, CategoryTheory.DeltaFunctor.isUniversal_of_forall_exists_mono, CategoryTheory.DeltaFunctor.isUniversal_of_isZero_injective, CategoryTheory.DeltaFunctor.IsUniversal.iso_ext, CategoryTheory.DeltaFunctor.IsUniversal.isoOfIso
statement: formalized
proof: formalized
---

# 12.12 Cohomological delta-functors

Section 12.12 of the Stacks Project, [Tag 010P](https://stacks.math.columbia.edu/tag/010P). 5 tags here are carried by 8 declarations of the repository (all in StacksCore), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 010Q, a definition

[Tag 010Q](https://stacks.math.columbia.edu/tag/010Q) in the Stacks Project.

**`CategoryTheory.DeltaFunctor`**, a structure in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/DeltaFunctor/Basic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/DeltaFunctor/Basic.lean#L55). The attribute's comment: “cohomological δ-functor: additive `Fⁿ`, long exact sequence, natural `δ`”. References: SGA 7 VII (3.7.5).

> Stacks 010Q: a cohomological δ-functor from `A` to `B`: additive functors `Fⁿ : A ⥤ B`
> (`n ≥ 0`) and, for every short exact sequence `0 → X₁ → X₂ → X₃ → 0` of `A`, connecting
> morphisms `δ : Fⁿ(X₃) ⟶ Fⁿ⁺¹(X₁)`, natural in the short exact sequence, such that
> `0 → F⁰(X₁) → F⁰(X₂) → F⁰(X₃) → F¹(X₁) → F¹(X₂) → …` is exact.

```lean
structure DeltaFunctor [Preadditive A] [Preadditive B]
```

## Tag 010R, a definition

[Tag 010R](https://stacks.math.columbia.edu/tag/010R) in the Stacks Project.

**`CategoryTheory.DeltaFunctor.Hom`**, a structure in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/DeltaFunctor/Basic.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/DeltaFunctor/Basic.lean#L145). The attribute's comment: “morphism of δ-functors: `tⁿ : Fⁿ ⟶ Gⁿ` commuting with the `δ`”.

> Stacks 010R: a morphism of δ-functors `F ⟶ G` is a family of natural transformations
> `tⁿ : Fⁿ ⟶ Gⁿ` commuting with the connecting morphisms of every short exact sequence.

```lean
structure Hom (F G : DeltaFunctor A B)
```

## Tag 010S, a definition

[Tag 010S](https://stacks.math.columbia.edu/tag/010S) in the Stacks Project.

**`CategoryTheory.DeltaFunctor.IsUniversal`**, a class in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/DeltaFunctor/Basic.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/DeltaFunctor/Basic.lean#L177). The attribute's comment: “universal δ-functor: every `t : F⁰ ⟶ G⁰` extends uniquely to `F ⟶ G`”.

> Stacks 010S: a δ-functor `F` is universal if every natural transformation `t : F⁰ ⟶ G⁰`
> extends uniquely to a morphism of δ-functors `F ⟶ G`.

```lean
class IsUniversal (F : DeltaFunctor A B) : Prop
```

## Tag 010T, a lemma

[Tag 010T](https://stacks.math.columbia.edu/tag/010T) in the Stacks Project.

**`CategoryTheory.DeltaFunctor.isUniversal_of_effaceable`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean#L317). The attribute's comment: “an effaceable δ-functor is universal (Grothendieck's Tohoku argument)”.

> Stacks 010T: an effaceable δ-functor is universal.

```lean
theorem isUniversal_of_effaceable [F.Effaceable] : F.IsUniversal
```

**`CategoryTheory.DeltaFunctor.isUniversal_of_forall_exists_mono`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean#L325). The attribute's comment: “literal form: monos `u : A → B` with `Fⁿ(u) = 0` for all `n > 0`, `A`”.

> Stacks 010T in its literal form: if for every `n > 0` and every `X` there is a monomorphism
> `u : X ⟶ I` with `Fⁿ(u) = 0`, then `F` is universal.

```lean
theorem isUniversal_of_forall_exists_mono
    (h : ∀ (n : ℕ) (X : A), ∃ (I : A) (u : X ⟶ I), Mono u ∧ (F.functor (n + 1)).map u = 0) :
    F.IsUniversal
```

**`CategoryTheory.DeltaFunctor.isUniversal_of_isZero_injective`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean#L345). The attribute's comment: “enough injectives and `Fⁿ(I) = 0` for `I` injective, `n > 0`: universal”. References: SGA 3 I (5.2.1), “special case”.

> Stacks 010T for the standard source of effaceability: if `A` has enough injectives and `Fⁿ`
> vanishes on injectives for `n > 0`, then `F` is universal. This is the form used for derived
> functors and Čech cohomology.

```lean
theorem isUniversal_of_isZero_injective [Balanced B] [EnoughInjectives A]
    (h : ∀ (n : ℕ) (I : A) [Injective I], IsZero ((F.functor (n + 1)).obj I)) : F.IsUniversal
```

## Tag 010U, a lemma

[Tag 010U](https://stacks.math.columbia.edu/tag/010U) in the Stacks Project.

**`CategoryTheory.DeltaFunctor.IsUniversal.iso_ext`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean#L357). The attribute's comment: “the isomorphism is unique: it is determined by its degree-zero component”.

> Stacks 010U, uniqueness: an isomorphism of universal δ-functors is determined by its
> degree-zero component.

```lean
lemma iso_ext {α β : F ≅ G} (h : α.hom.app 0 = β.hom.app 0) : α = β
```

**`CategoryTheory.DeltaFunctor.IsUniversal.isoOfIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/DeltaFunctor/Effaceable.lean#L365). The attribute's comment: “universal δ-functors with the same `F⁰` are isomorphic, extending `F⁰ ≅ G⁰`”.

> Stacks 010U: two universal δ-functors with isomorphic degree-zero parts are isomorphic as
> δ-functors, by the isomorphism extending the given one.

```lean
noncomputable def isoOfIso (e : F.functor 0 ≅ G.functor 0) : F ≅ G
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.12, Tag 010P](https://stacks.math.columbia.edu/tag/010P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
