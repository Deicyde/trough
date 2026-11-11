---
declaration: theorem
origin: cited
lean: TauCeti.topologicalClosure_closure_eq_top_iff_quotient_profiniteFrattini
statement: formalized
proof: formalized
---

# Generation modulo the Frattini subgroup

A set topologically generates a profinite
group if and only if its image topologically generates the quotient by the Frattini subgroup.

```lean
TauCeti.topologicalClosure_closure_eq_top_iff_quotient_profiniteFrattini.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  (s : Set G) :
  (Subgroup.closure s).topologicalClosure = ⊤ ↔
    (Subgroup.closure
          (⇑(QuotientGroup.mk' (TauCeti.profiniteFrattini G)) '' s)).topologicalClosure =
      ⊤
```

## Depends on

- [TauCeti.profiniteFrattini](tauceti-profinitefrattini.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.topologicalClosure_closure_eq_top_iff_quotient_profiniteFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Frattini.html#TauCeti.topologicalClosure_closure_eq_top_iff_quotient_profiniteFrattini).

## Sources

- [Tau Ceti documentation: `TauCeti.topologicalClosure_closure_eq_top_iff_quotient_profiniteFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Frattini.html#TauCeti.topologicalClosure_closure_eq_top_iff_quotient_profiniteFrattini)
- [Source of `TauCeti.topologicalClosure_closure_eq_top_iff_quotient_profiniteFrattini` in TauCeti/Topology/Algebra/Group/Profinite/Frattini.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Frattini.lean#L227)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteProPGroups/STATUS.md)
