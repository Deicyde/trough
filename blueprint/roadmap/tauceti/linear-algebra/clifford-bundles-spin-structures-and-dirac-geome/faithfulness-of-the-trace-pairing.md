---
declaration: theorem
origin: cited
lean: CliffordAlgebra.scalarTrace_reverse_mul_self_eq_zero_iff
statement: formalized
proof: formalized
---

# Faithfulness of the trace pairing

if `Q` is positive on an orthogonal basis, then
`τ (reverse x * x) = 0` only for `x = 0`.

```lean
CliffordAlgebra.scalarTrace_reverse_mul_self_eq_zero_iff.{u_1, u_2, u_3} {R : Type u_1}
  {M : Type u_2} [CommRing R] [AddCommGroup M] [_root_.Module R M] [Invertible 2]
  {Q : QuadraticForm R M} {I : Type u_3} [LinearOrder I] {b : Module.Basis I R M} [LinearOrder R]
  [IsStrictOrderedRing R] (hb : LinearMap.IsOrthoᵢ (QuadraticMap.associated Q) ⇑b)
  (hQ : ∀ (i : I), 0 < Q (b i)) {x : CliffordAlgebra Q} :
  (CliffordAlgebra.scalarTrace Q) (CliffordAlgebra.reverse x * x) = 0 ↔ x = 0
```

## Depends on

- [CliffordAlgebra.scalarTrace](cliffordalgebra-scalartrace.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.scalarTrace_reverse_mul_self_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/OrthogonalBasis.html#CliffordAlgebra.scalarTrace_reverse_mul_self_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.scalarTrace_reverse_mul_self_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/OrthogonalBasis.html#CliffordAlgebra.scalarTrace_reverse_mul_self_eq_zero_iff)
- [Source of `CliffordAlgebra.scalarTrace_reverse_mul_self_eq_zero_iff` in TauCeti/LinearAlgebra/CliffordAlgebra/OrthogonalBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/OrthogonalBasis.lean#L556)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
