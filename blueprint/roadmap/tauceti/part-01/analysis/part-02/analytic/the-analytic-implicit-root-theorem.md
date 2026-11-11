---
declaration: theorem
origin: cited
lean: AnalyticAt.exists_analyticAt_eventually_eq_zero_iff
statement: formalized
proof: formalized
---

# The analytic implicit root theorem

Let `f (w, z)` be analytic at `u = (w₀, z₀)`, with
`f u = 0` and `∂f/∂z ≠ 0` at `u`. Then there is a function `g`, analytic at `w₀` with
`g w₀ = z₀`, such that near `u` the zeros of `f` are exactly the points `(w, g w)`; in particular
`f (w, g w) = 0` for all `w` near `w₀`.

```lean
AnalyticAt.exists_analyticAt_eventually_eq_zero_iff.{u_1, u_2} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] [CompleteSpace 𝕜] {f : E × 𝕜 → 𝕜} {u : E × 𝕜} (hf : AnalyticAt 𝕜 f u)
  (hu : f u = 0) (h : deriv (fun z => f (u.1, z)) u.2 ≠ 0) :
  ∃ g,
    AnalyticAt 𝕜 g u.1 ∧
      g u.1 = u.2 ∧
        (∀ᶠ (w : E) in nhds u.1, f (w, g w) = 0) ∧ ∀ᶠ (v : E × 𝕜) in nhds u, f v = 0 ↔ g v.1 = v.2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic implicit function theorem](the-analytic-implicit-function-theorem.md)

## Lean

Formalized in Tau Ceti as [`AnalyticAt.exists_analyticAt_eventually_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Inverse.html#AnalyticAt.exists_analyticAt_eventually_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `AnalyticAt.exists_analyticAt_eventually_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Inverse.html#AnalyticAt.exists_analyticAt_eventually_eq_zero_iff)
- [Source of `AnalyticAt.exists_analyticAt_eventually_eq_zero_iff` in TauCeti/Analysis/Analytic/Inverse.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Analytic/Inverse.lean#L160)
