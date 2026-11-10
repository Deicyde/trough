---
declaration: theorem
origin: cited
lean: ContinuousLinearEquiv.integral_divergence_affineFluxPullback
statement: formalized
proof: formalized
---

# The divergence theorem on an affine parallelepiped

Let `A u = p + L u` and let `F` be a
flux field continuous on the parallelepiped `A '' [0, 1]ⁿ⁺¹`, differentiable with derivatives
`F' i` at `A u` for every interior point `u` of the unit cube off a countable set, and with
`u ↦ div F (A u)` integrable on the unit cube. Then `det L` times the integral of `div F ∘ A` over
the unit cube is the boundary sum of the cofactor pullback `H = L.affineFluxPullback p F`: the sum
over `j` of the integral of `H j` over the front face `u j = 1` minus that over the back face
`u j = 0`. The determinant is signed.

```lean
ContinuousLinearEquiv.integral_divergence_affineFluxPullback.{u_2} {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {n : ℕ} (L : (Fin (n + 1) → ℝ) ≃L[ℝ] Fin (n + 1) → ℝ)
  (p : Fin (n + 1) → ℝ) (F : Fin (n + 1) → (Fin (n + 1) → ℝ) → E)
  (F' : Fin (n + 1) → (Fin (n + 1) → ℝ) → (Fin (n + 1) → ℝ) →L[ℝ] E) (s : Set (Fin (n + 1) → ℝ))
  (hs : s.Countable)
  (Hc : ∀ (i : Fin (n + 1)), ContinuousOn (F i) ((fun u => p + L u) '' Set.Icc 0 1))
  (Hd :
    ∀ u ∈ (Set.univ.pi fun x => Set.Ioo 0 1) \ s,
      ∀ (i : Fin (n + 1)), HasFDerivAt (F i) (F' i (p + L u)) (p + L u))
  (Hi :
    MeasureTheory.IntegrableOn (fun u => ∑ i, (F' i (p + L u)) (Pi.single i 1)) (Set.Icc 0 1)
      MeasureTheory.volume) :
  LinearMap.det ↑↑L •
      ∫ (u : Fin (n + 1) → ℝ) in Set.Icc 0 1, ∑ i, (F' i (p + L u)) (Pi.single i 1) =
    ∑ j,
      ((∫ (x : Fin n → ℝ) in Set.Icc 0 1, L.affineFluxPullback p F j (j.insertNth 1 x)) -
        ∫ (x : Fin n → ℝ) in Set.Icc 0 1, L.affineFluxPullback p F j (j.insertNth 0 x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearEquiv.integral_divergence_affineFluxPullback`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem/Affine.html#ContinuousLinearEquiv.integral_divergence_affineFluxPullback).

## Sources

- [Tau Ceti documentation: `ContinuousLinearEquiv.integral_divergence_affineFluxPullback`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem/Affine.html#ContinuousLinearEquiv.integral_divergence_affineFluxPullback)
- [Source of `ContinuousLinearEquiv.integral_divergence_affineFluxPullback` in TauCeti/MeasureTheory/Integral/DivergenceTheorem/Affine.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/DivergenceTheorem/Affine.lean#L123)
