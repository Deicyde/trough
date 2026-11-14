---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.allBits_eq_iterate, MIPRE.Tailored.Sofic.dedup_eq_foldr, MIPRE.Tailored.Sofic.zipIdx_map_eq, MIPRE.Tailored.Sofic.primrec_consWord, MIPRE.Tailored.Sofic.primrec_consWords, MIPRE.Tailored.Sofic.primrec_clause, MIPRE.Tailored.Sofic.primrec_clauses, MIPRE.Tailored.Sofic.totalWeight_eq, MIPRE.Tailored.Sofic.primrec_assocTest
statement: formalized
proof: formalized
---

# The associated test is computable from the game

The map from a tailored game description to the description of its associated test is primitive recursive.

## Depends on

- [The associated subgroup test; I:2086](def-assoc-test.md)
- [A tailored game description as a game description](../../the-aldous-lyons-track-tmip-re/part-02/lem-tailored-conversion.md)

## Proof

Each construction is a composition of list operations. Three are rewritten first: the readable values as an iterate, deduplication as a fold, and the enumeration of the fixed literals by a range.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.allBits_eq_iterate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.allBits_eq_iterate), [`MIPRE.Tailored.Sofic.dedup_eq_foldr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.dedup_eq_foldr), [`MIPRE.Tailored.Sofic.zipIdx_map_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.zipIdx_map_eq), [`MIPRE.Tailored.Sofic.primrec_consWord`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.primrec_consWord), [`MIPRE.Tailored.Sofic.primrec_consWords`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.primrec_consWords), [`MIPRE.Tailored.Sofic.primrec_clause`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.primrec_clause), [`MIPRE.Tailored.Sofic.primrec_clauses`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.primrec_clauses), [`MIPRE.Tailored.Sofic.totalWeight_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.totalWeight_eq), [`MIPRE.Tailored.Sofic.primrec_assocTest`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.primrec_assocTest).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 100](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L100)
