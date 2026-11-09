---
declaration: theorem
origin: cited
lean: TauCeti.hasContinuousLogOn_sub_div_sub_iff
statement: formalized
proof: formalized
---

# The Borsuk criterion

For two points outside a bounded closed set `K ⊆ ℂ`, the Borsuk map
`z ↦ (z - a) / (z - b)` has a continuous logarithm on `K` exactly when `K` fails to separate the
two points; both sides already force `a` and `b` outside `K`. The easy direction is
`TauCeti.hasContinuousLogOn_sub_div_sub`, the hard one
`TauCeti.mem_connectedComponentIn_of_hasContinuousLogOn`.

```lean
TauCeti.hasContinuousLogOn_sub_div_sub_iff {K : Set ℂ} {a b : ℂ} (hK : IsClosed K)
  (hKb : Bornology.IsBounded K) :
  TauCeti.HasContinuousLogOn (fun z => (z - a) / (z - b)) K ↔ b ∈ connectedComponentIn Kᶜ a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Borsuk's separation theorem](borsuks-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasContinuousLogOn_sub_div_sub_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Basic.html#TauCeti.hasContinuousLogOn_sub_div_sub_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.hasContinuousLogOn_sub_div_sub_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Basic.html#TauCeti.hasContinuousLogOn_sub_div_sub_iff)
- [Source of `TauCeti.hasContinuousLogOn_sub_div_sub_iff` in TauCeti/Analysis/Complex/PlaneSeparation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/PlaneSeparation/Basic.lean#L232)
