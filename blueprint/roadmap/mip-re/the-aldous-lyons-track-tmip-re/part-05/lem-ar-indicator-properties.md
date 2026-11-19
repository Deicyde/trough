---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.lstarOK_pad, MIPRE.Tailored.AnsRed.accepts_of_lstarOK, MIPRE.Tailored.AnsRed.tableSat_of_accepts
statement: formalized
proof: formalized
---

# Properties of the output indicator; claim:properties_of_L\*

(1) On readable answers of the readable lengths, padded with zeros to $N$ bits, the check passes for $O$ the table, when the lengths are at most $N$ and $D$ is large enough; and $O$ is the only string it accepts after them. (2) When the check passes on the lengths and constraints of the game at $(x, y)$, five assignments satisfying the table held by $a$ give answers that the game accepts: the readable answers completed by the first two blocks, read at the linear lengths. (3) Answers of the right lengths that the game accepts give the satisfying 5-tuple $\mathsf{Extend}$ of the table, the last three blocks linear in the linear answers.

## Depends on

- [The table holds the decoupled system; fact:polynomial_condition_for_satisfiability](lem-ar-indicator-table.md)
- [The extension; cor:triang_and_decoupling_extend](lem-ar-extend.md)

## Proof

Lemma [The table holds the decoupled system; fact:polynomial_condition_for_satisfiability](lem-ar-indicator-table.md) turns the table into the decoupled system, which is below $D$ by Lemma [Triangulation and decoupling; rem:prop_triangulated_system](lem-ar-triangle-decouple.md) when there are enough triangulation variables, and Lemma [The extension; cor:triang_and_decoupling_extend](lem-ar-extend.md) relates the system to the game.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.lstarOK_pad`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.lstarOK_pad), [`MIPRE.Tailored.AnsRed.accepts_of_lstarOK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.accepts_of_lstarOK), [`MIPRE.Tailored.AnsRed.tableSat_of_accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.tableSat_of_accepts).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2520](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2520)
