---
declaration: theorem
origin: cited
lean: TauCeti.monodromy_theorem_of_free_homotopy
statement: formalized
proof: formalized
---

# The monodromy theorem for a free homotopy of paths

Let `h` be a continuous map of the
square, read as a family of paths `h (t, ·)` whose *endpoints are allowed to move*, and suppose a
family of germs continues along each of those paths. If the initial germs — the germ of `f t 0` at
`h (t, 0)` — themselves continue along the initial edge `t ↦ h (t, 0)`, then the terminal germs
continue along the terminal edge `t ↦ h (t, 1)`.

This is the monodromy theorem in the form the deck-group and covering-space consumers need: the
continuation of a germ across a homotopy is itself a continuation, along the path the far endpoint
sweeps out. Nothing is assumed rel endpoints; `TauCeti.monodromy_theorem` is the special case in
which both edges are constant, where "continues along a constant path" degenerates to "carries one
germ throughout".

```lean
TauCeti.monodromy_theorem_of_free_homotopy.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] {h : ↑unitInterval × ↑unitInterval → ℂ} (hh : Continuous h)
  {f : ↑unitInterval → ↑unitInterval → ℂ → E}
  (hf :
    ∀ (t : ↑unitInterval), TauCeti.IsAnalyticContinuationAlong (f t) (fun x => h (t, x)) Set.univ)
  (hstart : TauCeti.IsAnalyticContinuationAlong (fun t => f t 0) (fun t => h (t, 0)) Set.univ) :
  TauCeti.IsAnalyticContinuationAlong (fun t => f t 1) (fun t => h (t, 1)) Set.univ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.monodromy_theorem_of_free_homotopy`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Monodromy.html#TauCeti.monodromy_theorem_of_free_homotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.monodromy_theorem_of_free_homotopy`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Monodromy.html#TauCeti.monodromy_theorem_of_free_homotopy)
- [Source of `TauCeti.monodromy_theorem_of_free_homotopy` in TauCeti/Analysis/Complex/Conformal/Monodromy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/Monodromy.lean#L324)
