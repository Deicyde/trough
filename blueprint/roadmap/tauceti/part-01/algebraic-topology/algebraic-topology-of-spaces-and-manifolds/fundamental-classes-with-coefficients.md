---
declaration: def
origin: cited
lean: TauCeti.IsFundamentalClass
statement: formalized
---

# Fundamental classes with coefficients

A class `μ` of `Hₙ(M; N)` is a *fundamental class*
when, for every point `x` of `M`, its image in the local homology `Hₙ(M, M ∖ {x}; N)` generates
that `R`-module. The image is the quotient map to `Hₙ(M, M ∖ M; N)` followed by restriction to
`{x}`. For `N = R` and `M` a topological `n`-manifold this is an `R`-fundamental class in the sense
of Hatcher, p.236.

```lean
TauCeti.IsFundamentalClass.{w, u} {M : Type w} [TopologicalSpace M] {R : Type u} [Ring R]
  {N : ModuleCat R} {n : ℕ} (μ : ↑((TopCat.toSSet.obj ↧M).homology N n)) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsFundamentalClass`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/LocalHomology/IsFundamentalClass.html#TauCeti.IsFundamentalClass).

## Sources

- [Tau Ceti documentation: `TauCeti.IsFundamentalClass`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/LocalHomology/IsFundamentalClass.html#TauCeti.IsFundamentalClass)
- [Source of `TauCeti.IsFundamentalClass` in TauCeti/AlgebraicTopology/Singular/LocalHomology/IsFundamentalClass.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/LocalHomology/IsFundamentalClass.lean#L79)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
