---
declaration: section
origin: cited
lean: Cslib.AutomatedReasoning.StringConstraints.BlockSym, Cslib.AutomatedReasoning.StringConstraints.dominoLetter, Cslib.AutomatedReasoning.StringConstraints.topFun, Cslib.AutomatedReasoning.StringConstraints.botFun, Cslib.AutomatedReasoning.StringConstraints.dominoRegex, Cslib.AutomatedReasoning.StringConstraints.pcpConstraint, Cslib.AutomatedReasoning.StringConstraints.blockDomino, Cslib.AutomatedReasoning.StringConstraints.mem_sum_matches
statement: formalized
proof: formalized
---

# PCP characterization of a string-constraint family

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html).

## Alphabet for the PCP encoding

The alphabet for the PCP encoding: dominoes (as index letters) and
plain letters.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.BlockSym`, an abbreviation declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#block-sym).

## Domino as an index letter

A domino as an index letter.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.dominoLetter`, an abbreviation declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#domino-letter).

## Top morphism of the PCP encoding

The top morphism: a domino letter maps to its top word as plain
letters; plain letters map to `[]` (they never occur in an index word).

Formalized by `Cslib.AutomatedReasoning.StringConstraints.topFun`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#top-fun).

## Bottom morphism of the PCP encoding

The bottom morphism.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.botFun`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#bot-fun).

## Regular language of domino index words

The regular language of index words: concatenations of domino
letters.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.dominoRegex`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#domino-regex).

## PCP encoding as a one-variable string constraint

The PCP encoding as a string constraint over one variable.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.pcpConstraint`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#pcp-constraint).

## Domino named by a one-letter block

The domino named by a one-letter block; junk `([], [])` otherwise.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.blockDomino`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#block-domino).

## Membership in a sum of regular expressions

Membership in a sum of regular expressions.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.mem_sum_matches`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#mem-sum-matches).

## Membership in the domino index-word language

Membership in the index-word language: the word is a concatenation
of domino letters.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.mem_dominoRegex`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#mem-domino-regex).

## Membership atom of the PCP encoding checks index words

The membership atom of the encoding checks index-word membership.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.sat_mem_dominoRegex`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#sat-mem-domino-regex).

## Top morphism applied to an index word

The top morphism applied to an index word.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.flatMap_topFun`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#flat-map-top-fun).

## Bottom morphism applied to an index word

The bottom morphism applied to an index word.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.flatMap_botFun`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#flat-map-bot-fun).

## Flattening a list of one-letter blocks

Flattening a list of one-letter blocks.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.map_inl_flatten`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#map-inl-flatten).

## PCP is characterized by string-constraint satisfiability:

For each
PCP instance `P`, `PCP P` holds iff the encoding constraint is satisfiable.
This is a semantic characterization, not a computable reduction to a
formula-indexed satisfiability predicate (see the module header).

Formalized by `Cslib.AutomatedReasoning.StringConstraints.pcp_iff_stringSat`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/PCPCharacterization.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html#pcp-iff-string-sat).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: PCP characterization of a string-constraint family](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/pcp-characterization-of-a-string-constraint-fami)
