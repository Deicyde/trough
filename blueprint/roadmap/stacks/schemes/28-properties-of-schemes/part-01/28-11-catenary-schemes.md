---
declaration: section
origin: cited
lean: IrreducibleClosedsCodim.IsCatenarySpace, AlgebraicGeometry.isCatenarySpace_tfae, AlgebraicGeometry.IsCatenarySpace.of_isImmersion, AlgebraicGeometry.isCatenarySpace_iff_locally_dimensionFunction, AlgebraicGeometry.isCatenarySpace_iff_stalk_isCatenary
statement: formalized
proof: formalized
---

# 28.11 Catenary schemes

Section 28.11 of the Stacks Project, [Tag 02IV](https://stacks.math.columbia.edu/tag/02IV). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02IW, a definition

[Tag 02IW](https://stacks.math.columbia.edu/tag/02IW) in the Stacks Project.

Declarations registered for the tag:

- [`IrreducibleClosedsCodim.IsCatenarySpace`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/Catenary.lean#L104), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/Catenary.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Catenary.lean#L70) (StacksFrontier).

## Tag 02IX, a lemma

[Tag 02IX](https://stacks.math.columbia.edu/tag/02IX) in the Stacks Project.

**`AlgebraicGeometry.isCatenarySpace_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/SchemeTypesAndCatenary/Catenary.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/SchemeTypesAndCatenary/Catenary.lean#L186). The attribute's comment: “local criteria”.

> A scheme is catenary exactly when this holds on an open covering, or when the rings of
> sections of every affine open (equivalently, of one affine open covering) are catenary.

```lean
public theorem isCatenarySpace_tfae (S : Scheme.{u}) :
    List.TFAE [
      IsCatenarySpace S,
      ∃ (ι : Type u) (U : ι → S.Opens),
        IsOpenCover U ∧ ∀ i, IsCatenarySpace (U i).toScheme,
      ∀ U : S.affineOpens, Ring.IsCatenary Γ(S, U),
      ∃ (ι : Type u) (U : ι → S.affineOpens),
        IsOpenCover (fun i ↦ (U i : S.Opens)) ∧
          ∀ i, Ring.IsCatenary Γ(S, U i)]
```

**`AlgebraicGeometry.IsCatenarySpace.of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/SchemeTypesAndCatenary/Catenary.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/SchemeTypesAndCatenary/Catenary.lean#L209). The attribute's comment: “locally closed subschemes”.

> A locally closed subscheme of a catenary scheme is catenary.

```lean
public theorem IsCatenarySpace.of_isImmersion {S Z : Scheme.{u}} (i : Z ⟶ S)
    [IsImmersion i] (hS : IsCatenarySpace S) : IsCatenarySpace Z
```

## Tag 02IY, a lemma

[Tag 02IY](https://stacks.math.columbia.edu/tag/02IY) in the Stacks Project.

**`AlgebraicGeometry.isCatenarySpace_iff_locally_dimensionFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Catenary.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Catenary.lean#L51). References: SGA 6 X (1.6), “more general”.

> A locally Noetherian scheme is catenary if and only if every point has an open
> neighbourhood admitting a dimension function.

```lean
public theorem isCatenarySpace_iff_locally_dimensionFunction
    (S : Scheme.{u}) [IsLocallyNoetherian S] :
    IrreducibleClosedsCodim.IsCatenarySpace S ↔
      ∀ x : S, ∃ U : Set S, IsOpen U ∧ x ∈ U ∧ Nonempty (DimensionFunction U)
```

## Tag 02J0, a lemma

[Tag 02J0](https://stacks.math.columbia.edu/tag/02J0) in the Stacks Project.

**`AlgebraicGeometry.isCatenarySpace_iff_stalk_isCatenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/SchemeTypesAndCatenary/Catenary.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/SchemeTypesAndCatenary/Catenary.lean#L308).

> A scheme is catenary if and only if each of its local rings is catenary.

```lean
public theorem isCatenarySpace_iff_stalk_isCatenary (X : Scheme.{u}) :
    IrreducibleClosedsCodim.IsCatenarySpace X ↔
      ∀ x : X, Ring.IsCatenary (X.presheaf.stalk x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.11, Tag 02IV](https://stacks.math.columbia.edu/tag/02IV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
