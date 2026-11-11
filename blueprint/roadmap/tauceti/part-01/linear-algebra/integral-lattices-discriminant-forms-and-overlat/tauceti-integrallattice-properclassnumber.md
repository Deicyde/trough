---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.properClassNumber
statement: formalized
---

# TauCeti.IntegralLattice.properClassNumber

The proper class number `h⁺(L)`: the number of proper classes in the genus of `L`. It is `0`
when the genus contains infinitely many proper classes.

```lean
TauCeti.IntegralLattice.properClassNumber.{u} {V : Type u} [AddCommGroup V] [_root_.Module ℚ V]
  (L : TauCeti.IntegralLattice V) : ℕ
```

## Depends on

- [TauCeti.IntegralLattice](tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.properClassNumber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/ProperClassNumber.html#TauCeti.IntegralLattice.properClassNumber).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.properClassNumber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/ProperClassNumber.html#TauCeti.IntegralLattice.properClassNumber)
- [Source of `TauCeti.IntegralLattice.properClassNumber` in TauCeti/NumberTheory/IntegralLattice/ProperClassNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/IntegralLattice/ProperClassNumber.lean#L154)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/IntegralLattices/STATUS.md)
