---
declaration: section
origin: cited
lean: Cslib.Language.LBABoundary, Cslib.Language.LBABoundary.ofHead, Cslib.Language.LBABoundary.ofHead_eq_both, Cslib.Language.LBABoundary.ofHead_eq_left, Cslib.Language.LBABoundary.ofHead_eq_right, Cslib.Language.LBABoundary.ofHead_eq_middle, Cslib.Language.LBAMove, Cslib.Language.LBAMove.moveHead
statement: formalized
proof: formalized
---

# Linear bounded automata

94 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html).

## Boundary tag of a linear bounded automaton head

Where the head sits relative to the tape boundaries: strictly inside
the tape, on the first cell, on the last cell, or on the only cell of a
one-cell tape. The transition function observes this tag, so the machine
can tell the two ends of its tape apart from interior cells.

Formalized by `Cslib.Language.LBABoundary`, an inductive type declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#lbaboundary).

## Boundary tag of a head position

The boundary tag of head position `h` on a tape of length `n`.

Formalized by `Cslib.Language.LBABoundary.ofHead`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#of-head).

## Boundary tag on a one-cell tape

The boundary tag at the head of a one-cell tape.

Formalized by `Cslib.Language.LBABoundary.ofHead_eq_both`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#of-head-eq-both).

## Boundary tag on the first cell of a longer tape

The boundary tag at the head of the first cell of a longer tape.

Formalized by `Cslib.Language.LBABoundary.ofHead_eq_left`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#of-head-eq-left).

## Boundary tag on the last cell of a longer tape

The boundary tag at the head of the last cell of a longer tape.

Formalized by `Cslib.Language.LBABoundary.ofHead_eq_right`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#of-head-eq-right).

## Boundary tag at an interior head position

The boundary tag at an interior head position.

Formalized by `Cslib.Language.LBABoundary.ofHead_eq_middle`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#of-head-eq-middle).

## Head move of a linear bounded automaton

A head move of a linear bounded automaton: left, stay, or right.

Formalized by `Cslib.Language.LBAMove`, an inductive type declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#lbamove).

## Head position after a move

The head position after a move: left decrements, stay keeps, right
increments.

Formalized by `Cslib.Language.LBAMove.moveHead`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#move-head).

## Legal head move of a linear bounded automaton

A move is legal from the head position `h` on a tape of length `n` when
the source head is on the tape and the new head position is still on the
tape. In particular a left move from an out-of-bounds head is illegal,
even though the truncated new head `h - 1` would still be out of bounds:
legality requires `h < n` for left moves as well.

Formalized by `Cslib.Language.LBAMove.legal`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#legal).

## Linear bounded automaton

A **linear bounded automaton**: a nondeterministic Turing machine whose
tape is the input word. The transition function gives, for a state, the
symbol under the head (`none` for a blank cell), and the boundary tag of
the head position, the finite set of possible next states, symbols to
write (`none` for a blank), and head moves. The boundary tag is what lets
the machine detect the ends of its tape: without it the model could not
recognize general context-sensitive languages. A move that would take
the head off the tape is not a step.

Formalized by `Cslib.Language.LinearBoundedAutomaton`, a structure declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#linear-bounded-automaton).

## Configuration of a linear bounded automaton

A configuration of a linear bounded automaton: the state, the tape
(a list of cells, one per input cell; `none` is a blank), and the head
position.

Formalized by `Cslib.Language.LBAConfig`, a structure declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#lbaconfig).

## Initial configuration of a linear bounded automaton

The initial configuration on the input `w`: the initial state, the tape
`w` itself (no blanks), the head on the first cell.

Formalized by `Cslib.Language.LinearBoundedAutomaton.initCfg`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#init-cfg).

## One step of a linear bounded automaton

One step of the machine: choose a transition for the current state,
the symbol under the head, and its boundary tag, write the symbol, move
the head legally. A step from a configuration whose head is off the
tape is impossible: legality requires the source head to be on the
tape.

Formalized by `Cslib.Language.LinearBoundedAutomaton.Step`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#step).

## Acceptance by a linear bounded automaton

`M` **accepts** `w` when some run from the initial configuration on `w`
reaches a configuration in the accepting state.

Formalized by `Cslib.Language.LinearBoundedAutomaton.Accepts`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#accepts).

