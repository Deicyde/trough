---
declaration: section
origin: cited
lean: Stacks.Injectives.IsGenerator, Stacks.Injectives.isGenerator_iff_subobject, Stacks.Injectives.isGenerator_iff_isSeparator, Stacks.Injectives.isGrothendieckAbelian_iff_ab5_and_exists_isGenerator
statement: formalized
proof: formalized
---

# 19.10 Grothendieck's AB conditions

Section 19.10 of the Stacks Project, [Tag 079A](https://stacks.math.columbia.edu/tag/079A). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 079B, a definition

[Tag 079B](https://stacks.math.columbia.edu/tag/079B) in the Stacks Project.

**`Stacks.Injectives.IsGenerator`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L84). The attribute's comment: “generator”.

> An object `U` of `C` is a *generator* if for every `N ⊂ M` with `N ≠ M` there is a morphism
> `U ⟶ M` which does not factor through `N`. A subobject `N ⊂ M` is given by a monomorphism
> `i : N ⟶ M`, and `N ≠ M` says that `i` is not an isomorphism.
>
> Mathlib has no name for this condition; it uses `CategoryTheory.IsSeparator` instead, with which
> this agrees by `Stacks.Injectives.isGenerator_iff_isSeparator`.

```lean
def IsGenerator (U : C) : Prop
```

**`Stacks.Injectives.isGenerator_iff_subobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L92). The attribute's comment: “generator as a subobject condition”.

> The definition of a generator, phrased with subobjects: `U` is a generator if and only if for
> every object `M` and every subobject `N` of `M` other than `M` itself there is a morphism `U ⟶ M`
> which does not factor through `N`.

```lean
theorem isGenerator_iff_subobject (U : C) :
    IsGenerator U ↔ ∀ (M : C) (N : Subobject M), N ≠ ⊤ →
      ∃ u : U ⟶ M, ∀ v : U ⟶ (N : C), v ≫ N.arrow ≠ u
```

**`Stacks.Injectives.isGenerator_iff_isSeparator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L116). The attribute's comment: “generator is separator”.

> A generator in the sense of the Stacks project is the same thing as a separator in the sense of
> Mathlib: morphisms out of `U` see every proper subobject if and only if they distinguish parallel
> morphisms.
>
> From left to right: if `f : X ⟶ Y` is killed by every morphism `U ⟶ X` then every such morphism
> factors through `ker f`, which therefore cannot be a proper subobject of `X`, so `f = 0`. From
> right to left: if `i : N ⟶ M` is a monomorphism through which every morphism `U ⟶ M` factors, then
> every morphism `U ⟶ M` is killed by `coker i ≠ 0`, so `i` is an epimorphism and hence, `C` being
> balanced, an isomorphism.

```lean
theorem isGenerator_iff_isSeparator (U : C) : IsGenerator U ↔ IsSeparator U
```

**`Stacks.Injectives.isGrothendieckAbelian_iff_ab5_and_exists_isGenerator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L151). The attribute's comment: “Grothendieck abelian category”.

> An abelian category is a *Grothendieck abelian category* if it has AB5 and a generator. Both
> sides are expressed with Mathlib's vocabulary: AB5 at size `v` is
> `CategoryTheory.AB5OfSize.{v, v}`, and `CategoryTheory.IsGrothendieckAbelian.{v}` is Mathlib's
> class.
>
> The equivalence is stated at `w = v`, for `v` the hom universe of `C`, because Mathlib's class
> carries the further requirement `LocallySmall.{w} C`, which has no counterpart in the Stacks
> definition and is vacuous exactly for that choice of `w`. The hypothesis that filtered colimits of
> size `v` exist is part of AB5 as the Stacks project states it, AB5 being AB3 together with
> exactness of filtered colimits; in Mathlib it is the instance argument of
> `CategoryTheory.AB5OfSize`, so it has to be assumed on both sides at once.

```lean
theorem isGrothendieckAbelian_iff_ab5_and_exists_isGenerator
    [HasFilteredColimitsOfSize.{v, v} C] :
    CategoryTheory.IsGrothendieckAbelian.{v} C ↔
      (CategoryTheory.AB5OfSize.{v, v} C ∧ ∃ U : C, IsGenerator U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.10, Tag 079A](https://stacks.math.columbia.edu/tag/079A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
