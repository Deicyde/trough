---
declaration: section
origin: cited
lean: Cslib.Language.Yields.terminal_not_mem, Cslib.Language.EncodedCFG.noTerminals, Cslib.Language.EncodedCFG.nullable, Cslib.Language.EncodedCFG.yields_noTerminals, Cslib.Language.EncodedCFG.eq_nil_of_yields_noTerminals, Cslib.Language.EncodedCFG.yields_of_yields_noTerminals, Cslib.Language.EncodedCFG.mem_nullable_iff, Cslib.Language.EncodedCFG.deletions
statement: formalized
proof: formalized
---

# Computable reduction of context-free grammars

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html).

## A form yielding the empty word contains no terminal

Let $G$ be a context-free grammar
over terminals $T$ and let $\alpha$ be a sentential form of $G$. If $\alpha$ yields the empty
word in $G$, then no terminal symbol $a \in T$ occurs in $\alpha$.

Formalized by `Cslib.Language.Yields.terminal_not_mem`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#terminal-not-mem).

## Productions without terminals of an encoded grammar

For an encoded context-free grammar
$g$, the encoded grammar with the same start nonterminal whose productions are the productions
of $g$, in their order, whose right-hand sides contain no terminal.

Formalized by `Cslib.Language.EncodedCFG.noTerminals`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#no-terminals).

## Computed nullable nonterminals of an encoded grammar

For an encoded context-free grammar
$g$, the list of generating nonterminals of the encoded grammar that has the start nonterminal
of $g$ and, as productions, the productions of $g$ whose right-hand sides contain no terminal.

A nonterminal is in this list exactly when it derives the empty word in the grammar denoted by
$g$.

Formalized by `Cslib.Language.EncodedCFG.nullable`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#nullable).

## Yields of the empty word need only terminal-free productions

Let $g$ be an encoded
context-free grammar and $\alpha$ a sentential form of the grammar $g$ denotes. If $\alpha$ yields
the empty word in that grammar, then $\alpha$ also yields the empty word in the grammar denoted by
the encoded grammar consisting of the productions of $g$ that contain no terminal.

Formalized by `Cslib.Language.EncodedCFG.yields_noTerminals`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#yields-no-terminals).

## Terminal-free productions yield only the empty word

Let $g$ be an encoded context-free
grammar and consider the grammar of its productions without terminals. If a sentential form
$\alpha$ that contains no terminal yields a word $w$ in that grammar, then $w$ is the empty
word.

Formalized by `Cslib.Language.EncodedCFG.eq_nil_of_yields_noTerminals`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#eq-nil-of-yields-no-terminals).

## Yields in the terminal-free subgrammar are yields of the grammar

Let $g$ be an encoded
context-free grammar, $\alpha$ a sentential form and $w$ a word. If $\alpha$ yields $w$ in the
grammar denoted by the encoded grammar consisting of the productions of $g$ that contain no
terminal, then $\alpha$ yields $w$ in the grammar $g$ denotes.

Formalized by `Cslib.Language.EncodedCFG.yields_of_yields_noTerminals`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#yields-of-yields-no-terminals).

## The nullable nonterminals are computed

For every encoded context-free grammar $g$ and
every natural number $A$, $A$ belongs to the computed list of nullable nonterminals of $g$ (the
generating nonterminals of the productions of $g$ without terminals) if and only if $A$ is
nullable in the grammar denoted by $g$, that is, $A$ derives the empty word.

Formalized by `Cslib.Language.EncodedCFG.mem_nullable_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#mem-nullable-iff).

## Deleting nonterminals from an encoded right-hand side

Let $N$ be a list of natural
numbers and $u$ an encoded right-hand side, that is, a word whose letters are nonterminals
$i \in \mathbb{N}$ or terminals. The result is the list of all words obtained from $u$ by
deleting some of the occurrences of nonterminals that belong to $N$ (possibly none, possibly
all) and keeping every other letter in order; each choice of deleted occurrences contributes one
entry of the list.

Formalized by `Cslib.Language.EncodedCFG.deletions`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#deletions).

## Computed deletions agree with nullable deletions

Let $g$ be an encoded context-free
grammar. For every encoded word $u$ and every sentential form $\alpha$ of the grammar denoted by
$g$, $\alpha$ is obtained from the decoding of $u$ by deleting some occurrences of nullable
nonterminals of the grammar denoted by $g$ if and only if $\alpha$ is the decoding of a word
obtained from $u$ by deleting some occurrences of nonterminals in the computed list of nullable
nonterminals of $g$.

Formalized by `Cslib.Language.EncodedCFG.mem_nullableDeletions_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#mem-nullable-deletions-iff).

## Removing empty productions from an encoded grammar

For an encoded context-free grammar
$g$, the encoded grammar with the same start nonterminal whose productions are, for each
production $A \to u$ of $g$, the productions $A \to v$ for every nonempty word $v$ obtained from
$u$ by deleting some occurrences of nonterminals in the computed list of nullable nonterminals of
$g$.

Formalized by `Cslib.Language.EncodedCFG.epsElim`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#eps-elim).

## Productions of the computable removal of empty productions

For every encoded context-free
grammar $g$, a production is a production of the grammar denoted by the encoded grammar obtained
from $g$ by removing empty productions if and only if it is a production of the grammar obtained
from the grammar denoted by $g$ by eliminating empty productions.

Formalized by `Cslib.Language.EncodedCFG.mem_epsElim_rules`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#mem-eps-elim-rules).

## Computable removal of empty productions agrees with the classical one

For every encoded
context-free grammar $g$, the grammar denoted by the encoded grammar obtained from $g$ by removing
empty productions is equal to the grammar obtained from the grammar denoted by $g$ by eliminating
empty productions: from each production, all productions obtained by deleting some occurrences of
nullable nonterminals from its output, except those with empty output.