## Language of a linear bounded automaton

The language of `M`: the words it accepts.

Formalized by `Cslib.Language.LinearBoundedAutomaton.language`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#language).

## Nonterminals of the grammar of a linear bounded automaton

The nonterminals of the grammar of an LBA: a cell, a generator, and the
start symbol. A cell records the original input symbol, the current tape
symbol, the head state if the head is on the cell, whether the cell is
active (simulation acts only on active cells), and the boundary tag of
its position (so simulation can apply the boundary-aware transitions).

Formalized by `Cslib.Language.LBANT`, an inductive type declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#lbant).

## Cell symbol of the LBA grammar

A grammar symbol for the LBA grammar: a cell as a nonterminal.

Formalized by `Cslib.Language.LinearBoundedAutomaton.cellSym`, an abbreviation declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#cell-sym).

## Start symbol of the LBA grammar

The start symbol as a grammar symbol.

Formalized by `Cslib.Language.LinearBoundedAutomaton.startSym`, an abbreviation declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#start-sym).

## Generator symbol of the LBA grammar

The generator as a grammar symbol.

Formalized by `Cslib.Language.LinearBoundedAutomaton.genSym`, an abbreviation declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#gen-sym).

## Terminal symbol of the LBA grammar

A terminal symbol of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.termSym`, an abbreviation declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#term-sym).

## Generation rules of the LBA grammar

The generation rules: the start symbol produces the first cell and the
generator (or, for a one-cell word, the first cell alone, tagged `both`);
the generator produces a middle non-head cell and itself, or a final
right non-head cell. The first cell of a longer word is tagged `left`.

Formalized by `Cslib.Language.LinearBoundedAutomaton.genRules`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#gen-rules).

## Activation rules of the LBA grammar

The activation rules: an inactive cell becomes active, keeping its
original, current, head state, and boundary tag.

Formalized by `Cslib.Language.LinearBoundedAutomaton.activateRules`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#activate-rules).

## Simulation rules for a stay move

The simulation rules for a stay move: the head cell rewrites its current
symbol and state, staying active, keeping its boundary tag.

Formalized by `Cslib.Language.LinearBoundedAutomaton.simStayRules`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#sim-stay-rules).

## Simulation rules for a right move

The simulation rules for a right move: the head cell rewrites its current
symbol and loses the head; the neighbouring cell gains the head. Both cells
keep their boundary tags.

Formalized by `Cslib.Language.LinearBoundedAutomaton.simRightRules`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#sim-right-rules).

## Simulation rules for a left move

The simulation rules for a left move: the neighbouring cell gains the head;
the head cell rewrites its current symbol and loses the head. Both cells
keep their boundary tags.

Formalized by `Cslib.Language.LinearBoundedAutomaton.simLeftRules`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#sim-left-rules).

## Conversion rules of the LBA grammar

The conversion rules: an active cell becomes its original terminal. The
head cell converts only in the accepting state, so a terminal word is
produced only from an accepting configuration. The boundary tag is
discarded on conversion.

Formalized by `Cslib.Language.LinearBoundedAutomaton.convRules`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#conv-rules).

## All rules of the LBA grammar

All the rules of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.allRules`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#all-rules).

## The grammar of an LBA

The grammar whose rules are the generation,
activation, simulation, and conversion rules above, starting from the start
symbol.

Formalized by `Cslib.Language.LinearBoundedAutomaton.lbaGrammar`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#lba-grammar).

## The start rule is a generation rule of the LBA grammar

