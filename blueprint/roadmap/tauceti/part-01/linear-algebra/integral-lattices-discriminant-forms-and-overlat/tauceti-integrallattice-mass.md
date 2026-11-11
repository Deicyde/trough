---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.mass
statement: formalized
---

# TauCeti.IntegralLattice.mass

The **mass** of the genus of `L`: the sum of `1 / |O(M)|` over the classes `cls M` in the genus
of `L`. It is a finite sum when the genus contains finitely many classes.

Since `Nat.card` of an infinite type is `0` and `0⁻¹ = 0`, a class whose isometry group is infinite
contributes `0`, and `finsum` makes the mass of a genus with infinitely many classes `0`. The mass
therefore has its classical meaning only for definite lattices, where `O(M)` is finite.

```lean
TauCeti.IntegralLattice.mass.{u} {V : Type u} [AddCommGroup V] [_root_.Module ℚ V]
  (L : TauCeti.IntegralLattice V) : ℚ
```

## Depends on

- [TauCeti.IntegralLattice](tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.mass`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/Mass.html#TauCeti.IntegralLattice.mass).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.mass`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/Mass.html#TauCeti.IntegralLattice.mass)
- [Source of `TauCeti.IntegralLattice.mass` in TauCeti/NumberTheory/IntegralLattice/Mass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/IntegralLattice/Mass.lean#L97)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/IntegralLattices/STATUS.md)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/IntegralLattices/STATUS.md)
