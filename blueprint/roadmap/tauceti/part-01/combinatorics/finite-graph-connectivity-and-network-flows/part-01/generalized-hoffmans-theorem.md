---
declaration: theorem
origin: cited
lean: TauCeti.ExcessFlow.nonempty_iff
statement: formalized
proof: formalized
---

# Generalized Hoffman's theorem

Ordered signed bounds admit an assignment of prescribed
excess exactly when that excess is balanced and every cut can supply its demand.

```lean
TauCeti.ExcessFlow.nonempty_iff.{u, v, w} {V : Type u} {Q : V → V → Type v} {K : Type w} [Fintype V]
  [(x y : V) → Fintype (Q x y)] [AddCommGroup K] [LinearOrder K] [IsOrderedAddMonoid K]
  [DecidableEq V] {lo hi : TauCeti.Assignment Q K} {b : V → K} (hlo : lo ≤ hi) :
  Nonempty (TauCeti.ExcessFlow lo hi b) ↔
    ∑ v, b v = 0 ∧
      ∀ (S : Finset V), ∑ v ∈ S, b v + TauCeti.arrowSum lo S Sᶜ ≤ TauCeti.arrowSum hi Sᶜ S
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.residualUpdate](tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExcessFlow.nonempty_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Hoffman.html#TauCeti.ExcessFlow.nonempty_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ExcessFlow.nonempty_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Hoffman.html#TauCeti.ExcessFlow.nonempty_iff)
- [Source of `TauCeti.ExcessFlow.nonempty_iff` in TauCeti/Combinatorics/Network/Hoffman.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Network/Hoffman.lean#L382)
