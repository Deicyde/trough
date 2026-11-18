---
declaration: theorem
origin: cited
lean: TauCeti.LyndonLength.isTree_chiswellMetric
statement: formalized
proof: formalized
---

# Chiswell's theorem, the metric part

the tree of a Lyndon length function whose Gromov
products lie in `Λ`, axiom (L4), is a `Λ`-tree.

```lean
TauCeti.LyndonLength.isTree_chiswellMetric.{u_1, u_2} {G : Type u_1} {Λ : Type u_2} [Group G]
  [AddCommGroup Λ] [LinearOrder Λ] [IsOrderedAddMonoid Λ] (l : TauCeti.LyndonLength G Λ)
  (hl : ∀ (g f : G), ∃ c, ↑c = l.gromovProduct g f) : l.chiswellMetric.IsTree
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LyndonLength.isTree_chiswellMetric`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LambdaTree/Chiswell.html#TauCeti.LyndonLength.isTree_chiswellMetric).

## Sources

- [Tau Ceti documentation: `TauCeti.LyndonLength.isTree_chiswellMetric`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LambdaTree/Chiswell.html#TauCeti.LyndonLength.isTree_chiswellMetric)
- [Source of `TauCeti.LyndonLength.isTree_chiswellMetric` in TauCeti/GroupTheory/LambdaTree/Chiswell.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/LambdaTree/Chiswell.lean#L334)
