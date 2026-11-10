---
declaration: theorem
origin: cited
lean: flt_regular
statement: formalized
proof: formalized
---

# flt_regular

```lean
open scoped NumberField
theorem flt_regular {p : ℕ} [Fact p.Prime] (hreg : p.Coprime (Fintype.card (ClassGroup (𝓞 (CyclotomicField p ℚ))))) (hodd : p ≠ 2) : FermatLastTheoremFor p
```

*Quoted from [Theorems/Thm_flt_regular.lean, line 6](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_flt_regular.lean#L6) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Kummer”, “regular primes”, “flt-regular”.

PROOF-PATH.md names it in [3. Irreducibility](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`flt_regular`, stated in [Theorems/Thm_flt_regular.lean, line 6](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_flt_regular.lean#L6) and proved in [P2M/Sol/S_flt_regular.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_flt_regular.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `flt_regular` in Theorems/Thm_flt_regular.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_flt_regular.lean#L6)
- [Proof of `flt_regular` in P2M/Sol/S_flt_regular.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_flt_regular.lean)
- [The repository's documentation page for `flt_regular`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#flt_regular)
