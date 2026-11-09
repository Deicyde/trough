---
declaration: theorem
origin: cited
lean: TauCeti.IsCompleteBernsteinFunction.existsUnique_representsCompleteBernstein
statement: formalized
proof: formalized
---

# The complete Bernstein representation theorem, uniqueness form

A complete Bernstein
function has exactly one representing triple `(a, b, μ)`.

```lean
TauCeti.IsCompleteBernsteinFunction.existsUnique_representsCompleteBernstein {f : ℝ → ℝ}
  (hf : TauCeti.IsCompleteBernsteinFunction f) :
  ∃! p, TauCeti.RepresentsCompleteBernstein p.2.2 p.1 p.2.1 f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](../../part-01/weighted-orthogonal-l2-bases-completeness-hilber/moment-determinacy-exponential-moment-form-the-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsCompleteBernsteinFunction.existsUnique_representsCompleteBernstein`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Stieltjes/Uniqueness.html#TauCeti.IsCompleteBernsteinFunction.existsUnique_representsCompleteBernstein).

## Sources

- [Tau Ceti documentation: `TauCeti.IsCompleteBernsteinFunction.existsUnique_representsCompleteBernstein`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Stieltjes/Uniqueness.html#TauCeti.IsCompleteBernsteinFunction.existsUnique_representsCompleteBernstein)
- [Source of `TauCeti.IsCompleteBernsteinFunction.existsUnique_representsCompleteBernstein` in TauCeti/Analysis/CompletelyMonotone/Stieltjes/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CompletelyMonotone/Stieltjes/Uniqueness.lean#L326)
