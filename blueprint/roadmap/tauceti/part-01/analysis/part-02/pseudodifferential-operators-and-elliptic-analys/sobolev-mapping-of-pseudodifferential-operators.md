---
declaration: theorem
origin: cited
lean: TauCeti.Symbol.exists_quantizeSobolev
statement: formalized
proof: formalized
---

# Sobolev mapping of pseudodifferential operators with compact spatial support

For a
symbol `a` of order `m` with compact spatial support between finite-dimensional complex normed
spaces and every real `s`, the quantization `Op(a)` extends from Schwartz functions to a bounded
operator `H^s(ℝⁿ; V) → H^{s - m}(ℝⁿ; W)`.

The norms of `V` and `W` need not come from inner products: isomorphisms `e₁ : V ≃L[ℂ] ℂ^k`,
`e₂ : W ≃L[ℂ] ℂ^l` induce isomorphisms of the Bessel-potential spaces
(`BesselPotentialSpace.postcomp`), and the operator is `e₂⁻¹ ∘ Op(e₂ a e₁⁻¹) ∘ e₁` with the
Hilbert-space operator `TauCeti.Symbol.quantizeSobolev`
(`TauCeti.Symbol.toDistr_postcomp_comp_comp_postcomp_toBesselPotentialSpaceCLM_apply`).

```lean
TauCeti.Symbol.exists_quantizeSobolev.{u_1, u_2} {n : ℕ} {m : ℝ} {V : Type u_1} {W : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [CompleteSpace V] [FiniteDimensional ℂ V]
  [NormedAddCommGroup W] [NormedSpace ℂ W] [CompleteSpace W] [FiniteDimensional ℂ W]
  (a : TauCeti.Symbol n V W m) (ha : a.HasCompactSpatialSupport) (s : ℝ) :
  ∃ T,
    ∀ (u : SchwartzMap (TauCeti.CoordinateSpace n) V)
      (φ : SchwartzMap (TauCeti.CoordinateSpace n) ℂ),
      ↑(T ((SchwartzMap.toBesselPotentialSpaceCLM s 2) u)) φ =
        ∫ (x : TauCeti.CoordinateSpace n), φ x • TauCeti.quantizeSchwartzValue a.coefficient u x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Sobolev estimate on Schwartz functions](the-sobolev-estimate-on-schwartz-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.exists_quantizeSobolev`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Sobolev.html#TauCeti.Symbol.exists_quantizeSobolev).

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.exists_quantizeSobolev`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Sobolev.html#TauCeti.Symbol.exists_quantizeSobolev)
- [Source of `TauCeti.Symbol.exists_quantizeSobolev` in TauCeti/Analysis/Pseudodifferential/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Pseudodifferential/Sobolev.lean#L940)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
