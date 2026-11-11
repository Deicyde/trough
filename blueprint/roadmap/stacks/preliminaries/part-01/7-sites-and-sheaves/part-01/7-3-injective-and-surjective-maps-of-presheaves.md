---
declaration: section
origin: cited
lean: CategoryTheory.Presheaf.isLocallyInjective_bot, CategoryTheory.Presheaf.isLocallySurjective_bot, Presheaf.IsLocallyInjective, Presheaf.IsLocallySurjective, CategoryTheory.Presheaf.isLocallyInjective_bot_iff_mono, CategoryTheory.Presheaf.isLocallySurjective_bot_iff_epi, CategoryTheory.Presheaf.isIso_iff_isLocallyBijective, Subfunctor
statement: formalized
proof: formalized
---

# 7.3 Injective and surjective maps of presheaves

Section 7.3 of the Stacks Project, [Tag 00V5](https://stacks.math.columbia.edu/tag/00V5). 5 tags here are carried by 6 declarations of the repository (5 in StacksCore and 1 in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00V6, a definition

[Tag 00V6](https://stacks.math.columbia.edu/tag/00V6) in the Stacks Project.

**`CategoryTheory.Presheaf.isLocallyInjective_bot`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Presheaf.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Presheaf.lean#L34).

> A morphism of presheaves is locally injective with respect to the trivial topology if and only
> if it is injective.

```lean
lemma Presheaf.isLocallyInjective_bot {C : Type*} [Category* C] {A : Type*} [Category* A]
    {FA : A → A → Type*} {CA : A → Type*} [(X Y : A) → FunLike (FA X Y) (CA X) (CA Y)]
    [ConcreteCategory A FA] {F G : Cᵒᵖ ⥤ A} {f : F ⟶ G} :
    IsLocallyInjective ⊥ f ↔ ∀ X, Function.Injective (f.app X)
```

**`CategoryTheory.Presheaf.isLocallySurjective_bot`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Presheaf.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Presheaf.lean#L44).

> A morphism of presheaves is locally surjective with respect to the trivial topology if and only
> if it is surjective.

```lean
lemma Presheaf.isLocallySurjective_bot {C : Type*} [Category* C] {A : Type*} [Category* A]
    {FA : A → A → Type*} {CA : A → Type*} [(X Y : A) → FunLike (FA X Y) (CA X) (CA Y)]
    [ConcreteCategory A FA] {F G : Cᵒᵖ ⥤ A} {f : F ⟶ G} :
    IsLocallySurjective ⊥ f ↔ ∀ X, Function.Surjective (f.app X)
```

Declarations registered for the tag:

- [`Presheaf.IsLocallyInjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Presheaf.IsLocallyInjective#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Presheaf.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Presheaf.lean#L24) (StacksCore): “Mathlib defines a more generally property of being locally injective with respect to a Grothendieck topology; letting that be the trivial topology recovers the property of being injective.”.
- [`Presheaf.IsLocallySurjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Presheaf.IsLocallySurjective#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Presheaf.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Presheaf.lean#L27) (StacksCore): “Mathlib defines a more generally property of being locally surjective with respect to a Grothendieck topology; letting that be the trivial topology recovers the property of being surjective.”.

## Tag 00V7, a lemma

[Tag 00V7](https://stacks.math.columbia.edu/tag/00V7) in the Stacks Project.

**`CategoryTheory.Presheaf.isLocallyInjective_bot_iff_mono`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Presheaf.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Presheaf.lean#L69).

> A morphism of presheaves of types is injective if and only if it is a monomorphism.

```lean
lemma Presheaf.isLocallyInjective_bot_iff_mono {C : Type*} [Category* C] {F G : Cᵒᵖ ⥤ Type w}
    {f : F ⟶ G} : IsLocallyInjective ⊥ f ↔ Mono f
```

**`CategoryTheory.Presheaf.isLocallySurjective_bot_iff_epi`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Presheaf.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Presheaf.lean#L91). References: SGA 3 IV (6.7), “more general”.

> A morphism of presheaves of types is surjective if and only if it is an epimorphism.

```lean
lemma Presheaf.isLocallySurjective_bot_iff_epi {C : Type*} [Category* C] {F G : Cᵒᵖ ⥤ Type w}
    {f : F ⟶ G} : IsLocallySurjective ⊥ f ↔ Epi f
```

**`CategoryTheory.Presheaf.isIso_iff_isLocallyBijective`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Presheaf.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Presheaf.lean#L98). References: SGA 4 I (3.3), “mono + epi => iso”.

> A morphism of presheaves of types is an isomorphism if and only if it is both injective and
> surjective.

```lean
lemma Presheaf.isIso_iff_isLocallyBijective {C : Type*} [Category* C] {F G : Cᵒᵖ ⥤ Type w}
    {f : F ⟶ G} : IsIso f ↔ IsLocallyInjective ⊥ f ∧ IsLocallySurjective ⊥ f
```

## Tag 00V8, a definition

[Tag 00V8](https://stacks.math.columbia.edu/tag/00V8) in the Stacks Project.

Declarations registered for the tag:

- [`Subfunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Subfunctor#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Presheaf.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Presheaf.lean#L102) (StacksCore).

## Tag 00V9, a lemma

[Tag 00V9](https://stacks.math.columbia.edu/tag/00V9) in the Stacks Project.

**`CategoryTheory.Presheaf.existsUnique_subfunctor_surjective_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/RangeFactorization.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/RangeFactorization.lean#L65). The attribute's comment: “The unique subpresheaf `G' ⊆ G` through which `φ : F ⟶ G` factors with objectwise surjective first map, stated as `∃!` over `Subfunctor G`; the witness is the pointwise image `Subfunctor.range φ` with `Subfunctor.toRange φ`.”. References: SGA 3 VIB (7.3.0).

> **Stacks 00V9.** A map of presheaves of sets `φ : F ⟶ G` factors as `F ⟶ G' ⟶ G` with
> `G' ⊆ G` a subpresheaf and the first map surjective on sections over every object, and the
> subpresheaf `G'` doing this is unique: it is the pointwise image `U ↦ φ_U (F(U))` of `φ`.

```lean
theorem existsUnique_subfunctor_surjective_factorization (φ : F ⟶ G) :
    ∃! G' : Subfunctor G, ∃ ψ : F ⟶ G'.toFunctor,
      (∀ U, Function.Surjective (ψ.app U)) ∧ ψ ≫ G'.ι = φ
```

## Tag 00VA, a definition

[Tag 00VA](https://stacks.math.columbia.edu/tag/00VA) in the Stacks Project.

Declarations registered for the tag:

- [`Subfunctor.range`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Subfunctor.range#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Presheaf.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Presheaf.lean#L108) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.3, Tag 00V5](https://stacks.math.columbia.edu/tag/00V5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
