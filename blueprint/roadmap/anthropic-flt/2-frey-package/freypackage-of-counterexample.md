---
declaration: theorem
origin: cited
lean: FreyPackage.of_counterexample
statement: formalized
proof: formalized
---

# FreyPackage.of_counterexample

```lean
theorem FreyPackage.of_counterexample (a b c : ℤ) (ha : a ≠ 0) (hb : b ≠ 0) (hc : c ≠ 0) (p : ℕ) (pp : p.Prime) (hp5 : 5 ≤ p) (H : a ^ p + b ^ p = c ^ p) : Nonempty FreyPackage
```

*Quoted from [Theorems/Thm_FreyPackage_of_counterexample.lean, line 6](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_of_counterexample.lean#L6) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Frey curve”, “Frey”.

PROOF-PATH.md names it in [1. Reduction to a prime p ≥ 5](../1-reduction-to-a-prime-p-5/README.md) and [2. Frey package](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`FreyPackage.of_counterexample`, stated in [Theorems/Thm_FreyPackage_of_counterexample.lean, line 6](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_of_counterexample.lean#L6) and proved in [P2M/Sol/S_FreyPackage_of_counterexample.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_of_counterexample.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.of_counterexample` in Theorems/Thm_FreyPackage_of_counterexample.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_of_counterexample.lean#L6)
- [Proof of `FreyPackage.of_counterexample` in P2M/Sol/S_FreyPackage_of_counterexample.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_of_counterexample.lean)
- [The repository's documentation page for `FreyPackage.of_counterexample`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.of_counterexample)