The first generation rule is a rule of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_genRules_start`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-gen-rules-start).

## The grammar of an LBA is context-sensitive

Every production has a
nonterminal on its left side and does not shrink.

Formalized by `Cslib.Language.LinearBoundedAutomaton.lbaGrammar_contextSensitive`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#lba-grammar-context-sensitive).

## Cell tuples of an LBA configuration from an offset

The cells of a configuration, as a list of cell tuples: original symbol,
current symbol, head state, active, boundary tag. The head is given as
`some i` for the head position, or `none` once it has been passed. The
`start` index is the position of the first cell in the whole word and
`total` is the whole word's length, so the boundary tag of the cell at
offset `j` is `ofHead (start + j) total`.

Formalized by `Cslib.Language.LinearBoundedAutomaton.encodeCellsAux`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#encode-cells-aux).

## Cell tuple as a grammar symbol

A cell tuple as a grammar symbol.

Formalized by `Cslib.Language.LinearBoundedAutomaton.cellTupleSym`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#cell-tuple-sym).

## Configuration encoded as a sentential form

A configuration as a sentential form: the cells of its tape, with the
original symbols taken from the input word `w`.

Formalized by `Cslib.Language.LinearBoundedAutomaton.encodeCfg`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#encode-cfg).

## Middle generated cells of a word

The middle non-head generated cells of a word, inactive: the cells the
generator produces while the generator remains.

Formalized by `Cslib.Language.LinearBoundedAutomaton.tailCellsMid`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#tail-cells-mid).

## Tail generated cells of a word

The non-head generated cells of a word, inactive, as the tail of a
generated word: middle cells and a final right cell.

Formalized by `Cslib.Language.LinearBoundedAutomaton.tailCells`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#tail-cells).

## Generated cells of a word

The generated cells of a word, inactive, with the head state on the first
cell: the sentential form generation produces. The first cell is tagged
`both` for a one-cell word and `left` otherwise; the tail is `tailCells`.

Formalized by `Cslib.Language.LinearBoundedAutomaton.genCells`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#gen-cells).

## Generated sentential form of a word

The generated sentential form of a word.

Formalized by `Cslib.Language.LinearBoundedAutomaton.genEncode`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#gen-encode).

## Tail generated sentential form of a word

The non-head generated sentential form of a word.

Formalized by `Cslib.Language.LinearBoundedAutomaton.tailEncode`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#tail-encode).

## Middle generated sentential form of a word

The middle non-head generated sentential form of a word: every cell
tagged `middle`, for the generator's intermediate stage.

Formalized by `Cslib.Language.LinearBoundedAutomaton.tailEncodeMid`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#tail-encode-mid).

## Length of the cell-tuple encoding

The encoding has as many cells as the input word, when the tape has the
same length.

Formalized by `Cslib.Language.LinearBoundedAutomaton.length_encodeCellsAux`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 530](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L530). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#length-encode-cells-aux).

## Entries of the cell-tuple encoding

The `i`-th cell of the encoding: original `w[i]`, current `tape[i]`,
head state exactly at the head position, boundary tag of position
`start + i` in a word of length `total`.

Formalized by `Cslib.Language.LinearBoundedAutomaton.getElem_encodeCellsAux`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#get-elem-encode-cells-aux).

## Replacing a block by a rule is a derivation step

One grammar step replacing a block: if `u` splits as `p ++ lhs ++ q`
and `(lhs, rhs)` is a rule, then `u` derives `p ++ rhs ++ q`.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_replace_list`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-replace-list).

## Replacing a single cell is a derivation step

One grammar step replacing a single cell by a single cell.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_single_cell`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-single-cell).

## Replacing two consecutive cells is a derivation step

One grammar step replacing two consecutive cells.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_two_cells`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-two-cells).

## Singleton-to-singleton productions are derivation steps

A singleton-to-singleton production is a derivation step.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_singleton_cell`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 624](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L624). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-singleton-cell).

## Derivations extend by a left context

A derivation may be appended on the left.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_append_left`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-append-left).

## Derivations extend by a right context

A derivation may be appended on the right.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_append_right`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-append-right).

## Derivations compose under concatenation

Derivations compose under append.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_append`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 643](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L643). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-append).

## Transitivity of grammar derivations

Derivations are transitive.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_trans`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-trans).

## The first generation rule belongs to the LBA grammar

The first generation rule is a rule of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_gen_start`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-gen-start).

## The one-cell generation rule belongs to the LBA grammar

The one-cell generation rule is a rule of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_gen_single`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-gen-single).

## The generator step rule belongs to the LBA grammar

The generator step rule is a rule of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_gen_step`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 671](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L671). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-gen-step).

## The final generation rule belongs to the LBA grammar

The final generation rule is a rule of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_gen_last`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 678](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L678). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-gen-last).

## The activation rule belongs to the LBA grammar

The activation rule is a rule of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_activate`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-activate).

## Stay transitions give simulation rules

