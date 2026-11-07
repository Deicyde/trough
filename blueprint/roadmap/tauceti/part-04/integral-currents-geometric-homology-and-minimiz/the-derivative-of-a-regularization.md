---
declaration: theorem
origin: cited
lean: Distribution.fderiv_translatePairing_apply
statement: formalized
proof: formalized
---

# The derivative of a regularization

At every admissible translation, the derivative of
`x ↦ T (ρ (· - x))` in the direction `v` is the regularization of the distributional derivative
`∂_{v} T`.

```lean
Distribution.fderiv_translatePairing_apply.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {Ω V : TopologicalSpace.Opens E} [FiniteDimensional ℝ E] (T : Distribution Ω F ⊤)
  (ρ : TestFunction V ℝ ⊤) {x : E} (hx : Set.MapsTo (fun x_1 => x_1 + x) (tsupport ⇑ρ) ↑Ω) (v : E) :
  (fderiv ℝ (T.translatePairing ρ) x) v = (LineDeriv.lineDerivOp v T).translatePairing ρ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A distribution has finite order on each compact set](a-distribution-has-finite-order-on-each-compact.md)

## Lean

Formalized in Tau Ceti as [`Distribution.fderiv_translatePairing_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Regularization.html#Distribution.fderiv_translatePairing_apply).

## Sources

- [Tau Ceti documentation: `Distribution.fderiv_translatePairing_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Regularization.html#Distribution.fderiv_translatePairing_apply)
- [Source of `Distribution.fderiv_translatePairing_apply` in TauCeti/Analysis/Distribution/Regularization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Distribution/Regularization.lean#L242)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricCurrents/STATUS.md)
