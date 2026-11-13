---
declaration: section
origin: cited
lean: Functor.additive_of_mono_biprodComparison, Functor.additive_of_epi_biprodComparison', CategoryTheory.Functor.additive_of_isIso_biprodComparison, CategoryTheory.Functor.additive_of_isIso_biprodComparison', CategoryTheory.Functor.tfae_additive, Functor.preservesFiniteBiproductsOfAdditive, preservesBinaryBiproducts_of_preservesBiproducts, Functor.mapBiprod
statement: formalized
proof: formalized
---

# 12.7 Additive functors

Section 12.7 of the Stacks Project, [Tag 010M](https://stacks.math.columbia.edu/tag/010M). 3 tags here are carried by 9 declarations of the repository (2 in StacksCore and 7 in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DLP, a lemma

[Tag 0DLP](https://stacks.math.columbia.edu/tag/0DLP) in the Stacks Project.

**`Functor.additive_of_mono_biprodComparison`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L22). The attribute's comment: “(3) => (1)”.

```lean
lemma Functor.additive_of_mono_biprodComparison [HasBinaryBiproducts C] [HasBinaryBiproducts D]
    (G : C ⥤ D) [G.PreservesZeroMorphisms] (h : ∀ X Y : C, Mono (G.biprodComparison X Y)) :
    G.Additive
```

**`Functor.additive_of_epi_biprodComparison'`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L29). The attribute's comment: “(2) => (1)”.

```lean
lemma Functor.additive_of_epi_biprodComparison' [HasBinaryBiproducts C] [HasBinaryBiproducts D]
    (G : C ⥤ D) [G.PreservesZeroMorphisms] (h : ∀ X Y : C, Epi (G.biprodComparison' X Y)) :
    G.Additive
```

**`CategoryTheory.Functor.additive_of_isIso_biprodComparison`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/AdditiveFunctorTFAE.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/AdditiveFunctorTFAE.lean#L67). The attribute's comment: “(3) => (1)”.

> Stacks 0DLP (3) ⇒ (1): a functor between preadditive categories with zero objects and binary
> biproducts is additive if the comparison maps `G.obj (X ⊞ Y) ⟶ G.obj X ⊞ G.obj Y` are
> isomorphisms. That `G` preserves zero morphisms is deduced from the case `X = Y = 0`.

```lean
lemma additive_of_isIso_biprodComparison
    (h : ∀ X Y : C, IsIso (G.biprodComparison X Y)) : G.Additive
```

**`CategoryTheory.Functor.additive_of_isIso_biprodComparison'`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/AdditiveFunctorTFAE.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/AdditiveFunctorTFAE.lean#L77). The attribute's comment: “(2) => (1)”.

> Stacks 0DLP (2) ⇒ (1): a functor between preadditive categories with zero objects and binary
> biproducts is additive if the comparison maps `G.obj X ⊞ G.obj Y ⟶ G.obj (X ⊞ Y)` are
> isomorphisms. That `G` preserves zero morphisms is deduced from the case `X = Y = 0`.

```lean
lemma additive_of_isIso_biprodComparison'
    (h : ∀ X Y : C, IsIso (G.biprodComparison' X Y)) : G.Additive
```

