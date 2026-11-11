---
declaration: theorem
origin: cited
lean: TauCeti.eventually_exists_hasFDerivAt_iff_eventually_isFrobeniusIntegrableAt
statement: formalized
proof: formalized
---

# The Frobenius theorem for total differential equations

Let `E` and `F` be
finite-dimensional real normed spaces and let `f : E × F → (E →L[ℝ] F)` be `C^(n+1)` near `p₀`,
for instance `C¹`. The total differential equation `D u x = f (x, u x)` has a local solution
through every point near `p₀` if and only if `f` satisfies the Frobenius integrability condition
near `p₀`.

```lean
TauCeti.eventually_exists_hasFDerivAt_iff_eventually_isFrobeniusIntegrableAt.{u} {E F : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ E] [FiniteDimensional ℝ F] {n : ℕ∞} {f : E × F → E →L[ℝ] F} {s : Set (E × F)}
  {p₀ : E × F} (hf : ContDiffOn ℝ (↑n + 1) f s) (hs : s ∈ nhds p₀) :
  (∀ᶠ (p : E × F) in nhds p₀,
      ∃ u, u p.1 = p.2 ∧ ∀ᶠ (x : E) in nhds p.1, HasFDerivAt u (f (x, u x)) x) ↔
    ∀ᶠ (p : E × F) in nhds p₀, TauCeti.IsFrobeniusIntegrableAt f p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The local Frobenius theorem (`TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt`)](the-local-frobenius-theorem-tauceti-exists-event.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eventually_exists_hasFDerivAt_iff_eventually_isFrobeniusIntegrableAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Frobenius.html#TauCeti.eventually_exists_hasFDerivAt_iff_eventually_isFrobeniusIntegrableAt).

## Sources

- [Tau Ceti documentation: `TauCeti.eventually_exists_hasFDerivAt_iff_eventually_isFrobeniusIntegrableAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Frobenius.html#TauCeti.eventually_exists_hasFDerivAt_iff_eventually_isFrobeniusIntegrableAt)
- [Source of `TauCeti.eventually_exists_hasFDerivAt_iff_eventually_isFrobeniusIntegrableAt` in TauCeti/Analysis/ODE/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/ODE/Frobenius.lean#L892)
