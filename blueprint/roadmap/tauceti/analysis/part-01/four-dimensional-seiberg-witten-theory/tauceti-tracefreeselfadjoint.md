---
declaration: def
origin: cited
lean: TauCeti.traceFreeSelfAdjoint
statement: formalized
---

# TauCeti.traceFreeSelfAdjoint

The real subspace `{T : T* = T, tr T = 0}` of trace-free self-adjoint endomorphisms of a complex
inner product space.

```lean
TauCeti.traceFreeSelfAdjoint.{u_1} (E : Type u_1) [NormedAddCommGroup E] [InnerProductSpace ℂ E]
  [CompleteSpace E] : Submodule ℝ (E →L[ℂ] E)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.traceFreeSelfAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Trace/Free.html#TauCeti.traceFreeSelfAdjoint).

## Sources

- [Tau Ceti documentation: `TauCeti.traceFreeSelfAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Trace/Free.html#TauCeti.traceFreeSelfAdjoint)
- [Source of `TauCeti.traceFreeSelfAdjoint` in TauCeti/Analysis/InnerProductSpace/Trace/Free.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Trace/Free.lean#L218)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
