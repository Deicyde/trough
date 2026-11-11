---
declaration: theorem
origin: cited
lean: TauCeti.topologicalClosure_closure_range_eq_top_of_ker_le_profiniteFrattini
statement: formalized
proof: formalized
---

# Every lift of a generating family along a Frattini cover generates

Let `f : G →* K` be a
continuous homomorphism from a profinite group to a Hausdorff group with kernel in the Frattini
subgroup of `G`. A family `g` of elements of `G` whose image under `f` topologically generates `K`
topologically generates `G`. No finiteness of the index type is needed, and `f` is automatically
surjective: its range is compact, hence closed in `K`, and contains the generating family.

```lean
TauCeti.topologicalClosure_closure_range_eq_top_of_ker_le_profiniteFrattini.{u, v, u_1} {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] {K : Type v} [Group K] [TopologicalSpace K] [IsTopologicalGroup K]
  [T2Space K] {f : G →* K} (hf : Continuous ⇑f) (hker : f.ker ≤ TauCeti.profiniteFrattini G)
  {ι : Type u_1} {g : ι → G} (hg : (Subgroup.closure (Set.range (⇑f ∘ g))).topologicalClosure = ⊤) :
  (Subgroup.closure (Set.range g)).topologicalClosure = ⊤
```

## Depends on

- [TauCeti.profiniteFrattini](tauceti-profinitefrattini.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.topologicalClosure_closure_range_eq_top_of_ker_le_profiniteFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Frattini.html#TauCeti.topologicalClosure_closure_range_eq_top_of_ker_le_profiniteFrattini).

## Sources

- [Tau Ceti documentation: `TauCeti.topologicalClosure_closure_range_eq_top_of_ker_le_profiniteFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Frattini.html#TauCeti.topologicalClosure_closure_range_eq_top_of_ker_le_profiniteFrattini)
- [Source of `TauCeti.topologicalClosure_closure_range_eq_top_of_ker_le_profiniteFrattini` in TauCeti/Topology/Algebra/Group/Profinite/Frattini.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Frattini.lean#L209)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteProPGroups/STATUS.md)
