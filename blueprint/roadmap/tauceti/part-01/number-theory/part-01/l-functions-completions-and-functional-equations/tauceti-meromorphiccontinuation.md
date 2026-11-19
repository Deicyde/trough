---
declaration: def
origin: cited
lean: TauCeti.meromorphicContinuation
statement: formalized
---

# TauCeti.meromorphicContinuation

The unique whole-plane meromorphic normal form agreeing with `f` on `σ < re s`,
or zero when no such continuation exists. Existence must be proved separately before
using its agreement with the original function.

```lean
TauCeti.meromorphicContinuation.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  (σ : ℝ) (f : ℂ → E) : ℂ → E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.meromorphicContinuation`](https://taucetiproject.org/docs/TauCeti/Analysis/Meromorphic/Continuation.html#TauCeti.meromorphicContinuation).

## Sources

- [Tau Ceti documentation: `TauCeti.meromorphicContinuation`](https://taucetiproject.org/docs/TauCeti/Analysis/Meromorphic/Continuation.html#TauCeti.meromorphicContinuation)
- [Source of `TauCeti.meromorphicContinuation` in TauCeti/Analysis/Meromorphic/Continuation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Meromorphic/Continuation.lean#L69)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LFunctions/STATUS.md)
