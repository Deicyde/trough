---
declaration: theorem
origin: cited
lean: CliffordAlgebra.scalarTrace_conjStar_mul_self_nonneg
statement: formalized
proof: formalized
---

# Positivity of the negative-metric trace norm

**Positivity of the negative-metric trace norm** on the complexified Clifford algebra of a
negative semidefinite real quadratic form.

```lean
CliffordAlgebra.scalarTrace_conjStar_mul_self_nonneg.{u_1} {V : Type u_1} [AddCommGroup V]
  [_root_.Module ℝ V] {Q : QuadraticForm ℝ V} [FiniteDimensional ℝ V] (hQ : ∀ (v : V), Q v ≤ 0)
  (x : CliffordAlgebra (QuadraticForm.baseChange ℂ Q)) :
  0 ≤
    (CliffordAlgebra.scalarTrace (QuadraticForm.baseChange ℂ Q))
      ((CliffordAlgebra.conjStar Q) x * x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.scalarTrace_conjStar_mul_self_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Positivity.html#CliffordAlgebra.scalarTrace_conjStar_mul_self_nonneg).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.scalarTrace_conjStar_mul_self_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Positivity.html#CliffordAlgebra.scalarTrace_conjStar_mul_self_nonneg)
- [Source of `CliffordAlgebra.scalarTrace_conjStar_mul_self_nonneg` in TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Positivity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Positivity.lean#L297)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpinGeometry/STATUS.md)
