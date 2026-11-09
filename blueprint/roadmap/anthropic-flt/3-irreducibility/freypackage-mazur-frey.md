---
declaration: theorem
origin: cited
lean: FreyPackage.Mazur_Frey
statement: formalized
proof: formalized
---

# Irreducibility

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.Mazur_Frey (P : FreyPackage) : GaloisRepIsIrreducible (K := AlgebraicClosure ℚ) ℚ P.freyCurve P.p
```

*Quoted from [Theorems/Thm_FreyPackage_Mazur_Frey.lean, line 70](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_Mazur_Frey.lean#L70) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Mazur”, “irreducibility of the mod-p representation”.

PROOF-PATH.md names it in [3. Irreducibility](README.md), as the theorem that carries step 3.

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [FreyPackage.Mazur_Frey_of_a_mod_eight](freypackage-mazur-frey-of-a-mod-eight.md)
- [FreyPackage.frey_no_cofixed_eleven](freypackage-frey-no-cofixed-eleven.md)
- [FreyPackage.frey_no_cofixed_large](freypackage-frey-no-cofixed-large.md)
- [FreyPackage.frey_no_cofixed_small](freypackage-frey-no-cofixed-small.md)
- [FreyPackage.frey_reducible_hasCofixedLine](freypackage-frey-reducible-hascofixedline.md)

## Lean

`FreyPackage.Mazur_Frey`, stated in [Theorems/Thm_FreyPackage_Mazur_Frey.lean, line 70](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_Mazur_Frey.lean#L70) and proved in [P2M/Sol/S_FreyPackage_Mazur_Frey.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_Mazur_Frey.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.Mazur_Frey` in Theorems/Thm_FreyPackage_Mazur_Frey.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_Mazur_Frey.lean#L70)
- [Proof of `FreyPackage.Mazur_Frey` in P2M/Sol/S_FreyPackage_Mazur_Frey.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_Mazur_Frey.lean)
- [The repository's documentation page for `FreyPackage.Mazur_Frey`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.Mazur_Frey)
