---
declaration: section
origin: cited
lean: hasRightInverse_iff_isLocallySurjective_surjective, CategoryTheory.GrothendieckTopology.IsWeaklyContractible, CategoryTheory.GrothendieckTopology.HasEnoughObjects, CategoryTheory.GrothendieckTopology.HasEnoughWeaklyContractibleObjects
statement: formalized
proof: formalized
---

# 7.40 Weakly contractible objects

Section 7.40 of the Stacks Project, [Tag 090J](https://stacks.math.columbia.edu/tag/090J). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 090K, a lemma

[Tag 090K](https://stacks.math.columbia.edu/tag/090K) in the Stacks Project.

**`hasRightInverse_iff_isLocallySurjective_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/WeaklyContractible/Objects.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/WeaklyContractible/Objects.lean#L241).

> Let `C` be a site with Grothendieck topology `J`, and let `U`
> be an object of `C`. The following are equivalent.
>
> 1. For every covering `{U_i → U}_{i ∈ I}` of `U`, the sheafified covering map
>    `π^# : ∐ h_{U_i}^# ⟶ h_U^#` admits a right inverse (a section) `σ`, i.e.
>    `σ ≫ π^# = 𝟙`.
>
> 2. For every surjection (locally surjective morphism) of sheaves of sets `φ : F ⟶ G`,
>    the induced map on sections over `U`, `φ_U : F(U) → G(U)`, is surjective.

```lean
theorem hasRightInverse_iff_isLocallySurjective_surjective :
    (∀ (I : Type v) (Ui : I → C) (f : ∀ i, Ui i ⟶ U),
        (Sieve.ofArrows Ui f) ∈ J U → Stacks.WeaklyContractible.HasRightInverse J Ui f) ↔
    (∀ (F G : Sheaf J (Type v)) (φ : F ⟶ G), Sheaf.IsLocallySurjective φ →
        Function.Surjective ((sheafToPresheaf J (Type v)).map φ |>.app (op U)))
```

## Tag 090L, a definition

[Tag 090L](https://stacks.math.columbia.edu/tag/090L) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.IsWeaklyContractible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/WeaklyContractible.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/WeaklyContractible.lean#L52). The attribute's comment: “(1)”.

> An object `U` of a site `C` is *weakly contractible* if every surjection of sheaves of sets on
> `C` is surjective on sections over `U`.

```lean
def IsWeaklyContractible (U : C) : Prop
```

**`CategoryTheory.GrothendieckTopology.HasEnoughObjects`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/WeaklyContractible.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/WeaklyContractible.lean#L68). The attribute's comment: “(3)”.

> A site `C` *has enough `P` objects*, for a property `P` of objects of `C`, if every object
> `U` of `C` has a covering `{U_i → U}` with `P (U_i)` for all `i`.

```lean
def HasEnoughObjects (P : ObjectProperty C) : Prop
```

**`CategoryTheory.GrothendieckTopology.HasEnoughWeaklyContractibleObjects`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/WeaklyContractible.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/WeaklyContractible.lean#L75). The attribute's comment: “(2)”.

> A site `C` *has enough weakly contractible objects* if every object has a covering by weakly
> contractible objects, i.e. if it has enough `IsWeaklyContractible` objects.

```lean
def HasEnoughWeaklyContractibleObjects : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.40, Tag 090J](https://stacks.math.columbia.edu/tag/090J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
