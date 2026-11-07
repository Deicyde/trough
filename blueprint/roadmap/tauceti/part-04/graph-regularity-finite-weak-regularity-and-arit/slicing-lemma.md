---
declaration: theorem
origin: cited
lean: TauCeti.Colored3Graph.IsTopRegularOverPolyad.of_pairSupport_subset
statement: formalized
proof: formalized
---

# Slicing lemma

If `H` is `(δ, r)`-top-regular over `P` at a positive rank, then it is
`(max (2δ) (δ / α), r)`-top-regular over every polyad `P'` whose pair graphs lie in those of `P`
and whose support is at least an `α`-fraction of the support of `P`. The polyad `P'` may live
over a different skeleton, so this is how top regularity passes to a refined lower skeleton.

```lean
TauCeti.Colored3Graph.IsTopRegularOverPolyad.of_pairSupport_subset.{u_1, u_2, u_3, u_4}
  {κ : Type u_1} {κ₂ : Type u_2} {V : Type u_3} [Fintype V] [DecidableEq V]
  {S : TauCeti.PairSkeleton3 κ₂ V} {P : TauCeti.Polyad3 S} [DecidableEq κ]
  {H : TauCeti.Colored3Graph κ V} {δ : ℝ} {r : ℕ} {κ₂' : Type u_4}
  {S' : TauCeti.PairSkeleton3 κ₂' V} {P' : TauCeti.Polyad3 S'}
  (h₀₁ : P'.pairSupport₀₁ ⊆ P.pairSupport₀₁) (h₀₂ : P'.pairSupport₀₂ ⊆ P.pairSupport₀₂)
  (h₁₂ : P'.pairSupport₁₂ ⊆ P.pairSupport₁₂)
  (h : TauCeti.Colored3Graph.IsTopRegularOverPolyad P H δ r) (hr : 1 ≤ r) {α : ℝ} (hα : 0 < α)
  (hP' : α * ↑P.support.card ≤ ↑P'.support.card) :
  TauCeti.Colored3Graph.IsTopRegularOverPolyad P' H (max (2 * δ) (δ / α)) r
```

## Depends on

- [TauCeti.Colored3Graph.IsTopRegularOverPolyad](tauceti-colored3graph-istopregularoverpolyad.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Colored3Graph.IsTopRegularOverPolyad.of_pairSupport_subset`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Polyad/TopRegular.html#TauCeti.Colored3Graph.IsTopRegularOverPolyad.of_pairSupport_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.Colored3Graph.IsTopRegularOverPolyad.of_pairSupport_subset`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Polyad/TopRegular.html#TauCeti.Colored3Graph.IsTopRegularOverPolyad.of_pairSupport_subset)
- [Source of `TauCeti.Colored3Graph.IsTopRegularOverPolyad.of_pairSupport_subset` in TauCeti/Combinatorics/Hypergraph/Polyad/TopRegular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Hypergraph/Polyad/TopRegular.lean#L165)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Regularity/STATUS.md)
