---
declaration: section
origin: cited
lean: Stacks.Injectives.IsGenerator, Stacks.Injectives.isGenerator_iff_subobject, Stacks.Injectives.isGenerator_iff_isSeparator, Stacks.Injectives.isGrothendieckAbelian_iff_ab5_and_exists_isGenerator, Stacks.Injectives.AB3, Stacks.Injectives.AB4, Stacks.Injectives.AB5, Stacks.Injectives.AB3Star
statement: formalized
proof: formalized
---

# 19.10 Grothendieck's AB conditions

Section 19.10 of the Stacks Project, [Tag 079A](https://stacks.math.columbia.edu/tag/079A). 1 tag here is carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 079B, a definition

[Tag 079B](https://stacks.math.columbia.edu/tag/079B) in the Stacks Project.

**`Stacks.Injectives.IsGenerator`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L93). The attribute's comment: “generator”.

> An object `U` of `C` is a *generator* if for every `N ⊂ M` with `N ≠ M` there is a morphism
> `U ⟶ M` which does not factor through `N`. A subobject `N ⊂ M` is given by a monomorphism
> `i : N ⟶ M`, and `N ≠ M` says that `i` is not an isomorphism.
>
> Mathlib has no name for this condition; it uses `CategoryTheory.IsSeparator` instead, with which
> this agrees by `Stacks.Injectives.isGenerator_iff_isSeparator`.

```lean
def IsGenerator (U : C) : Prop
```

**`Stacks.Injectives.isGenerator_iff_subobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L101). The attribute's comment: “generator as a subobject condition”.

> The definition of a generator, phrased with subobjects: `U` is a generator if and only if for
> every object `M` and every subobject `N` of `M` other than `M` itself there is a morphism `U ⟶ M`
> which does not factor through `N`.

```lean
theorem isGenerator_iff_subobject (U : C) :
    IsGenerator U ↔ ∀ (M : C) (N : Subobject M), N ≠ ⊤ →
      ∃ u : U ⟶ M, ∀ v : U ⟶ (N : C), v ≫ N.arrow ≠ u
```

**`Stacks.Injectives.isGenerator_iff_isSeparator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L125). The attribute's comment: “generator is separator”.

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

**`Stacks.Injectives.isGrothendieckAbelian_iff_ab5_and_exists_isGenerator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L160). The attribute's comment: “Grothendieck abelian category”.

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

**`Stacks.Injectives.AB3`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L188). The attribute's comment: “AB3”.

> **AB3**: `C` has direct sums, i.e. coproducts indexed by every type in `Type w`.

```lean
def AB3 : Prop
```

**`Stacks.Injectives.AB4`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L192). The attribute's comment: “AB4”.

> **AB4**: `C` has AB3 and direct sums are exact.

```lean
def AB4 : Prop
```

**`Stacks.Injectives.AB5`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L199). The attribute's comment: “AB5”.

> **AB5**: `C` has AB3 and filtered colimits are exact. Filtered colimits exist as soon as AB3
> holds, `C` having coequalizers
> (`CategoryTheory.Limits.has_colimits_of_hasCoequalizers_and_coproducts`, [Stacks, Tag 002P]);
> exactness is `CategoryTheory.AB5OfSize`.

```lean
def AB5 : Prop
```

**`Stacks.Injectives.AB3Star`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L206). The attribute's comment: “AB3*”.

> **AB3\***: `C` has products, indexed by every type in `Type w`.

```lean
def AB3Star : Prop
```

**`Stacks.Injectives.AB4Star`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L210). The attribute's comment: “AB4*”.

> **AB4\***: `C` has AB3\* and products are exact.

```lean
def AB4Star : Prop
```

**`Stacks.Injectives.AB5Star`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L217). The attribute's comment: “AB5*”.

> **AB5\***: `C` has AB3\* and cofiltered limits are exact. Cofiltered limits exist as soon as
> AB3\* holds, `C` having equalizers
> (`CategoryTheory.Limits.has_limits_of_hasEqualizers_and_products`, [Stacks, Tag 002N]);
> exactness is `CategoryTheory.AB5StarOfSize`.

```lean
def AB5Star : Prop
```

**`Stacks.Injectives.ab3_iff_hasColimitsOfSize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L224). The attribute's comment: “AB3 gives all colimits”.

