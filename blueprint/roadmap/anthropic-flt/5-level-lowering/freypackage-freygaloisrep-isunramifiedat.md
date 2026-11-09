---
declaration: theorem
origin: cited
lean: FreyPackage.freyGaloisRep_isUnramifiedAt
statement: formalized
proof: formalized
---

# FreyPackage.freyGaloisRep_isUnramifiedAt

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem FreyPackage.freyGaloisRep_isUnramifiedAt (P : FreyPackage) {q : ℕ} (hq : q.Prime) (hq2 : q ≠ 2) (hqp : q ≠ P.p) : P.GaloisRepUnramifiedAt q
```

*Quoted from [Theorems/Thm_FreyPackage_freyGaloisRep_isUnramifiedAt.lean, line 15](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_freyGaloisRep_isUnramifiedAt.lean#L15) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`FreyPackage.freyGaloisRep_isUnramifiedAt`, stated in [Theorems/Thm_FreyPackage_freyGaloisRep_isUnramifiedAt.lean, line 15](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_freyGaloisRep_isUnramifiedAt.lean#L15) and proved in [P2M/Sol/S_FreyPackage_freyGaloisRep_isUnramifiedAt.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_freyGaloisRep_isUnramifiedAt.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyPackage.freyGaloisRep_isUnramifiedAt` in Theorems/Thm_FreyPackage_freyGaloisRep_isUnramifiedAt.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyPackage_freyGaloisRep_isUnramifiedAt.lean#L15)
- [Proof of `FreyPackage.freyGaloisRep_isUnramifiedAt` in P2M/Sol/S_FreyPackage_freyGaloisRep_isUnramifiedAt.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyPackage_freyGaloisRep_isUnramifiedAt.lean)
- [The repository's documentation page for `FreyPackage.freyGaloisRep_isUnramifiedAt`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyPackage.freyGaloisRep_isUnramifiedAt)
