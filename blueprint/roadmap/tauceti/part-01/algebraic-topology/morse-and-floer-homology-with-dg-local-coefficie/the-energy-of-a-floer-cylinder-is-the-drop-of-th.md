---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_eq_contractibleLoopAction_sub
statement: formalized
proof: formalized
---

# The energy of a Floer cylinder is the drop of the contractible action

Let `ω` be a
nondegenerate weakly exact two-form on a finite-dimensional manifold, `H` a `C¹` time-dependent
Hamiltonian, and `u` a `C²` map, `1`-periodic in its second coordinate. If the loop
`γ_b = u(b, ·)` bounds a cap, the Floer energy of `u` over `[a, b] × [0, 1]` for the cylindrical
perturbation `K = H_t dt` is `A_H(γ_a) - A_H(γ_b)`, where `γ_a = u(a, ·)` and `A_H` is the action
`TauCeti.contractibleLoopAction` of contractible loops. The loop `γ_a` is capped by gluing `u` to
the cap of `γ_b`, so both actions are computed with genuine caps.

```lean
TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_eq_contractibleLoopAction_sub.{u_1,
    u_2, u_3}
  {E : Type u_1} {HM : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace HM] {I : ModelWithCorners ℝ E HM} [TopologicalSpace M] [ChartedSpace HM M]
  [IsManifold I (↑⊤) M] {ω : TauCeti.SmoothTwoForm I M} {H : ℝ → M → ℝ} {u : ℝ × ℝ → M}
  [FiniteDimensional ℝ E] (hω : ω.IsNondegenerate) (hωe : TauCeti.IsWeaklyExact ↑ω)
  (hH :
    ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (modelWithCornersSelf ℝ ℝ) 1 (Function.uncurry H))
  (hu : ContMDiff (modelWithCornersSelf ℝ (ℝ × ℝ)) I 2 u)
  (hper : ∀ (z : ℝ × ℝ), u (z.1, z.2 + 1) = u z) {a b : ℝ} (hab : a ≤ b) {v : ℝ × ℝ → M}
  (hv : TauCeti.IsCap I v fun t => u (b, t)) :
  ∫ (z : ℝ × ℝ) in Set.Icc a b ×ˢ Set.Icc 0 1,
      ω.floerEnergyDensity (fun x x_1 => 0) (fun w => H w.2) u z =
    (TauCeti.contractibleLoopAction (↑ω) H fun t => u (a, t)) -
      TauCeti.contractibleLoopAction (↑ω) H fun t => u (b, t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The energy identity on a rectangle, for a manifold target](../../geometry/part-01/hamiltonian-floer-operations-geometric-product-a/the-energy-identity-on-a-rectangle-for-a-manifol.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_eq_contractibleLoopAction_sub`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/CylinderAction.html#TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_eq_contractibleLoopAction_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_eq_contractibleLoopAction_sub`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/CylinderAction.html#TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_eq_contractibleLoopAction_sub)
- [Source of `TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_eq_contractibleLoopAction_sub` in TauCeti/Geometry/Symplectic/Floer/CylinderAction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Floer/CylinderAction.lean#L470)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)
