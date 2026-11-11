---
declaration: section
origin: cited
lean: Stacks.Chow.IsLocallyEquidimensional.of_isCohenMacaulay, Stacks.Chow.HasDimensionDecomposition.of_isCohenMacaulay, Stacks.Chow.IsLocallyPureDimensional.of_isCohenMacaulay, Stacks.Chow.locallyEquidimensional_tfae, Stacks.Chow.HasDimensionDecomposition.of_isNormal, Stacks.Chow.IsLocallyPureDimensional.of_isNormal, Stacks.Chow.IsLocallyEquidimensional.of_isNormal, Stacks.Chow.fundamentalClass
statement: formalized
proof: formalized
---

# 42.42 Cycles of given codimension

Section 42.42 of the Stacks Project, [Tag 0FE2](https://stacks.math.columbia.edu/tag/0FE2). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FE3, a lemma

[Tag 0FE3](https://stacks.math.columbia.edu/tag/0FE3) in the Stacks Project.

**`Stacks.Chow.IsLocallyEquidimensional.of_isCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Codimension/CohenMacaulayCase.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Codimension/CohenMacaulayCase.lean#L46). The attribute's comment: “cohen\_macaulay\_case”.

> **Stacks 0FE3.** The relative dimension function of a Cohen--Macaulay scheme locally of
> finite type over the base of a Chow situation is locally equidimensional: at each point, all
> irreducible components through it have the same relative dimension at their generic points.

```lean
theorem IsLocallyEquidimensional.of_isCohenMacaulay (B : ChowSituation.{u}) (X : Scheme.{u})
    (f : X ⟶ B.S) [LocallyOfFiniteType f] (hX : IsCohenMacaulay X) :
    IsLocallyEquidimensional (relativeDimension B.dimensionFunction f)
```

**`Stacks.Chow.HasDimensionDecomposition.of_isCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Codimension/CohenMacaulayCase.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Codimension/CohenMacaulayCase.lean#L70). The attribute's comment: “cohen\_macaulay\_case”.

> **Stacks 0FE3.** A Cohen--Macaulay scheme locally of finite type over the base of a Chow
> situation decomposes into open and closed subschemes of constant relative dimension.

```lean
theorem HasDimensionDecomposition.of_isCohenMacaulay (B : ChowSituation.{u}) (X : Scheme.{u})
    (f : X ⟶ B.S) [LocallyOfFiniteType f] (hX : IsCohenMacaulay X) :
    HasDimensionDecomposition (relativeDimension B.dimensionFunction f)
```

**`Stacks.Chow.IsLocallyPureDimensional.of_isCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Codimension/CohenMacaulayCase.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Codimension/CohenMacaulayCase.lean#L79). The attribute's comment: “cohen\_macaulay\_case”.

> **Stacks 0FE3.** The relative dimension function of a Cohen--Macaulay scheme locally of
> finite type over the base of a Chow situation is locally pure dimensional.

```lean
theorem IsLocallyPureDimensional.of_isCohenMacaulay (B : ChowSituation.{u}) (X : Scheme.{u})
    (f : X ⟶ B.S) [LocallyOfFiniteType f] (hX : IsCohenMacaulay X) :
    IsLocallyPureDimensional (relativeDimension B.dimensionFunction f)
```

**`Stacks.Chow.locallyEquidimensional_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Codimension/Equidimensional.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Codimension/Equidimensional.lean#L182). The attribute's comment: “equivalent\_conditions”.

> **Stacks 0FE3.** For an integer-valued function on a locally Noetherian scheme, having a
> decomposition into pure-dimensional open and closed subschemes, being locally pure dimensional,
> and being locally equidimensional are equivalent.

```lean
theorem locallyEquidimensional_tfae (X : Scheme.{u}) [IsLocallyNoetherian X] (δ : X → ℤ) :
    List.TFAE [
      HasDimensionDecomposition δ,
      IsLocallyPureDimensional δ,
      IsLocallyEquidimensional δ]
```

**`Stacks.Chow.HasDimensionDecomposition.of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Codimension/NormalCase.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Codimension/NormalCase.lean#L96). The attribute's comment: “normal\_case”.

> **Stacks 0FE3.** A locally Noetherian normal scheme decomposes into open and closed
> subschemes on whose irreducible components any given integer-valued function is constant at the
> generic points, the constant being the index of the piece.

```lean
theorem HasDimensionDecomposition.of_isNormal (X : Scheme.{u}) [IsLocallyNoetherian X]
    [IsNormal X] (δ : X → ℤ) : HasDimensionDecomposition δ
```

**`Stacks.Chow.IsLocallyPureDimensional.of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Codimension/NormalCase.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Codimension/NormalCase.lean#L130). The attribute's comment: “normal\_case”.

> **Stacks 0FE3.** On a locally Noetherian normal scheme every integer-valued function is
> locally pure dimensional.

```lean
theorem IsLocallyPureDimensional.of_isNormal (X : Scheme.{u}) [IsLocallyNoetherian X]
    [IsNormal X] (δ : X → ℤ) : IsLocallyPureDimensional δ
```

**`Stacks.Chow.IsLocallyEquidimensional.of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Codimension/NormalCase.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Codimension/NormalCase.lean#L137). The attribute's comment: “normal\_case”.

> **Stacks 0FE3.** On a locally Noetherian normal scheme every integer-valued function is
> locally equidimensional.

```lean
theorem IsLocallyEquidimensional.of_isNormal (X : Scheme.{u}) [IsLocallyNoetherian X]
    [IsNormal X] (δ : X → ℤ) : IsLocallyEquidimensional δ
```

## Tag 0FE4, a remark

[Tag 0FE4](https://stacks.math.columbia.edu/tag/0FE4) in the Stacks Project.

**`Stacks.Chow.fundamentalClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Codimension/FundamentalClass.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Codimension/FundamentalClass.lean#L60). The attribute's comment: “fundamental\_class”.

> **Stacks 0FE4.** The fundamental class `[X] = ∑_n [X_n]_n` of a scheme whose relative
> dimension function has a dimension decomposition: the family whose `n`th coordinate is the class
> in `CH_n(X_n)` of the cycle associated to the piece `X_n` itself.

```lean
def fundamentalClass (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f]
    (h : HasDimensionDecomposition (relativeDimension C.dimensionFunction f)) :
    degreeZeroChowGroup C f h
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.42, Tag 0FE2](https://stacks.math.columbia.edu/tag/0FE2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
