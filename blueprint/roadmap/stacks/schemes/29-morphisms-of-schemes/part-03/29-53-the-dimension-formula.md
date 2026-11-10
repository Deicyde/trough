---
declaration: section
origin: cited
lean: AlgebraicGeometry.ringKrullDim_stalk_add_trdeg_residueField_le, AlgebraicGeometry.ringKrullDim_stalk_add_trdeg_residueField_eq, AlgebraicGeometry.localDimension_add_trdeg_le, AlgebraicGeometry.localDimension_add_trdeg_eq, AlgebraicGeometry.ringKrullDim_stalk_add_residueFieldTranscendenceDegree_le, Stacks.Chow.relativeDimension_isDimensionFunction, AlgebraicGeometry.topologicalKrullDim_le_add_trdeg, AlgebraicGeometry.topologicalKrullDim_eq_add_trdeg_of_isClosedMap
statement: formalized
proof: formalized
---

# 29.53 The dimension formula

Section 29.53 of the Stacks Project, [Tag 02JT](https://stacks.math.columbia.edu/tag/02JT). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02JU, a lemma

[Tag 02JU](https://stacks.math.columbia.edu/tag/02JU) in the Stacks Project.

**`AlgebraicGeometry.ringKrullDim_stalk_add_trdeg_residueField_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DimensionFormula/Formula.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DimensionFormula/Formula.lean#L100). The attribute's comment: “inequality”. References: EGA IV (13.3.4), “Inequality dim O_{X_j”; EGA IV (5.5.6), “partial”; EGA IV (5.5.8), “more general”; EGA IV (5.6.5), “(5.6.5.1), special case”.

> The dimension formula for a dominant morphism `f : X ⟶ S` locally of finite type between
> integral schemes over a locally Noetherian base:
> `dim 𝒪_{X, x} + trdeg_{κ(f x)} κ(x) ≤ dim 𝒪_{S, f x} + trdeg_{R(S)} R(X)`.

```lean
theorem ringKrullDim_stalk_add_trdeg_residueField_le
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] [IsIntegral X] [IsIntegral S] [IsDominant f]
    (x : X) :
    letI : Algebra (S.residueField (f x)) (X.residueField x) :=
      (f.residueFieldMap x).hom.toAlgebra
    letI : Algebra S.functionField X.functionField := f.functionFieldMap.hom.toAlgebra
    ringKrullDim (X.presheaf.stalk x) +
        (Cardinal.toNat (Algebra.trdeg (S.residueField (f x)) (X.residueField x)) : WithBot ℕ∞)
      ≤ ringKrullDim (S.presheaf.stalk (f x)) +
        (Cardinal.toNat (Algebra.trdeg S.functionField X.functionField) : WithBot ℕ∞)
```

**`AlgebraicGeometry.ringKrullDim_stalk_add_trdeg_residueField_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DimensionFormula/Formula.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DimensionFormula/Formula.lean#L119). The attribute's comment: “equality for a universally catenary base”. References: EGA IV (5.5.8), “special case”; EGA IV (5.6.5), “partial”.

> Over a universally catenary base the dimension formula is an equality:
> `dim 𝒪_{X, x} + trdeg_{κ(f x)} κ(x) = dim 𝒪_{S, f x} + trdeg_{R(S)} R(X)`.

```lean
theorem ringKrullDim_stalk_add_trdeg_residueField_eq
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] [IsIntegral X] [IsIntegral S] [IsDominant f]
    (hS : Scheme.IsUniversallyCatenary S) (x : X) :
    letI : Algebra (S.residueField (f x)) (X.residueField x) :=
      (f.residueFieldMap x).hom.toAlgebra
    letI : Algebra S.functionField X.functionField := f.functionFieldMap.hom.toAlgebra
    ringKrullDim (X.presheaf.stalk x) +
        (Cardinal.toNat (Algebra.trdeg (S.residueField (f x)) (X.residueField x)) : WithBot ℕ∞)
      = ringKrullDim (S.presheaf.stalk (f x)) +
        (Cardinal.toNat (Algebra.trdeg S.functionField X.functionField) : WithBot ℕ∞)
```

**`AlgebraicGeometry.localDimension_add_trdeg_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionFormula.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionFormula.lean#L400). The attribute's comment: “dimension-formula inequality”.

> **Stacks 02JU.** The dimension formula for a dominant locally finite-type morphism of
> integral schemes over a locally Noetherian base: the dimension of the local ring at `x` plus
> the transcendence degree of `κ(x)/κ(f x)` is at most the dimension of the local ring at `f x`
> plus the transcendence degree of the function field extension.

```lean
theorem localDimension_add_trdeg_le {X S : Scheme.{u}} (f : X ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f]
    [IsIntegral X] [IsIntegral S] [IsDominant f] (x : X) :
    letI := (dominantFunctionFieldMap f).toAlgebra
    letI := (f.residueFieldMap x).hom.toAlgebra
    ringKrullDim (X.presheaf.stalk x) +
        (Cardinal.toENat
          (Algebra.trdeg (S.residueField (f x)) (X.residueField x)) : WithBot ℕ∞) ≤
      ringKrullDim (S.presheaf.stalk (f x)) +
        (Cardinal.toENat (Algebra.trdeg S.functionField X.functionField) : WithBot ℕ∞)
```

**`AlgebraicGeometry.localDimension_add_trdeg_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionFormula.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionFormula.lean#L417). The attribute's comment: “universally catenary equality”.

> **Stacks 02JU.** Over a universally catenary base the dimension formula is an equality.

```lean
theorem localDimension_add_trdeg_eq {X S : Scheme.{u}} (f : X ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f]
    [IsIntegral X] [IsIntegral S] [IsDominant f]
    (hS : Scheme.IsUniversallyCatenary S) (x : X) :
    letI := (dominantFunctionFieldMap f).toAlgebra
    letI := (f.residueFieldMap x).hom.toAlgebra
    ringKrullDim (X.presheaf.stalk x) +
        (Cardinal.toENat
          (Algebra.trdeg (S.residueField (f x)) (X.residueField x)) : WithBot ℕ∞) =
      ringKrullDim (S.presheaf.stalk (f x)) +
        (Cardinal.toENat (Algebra.trdeg S.functionField X.functionField) : WithBot ℕ∞)
```

## Tag 0BAE, a lemma

[Tag 0BAE](https://stacks.math.columbia.edu/tag/0BAE) in the Stacks Project.

**`AlgebraicGeometry.ringKrullDim_stalk_add_residueFieldTranscendenceDegree_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionFormula.lean, line 881](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionFormula.lean#L881). References: EGA IV (13.3.4), “partial”; EGA IV (5.5.6), “partial”; EGA IV (5.5.7), “more general”; EGA IV (5.5.8), “more general”; EGA IV (5.6.5), “more general”.

> **Stacks 0BAE.** The general dimension formula: for a morphism `f : X ⟶ S` locally of finite
> type over a locally Noetherian scheme and a point `x` of `X`,
> `dim 𝒪_{X,x} + trdeg_{κ(f x)} κ(x) ≤ dim 𝒪_{S,f x} + E`, where `E` is the supremum of
> `trdeg_{κ(f ξ)} κ(ξ)` over the generic points `ξ` of the irreducible components of `X`
> containing `x`.

```lean
theorem ringKrullDim_stalk_add_residueFieldTranscendenceDegree_le {X S : Scheme.{u}}
    (f : X ⟶ S) (x : X)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] :
    ringKrullDim (X.presheaf.stalk x) + (residueFieldTranscendenceDegree f x : WithBot ℕ∞) ≤
      ringKrullDim (S.presheaf.stalk (f x)) +
        (genericResidueFieldTranscendenceDegreeAt f x : WithBot ℕ∞)
```

## Tag 02JW, a lemma

[Tag 02JW](https://stacks.math.columbia.edu/tag/02JW) in the Stacks Project.

**`Stacks.Chow.relativeDimension_isDimensionFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeDimension.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeDimension.lean#L544). References: SGA 6 X (1.5), “special case”.

> **Stacks 02JW.** A dimension function on a locally Noetherian universally catenary scheme
> propagates along every locally finite-type morphism by adding the transcendence degree of the
> residue-field extension: `relativeDimension δ f` is the underlying function of a dimension
> function on the source.

```lean
theorem relativeDimension_isDimensionFunction {X S : Scheme.{u}}
    [IsLocallyNoetherian S] (hS : Scheme.IsUniversallyCatenary S)
    (δ : DimensionFunction S) (f : X ⟶ S) [LocallyOfFiniteType f] :
    ∃ d : DimensionFunction X, ∀ x, d x = relativeDimension δ f x
```

## Tag 02JX, a lemma

[Tag 02JX](https://stacks.math.columbia.edu/tag/02JX) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDim_le_add_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionDominant.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionDominant.lean#L162). The attribute's comment: “dimension inequality”.

> **Stacks Project, Tag 02JX.** For a dominant morphism of integral schemes locally of finite
> type over a locally Noetherian base, the dimension of the source is at most the dimension of the
> target plus the transcendence degree of the extension of function fields.

```lean
theorem topologicalKrullDim_le_add_trdeg (f : X ⟶ Y) [IsLocallyNoetherian Y]
    [IsIntegral X] [IsIntegral Y] [IsDominant f] [LocallyOfFiniteType f] :
    letI := (functionFieldMap f).toAlgebra
    topologicalKrullDim X ≤ topologicalKrullDim Y +
      (Cardinal.toENat (Algebra.trdeg Y.functionField X.functionField) : WithBot ℕ∞)
```

**`AlgebraicGeometry.topologicalKrullDim_eq_add_trdeg_of_isClosedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionDominant.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionDominant.lean#L233). The attribute's comment: “equality for closed morphisms”.

> **Stacks Project, Tag 02JX.** For a *closed* dominant morphism of integral schemes locally of
> finite type over a locally Noetherian base — in particular for a proper one — the bound on the
> dimension of the source is an equality.

```lean
theorem topologicalKrullDim_eq_add_trdeg_of_isClosedMap (f : X ⟶ Y) [IsLocallyNoetherian Y]
    [IsIntegral X] [IsIntegral Y] [IsDominant f] [LocallyOfFiniteType f] (hf : IsClosedMap f) :
    letI := (functionFieldMap f).toAlgebra
    topologicalKrullDim X = topologicalKrullDim Y +
      (Cardinal.toENat (Algebra.trdeg Y.functionField X.functionField) : WithBot ℕ∞)
```

## Tag 0BAG, a lemma

[Tag 0BAG](https://stacks.math.columbia.edu/tag/0BAG) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDim_le_add_iSup_residueFieldTrdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionFormula.lean, line 920](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/DimensionFormula.lean#L920). References: EGA IV (5.6.6), “more general”.

> **Stacks 0BAG.** The dimension of the source of a morphism locally of finite type over a
> locally Noetherian scheme is at most the dimension of the target plus the supremum of the
> residue-field transcendence degrees at the generic points of the irreducible components of the
> source.

```lean
theorem topologicalKrullDim_le_add_iSup_residueFieldTrdeg
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian Y] [LocallyOfFiniteType f] :
    topologicalKrullDim X ≤ topologicalKrullDim Y +
      ((⨆ ξ : genericPoints X, residueFieldTranscendenceDegree f ξ.1 : ℕ∞) : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.53, Tag 02JT](https://stacks.math.columbia.edu/tag/02JT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
