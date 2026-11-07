---
declaration: theorem
origin: cited
lean: CliffordAlgebra.scalarTrace_reverse_mul_self_nonneg
statement: formalized
proof: formalized
---

# Positivity of the trace pairing

if `Q` is nonnegative on an orthogonal basis, then
`τ (reverse x * x) ≥ 0` for every `x`.

```lean
CliffordAlgebra.scalarTrace_reverse_mul_self_nonneg.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2}
  [CommRing R] [AddCommGroup M] [_root_.Module R M] [Invertible 2] {Q : QuadraticForm R M}
  {I : Type u_3} [LinearOrder I] {b : Module.Basis I R M} [LinearOrder R] [IsOrderedRing R]
  (hb : LinearMap.IsOrthoᵢ (QuadraticMap.associated Q) ⇑b) (hQ : ∀ (i : I), 0 ≤ Q (b i))
  (x : CliffordAlgebra Q) : 0 ≤ (CliffordAlgebra.scalarTrace Q) (CliffordAlgebra.reverse x * x)
```

## Depends on

- [CliffordAlgebra.scalarTrace](cliffordalgebra-scalartrace.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.scalarTrace_reverse_mul_self_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/OrthogonalBasis.html#CliffordAlgebra.scalarTrace_reverse_mul_self_nonneg).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.scalarTrace_reverse_mul_self_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/OrthogonalBasis.html#CliffordAlgebra.scalarTrace_reverse_mul_self_nonneg)
- [Source of `CliffordAlgebra.scalarTrace_reverse_mul_self_nonneg` in TauCeti/LinearAlgebra/CliffordAlgebra/OrthogonalBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/OrthogonalBasis.lean#L529)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
