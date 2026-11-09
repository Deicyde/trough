---
declaration: theorem
origin: cited
lean: FreyPackage.frey_no_cofixed_large
statement: formalized
proof: formalized
---

# FreyPackage.frey_no_cofixed_large

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.frey_no_cofixed_large (P : FreyPackage) (hp : 17 ≤ P.p) : ¬ HasGaloisStableCofixedLine (K := AlgebraicClosure ℚ) ℚ P.freyCurve P.p
```

*Quoted from [Theorems/Thm_FreyPackage_frey_no_cofixed_large.lean, line 70](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_no_cofixed_large.lean#L70) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Mazur”, “Eisenstein ideal”, “Eisenstein quotient”.

PROOF-PATH.md names it in [3. Irreducibility](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [WeierstrassCurve.mazurStepThree_not_inZeroComponentAt](weierstrasscurve-mazurstepthree-not-inzerocompon.md)

## Lean

`FreyPackage.frey_no_cofixed_large`, stated in [Theorems/Thm_FreyPackage_frey_no_cofixed_large.lean, line 70](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_no_cofixed_large.lean#L70) and proved in [P2M/Sol/S_FreyPackage_frey_no_cofixed_large.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_frey_no_cofixed_large.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.frey_no_cofixed_large` in Theorems/Thm_FreyPackage_frey_no_cofixed_large.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_no_cofixed_large.lean#L70)
- [Proof of `FreyPackage.frey_no_cofixed_large` in P2M/Sol/S_FreyPackage_frey_no_cofixed_large.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_frey_no_cofixed_large.lean)
- [The repository's documentation page for `FreyPackage.frey_no_cofixed_large`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.frey_no_cofixed_large)
