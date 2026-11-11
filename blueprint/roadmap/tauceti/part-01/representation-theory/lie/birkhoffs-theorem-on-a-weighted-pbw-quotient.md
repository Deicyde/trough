---
declaration: theorem
origin: cited
lean: TauCeti.exists_faithful_weightedPBWRepresentation
statement: formalized
proof: formalized
---

# Birkhoff's theorem on a weighted PBW quotient

A finite-dimensional nilpotent Lie
algebra has a faithful left-multiplication representation on a finite-dimensional weighted
enveloping quotient, with one positive nilpotence bound for all acting operators.
The basis, weights, and cutoff are supplied by the conclusion, in every characteristic.

```lean
TauCeti.exists_faithful_weightedPBWRepresentation.{u_1, u_2} (K : Type u_1) (L : Type u_2) [Field K]
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [LieRing.IsNilpotent L] :
  ∃ N b w,
    ∃ (hbracket :
      ∀ (i j k : Fin (Module.finrank K L)), w k < w i + w j → (b.repr ⁅b i, b j⁆) k = 0),
      0 < N ∧
        (∀ (i : Fin (Module.finrank K L)), 0 < w i ∧ w i < N) ∧
          Module.Finite K (UniversalEnvelopingAlgebra K L ⧸ b.weightedPBWIdeal w hbracket N) ∧
            Function.Injective ⇑(b.weightedPBWRepresentation w hbracket N) ∧
              ∀ (x : L), (b.weightedPBWRepresentation w hbracket N) x ^ N = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_faithful_weightedPBWRepresentation`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/NilpotentFaithful.html#TauCeti.exists_faithful_weightedPBWRepresentation).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_faithful_weightedPBWRepresentation`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/NilpotentFaithful.html#TauCeti.exists_faithful_weightedPBWRepresentation)
- [Source of `TauCeti.exists_faithful_weightedPBWRepresentation` in TauCeti/RepresentationTheory/Lie/NilpotentFaithful.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Lie/NilpotentFaithful.lean#L102)
