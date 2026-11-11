---
declaration: theorem
origin: cited
lean: TauCeti.janiszewski
statement: formalized
proof: formalized
---

# Janiszewski's theorem

If two bounded closed subsets `S`, `T` of the plane have preconnected
intersection and neither separates `a` from `b`, then their union does not separate them either.

```lean
TauCeti.janiszewski {a b : ℂ} {S T : Set ℂ} (hS : IsClosed S) (hT : IsClosed T)
  (hSb : Bornology.IsBounded S) (hTb : Bornology.IsBounded T) (hST : IsPreconnected (S ∩ T))
  (hSsep : b ∈ connectedComponentIn Sᶜ a) (hTsep : b ∈ connectedComponentIn Tᶜ a) :
  b ∈ connectedComponentIn (S ∪ T)ᶜ a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Borsuk's separation theorem](../part-01/borsuks-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.janiszewski`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Basic.html#TauCeti.janiszewski).

## Sources

- [Tau Ceti documentation: `TauCeti.janiszewski`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Basic.html#TauCeti.janiszewski)
- [Source of `TauCeti.janiszewski` in TauCeti/Analysis/Complex/PlaneSeparation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/PlaneSeparation/Basic.lean#L235)
