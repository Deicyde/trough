---
declaration: theorem
origin: cited
lean: TauCeti.IsInvolutiveDistribution.exists_eventually_hasFDerivAt, TauCeti.isInvolutiveDistribution_graphDistribution_iff_forall_exists, TauCeti.IsInvolutiveDistribution.exists_eventually_eq_graph_fderiv
statement: formalized
proof: formalized
---

# The Frobenius theorem in coordinates

Let `f` be of class `C^(n+1)` near `(x₀, y₀)`, with
an involutive graph distribution. Then the distribution has an integral manifold through
`(x₀, y₀)`: the graph of a function `u`, of class `C^(n+1)` at `x₀`, with `u x₀ = y₀` and
`D u x = f (x, u x)` near `x₀`, so that the tangent space of the graph at `(x, u x)` is the graph
of `f (x, u x)`.

```lean
TauCeti.IsInvolutiveDistribution.exists_eventually_hasFDerivAt.{u} {E F : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {n : ℕ∞} {f : E × F → E →L[ℝ] F} {s : Set (E × F)}
  {x₀ : E} {y₀ : F}
  (hD :
    TauCeti.IsInvolutiveDistribution (modelWithCornersSelf ℝ (E × F)) (TauCeti.graphDistribution f))
  (hf : ContDiffOn ℝ (↑n + 1) f s) (hs : s ∈ nhds (x₀, y₀)) :
  ∃ u, u x₀ = y₀ ∧ ContDiffAt ℝ (↑n + 1) u x₀ ∧ ∀ᶠ (x : E) in nhds x₀, HasFDerivAt u (f (x, u x)) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Frobenius theorem for total differential equations](../../../../analysis/part-03/ode/the-frobenius-theorem-for-total-differential-equ.md)
- [The local Frobenius theorem (`TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt`)](../../../../analysis/part-03/ode/the-local-frobenius-theorem-tauceti-exists-event.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsInvolutiveDistribution.exists_eventually_hasFDerivAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/Graph.html#TauCeti.IsInvolutiveDistribution.exists_eventually_hasFDerivAt).

## Other forms

**The Frobenius theorem for graph distributions.** Formalized in Tau Ceti as [`TauCeti.isInvolutiveDistribution_graphDistribution_iff_forall_exists`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/Graph.html#TauCeti.isInvolutiveDistribution_graphDistribution_iff_forall_exists).

```lean
TauCeti.isInvolutiveDistribution_graphDistribution_iff_forall_exists.{u} {E F : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : E × F → E →L[ℝ] F} (hf : ContDiff ℝ 1 f) :
  TauCeti.IsInvolutiveDistribution (modelWithCornersSelf ℝ (E × F)) (TauCeti.graphDistribution f) ↔
    ∀ (p : E × F), ∃ u, u p.1 = p.2 ∧ ∀ᶠ (x : E) in nhds p.1, HasFDerivAt u (f (x, u x)) x
```

**The Frobenius theorem for transverse distributions.** Formalized in Tau Ceti as [`TauCeti.IsInvolutiveDistribution.exists_eventually_eq_graph_fderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/Transverse.html#TauCeti.IsInvolutiveDistribution.exists_eventually_eq_graph_fderiv).

```lean
TauCeti.IsInvolutiveDistribution.exists_eventually_eq_graph_fderiv.{u} {E F : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {n : ℕ∞} {D : E × F → Submodule ℝ (E × F)}
  (hinv : TauCeti.IsInvolutiveDistribution (modelWithCornersSelf ℝ (E × F)) D)
  (hD :
    TauCeti.IsContMDiffDistribution (modelWithCornersSelf ℝ (E × F)) (↑n + 1) (Module.finrank ℝ E)
      D)
  {x₀ : E} {y₀ : F} (h₀ : Disjoint (D (x₀, y₀)) (LinearMap.fst ℝ E F).ker) :
  ∃ u,
    u x₀ = y₀ ∧
      ContDiffAt ℝ (↑n + 1) u x₀ ∧
        ∀ᶠ (x : E) in nhds x₀, DifferentiableAt ℝ u x ∧ D (x, u x) = (↑(fderiv ℝ u x)).graph
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsInvolutiveDistribution.exists_eventually_hasFDerivAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/Graph.html#TauCeti.IsInvolutiveDistribution.exists_eventually_hasFDerivAt)
- [Source of `TauCeti.IsInvolutiveDistribution.exists_eventually_hasFDerivAt` in TauCeti/Geometry/Manifold/Distribution/Graph.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Distribution/Graph.lean#L239)
