---
declaration: theorem
origin: cited
lean: Distribution.translatePairing_eq_of_lineDerivOp_eq_zero
statement: formalized
proof: formalized
---

# Distributions with vanishing derivatives have locally constant regularizations

If every
directional derivative of `T` vanishes, then `x ↦ T (ρ (· - x))` is constant on every
preconnected open set of translations for which `ρ (· - x)` is supported in `Ω`.

```lean
Distribution.translatePairing_eq_of_lineDerivOp_eq_zero.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {Ω V : TopologicalSpace.Opens E} {T : Distribution Ω F ⊤}
  (hT : ∀ (v : E), LineDeriv.lineDerivOp v T = 0) (ρ : TestFunction V ℝ ⊤) {U : Set E}
  (hUo : IsOpen U) (hUc : IsPreconnected U)
  (hU : ∀ x ∈ U, Set.MapsTo (fun x_1 => x_1 + x) (tsupport ⇑ρ) ↑Ω) {x y : E} (hx : x ∈ U)
  (hy : y ∈ U) : T.translatePairing ρ x = T.translatePairing ρ y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A distribution has finite order on each compact set](a-distribution-has-finite-order-on-each-compact.md)
- [The derivative of a regularization](the-derivative-of-a-regularization.md)
- [Uniform first-order Taylor estimate in a parameter](../../part-02/calculus/part-02/uniform-first-order-taylor-estimate-in-a-paramet.md)

## Lean

Formalized in Tau Ceti as [`Distribution.translatePairing_eq_of_lineDerivOp_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Regularization.html#Distribution.translatePairing_eq_of_lineDerivOp_eq_zero).

## Sources

- [Tau Ceti documentation: `Distribution.translatePairing_eq_of_lineDerivOp_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Regularization.html#Distribution.translatePairing_eq_of_lineDerivOp_eq_zero)
- [Source of `Distribution.translatePairing_eq_of_lineDerivOp_eq_zero` in TauCeti/Analysis/Distribution/Regularization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/Regularization.lean#L275)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricCurrents/STATUS.md)
