---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.univ_zmod_two, MIPRE.Tailored.observableSign_eq_bitSign, MIPRE.Tailored.encObs_observableToProjector, MIPRE.Tailored.encObs_observableToProjector_const, MIPRE.Tailored.pauliX_eq, MIPRE.Tailored.pauliZ_eq, MIPRE.Tailored.isSignedPerm_pauliX, MIPRE.Tailored.isSignedPerm_pauliZ, MIPRE.Tailored.isDiag_pauliZ, MIPRE.Tailored.isSignedPerm_grid
statement: formalized
proof: formalized
---

# Binary measurements, the qubit Paulis and the Magic Square grid

For an observable $O$, an answer bit reading the outcome of the measurement $\frac12(1 \pm O)$, flipped by a constant $c$, has observable $(-1)^c O$, and one ignoring it has observable $\pm {I}$. The qubit Paulis $X$ and $Z$ are signed permutation matrices, $Z$ diagonal; hence so are the nine observables of the Magic Square grid of the Pauli basis test's honest strategy, $A \otimes {I}, {I} \otimes X, \ldots, AB \otimes ZX$, when $A$ and $B$ are.

## Depends on

- [Signed permutation matrices](../part-01/lem-signed-perm.md)
- [The bit observables of an encoded measurement](lem-encoded-pvm-obs.md)
- [Observables and projective measurements correspond](../../foundations/part-01/lem-observable-projector.md)

## Proof

The observable is $\sum_b (-1)^{\mathrm{enc}(b)} \frac12(1 + (-1)^b O)$, a two-term sum. $X$ is the matrix of the transposition, $Z$ the diagonal of the signs $(1, -1)$, and the grid is built from them, $A$ and $B$ by Kronecker products and products.

## Lean

Formalized as [`MIPRE.Tailored.univ_zmod_two`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.univ_zmod_two), [`MIPRE.Tailored.observableSign_eq_bitSign`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.observableSign_eq_bitSign), [`MIPRE.Tailored.encObs_observableToProjector`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs_observableToProjector), [`MIPRE.Tailored.encObs_observableToProjector_const`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs_observableToProjector_const), [`MIPRE.Tailored.pauliX_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.pauliX_eq), [`MIPRE.Tailored.pauliZ_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.pauliZ_eq), [`MIPRE.Tailored.isSignedPerm_pauliX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_pauliX), [`MIPRE.Tailored.isSignedPerm_pauliZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_pauliZ), [`MIPRE.Tailored.isDiag_pauliZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_pauliZ), [`MIPRE.Tailored.isSignedPerm_grid`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_grid).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1434](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1434)
