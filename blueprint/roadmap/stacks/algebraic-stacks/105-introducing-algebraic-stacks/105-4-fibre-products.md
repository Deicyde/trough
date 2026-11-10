---
declaration: section
origin: cited
lean: AlgebraicGeometry.ModuliEllipticCurves.Comparison, AlgebraicGeometry.ModuliEllipticCurves.Comparison.IsBaseChange, AlgebraicGeometry.ModuliEllipticCurves.RepresentsComparisons, AlgebraicGeometry.ModuliEllipticCurves.exists_representsComparisons, AlgebraicGeometry.ModuliEllipticCurves.PointedFamily.IsSmooth
statement: formalized
proof: formalized
---

# 105.4 Fibre products

Section 105.4 of the Stacks Project, [Tag 072L](https://stacks.math.columbia.edu/tag/072L). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 072L, the section

[Tag 072L](https://stacks.math.columbia.edu/tag/072L) in the Stacks Project.

**`AlgebraicGeometry.ModuliEllipticCurves.Comparison`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean#L173). The attribute's comment: “the triples (a, a', α)”.

> A `T`-point of `S ×_{𝓜₁,₁} S'`: morphisms `a : T ⟶ S` and `a' : T ⟶ S'` together with an
> isomorphism `α : E ×_{S,a} T ⟶ E' ×_{S',a'} T` of elliptic curves over `T`, that is, one
> compatible with the structure morphisms and the sections.

```lean
structure Comparison {S S' : Scheme.{u}} (E : PointedFamily S) (E' : PointedFamily S')
    (T : Scheme.{u})
```

**`AlgebraicGeometry.ModuliEllipticCurves.Comparison.IsBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean#L192). The attribute's comment: “pullback of the triples”.

> The triple `y` over `U` is the base change of the triple `x` over `T` along `h : U ⟶ T`
> when the two morphisms to the bases compose with `h` and the two isomorphisms agree after the
> canonical projections of the pulled-back families.

```lean
def IsBaseChange {S S' T : Scheme.{u}} {E : PointedFamily S} {E' : PointedFamily S'}
    (x : Comparison E E' T) {U : Scheme.{u}} (h : U ⟶ T) (y : Comparison E E' U) : Prop
```

**`AlgebraicGeometry.ModuliEllipticCurves.RepresentsComparisons`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean#L237). The attribute's comment: “the scheme S ×_{M_{1,1}} S'”.

> A scheme `P` is a fibre product `S ×_{𝓜₁,₁} S'` when its `T`-points are the triples
> `(a, a', α)`, naturally in `T`.

```lean
structure RepresentsComparisons {S S' : Scheme.{u}} (E : PointedFamily S)
    (E' : PointedFamily S') (P : Scheme.{u})
```

## Tag 072M, a lemma

[Tag 072M](https://stacks.math.columbia.edu/tag/072M) in the Stacks Project.

**`AlgebraicGeometry.ModuliEllipticCurves.exists_representsComparisons`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurvesFibreProduct.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurvesFibreProduct.lean#L86).

> **Stacks Project, Tag 072M.** *Key fact.* For elliptic curves `E` over `S` and `E'` over `S'`,
> the functor sending a scheme `T` to the triples `(a, a', α)` is representable by a scheme, the
> fibre product `S ×_{𝓜₁,₁} S'`.

```lean
theorem exists_representsComparisons (E : PointedFamily S) (E' : PointedFamily S')
    (hE : E.IsElliptic) (hE' : E'.IsElliptic) :
    ∃ P : Scheme.{u}, Nonempty (RepresentsComparisons E E' P)
```

## Tag 072P, a definition

[Tag 072P](https://stacks.math.columbia.edu/tag/072P) in the Stacks Project.

**`AlgebraicGeometry.ModuliEllipticCurves.PointedFamily.IsSmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean#L275).

> A morphism `S ⟶ 𝓜₁,₁`, that is, an elliptic curve over `S`, is smooth when for every
> morphism `S' ⟶ 𝓜₁,₁` the projection `S ×_{𝓜₁,₁} S' ⟶ S'` is a smooth morphism of schemes.

```lean
def PointedFamily.IsSmooth {S : Scheme.{u}} (E : PointedFamily S) (_hE : E.IsElliptic) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 105.4, Tag 072L](https://stacks.math.columbia.edu/tag/072L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
