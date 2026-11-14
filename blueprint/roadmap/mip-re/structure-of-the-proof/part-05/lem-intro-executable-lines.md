---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.LineProgram.lineRepresentativeProg_correct, MIPRE.Introspection.LineProgram.lineRepresentativeProg_runs, MIPRE.Introspection.LineProgram.lineRepresentativeProg_time_le, MIPRE.QLD.PauliCL.coordNumbering_point_X, MIPRE.QLD.PauliCL.coordNumbering_point_Z, MIPRE.QLD.PauliCL.coordNumbering_seed, MIPRE.QLD.PauliCL.coordNumbering_direction, MIPRE.QLD.PauliCL.coordNumbering_scalar_X, MIPRE.QLD.PauliCL.coordNumbering_scalar_Z, MIPRE.QLD.PauliCL.binaryCoordEquiv_val, MIPRE.QLD.PauliCL.binaryVectorEquiv_apply, MIPRE.QLD.PauliCL.representative_eq_canonLin, MIPRE.QLD.PauliCL.lineRepresentativeProg_canonLin
statement: formalized
proof: formalized
---

# Executable canonical lines and explicit binary coordinates

One uniform polynomial-time program computes the canonical base point of a line from its field-encoded point and direction, including zero direction. One polynomial in field width plus vector length bounds its runtime, and the program halts on every raw input. The Pauli CL coordinates are numbered explicitly in the order point-X, point-Z, seed, direction, scale-X, scale-Z, with each field coordinate followed by its basis bits.

## Depends on

- [Uniform deterministic binary irreducible polynomials](../../background-results/part-05/lem-binary-uniform-irreducible.md)
- [Effective polynomial-basis field arithmetic](../../background-results/part-05/lem-effective-binary-field-arithmetic.md)
- [Effective inversion, Frobenius iteration and trace](../../background-results/part-05/lem-effective-field-inverse-trace.md)
- [The bespoke PCP for deciders](../part-07/thm-pcp-decider.md)
- [Pauli basis test](../../background-results/part-01/def-qld-game.md)
- [Downsizing](../part-01/lem-cl-downsize.md)

## Proof depends on

- [Effective binary matrix arithmetic and elimination](../../background-results/part-05/lem-effective-binary-linear-algebra.md)
- [Effective Frobenius, trace Gram matrices and table transport](../../background-results/part-05/lem-effective-field-matrices.md)
- [Effective circuit polynomial evaluation](../part-07/lem-pcp-circuit-evaluator.md)
- [The two complements](../part-01/lem-cl-canonical.md)

## Proof

Scan for the first nonzero direction coordinate, compute the scalar with the checked Shoup inverse and multiplication programs, and subtract that multiple of the direction. Identify this expression with the existing canonical-line representative. Compose the polynomial runtime bounds. The coordinate numbering is a sum and product of explicit finite equivalences; its value equations identify every block and bit.

## Lean

Formalized as [`MIPRE.Introspection.LineProgram.lineRepresentativeProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.LineProgram.lineRepresentativeProg_correct), [`MIPRE.Introspection.LineProgram.lineRepresentativeProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.LineProgram.lineRepresentativeProg_runs), [`MIPRE.Introspection.LineProgram.lineRepresentativeProg_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.LineProgram.lineRepresentativeProg_time_le), [`MIPRE.QLD.PauliCL.coordNumbering_point_X`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.coordNumbering_point_X), [`MIPRE.QLD.PauliCL.coordNumbering_point_Z`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.coordNumbering_point_Z), [`MIPRE.QLD.PauliCL.coordNumbering_seed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.coordNumbering_seed), [`MIPRE.QLD.PauliCL.coordNumbering_direction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.coordNumbering_direction), [`MIPRE.QLD.PauliCL.coordNumbering_scalar_X`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.coordNumbering_scalar_X), [`MIPRE.QLD.PauliCL.coordNumbering_scalar_Z`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.coordNumbering_scalar_Z), [`MIPRE.QLD.PauliCL.binaryCoordEquiv_val`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.binaryCoordEquiv_val), [`MIPRE.QLD.PauliCL.binaryVectorEquiv_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.binaryVectorEquiv_apply), [`MIPRE.QLD.PauliCL.representative_eq_canonLin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.representative_eq_canonLin), [`MIPRE.QLD.PauliCL.lineRepresentativeProg_canonLin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.lineRepresentativeProg_canonLin).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3436](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3436)