A stay transition gives a simulation rule.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_sim_stay`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-sim-stay).

## Right transitions give simulation rules

A right transition gives a simulation rule.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_sim_right`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-sim-right).

## Left transitions give simulation rules

A left transition gives a simulation rule.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_sim_left`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 724](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L724). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-sim-left).

## The accepting conversion rule belongs to the LBA grammar

The accepting conversion rule is a rule of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_conv_acc`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 741](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L741). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-conv-acc).

## The non-head conversion rule belongs to the LBA grammar

The non-head conversion rule is a rule of the grammar.

Formalized by `Cslib.Language.LinearBoundedAutomaton.mem_rule_conv_none`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 746](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L746). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mem-rule-conv-none).

## The generator derives the middle cells and itself

The generator derives the middle tail cells followed by itself.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_gen_tail`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 753](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L753). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-gen-tail).

## The generator derives the full tail of cells

The generator derives the tail cells, ending the generation.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_gen_tail_last`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 770](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L770). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-gen-tail-last).

## The start symbol derives the generated form of a word

The start symbol derives the generated sentential form of a word.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_start_genEncode`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-start-gen-encode).

## Tail cells derive their activated encoding

The tail cells, sitting at offset `start ≥ 1` in a word of total length
`start + w.length`, derive their activated encoding. The offset stays
`≥ 1` in the induction step, so the first tail cell is never tagged
`left`: it is `right` when it is the last cell and `middle` otherwise.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_tail_activate`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 817](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L817). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-tail-activate).

## Generated form derives the initial configuration encoding

The generated form derives the encoding of the initial configuration.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_gen_activate`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 859](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L859). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-gen-activate).

## Splitting a list at two consecutive positions

A list splits at two consecutive positions.

Formalized by `Cslib.Language.LinearBoundedAutomaton.take_append_two`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 901](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L901). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#take-append-two).

## Setting one list position by a production is a derivation step

A single-cell replacement that is a production is a derivation step.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_set_single`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 911](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L911). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-set-single).

## Dropping past an updated list position

Dropping past a set position is unaffected by the set.

Formalized by `Cslib.Language.LinearBoundedAutomaton.drop_set_of_gt`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 924](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L924). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#drop-set-of-gt).

## Taking past an updated list position

Taking past a set position keeps the new value at that position.

Formalized by `Cslib.Language.LinearBoundedAutomaton.take_set`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 936](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L936). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#take-set).

## Setting two adjacent list positions by a production is a derivation step

A two-cell replacement that is a production is a derivation step.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_set_two`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 948](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L948). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-set-two).

## Two-cell replacement at indices $i$ and $j = i + 1$

A two-cell replacement at positions `i` and `j = i + 1`.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_set_two'`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 971](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L971). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-set-two-2).

## Length of a configuration encoding

The encoding of a configuration has as many cells as the input word.

Formalized by `Cslib.Language.LinearBoundedAutomaton.length_encodeCfg`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 981](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L981). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#length-encode-cfg).

## Entries of a configuration encoding

The `i`-th cell of the encoding.

Formalized by `Cslib.Language.LinearBoundedAutomaton.getElem_encodeCfg`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 987](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L987). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#get-elem-encode-cfg).

## LBA steps preserve tape length

One step preserves the tape length.

Formalized by `Cslib.Language.LinearBoundedAutomaton.step_tape_length`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1013](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1013). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#step-tape-length).

## LBA steps keep the head on the tape

One step keeps the head on the tape, when the source head is on the tape.

Formalized by `Cslib.Language.LinearBoundedAutomaton.step_head_lt`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1019](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1019). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#step-head-lt).

## Reachable LBA configurations keep the tape length and the head on the tape

Reachable configurations have the input tape length and the head on the
tape, for a nonempty input word.

Formalized by `Cslib.Language.LinearBoundedAutomaton.reachable_tape_length`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1027](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1027). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#reachable-tape-length).

## An LBA step is a grammar derivation step on encodings

