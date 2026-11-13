---
declaration: section
origin: cited
lean: Cslib.PDL.Hoare, Cslib.PDL.hoare_iff_subset_core, Cslib.PDL.hoare_iff_test_le, Cslib.PDL.hoare_iff_test_eq, Cslib.PDL.hoare_iff_box, Cslib.PDL.Hoare.consequence, Cslib.PDL.Hoare.seq, Cslib.PDL.Hoare.choice_iff
statement: formalized
proof: formalized
---

# Partial correctness and loop invariants for PDL

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html).

## PDL

## Partial-correctness Hoare triple for PDL programs

Every execution of `a` from `P` ends in `Q`, without a termination
requirement.

Formalized by `Cslib.PDL.Hoare`, a definition declared in [CSLibExt/Logics/PDL/Hoare.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#hoare).

## Partial correctness as inclusion in the relational core

Partial correctness agrees with the canonical relation's core.

Formalized by `Cslib.PDL.hoare_iff_subset_core`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#hoare-iff-subset-core).

## Hoare triples as KAT test inequalities

Hoare verification is equivalent to the KAT test inequality.

Formalized by `Cslib.PDL.hoare_iff_test_le`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#hoare-iff-test-le).

## Hoare triples as KAT absorption equations

The equivalent KAT absorption equation for verification.

Formalized by `Cslib.PDL.hoare_iff_test_eq`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#hoare-iff-test-eq).

## Hoare triples with formula assertions as box validity

Formula assertions connect Hoare verification to global PDL validity,
not just an atomic-action modality.

Formalized by `Cslib.PDL.hoare_iff_box`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#hoare-iff-box).

## Hoare rule of consequence

Strengthen the precondition and weaken the postcondition.

Formalized by `Cslib.PDL.Hoare.consequence`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#consequence).

## Hoare rule for sequential composition

Sequential verification uses the first postcondition as the second
precondition.

Formalized by `Cslib.PDL.Hoare.seq`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#seq).

## Hoare rule for nondeterministic choice

Nondeterministic choice is safe exactly when both branches are.

Formalized by `Cslib.PDL.Hoare.choice_iff`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#choice-iff).

## Hoare rule for formula tests

A formula test requires the postcondition only where the test passes.

Formalized by `Cslib.PDL.Hoare.test_iff`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#test-iff).

## Hoare invariant rule for iteration

A one-step invariant holds after every finite number of iterations,
including zero, via CSLib's canonical closure-preservation theorem.

Formalized by `Cslib.PDL.Hoare.star`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#star).

## Guarded while loop in PDL

A guarded loop in the existing PDL syntax: iterate guarded body
steps, then test that the guard is false.

Formalized by `Cslib.PDL.Program.whileDo`, a definition declared in [CSLibExt/Logics/PDL/Hoare.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#while-do).

## Hoare invariant rule for guarded while loops

The guarded-loop invariant rule is partial correctness, including
zero-step exits; it does not guarantee termination.

Formalized by `Cslib.PDL.Hoare.whileDo`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#while-do-2).

## While-loop rule with initialization and exit implication

Verify a guarded loop using initialization, invariant preservation,
and the exit implication to the desired postcondition.

Formalized by `Cslib.PDL.Hoare.whileDo_consequence`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#while-do-consequence).

## Semantic completeness of the while-loop invariant rule

The guarded-loop rule is semantically complete for arbitrary set
assertions. The witness is guarded-body reachability from `P`, independent
of `Q`; this is not a completeness claim for a syntactic assertion language.

Formalized by `Cslib.PDL.Hoare.whileDo_iff_exists_invariant`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#while-do-iff-exists-invariant).

## PDL induction restricted to reachable states

PDL induction restricted to states reachable from the initial world.
This proves `[a*]&#40;φ → [a]φ) → (φ → [a*]φ)` without assuming preservation
on unreachable states.

Formalized by `Cslib.PDL.sat_box_star_induction`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#sat-box-star-induction).

## Test absorption lifts through iteration

Concrete relational test absorption lifts through PDL iteration,
connecting the algebraic verification equation to closure invariance.

Formalized by `Cslib.PDL.test_mul_star_absorption`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#test-mul-star-absorption).

## Loop exit absorption from a guarded-body absorption equation

A guarded-body verification equation implies the loop's exit
verification equation over the same canonical relational carrier.

Formalized by `Cslib.PDL.test_mul_whileDo_absorption`, a theorem declared in [CSLibExt/Logics/PDL/Hoare.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/PDL/Hoare.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html#test-mul-while-do-absorption).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partial correctness and loop invariants for PDL](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/modal-logic/propositional-dynamic-logic/partial-correctness-and-loop-invariants-for-pdl)
