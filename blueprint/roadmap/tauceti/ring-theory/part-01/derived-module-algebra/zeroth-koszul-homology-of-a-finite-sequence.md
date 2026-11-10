---
declaration: def
origin: cited
lean: TauCeti.koszulComplex.homologyZeroEquivSpan
statement: formalized
---

# Zeroth Koszul homology of a finite sequence

for `x = (xᵢ)` in `R`, the Koszul complex of
the functional `v ↦ ∑ᵢ vᵢ xᵢ` has `H₀ ≃ R ⧸ (xᵢ)`.

```lean
TauCeti.koszulComplex.homologyZeroEquivSpan.{u, u_1} {R : Type u} [CommRing R] {ι : Type u_1}
  [Fintype ι] (x : ι → R) :
  ↑(HomologicalComplex.homology (TauCeti.koszulComplex (Fintype.linearCombination R x)) 0) ≃ₗ[R]
    R ⧸ Ideal.span (Set.range x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.koszulComplex.homologyZeroEquivSpan`](https://taucetiproject.org/docs/TauCeti/RingTheory/KoszulComplex/Basic.html#TauCeti.koszulComplex.homologyZeroEquivSpan).

## Sources

- [Tau Ceti documentation: `TauCeti.koszulComplex.homologyZeroEquivSpan`](https://taucetiproject.org/docs/TauCeti/RingTheory/KoszulComplex/Basic.html#TauCeti.koszulComplex.homologyZeroEquivSpan)
- [Source of `TauCeti.koszulComplex.homologyZeroEquivSpan` in TauCeti/RingTheory/KoszulComplex/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/KoszulComplex/Basic.lean#L397)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
