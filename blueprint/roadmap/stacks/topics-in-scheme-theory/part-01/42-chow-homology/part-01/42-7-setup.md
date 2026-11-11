---
declaration: section
origin: cited
lean: Stacks.Chow.ChowSituation, Stacks.Chow.fieldChowSituation, AlgebraicGeometry.fieldBaseDimensionFunction, Stacks.Chow.exists_chowSituation_spec_of_ringKrullDim_eq_one, AlgebraicGeometry.negativeLocalRingDimension, AlgebraicGeometry.IsCohenMacaulay.isLocallyNoetherian, AlgebraicGeometry.IsCohenMacaulay.isUniversallyCatenary, AlgebraicGeometry.IsCohenMacaulay.negativeLocalRingDimension_isDimensionFunction
statement: formalized
proof: formalized
---

# 42.7 Setup

Section 42.7 of the Stacks Project, [Tag 02QK](https://stacks.math.columbia.edu/tag/02QK). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02QL, a situation

[Tag 02QL](https://stacks.math.columbia.edu/tag/02QL) in the Stacks Project.

**`Stacks.Chow.ChowSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean#L103).

> The base situation of chapter 42: a locally Noetherian, universally catenary scheme equipped
> with a dimension function on its underlying topological space.

```lean
structure ChowSituation
```

## Tag 02QM, an example

[Tag 02QM](https://stacks.math.columbia.edu/tag/02QM) in the Stacks Project.

**`Stacks.Chow.fieldChowSituation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FieldSituation/Base.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FieldSituation/Base.lean#L90). The attribute's comment: “the spectrum of a field with the zero dimension function is a Situation 02QL”.

> **Stacks 02QM.** For a field `k`, the pair `(Spec k, δ)` with `δ(pt) = 0` at the unique point
> is a base situation of chapter 42 (Situation 02QL): `Spec k` is Noetherian, it is universally
> catenary (`AlgebraicGeometry.Scheme.isUniversallyCatenary_spec_of_field`), and the constant zero
> is a dimension function on it (`Stacks.Chow.fieldDimensionFunction`). The base scheme is
> `Spec k` by definition, and the dimension function vanishes by
> `Stacks.Chow.fieldChowSituation_dimensionFunction`.
>
> It is an `abbrev` so that its base scheme is reducibly `Spec k`: the cycle groups of the fibres
> of a morphism are formed for this situation, and instance search on them has to see through to
> `AlgebraicGeometry.Spec`.

```lean
abbrev fieldChowSituation (k : Type u) [Field k] : ChowSituation.{u}
```

**`AlgebraicGeometry.fieldBaseDimensionFunction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/Field.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/Field.lean#L35). The attribute's comment: “field\_base\_dimension\_function”.

> The base dimension function on the spectrum of a field, taking every point to zero.

```lean
abbrev fieldBaseDimensionFunction (k : Type u) [Field k] :
    AlgebraicGeometry.Spec (.of k) → ℤ
```

## Tag 02QN, an example

[Tag 02QN](https://stacks.math.columbia.edu/tag/02QN) in the Stacks Project.

**`Stacks.Chow.exists_chowSituation_spec_of_ringKrullDim_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/DimensionOneDomain.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/DimensionOneDomain.lean#L147).

> The spectrum of a Noetherian domain of Krull dimension one, with the dimension function
> which is zero at its maximal ideals and one at its generic point, is a base situation for Chow
> homology.

```lean
theorem exists_chowSituation_spec_of_ringKrullDim_eq_one (A : Type u) [CommRing A] [IsDomain A]
    [IsNoetherianRing A] (hdim : ringKrullDim A = 1) :
    ∃ (C : ChowSituation.{u}) (hC : C.S = Spec (CommRingCat.of A)),
      (∀ p : PrimeSpectrum A, p.asIdeal.IsMaximal →
        (hC ▸ C.dimensionFunction) p = 0) ∧
      (hC ▸ C.dimensionFunction) (⊥ : PrimeSpectrum A) = 1
```

## Tag 0F91, an example

[Tag 0F91](https://stacks.math.columbia.edu/tag/0F91) in the Stacks Project.

**`AlgebraicGeometry.negativeLocalRingDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/CohenMacaulayBase.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/CohenMacaulayBase.lean#L93). The attribute's comment: “the function”.

> The negative of the dimension of the local ring of a scheme at a point, as an integer.

```lean
noncomputable def negativeLocalRingDimension (S : Scheme.{u}) (s : S) : ℤ
```

**`AlgebraicGeometry.IsCohenMacaulay.isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/CohenMacaulayBase.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/CohenMacaulayBase.lean#L100). The attribute's comment: “local Noetherianity”.

> **Stacks Project, Tag 0F91.** A Cohen--Macaulay scheme is locally Noetherian.

```lean
theorem IsCohenMacaulay.isLocallyNoetherian {S : Scheme.{u}} (hS : IsCohenMacaulay S) :
    IsLocallyNoetherian S
```

**`AlgebraicGeometry.IsCohenMacaulay.isUniversallyCatenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/CohenMacaulayBase.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/CohenMacaulayBase.lean#L108). The attribute's comment: “universal catenarity”. References: EGA IV (5.2.5), “more general”; SGA 6 X (1.5), “special case”.

> **Stacks Project, Tag 0F91.** A Cohen--Macaulay scheme is universally catenary: each of its
> local rings is a Noetherian Cohen--Macaulay local ring, hence universally catenary, and
> universal catenarity of a locally Noetherian scheme is a condition on its local rings.

```lean
theorem IsCohenMacaulay.isUniversallyCatenary {S : Scheme.{u}} (hS : IsCohenMacaulay S)
    [IsLocallyNoetherian S] : Scheme.IsUniversallyCatenary S
```

**`AlgebraicGeometry.IsCohenMacaulay.negativeLocalRingDimension_isDimensionFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/CohenMacaulayBase.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/CohenMacaulayBase.lean#L264). The attribute's comment: “the dimension function”. References: SGA 6 X (1.5), “CM S, (1.5.1) on S”.

> **Stacks Project, Tag 0F91.** On a Cohen--Macaulay scheme the negative of the dimension of
> the local ring is a dimension function: it strictly increases along a nontrivial generization,
> and drops by exactly one along an immediate specialization.

```lean
theorem IsCohenMacaulay.negativeLocalRingDimension_isDimensionFunction {S : Scheme.{u}}
    (hS : IsCohenMacaulay S) :
    ∃ d : DimensionFunction S, ∀ s : S, d s = negativeLocalRingDimension S s
```

## Tag 02QO, a lemma

[Tag 02QO](https://stacks.math.columbia.edu/tag/02QO) in the Stacks Project.

**`Stacks.Chow.relativeDimension_nonneg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/JacobsonDimension.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/JacobsonDimension.lean#L241). The attribute's comment: “nonnegativity of the relative dimension”.

> **Stacks Project, Tag 02QO.** Over a Jacobson base whose dimension function vanishes at
> closed points, the relative dimension of a scheme locally of finite type is nonnegative. Every
> point specializes to a closed point of the closure of its singleton, where the relative
> dimension vanishes, and a dimension function strictly decreases along specialization.

```lean
theorem relativeDimension_nonneg {X : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] (x : X) :
    0 ≤ relativeDimension C.dimensionFunction f x
```

**`Stacks.Chow.topologicalKrullDim_eq_relativeDimension_toNat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/JacobsonDimension.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/JacobsonDimension.lean#L260). The attribute's comment: “relative dimension equals the dimension of the closed subscheme”.

> **Stacks Project, Tag 02QO.** The dimension of an integral closed subscheme of a scheme
> locally of finite type over a Jacobson base is the relative dimension at its generic point. The
> latter is converted to a natural number; its nonnegativity is
> `Stacks.Chow.relativeDimension_nonneg`.

```lean
theorem topologicalKrullDim_eq_relativeDimension_toNat {X Z : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (i : Z ⟶ X) [IsClosedImmersion i] [IsIntegral Z] (ξ : Z)
    (hξ : IsGenericPoint ξ (Set.univ : Set Z)) :
    topologicalKrullDim Z = (relativeDimension C.dimensionFunction f (i ξ)).toNat
```

**`Stacks.Chow.topologicalKrullDim_eq_ringKrullDim_stalk_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Setup/JacobsonDimension.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Setup/JacobsonDimension.lean#L285). The attribute's comment: “dimension of the local ring at a closed point”. References: EGA IV (10.6.1), “(i)”.

> **Stacks Project, Tag 02QO.** The dimension of an integral closed subscheme of a scheme
> locally of finite type over a Jacobson base equals the dimension of its local ring at every
> closed point.

```lean
theorem topologicalKrullDim_eq_ringKrullDim_stalk_of_isClosed {X Z : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (i : Z ⟶ X) [IsClosedImmersion i] [IsIntegral Z] (z : Z)
    (hz : IsClosed ({z} : Set Z)) :
    topologicalKrullDim Z = ringKrullDim (Z.presheaf.stalk z)
```

## Tag 02QP, a definition

[Tag 02QP](https://stacks.math.columbia.edu/tag/02QP) in the Stacks Project.

**`Stacks.Chow.deltaDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean#L120). The attribute's comment: “irreducible closed subsets”.

> The delta-dimension of an irreducible closed subset of a scheme locally of finite type over
> the base is the value at its generic point of the dimension function propagated from the base.

```lean
def deltaDimension (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (Z : IrreducibleCloseds X) : ℤ
```

**`Stacks.Chow.schemeDeltaDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean#L136). The attribute's comment: “closed subschemes”.

> The delta-dimension of a scheme locally of finite type over the base is the supremum of the
> delta-dimensions of its irreducible components. In particular this defines the delta-dimension
> of every closed subscheme of such a scheme.

```lean
def schemeDeltaDimension (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] : EInt
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.7, Tag 02QK](https://stacks.math.columbia.edu/tag/02QK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
