---
declaration: def
origin: cited
lean: TauCeti.CkHolderSpace
statement: formalized
---

# TauCeti.CkHolderSpace

The space of bounded `C^k` maps whose iterated Fréchet derivatives through order `k` are
bounded and whose `k`-th iterated derivative is globally `α`-Hölder. Its norm is

`∑_{i ≤ k} ‖D^i f‖_∞ + [D^k f]_α`.

```lean
TauCeti.CkHolderSpace.{u, v} (k : ℕ) (α : NNReal) (E : Type u) (F : Type v) [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] : Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CkHolderSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Holder/Iterated.html#TauCeti.CkHolderSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.CkHolderSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Holder/Iterated.html#TauCeti.CkHolderSpace)
- [Source of `TauCeti.CkHolderSpace` in TauCeti/Analysis/Holder/Iterated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Holder/Iterated.lean#L92)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PDE/STATUS.md)