One machine step is one grammar derivation step on encodings.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_encodeCfg_step`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1045](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1045). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-encode-cfg-step).

## Head states in a configuration encoding

Every cell of an encoding has head state `none` or the given state.

Formalized by `Cslib.Language.LinearBoundedAutomaton.encodeCellsAux_state`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#encode-cells-aux-state).

## Every cell of a configuration encoding is active

Every cell of an encoding is active.

Formalized by `Cslib.Language.LinearBoundedAutomaton.encodeCellsAux_active`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#encode-cells-aux-active).

## Original symbols of an encoding are the input word

The original symbols of an encoding are the input word.

Formalized by `Cslib.Language.LinearBoundedAutomaton.map_orig_encodeCellsAux`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#map-orig-encode-cells-aux).

## Non-head or accepting cells convert to terminals

A list of cells, each non-head or accepting, converts to its original
terminals.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_convert_cells`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-convert-cells).

## Runs of an LBA give grammar derivations

Derivations along a run, keeping the tape length and head on the tape.

Formalized by `Cslib.Language.LinearBoundedAutomaton.derives_encodeCfg_reflTransGen`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#derives-encode-cfg-refl-trans-gen).

## If the LBA accepts a nonempty word, the grammar derives it

This is
one inclusion of the LBA-to-grammar direction.

Formalized by `Cslib.Language.LinearBoundedAutomaton.lba_accepts_implies_grammar_derives`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/LBA.lean, line 1401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextSensitive/LBA.lean#L1401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#lba-accepts-implies-grammar-derives).

## Space-bounded single-tape machines

Let $s : \mathbb{N} \to \mathbb{N}$. A single-tape
Turing machine $M$ runs in space $s$ when, for every input word $l$ of length $|l|$, every
configuration reachable from the initial configuration of $M$ on $l$ uses at most $s(|l|)$
cells, whether or not the run halts. The cells used by a configuration are the head cell
together with the cells on each side of it up to the outermost non-blank cell.

Formalized by `Cslib.Turing.SingleTapeTM.SpaceBoundedBy`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#space-bounded-by).

## Linear bounded automaton

A single-tape machine is a linear bounded automaton when it runs
in space $n + 1$ on inputs of length $n$: every configuration of its run on an input of length $n$
uses at most $n + 1$ cells, whether or not the run halts.

The input itself uses $\max(1, n)$ cells, and the extra cell lets the head step onto a blank cell
next to the input, the analogue of Sipser's endmarkers. With the bound $n$ instead, no machine
would qualify, since the empty input already uses one cell.

Formalized by `Cslib.Turing.SingleTapeTM.IsLBA`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#is-lba).

## Space bounds can be weakened

If a single-tape machine runs in space
$s : \mathbb{N} \to \mathbb{N}$ and $s' : \mathbb{N} \to \mathbb{N}$ satisfies $s(n) \le s'(n)$ for
every $n \in \mathbb{N}$, then it runs in space $s'$.

Formalized by `Cslib.Turing.SingleTapeTM.SpaceBoundedBy.mono`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#mono).

## A space bound is at least the space of the input

If a single-tape machine runs in space
$s : \mathbb{N} \to \mathbb{N}$, then $\max(1, n) \le s(n)$ for the length $n$ of every input word,
since the initial configuration on an input of length $n$ uses $\max(1, n)$ cells.

Formalized by `Cslib.Turing.SingleTapeTM.SpaceBoundedBy.max_one_le`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#max-one-le).

## A machine that, on a blank cell, writes a blank and does not move is a linear bounded automaton

**A machine that, on a blank cell, writes a blank and does not move is a linear bounded
automaton.** Its head never leaves a blank cell, so it stays on the input or on the two blank
cells next to it, and it writes non-blank symbols only on the input. The machine may change state
on a blank cell, or halt there.

Formalized by `Cslib.Turing.SingleTapeTM.isLBA_of_stays_on_blank`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#is-lba-of-stays-on-blank).

## Configuration bound

For a single-tape machine with state set $Q$ over a finite alphabet
$\Sigma$ and $k \in \mathbb{N}$, the configuration bound at $k$ is the number
$(|Q| + 1)(|\Sigma| + 1)(|\Sigma| + 2)^{2k}$.

A configuration that uses at most $k$ cells is determined by a state or the halting state, the
symbol or blank under the head, and the first $k$ cells to either side of the head, each a symbol,
a blank, or past the last non-blank cell; so this number bounds how many such configurations
there are.

Formalized by `Cslib.Turing.SingleTapeTM.cfgBound`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#cfg-bound).

## Configurations of bounded space are finitely many

