---
declaration: theorem
origin: cited
lean: ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd
statement: formalized
proof: formalized
---

# ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd

```lean
theorem ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd {k : Type} [Field k]
    (ρ : ResidualGaloisRep k) (h2 : (2 : k) ≠ 0) (hirr : ρ.IsIrreducible) (hodd : ρ.IsOdd) :
    ρ.IsAbsolutelyIrreducible
```

*Quoted from [Theorems/Thm_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean, line 5](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean#L5) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “absolutely irreducible”, “odd”.

PROOF-PATH.md names it in [Exact strength of the named steps](../exact-strength-of-the-named-steps/README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd`, stated in [Theorems/Thm_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean, line 5](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean#L5) and proved in [P2M/Sol/S_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd` in Theorems/Thm_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean#L5)
- [Proof of `ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd` in P2M/Sol/S_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_ResidualGaloisRep_isAbsolutelyIrreducible_of_isIrreducible_of_isOdd.lean)
- [The repository's documentation page for `ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd)
