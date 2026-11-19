---
declaration: def
origin: cited
lean: TauCeti.MemWkpLoc
statement: formalized
---

# TauCeti.MemWkpLoc

The iterated weak derivatives through order `k` exist on `interior U` and are `Lᵖ` on
every compact subset of `U`, including compact sets reaching its boundary.
The first derivative takes values in `ℂ →L[ℝ] F`; higher derivatives iterate this construction.
No integrability at infinity or boundary trace is required.

```lean
TauCeti.MemWkpLoc.{u_3} (p : ENNReal) (U : Set ℂ) (k : ℕ) {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace ℝ F] : (ℂ → F) → Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MemWkpLoc`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Basic.html#TauCeti.MemWkpLoc).

## Sources

- [Tau Ceti documentation: `TauCeti.MemWkpLoc`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Basic.html#TauCeti.MemWkpLoc)
- [Source of `TauCeti.MemWkpLoc` in TauCeti/Analysis/Sobolev/Local/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/Local/Basic.lean#L318)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
