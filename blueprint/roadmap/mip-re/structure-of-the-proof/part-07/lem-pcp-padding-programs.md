---
declaration: lemma
origin: cited
lean: MIPRE.SAT.ArrayProg.eqBits, MIPRE.SAT.ArrayProg.eqNat, MIPRE.SAT.ArrayProg.getD, MIPRE.SAT.Fml.renameBy, MIPRE.SAT.Fml.eval_rename, MIPRE.SAT.ceilPowerProg, MIPRE.SAT.le_ceilPower, MIPRE.SAT.ceilPower_le_twice, MIPRE.Cost.PolyTimeFun.bitsValue, MIPRE.Cost.PolyTimeFun.predN, MIPRE.Cost.PolyTimeFun.addUnary, MIPRE.Cost.PolyTimeFun.subUnary
statement: formalized
proof: formalized
---

# Effective indexing and padding arithmetic

Binary equality, array lookup by a binary index, and formula renaming have ambient polynomial-time programs. The least power of two above a unary number can be produced in unary in polynomial time. Binary normalization, predecessor, and addition or subtraction of a unary offset are polynomial-time as well.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Scan the supplied array instead of expanding its index. Rename the formula's postorder input nodes. For power-of-two rounding, double a unary accumulator once per binary digit, capping every intermediate state by twice the input length plus one. Normalize binary numbers by a fold of the binary constructor; the existing borrow machine gives predecessor, including a separate zero case. The offset loops have explicit bounds on every intermediate encoding.

## Lean

Formalized as [`MIPRE.SAT.ArrayProg.eqBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.ArrayProg.eqBits), [`MIPRE.SAT.ArrayProg.eqNat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.ArrayProg.eqNat), [`MIPRE.SAT.ArrayProg.getD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.ArrayProg.getD), [`MIPRE.SAT.Fml.renameBy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Fml.renameBy), [`MIPRE.SAT.Fml.eval_rename`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Fml.eval_rename), [`MIPRE.SAT.ceilPowerProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.ceilPowerProg), [`MIPRE.SAT.le_ceilPower`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.le_ceilPower), [`MIPRE.SAT.ceilPower_le_twice`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.ceilPower_le_twice), [`MIPRE.Cost.PolyTimeFun.bitsValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.PolyTimeFun.bitsValue), [`MIPRE.Cost.PolyTimeFun.predN`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.PolyTimeFun.predN), [`MIPRE.Cost.PolyTimeFun.addUnary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.PolyTimeFun.addUnary), [`MIPRE.Cost.PolyTimeFun.subUnary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.PolyTimeFun.subUnary).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4759](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4759)
