---
declaration: theorem
origin: cited
lean: TauCeti.mem_connectedComponentIn_of_hasContinuousLogOn
statement: formalized
proof: formalized
---

# Borsuk's separation theorem

If the Borsuk map `z ↦ (z - a) / (z - b)` of two points
outside a bounded closed set `K ⊆ ℂ` has a continuous logarithm on `K`, then `K` does not separate
them: `b` lies in the connected component of `a` in `Kᶜ`.

That the two points lie outside `K` is not assumed: the Borsuk map vanishes at `a` and, by the
division convention, at `b` as well, so a logarithm on `K` already excludes both from `K`.

This is the converse of `TauCeti.hasContinuousLogOn_sub_div_sub`, and the direction that fails
without boundedness — the real axis separates `i` from `-i` while carrying a logarithm of their
Borsuk map.

```lean
TauCeti.mem_connectedComponentIn_of_hasContinuousLogOn {K : Set ℂ} {a b : ℂ} (hK : IsClosed K)
  (hKb : Bornology.IsBounded K) (hlog : TauCeti.HasContinuousLogOn (fun z => (z - a) / (z - b)) K) :
  b ∈ connectedComponentIn Kᶜ a
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_connectedComponentIn_of_hasContinuousLogOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Basic.html#TauCeti.mem_connectedComponentIn_of_hasContinuousLogOn).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_connectedComponentIn_of_hasContinuousLogOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Basic.html#TauCeti.mem_connectedComponentIn_of_hasContinuousLogOn)
- [Source of `TauCeti.mem_connectedComponentIn_of_hasContinuousLogOn` in TauCeti/Analysis/Complex/PlaneSeparation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/PlaneSeparation/Basic.lean#L204)
