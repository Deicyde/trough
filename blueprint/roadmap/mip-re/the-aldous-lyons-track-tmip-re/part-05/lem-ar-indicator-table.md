---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.indTable_eq_indLoop, MIPRE.Tailored.AnsRed.tableSat_indTable_iff
statement: formalized
proof: formalized
---

# The table holds the decoupled system; fact:polynomial_condition_for_satisfiability

The table is the output of the loops over the coordinates, the signs outermost and the first coordinate innermost. If $N > 0$, $2N \le D$ and the triangulated equations are below $D$, five assignments satisfy the table exactly when they satisfy the decoupled system.

## Depends on

- [The table and the output indicator](def-ar-indicator.md)

## Proof depends on

- [Triangulation and decoupling; rem:prop_triangulated_system](lem-ar-triangle-decouple.md)

## Proof

An index decodes into its coordinates by division and remainder, which locates it in the loops. Each kind of equation of the decoupled system has an index in range, a block of sign $0$ taking the coordinate $0$, and the table contains it; conversely, every equation the table contains is one of the system.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.indTable_eq_indLoop`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.indTable_eq_indLoop), [`MIPRE.Tailored.AnsRed.tableSat_indTable_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.tableSat_indTable_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2501](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2501)
