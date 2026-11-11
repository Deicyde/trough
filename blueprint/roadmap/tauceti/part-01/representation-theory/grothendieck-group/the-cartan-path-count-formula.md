---
declaration: theorem
origin: cited
lean: TauCeti.jordanHolderMultiplicity_vertexProjectiveModuleFG_eq_card_path
statement: formalized
proof: formalized
---

# The Cartan path-count formula

The multiplicity of `Sᵢ` in the vertex projective `Pⱼ`
is the number of oriented paths from `j` to `i`. With simples in rows and projectives in columns,
these are the entries of the Cartan matrix of a finite acyclic path algebra.

```lean
TauCeti.jordanHolderMultiplicity_vertexProjectiveModuleFG_eq_card_path.{v, w} (k : Type (max v w))
  (Q : Type v) [Field k] [Quiver Q] [Finite Q] [FiniteDimensional k (TauCeti.pathAlgebra k Q)]
  (i j : Q) :
  TauCeti.jordanHolderMultiplicity (TauCeti.pathAlgebra k Q)
      ↑(TauCeti.vertexProjectiveModuleFG k Q j) ↑(TauCeti.vertexSimpleModuleFG k Q i) =
    Nat.card (Quiver.Path j i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.jordanHolderMultiplicity_vertexProjectiveModuleFG_eq_card_path`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/Quiver/Multiplicity.html#TauCeti.jordanHolderMultiplicity_vertexProjectiveModuleFG_eq_card_path).

## Sources

- [Tau Ceti documentation: `TauCeti.jordanHolderMultiplicity_vertexProjectiveModuleFG_eq_card_path`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/Quiver/Multiplicity.html#TauCeti.jordanHolderMultiplicity_vertexProjectiveModuleFG_eq_card_path)
- [Source of `TauCeti.jordanHolderMultiplicity_vertexProjectiveModuleFG_eq_card_path` in TauCeti/RepresentationTheory/GrothendieckGroup/Quiver/Multiplicity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/GrothendieckGroup/Quiver/Multiplicity.lean#L136)