Formalized by `Cslib.Language.EncodedCFG.epsElim_toCFG`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#eps-elim-to-cfg).

## Removing empty productions drops only the empty word

For every encoded context-free
grammar $g$, the language of the encoded grammar obtained from $g$ by removing empty productions
consists of the nonempty words of the language of $g$.

Formalized by `Cslib.Language.EncodedCFG.language_epsElim`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#language-eps-elim).

## Nonterminals of an encoded grammar

For an encoded context-free grammar $g$, the list
obtained by duplicate removal from the list made of the start nonterminal of $g$ followed, for
each production of $g$ in order, by its left-hand side and then the nonterminals of its
right-hand side in order. It lists without repetitions the nonterminals that $g$ mentions.

Formalized by `Cslib.Language.EncodedCFG.ntList`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#nt-list).

## Target of a unit right-hand side

For an encoded right-hand side $u$, a list whose entries
are nonterminals $i \in \mathbb{N}$ or terminals, the optional value is $B$ when $u$ consists of
the single nonterminal $B$, and there is no value otherwise.

Formalized by `Cslib.Language.EncodedCFG.unitTarget`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#unit-target).

## One round of unit reachability

For an encoded context-free grammar $g$, a natural number
$A$ and a list $S$ of natural numbers, the list consisting of $A$ followed, for each production of
$g$ in order whose left-hand side lies in $S$ and whose right-hand side is a single nonterminal
$B$, by that nonterminal $B$.

Formalized by `Cslib.Language.EncodedCFG.unitStep`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#unit-step).

## Nonterminals reachable by unit productions in an encoded grammar

For an encoded
context-free grammar $g$ and a natural number $A$, let $n$ be the number of distinct nonterminals
mentioned in $g$ (the start, the left-hand sides, and the nonterminals on right-hand sides). The
list is obtained from the empty list by applying one round of unit reachability from $A$
exactly $n + 1$ times.

Its entries are exactly the nonterminals $B$ reachable from $A$ by a possibly empty chain of
unit productions $A \to \dots \to B$ of $g$; in particular $A$ itself is an entry.

Formalized by `Cslib.Language.EncodedCFG.unitReach`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#unit-reach).

## Unit reachability is computed

Let $g$ be an encoded context-free grammar and let $A$ and
$B$ be natural numbers. Then $B$ belongs to the computed list of nonterminals reachable from $A$
by unit productions of $g$ if and only if there are $k \ge 0$ and nonterminals
$A = C_0, C_1, \dots, C_k = B$ such that $C_{i-1} \to C_i$ is a production of the grammar denoted
by $g$ for every $i$ with $1 \le i \le k$.

Formalized by `Cslib.Language.EncodedCFG.mem_unitReach_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#mem-unit-reach-iff).

## Unit elimination for encoded grammars

For an encoded context-free grammar $g$, the
encoded grammar with the start nonterminal of $g$ whose productions are listed as follows: for
each nonterminal $A$ in the list of nonterminals of $g$, and for each production $B \to u$ of $g$
in order such that $B$ is in the computed list of nonterminals reachable from $A$ by unit
productions and $u$ is not a single nonterminal, the production $A \to u$.

Formalized by `Cslib.Language.EncodedCFG.unitElim`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#unit-elim).

## Productions of the encoded unit elimination

Let $g$ be an encoded context-free grammar
over terminals $T$ and let $r$ be a production with terminals in $T$ and nonterminals in
$\mathbb{N}$. Then $r$ is a production of the grammar denoted by the encoded unit elimination of
$g$ if and only if $r$ is a production of the grammar obtained from the grammar denoted by $g$ by
eliminating unit productions.

Formalized by `Cslib.Language.EncodedCFG.mem_unitElim_rules`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#mem-unit-elim-rules).

## The encoded unit elimination denotes the unit-eliminated grammar

For every encoded
context-free grammar $g$, the grammar denoted by the encoded unit elimination of $g$ is equal to
the grammar obtained from the grammar denoted by $g$ by eliminating unit productions.

Formalized by `Cslib.Language.EncodedCFG.unitElim_toCFG`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#unit-elim-to-cfg).

## Reduction of an encoded grammar

For an encoded context-free grammar $g$, the encoded
grammar obtained by first removing the empty productions of $g$ (encoded
$\varepsilon$-elimination) and then removing the unit productions of the result (encoded unit
elimination).

Formalized by `Cslib.Language.EncodedCFG.reduce`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#reduce).

## The reduced grammar generates the language minus the empty word

For every encoded
context-free grammar $g$, the language of the reduction of $g$ (empty productions removed, then
unit productions removed) consists of the nonempty words of the language of $g$.

Formalized by `Cslib.Language.EncodedCFG.language_reduce`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#language-reduce).

## The reduced grammar has no empty and no unit productions

For every encoded context-free
grammar $g$, every production of the grammar denoted by the reduction of $g$ (empty productions
removed, then unit productions removed) has a nonempty output, and that output is not a single
nonterminal.

Formalized by `Cslib.Language.EncodedCFG.isReduced_reduce`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#is-reduced-reduce).

## Reduction is primitive recursive

Let $T$ be a type of terminals with a primitive
recursive encoding. The map sending an encoded context-free grammar $g$ over $T$ to its
reduction, the encoded grammar obtained from $g$ by removing empty productions and then unit
productions, is primitive recursive, where encoded grammars are encoded as pairs of a start
nonterminal and a list of productions.

Formalized by `Cslib.Language.EncodedCFG.primrec_reduce`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/EncodedReduced.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html#primrec-reduce).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Computable reduction of context-free grammars](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/computable-reduction-of-context-free-grammars)
