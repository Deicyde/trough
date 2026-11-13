---
declaration: section
origin: cited
lean: Cslib.Decidability.Grammar.ambGrammar, Cslib.Decidability.Grammar.canon, Cslib.Decidability.Grammar.cases_of_mem_ambGrammar_of_input, Cslib.Decidability.Grammar.eq_canon_of_leftDerivation, Cslib.Decidability.Grammar.leftDerivation_canon, Cslib.Decidability.Grammar.startRule, Cslib.Decidability.Grammar.cases_of_leftDerivation_start, Cslib.Decidability.Grammar.leftDerivation_start
statement: formalized
proof: formalized
---

# Ambiguity problem for context-free grammars

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html).

## The ambiguity grammar of a PCP instance

Let $P = [(t_0, b_0), \dots, (t_{m-1}, b_{m-1})]$
be a list of dominoes over an alphabet $\alpha$, with top words $t_i$ and bottom words $b_i$. The
ambiguity grammar of $P$ is the encoded context-free grammar over the terminals
$\alpha \sqcup \mathbb{N}$ (letters and indices) with nonterminals $S = 0$, $A = 1$, $B = 2$, start
symbol $S$, and the productions $S \to A$ and $S \to B$ together with, for every $i < m$, the
productions $A \to t_i\, A\, i$, $A \to t_i\, i$, $B \to b_i\, B\, i$ and $B \to b_i\, i$, in which
the index $i$ is a terminal.

Formalized by `Cslib.Decidability.Grammar.ambGrammar`, a definition declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#amb-grammar).

## The canonical rule sequence along an index sequence

Let $P$ be a list of dominoes over
$\alpha$, let $\sigma$ assign a word over $\alpha$ to each domino, let $A$ be a natural number,
and for $i \in \mathbb{N}$ write $w_i$ for $\sigma$ applied to the $i$-th domino of $P$ (the domino
with both words empty when $i$ is past the end of $P$). For a sequence $i_1, \dots, i_n$ of
natural numbers, this is the list of productions, with terminals $\alpha \sqcup \mathbb{N}$ and
nonterminals $\mathbb{N}$, consisting of $A \to w_{i_k}\, A\, i_k$ for $k = 1, \dots, n - 1$ in
order, followed by $A \to w_{i_n}\, i_n$, where the letters of $w_{i_k}$ and the index $i_k$ are
terminals and $A$ is a nonterminal; the empty sequence gives the empty list.

Formalized by `Cslib.Decidability.Grammar.canon`, a definition declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#canon).

## The productions of $A$ and $B$ in the ambiguity grammar

Let
$P = [(t_0, b_0), \dots, (t_{m-1}, b_{m-1})]$ be a list of dominoes, and let $A$, $B$ be the
nonterminals of the ambiguity grammar of $P$ for its top and bottom words. Every production of
that grammar with left-hand side $A$ is $A \to t_i\, A\, i$ or $A \to t_i\, i$ for some $i < m$,
and every production with left-hand side $B$ is $B \to b_i\, B\, i$ or $B \to b_i\, i$ for some
$i < m$.

Formalized by `Cslib.Decidability.Grammar.cases_of_mem_ambGrammar_of_input`, a theorem declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#cases-of-mem-amb-grammar-of-input).

## Leftmost derivations from $A$ and $B$ follow an index sequence

Let
$P = [(t_0, b_0), \dots, (t_{m-1}, b_{m-1})]$ be a list of dominoes, let $A$, $B$ be the
nonterminals of the ambiguity grammar of $P$ for its top and bottom words, and let $u$, $v$ be
words of terminals. Every leftmost derivation of a word $w$ from the sentential form $u\,A\,v$ is
the canonical rule sequence from $A$ for the words $t_i$ along some nonempty sequence
$i_1, \dots, i_n$ of indices less than $m$, and
$w = u\, t_{i_1} \cdots t_{i_n}\, i_n \cdots i_1\, v$. Likewise, every leftmost derivation of $w$
from $u\,B\,v$ is the canonical rule sequence from $B$ for the words $b_i$ along such a sequence,
and $w = u\, b_{i_1} \cdots b_{i_n}\, i_n \cdots i_1\, v$.

Formalized by `Cslib.Decidability.Grammar.eq_canon_of_leftDerivation`, a theorem declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#eq-canon-of-left-derivation).

## The leftmost derivation along an index sequence

