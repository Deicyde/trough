---
declaration: theorem
origin: cited
lean: FreyPackage.Mazur_Frey_of_a_mod_eight
statement: formalized
proof: formalized
---

# FreyPackage.Mazur_Frey_of_a_mod_eight

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
theorem FreyPackage.Mazur_Frey_of_a_mod_eight (P : FreyPackage)
    (h8 : (P.a : ZMod 8) = 3) :
    GaloisRepIsIrreducible (K := AlgebraicClosure ℚ) ℚ P.freyCurve P.p
```

*Quoted from [Theorems/Thm_FreyPackage_Mazur_Frey_of_a_mod_eight.lean, line 12](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_Mazur_Frey_of_a_mod_eight.lean#L12) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

PROOF-PATH.md names it in [3. Irreducibility](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [FreyPackage.frey_reducible_hasCofixedLine](freypackage-frey-reducible-hascofixedline.md)

## Lean

`FreyPackage.Mazur_Frey_of_a_mod_eight`, stated in [Theorems/Thm_FreyPackage_Mazur_Frey_of_a_mod_eight.lean, line 12](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_Mazur_Frey_of_a_mod_eight.lean#L12) and proved in [P2M/Sol/S_FreyPackage_Mazur_Frey_of_a_mod_eight.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_Mazur_Frey_of_a_mod_eight.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.Mazur_Frey_of_a_mod_eight` in Theorems/Thm_FreyPackage_Mazur_Frey_of_a_mod_eight.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_Mazur_Frey_of_a_mod_eight.lean#L12)
- [Proof of `FreyPackage.Mazur_Frey_of_a_mod_eight` in P2M/Sol/S_FreyPackage_Mazur_Frey_of_a_mod_eight.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_Mazur_Frey_of_a_mod_eight.lean)
- [The repository's documentation page for `FreyPackage.Mazur_Frey_of_a_mod_eight`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.Mazur_Frey_of_a_mod_eight)
