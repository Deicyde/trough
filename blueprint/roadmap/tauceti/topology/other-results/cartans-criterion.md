---
declaration: theorem
origin: cited
lean: TauCeti.Topology.subsingleton_H'_succ_of_isCechAcyclicOn
statement: formalized
proof: formalized
---

# Cartan's criterion

Let `B` be a set of quasi-compact opens of `X` which is closed under
binary intersections and contains, inside each of its members, a basis of the topology of that
member. A sheaf of abelian groups which is Čech acyclic for the finite covers of members of `B` by
members of `B` has no cohomology in positive degrees on the members of `B`.

```lean
TauCeti.Topology.subsingleton_H'_succ_of_isCechAcyclicOn.{u} {X : TopCat}
  {B : Set (TopologicalSpace.Opens ↑X)}
  {F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) AddCommGrpCat}
  (hinf : ∀ U ∈ B, ∀ V ∈ B, U ⊓ V ∈ B) (hcpt : ∀ U ∈ B, IsCompact ↑U)
  (hbasis : ∀ U ∈ B, ∀ V ≤ U, ∀ x ∈ V, ∃ W ∈ B, x ∈ W ∧ W ≤ V)
  (hF : TauCeti.Topology.IsCechAcyclicOn B F) {Y : TopologicalSpace.Opens ↑X} (hY : Y ∈ B) (n : ℕ) :
  Subsingleton ↑(F.H' (n + 1) Y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Topology.subsingleton_H'_succ_of_isCechAcyclicOn`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cartan.html#TauCeti.Topology.subsingleton_H'_succ_of_isCechAcyclicOn).

## Sources

- [Tau Ceti documentation: `TauCeti.Topology.subsingleton_H'_succ_of_isCechAcyclicOn`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cartan.html#TauCeti.Topology.subsingleton_H'_succ_of_isCechAcyclicOn)
- [Source of `TauCeti.Topology.subsingleton_H'_succ_of_isCechAcyclicOn` in TauCeti/Topology/Sheaves/Cartan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Sheaves/Cartan.lean#L330)
