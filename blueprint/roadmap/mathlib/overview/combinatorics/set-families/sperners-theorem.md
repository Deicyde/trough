# Sperner's theorem

**Sperner's theorem**. The size of an antichain in `Finset α` is bounded by the size of the
maximal layer in `Finset α`. This precisely means that `Finset α` is a Sperner order.

```lean
IsAntichain.sperner.{u_2} {α : Type u_2} [Fintype α] {𝒜 : Finset (Finset α)}
  (h𝒜 : IsAntichain (fun x1 x2 => x1 ⊆ x2) ↑𝒜) :
  𝒜.card ≤ (Fintype.card α).choose (Fintype.card α / 2)
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [LYM inequality](lym-inequality.md)

## Sources

- [Mathlib documentation: `IsAntichain.sperner`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/LYM.html#IsAntichain.sperner)
- [Source of `IsAntichain.sperner` in Mathlib/Combinatorics/SetFamily/LYM.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SetFamily/LYM.lean#L233)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L514)
- [1000+ theorems list: Q2226786](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2094)
- [1000+ theorems project: Q2226786](https://1000-plus.github.io/all.html?length=-1#Q2226786)
- [Wikipedia: Sperner's theorem](https://en.wikipedia.org/wiki/Sperner's_theorem)
- [Wikidata: Q2226786](https://www.wikidata.org/wiki/Q2226786)
