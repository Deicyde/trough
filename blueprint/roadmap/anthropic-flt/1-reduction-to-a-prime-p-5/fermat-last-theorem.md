---
declaration: theorem
origin: cited
lean: fermat_last_theorem
statement: formalized
proof: formalized
---

# fermat_last_theorem

```lean
theorem fermat_last_theorem (n : ℕ) (hn : 3 ≤ n) (a b c : ℕ) (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) : a ^ n + b ^ n ≠ c ^ n
```

*Quoted from [Theorems/Thm_fermat_last_theorem.lean, line 128](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_fermat_last_theorem.lean#L128) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Fermat's Last Theorem”, “FLT”.

PROOF-PATH.md names it in [1. Reduction to a prime p ≥ 5](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [FreyPackage.fermatLastTheoremFor_of_five_le](freypackage-fermatlasttheoremfor-of-five-le.md)

## Lean

`fermat_last_theorem`, stated in [Theorems/Thm_fermat_last_theorem.lean, line 128](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_fermat_last_theorem.lean#L128) and proved in [P2M/Sol/S_fermat_last_theorem.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_fermat_last_theorem.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `fermat_last_theorem` in Theorems/Thm_fermat_last_theorem.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_fermat_last_theorem.lean#L128)
- [Proof of `fermat_last_theorem` in P2M/Sol/S_fermat_last_theorem.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_fermat_last_theorem.lean)
- [The repository's documentation page for `fermat_last_theorem`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#fermat_last_theorem)
