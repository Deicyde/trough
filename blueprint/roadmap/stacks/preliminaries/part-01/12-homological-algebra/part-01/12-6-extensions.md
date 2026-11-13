---
declaration: section
origin: cited
lean: CategoryTheory.Abelian.Extension, CategoryTheory.Abelian.Extension.Hom, CategoryTheory.Abelian.Extension.category, CategoryTheory.ShortComplex.ShortExact, CategoryTheory.Abelian.YonedaExt, CategoryTheory.Abelian.Ext, CategoryTheory.Abelian.YonedaExt.instAddCommGroup, CategoryTheory.Abelian.YonedaExt.functor
statement: formalized
proof: formalized
---

# 12.6 Extensions

Section 12.6 of the Stacks Project, [Tag 010I](https://stacks.math.columbia.edu/tag/010I). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 010J, a definition

[Tag 010J](https://stacks.math.columbia.edu/tag/010J) in the Stacks Project.

**`CategoryTheory.Abelian.Extension`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/Extension.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ShortComplex/Extension.lean#L34). The attribute's comment: “extensions of `B` by `A`”.

> An *extension of `B` by `A`* in an abelian category `𝒜`: a short exact sequence
> `0 → A → X → B → 0`, given by its middle term `X` and its maps `f : A ⟶ X` and `g : X ⟶ B`.

```lean
structure Extension (B A : 𝒜)
```

**`CategoryTheory.Abelian.Extension.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/Extension.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ShortComplex/Extension.lean#L69). The attribute's comment: “morphisms of extensions”.

> A *morphism of extensions* from `0 → A → E → B → 0` to `0 → A → F → B → 0`: a morphism
> `hom : E → F` of the middle terms making the ladder commute with the identity maps on `A` and
> on `B`, i.e. `E.f ≫ hom = F.f` and `hom ≫ F.g = E.g`.

```lean
structure Hom (E F : Extension B A)
```

**`CategoryTheory.Abelian.Extension.category`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/Extension.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ShortComplex/Extension.lean#L92). The attribute's comment: “the category of extensions of `B` by `A`”.

> The extensions of `B` by `A` form a category, whose morphisms are the morphisms of
> extensions `CategoryTheory.Abelian.Extension.Hom`.

```lean
instance category : Category (Extension B A)
```

Declarations registered for the tag:

- [`CategoryTheory.ShortComplex.ShortExact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.ShortExact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/ShortExact.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/ShortExact.lean#L26) (StacksCore). References: EGA 0 (12.3.2).

## Tag 010K, a definition

[Tag 010K](https://stacks.math.columbia.edu/tag/010K) in the Stacks Project.

**`CategoryTheory.Abelian.YonedaExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ExtensionClasses.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ExtensionClasses.lean#L90).

> **The Ext-group `Ext_𝒜(B, A)`.** For objects `A`, `B` of an abelian category `𝒜`, the set of
> isomorphism classes of extensions `0 → A → E → B → 0` of `B` by `A`, two extensions being
> isomorphic when there is an isomorphism of their middle terms compatible with the identities of
> `A` and `B`. (Stacks also registers 010K, in `StacksCore/`, on Mathlib's derived
> `CategoryTheory.Abelian.Ext`; `YonedaExt.equivExt` identifies the two in degree one.)

```lean
def YonedaExt (B A : C) : Type (max u v)
```

Declarations registered for the tag:

- [`CategoryTheory.Abelian.Ext`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/DerivedCategory/Ext/Basic.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/DerivedCategory/Ext/Basic.lean#L8) (StacksCore). References: SGA 4 V (2.1.1); SGA 4½ Etat 0 (3.2.1), “special case”; SGA 7 VII (3.2), “special case”.

## Tag 010L, a lemma

[Tag 010L](https://stacks.math.columbia.edu/tag/010L) in the Stacks Project.

**`CategoryTheory.Abelian.YonedaExt.instAddCommGroup`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ExtensionClassesBaerSum.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ExtensionClassesBaerSum.lean#L518). The attribute's comment: “the commutative group law: the Baer sum on the isomorphism classes of extensions of `B` by `A`, in an arbitrary abelian category”.

> **Stacks 010L**, the group law. The Baer sum `(E₁, E₂) ↦ E₁ + E₂` (push out `E₁ ⊕ E₂` along
> the sum map `A ⊕ A → A`, pull back along the diagonal `B → B ⊕ B`) is a commutative group law
> on `Ext_C(B, A)`, with zero the class of the split extension `A ⊕ B` and negation the pullback
> along `-𝟙 B`.

```lean
noncomputable instance instAddCommGroup : AddCommGroup (YonedaExt B A)
```

**`CategoryTheory.Abelian.YonedaExt.functor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ExtensionClassesBaerSum.lean, line 571](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ExtensionClassesBaerSum.lean#L571). The attribute's comment: “functoriality in both variables: pushout and pullback are group homomorphisms, functorial and commuting with each other”.

> **Stacks 010L**, functoriality. With the Baer sum, `(B, A) ↦ Ext_C(B, A)` is a functor
> `Cᵒᵖ ⥤ C ⥤ AddCommGrpCat`: a map `α : A → A'` acts by pushout along `α`, a map `β : B' → B`
> acts by pullback along `β`, these maps are group homomorphisms, compatible with identities and
> composition, and pushouts commute with pullbacks.

```lean
noncomputable def functor : Cᵒᵖ ⥤ C ⥤ AddCommGrpCat.{max u v}
```

Declarations registered for the tag:

- [`CategoryTheory.Abelian.extFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.extFunctor#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/DerivedCategory/Ext/Basic.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/DerivedCategory/Ext/Basic.lean#L9) (StacksCore). References: EGA 0 (12.3.1), “partial”; SGA 4½ Etat 0 (3.2.1), “special case”.

## Tag 05E2, a lemma

[Tag 05E2](https://stacks.math.columbia.edu/tag/05E2) in the Stacks Project.

**`CategoryTheory.Abelian.Ext.contravariant_hom_ext_one_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ConnectingSurjective.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ConnectingSurjective.lean#L121). The attribute's comment: “(1), with Mathlib's derived-category `Ext` in place of Yoneda extensions and `Hom(A, N)` as `Ext A N 0` (see `Ext.addEquiv₀`)”.

> **Stacks 05E2 (1).** For a short exact sequence `0 → X₁ → X₂ → X₃ → 0` and an object `N`,
> the sequence
> `0 → Hom(X₃, N) → Hom(X₂, N) → Hom(X₁, N) → Ext¹(X₃, N) → Ext¹(X₂, N) → Ext¹(X₁, N)`
> is exact: the six-term sequence `Ext⁰(X₃, N) → ⋯ → Ext¹(X₁, N)` is exact and its first map,
> precomposition with `X₂ → X₃`, is injective.

```lean
theorem contravariant_hom_ext_one_exact (N : C) :
    (contravariantSequence hS N 0 1 (add_zero 1)).Exact ∧
      Function.Injective ((mk₀ S.g).precomp N (zero_add 0))
```

**`CategoryTheory.Abelian.Ext.covariant_hom_ext_one_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ConnectingSurjective.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/ConnectingSurjective.lean#L134). The attribute's comment: “(2), with Mathlib's derived-category `Ext` in place of Yoneda extensions and `Hom(N, A)` as `Ext N A 0` (see `Ext.addEquiv₀`)”.

> **Stacks 05E2 (2).** For a short exact sequence `0 → X₁ → X₂ → X₃ → 0` and an object `N`,
> the sequence
> `0 → Hom(N, X₁) → Hom(N, X₂) → Hom(N, X₃) → Ext¹(N, X₁) → Ext¹(N, X₂) → Ext¹(N, X₃)`
> is exact: the six-term sequence `Ext⁰(N, X₁) → ⋯ → Ext¹(N, X₃)` is exact and its first map,
> postcomposition with `X₁ → X₂`, is injective.

```lean
theorem covariant_hom_ext_one_exact (N : C) :
    (covariantSequence N hS 0 1 (zero_add 1)).Exact ∧
      Function.Injective ((mk₀ S.f).postcomp N (add_zero 0))
```

Declarations registered for the tag:

- [`CategoryTheory.Abelian.Ext.covariantSequence_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.covariantSequence_exact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/DerivedCategory/Ext/ExactSequences.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/DerivedCategory/Ext/ExactSequences.lean#L8) (StacksCore). References: SGA 3 XV (2.10), “more general”; SGA 4 V (6.2), “Exactness of (6.2.1)”; SGA 4½ Etat 0 (1.1.2), “special case”; SGA 4½ Etat 0 (3.2.2), “special case”; SGA 7 VII (3.3.6), “partial”; SGA 7 VII (3.7.5), “special case”.
- [`CategoryTheory.Abelian.Ext.contravariantSequence_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.contravariantSequence_exact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch12.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch12.lean#L21) (StacksFrontier): “part (1): the contravariant long exact sequence of Ext groups attached to a short exact sequence.”. References: SGA 4 V (2.1.1), “partial”; SGA 4 V (6.2), “Exactness of (6.2.2)”; SGA 4½ Etat 0 (1.1.2), “special case”; SGA 4½ Etat 0 (3.2.2), “special case”; SGA 7 VII (3.4.9), “partial”; SGA 7 VII (3.7.5), “special case”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.6, Tag 010I](https://stacks.math.columbia.edu/tag/010I)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
