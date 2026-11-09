# Four functions theorem

The **Four Functions Theorem**, aka **Ahlswede-Daykin Inequality**.

```lean
four_functions_theorem.{u_1, u_2} {α : Type u_1} {β : Type u_2} [DistribLattice α] [CommSemiring β]
  [LinearOrder β] [IsStrictOrderedRing β] [ExistsAddOfLE β] (f₁ f₂ f₃ f₄ : α → β) [DecidableEq α]
  (h₁ : 0 ≤ f₁) (h₂ : 0 ≤ f₂) (h₃ : 0 ≤ f₃) (h₄ : 0 ≤ f₄)
  (h : ∀ (a b : α), f₁ a * f₂ b ≤ f₃ (a ⊓ b) * f₄ (a ⊔ b)) (s t : Finset α) :
  (∑ a ∈ s, f₁ a) * ∑ a ∈ t, f₂ a ≤ (∑ a ∈ s ⊼ t, f₃ a) * ∑ a ∈ s ⊻ t, f₄ a
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `four_functions_theorem`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/FourFunctions.html#four_functions_theorem)
- [Source of `four_functions_theorem` in Mathlib/Combinatorics/SetFamily/FourFunctions.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/SetFamily/FourFunctions.lean#L302)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L509)
- [1000+ theorems list: Q4695203](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L2776)
- [1000+ theorems project: Q4695203](https://1000-plus.github.io/all.html?length=-1#Q4695203)
- [Wikipedia: Four functions theorem](https://en.wikipedia.org/wiki/Four_functions_theorem)
- [Wikidata: Q4695203](https://www.wikidata.org/wiki/Q4695203)
