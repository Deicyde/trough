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
  {Ω V : TopologicalSpace.Opens E} (T : Distribution Ω F ⊤) (ρ : TestFunction V ℝ ⊤) {x : E}
  (hx : Set.MapsTo (fun x_1 => x_1 + x) (tsupport ⇑ρ) ↑Ω) (v : E) :
  (fderiv ℝ (T.translatePairing ρ) x) v = (LineDeriv.lineDerivOp v T).translatePairing ρ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A distribution has finite order on each compact set](a-distribution-has-finite-order-on-each-compact.md)
- [Uniform first-order Taylor estimate in a parameter](../../part-02/calculus/part-02/uniform-first-order-taylor-estimate-in-a-paramet.md)

## Lean

Formalized in Tau Ceti as [`Distribution.fderiv_translatePairing_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Regularization.html#Distribution.fderiv_translatePairing_apply).

## Sources

- [Tau Ceti documentation: `Distribution.fderiv_translatePairing_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Regularization.html#Distribution.fderiv_translatePairing_apply)
- [Source of `Distribution.fderiv_translatePairing_apply` in TauCeti/Analysis/Distribution/Regularization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/Regularization.lean#L244)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricCurrents/STATUS.md)
