---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.LinCheck, MIPRE.Tailored.Intro.LinCheck.toCon, MIPRE.Tailored.Intro.satisfies_toCon_iff, MIPRE.Tailored.Intro.fldAt, MIPRE.Tailored.Intro.fieldChecks, MIPRE.Tailored.Intro.forall_fieldChecks_iff, MIPRE.Tailored.Intro.PauliCons.pairChecks, MIPRE.Tailored.Intro.PauliCons.pairChecks_iff, MIPRE.Tailored.Intro.PauliCons.pauliCons, MIPRE.Tailored.Intro.PauliCons.pauliCons_iff, MIPRE.Tailored.Intro.PauliCons.length_of_mem_pauliCons, MIPRE.Tailored.Intro.PauliCons.endpointValid_iff, MIPRE.Tailored.Intro.PauliCons.program_pauli_iff_cons
statement: formalized
proof: formalized
---

# The Pauli basis test as linear constraints

At a pair of Pauli questions of the low individual degree test over $\mathbb{F}_{2^k}$, there is a list of linear constraints on the two answers' bits, depending on the questions only, that hold exactly when the test accepts the two decoded answers. The kernel of the introspection decider accepts a pair of Pauli answers exactly when they have the lengths of their labels, these constraints hold, and its auxiliary check passes.

## Depends on

- [Pauli basis test](../../background-results/part-01/def-qld-game.md)
- [Tailored game; II:1243](../part-01/def-tailored-game.md)
- [The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006](../part-01/def-fourier-forms.md)
- [The input's question at an auxiliary answer, and the Pauli labels](def-intro-source.md)
- [The introspective verifier](../../structure-of-the-proof/part-02/def-intro-verifier.md)
- [Self-dual and normal bases](../../background-results/part-04/def-self-dual-basis.md)
- [Effective unary prime-power decomposition](../../background-results/part-04/lem-binary-degree-decomposition.md)
- [Uniform deterministic binary irreducible polynomials](../../background-results/part-05/lem-binary-uniform-irreducible.md)
- [Downsizing](../../structure-of-the-proof/part-01/lem-cl-downsize.md)
- [Effective polynomial-basis field arithmetic](../../background-results/part-05/lem-effective-binary-field-arithmetic.md)
- [Effective binary matrix arithmetic and elimination](../../background-results/part-05/lem-effective-binary-linear-algebra.md)
- [Effective inversion, Frobenius iteration and trace](../../background-results/part-05/lem-effective-field-inverse-trace.md)
- [Effective Frobenius, trace Gram matrices and table transport](../../background-results/part-05/lem-effective-field-matrices.md)
- [Effective normal element by fixed-space projections](../../background-results/part-05/lem-effective-normal-element.md)
- [Effective self-dualization of a supplied normal basis](../../background-results/part-05/lem-effective-normal-selfdualization.md)
- [The complete binary Pauli predicate](../../structure-of-the-proof/part-06/lem-intro-binary-pauli-predicate.md)
- [Effective circuit polynomial evaluation](../../structure-of-the-proof/part-07/lem-pcp-circuit-evaluator.md)
- [Effective indexing and padding arithmetic](../../structure-of-the-proof/part-07/lem-pcp-padding-programs.md)
- [When a permutation strategy is perfect](../part-01/lem-perm-strategy-perfect.md)
- [Deterministic self-dual normal basis](../../background-results/part-04/lem-self-dual-basis.md)
- [The bespoke PCP for deciders](../../structure-of-the-proof/part-07/thm-pcp-decider.md)

## Proof

Each rule of the test compares field elements and bits that are $\mathbb{F}_2$-linear in the answer bits, with coefficients given by the questions: the evaluation of a line's polynomial at a parameter, the indicator of a point, the trace. A field equation is its $k$ coordinate equations. Where a rule rejects on the questions alone, the list is the rejecting constraint; where it accepts on the questions alone, it is empty.

## Lean

Formalized as [`MIPRE.Tailored.Intro.LinCheck`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LinCheck), [`MIPRE.Tailored.Intro.LinCheck.toCon`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.LinCheck.toCon), [`MIPRE.Tailored.Intro.satisfies_toCon_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.satisfies_toCon_iff), [`MIPRE.Tailored.Intro.fldAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.fldAt), [`MIPRE.Tailored.Intro.fieldChecks`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.fieldChecks), [`MIPRE.Tailored.Intro.forall_fieldChecks_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.forall_fieldChecks_iff), [`MIPRE.Tailored.Intro.PauliCons.pairChecks`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliCons.pairChecks), [`MIPRE.Tailored.Intro.PauliCons.pairChecks_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliCons.pairChecks_iff), [`MIPRE.Tailored.Intro.PauliCons.pauliCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliCons.pauliCons), [`MIPRE.Tailored.Intro.PauliCons.pauliCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliCons.pauliCons_iff), [`MIPRE.Tailored.Intro.PauliCons.length_of_mem_pauliCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliCons.length_of_mem_pauliCons), [`MIPRE.Tailored.Intro.PauliCons.endpointValid_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliCons.endpointValid_iff), [`MIPRE.Tailored.Intro.PauliCons.program_pauli_iff_cons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliCons.program_pauli_iff_cons).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1717](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1717)
