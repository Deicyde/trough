---
declaration: theorem
origin: cited
lean: TauCeti.koszulComplex.exactAt_of_isWeaklyRegular
statement: formalized
proof: formalized
---

# The Koszul complex of a weakly regular sequence is acyclic in positive degrees

if
`x = (x₀, …, xₙ₋₁)` is a weakly regular sequence in `R`, then `Hₖ₊₁(K(x)) = 0` for every `k`.
With `homologyZeroEquivSpan`, the complex of finite free modules `K(x)` resolves
`R ⧸ (x₀, …, xₙ₋₁)`.

```lean
TauCeti.koszulComplex.exactAt_of_isWeaklyRegular.{u} {R : Type u} [CommRing R] {n : ℕ}
  (x : Fin n → R) (hx : RingTheory.Sequence.IsWeaklyRegular R (List.ofFn x)) (k : ℕ) :
  HomologicalComplex.ExactAt (TauCeti.koszulComplex (Fintype.linearCombination R x)) (k + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.koszulComplex.exactAt_of_isWeaklyRegular`](https://taucetiproject.org/docs/TauCeti/RingTheory/KoszulComplex/Regular.html#TauCeti.koszulComplex.exactAt_of_isWeaklyRegular).

## Sources

- [Tau Ceti documentation: `TauCeti.koszulComplex.exactAt_of_isWeaklyRegular`](https://taucetiproject.org/docs/TauCeti/RingTheory/KoszulComplex/Regular.html#TauCeti.koszulComplex.exactAt_of_isWeaklyRegular)
- [Source of `TauCeti.koszulComplex.exactAt_of_isWeaklyRegular` in TauCeti/RingTheory/KoszulComplex/Regular.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/KoszulComplex/Regular.lean#L136)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
