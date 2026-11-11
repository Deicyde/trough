---
declaration: theorem
origin: cited
lean: TauCeti.not_isPreconnected_compl_union_of_not_isPreconnected_inter
statement: formalized
proof: formalized
---

# Janiszewski's second theorem

If two closed preconnected subsets `S`, `T` of the plane have
a bounded intersection that is not preconnected, then their union separates the plane: the
complement of `S ∪ T` is not preconnected.

```lean
TauCeti.not_isPreconnected_compl_union_of_not_isPreconnected_inter {S T : Set ℂ} (hS : IsClosed S)
  (hT : IsClosed T) (hSc : IsPreconnected S) (hTc : IsPreconnected T)
  (hSTb : Bornology.IsBounded (S ∩ T)) (hST : ¬IsPreconnected (S ∩ T)) : ¬IsPreconnected (S ∪ T)ᶜ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Borsuk's separation theorem](../part-01/borsuks-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.not_isPreconnected_compl_union_of_not_isPreconnected_inter`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Basic.html#TauCeti.not_isPreconnected_compl_union_of_not_isPreconnected_inter).

## Sources

- [Tau Ceti documentation: `TauCeti.not_isPreconnected_compl_union_of_not_isPreconnected_inter`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Basic.html#TauCeti.not_isPreconnected_compl_union_of_not_isPreconnected_inter)
- [Source of `TauCeti.not_isPreconnected_compl_union_of_not_isPreconnected_inter` in TauCeti/Analysis/Complex/PlaneSeparation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/PlaneSeparation/Basic.lean#L294)