Let $M$ be a single-tape machine with
state set $Q$ over a finite alphabet $\Sigma$, where a configuration uses the cell under the head
and the cells on either side of it up to the last non-blank one. For every $k \in \mathbb{N}$, at
most $(|Q| + 1)(|\Sigma| + 1)(|\Sigma| + 2)^{2k}$ configurations of $M$ use at most $k$ cells.

Formalized by `Cslib.Turing.SingleTapeTM.encard_le_cfgBound`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#encard-le-cfg-bound).

## Space-bounded machines halt within the configuration bound

Let $M$ be a single-tape
machine with state set $Q$ over a finite alphabet $\Sigma$ that runs in space
$s : \mathbb{N} \to \mathbb{N}$. If $M$ halts on an input word $w$ of length $n$, then from the
initial configuration on $w$ it reaches a configuration in the halting state in at most
$(|Q| + 1)(|\Sigma| + 1)(|\Sigma| + 2)^{2 s(n)}$ steps.

Its run visits only configurations of space at most $s(n)$, and does not repeat one before
halting.

Formalized by `Cslib.Turing.SingleTapeTM.SpaceBoundedBy.exists_halted_relatesWithinSteps`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#exists-halted-relates-within-steps).

## Halting of a machine running in computable space is computable

Let $M$ be a single-tape
machine with state set $Q$ over a finite alphabet $\Sigma$, fix any primitive recursive coding of
$\Sigma$, and let $s : \mathbb{N} \to \mathbb{N}$ be computable. If $M$ runs in space $s$, then the
set of input words over $\Sigma$ on which $M$ halts is computable.

The decision procedure runs $M$ for $(|Q| + 1)(|\Sigma| + 1)(|\Sigma| + 2)^{2 s(n)}$ steps on an
input of length $n$ and checks whether it has halted.

Formalized by `Cslib.Turing.SingleTapeTM.SpaceBoundedBy.computablePred_haltsOn`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#computable-pred-halts-on).

## Halting of a linear bounded automaton is decidable

Let $M$ be a single-tape machine over
a finite alphabet $\Sigma$, and fix any primitive recursive coding of $\Sigma$. If $M$ is a linear
bounded automaton, then the set of input words over $\Sigma$ on which $M$ halts is computable.

## Sources

- Sipser, *Introduction to the Theory of Computation*, Theorem 5.9, of which this is a fixed-machine halting analogue: Sipser decides acceptance uniformly over machine descriptions, which needs a code type for CSLib machines.

Formalized by `Cslib.Turing.SingleTapeTM.IsLBA.computablePred_haltsOn`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#computable-pred-halts-on-2).

## Halting of a linear bounded automaton on binary codes is decidable

Let $M$ be a
single-tape machine over a finite alphabet $\Sigma$ that is a linear bounded automaton, let
$\alpha$ be a primitive recursively coded type, and let $\iota : \{0, 1\} \to \Sigma$ be any map.
For $a \in \alpha$, let $w_a$ be the word over $\Sigma$ obtained by applying $\iota$ to each bit of
the binary expansion, least significant bit first and without leading zeros, of the
natural-number code of $a$; so $w_a$ is empty when that code is $0$. Then the set of
$a \in \alpha$ such that $M$ halts on $w_a$ is computable.

Formalized by `Cslib.Turing.SingleTapeTM.IsLBA.computablePred_haltsOn_encodeNat`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#computable-pred-halts-on-encode-nat).

## A single-tape machine decides the halting problem of a linear bounded automaton

Let $M$
be a linear bounded automaton over a finite tape alphabet $\Sigma$, let $\iota$ be any map from
the Booleans to $\Sigma$, and let $\alpha$ be a primitively encodable type. For $a \in \alpha$, let
$w_a$ be the word obtained by writing, letter by letter through $\iota$, the binary expansion
(least significant bit first) of the natural-number code of $a$. Then the predicate on $\alpha$
that holds at $a$ exactly when $M$ halts on the input $w_a$ is decidable by a single-tape
machine.

Formalized by `Cslib.Turing.SingleTapeTM.IsLBA.singleTapeDecidable_haltsOn_encodeNat`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/SpaceBounded.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html#single-tape-decidable-halts-on-encode-na).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear bounded automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-sensitive-languages/linear-bounded-automata)
