---
declaration: def
origin: cited
lean: TauCeti.SpinPolarizationData.evenCliffordEquivProdEnd
statement: formalized
---

# The even structure theorem

for an even-dimensional polarized quadratic space the even
Clifford subalgebra is the product of the endomorphism algebras of the two half-spin summands.

This is the even-subalgebra companion of `TauCeti.SpinPolarizationData.cliffordEquivEnd`. It gives
the invariant-subspace dichotomy for both summands, which is simplicity for `S⁺` and, when
`P.W ≠ ⊥`, for `S⁻`; it also distinguishes their two even-Clifford actions.

```lean
TauCeti.SpinPolarizationData.evenCliffordEquivProdEnd.{u, v} {K : Type u} [Field K] {V : Type v}
  [AddCommGroup V] [_root_.Module K V] {Q : QuadraticForm K V} (P : TauCeti.SpinPolarizationData Q)
  [FiniteDimensional K V] (hline : P.line = ⊥) :
  ↥(CliffordAlgebra.even Q) ≃ₐ[K]
    Module.End K ↥(TauCeti.spinPlus Q P) × Module.End K ↥(TauCeti.spinMinus Q P)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.evenCliffordEquivProdEnd`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Structure.html#TauCeti.SpinPolarizationData.evenCliffordEquivProdEnd).

## Sources

- [Tau Ceti documentation: `TauCeti.SpinPolarizationData.evenCliffordEquivProdEnd`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Structure.html#TauCeti.SpinPolarizationData.evenCliffordEquivProdEnd)
- [Source of `TauCeti.SpinPolarizationData.evenCliffordEquivProdEnd` in TauCeti/RepresentationTheory/Spin/Structure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Spin/Structure.lean#L372)
