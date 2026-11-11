---
declaration: abbrev
origin: cited
lean: TauCeti.AInfinityAlgebra.PositiveHochschild.normalizedComplex
statement: formalized
---

# TauCeti.AInfinityAlgebra.PositiveHochschild.normalizedComplex

The **normalized Hochschild complex** of a strictly unital `A∞` algebra: the normalized
positive-arity suspended Hochschild cochains, with differential `[m, -]`.

```lean
TauCeti.AInfinityAlgebra.PositiveHochschild.normalizedComplex.{uR, uA} {R : Type uR} {A : Type uA}
  [CommRing R] [AddCommGroup A] [_root_.Module R A] (𝒜 : TauCeti.AInfinityAlgebra R A) {e : A}
  (h : 𝒜.StrictUnit e) : CochainComplex (ModuleCat R) ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hochschild differential squares to zero](the-hochschild-differential-squares-to-zero.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityAlgebra.PositiveHochschild.normalizedComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Hochschild/Normalized.html#TauCeti.AInfinityAlgebra.PositiveHochschild.normalizedComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityAlgebra.PositiveHochschild.normalizedComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Hochschild/Normalized.html#TauCeti.AInfinityAlgebra.PositiveHochschild.normalizedComplex)
- [Source of `TauCeti.AInfinityAlgebra.PositiveHochschild.normalizedComplex` in TauCeti/Algebra/Homology/AInfinity/Algebra/Hochschild/Normalized.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/AInfinity/Algebra/Hochschild/Normalized.lean#L370)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGAInfinity/STATUS.md)
