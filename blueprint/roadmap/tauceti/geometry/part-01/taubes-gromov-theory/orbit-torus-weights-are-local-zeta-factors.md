---
declaration: theorem
origin: cited
lean: TauCeti.X_mul_derivative_torusWeightSeries_of_det_eq_one
statement: formalized
proof: formalized
---

# Orbit-torus weights are local zeta factors

Let `P` be a `2 × 2` matrix of determinant
one all of whose iterates are nondegenerate, `det (1 - P ^ k) ≠ 0` for `k ≥ 1`. Read off the label
`σ = (0 < det (1 - P))` and `i = 1` if `det (1 + P) < 0`, `i = 0` otherwise. Then the local series
`f = f_(σ, i)` satisfies `t f' = f ∑_{k ≥ 1} sgn det (1 - P ^ k) t ^ k`; over `ℚ` this says
`log f = ∑_{k ≥ 1} sgn det (1 - P ^ k) t ^ k / k`.

```lean
TauCeti.X_mul_derivative_torusWeightSeries_of_det_eq_one.{u_1} {R : Type u_1} [CommRing R]
  [LinearOrder R] [IsStrictOrderedRing R] {P : Matrix (Fin 2) (Fin 2) R} (hdet : P.det = 1)
  (hP : ∀ (k : ℕ), k ≠ 0 → (1 - P ^ k).det ≠ 0) :
  PowerSeries.X *
      PowerSeries.derivative
        (TauCeti.torusWeightSeries (decide (0 < (1 - P).det)) (if (1 + P).det < 0 then 1 else 0)) =
    TauCeti.torusWeightSeries (decide (0 < (1 - P).det)) (if (1 + P).det < 0 then 1 else 0) *
      PowerSeries.mk fun k => if k = 0 then 0 else ↑(SignType.sign (1 - P ^ k).det)
```

## Depends on

- [TauCeti.torusWeightSeries](tauceti-torusweightseries.md)

## Proof depends on

- [Cayley–Hamilton in size two](../../../linear-algebra/matrix/cayley-hamilton-in-size-two.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.X_mul_derivative_torusWeightSeries_of_det_eq_one`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/Weight.html#TauCeti.X_mul_derivative_torusWeightSeries_of_det_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.X_mul_derivative_torusWeightSeries_of_det_eq_one`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/Weight.html#TauCeti.X_mul_derivative_torusWeightSeries_of_det_eq_one)
- [Source of `TauCeti.X_mul_derivative_torusWeightSeries_of_det_eq_one` in TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/Weight.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/Weight.lean#L151)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
