---
declaration: section
origin: cited
lean: Stacks.Cohomology.ProperBaseChange.isIso_properBaseChangeMap, Stacks.Cohomology.AbelianProperBaseChange.isIso_abelianBaseChange, Stacks.Topology.ProperBaseChange.isIso_properBaseChangeMap
statement: formalized
proof: formalized
---

# 20.18 Proper base change in topology

Section 20.18 of the Stacks Project, [Tag 09V4](https://stacks.math.columbia.edu/tag/09V4). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09V5, a lemma

[Tag 09V5](https://stacks.math.columbia.edu/tag/09V5) in the Stacks Project.

**`Stacks.Cohomology.ProperBaseChange.isIso_properBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/ProperBaseChangeAtAPoint.lean, line 746](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/ProperBaseChangeAtAPoint.lean#L746).

> **Proper base change in topology.** For a closed separated morphism of ringed
> spaces `f : X ⟶ Y` and a point `y` of `Y` with quasi-compact fibre, the canonical base-change
> morphism from the stalk at `y` of the derived direct image to the derived sections on the fibre
> is an isomorphism: for every bounded below complex `E` of `𝒪_X`-modules,
>
> `(Rf_* E)_y = RΓ(f⁻¹(y), E|_{f⁻¹(y)})`
>
> in the bounded below derived category of `𝒪_{Y,y}`-modules, naturally in `E`.

```lean
theorem isIso_properBaseChangeMap
    (hclosed : IsClosedMap (ConcreteCategory.hom f.hom.base))
    (hsep : IsSeparatedMap (ConcreteCategory.hom f.hom.base))
    (hcompact : IsCompact ((ConcreteCategory.hom f.hom.base) ⁻¹' ({y} : Set Y))) :
    IsIso (properBaseChangeMap f y)
```

## Tag 09V6, a theorem

[Tag 09V6](https://stacks.math.columbia.edu/tag/09V6) in the Stacks Project.

**`Stacks.Cohomology.AbelianProperBaseChange.isIso_abelianBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/AbelianProperBaseChange.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/AbelianProperBaseChange.lean#L379). The attribute's comment: “derived proper base change for abelian sheaves: g^{-1} Rf_* ⟶ Rf'_* (g')^{-1} is an isomorphism of functors on D⁺ for f proper and the square cartesian; the underived base change morphism is inverted by isIso_abelianSheafBaseChange_of_properMap, the acyclicity R^p f'_* (g')^{-1} I = 0 for p > 0 is rightAcyclic_pushforward_pullback_of_injective, and properness of f' is isClosedMap_baseChange/isCompact_fiber_baseChange/isSeparatedMap_baseChange”. References: SGA 4 Vbis (4.1.1), “more general”.

> **Proper base change for abelian sheaves on topological spaces, [Stacks, Tag 09V6].** For a
> cartesian square of topological spaces
>
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> Y' --g---> Y
> ```
>
> with `f` proper in the sense of [Stacks, Tag 005O] (5), the canonical base change morphism
>
> `g^{-1} Rf_* ⟶ Rf'_* (g')^{-1}`
>
> of `Stacks.Cohomology.BaseChange.abelianBaseChange` is an isomorphism of functors
> `D⁺(X) ⥤ D⁺(Y')` on bounded below derived categories of abelian sheaves — hence an isomorphism
> at every bounded below complex, naturally in it.
>
> Both inputs of the criterion `Stacks.Cohomology.ProperBaseChange.isIso_baseChangeDerived` are
> proved from properness.
> They are the invertibility of the *underived* base change morphism
> `Stacks.Cohomology.BaseChange.abelianSheafBaseChange`, `g^{-1} f_* ⟶ f'_* (g')^{-1}`, which is
> `isIso_abelianSheafBaseChange_of_properMap` above — asked for by the criterion only at injective
> sheaves, because both derived functors on its right-hand side are computed on a complex of
> injectives, but proved at every abelian sheaf — and the vanishing
> `R^{p>0} f'_*((g')^{-1} I) = 0` at an injective `I`, which is
> `rightAcyclic_pushforward_pullback_of_injective`, together with the transfer of properness from
> `f` to `f'`.

```lean
theorem isIso_abelianBaseChange (hcart : IsPullback g' f' f g)
    (hf : StacksDraft.Topology.IsProperMap.{u, u, u} (f.hom : X → Y)) :
    IsIso (BaseChange.abelianBaseChange f f' g g' hcart.w)
```

## Tag 0D90, a lemma

[Tag 0D90](https://stacks.math.columbia.edu/tag/0D90) in the Stacks Project.

**`Stacks.Topology.ProperBaseChange.isIso_properBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ProperPushforward/ProperBaseChange.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ProperPushforward/ProperBaseChange.lean#L531).

> **Proper base change for sheaves of sets, Stacks 0D90.** Let
>
> ```
> X ×_Y Z --- g' ---> X
>    |                |
>    f'               f
>    v                v
>    Z  --- g ----->  Y
> ```
>
> be a cartesian square of topological spaces with `f` proper in the sense of Stacks 005O (5).
> Then for every sheaf of sets `F` on `X` the canonical base-change map
> `g⁻¹(f_*F) ⟶ f'_*((g')⁻¹F)` is an isomorphism.

```lean
theorem isIso_properBaseChangeMap (f : X ⟶ Y) (g : Z ⟶ Y) (F : X.Sheaf (Type u))
    (hf : StacksDraft.Topology.IsProperMap.{u, u, u} (⇑f)) :
    IsIso (properBaseChangeMap f g F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.18, Tag 09V4](https://stacks.math.columbia.edu/tag/09V4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
