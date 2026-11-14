# Background results

This chapter collects theorems that the proof relies on but whose proofs appear in other papers. Each entry gives a full statement, a pointer to the literature, and comments on its role and on formalization. The project may initially assume these as axioms; discharging them are independent sub-projects. Three of these results are larger sub-projects and are developed in their own sections: the computability results in Section [Computability](../computability/README.md) and parallel repetition in Section [Parallel repetition](../parallel-repetition/README.md); they are included in the summary table below for completeness. Statements are given in the form closest to how they will be used. The compression pipeline carries bipartite soundness in $\mathrm{val}^*$; synchronous and tracial results appear as internal ingredients with their own transfer obligations.

Each entry carries an estimate of the formalization effort: [$\bullet$ easy] for self-contained arguments of at most a few pages, [$\bullet\bullet$ medium] for substantial but well-delimited developments, and [$\bullet\bullet\bullet$ hard] for results whose formalization is a project in itself; [$\checkmark$ (mostly) in Mathlib] marks statements essentially available in Mathlib. The estimates are for the statement as it will be used (including any required interface translation) and are of course provisional. Independently of the effort estimate, the [[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] badge (introduced in Section [Foundations](../foundations/README.md)) marks results of general quantum-information interest that are intended to be upstreamed to QuantumLib.

| Result | Statement | Source | Effort |
| --- | --- | --- | --- |
| Gowers–Hatami | Thm. [Gowers–Hatami](part-01/thm-gowers-hatami.md) | (GH17, dlS21) | ✓ |
| Almost-synchronous correlations | Thm. [Almost-synchronous strategies are near synchronous strategies](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L137) | (Vid22) | hard |
| Orthonormalization | Thm. [Orthonormalization](part-01/thm-orthonormalization.md) | (dlS21) | ✓ |
| Magic Square rigidity | Thm. [Magic Square rigidity](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L420) | (WBMS16) | easy |
| Low individual degree test (canonical lines) | Thm. [Quantum soundness of the canonical-line low individual degree test](part-01/thm-lidt-soundness.md) | (JNVWY21qld) | ✓ |
| Low individual degree test (seeded CL) | Thm. [Quantum soundness of the seeded CL test](part-01/thm-lidt-cl-soundness.md) | (AuditSync26) | ✓ |
| Low individual degree test (seeded CL, one codeword) | Thm. [Quantum soundness of the seeded CL test, one codeword](part-01/thm-lidt-cl-soundness-one.md) | (JNVWY21qld) | ✓ |
| Low individual degree test (Pauli) | Thm. [Pauli basis test / quantum low individual degree test](part-01/thm-qld.md) | (AuditSync26) | hard |
| Direct parallel repetition (commuting-operator) | Thm. [Direct parallel repetition for commuting-operator strategies](../parallel-repetition/thm-direct-repetition-co.md) | (Vid26) | ✓ |
| Direct parallel repetition (entangled) | Thm. [Direct parallel repetition for entangled strategies](../parallel-repetition/thm-direct-repetition-q.md) | (OpenAI26) | ✓ |
| Tracial density | Thm. [Lin's tracial density theorem](../parallel-repetition/thm-tracial-density.md) | (Lin23, Vid26) | ✓ |
| Recursive compression lemma | Lem. [Recursive compression](../computability/lem-recursive-compression.md) | (MNY) | ✓ |
| Compressibility criterion | Lem. [Compressibility criterion](../computability/lem-compressible-criterion.md) | (Lin25) | ✓ |
| Efficient computability toolkit | Lems. [Efficient universal Turing machine](../computability/lem-universal-tm.md)–[Efficient Kleene recursion theorem](../computability/lem-kleene.md) | (MNY) | hard |
| Halting undecidability | Thm. [Turing](part-03/thm-halting-undecidable.md) | Mathlib | ✓ |
| Succinct Cook–Levin | Thm. [Explicit succinct Cook–Levin](part-04/thm-succinct-sat.md) | (Coo71, PY86) | ✓ |
| Self-dual normal bases | Lem. [Deterministic self-dual normal basis](part-04/lem-self-dual-basis.md) | (Sho90, Len91) | medium |
| Schwartz–Zippel | Lem. [Schwartz–Zippel](part-05/lem-schwartz-zippel.md) | (Sch80, Zip79) | ✓ |
| Value approximable from below | Lem. [The value is approximable from below](part-05/lem-value-lower-approx.md) | folklore | medium |

The anchored parallel repetition theorem of (BVY17), and the entropy and fidelity toolkit its proof needs, are not on the path to the main theorem and are not stated in this blueprint (Remark [Direct versus anchored repetition](../parallel-repetition/README.md)).

## The Gowers–Hatami theorem

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)]

