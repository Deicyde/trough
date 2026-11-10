---
declaration: section
origin: cited
lean: AlgebraicGeometry.isVariety_and_topologicalKrullDim_pullback, AlgebraicGeometry.topologicalKrullDim_component_pullback_bounds, Stacks.Intersection.isRegularImmersion_diagonal, Stacks.Intersection.isFiniteLocallyFreeOfRank_conormalSheaf_diagonal, Stacks.Intersection.codimension_diagonal_eq_topologicalKrullDim, Stacks.Intersection.add_topologicalKrullDim_le_add_topologicalKrullDim_of_irreducibleComponent, AlgebraicGeometry.IntersectProperly, AlgebraicGeometry.AlgebraicCycle.IntersectProperly
statement: formalized
proof: formalized
---

# 43.13 Proper intersections

Section 43.13 of the Stacks Project, [Tag 0AZL](https://stacks.math.columbia.edu/tag/0AZL). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AZM, a lemma

[Tag 0AZM](https://stacks.math.columbia.edu/tag/0AZM) in the Stacks Project.

**`AlgebraicGeometry.isVariety_and_topologicalKrullDim_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean#L117). The attribute's comment: “the whole lemma, both of its conclusions: for `X` and `Y` varieties over an algebraically closed field `k` — the source's own hypothesis, and one the first conclusion needs, since over a field that is not algebraically closed a product of two varieties can be reducible (`AlgebraicGeometry.gaussianRationals_product_not_isVariety` below) — the product `X ×_{Spec k} Y`, with structure morphism the first projection followed by the structure morphism of `X`, is again a variety, AND its dimension is `dim X + dim Y`. A variety is `AlgebraicGeometry.IsVariety`: integral, separated, locally of finite type and quasi-compact over the field, so the first conclusion carries the integrality and separatedness of the product. Dimensions are `topologicalKrullDim`, valued in `WithBot ℕ∞`, and the formula is an equation there. The first conclusion is also Stacks 05P3, `AlgebraicGeometry.isVariety_pullback`; the second holds over an arbitrary field, `AlgebraicGeometry.topologicalKrullDim_pullback_of_isVariety`.”.

> **Stacks Project, Tag 0AZM.** Let `X` and `Y` be varieties over an algebraically closed
> field `k`. Then the product `X ×_{Spec k} Y` is a variety and its dimension is the sum of the
> dimensions of `X` and of `Y`.

```lean
public theorem isVariety_and_topologicalKrullDim_pullback (k : Type u) [Field k] [IsAlgClosed k]
    {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [IsVariety k f] [IsVariety k g] :
    IsVariety k (pullback.fst f g ≫ f) ∧
      topologicalKrullDim ↑(pullback f g) = topologicalKrullDim X + topologicalKrullDim Y
```

## Tag 0AZN, a lemma

[Tag 0AZN](https://stacks.math.columbia.edu/tag/0AZN) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDim_component_pullback_bounds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/PreimageDimension.lean, line 853](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/PreimageDimension.lean#L853). The attribute's comment: “both bounds in one statement, for a morphism `f : X ⟶ Y` of varieties over a field, a closed subvariety `Z ⊆ Y` presented by an ideal sheaf, and `W` an irreducible component of the scheme-theoretic inverse image `f⁻¹(Z) = X ×_Y Z`. (1) when `f` is a regular immersion whose conormal sheaf is finite locally free of rank `c` — the source's codimension — `dim Z ≤ dim W + c`; (2) when `f` is a local complete intersection morphism of relative dimension `r`, in the sense of `AlgebraicGeometry.IsLocalCompleteIntersectionOfRelativeDimension`, `d + r ≤ m` for `d = dim Z` and `m = dim W`. The regular-immersion data of (1) and the local complete intersection data of (2) are the source's own, and each binds inside its own clause, as in the source. Dimensions are `topologicalKrullDim`, valued in `WithBot ℕ∞`, which has no subtraction, so the source's `dim W ≥ d - c` is spelled as the relation `dim Z ≤ dim W + c`; in (2) the relative dimension is an integer and may be negative, so the two dimensions are produced as the natural numbers they are — both are transcendence degrees of residue fields over the base field — and `d + r ≤ m` is an inequality in `ℤ`. The two bounds are `AlgebraicGeometry.topologicalKrullDim_le_component_pullback_add_of_isRegularImmersion` and `AlgebraicGeometry.exists_add_relativeDimension_le_topologicalKrullDim_component_pullback`.”.

> **Stacks Project, Tag 0AZN.** Let `f : X ⟶ Y` be a morphism of varieties over a field, let
> `Z ⊆ Y` be a closed subvariety, presented by the ideal sheaf `I`, and let `W` be an irreducible
> component of the scheme-theoretic inverse image `f⁻¹(Z) = X ×_Y Z`. Then:
>
> 1. if `f` is a regular immersion of codimension `c`, then `dim Z ≤ dim W + c`, that is, `W` has
>    dimension at least `dim Z - c`;
> 2. if `f` is a local complete intersection morphism of relative dimension `r`, and `Z` has
>    dimension `d`, then `W` has dimension `m` with `d + r ≤ m`.
>
> Dimensions are `topologicalKrullDim`, valued in `WithBot ℕ∞`, which has no subtraction: the
> source's `dim W ≥ d - c` in part (1) is accordingly a relation between the two dimensions,
> `dim Z ≤ dim W + c`. In part (2) the relative dimension `r` is an integer, negative for a
> regular immersion, so there the two dimensions are produced as the natural numbers they are and
> `d + r ≤ m` is an inequality in `ℤ`.

```lean
theorem topologicalKrullDim_component_pullback_bounds
    (k : Type u) [Field k] {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of k)) (sY : Y ⟶ Spec (.of k))
    [IsVariety k sX] [IsVariety k sY] (f : X ⟶ Y) (hf : f ≫ sY = sX)
    (I : Y.IdealSheafData) [IsIntegral I.subscheme]
    (W : Set (pullback f I.subschemeι : Scheme.{u}))
    (hW : W ∈ irreducibleComponents (pullback f I.subschemeι : Scheme.{u})) :
    (∀ [IsImmersion f], Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion f →
        ∀ (c : ℕ) [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
          (Stacks.Conormal.conormalSheaf f) c],
          topologicalKrullDim I.subscheme ≤ topologicalKrullDim W + (c : WithBot ℕ∞)) ∧
      (∀ r : ℤ, IsLocalCompleteIntersectionOfRelativeDimension f r →
        ∃ d m : ℕ, topologicalKrullDim I.subscheme = (d : WithBot ℕ∞) ∧
          topologicalKrullDim W = (m : WithBot ℕ∞) ∧ (d : ℤ) + r ≤ (m : ℤ))
```

## Tag 0B0Q, a lemma

[Tag 0B0Q](https://stacks.math.columbia.edu/tag/0B0Q) in the Stacks Project.

**`Stacks.Intersection.isRegularImmersion_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/DiagonalRegularImmersion.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/DiagonalRegularImmersion.lean#L78). The attribute's comment: “the diagonal is a regular immersion”. References: SGA 1 II (4.18), “variety over perfect fld”.

> The diagonal `X ⟶ X ×ₖ X` of a nonsingular variety over a perfect field is a regular
> immersion.

```lean
theorem isRegularImmersion_diagonal [IsVariety k f] (hX : IsRegular X) :
    Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion (pullback.diagonal f)
```

**`Stacks.Intersection.isFiniteLocallyFreeOfRank_conormalSheaf_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/DiagonalRegularImmersion.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/DiagonalRegularImmersion.lean#L114). The attribute's comment: “the codimension of the diagonal is the dimension of the variety”.

> The conormal sheaf of the diagonal of a nonsingular variety over a perfect field is finite
> locally free of rank the dimension of the variety: the diagonal is a regular immersion of
> codimension `dim X`.

```lean
theorem isFiniteLocallyFreeOfRank_conormalSheaf_diagonal [IsVariety k f] (hX : IsRegular X)
    (n : ℕ) (hdim : topologicalKrullDim X = (n : WithBot ℕ∞)) :
    SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      (Stacks.Conormal.conormalSheaf (pullback.diagonal f)) n
```

**`Stacks.Intersection.codimension_diagonal_eq_topologicalKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/DiagonalRegularImmersion.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/DiagonalRegularImmersion.lean#L233). The attribute's comment: “the codimension of the image of the diagonal is the dimension of the variety”.

> The image of the diagonal of a variety has codimension the dimension of the variety inside
> the product `X ×ₖ X`: the codimension of the closure of the image of the generic point is
> `dim X`.

```lean
theorem codimension_diagonal_eq_topologicalKrullDim [IsVariety k f] :
    (codimension (IrreducibleCloseds.closureSingleton
      (pullback.diagonal f (genericPoint X))) : WithBot ℕ∞) = topologicalKrullDim X
```

## Tag 0AZP, a lemma

[Tag 0AZP](https://stacks.math.columbia.edu/tag/0AZP) in the Stacks Project.

**`Stacks.Intersection.add_topologicalKrullDim_le_add_topologicalKrullDim_of_irreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/IntersectionDimension.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/IntersectionDimension.lean#L207).

> **Stacks Project, Tag 0AZP.** Let `X` be a nonsingular variety over an algebraically closed
> field and let `V, W ⊆ X` be closed subvarieties of dimensions `r` and `s`. Then every irreducible
> component `Z` of `V ∩ W` satisfies `r + s ≤ dim X + dim Z`, that is, has dimension at least
> `r + s - dim X`.

```lean
theorem add_topologicalKrullDim_le_add_topologicalKrullDim_of_irreducibleComponent
    [IsAlgClosed k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsVariety k f] (hX : IsRegular X)
    (I J : X.IdealSheafData) [IsIntegral I.subscheme] [IsIntegral J.subscheme]
    (Z : Set ↥((I.support : Set X) ∩ (J.support : Set X)))
    (hZ : Z ∈ irreducibleComponents ↥((I.support : Set X) ∩ (J.support : Set X))) :
    topologicalKrullDim I.subscheme + topologicalKrullDim J.subscheme ≤
      topologicalKrullDim X + topologicalKrullDim Z
```

## Tag 0AZQ, a definition

[Tag 0AZQ](https://stacks.math.columbia.edu/tag/0AZQ) in the Stacks Project.

**`AlgebraicGeometry.IntersectProperly`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/Defs.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/Defs.lean#L54). The attribute's comment: “closed subvarieties”.

> Two irreducible closed subsets of a scheme **intersect properly** when their intersection
> has at most the expected dimension, namely `dim (W ∩ V) ≤ dim W + dim V - dim X`.

```lean
public def IntersectProperly (W V : IrreducibleCloseds X) : Prop
```

**`AlgebraicGeometry.AlgebraicCycle.IntersectProperly`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/Defs.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/Defs.lean#L80). The attribute's comment: “cycles”.

> Two algebraic cycles **intersect properly** when every pair of components occurring in them
> with a nonzero coefficient intersects properly.

```lean
public def IntersectProperly {R : Type*} [Zero R] (α β : AlgebraicCycle X R) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.13, Tag 0AZL](https://stacks.math.columbia.edu/tag/0AZL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
