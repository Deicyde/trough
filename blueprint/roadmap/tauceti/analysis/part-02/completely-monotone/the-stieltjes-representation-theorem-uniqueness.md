---
declaration: theorem
origin: cited
lean: TauCeti.IsStieltjesFunction.existsUnique_representsStieltjes
statement: formalized
proof: formalized
---

# The Stieltjes representation theorem, uniqueness form

A Stieltjes function has exactly
one representing triple `(a, b, μ)`.

```lean
TauCeti.IsStieltjesFunction.existsUnique_representsStieltjes {f : ℝ → ℝ}
  (hf : TauCeti.IsStieltjesFunction f) : ∃! p, TauCeti.RepresentsStieltjes p.2.2 p.1 p.2.1 f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](../../part-01/weighted-orthogonal-l2-bases-completeness-hilber/moment-determinacy-exponential-moment-form-the-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsStieltjesFunction.existsUnique_representsStieltjes`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Stieltjes/Uniqueness.html#TauCeti.IsStieltjesFunction.existsUnique_representsStieltjes).

## Sources

- [Tau Ceti documentation: `TauCeti.IsStieltjesFunction.existsUnique_representsStieltjes`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Stieltjes/Uniqueness.html#TauCeti.IsStieltjesFunction.existsUnique_representsStieltjes)
- [Source of `TauCeti.IsStieltjesFunction.existsUnique_representsStieltjes` in TauCeti/Analysis/CompletelyMonotone/Stieltjes/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CompletelyMonotone/Stieltjes/Uniqueness.lean#L315)
