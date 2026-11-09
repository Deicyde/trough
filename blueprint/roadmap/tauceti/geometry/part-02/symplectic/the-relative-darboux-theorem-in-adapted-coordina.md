---
declaration: theorem
origin: cited
lean: TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq
statement: formalized
proof: formalized
---

# The relative Darboux theorem in adapted coordinates

Let `ω₀`, `ω₁` be closed `C^r`
two-forms (`r ≥ 1`) on an open subset `W` of `E × N` containing `(q₀, 0)`, both nondegenerate at
`(q₀, 0)`, with the same pullback to the zero section `E × {0}`. Then some `C^r` diffeomorphism `ψ`
of `E × N` fixes every point `(q, 0)` with `q` near `q₀` and pulls `ω₁` back to `ω₀` near `(q₀, 0)`.
The pullback to the zero section may be degenerate, of any rank.

```lean
TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq.{u_1, u_2}
  {E : Type u_1} {N : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup N] [NormedSpace ℝ N] [FiniteDimensional ℝ N]
  {ω₀ ω₁ : E × N → (E × N) [⋀^Fin 2]→L[ℝ] ℝ} {W : Set (E × N)} {q₀ : E} {r : ℕ∞} (hr : 1 ≤ r)
  (hW : IsOpen W) (hq₀ : (q₀, 0) ∈ W) (hω₀ : ContDiffOn ℝ (↑r) ω₀ W) (hω₁ : ContDiffOn ℝ (↑r) ω₁ W)
  (hdω₀ : ∀ x ∈ W, extDeriv ω₀ x = 0) (hdω₁ : ∀ x ∈ W, extDeriv ω₁ x = 0)
  (htan :
    ∀ (q : E),
      (q, 0) ∈ W →
        (ω₁ (q, 0)).compContinuousLinearMap (ContinuousLinearMap.inl ℝ E N) =
          (ω₀ (q, 0)).compContinuousLinearMap (ContinuousLinearMap.inl ℝ E N))
  (hnd₀ : ∀ (v : E × N), (∀ (w : E × N), (ω₀ (q₀, 0)) ![v, w] = 0) → v = 0)
  (hnd₁ : ∀ (v : E × N), (∀ (w : E × N), (ω₁ (q₀, 0)) ![v, w] = 0) → v = 0) :
  ∃ ψ,
    (∀ᶠ (q : E) in nhds q₀, ψ (q, 0) = (q, 0)) ∧
      ∀ᶠ (x : E × N) in nhds (q₀, 0), (ω₁ (ψ x)).compContinuousLinearMap (fderiv ℝ (⇑ψ) x) = ω₀ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Moser's lemma, local form](../../../analysis/part-01/analytic-heegaard-floer-homology/mosers-lemma-local-form.md)
- [The relative Poincaré lemma](../../../analysis/part-02/calculus/part-01/the-relative-poincare-lemma.md)
- [Witt's extension theorem](witts-extension-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Relative.html#TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Relative.html#TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq)
- [Source of `TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq` in TauCeti/Geometry/Symplectic/Darboux/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Darboux/Relative.lean#L129)
