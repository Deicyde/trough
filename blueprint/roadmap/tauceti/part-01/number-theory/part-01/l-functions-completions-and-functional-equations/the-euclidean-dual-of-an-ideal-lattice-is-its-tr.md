---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.mixedEmbedding.mixedDual_idealLattice
statement: formalized
proof: formalized
---

# The Euclidean dual of an ideal lattice is its trace dual

the Euclidean dual
`mixedDual K σ(I)` of the lattice of a fractional ideal `I` is the image under
`traceToEuclidean K` of the lattice `σ(J)` of its trace dual
`J = I^∨ = FractionalIdeal.dual ℤ ℚ I`.

```lean
TauCeti.NumberField.mixedEmbedding.mixedDual_idealLattice.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {I J : (FractionalIdeal (nonZeroDivisors (NumberField.RingOfIntegers K)) K)ˣ}
  (hJ : ↑J = FractionalIdeal.dual ℤ ℚ ↑I) :
  TauCeti.NumberField.mixedEmbedding.mixedDual K (NumberField.mixedEmbedding.idealLattice K I) =
    Submodule.map (↑ℤ ↑↑(TauCeti.NumberField.mixedEmbedding.traceToEuclidean K))
      (NumberField.mixedEmbedding.idealLattice K J)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.mixedEmbedding.mixedDual_idealLattice`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/TraceDual.html#TauCeti.NumberField.mixedEmbedding.mixedDual_idealLattice).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.mixedEmbedding.mixedDual_idealLattice`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/TraceDual.html#TauCeti.NumberField.mixedEmbedding.mixedDual_idealLattice)
- [Source of `TauCeti.NumberField.mixedEmbedding.mixedDual_idealLattice` in TauCeti/NumberTheory/NumberField/CanonicalEmbedding/TraceDual.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/TraceDual.lean#L197)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LFunctions/STATUS.md)