## [Approximate representation to Pauli basis test / quantum low…](part-01/README.md)

- [Approximate representation](part-01/def-approx-rep.md)
- [Gowers–Hatami](part-01/thm-gowers-hatami.md)
- [Orthonormalization](part-01/thm-orthonormalization.md)
- [A centre-valued trace from a vector trace](part-01/lem-center-valued-trace.md)
- [Orthonormalization in algebras without abelian projections](part-01/thm-orthonormalization-no-abelian.md)
- [Direct Magic Square anticommutation — what the pipeline actually needs](part-01/lem-ms-direct-anticomm.md)
- [Canonical-line low individual degree test](part-01/def-lidt.md)
- [Quantum soundness of the canonical-line low individual degree test](part-01/thm-lidt-soundness.md)
- [Seeded CL low individual degree test](part-01/def-lidt-cl.md)
- [Quantum soundness of the seeded CL test](part-01/thm-lidt-cl-soundness.md)
- [The adapter's two maps, and acceptance](part-01/lem-lidt-cl-adapter-maps.md)
- [The adapter's cost in the question distributions](part-01/lem-lidt-cl-adapter-weights.md)
- [The parameter choice](part-01/lem-lidt-cl-adapter-params.md)
- [Quantum soundness of the seeded CL test, one codeword](part-01/thm-lidt-cl-soundness-one.md)
- [Several codewords: the simultaneity reduction](part-01/lem-lidt-ldc.md)
- [The padded multi-codeword game adapter](part-01/lem-lidt-ldc-adapter.md)
- [Extracting exactly linear combined codewords](part-01/lem-lidt-ldc-extraction.md)
- [Absorbing the simultaneous reduction's error](part-01/lem-lidt-ldc-error.md)
- [Pauli basis test](part-01/def-qld-game.md)
- [Pauli basis test / quantum low individual degree test](part-01/thm-qld.md)

## [Theorem Pauli basis test /… to The sublines distribution](part-02/README.md)

- [Theorem Pauli basis test / quantum low individual degree test on the valid answers](part-02/cor-qld-valid.md)
- [Theorem Pauli basis test / quantum low individual degree test on qubits](part-02/cor-qld-binary.md)
- [Anticommuting question tuples](part-02/fact-omega-anticomm-prob.md)
- [Averaging preserves closeness](part-02/lem-qld-averaging.md)
- [From POVM elements to generalized observables](part-02/lem-qld-povm-to-obs.md)
- [Win implications](part-02/lem-qld-win.md)
- [Consistency of the point observables](part-02/lem-qld-obs-consistency.md)
- [Signed commutation of the point observables](part-02/lem-qld-obs-commutation.md)
- [Signed commutation, the commuting case](part-02/lem-qld-obs-commutation-comm.md)
- [Signed commutation, the anticommuting case](part-02/lem-qld-obs-commutation-acomm.md)
- [Expanded point measurements](part-02/lem-qld-expanded-points.md)
- [Expanded point measurements are self-consistent](part-02/lem-qld-expanded-consistency.md)
- [Expanded point observables commute](part-02/lem-qld-expanded-commutation.md)
- [Expanded line measurements](part-02/lem-qld-expanded-lines.md)
- [Exact linearity from approximate linearity](part-02/thm-linearity.md)
- [Combined $XZ$ point measurements](part-02/lem-qld-combined-points.md)
- [Axis degree for expanded line measurements](part-02/lem-qld-axis-degree.md)
- [Pairs of lines](part-02/lem-qld-pairs-of-lines.md)
- [Padded point measurements](part-02/lem-qld-padded-points.md)
- [The sublines distribution](part-02/lem-qld-sublines.md)

## [Padded line POVM to Succinctly described 3SAT and…](part-03/README.md)

- [Padded line POVM](part-03/lem-qld-padded-lines.md)
- [The models of stages 4 and 5](part-03/def-qld-physical-model.md)
- [The simultaneous global measurement](part-03/lem-qld-simultaneous.md)
- [Admissible padded setup](part-03/lem-qld-global-setup.md)
- [All padded subtests succeed](part-03/lem-qld-global-success.md)
- [A global padded polynomial PVM](part-03/lem-qld-global-pvm.md)
- [Removing dummy-coordinate dependence](part-03/lem-qld-global-dummy.md)
- [Ordered products with global outcome multipliers](part-03/lem-qld-global-products.md)
- [Linearity in the two combining coefficients](part-03/lem-qld-global-linear.md)
- [Separating the two point variables](part-03/lem-qld-global-separate.md)
- [Completing the pair measurement projectively](part-03/lem-qld-global-complete.md)
- [Sandwich estimates and the two marginals](part-03/lem-qld-global-sandwich.md)
- [Global robustness in both register versions](part-03/lem-qld-global-robustness.md)
- [The marginals track the point measurements](part-03/lem-qld-helper.md)
- [Exact Pauli operators](part-03/lem-qld-exact-paulis.md)
- [Self-consistency of the exact Pauli observables](part-03/lem-qld-pauli-selfcons.md)
- [The swap isometry](part-03/lem-qld-swap.md)
- [The error of the Pauli basis test](part-03/lem-qld-error.md)
- [Turing](part-03/thm-halting-undecidable.md)
- [Succinctly described 3SAT and decoupled 5SAT](part-03/def-succinct-3sat.md)

## [Explicit succinct Cook–Levin to Effective unary prime-power…](part-04/README.md)

- [Explicit succinct Cook–Levin](part-04/thm-succinct-sat.md)
- [Correctness of the Cook–Levin tableau](part-04/lem-correct-tableau.md)
- [Self-dual and normal bases](part-04/def-self-dual-basis.md)
- [Self-dual coordinates are trace pairings](part-04/lem-downsize-field.md)
- [Deterministic self-dual normal basis](part-04/lem-self-dual-basis.md)
- [Self-dualization in the group algebra](part-04/lem-group-algebra-selfdualization.md)
- [The binary square-root program](part-04/lem-binary-square-root-program.md)
- [Existence of a self-dual normal basis](part-04/lem-self-dual-basis-exists.md)
- [Effective normalization of binary polynomials](part-04/lem-binary-polynomial-normalization.md)
- [Effective monic binary division](part-04/lem-binary-monic-division.md)
- [Canonical coordinates in monic binary quotients](part-04/lem-binary-monic-quotient.md)
- [Canonical binary Euclidean algorithms](part-04/lem-binary-euclidean-algorithms.md)
- [Effective Frobenius fixed spaces in binary quotients](part-04/lem-binary-quotient-fixed-space.md)
- [Deterministic squarefree binary factorization](part-04/lem-binary-squarefree-factorization.md)
- [Effective closed Frobenius orbit polynomials](part-04/lem-binary-orbit-polynomial.md)
- [Effective odd-prime nonresidues](part-04/lem-binary-odd-prime-nonresidue.md)
- [Effective irreducibles of every power-of-two degree](part-04/lem-binary-power-two-irreducible.md)
- [Effective irreducibles of every odd-prime-power degree](part-04/lem-binary-odd-prime-power-irreducible.md)
- [Effective combination of coprime degrees](part-04/lem-binary-coprime-degree-combination.md)
- [Effective unary prime-power decomposition](part-04/lem-binary-degree-decomposition.md)

## [Uniform deterministic binary… to The perturbation split](part-05/README.md)

- [Uniform deterministic binary irreducible polynomials](part-05/lem-binary-uniform-irreducible.md)
- [Effective polynomial-basis field arithmetic](part-05/lem-effective-binary-field-arithmetic.md)
- [Effective inversion, Frobenius iteration and trace](part-05/lem-effective-field-inverse-trace.md)
- [Effective binary matrix arithmetic and elimination](part-05/lem-effective-binary-linear-algebra.md)
- [Effective Frobenius, trace Gram matrices and table transport](part-05/lem-effective-field-matrices.md)
- [Effective normal element by fixed-space projections](part-05/lem-effective-normal-element.md)
- [Effective self-dualization of a supplied normal basis](part-05/lem-effective-normal-selfdualization.md)
- [An admissible field with a bit representation](part-05/lem-admissible-field-exists.md)
- [Schwartz–Zippel](part-05/lem-schwartz-zippel.md)
- [The value is approximable from below](part-05/lem-value-lower-approx.md)
- [Gaussian-rational projective measurements are dense](part-05/lem-rational-pvm-dense.md)
- [Exact rational strategies suffice](part-05/lem-rational-strategies-suffice.md)
- [Decidable candidate set: a norm constraint is two psd tests](part-05/lem-norm-two-psd.md)
- [The perturbation split](part-05/lem-perturbation-split.md)
