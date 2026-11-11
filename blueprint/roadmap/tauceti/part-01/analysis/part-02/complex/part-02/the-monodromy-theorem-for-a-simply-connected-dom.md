---
declaration: theorem
origin: cited
lean: TauCeti.ContinuesInside.exists_analyticOnNhd
statement: formalized
proof: formalized
---

# The monodromy theorem for a simply connected domain

A germ that continues along every
path of a simply connected open set `U` issuing from `z₀` is the germ at `z₀` of a single function
analytic on all of `U`.

So on a simply connected domain analytic continuation produces no new branches, and a
"multi-valued analytic function" there is single-valued after all.

```lean
TauCeti.ContinuesInside.exists_analyticOnNhd.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] {U : Set ℂ} {z₀ : ℂ} {f₀ : ℂ → E} (hUo : IsOpen U)
  (hUc : IsSimplyConnected U) (hz₀ : z₀ ∈ U) (H : TauCeti.ContinuesInside f₀ U z₀) :
  ∃ F, AnalyticOnNhd ℂ F U ∧ F =ᶠ[nhds z₀] f₀
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [The monodromy theorem](the-monodromy-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ContinuesInside.exists_analyticOnNhd`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/GlobalBranch.html#TauCeti.ContinuesInside.exists_analyticOnNhd).

## Sources

- [Tau Ceti documentation: `TauCeti.ContinuesInside.exists_analyticOnNhd`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/GlobalBranch.html#TauCeti.ContinuesInside.exists_analyticOnNhd)
- [Source of `TauCeti.ContinuesInside.exists_analyticOnNhd` in TauCeti/Analysis/Complex/Conformal/GlobalBranch.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/GlobalBranch.lean#L207)
