---
declaration: lemma
origin: cited
lean: MIPRE.Cost.Data.primrec_decode_prod_nat, MIPRE.Cost.exists_semidecider_of_decode, MIPRE.Cost.exists_semidecider_prod_nat
statement: formalized
proof: formalized
---

# Semideciders on encoded values

Let $\alpha$ be a type encoded as data with a primitive recursive decoding. Then every recursively enumerable predicate on $\alpha$ is the halting set of a closed program of the cost model on the encodings of its arguments. In particular this holds for pairs $(x, n)$ of a bit string and a number.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [The value is approximable from below](../background-results/part-05/lem-value-lower-approx.md)

## Proof

Prefix the bit-string semidecider of Lemma [The value is approximable from below](../background-results/part-05/lem-value-lower-approx.md) with the program that writes the postorder serialization of its input (`Prog.serProg`, Remark [Relation to the abstract compression lemma](../structure-of-the-proof/README.md)). Serialization and the stack machine `Data.parse` invert each other, so the predicate “decode the parse of this bit string, and test it” holds of the serialization of $\mathrm{encode}(a)$ exactly when the original predicate holds of $a$; and it is recursively enumerable, being the original predicate precomposed with a computable function.

## Lean

Formalized as [`MIPRE.Cost.Data.primrec_decode_prod_nat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Data.primrec_decode_prod_nat), [`MIPRE.Cost.exists_semidecider_of_decode`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.exists_semidecider_of_decode), [`MIPRE.Cost.exists_semidecider_prod_nat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.exists_semidecider_prod_nat).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 552](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L552)
