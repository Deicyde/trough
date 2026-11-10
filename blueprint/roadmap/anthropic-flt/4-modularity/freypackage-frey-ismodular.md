---
declaration: theorem
origin: cited
lean: FreyPackage.frey_isModular
statement: formalized
proof: formalized
---

# Modularity

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.frey_isModular (P : FreyPackage) : P.freyCurve.IsModular
```

*Quoted from [Theorems/Thm_FreyPackage_frey_isModular.lean, line 131](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_isModular.lean#L131) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Wiles”, “Taylor-Wiles”, “modularity of the Frey curve”.

PROOF-PATH.md names it in [4. Modularity](README.md), as the theorem that carries step 4.

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [WeierstrassCurve.modularity_of_semistableModel](weierstrasscurve-modularity-of-semistablemodel.md)

## Lean

`FreyPackage.frey_isModular`, stated in [Theorems/Thm_FreyPackage_frey_isModular.lean, line 131](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_isModular.lean#L131) and proved in [P2M/Sol/S_FreyPackage_frey_isModular.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_frey_isModular.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.frey_isModular` in Theorems/Thm_FreyPackage_frey_isModular.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_frey_isModular.lean#L131)
- [Proof of `FreyPackage.frey_isModular` in P2M/Sol/S_FreyPackage_frey_isModular.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_frey_isModular.lean)
- [The repository's documentation page for `FreyPackage.frey_isModular`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.frey_isModular)
