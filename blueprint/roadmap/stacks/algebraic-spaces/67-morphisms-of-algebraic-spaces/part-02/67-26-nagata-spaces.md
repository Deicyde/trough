---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType, AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_nagataScheme, AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_field, AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_completeLocalRing, AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_int, AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_dedekindDomain
statement: formalized
proof: formalized
---

# 67.26 Nagata spaces

Section 67.26 of the Stacks Project, [Tag 0BAT](https://stacks.math.columbia.edu/tag/0BAT). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BAU, a lemma

[Tag 0BAU](https://stacks.math.columbia.edu/tag/0BAU) in the Stacks Project.

**`AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L306).

> **Stacks 0BAU.** A morphism of algebraic spaces over `S` which is locally of finite type
> and whose target is Nagata has Nagata source.
>
> A surjective étale chart `q : h_V ⟶ Y` witnessing that the target is Nagata lifts, by
> Stacks 02X1, to a surjective étale chart `p : h_U ⟶ X` of the source and a morphism
> `α : U ⟶ V` of the site making the square commute. Local finite type of the morphism tests
> exactly such squares, so the scheme morphism underlying `α` is locally of finite type with
> Nagata target, whence `U` is Nagata by Stacks 035A and `p` is the required chart.

```lean
theorem isNagata_of_isLocallyOfFiniteType
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (hN : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsNagataScheme T)) :
    HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsNagataScheme T)
```

## Tag 0BAV, a lemma

[Tag 0BAV](https://stacks.math.columbia.edu/tag/0BAV) in the Stacks Project.

**`AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_nagataScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L333). The attribute's comment: “part (1): over a Nagata scheme”.

> **Stacks 0BAV, part (1).** An algebraic space over `S` locally of finite type over a
> Nagata scheme is Nagata.

```lean
theorem isNagata_of_isLocallyOfFiniteType_over_nagataScheme (hX : IsAlgebraicSpace B S hS X)
    (T : BigFppfOver B S hS) (hT : IsNagataScheme ((BigFppfOver.toScheme B S hS).obj T))
    (f : X ⟶ yoneda.obj T) (hf : IsLocallyOfFiniteType B S hS f) :
    HasEtaleLocalProperty B S hS X (fun Z : Scheme.{u} => IsNagataScheme Z)
```

**`AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L345). The attribute's comment: “part (2): over a field”.

> **Stacks 0BAV, part (2).** An algebraic space over `S` locally of finite type over a field
> is Nagata.

```lean
theorem isNagata_of_isLocallyOfFiniteType_over_field (hX : IsAlgebraicSpace B S hS X)
    (k : Type u) [Field k] (T : BigFppfOver B S hS)
    (e : (BigFppfOver.toScheme B S hS).obj T ≅ Spec (.of k))
    (f : X ⟶ yoneda.obj T) (hf : IsLocallyOfFiniteType B S hS f) :
    HasEtaleLocalProperty B S hS X (fun Z : Scheme.{u} => IsNagataScheme Z)
```

**`AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_completeLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L358). The attribute's comment: “part (3): over a Noetherian complete local ring”.

> **Stacks 0BAV, part (3).** An algebraic space over `S` locally of finite type over a
> Noetherian complete local ring is Nagata. Completeness is
> `IsPrecomplete (IsLocalRing.maximalIdeal R) R`, as in Stacks 032W.

```lean
theorem isNagata_of_isLocallyOfFiniteType_over_completeLocalRing (hX : IsAlgebraicSpace B S hS X)
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsPrecomplete (IsLocalRing.maximalIdeal R) R] (T : BigFppfOver B S hS)
    (e : (BigFppfOver.toScheme B S hS).obj T ≅ Spec (.of R))
    (f : X ⟶ yoneda.obj T) (hf : IsLocallyOfFiniteType B S hS f) :
    HasEtaleLocalProperty B S hS X (fun Z : Scheme.{u} => IsNagataScheme Z)
```

**`AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L372). The attribute's comment: “part (4): over the integers”.

> **Stacks 0BAV, part (4).** An algebraic space over `S` locally of finite type over the
> integers is Nagata. "Over the integers" is read as "over the terminal scheme of the ambient
> universe", which is the spectrum of `ULift ℤ`.

```lean
theorem isNagata_of_isLocallyOfFiniteType_over_int (hX : IsAlgebraicSpace B S hS X)
    (T : BigFppfOver B S hS) (hT : IsTerminal ((BigFppfOver.toScheme B S hS).obj T))
    (f : X ⟶ yoneda.obj T) (hf : IsLocallyOfFiniteType B S hS f) :
    HasEtaleLocalProperty B S hS X (fun Z : Scheme.{u} => IsNagataScheme Z)
```

**`AlgebraicGeometry.Space.isNagata_of_isLocallyOfFiniteType_over_dedekindDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L385). The attribute's comment: “part (5): over a Dedekind domain of characteristic zero”.

> **Stacks 0BAV, part (5).** An algebraic space over `S` locally of finite type over a
> Dedekind domain of characteristic zero is Nagata.

```lean
theorem isNagata_of_isLocallyOfFiniteType_over_dedekindDomain (hX : IsAlgebraicSpace B S hS X)
    (R : Type u) [CommRing R] [IsDedekindDomain R] [CharZero R] (T : BigFppfOver B S hS)
    (e : (BigFppfOver.toScheme B S hS).obj T ≅ Spec (.of R))
    (f : X ⟶ yoneda.obj T) (hf : IsLocallyOfFiniteType B S hS f) :
    HasEtaleLocalProperty B S hS X (fun Z : Scheme.{u} => IsNagataScheme Z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.26, Tag 0BAT](https://stacks.math.columbia.edu/tag/0BAT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
