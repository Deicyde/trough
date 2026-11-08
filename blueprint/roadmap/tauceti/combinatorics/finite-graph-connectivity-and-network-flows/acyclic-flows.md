---
declaration: theorem
origin: cited
lean: TauCeti.Flow.exists_isAcyclic
statement: formalized
proof: formalized
---

# Acyclic flows

Every ordinary `s`–`t` flow `f` has an acyclic ordinary `s`–`t` flow of the
same value that is arrowwise at most `f`.

```lean
TauCeti.Flow.exists_isAcyclic.{u, v, w} {V : Type u} {Q : V → V → Type v} {K : Type w} [Fintype V]
  [(x y : V) → Fintype (Q x y)] [AddCommGroup K] [LinearOrder K] [IsOrderedAddMonoid K]
  {cap : TauCeti.Assignment Q K} {s t : V} (f : TauCeti.Flow cap s t) :
  ∃ g, g.toFun.IsAcyclic ∧ g.val = f.val ∧ g.toFun ≤ f.toFun
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Flow.exists_isAcyclic`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Acyclic.html#TauCeti.Flow.exists_isAcyclic).

## Sources

- [Tau Ceti documentation: `TauCeti.Flow.exists_isAcyclic`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Acyclic.html#TauCeti.Flow.exists_isAcyclic)
- [Source of `TauCeti.Flow.exists_isAcyclic` in TauCeti/Combinatorics/Network/Acyclic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/Acyclic.lean#L173)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
