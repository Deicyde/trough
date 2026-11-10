---
declaration: section
origin: cited
lean: Stacks.IdealSheaf.isNthOrderThickening_inclusion, AlgebraicGeometry.Space.nthOrderInfinitesimalNeighbourhood, AlgebraicGeometry.Space.firstOrderInfinitesimalNeighbourhood, AlgebraicGeometry.Space.immersionClosedLift_comp_ι, AlgebraicGeometry.Space.nthOrderInfinitesimalNeighbourhoodOfImmersion, AlgebraicGeometry.Space.firstOrderInfinitesimalNeighbourhoodOfImmersion, AlgebraicGeometry.Space.le_nthOrderInfinitesimalNeighbourhoodOfImmersion, AlgebraicGeometry.Space.isNthOrderThickening_nthOrderInfinitesimalNeighbourhoodOfImmersion
statement: formalized
proof: formalized
---

# 76.12 Infinitesimal neighbourhoods

Section 76.12 of the Stacks Project, [Tag 05ZU](https://stacks.math.columbia.edu/tag/05ZU). 3 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05ZV, a definition

[Tag 05ZV](https://stacks.math.columbia.edu/tag/05ZV) in the Stacks Project.

**`Stacks.IdealSheaf.isNthOrderThickening_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhood.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhood.lean#L113). The attribute's comment: “the order asserted by the definition, read on an étale chart”.

> The subscheme of a sheaf of ideals is an `n`th order thickening inside the subscheme of its
> `(n + 1)`st power.

```lean
theorem isNthOrderThickening_inclusion (I : X.IdealSheafData) (n : ℕ) :
    _root_.Stacks.Thickenings.IsNthOrderThickening n
      (Scheme.IdealSheafData.inclusion (pow_succ_le_self I n))
```

**`AlgebraicGeometry.Space.nthOrderInfinitesimalNeighbourhood`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhood.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhood.lean#L172). The attribute's comment: “part (2); the ideal of `Z` is given on an étale chart, 03MB being unavailable”.

> The `n`th order infinitesimal neighbourhood of the closed subspace cut out by a sheaf of
> ideals `J` on a chart `φ : U ⟶ X`: the subspace of `X` cut out on that chart by `J ^ (n + 1)`.

```lean
def nthOrderInfinitesimalNeighbourhood (φ : yoneda.obj U ⟶ X.1)
    (J : ((BigFppfOver.toScheme B S hS).obj U).IdealSheafData) (n : ℕ) : Subfunctor X.1
```

**`AlgebraicGeometry.Space.firstOrderInfinitesimalNeighbourhood`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhood.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhood.lean#L179). The attribute's comment: “part (1); the ideal of `Z` is given on an étale chart, 03MB being unavailable”.

> The first order infinitesimal neighbourhood of the closed subspace cut out by a sheaf of
> ideals on a chart: the subspace cut out there by the square of that sheaf of ideals.

```lean
abbrev firstOrderInfinitesimalNeighbourhood (φ : yoneda.obj U ⟶ X.1)
    (J : ((BigFppfOver.toScheme B S hS).obj U).IdealSheafData) : Subfunctor X.1
```

**`AlgebraicGeometry.Space.immersionClosedLift_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean#L583). The attribute's comment: “over `X`: the immersion is the closed immersion of `Z` into the open `U ⊆ X` followed by the inclusion of `U`, which is what puts `Z ⊆ Z_n` over `X`”.

> The factorisation of an immersion through the complement of the boundary of its image
> recovers the immersion. This is what puts the pair `Z ⊆ Z_n ⊆ U` of Stacks 05ZV *over `X`*: the
> open subspace `U` sits in `X`, and `i` is the composite of the closed immersion of `Z` into `U`
> with that inclusion.

```lean
theorem immersionClosedLift_comp_ι (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (i : Y ⟶ X) (hi : IsImmersion B S hS i) :
    immersionClosedLift B S hS hX hY i hi ≫
        (boundaryComplement B S hS X (Set.range (pointsMap B S hS Y i))).ι = i
```

**`AlgebraicGeometry.Space.nthOrderInfinitesimalNeighbourhoodOfImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean#L605). The attribute's comment: “the construction of `Z_n`: the closed subspace of the open `U = X ∖ ∂Z` cut out by `𝓘 ^ (n + 1)`”. References: EGA II (8.10.1), “more general”.

> **Stacks 05ZV.** The *`n`th order infinitesimal neighbourhood* `Z_n` of an immersion
> `i : Z ⟶ X` of algebraic spaces over `S`: the closed subspace of the open subspace `U ⊆ X` in
> which `Z` is closed which is cut out by the `(n + 1)`st power of the quasi-coherent sheaf of
> ideals of `Z` in `U`.

```lean
def nthOrderInfinitesimalNeighbourhoodOfImmersion (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (i : Y ⟶ X) (hi : IsImmersion B S hS i) (n : ℕ) :
    ClosedSubspaces B S hS (immersionAmbientOpen B S hS hX i hi).1
```

**`AlgebraicGeometry.Space.firstOrderInfinitesimalNeighbourhoodOfImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean#L614). The attribute's comment: “part (1): the first order infinitesimal neighbourhood”.

> **Stacks 05ZV, part (1).** The *first order infinitesimal neighbourhood* of an immersion:
> the closed subspace cut out by the square of the sheaf of ideals of its source.

```lean
abbrev firstOrderInfinitesimalNeighbourhoodOfImmersion (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (i : Y ⟶ X) (hi : IsImmersion B S hS i) :
    ClosedSubspaces B S hS (immersionAmbientOpen B S hS hX i hi).1
```

**`AlgebraicGeometry.Space.le_nthOrderInfinitesimalNeighbourhoodOfImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean#L636). The attribute's comment: “the inclusion `Z ⊆ Z_n` inside the ambient open `U`”.

> **The source of an immersion is contained in each of its infinitesimal
> neighbourhoods.** This is the inclusion `Z ⊆ Z_n` of Stacks 05ZV.

```lean
theorem le_nthOrderInfinitesimalNeighbourhoodOfImmersion (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (i : Y ⟶ X) (hi : IsImmersion B S hS i) (n : ℕ) :
    (immersionSourceSubspace B S hS hX hY i hi).1 ≤
      (nthOrderInfinitesimalNeighbourhoodOfImmersion B S hS hX hY i hi n).1
```

**`AlgebraicGeometry.Space.isNthOrderThickening_nthOrderInfinitesimalNeighbourhoodOfImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean, line 653](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/InfinitesimalNeighbourhoodImmersion.lean#L653). The attribute's comment: “the order: `Z ⊆ Z_n` is an nth order thickening, as the definition asserts”.

> **Stacks 05ZV, the order.** The source of an immersion sits inside its `n`th order
> infinitesimal neighbourhood as an `n`th order thickening: on the small étale site of `Z_n` the
> `(n + 1)`st power of the defining ideal of `Z` vanishes. Together with
> `AlgebraicGeometry.Space.le_nthOrderInfinitesimalNeighbourhoodOfImmersion` and
> `AlgebraicGeometry.Space.immersionClosedLift_comp_ι` this is the assertion of the definition
> that `Z ⊆ Z_n` is the *`n`th order* thickening of `Z` over `X`.
>
> The subspace of `Z_n` is the image of `Z` under the inclusion `Z ⟶ Z_n` of
> `AlgebraicGeometry.Space.le_nthOrderInfinitesimalNeighbourhoodOfImmersion`, that is, `Z` itself
> read inside `Z_n`.

```lean
theorem isNthOrderThickening_nthOrderInfinitesimalNeighbourhoodOfImmersion
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (i : Y ⟶ X)
    (hi : IsImmersion B S hS i) (n : ℕ) :
    IsNthOrderThickening B S hS n
        (closedSubspaceSpace B S hS (immersionAmbientOpen B S hS hX i hi)
          (nthOrderInfinitesimalNeighbourhoodOfImmersion B S hS hX hY i hi n))
      (Subfunctor.range (Subfunctor.homOfLe
        (le_nthOrderInfinitesimalNeighbourhoodOfImmersion B S hS hX hY i hi n)))
```

## Tag 05ZW, a lemma

[Tag 05ZW](https://stacks.math.columbia.edu/tag/05ZW) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_lift_of_isNthOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Infinitesimal.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Infinitesimal.lean#L240). The attribute's comment: “part (2): nth-order universal property”.

> **Stacks 05ZW, part (2).** The universal property of the `n`th-order infinitesimal
> neighbourhood of an immersion. Let `Z` be a closed subspace of an open subspace `U` of `X` and
> let `N` be the closed subspace of `U` cut out by the `(n+1)`st power of the ideal sheaf of `Z`.
> Then every `n`th-order thickening `G ⊆ T'` over `X` compatible with `Z` admits a unique
> morphism to `N` over `X` extending the given map of its closed part.

```lean
theorem existsUnique_lift_of_isNthOrderThickening {n : ℕ} {X T' : AlgebraicSpaces B S hS}
    {U : Subfunctor X.1} (hU : IsOpenSubspace B S hS U)
    (Z N : ClosedSubspaces B S hS U.toFunctor)
    (hN : ∀ V : SmallEtale B S hS U.toFunctor,
      ((BigFppfOver.toScheme B S hS).map (N.2.2.rep.snd V.1.hom)).ker =
        ((BigFppfOver.toScheme B S hS).map (Z.2.2.rep.snd V.1.hom)).ker ^ (n + 1))
    {G : Subfunctor T'.1} (hG : IsNthOrderThickening B S hS n T' G)
    (a : G.toFunctor ⟶ Z.1.toFunctor) (b : T'.1 ⟶ X.1)
    (hab : G.ι ≫ b = a ≫ Z.1.ι ≫ U.ι) :
    ∃! a' : T'.1 ⟶ N.1.toFunctor,
      G.ι ≫ a' ≫ N.1.ι = a ≫ Z.1.ι ∧ a' ≫ N.1.ι ≫ U.ι = b
```

**`AlgebraicGeometry.Space.existsUnique_lift_of_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Infinitesimal.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Infinitesimal.lean#L283). The attribute's comment: “part (1): first-order universal property”.

> **Stacks 05ZW, part (1).** The universal property of the first-order infinitesimal
> neighbourhood of an immersion: the case `n = 1` of
> `AlgebraicGeometry.Space.existsUnique_lift_of_isNthOrderThickening`.

```lean
theorem existsUnique_lift_of_isFirstOrderThickening {X T' : AlgebraicSpaces B S hS}
    {U : Subfunctor X.1} (hU : IsOpenSubspace B S hS U)
    (Z N : ClosedSubspaces B S hS U.toFunctor)
    (hN : ∀ V : SmallEtale B S hS U.toFunctor,
      ((BigFppfOver.toScheme B S hS).map (N.2.2.rep.snd V.1.hom)).ker =
        ((BigFppfOver.toScheme B S hS).map (Z.2.2.rep.snd V.1.hom)).ker ^ 2)
    {G : Subfunctor T'.1} (hG : IsFirstOrderThickening B S hS T' G)
    (a : G.toFunctor ⟶ Z.1.toFunctor) (b : T'.1 ⟶ X.1)
    (hab : G.ι ≫ b = a ≫ Z.1.ι ≫ U.ι) :
    ∃! a' : T'.1 ⟶ N.1.toFunctor,
      G.ι ≫ a' ≫ N.1.ι = a ≫ Z.1.ι ∧ a' ≫ N.1.ι ≫ U.ι = b
```

## Tag 05ZX, a lemma

[Tag 05ZX](https://stacks.math.columbia.edu/tag/05ZX) in the Stacks Project.

**`AlgebraicGeometry.Space.epi_conormalMap_firstOrderNeighbourhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFirstOrderNeighbourhood.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFirstOrderNeighbourhood.lean#L89). The attribute's comment: “surjectivity of the comparison map of conormal modules”.

> Let `Z` be a closed subspace of an algebraic space `X` and let `Z'` be the first order
> infinitesimal neighbourhood of `Z` in `X`. The map of conormal modules `𝒞_{Z/X} ⟶ 𝒞_{Z/Z'}`
> induced by the fibre product square formed by `Z ⊆ Z'` and the inclusion `Z' ⟶ X` is an
> epimorphism.

```lean
theorem epi_conormalMap_firstOrderNeighbourhood (X : AlgebraicSpaces B S hS)
    (Z Z' : ClosedSubspaces B S hS X.1) (h : IsFirstOrderNeighbourhood B S hS X Z Z') :
    Epi (conormalMap B S hS
      (preimageSubspace B S hS (subspaceInclusion B S hS X Z') Z) Z
      (subspaceInclusion B S hS X Z')
      (preimageProjection B S hS (subspaceInclusion B S hS X Z') Z)
      (conormalEtaleRestrictionSquare B S hS (subspaceInclusion B S hS X Z') Z))
```

**`AlgebraicGeometry.Space.isIso_immersionLiftConormalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFirstOrderNeighbourhoodImmersion.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFirstOrderNeighbourhoodImmersion.lean#L387). The attribute's comment: “the map of conormal modules of 04CP from an immersion to its first order infinitesimal neighbourhood is an isomorphism”.

> **[Stacks Project, Tag 05ZX].**  Let `i : Z ⟶ X` be an immersion of algebraic spaces and let
> `Z ⊆ Z'` be the first order infinitesimal neighbourhood of `Z` in `X`: the closed subspace of
> the complement `X ∖ ∂Z` of the boundary of the image, through which `i` factors as a closed
> immersion, cut out by the square of the defining ideal sheaf of `Z` there.  Then the map
> `𝒞_{Z/X} ⟶ 𝒞_{Z/Z'}` of [Stacks Project, Tag 04CP] induced by the square with `𝟙 Z` on the left
> and `Z' ⟶ X` on the right, `AlgebraicGeometry.Space.immersionLiftConormalMap`, is an isomorphism
> of `𝒪_Z`-modules.
>
> The two conormal modules are `AlgebraicGeometry.Space.conormalModuleOfImmersion` of
> [Stacks Project, Tag 04CN], for `i` and for the immersion `Z ⟶ Z'`.  The containment of the
> image of `Z` in `Z'`, which the map is built from, is derived from the neighbourhood hypothesis
> by `AlgebraicGeometry.Space.le_of_isFirstOrderNeighbourhood`.

```lean
theorem isIso_immersionLiftConormalMap
    (h : IsFirstOrderNeighbourhood B S hS (immersionAmbient B S hS hX hZ i hi)
      (immersionRangeSubspace B S hS hX hZ i hi) Z') :
    IsIso (immersionLiftConormalMap B S hS hX hZ i hi Z'
      (le_of_isFirstOrderNeighbourhood B S hS _ _ Z' h))
```

**`AlgebraicGeometry.Space.isIso_conormalMap_of_ker_eq_ker_sq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFirstOrderNeighbourhoodIso.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFirstOrderNeighbourhoodIso.lean#L353). The attribute's comment: “the isomorphism, for a closed subspace”.

> Let `Z` be a closed subspace of an algebraic space `X` and let `N ⊆ X` be its first order
> infinitesimal neighbourhood, the closed subspace whose ideal sheaf is on every étale chart of `X`
> the square of that of `Z`.  The map `𝒞_{Z/X} ⟶ 𝒞_{Z_N/N}` of conormal modules of
> [Stacks Project, Tag 04CP] attached to the fibre product square of `Z_N = Z ×_X N ⊆ N` over
> `Z ⊆ X` is an isomorphism.

```lean
theorem isIso_conormalMap_of_ker_eq_ker_sq :
    IsIso (conormalMap B S hS (preimageSubspace B S hS (subspaceInclusion B S hS X N) Z) Z
      (subspaceInclusion B S hS X N)
      (preimageProjection B S hS (subspaceInclusion B S hS X N) Z)
      (conormalEtaleRestrictionSquare B S hS (subspaceInclusion B S hS X N) Z))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.12, Tag 05ZU](https://stacks.math.columbia.edu/tag/05ZU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