> AB3 is the existence of all colimits of size `w` ([Stacks, Tag 002P]).

```lean
theorem ab3_iff_hasColimitsOfSize : AB3.{w} C ↔ HasColimitsOfSize.{w, w} C
```

**`Stacks.Injectives.ab3Star_iff_hasLimitsOfSize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L231). The attribute's comment: “AB3* gives all limits”.

> AB3\* is the existence of all limits of size `w` ([Stacks, Tag 002N]).

```lean
theorem ab3Star_iff_hasLimitsOfSize : AB3Star.{w} C ↔ HasLimitsOfSize.{w, w} C
```

**`Stacks.Injectives.ab4_iff_ab4OfSize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L239). The attribute's comment: “AB4 in Mathlib's terms”.

> On a category with direct sums, AB4 is Mathlib's `CategoryTheory.AB4OfSize`.

```lean
theorem ab4_iff_ab4OfSize [HasCoproducts.{w} C] : AB4.{w} C ↔ CategoryTheory.AB4OfSize.{w} C
```

**`Stacks.Injectives.ab5_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L244). The attribute's comment: “AB5 in Mathlib's terms”.

> AB5 is AB3 together with Mathlib's `CategoryTheory.AB5OfSize`.

```lean
theorem ab5_iff [HasFilteredColimitsOfSize.{w, w} C] :
    AB5.{w} C ↔ HasCoproducts.{w} C ∧ CategoryTheory.AB5OfSize.{w, w} C
```

**`Stacks.Injectives.ab4Star_iff_ab4StarOfSize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L251). The attribute's comment: “AB4* in Mathlib's terms”.

> On a category with products, AB4\* is Mathlib's `CategoryTheory.AB4StarOfSize`.

```lean
theorem ab4Star_iff_ab4StarOfSize [HasProducts.{w} C] :
    AB4Star.{w} C ↔ CategoryTheory.AB4StarOfSize.{w} C
```

**`Stacks.Injectives.ab5Star_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L257). The attribute's comment: “AB5* in Mathlib's terms”.

> AB5\* is AB3\* together with Mathlib's `CategoryTheory.AB5StarOfSize`.

```lean
theorem ab5Star_iff [HasCofilteredLimitsOfSize.{w, w} C] :
    AB5Star.{w} C ↔ HasProducts.{w} C ∧ CategoryTheory.AB5StarOfSize.{w, w} C
```

**`Stacks.Injectives.IsGrothendieckAbelianCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L274). The attribute's comment: “Grothendieck abelian category, Stacks definition”.

> **Grothendieck abelian category**: `C` has AB5 and a generator. The direct sums and filtered
> colimits of AB5 are indexed by sets in the hom universe `v` of `C`, the size at which the
> Stacks project's (locally small) categories live.

```lean
def IsGrothendieckAbelianCategory : Prop
```

**`Stacks.Injectives.isGrothendieckAbelianCategory_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L281). The attribute's comment: “Grothendieck abelian category, agreement with Mathlib”.

> A category is a Grothendieck abelian category in the sense of the Stacks project, that is it
> has AB5 and a generator, if and only if it is one in the sense of Mathlib,
> `CategoryTheory.IsGrothendieckAbelian.{v}` (locally small, exact filtered colimits of size `v`,
> a separator), with no further hypothesis.

```lean
theorem isGrothendieckAbelianCategory_iff :
    IsGrothendieckAbelianCategory C ↔ CategoryTheory.IsGrothendieckAbelian.{v} C
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.10, Tag 079A](https://stacks.math.columbia.edu/tag/079A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
