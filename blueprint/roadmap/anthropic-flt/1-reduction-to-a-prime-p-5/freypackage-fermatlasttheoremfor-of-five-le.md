---
declaration: theorem
origin: cited
lean: FreyPackage.fermatLastTheoremFor_of_five_le
statement: formalized
proof: formalized
---

# FreyPackage.fermatLastTheoremFor_of_five_le

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.fermatLastTheoremFor_of_five_le (p : ℕ) (pp : p.Prime) (hp5 : 5 ≤ p) : FermatLastTheoremFor p
```

*Quoted from [Theorems/Thm_FreyPackage_fermatLastTheoremFor_of_five_le.lean, line 136](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_fermatLastTheoremFor_of_five_le.lean#L136) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

PROOF-PATH.md names it in [1. Reduction to a prime p ≥ 5](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [FreyPackage.no_frey_package](../2-frey-package/freypackage-no-frey-package.md)
- [FreyPackage.of_counterexample](../2-frey-package/freypackage-of-counterexample.md)

## Lean

`FreyPackage.fermatLastTheoremFor_of_five_le`, stated in [Theorems/Thm_FreyPackage_fermatLastTheoremFor_of_five_le.lean, line 136](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_fermatLastTheoremFor_of_five_le.lean#L136) and proved in [P2M/Sol/S_FreyPackage_fermatLastTheoremFor_of_five_le.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_fermatLastTheoremFor_of_five_le.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.fermatLastTheoremFor_of_five_le` in Theorems/Thm_FreyPackage_fermatLastTheoremFor_of_five_le.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_fermatLastTheoremFor_of_five_le.lean#L136)
- [Proof of `FreyPackage.fermatLastTheoremFor_of_five_le` in P2M/Sol/S_FreyPackage_fermatLastTheoremFor_of_five_le.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_fermatLastTheoremFor_of_five_le.lean)
- [The repository's documentation page for `FreyPackage.fermatLastTheoremFor_of_five_le`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.fermatLastTheoremFor_of_five_le)
