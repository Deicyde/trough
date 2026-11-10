---
declaration: section
origin: cited
lean: preservesFiniteLimits_sheafFiber, StacksStalk.nbh_isCofiltered, StacksStalk.sheafStalkFunctor_preservesFiniteLimits, CategoryTheory.GrothendieckTopology.Point.ofPreservesFiniteLimits, CategoryTheory.GrothendieckTopology.Point.equivFiber, Counterexample.u_not_point
statement: formalized
proof: formalized
---

# 7.33 Constructing points

Section 7.33 of the Stacks Project, [Tag 05UZ](https://stacks.math.columbia.edu/tag/05UZ). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F4E, a lemma

[Tag 0F4E](https://stacks.math.columbia.edu/tag/0F4E) in the Stacks Project.

**`preservesFiniteLimits_sheafFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkIso.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/StalkIso.lean#L27).

> **Stacks 0F4E.** Let `Φ` be a point of the site `(C, J)`, i.e. a functor `u : C ⥤ Type`
> together with cofilteredness of its category of neighbourhoods. Then the stalk functor
> `Sh(C) ⥤ Set` at `Φ` is left exact, i.e. it preserves finite limits.

```lean
theorem preservesFiniteLimits_sheafFiber
    {C : Type u} [SmallCategory C] {J : GrothendieckTopology C}
    (Φ : J.Point) :
    Limits.PreservesFiniteLimits (Φ.sheafFiber (A := Type u))
```

## Tag 00YB, a lemma

[Tag 00YB](https://stacks.math.columbia.edu/tag/00YB) in the Stacks Project.

**`StacksStalk.nbh_isCofiltered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/NeighbourhoodsCofiltered.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/NeighbourhoodsCofiltered.lean#L70). The attribute's comment: “(1)”. References: SGA 4 IV (6.8.2), “special case”; SGA 4 IV (6.8.5), “partial”.

> Statement 1 (Main, tag `00YB`): under the hypotheses, the category of
> neighbourhoods `Nbh(p)` of `p` is cofiltered.

```lean
theorem nbh_isCofiltered [HasTerminal C] [HasPullbacks C]
    (u : C ⥤ Type w) (hu : IsPoint u) : IsCofiltered u.Elements
```

**`StacksStalk.sheafStalkFunctor_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/NeighbourhoodsCofiltered.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/NeighbourhoodsCofiltered.lean#L106). The attribute's comment: “(2)”.

> Statement 2 (Consequence, tag `00YB`): under the hypotheses, the stalk
> functor on sheaves commutes with finite limits, i.e. it is left exact.

```lean
theorem sheafStalkFunctor_preservesFiniteLimits
    [HasTerminal C] [HasPullbacks C] (J : GrothendieckTopology C)
    (u : C ⥤ Type w) (hu : IsPoint u) :
    PreservesFiniteLimits
      (sheafToPresheaf J (Type w) ⋙ CategoryTheory.elementColimit u (Type w))
```

## Tag 00YC, a proposition

[Tag 00YC](https://stacks.math.columbia.edu/tag/00YC) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.ofPreservesFiniteLimits`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OfPreservesFiniteLimits.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/OfPreservesFiniteLimits.lean#L104). References: SGA 4 IV (6.3), “left exact ⇒ point”.

> On a site in which finite limits exist, the point with fiber functor `u : C ⥤ Type w`, for
> `u` commuting with finite limits, with initially small category of elements, and jointly
> surjective on covering sieves.

```lean
def ofPreservesFiniteLimits (u : C ⥤ Type w) [PreservesFiniteLimits u]
    [InitiallySmall.{w} u.Elements] (hu : u.CoveringJointlySurjective J) :
    Point.{w} J
```

**`CategoryTheory.GrothendieckTopology.Point.equivFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OfPreservesFiniteLimits.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/OfPreservesFiniteLimits.lean#L124). References: SGA 4 IV (6.3), “characterization”.

> Let `C` be a site in which finite limits exist. Then the points of `C`
> correspond bijectively to the functors `u : C ⥤ Type w` such that
>
> 1. `u` commutes with finite limits, and
> 2. `∐ u(U_i) → u(U)` is surjective for every covering `{U_i → U}`
>    (in the sieve form `Functor.CoveringJointlySurjective`), and whose category of elements is
>    initially small,
>
> the bijection being `Φ ↦ Φ.fiber` in one direction and `ofPreservesFiniteLimits` in the
> other.

```lean
noncomputable def equivFiber :
    Point.{w} J ≃ {u : C ⥤ Type w //
      InitiallySmall.{w} u.Elements ∧ PreservesFiniteLimits u ∧
        u.CoveringJointlySurjective J}
```

## Tag 00YD, a remark

[Tag 00YD](https://stacks.math.columbia.edu/tag/00YD) in the Stacks Project.

**`Counterexample.u_not_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/NonExactStalkCounterexample.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/NonExactStalkCounterexample.lean#L534).

> **Statement 3.** Because the stalk functor `ℱ ↦ ℱ_p` fails to preserve
> monomorphisms (Statement 2), it fails to be left exact.

```lean
theorem u_not_point : ¬ PreservesFiniteLimits stalkFunctor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.33, Tag 05UZ](https://stacks.math.columbia.edu/tag/05UZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
