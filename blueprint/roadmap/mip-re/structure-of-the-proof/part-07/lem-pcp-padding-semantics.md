---
declaration: lemma
origin: cited
lean: MIPRE.SAT.Cnf5.sat_pad_iff, MIPRE.SAT.Circuit.DescribesDecider.of_pad
statement: formalized
proof: formalized
---

# Padding preserves the complete answer tapes

Embed the five blocks of a decoupled formula into larger blocks. Add every clause whose first or second literal is beyond its original answer block and has the blank-tape sign: positive at even indices, negative at odd indices. The enlarged formula is satisfied exactly when the restrictions satisfy the original formula and both complete answer tails equal the blank tape. Thus a circuit implementing this clause set still describes the same decider, provided the original answer block has length at least $2T$.

## Depends on

- [Succinctly described 3SAT and decoupled 5SAT](../../background-results/part-03/def-succinct-3sat.md)

## Proof

Restriction proves the original clauses. To isolate an answer-tail bit, choose the signs in the other four blocks so that their literals are false. Conversely, each added clause contains a true blank-tail literal. Extend the three auxiliary assignments arbitrarily, and use that every accepted answer has length at most $T$, so its tape is blank beyond $2T$. This is the semantic part of the paper's `prop:exciting-padding-prop`; the circuit algorithm and its cost remain separate obligations.

## Lean

Formalized as [`MIPRE.SAT.Cnf5.sat_pad_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Cnf5.sat_pad_iff), [`MIPRE.SAT.Circuit.DescribesDecider.of_pad`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.DescribesDecider.of_pad).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4734](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4734)
