---
declaration: def
origin: cited
lean: TauCeti.SpinPolarizationData.cliffordEquivMatrix
statement: formalized
---

# The structure theorem

the Clifford algebra of a polarized quadratic space of dimension
`2 * l` is the matrix algebra `M_{2^l}(K)`, read in a basis of the spinor module `⋀·W`, which has
dimension `2 ^ l`.

```lean
TauCeti.SpinPolarizationData.cliffordEquivMatrix.{u, v} {K : Type u} [Field K] {V : Type v}
  [AddCommGroup V] [_root_.Module K V] {Q : QuadraticForm K V} (P : TauCeti.SpinPolarizationData Q)
  [Invertible 2] [FiniteDimensional K V] {l : ℕ} (hV : Module.finrank K V = 2 * l) :
  CliffordAlgebra Q ≃ₐ[K] Matrix (Fin (2 ^ l)) (Fin (2 ^ l)) K
```

## Depends on

- [The structure theorem in operator form](the-structure-theorem-in-operator-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.cliffordEquivMatrix`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Structure.html#TauCeti.SpinPolarizationData.cliffordEquivMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.SpinPolarizationData.cliffordEquivMatrix`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Structure.html#TauCeti.SpinPolarizationData.cliffordEquivMatrix)
- [Source of `TauCeti.SpinPolarizationData.cliffordEquivMatrix` in TauCeti/RepresentationTheory/Spin/Structure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Spin/Structure.lean#L191)
