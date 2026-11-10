---
declaration: theorem
origin: cited
lean: FreyPackage.frey_no_cofixed_small
statement: formalized
proof: formalized
---

# FreyPackage.frey_no_cofixed_small

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.frey_no_cofixed_small (P : FreyPackage) (hp : P.p = 5 ∨ P.p = 7 ∨ P.p = 13) : ¬ HasGaloisStableCofixedLine (K := AlgebraicClosure ℚ) ℚ P.freyCurve P.p
```

*Quoted from [Theorems/Thm_FreyPackage_frey_no_cofixed_small.lean, line 13](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_no_cofixed_small.lean#L13) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

PROOF-PATH.md names it in [3. Irreducibility](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [fermatLastTheoremFive](fermatlasttheoremfive.md)
- [fermatLastTheoremSeven](fermatlasttheoremseven.md)
- [flt_regular](flt-regular.md)

## Lean

`FreyPackage.frey_no_cofixed_small`, stated in [Theorems/Thm_FreyPackage_frey_no_cofixed_small.lean, line 13](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_no_cofixed_small.lean#L13) and proved in [P2M/Sol/S_FreyPackage_frey_no_cofixed_small.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_frey_no_cofixed_small.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.frey_no_cofixed_small` in Theorems/Thm_FreyPackage_frey_no_cofixed_small.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_no_cofixed_small.lean#L13)
- [Proof of `FreyPackage.frey_no_cofixed_small` in P2M/Sol/S_FreyPackage_frey_no_cofixed_small.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_frey_no_cofixed_small.lean)
- [The repository's documentation page for `FreyPackage.frey_no_cofixed_small`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.frey_no_cofixed_small)
