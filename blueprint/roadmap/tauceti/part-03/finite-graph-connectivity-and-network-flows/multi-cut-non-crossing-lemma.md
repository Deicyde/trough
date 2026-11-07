---
declaration: theorem
origin: cited
lean: TauCeti.TerminalCut.exists_isMinimum_forall_not_crosses
statement: formalized
proof: formalized
---

# Multi-cut non-crossing lemma

Let `𝒞` be a pairwise non-crossing family of cuts, each a
minimum cut of a symmetric submodular `f` between some pair of vertices. If none of them
separates the distinct vertices `s` and `t`, then some minimum `s`–`t` cut crosses none of
them.

```lean
TauCeti.TerminalCut.exists_isMinimum_forall_not_crosses.{u_1, u_2} {V : Type u_1} {K : Type u_2}
  [Fintype V] [DecidableEq V] [AddCommMonoid K] [LinearOrder K] [IsOrderedCancelAddMonoid K]
  {f : Finset V → K} (hf : TauCeti.IsSymmSubmodular f) {𝒞 : Set (Finset V)}
  (h𝒞 : 𝒞.Pairwise fun Y Z => ¬Y.Crosses Z)
  (hmin : ∀ Y ∈ 𝒞, ∃ a b, TauCeti.TerminalCut.IsMinimum f {a} {b} Y) {s t : V} (hst : s ≠ t)
  (hsep : ∀ Y ∈ 𝒞, s ∈ Y ↔ t ∈ Y) :
  ∃ X, TauCeti.TerminalCut.IsMinimum f {s} {t} X ∧ ∀ Y ∈ 𝒞, ¬X.Crosses Y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TerminalCut.exists_isMinimum_forall_not_crosses`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/Noncrossing.html#TauCeti.TerminalCut.exists_isMinimum_forall_not_crosses).

## Sources

- [Tau Ceti documentation: `TauCeti.TerminalCut.exists_isMinimum_forall_not_crosses`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/Noncrossing.html#TauCeti.TerminalCut.exists_isMinimum_forall_not_crosses)
- [Source of `TauCeti.TerminalCut.exists_isMinimum_forall_not_crosses` in TauCeti/Combinatorics/Network/MinimumCut/Noncrossing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/MinimumCut/Noncrossing.lean#L164)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
