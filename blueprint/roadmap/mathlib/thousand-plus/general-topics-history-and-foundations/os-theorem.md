# Łoś' theorem

**Łoś's Theorem**: A sentence is true in an ultraproduct if and only if the set of structures
it is true in is in the ultrafilter.

```lean
FirstOrder.Language.Ultraproduct.sentence_realize.{u, v, u_1, u_2} {α : Type u_1} {M : α → Type u_2}
  {u : Ultrafilter α} {L : FirstOrder.Language} [(a : α) → L.Structure (M a)]
  [∀ (a : α), Nonempty (M a)] (φ : L.Sentence) : (↑u).Product M ⊨ φ ↔ ∀ᶠ (a : α) in ↑u, M a ⊨ φ
```

## Depends on

- [Filter](../../overview/topology/general-topology/part-01/filter.md)
- [First-order formula](../../overview/logic-and-computation/model-theory/first-order-formula.md)
- [First-order structure](../../overview/logic-and-computation/model-theory/first-order-structure.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.Ultraproduct.sentence_realize`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Ultraproducts.html#FirstOrder.Language.Ultraproduct.sentence_realize)
- [Source of `FirstOrder.Language.Ultraproduct.sentence_realize` in Mathlib/ModelTheory/Ultraproducts.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/ModelTheory/Ultraproducts.lean#L152)
- [1000+ theorems list: Q1535225](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1740)
- [1000+ theorems project: Q1535225](https://1000-plus.github.io/all.html?length=-1#Q1535225)
- [Wikipedia: Łoś' theorem](https://en.wikipedia.org/wiki/%C5%81o%C5%9B'_theorem)
- [Wikidata: Q1535225](https://www.wikidata.org/wiki/Q1535225)
