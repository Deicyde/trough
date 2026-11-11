---
declaration: def
origin: cited
lean: TauCeti.SpinPolarizationData.cliffordEquivEnd
statement: formalized
---

# The structure theorem in operator form

for an even-dimensional polarized quadratic space,
the Fock action is an isomorphism of `K`-algebras from `CliffordAlgebra Q` onto the endomorphism
algebra of the spinor module `S = ⋀·W`.

```lean
TauCeti.SpinPolarizationData.cliffordEquivEnd.{u, v} {K : Type u} [Field K] {V : Type v}
  [AddCommGroup V] [_root_.Module K V] {Q : QuadraticForm K V} (P : TauCeti.SpinPolarizationData Q)
  [FiniteDimensional K V] (h : Even (Module.finrank K V)) :
  CliffordAlgebra Q ≃ₐ[K] Module.End K (ExteriorAlgebra K ↥P.W)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.cliffordEquivEnd`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Structure.html#TauCeti.SpinPolarizationData.cliffordEquivEnd).

## Sources

- [Tau Ceti documentation: `TauCeti.SpinPolarizationData.cliffordEquivEnd`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Structure.html#TauCeti.SpinPolarizationData.cliffordEquivEnd)
- [Source of `TauCeti.SpinPolarizationData.cliffordEquivEnd` in TauCeti/RepresentationTheory/Spin/Structure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Spin/Structure.lean#L175)
