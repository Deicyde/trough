---
declaration: section
origin: cited
lean: Cslib.AutomatedReasoning.StringConstraints.map_fst_map_pair, Cslib.AutomatedReasoning.StringConstraints.wordsOfLength, Cslib.AutomatedReasoning.StringConstraints.mem_wordsOfLength, Cslib.AutomatedReasoning.StringConstraints.wordsOfLength_length, Cslib.AutomatedReasoning.StringConstraints.wordsUpToCount, Cslib.AutomatedReasoning.StringConstraints.wordsUpTo, Cslib.AutomatedReasoning.StringConstraints.nil_mem_wordsUpTo, Cslib.AutomatedReasoning.StringConstraints.mem_wordsUpTo
statement: formalized
proof: formalized
---

# Bounded string constraints: finite-search specification

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html).

## Keys of the association list built from an assignment

The keys of the association list built from an assignment are the
variables themselves.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.map_fst_map_pair`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#map-fst-map-pair).

## Words of a given length over a finite alphabet

All words of length exactly `n` over a finite alphabet, each occurring
once: each step extends only the words of the previous length, never the
whole `wordsUpTo` enumeration, so no word is duplicated.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.wordsOfLength`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#words-of-length).

## Membership in the exact-length word enumeration

Membership in the exact-length enumeration is exactly the length
equality.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.mem_wordsOfLength`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#mem-words-of-length).

## Size of the exact-length word enumeration

Counting the exact-length enumeration: `|Σ| ^ n` words.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.wordsOfLength_length`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#words-of-length-length).

## Number of words of length at most $B$

The number of words of length at most `B`: `∑_{n ≤ B} |Σ| ^ n`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.wordsUpToCount`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#words-up-to-count).

## Words of length at most $B$ over a finite alphabet

All words of length at most `B` over a finite alphabet, each occurring
once: the concatenation of the exact-length layers `0, …, B`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.wordsUpTo`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#words-up-to).

## Empty word is in every bounded enumeration

The empty word is enumerated at every bound.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.nil_mem_wordsUpTo`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#nil-mem-words-up-to).

## Membership in the bounded-length word enumeration

Membership in the enumeration is exactly the length bound.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.mem_wordsUpTo`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#mem-words-up-to).

## Sum of a constant over a list

Summing a constant over a list.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.sum_map_const`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#sum-map-const).

## Size of the bounded-length word enumeration

Counting the enumeration: `∑_{n ≤ B} |Σ| ^ n` words, the number of
distinct words of length at most `B`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.wordsUpTo_length`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#words-up-to-length).

## Association-list lookup defaulting to the empty word

Lookup in an association list; unbound variables read as `[]`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.getVal`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#get-val).

## Lookup inherits the length bound on values

A lookup returns one of the values in the list, so it inherits the
length bound on values.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.getVal_length_le`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#get-val-length-le).

## Lookup recovers the assignment from its association list

Lookup in the association list built from an assignment returns the
assignment.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.getVal_map`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#get-val-map).

## Enumeration of bounded assignments as association lists

All assignments of the variables in `vs` to words of length at most
`B`, as association lists, each occurring once (as in `wordsUpTo`).

Formalized by `Cslib.AutomatedReasoning.StringConstraints.assignLists`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#assign-lists).

## Membership in the bounded assignment enumeration

Membership in the assignment enumeration: the keys are exactly `vs`
and every value has length at most `B`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.mem_assignLists`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#mem-assign-lists).

## Size of the bounded assignment enumeration

Counting the assignment enumeration: the total (worst-case) size of
the candidate search space is `(wordsUpToCount B) ^ |vs|`. This counts
enumerated association lists; see the cost model in the module header
for when it coincides with the number of distinct assignments.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.assignLists_length`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#assign-lists-length).

## Enumerated lists over distinct variables are recovered from lookups

Under `vs.Nodup`, an enumerated association list is recovered from its
lookup function: there is no duplicate key for `getVal` to shadow, so
the list is exactly the association list built from its own lookups.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.assignLists_eq_map_getVal`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#assign-lists-eq-map-get-val).

## Enumerated lists over distinct variables give distinct assignments

Under `vs.Nodup`, distinct enumerated association lists denote
distinct assignments: if two enumerated lists agree as lookup functions
on `vs`, they are the same list. Without `Nodup` this fails, since a
duplicate key lets a later entry be shadowed by an earlier one.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.assignLists_getVal_injective`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#assign-lists-get-val-injective).

## Bounded-search satisfiability specification

The bounded-search specification: enumerate bounded assignments and
check `φ` on each one. This is a classical specification, not an
executable decision procedure: `assignLists` is `noncomputable`, so
this Boolean cannot be evaluated by `decide`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.boundedSatSpec`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#bounded-sat-spec).

## Soundness and completeness of the bounded-search specification

Soundness and completeness of the bounded-search specification: it
reports `true` exactly when `φ` has a solution whose values on `vs`
have length at most `B`. The hypothesis is that `vs` covers the
variables of `φ`.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.boundedSatSpec_iff`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Bounded.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html#bounded-sat-spec-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounded string constraints: finite-search specification](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/bounded-string-constraints-finite-search-specifi)
