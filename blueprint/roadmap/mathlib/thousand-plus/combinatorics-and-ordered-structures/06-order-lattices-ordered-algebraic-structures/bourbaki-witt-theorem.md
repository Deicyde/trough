# Bourbaki–Witt theorem

**The Bourbaki-Witt Theorem**: If `α` is a chain complete partial order and `f : α → α` is
inflationary, then `f` has a fixed point

```lean
ChainCompletePartialOrder.nonempty_fixedPoints_of_inflationary.{u_1} {α : Type u_1}
  [ChainCompletePartialOrder α] {f : α → α} [Nonempty α] (le_map : ∀ (x : α), x ≤ f x) :
  (Function.fixedPoints f).Nonempty
```

## Depends on

- [Fixed points](../../../overview/dynamics/general-theory/fixed-points.md)

## Sources

- [Mathlib documentation: `ChainCompletePartialOrder.nonempty_fixedPoints_of_inflationary`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/BourbakiWitt.html#ChainCompletePartialOrder.nonempty_fixedPoints_of_inflationary)
- [Source of `ChainCompletePartialOrder.nonempty_fixedPoints_of_inflationary` in Mathlib/Order/BourbakiWitt.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Order/BourbakiWitt.lean#L221)
- [1000+ theorems list: Q4950096](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L2944)
- [1000+ theorems project: Q4950096](https://1000-plus.github.io/all.html?length=-1#Q4950096)
- [Wikipedia: Bourbaki–Witt theorem](https://en.wikipedia.org/wiki/Bourbaki%E2%80%93Witt_theorem)
- [Wikidata: Q4950096](https://www.wikidata.org/wiki/Q4950096)