**`CategoryTheory.Functor.tfae_additive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/AdditiveFunctorTFAE.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/AdditiveFunctorTFAE.lean#L89).

> Stacks 0DLP: for a functor `G` between preadditive categories with zero objects and binary
> biproducts (e.g. additive categories), the following are equivalent:
> 1. `G` is additive;
> 2. the comparison maps `G.obj X ⊞ G.obj Y ⟶ G.obj (X ⊞ Y)` are isomorphisms;
> 3. the comparison maps `G.obj (X ⊞ Y) ⟶ G.obj X ⊞ G.obj Y` are isomorphisms.

```lean
theorem tfae_additive :
    List.TFAE [G.Additive, ∀ X Y : C, IsIso (G.biprodComparison' X Y),
      ∀ X Y : C, IsIso (G.biprodComparison X Y)]
```

Declarations registered for the tag:

- [`Functor.preservesFiniteBiproductsOfAdditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Functor.preservesFiniteBiproductsOfAdditive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L17) (StacksCore).
- [`preservesBinaryBiproducts_of_preservesBiproducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=preservesBinaryBiproducts_of_preservesBiproducts#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L18) (StacksCore).
- [`Functor.mapBiprod`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Functor.mapBiprod#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L19) (StacksCore): “1 => 2 and 1 => 3”.

## Tag 010N, a lemma

[Tag 010N](https://stacks.math.columbia.edu/tag/010N) in the Stacks Project.

**`CategoryTheory.Functor.preservesFiniteLimits_iff_forall_shortExact_exists_exact_and_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ShortComplex/ExactFunctor.lean#L94). The attribute's comment: “part 2, for an arbitrary (not necessarily additive) functor”.

> **Stacks 010N (2)**, for an arbitrary functor: a functor `F` between abelian categories is
> left exact if and only if for every short exact sequence `0 → A → B → C → 0` the sequence
> `0 → F(A) → F(B) → F(C)` is exact. `F` is not assumed additive.

```lean
theorem preservesFiniteLimits_iff_forall_shortExact_exists_exact_and_mono (F : C ⥤ D) :
    PreservesFiniteLimits F ↔ ∀ S : ShortComplex C, S.ShortExact →
      ∃ w : F.map S.f ≫ F.map S.g = 0, (ShortComplex.mk _ _ w).Exact ∧ Mono (F.map S.f)
```

**`CategoryTheory.Functor.preservesFiniteColimits_iff_forall_shortExact_exists_exact_and_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ShortComplex/ExactFunctor.lean#L110). The attribute's comment: “part 3, for an arbitrary (not necessarily additive) functor”.

> **Stacks 010N (3)**, for an arbitrary functor: a functor `F` between abelian categories is
> right exact if and only if for every short exact sequence `0 → A → B → C → 0` the sequence
> `F(A) → F(B) → F(C) → 0` is exact. `F` is not assumed additive.

```lean
theorem preservesFiniteColimits_iff_forall_shortExact_exists_exact_and_epi (F : C ⥤ D) :
    PreservesFiniteColimits F ↔ ∀ S : ShortComplex C, S.ShortExact →
      ∃ w : F.map S.f ≫ F.map S.g = 0, (ShortComplex.mk _ _ w).Exact ∧ Epi (F.map S.g)
```

**`CategoryTheory.Functor.exact_iff_forall_shortExact_exists_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ShortComplex/ExactFunctor.lean#L127). The attribute's comment: “part 4, for an arbitrary (not necessarily additive) functor”.

> **Stacks 010N (4)**, for an arbitrary functor: a functor `F` between abelian categories is
> exact (preserves finite limits and finite colimits) if and only if for every short exact sequence
> `0 → A → B → C → 0` the sequence `0 → F(A) → F(B) → F(C) → 0` is exact. `F` is not assumed
> additive.

```lean
theorem exact_iff_forall_shortExact_exists_shortExact (F : C ⥤ D) :
    PreservesFiniteLimits F ∧ PreservesFiniteColimits F ↔ ∀ S : ShortComplex C, S.ShortExact →
      ∃ w : F.map S.f ≫ F.map S.g = 0, (ShortComplex.mk _ _ w).ShortExact
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.preservesFiniteLimits_iff_forall_exact_map_and_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesFiniteLimits_iff_forall_exact_map_and_mono#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean#L13) (StacksCore): “part 2”.
- [`CategoryTheory.Functor.preservesFiniteColimits_iff_forall_exact_map_and_epi`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesFiniteColimits_iff_forall_exact_map_and_epi#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean#L15) (StacksCore): “part 3”.
- [`CategoryTheory.Functor.exact_tfae`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.exact_tfae#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean#L17) (StacksCore): “part 4”.
- [`CategoryTheory.AdditiveFunctor.ofLeftExact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.AdditiveFunctor.ofLeftExact#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L35) (StacksCore): “part 1 (i)”.
- [`CategoryTheory.AdditiveFunctor.ofRightExact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.AdditiveFunctor.ofRightExact#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L36) (StacksCore): “part 1 (ii)”.

## Tag 010O, a lemma

[Tag 010O](https://stacks.math.columbia.edu/tag/010O) in the Stacks Project.

**`CategoryTheory.Functor.mapExtAddHom_one_extClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/MapExactFunctor.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/MapExactFunctor.lean#L41). The attribute's comment: “The group homomorphism is `CategoryTheory.Functor.mapExtAddHom` in degree one; `Ext¹` is the group of extensions by `CategoryTheory.Abelian.Ext.extClass`.”.

> **Stacks 010O.** An exact functor `F : C ⥤ D` of abelian categories induces, for all objects
> `A, B` of `C`, the abelian group homomorphism `F.mapExtAddHom B A 1 : Ext¹(B, A) →+
> Ext¹(F B, F A)`, and it maps the class of an extension `0 → A → E → B → 0` to the class of the
> extension `0 → F A → F E → F B → 0`.

```lean
theorem Functor.mapExtAddHom_one_extClass (F : C ⥤ D) [F.Additive]
    [PreservesFiniteLimits F] [PreservesFiniteColimits F] {E : ShortComplex C}
    (hE : E.ShortExact) :
    F.mapExtAddHom E.X₃ E.X₁ 1 hE.extClass = (hE.map_of_exact F).extClass
```

Declarations registered for the tag:

- [`CategoryTheory.Abelian.Ext.mapExactFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.mapExactFunctor#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/DerivedCategory/Ext/Map.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/DerivedCategory/Ext/Map.lean#L8) (StacksCore). References: SGA 6 II (2.1.3).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.7, Tag 010M](https://stacks.math.columbia.edu/tag/010M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
