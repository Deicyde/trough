---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsIrreducibleComponent, AlgebraicGeometry.Space.IsGenericPointOf, AlgebraicGeometry.Space.bijective_closure_genericPoint_irreducibleComponents, AlgebraicGeometry.Space.bijective_range_irreducibleComponent, AlgebraicGeometry.Space.existsUnique_isGenericPointOf_of_isIrreducibleComponent, AlgebraicGeometry.Space.existsUnique_isIrreducibleComponent_isGenericPointOf, AlgebraicGeometry.Space.closedSubspaceCycle, AlgebraicGeometry.Space.closedSubspaceMultiplicity
statement: formalized
proof: formalized
---

# 82.5 Cycle associated to a closed subspace

Section 82.5 of the Stacks Project, [Tag 0EE7](https://stacks.math.columbia.edu/tag/0EE7). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EE8, a remark

[Tag 0EE8](https://stacks.math.columbia.edu/tag/0EE8) in the Stacks Project.

**`AlgebraicGeometry.Space.IsIrreducibleComponent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CycleOfClosedSubspace.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CycleOfClosedSubspace.lean#L67). The attribute's comment: “the terminology: an irreducible component of Y”.

> **Stacks 0EE8.** An *irreducible component* of an algebraic space `Y` over `S` is a closed
> subspace which is an integral algebraic space and whose set of points is an irreducible
> component of `|Y|`.

```lean
abbrev IsIrreducibleComponent (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (_hY : IsAlgebraicSpace B S hS Y)
    (Z : Subfunctor Y) : Prop
```

**`AlgebraicGeometry.Space.IsGenericPointOf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CycleOfClosedSubspace.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CycleOfClosedSubspace.lean#L76). The attribute's comment: “the terminology: the generic point of an irreducible component”.

> **Stacks 0EE8.** A point of an algebraic space `Y` over `S` is the *generic point* of a
> subspace `Z` when it is the generic point of the set of points of `Z`.

```lean
abbrev IsGenericPointOf (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (_hY : IsAlgebraicSpace B S hS Y)
    (Z : Subfunctor Y) (ξ : points B S hS Y) : Prop
```

**`AlgebraicGeometry.Space.bijective_closure_genericPoint_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/IrreducibleComponentCorrespondence.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/IrreducibleComponentCorrespondence.lean#L73). The attribute's comment: “(1) and (2) correspond, by the closure of a point”.

> **Stacks 0EE8, (2) to (1).** For a closed subspace `Y` of a good algebraic space, taking the
> closure of a point is a bijection from the generic points of irreducible components of `|Y|`
> onto the irreducible components of `|Y|`.

```lean
theorem bijective_closure_genericPoint_irreducibleComponents (hf : D.IsGood f)
    (hY : IsClosedSubspace D.site D.base D.base_mem Y) :
    Function.Bijective
      (fun ξ : {ξ : points D.site D.base D.base_mem Y.toFunctor //
          closure {ξ} ∈ irreducibleComponents (points D.site D.base D.base_mem Y.toFunctor)} =>
        (⟨closure {ξ.1}, ξ.2⟩ :
          irreducibleComponents (points D.site D.base D.base_mem Y.toFunctor)))
```

**`AlgebraicGeometry.Space.bijective_range_irreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/IrreducibleComponentCorrespondence.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/IrreducibleComponentCorrespondence.lean#L134). The attribute's comment: “(3) and (1) correspond, by the set of points”.

> **Stacks 0EE8, (3) to (1).** For a closed subspace `Y` of a good algebraic space, taking the
> set of points is a bijection from the irreducible components of `Y` (integral closed subspaces
> `Z ⊂ Y` with `|Z|` an irreducible component of `|Y|`) onto the irreducible components of
> `|Y|`.

```lean
theorem bijective_range_irreducibleComponent (hf : D.IsGood f)
    (hY : IsClosedSubspace D.site D.base D.base_mem Y) :
    Function.Bijective
      (fun Z : {Z : Subfunctor Y.toFunctor //
          IsIrreducibleComponent D.site D.base D.base_mem hY.1 Z} =>
        (⟨Set.range (pointsMap D.site D.base D.base_mem Z.1.toFunctor Z.1.ι), Z.2.2.2⟩ :
          irreducibleComponents (points D.site D.base D.base_mem Y.toFunctor)))
```

**`AlgebraicGeometry.Space.existsUnique_isGenericPointOf_of_isIrreducibleComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/IrreducibleComponentCorrespondence.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/IrreducibleComponentCorrespondence.lean#L150). The attribute's comment: “(3) and (2) correspond: an irreducible component has a unique generic point”.

> **Stacks 0EE8, (3) to (2).** An irreducible component of a closed subspace `Y` of a good
> algebraic space has exactly one generic point.

```lean
theorem existsUnique_isGenericPointOf_of_isIrreducibleComponent (hf : D.IsGood f)
    (hY : IsClosedSubspace D.site D.base D.base_mem Y) {Z : Subfunctor Y.toFunctor}
    (hZ : IsIrreducibleComponent D.site D.base D.base_mem hY.1 Z) :
    ∃! ξ : points D.site D.base D.base_mem Y.toFunctor,
      IsGenericPointOf D.site D.base D.base_mem hY.1 Z ξ
```

**`AlgebraicGeometry.Space.existsUnique_isIrreducibleComponent_isGenericPointOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/IrreducibleComponentCorrespondence.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/IrreducibleComponentCorrespondence.lean#L168). The attribute's comment: “(2) and (3) correspond: a generic point belongs to a unique irreducible component”.

> **Stacks 0EE8, (2) to (3).** A generic point of an irreducible component of `|Y|`, for `Y` a
> closed subspace of a good algebraic space, is the generic point of exactly one irreducible
> component of `Y`.

```lean
theorem existsUnique_isIrreducibleComponent_isGenericPointOf (hf : D.IsGood f)
    (hY : IsClosedSubspace D.site D.base D.base_mem Y)
    {ξ : points D.site D.base D.base_mem Y.toFunctor}
    (hξ : closure {ξ} ∈ irreducibleComponents (points D.site D.base D.base_mem Y.toFunctor)) :
    ∃! Z : Subfunctor Y.toFunctor, IsIrreducibleComponent D.site D.base D.base_mem hY.1 Z ∧
      IsGenericPointOf D.site D.base D.base_mem hY.1 Z ξ
```

## Tag 0EE9, a definition

[Tag 0EE9](https://stacks.math.columbia.edu/tag/0EE9) in the Stacks Project.

**`AlgebraicGeometry.Space.closedSubspaceCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClosedSubspaceCycle.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClosedSubspaceCycle.lean#L183). The attribute's comment: “part (2): the k-cycle [Y]\_k of a closed subspace; the multiplicity at each point is independent of the choice of geometric representative by Lemma 0EE1 (closedSubspaceMultiplicity\_eq\_toNat\_geometricLength) and positive by Lemma 0EE4 (closedSubspaceMultiplicity\_pos)”.

> In Situation 0EDT let `X/B` be good, let `Y ⊆ X` be a closed subspace and assume
> `dim_δ(Y) ≤ k`. The *`k`-cycle associated to `Y`* is `[Y]_k = ∑ m_{Z, Y} [Z]`, the sum over the
> irreducible components `Z` of `Y` of δ-dimension `k`, with `m_{Z, Y}` the multiplicity of `Z` in
> `Y`; as an element of `Z_k(X)` it is the coefficient family
> `AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace` at the canonical geometric points.

```lean
def closedSubspaceCycle (sX : X ⟶ D.space) (hX : D.IsGood sX) (Y : Subfunctor X)
    (hY : IsClosedSubspace D.site D.base D.base_mem Y) (k : ℤ)
    (hdim : deltaDimensionSubspace D sX hX Y hY ≤ (k : EInt)) : CycleGroup D sX k
```

**`AlgebraicGeometry.Space.closedSubspaceMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClosedSubspaceCycleComponents.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClosedSubspaceCycleComponents.lean#L151). The attribute's comment: “part (1): the multiplicity m\_\{Z,Y}, together with its positivity (closedSubspaceMultiplicity\_pos, Lemma 0EE4)”.

> **Stacks 0EE9, part (1).** The multiplicity `m_{W, Y}` of an integral closed subspace
> `W ⊆ Y` in a closed subspace `Y ⊆ X`: the length of `𝒪_Y` at the generic point of `W`, read
> inside `Y`, at a geometric representative of that generic point.
>
> This is the coefficient the sum of part (2) attaches to `W`, as
> `AlgebraicGeometry.Space.closedSubspaceCycle_apply_eq_finsum` records. The representative used
> is `AlgebraicGeometry.Space.canonicalGeometricPoint`, but by Stacks 0EE1
> (`AlgebraicGeometry.Space.closedSubspaceMultiplicity_eq_toNat_geometricLength`) the value does
> not depend on this choice.

```lean
def closedSubspaceMultiplicity (Y : Subfunctor X)
    (hY : IsClosedSubspace D.site D.base D.base_mem Y)
    (W : IntegralClosedSubspace D.site D.base D.base_mem Y.toFunctor) : ℤ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.5, Tag 0EE7](https://stacks.math.columbia.edu/tag/0EE7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
