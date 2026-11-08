---
declaration: def
origin: cited
lean: TauCeti.eisensteinSet
statement: formalized
---

# TauCeti.eisensteinSet

The Eisenstein region in the space `Fin n → K` of coefficient vectors of monic polynomials of
degree `n`: every coefficient has valuation below `1`, and the constant term of `monicOfCoeff a`
has valuation at least that of every element of valuation below `1`. For `0 < n` the constant term
is `a 0`, which then has the valuation of a uniformizer; for `n = 0` it is `1`, and the region is
the whole one-point space. When `𝒪[K]` is a discrete valuation ring,
`TauCeti.mem_eisensteinSet_iff_exists_isEisensteinAt` identifies these with the coefficient vectors
of the polynomials over `𝒪[K]` that are Eisenstein at `𝓂[K]`.

```lean
TauCeti.eisensteinSet.{u_1} (K : Type u_1) [Field K] [ValuativeRel K] (n : ℕ) : Set (Fin n → K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.eisensteinSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Eisenstein/Region.html#TauCeti.eisensteinSet).

## Sources

- [Tau Ceti documentation: `TauCeti.eisensteinSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Eisenstein/Region.html#TauCeti.eisensteinSet)
- [Source of `TauCeti.eisensteinSet` in TauCeti/NumberTheory/LocalField/MassFormula/Eisenstein/Region.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Eisenstein/Region.lean#L92)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
