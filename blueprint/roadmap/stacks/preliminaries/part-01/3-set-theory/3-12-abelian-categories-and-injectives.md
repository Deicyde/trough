---
declaration: section
origin: cited
lean: exists_small_abelian_subcategory_with_enough_injectives
statement: formalized
proof: formalized
---

# 3.12 Abelian categories and injectives

Section 3.12 of the Stacks Project, [Tag 000Z](https://stacks.math.columbia.edu/tag/000Z). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0010, a lemma

[Tag 0010](https://stacks.math.columbia.edu/tag/0010) in the Stacks Project.

**`exists_small_abelian_subcategory_with_enough_injectives`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/SmallSubcategory.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/SmallSubcategory.lean#L126).

> **Stacks 0010**. Let `𝒜` be an abelian category with enough injectives and
> `A : S → 𝒜` a family of objects. There is an object property `P` whose full subcategory
> `𝒜' = P.FullSubcategory` has a set of objects, contains every `A s`, and admits an
> abelian structure for which the inclusion `P.ι` is additive and exact, `𝒜'` has enough
> injectives, and an object of `𝒜'` is injective there if and only if it is injective
> in `𝒜`.

```lean
theorem exists_small_abelian_subcategory_with_enough_injectives (A : S → 𝒜) :
    ∃ (P : ObjectProperty 𝒜),
      Small.{max v w} P.FullSubcategory ∧
      (∀ s, P (A s)) ∧
      ∃ (_ : Abelian P.FullSubcategory),
        P.ι.Additive ∧
        Nonempty (PreservesFiniteLimits P.ι) ∧
        Nonempty (PreservesFiniteColimits P.ι) ∧
        EnoughInjectives P.FullSubcategory ∧
        ∀ X : P.FullSubcategory, Injective X ↔ Injective (P.ι.obj X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 3.12, Tag 000Z](https://stacks.math.columbia.edu/tag/000Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