Let
$P = [(t_0, b_0), \dots, (t_{m-1}, b_{m-1})]$ be a list of dominoes, and let $A$, $B$ be the
nonterminals of the ambiguity grammar of $P$ for its top and bottom words. For every nonempty
sequence $i_1, \dots, i_n$ of indices less than $m$ and all words of terminals $u$, $v$, the
canonical rule sequence from $A$ for the words $t_i$ along $i_1, \dots, i_n$ is a leftmost
derivation of $u\, t_{i_1} \cdots t_{i_n}\, i_n \cdots i_1\, v$ from $u\,A\,v$, and the canonical
rule sequence from $B$ for the words $b_i$ along $i_1, \dots, i_n$ is a leftmost derivation of
$u\, b_{i_1} \cdots b_{i_n}\, i_n \cdots i_1\, v$ from $u\,B\,v$.

Formalized by `Cslib.Decidability.Grammar.leftDerivation_canon`, a theorem declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#left-derivation-canon).

## The start production $S \to A$

For an alphabet $\alpha$ and a natural number $A$, this is
the production with terminals $\alpha \sqcup \mathbb{N}$ and nonterminals $\mathbb{N}$ whose
left-hand side is the nonterminal $S = 0$ and whose right-hand side is the single nonterminal $A$.

In the ambiguity grammar of a PCP instance it is used with $A = 1$ and $A = 2$.

Formalized by `Cslib.Decidability.Grammar.startRule`, a definition declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#start-rule).

## Leftmost derivations in the ambiguity grammar

Let
$P = [(t_0, b_0), \dots, (t_{m-1}, b_{m-1})]$ be a list of dominoes, and let $S$, $A$, $B$ be the
nonterminals of the ambiguity grammar of $P$. Every leftmost derivation of a word $w$ from $S$ in
that grammar has one of two forms, for some nonempty sequence $i_1, \dots, i_n$ of indices less
than $m$: either it is $S \to A$ followed by the canonical rule sequence from $A$ for the words
$t_i$ along $i_1, \dots, i_n$, and $w = t_{i_1} \cdots t_{i_n}\, i_n \cdots i_1$; or it is
$S \to B$ followed by the canonical rule sequence from $B$ for the words $b_i$ along
$i_1, \dots, i_n$, and $w = b_{i_1} \cdots b_{i_n}\, i_n \cdots i_1$.

Formalized by `Cslib.Decidability.Grammar.cases_of_leftDerivation_start`, a theorem declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#cases-of-left-derivation-start).

## Leftmost derivations from the start symbol along an index sequence

Let
$P = [(t_0, b_0), \dots, (t_{m-1}, b_{m-1})]$ be a list of dominoes, and let $S$, $A$, $B$ be the
nonterminals of the ambiguity grammar of $P$. For every nonempty sequence $i_1, \dots, i_n$ of
indices less than $m$, the production $S \to A$ followed by the canonical rule sequence from $A$
for the words $t_i$ along $i_1, \dots, i_n$ is a leftmost derivation of
$t_{i_1} \cdots t_{i_n}\, i_n \cdots i_1$ from $S$, and the production $S \to B$ followed by the
canonical rule sequence from $B$ for the words $b_i$ along $i_1, \dots, i_n$ is a leftmost
derivation of $b_{i_1} \cdots b_{i_n}\, i_n \cdots i_1$ from $S$.

Formalized by `Cslib.Decidability.Grammar.leftDerivation_start`, a theorem declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#left-derivation-start).

## The ambiguity grammar of $P$ is ambiguous exactly when $P$ has a solution

For every list
$P$ of dominoes, the ambiguity grammar of $P$ is ambiguous, that is, some word has two different
leftmost derivations from its start symbol, if and only if $P$ has a PCP solution.

Formalized by `Cslib.Decidability.Grammar.isAmbiguous_iff_pcp`, a theorem declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#is-ambiguous-iff-pcp).

## The ambiguity grammar is primitive recursive

For every alphabet $\alpha$ with a
primitive recursive encoding by natural numbers, the map sending a list $P$ of dominoes over
$\alpha$ to the ambiguity grammar of $P$ is primitive recursive, where encoded grammars are
encoded as pairs of a start nonterminal and a list of productions.

Formalized by `Cslib.Decidability.Grammar.primrec_ambGrammar`, a theorem declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#primrec-amb-grammar).

## PCP many-one reduces to ambiguity of context-free grammars

For every alphabet $\alpha$
with a primitive recursive encoding by natural numbers and decidable equality, the Post
correspondence problem over $\alpha$ many-one reduces to ambiguity of encoded context-free
grammars over the terminals $\alpha \sqcup \mathbb{N}$: there is a computable function sending
each list $P$ of dominoes over $\alpha$ to such a grammar, which is ambiguous if and only if $P$
has a PCP solution.

Formalized by `Cslib.Decidability.Grammar.manyOneReducible_pcp_isAmbiguous`, a theorem declared in [CSLibExt/Computability/Decidability/PCPAmbiguity.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/PCPAmbiguity.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html#many-one-reducible-pcp-is-ambiguous).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ambiguity problem for context-free grammars](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/undecidable-problems/ambiguity-problem-for-context-free-grammars)
