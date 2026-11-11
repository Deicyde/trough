---
declaration: theorem
origin: cited
lean: TauCeti.exists_partialDiffeomorph_fix_immersion_compContinuousLinearMap_fderiv_eq, TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq
statement: formalized
proof: formalized
---

# The relative Darboux theorem along an immersion

Let `g : E' → E` be of class `C^(r + 1)`
near `y₀` with injective derivative at `y₀`, and let `ω₀`, `ω₁` be closed `C^r` two-forms (`r ≥ 1`)
on an open set `W ∋ g y₀`, both nondegenerate at `g y₀`, whose pullbacks along `g` agree near `y₀`.
Then some `C^r` partial diffeomorphism `Φ` of `E` with `g y₀` in its source fixes `g y` for every
`y` near `y₀` and pulls `ω₁` back to `ω₀` on its source. The pullbacks along `g` may be degenerate,
of any rank.

```lean
TauCeti.exists_partialDiffeomorph_fix_immersion_compContinuousLinearMap_fderiv_eq.{u_1, u_2}
  {E : Type u_1} {E' : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup E'] [NormedSpace ℝ E'] [FiniteDimensional ℝ E']
  {ω₀ ω₁ : E → E [⋀^Fin 2]→L[ℝ] ℝ} {W : Set E} {g : E' → E} {y₀ : E'} {r : ℕ∞} (hr : 1 ≤ r)
  (hW : IsOpen W) (hy₀ : g y₀ ∈ W) (hω₀ : ContDiffOn ℝ (↑r) ω₀ W) (hω₁ : ContDiffOn ℝ (↑r) ω₁ W)
  (hdω₀ : ∀ x ∈ W, extDeriv ω₀ x = 0) (hdω₁ : ∀ x ∈ W, extDeriv ω₁ x = 0)
  (hg : ∀ᶠ (y : E') in nhds y₀, ContDiffAt ℝ (↑r + 1) g y)
  (hinj : Function.Injective ⇑(fderiv ℝ g y₀))
  (htan :
    ∀ᶠ (y : E') in nhds y₀,
      (ω₁ (g y)).compContinuousLinearMap (fderiv ℝ g y) =
        (ω₀ (g y)).compContinuousLinearMap (fderiv ℝ g y))
  (hnd₀ : ∀ (v : E), (∀ (w : E), (ω₀ (g y₀)) ![v, w] = 0) → v = 0)
  (hnd₁ : ∀ (v : E), (∀ (w : E), (ω₁ (g y₀)) ![v, w] = 0) → v = 0) :
  ∃ Φ,
    g y₀ ∈ Φ.source ∧
      (∀ᶠ (y : E') in nhds y₀, ↑Φ.toPartialEquiv (g y) = g y) ∧
        ∀ x ∈ Φ.source,
          (ω₁ (↑Φ.toPartialEquiv x)).compContinuousLinearMap (fderiv ℝ (↑Φ.toPartialEquiv) x) = ω₀ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem, with a `C^n` inverse on the whole target](../../../analysis/part-02/calculus/part-01/the-inverse-function-theorem-with-a-c-n-inverse.md)
- [Moser's lemma, local form](mosers-lemma-local-form.md)
- [The relative Poincaré lemma](../../../analysis/part-02/calculus/part-02/the-relative-poincare-lemma.md)
- [Witt's extension theorem](witts-extension-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_partialDiffeomorph_fix_immersion_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Immersion.html#TauCeti.exists_partialDiffeomorph_fix_immersion_compContinuousLinearMap_fderiv_eq).

## Other forms

**The relative Darboux theorem in adapted coordinates.** Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Relative.html#TauCeti.exists_diffeomorph_fix_zeroSection_eventually_compContinuousLinearMap_fderiv_eq).

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

## Sources

- [Tau Ceti documentation: `TauCeti.exists_partialDiffeomorph_fix_immersion_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Immersion.html#TauCeti.exists_partialDiffeomorph_fix_immersion_compContinuousLinearMap_fderiv_eq)
- [Source of `TauCeti.exists_partialDiffeomorph_fix_immersion_compContinuousLinearMap_fderiv_eq` in TauCeti/Geometry/Symplectic/Darboux/Immersion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Darboux/Immersion.lean#L142)
