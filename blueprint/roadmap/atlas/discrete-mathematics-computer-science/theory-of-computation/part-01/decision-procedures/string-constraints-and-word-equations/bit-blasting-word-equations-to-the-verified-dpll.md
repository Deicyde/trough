---
declaration: section
origin: cited
lean: Cslib.AutomatedReasoning.StringConstraints.bitVar, Cslib.AutomatedReasoning.StringConstraints.blastWord, Cslib.AutomatedReasoning.StringConstraints.iffClauses, Cslib.AutomatedReasoning.StringConstraints.equalWordClauses, Cslib.AutomatedReasoning.StringConstraints.equationClauses, Cslib.AutomatedReasoning.StringConstraints.blastSystem, Cslib.AutomatedReasoning.StringConstraints.decodeAssignment, Cslib.AutomatedReasoning.StringConstraints.encodeAssignment
statement: formalized
proof: formalized
---

# Bit-blasting word equations to the verified DPLL solver

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html).

## SAT variable index for a bit of a string variable

A positive SAT index for position `p` of variable `i`; `0` is reserved.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.bitVar`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#bit-var).

## Bit-blasting a word into literals

Expand a word into literals at a fixed length for each string variable.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.blastWord`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#blast-word).

## Clauses forcing two literals to be equal

Two implication clauses forcing equal truth values of two literals.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.iffClauses`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#iff-clauses).

## Position-wise equality clauses for literal vectors

Compare literal vectors position by position; a length mismatch emits an empty clause.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.equalWordClauses`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#equal-word-clauses).

## Clauses for a word equation with a length check

Short-circuit unequal lengths before emitting position-wise equality clauses.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.equationClauses`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#equation-clauses).

## CNF encoding of a word-equation system at fixed lengths

CNF for a system at fixed lengths, with shared variables and one constant bit.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.blastSystem`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#blast-system).

## Decoding string values from a SAT assignment

Read each string variable's bits from a SAT assignment.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.decodeAssignment`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#decode-assignment).

## Encoding a substitution as a SAT assignment

Encode a substitution as a total SAT assignment, using inverse pairing.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.encodeAssignment`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#encode-assignment).

## Fixed-length bit-blasting is equisatisfiable

Fixed-length bit-blasting is satisfiability-preserving in both directions.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.cnfSat_blastSystem`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#cnf-sat-blast-system).

## Fixed-length word-equation solver via DPLL

Solve the fixed-length system by bit-blasting and the verified DPLL solver.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.fixedLengthSatB`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#fixed-length-sat-b).

## Correctness of the fixed-length SAT-backed solver

The executable SAT-backed procedure accepts exactly the fixed-length solutions.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.fixedLengthSatB_iff`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#fixed-length-sat-b-iff).

## Enumeration of bounded length profiles

All bounded length profiles, using Mathlib's finite Cartesian-product enumeration.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.lengthProfiles`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#length-profiles).

## Membership in the length-profile enumeration

The profile enumeration contains exactly the pointwise-bounded length assignments.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.mem_lengthProfiles`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#mem-length-profiles).

## Bounded word-equation solver via DPLL

Solve bounded word equations by trying finite length profiles and calling DPLL.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.boundedWordSatB`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#bounded-word-sat-b).

## Soundness and completeness of the bounded word-equation solver

The bounded SAT-backed solver is sound and complete, including empty strings.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.boundedWordSatB_iff`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#bounded-word-sat-b-iff).

## Decision procedure for bounded Boolean word equations

An executable decision procedure for bounded Boolean-alphabet word equations.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.decidableBoundedWordEq`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#decidable-bounded-word-eq).

## Size of the length-profile search

The complete length-profile search has `(B + 1)^n` entries.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.lengthProfiles_length`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#length-profiles-length).

## Clause count for one word equation

One empty clause for unequal lengths; otherwise two clauses per bit.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.equationClauses_length`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#equation-clauses-length).

## Exact clause count of the CNF encoding

Exact CNF size: one constant-bit clause plus the position clauses for every equation.
This is an output-size count, not a `TimeM` or DPLL runtime bound.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.blastSystem_length`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#blast-system-length).

## CNF encoding uses clauses of width at most two

Every emitted clause has at most two literals, including the constant unit clause.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.blastSystem_width`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#blast-system-width).

## Satisfiability as acceptance by some bounded SAT search

A source system is satisfiable iff some bounded SAT search accepts.
This does not make failure at one bound a decision of general UNSAT.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.wordSystem_satisfiable_iff_exists_boundedSatB`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#word-system-satisfiable-iff-exists-bound).

## Pattern-matching decision against a concrete target

Decide matching against a concrete target, with no bound supplied by the caller.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.patternMatchB`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#pattern-match-b).

## Target length bounds the pattern-matching search

The target length is a sufficient search bound for unrestricted pattern matching.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.patternMatchB_iff`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#pattern-match-b-iff).

## Decidability of Boolean-word pattern matching

Executable decidability for unrestricted Boolean-word pattern matching.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.decidablePatternMatch`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#decidable-pattern-match).

## Linear size bound for bit-blasted words

Expanded words are at most linear in source-word length and the supplied bound.
Together with `blastSystem_length`, this bounds CNF output size, not solver time.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.blastWord_length_le`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#blast-word-length-le).

## SAT backend agrees with the bounded formula semantics

The SAT backend decides the same bounded semantics as the existing formula language.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.boundedWordSatB_formula_iff`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/BitBlast.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html#bounded-word-sat-b-formula-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bit-blasting word equations to the verified DPLL solver](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bit-blasting-word-equations-to-the-verified-dpll)
