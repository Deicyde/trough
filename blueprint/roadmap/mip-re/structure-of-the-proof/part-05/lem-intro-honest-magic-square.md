---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.HonestMagicSquare.grid_isObservable, MIPRE.Introspection.HonestMagicSquare.cells_commute, MIPRE.Introspection.HonestMagicSquare.row_product, MIPRE.Introspection.HonestMagicSquare.variableOp_isPVM, MIPRE.Introspection.HonestMagicSquare.constraintOp_isPVM, MIPRE.Introspection.HonestMagicSquare.variable_constraint_commute, MIPRE.Introspection.HonestMagicSquare.constraint_reject_zero, MIPRE.Introspection.HonestMagicSquare.variableOp_embeds_first, MIPRE.Introspection.HonestMagicSquare.variableOp_embeds_second, MIPRE.Introspection.HonestMagicSquare.grid_transpose, MIPRE.Introspection.HonestMagicSquare.constraintOp_transpose, MIPRE.Introspection.HonestMagicSquare.questionOp_isPVM, MIPRE.Introspection.HonestMagicSquare.questionOp_reject, MIPRE.Introspection.HonestMagicSquare.strategy_isPCC, MIPRE.Introspection.HonestMagicSquare.strategy_value, MIPRE.Introspection.HonestMagicSquare.exists_perfectPCC
statement: formalized
proof: formalized
---

# Honest Magic Square extension of an anticommuting pair

Any two anticommuting self-adjoint involutions on a nonzero finite carrier extend, with one extra qubit, to the actual Magic Square game. Explicit binary variable measurements and three-bit constraint measurements are projective, preserve the original binary measurements at cells zero and four, and give a value-one PCC strategy for the doubled game. Symmetric input matrices give symmetric grid and constraint matrices.

## Depends on

- [The Magic Square](../../foundations/part-01/def-magic-square.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [LCS game](../../foundations/part-01/def-lcs-game.md)
- [Observables and projective measurements correspond](../../foundations/part-01/lem-observable-projector.md)

## Proof depends on

- [Pauli mixing with a retained classical fibre](../part-02/lem-pauli-mixing.md)
- [A perfect strategy rejects nothing on the support](../../foundations/part-01/lem-perfect-rejects-nothing.md)

## Proof

Construct all nine observables by tensoring the original pair with the single-qubit Pauli pair. Verify the six commuting triples and their parity products. Their joint spectral projectors have zero effect for wrong parity and zero joint effect for inconsistent incidence answers. Evaluate these explicit projectors on the EPR state to prove perfect acceptance and cross-question commutation directly.

## Lean

Formalized as [`MIPRE.Introspection.HonestMagicSquare.grid_isObservable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.grid_isObservable), [`MIPRE.Introspection.HonestMagicSquare.cells_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.cells_commute), [`MIPRE.Introspection.HonestMagicSquare.row_product`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.row_product), [`MIPRE.Introspection.HonestMagicSquare.variableOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.variableOp_isPVM), [`MIPRE.Introspection.HonestMagicSquare.constraintOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.constraintOp_isPVM), [`MIPRE.Introspection.HonestMagicSquare.variable_constraint_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.variable_constraint_commute), [`MIPRE.Introspection.HonestMagicSquare.constraint_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.constraint_reject_zero), [`MIPRE.Introspection.HonestMagicSquare.variableOp_embeds_first`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.variableOp_embeds_first), [`MIPRE.Introspection.HonestMagicSquare.variableOp_embeds_second`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.variableOp_embeds_second), [`MIPRE.Introspection.HonestMagicSquare.grid_transpose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.grid_transpose), [`MIPRE.Introspection.HonestMagicSquare.constraintOp_transpose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.constraintOp_transpose), [`MIPRE.Introspection.HonestMagicSquare.questionOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.questionOp_isPVM), [`MIPRE.Introspection.HonestMagicSquare.questionOp_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.questionOp_reject), [`MIPRE.Introspection.HonestMagicSquare.strategy_isPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.strategy_isPCC), [`MIPRE.Introspection.HonestMagicSquare.strategy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.strategy_value), [`MIPRE.Introspection.HonestMagicSquare.exists_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.HonestMagicSquare.exists_perfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3242](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3242)
