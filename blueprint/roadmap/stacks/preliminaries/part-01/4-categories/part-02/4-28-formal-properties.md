---
declaration: section
origin: cited
lean: NatTrans.hcomp, CategoryTheory.NatTrans.vcomp_hcomp_formal_properties
statement: formalized
proof: formalized
---

# 4.28 Formal properties

Section 4.28 of the Stacks Project, [Tag 003D](https://stacks.math.columbia.edu/tag/003D). 2 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 003E, a definition

[Tag 003E](https://stacks.math.columbia.edu/tag/003E) in the Stacks Project.

Declarations registered for the tag:

- [`NatTrans.hcomp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=NatTrans.hcomp#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Basic.lean#L89) (StacksCore).

## Tag 003F, a lemma

[Tag 003F](https://stacks.math.columbia.edu/tag/003F) in the Stacks Project.

**`CategoryTheory.NatTrans.vcomp_hcomp_formal_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Bicategory/FormalProperties.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Bicategory/FormalProperties.lean#L53).

> **Stacks 003F** (formal properties of vertical and horizontal composition). For natural
> transformations between functors of arbitrary categories:
> 1. vertical composition `≫` and horizontal composition `◫` are associative;
> 2. the identity transformations `𝟙 F` are units for `≫`;
> 3. the identity transformations `𝟙 (𝟭 A)` of identity functors are units for `◫` and `≫`;
> 4. the interchange law `(t ≫ t') ◫ (s ≫ s') = (t ◫ s) ≫ (t' ◫ s')` holds.
>
> Here `≫` is the Stacks `∘` in diagram order and `t ◫ s` is the Stacks `s ⋆ t`.

```lean
theorem vcomp_hcomp_formal_properties :
    -- (1) associativity of `≫`
    (∀ {F G H K : A ⥤ B} (a : F ⟶ G) (b : G ⟶ H) (c : H ⟶ K),
      (a ≫ b) ≫ c = a ≫ b ≫ c) ∧
    -- (1) associativity of `◫`
    (∀ {F F' : A ⥤ B} {G G' : B ⥤ C} {H H' : C ⥤ D}
      (t : F ⟶ F') (s : G ⟶ G') (r : H ⟶ H'), (t ◫ s) ◫ r = t ◫ (s ◫ r)) ∧
    -- (2) `𝟙 F` is a unit for `≫`
    (∀ {F G : A ⥤ B} (t : F ⟶ G), 𝟙 F ≫ t = t ∧ t ≫ 𝟙 G = t) ∧
    -- (3) `𝟙 (𝟭 A)` is a unit for `◫`
    (∀ {F F' : A ⥤ B} (t : F ⟶ F'), 𝟙 (𝟭 A) ◫ t = t ∧ t ◫ 𝟙 (𝟭 B) = t) ∧
    -- (3) `𝟙 (𝟭 A)` is a unit for `≫`
    (∀ {G : A ⥤ A} (u : 𝟭 A ⟶ G) (w : G ⟶ 𝟭 A), 𝟙 (𝟭 A) ≫ u = u ∧ w ≫ 𝟙 (𝟭 A) = w) ∧
    -- (4) the interchange law
    (∀ {F F' F'' : A ⥤ B} {G G' G'' : B ⥤ C}
      (t : F ⟶ F') (t' : F' ⟶ F'') (s : G ⟶ G') (s' : G' ⟶ G''),
      (t ≫ t') ◫ (s ≫ s') = (t ◫ s) ≫ (t' ◫ s'))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.28, Tag 003D](https://stacks.math.columbia.edu/tag/003D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
