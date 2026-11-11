---
declaration: theorem
origin: cited
lean: TauCeti.Comodule.isCompletelyReducible_of_isKilling
statement: formalized
proof: formalized
---

# Weyl's theorem for algebraic groups

Over an algebraically closed field of characteristic
zero, every finite-dimensional representation of a connected group whose Lie algebra has
nondegenerate Killing form is completely reducible.

```lean
TauCeti.Comodule.isCompletelyReducible_of_isKilling.{u, w} {k : Type u} [Field k] [CharZero k]
  [IsAlgClosed k] {H : TauCeti.FiniteTypeCommHopfAlgCat k} [ConnectedSpace (PrimeSpectrum ↑H.obj)]
  [LieAlgebra.IsKilling k (Derivation k (↑H.obj) (TauCeti.Bialgebra.CounitAlgebra k (↑H.obj) k))]
  {M : Type w} [AddCommGroup M] [_root_.Module k M] [TauCeti.Comodule k (↑H.obj) M]
  [FiniteDimensional k M] : TauCeti.Comodule.IsCompletelyReducible k (↑H.obj) M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartier's theorem](cartiers-theorem.md)
- [The global dimension of a regular local ring is its Krull dimension](../../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [Weyl's complete reducibility theorem](../../part-02/lie/part-02/weyls-complete-reducibility-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Comodule.isCompletelyReducible_of_isKilling`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/CompleteReducibility.html#TauCeti.Comodule.isCompletelyReducible_of_isKilling).

## Sources

- [Tau Ceti documentation: `TauCeti.Comodule.isCompletelyReducible_of_isKilling`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/CompleteReducibility.html#TauCeti.Comodule.isCompletelyReducible_of_isKilling)
- [Source of `TauCeti.Comodule.isCompletelyReducible_of_isKilling` in TauCeti/Algebra/AlgebraicGroup/Representation/CompleteReducibility.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Representation/CompleteReducibility.lean#L74)
