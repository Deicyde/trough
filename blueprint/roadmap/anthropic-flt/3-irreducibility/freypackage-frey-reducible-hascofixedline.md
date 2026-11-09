---
declaration: theorem
origin: cited
lean: FreyPackage.frey_reducible_hasCofixedLine
statement: formalized
proof: formalized
---

# FreyPackage.frey_reducible_hasCofixedLine

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.frey_reducible_hasCofixedLine (P : FreyPackage) (hred : ¬ GaloisRepIsIrreducible (K := AlgebraicClosure ℚ) ℚ P.freyCurve P.p) : HasGaloisStableCofixedLine (K := AlgebraicClosure ℚ) ℚ P.freyCurve P.p
```

*Quoted from [Theorems/Thm_FreyPackage_frey_reducible_hasCofixedLine.lean, line 15](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_reducible_hasCofixedLine.lean#L15) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Serre”, “cofixed line”.

PROOF-PATH.md names it in [3. Irreducibility](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [FreyPackage.freyGaloisRep_isUnramifiedAt](../5-level-lowering/freypackage-freygaloisrep-isunramifiedat.md)

## Lean

`FreyPackage.frey_reducible_hasCofixedLine`, stated in [Theorems/Thm_FreyPackage_frey_reducible_hasCofixedLine.lean, line 15](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_reducible_hasCofixedLine.lean#L15) and proved in [P2M/Sol/S_FreyPackage_frey_reducible_hasCofixedLine.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_frey_reducible_hasCofixedLine.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.frey_reducible_hasCofixedLine` in Theorems/Thm_FreyPackage_frey_reducible_hasCofixedLine.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_reducible_hasCofixedLine.lean#L15)
- [Proof of `FreyPackage.frey_reducible_hasCofixedLine` in P2M/Sol/S_FreyPackage_frey_reducible_hasCofixedLine.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_frey_reducible_hasCofixedLine.lean)
- [The repository's documentation page for `FreyPackage.frey_reducible_hasCofixedLine`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.frey_reducible_hasCofixedLine)
