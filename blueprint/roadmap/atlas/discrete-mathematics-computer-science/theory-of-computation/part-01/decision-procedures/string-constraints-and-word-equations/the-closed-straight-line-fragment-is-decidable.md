---
declaration: section
origin: cited
lean: Cslib.AutomatedReasoning.StringConstraints.SLSys, Cslib.AutomatedReasoning.StringConstraints.Acyclic, Cslib.AutomatedReasoning.StringConstraints.SLSat, Cslib.AutomatedReasoning.StringConstraints.slStep, Cslib.AutomatedReasoning.StringConstraints.values, Cslib.AutomatedReasoning.StringConstraints.sol, Cslib.AutomatedReasoning.StringConstraints.getD_eq_of_lt, Cslib.AutomatedReasoning.StringConstraints.foldl_take
statement: formalized
proof: formalized
---

# The closed straight-line fragment is decidable

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html).

## Closed straight-line system

A **closed straight-line system**: one defining term per variable, plus a
query formula. The definition at position `k` is the definition of
variable `k`. There are no free input variables: every variable the
system talks about must be defined by the system itself.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.SLSys`, a structure declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#slsys).

## Acyclic closed straight-line system

A closed straight-line system is **acyclic** when every defining term
mentions only earlier variables, and the query mentions only defined
variables. Hence every variable occurring anywhere in the system is
defined, and unfolding the definitions terminates at ground terms:
there is no free input variable.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.Acyclic`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#acyclic).

## Satisfaction of a closed straight-line system

Satisfaction of a closed straight-line system: the assignment obeys every
definition and satisfies the query.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.SLSat`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#slsat).

## One fold step of straight-line evaluation

One fold step: evaluate the next defining term under the values
computed so far and append the result.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.slStep`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#sl-step).

## Folded assignment values of a straight-line system

The folded assignment values, in variable order.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.values`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#values).

## Candidate assignment of a straight-line system

The candidate assignment of a straight-line system.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.sol`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#sol).

## In-bounds lookup with default equals indexed access

Lookup with a proof of the bound is the `getElem` value.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.getD_eq_of_lt`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#get-d-eq-of-lt).

## Straight-line fold preserves its initial segment

The fold preserves its initial segment.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.foldl_take`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#foldl-take).

## Straight-line fold appends one value per definition

The fold appends exactly one value per definition.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.foldl_length`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#foldl-length).

## Folded values have one entry per definition

Length of the folded values: one per definition.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.values_length`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#values-length).

## Lookup in a taken prefix agrees with the whole list

Lookup in a taken prefix agrees with lookup in the whole list.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.getD_take_of_lt`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#get-d-take-of-lt).

## Lookup in an appended list below the prefix length

Lookup in an appended list agrees with lookup below the prefix length.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.getD_append_of_lt`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#get-d-append-of-lt).

## Lookup in a folded list below the starting length

Lookup in a folded list agrees with lookup in the starting list
below its length.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.getD_foldl_of_lt`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#get-d-foldl-of-lt).

## Defining equation for the folded values

The defining equation for the folded values: the value at position
`acc.length + k` is the `k`-th defining term evaluated under the
folded values. The variable condition says the term only looks at
positions below `acc.length + k`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.foldl_getD`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#foldl-get-d).

## Candidate assignment satisfies every definition

The candidate assignment satisfies every definition.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.sol_satisfies_defs`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#sol-satisfies-defs).

## Satisfying assignments agree with the candidate on defined variables

Any satisfying assignment agrees with the candidate on defined
variables.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.eq_sol_of_sat`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#eq-sol-of-sat).

## Straight-line satisfiability iff the query holds on the candidate

Satisfiability of a closed straight-line system is equivalent to the query
holding on the candidate assignment.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.exists_sat_iff_sat_sol`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#exists-sat-iff-sat-sol).

## Satisfiability of a closed acyclic straight-line system is decidable

The decision procedure checks the query on the unique ground assignment;
it does not search over free inputs, because the closed fragment has none.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.decidableExistsSatOfAcyclic`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/StraightLine.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html#decidable-exists-sat-of-acyclic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The closed straight-line fragment is decidable](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/the-closed-straight-line-fragment-is-decidable)
