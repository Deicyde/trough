---
declaration: theorem
origin: cited
lean: TauCeti.Contour.eventuallyEq_meromorphicAnalyticPartAt_add_meromorphicPolarPartAt
statement: formalized
proof: formalized
---

# The canonical Laurent decomposition

near `s`, `f` is the analytic part plus the polar
part.

```lean
TauCeti.Contour.eventuallyEq_meromorphicAnalyticPartAt_add_meromorphicPolarPartAt {f : ℂ → ℂ}
  {s : ℂ} (hMero : MeromorphicAt f s) :
  ∀ᶠ (z : ℂ) in nhdsWithin s {s}ᶜ,
    f z =
      TauCeti.Contour.meromorphicAnalyticPartAt hMero z +
        TauCeti.Contour.meromorphicPolarPartAt hMero z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.eventuallyEq_meromorphicAnalyticPartAt_add_meromorphicPolarPartAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/MeromorphicLaurent.html#TauCeti.Contour.eventuallyEq_meromorphicAnalyticPartAt_add_meromorphicPolarPartAt).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.eventuallyEq_meromorphicAnalyticPartAt_add_meromorphicPolarPartAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/MeromorphicLaurent.html#TauCeti.Contour.eventuallyEq_meromorphicAnalyticPartAt_add_meromorphicPolarPartAt)
- [Source of `TauCeti.Contour.eventuallyEq_meromorphicAnalyticPartAt_add_meromorphicPolarPartAt` in TauCeti/Analysis/Contour/MeromorphicLaurent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/MeromorphicLaurent.lean#L251)
