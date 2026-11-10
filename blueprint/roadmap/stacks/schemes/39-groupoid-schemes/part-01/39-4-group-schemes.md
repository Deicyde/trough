---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupSchemeOverPoints, AlgebraicGeometry.GroupSchemeOverPoints.Hom, AlgebraicGeometry.GroupScheme.grpObjPullbackObj, AlgebraicGeometry.GroupScheme.pointsMulEquiv, AlgebraicGeometry.ClosedSubgroupScheme, AlgebraicGeometry.OpenSubgroupScheme, AlgebraicGeometry.isClosedSubgroupScheme_iff_factor, AlgebraicGeometry.isOpenSubgroupScheme_iff_factor
statement: formalized
proof: formalized
---

# 39.4 Group schemes

Section 39.4 of the Stacks Project, [Tag 022R](https://stacks.math.columbia.edu/tag/022R). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 022S, a definition

[Tag 022S](https://stacks.math.columbia.edu/tag/022S) in the Stacks Project.

**`AlgebraicGeometry.GroupSchemeOverPoints`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Defs.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Defs.lean#L63). The attribute's comment: “a group scheme over S”.

> **Stacks Project, Tag 022S** (1). A group scheme over `S`: a scheme `G` over `S` together
> with a multiplication morphism `m : G ×_S G ⟶ G` of schemes over `S`, such that for every
> scheme `T` over `S` the induced multiplication makes the set of `T`-valued points
> `G(T) = Hom_{Over S}(T, G)` into a group.

```lean
structure GroupSchemeOverPoints (S : Scheme.{u})
```

**`AlgebraicGeometry.GroupSchemeOverPoints.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Defs.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Defs.lean#L85). The attribute's comment: “morphisms of group schemes over S”. References: SGA 3 XI (2.1), “The value of M_H”; SGA 7 VII (2.9.6), “partial”.

> **Stacks Project, Tag 022S** (2). A morphism `ψ : (G, m) ⟶ (G', m')` of group schemes over
> `S`: a morphism `ψ : G ⟶ G'` of schemes over `S` such that for every scheme `T` over `S`, the
> induced map `ψ : G(T) ⟶ G'(T)` is a homomorphism of groups.

```lean
structure Hom (G H : GroupSchemeOverPoints S)
```

## Tag 022T, a lemma

[Tag 022T](https://stacks.math.columbia.edu/tag/022T) in the Stacks Project.

**`AlgebraicGeometry.GroupScheme.grpObjPullbackObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/BaseChange.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/BaseChange.lean#L92). References: SGA 3 VIA (0.4), “partial”.

> Let `(G, m)` be a group scheme over `S` and `f : S' ⟶ S` a morphism of schemes. The
> pullback `(G_{S'}, m_{S'})` is a group scheme over `S'`.

```lean
noncomputable instance grpObjPullbackObj : GrpObj ((Over.pullback f).obj G)
```

**`AlgebraicGeometry.GroupScheme.pointsMulEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/BaseChange.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/BaseChange.lean#L123).

> For every scheme `T` over `S'`, the pair `(G_{S'}(T), m_{S'})` is a group, and composition
> with the projection `G ×_S S' ⟶ G` identifies it with the group `(G(T), m)` of morphisms
> `T ⟶ G` over `S`.

```lean
noncomputable def pointsMulEquiv (T : Over S') :
    (T ⟶ (Over.pullback f).obj G) ≃* ((Over.map f).obj T ⟶ G)
```

## Tag 047D, a definition

[Tag 047D](https://stacks.math.columbia.edu/tag/047D) in the Stacks Project.

**`AlgebraicGeometry.ClosedSubgroupScheme`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Defs.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Defs.lean#L56). The attribute's comment: “part (1)”.

> A closed subgroup scheme of `G` over `S`.

```lean
structure ClosedSubgroupScheme {S : Scheme.{u}} (G : Grp (Over S))
```

**`AlgebraicGeometry.OpenSubgroupScheme`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Defs.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Defs.lean#L66). The attribute's comment: “part (2)”.

> An open subgroup scheme of `G` over `S`.

```lean
structure OpenSubgroupScheme {S : Scheme.{u}} (G : Grp (Over S))
```

## Tag 0G8L, a lemma

[Tag 0G8L](https://stacks.math.columbia.edu/tag/0G8L) in the Stacks Project.

**`AlgebraicGeometry.isClosedSubgroupScheme_iff_factor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Defs.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Defs.lean#L171). The attribute's comment: “part (1)”.

> The factorization criterion for a closed subscheme to be a subgroup scheme.

```lean
theorem isClosedSubgroupScheme_iff_factor {S : Scheme.{u}}
    (G : Grp (Over S)) {H : Over S} (j : H ⟶ G.X)
    [AlgebraicGeometry.IsClosedImmersion j.left] :
    (∃ K : ClosedSubgroupScheme G,
      ∃ e : H ≅ K.carrier.X, j = e.hom ≫ K.ι.hom.hom) ↔
      ((∃ e : 𝟙_ (Over S) ⟶ H, e ≫ j = η[G.X]) ∧
       (∃ m : H ⊗ H ⟶ H, m ≫ j = (j ⊗ₘ j) ≫ μ[G.X]) ∧
       (∃ i : H ⟶ H, i ≫ j = j ≫ ι[G.X]))
```

**`AlgebraicGeometry.isOpenSubgroupScheme_iff_factor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Defs.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Defs.lean#L186). The attribute's comment: “part (2)”.

> The factorization criterion for an open subscheme to be a subgroup scheme.

```lean
theorem isOpenSubgroupScheme_iff_factor {S : Scheme.{u}}
    (G : Grp (Over S)) {H : Over S} (j : H ⟶ G.X)
    [AlgebraicGeometry.IsOpenImmersion j.left] :
    (∃ K : OpenSubgroupScheme G,
      ∃ e : H ≅ K.carrier.X, j = e.hom ≫ K.ι.hom.hom) ↔
      ((∃ e : 𝟙_ (Over S) ⟶ H, e ≫ j = η[G.X]) ∧
       (∃ m : H ⊗ H ⟶ H, m ≫ j = (j ⊗ₘ j) ≫ μ[G.X]) ∧
       (∃ i : H ⟶ H, i ≫ j = j ≫ ι[G.X]))
```

## Tag 047E, a definition

[Tag 047E](https://stacks.math.columbia.edu/tag/047E) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Smooth`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Smooth#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch39.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch39.lean#L19) (StacksFrontier): “(1) smooth: `Smooth G.hom` for `G` a group object over `S`”. References: EGA IV (17.3.1); SGA 1 II (1.1); SGA 3 XI (1.1); SGA 3 XI (1.6); SGA 7 XIV (2.1), “partial”.
- [`AlgebraicGeometry.Flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch39.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch39.lean#L21) (StacksFrontier): “(2) flat: `Flat G.hom`”. References: EGA 0 (6.7.1); EGA IV (2.1.1); SGA 3 III (2.0), “partial”; SGA 7 VII (1.3.8), “flatness of p”.
- [`AlgebraicGeometry.IsSeparated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch39.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch39.lean#L22) (StacksFrontier): “(3) separated: `IsSeparated G.hom`”. References: EGA I (5.4.1); EGA I (10.15.1), “Separated morphism X → S”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.4, Tag 022R](https://stacks.math.columbia.edu/tag/022R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
