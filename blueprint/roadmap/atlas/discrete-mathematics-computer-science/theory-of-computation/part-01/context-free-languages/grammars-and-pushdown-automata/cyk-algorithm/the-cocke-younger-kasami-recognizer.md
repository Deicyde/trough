---
declaration: section
origin: cited
lean: Cslib.Language.no_empty_rule_of_mem_output, Cslib.Language.empty_rule_of_yields_nil, Cslib.Language.yields_nonterminal_iff_of_ne_nil, Cslib.Language.cykFits, Cslib.Language.cykCellFrom, Cslib.Language.mem_cykCellFrom_iff, Cslib.Language.cykCell, Cslib.Language.mem_cykCell_iff
statement: formalized
proof: formalized
---

# The Cocke–Younger–Kasami recognizer

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html).

## Yields under Chomsky normal form

## Nonterminals in outputs have no empty production

Let $g$ be a context-free grammar in
Chomsky normal form. If a nonterminal $B$ occurs in the output of some production of $g$, then
$g$ has no production $B \to \varepsilon$.

Such a production would have the initial nonterminal on the left, which then occurs in an output
while an empty production exists.

Formalized by `Cslib.Language.no_empty_rule_of_mem_output`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#no-empty-rule-of-mem-output).

## Forms yielding the empty word under Chomsky normal form

If $g$ is in Chomsky normal form,
then every symbol of a sentential form that yields the empty word is a nonterminal $B$ for which
$g$ has a production $B \to \varepsilon$.

Formalized by `Cslib.Language.empty_rule_of_yields_nil`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#empty-rule-of-yields-nil).

## Shape of yields under Chomsky normal form

Let $g$ be a context-free grammar in Chomsky
normal form, $A$ a nonterminal and $w$ a nonempty word. Then $A$ yields $w$ if and only if $g$
has a production $A \to a$ with $a$ a terminal and $w = a$, or a production $A \to BC$ with
nonterminals $B$ and $C$ and nonempty words $w_1$ and $w_2$ such that $w = w_1 w_2$, $B$ yields
$w_1$ and $C$ yields $w_2$.

Formalized by `Cslib.Language.yields_nonterminal_iff_of_ne_nil`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#yields-nonterminal-iff-of-ne-nil).

## When a production output fits a word

Let $f$ assign a cell (a finite set of nonterminals)
to every word. A production output fits a word $w$ with respect to $f$ exactly in two cases: the
output is a single terminal $a$ and $w$ is the one-letter word $a$; or the output is a pair of
nonterminals $B C$ and there is some $i$ with $0 < i < |w|$ such that $B$ lies in the cell of the
first $i$ letters of $w$ and $C$ lies in the cell of the remaining letters. No other output fits
any word.

Formalized by `Cslib.Language.cykFits`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#cyk-fits).

## The CYK cell built from given cells

Given an assignment $f$ of a cell (a finite set of
nonterminals of $g$) to every word, the cell of a word $w$ built from $f$ is the set of left-hand
sides of those productions of $g$ whose outputs fit $w$ with respect to $f$.

Formalized by `Cslib.Language.cykCellFrom`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#cyk-cell-from).

## The CYK step

Let $g$ be a context-free grammar in Chomsky normal form, let $f$ assign to
each word over the terminals a finite set of nonterminals, and let $w$ be a nonempty word. For
$0 < i < |w|$ write $u_i$ for the prefix of $w$ of length $i$ and $v_i$ for the remaining suffix,
so that $w = u_i v_i$. Suppose that for every such $i$ and every nonterminal $B$, $B \in f(u_i)$
if and only if $B$ yields $u_i$, and $B \in f(v_i)$ if and only if $B$ yields $v_i$. Then a
nonterminal $A$ lies in the CYK cell of $w$ built from $f$ if and only if $A$ yields $w$.

Formalized by `Cslib.Language.mem_cykCellFrom_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#mem-cyk-cell-from-iff).

## The unshared CYK recurrence

The depth-$n$ CYK cell of a word $w$ is defined by recursion
on $n$: at depth $0$ every cell is empty, and the depth-$(n + 1)$ cell of $w$ is the CYK cell of
$w$ built from the depth-$n$ cells of all words. Cells are recomputed without sharing.

Formalized by `Cslib.Language.cykCell`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#cyk-cell).

## Correctness of the CYK recurrence

Let $g$ be a context-free grammar in Chomsky normal
form. For every natural number $n$, every nonterminal $A$ and every nonempty word $w$ of length
at most $n$, $A$ lies in the depth-$n$ CYK cell of $w$ if and only if $A$ yields $w$.

Formalized by `Cslib.Language.mem_cykCell_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#mem-cyk-cell-iff).

## Looking up a word in a CYK table

In a table listing pairs of a word and a cell, the cell
recorded for a word $u$ is the cell of the first entry whose word is $u$, or the empty set if no
entry has word $u$.

Formalized by `Cslib.Language.cykLookup`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#cyk-lookup).

## The CYK table

The CYK table of a word $w$ up to length $l$ is a list of pairs of a word
and a cell, defined by recursion on $l$. Up to length $0$ it is empty. The table up to length
$l + 1$ is the table $t$ up to length $l$ followed by one entry for each position $i$ (counted
from $0$) with $i + l + 1 \le |w|$, in increasing order of $i$: the factor $u$ of $w$ of length
$l + 1$ starting at position $i$, together with the CYK cell of $u$ built from the cells recorded
in $t$.

Formalized by `Cslib.Language.cykTable`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#cyk-table).

## Correct CYK tables

A table listing pairs $(u, X)$ of a word $u$ and a set $X$ of
nonterminals of $g$ is correct when, for every entry $(u, X)$ with $u$ nonempty, $X$ consists
exactly of the nonterminals $B$ such that the one-symbol form $B$ yields $u$.

Formalized by `Cslib.Language.CykTableCorrect`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#cyk-table-correct).

## Correctness of the CYK table

Let $g$ be a context-free grammar in Chomsky normal form and
$w$ a word. For every $l$, the CYK table of $w$ up to length $l$ is correct, and for all $j$ and
$m$ with $0 < m \le l$ and $j + m \le |w|$, some entry of the table has as its word the factor of
$w$ of length $m$ starting at position $j$ (positions counted from $0$).

Formalized by `Cslib.Language.cykTable_spec`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#cyk-table-spec).

## The CYK recognizer

Let $g$ be a context-free grammar with initial nonterminal $S$. The
CYK recognizer accepts the empty word exactly when $g$ has a production $S \to \varepsilon$, and
accepts a nonempty word $w$ exactly when $S$ lies in the cell recorded for $w$ in the CYK table of
$w$ up to length $|w|$.

Formalized by `Cslib.Language.cykAccepts`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#cyk-accepts).

## Correctness of the CYK recognizer

Let $g$ be a context-free grammar in Chomsky normal
form. For every word $w$ over the terminals of $g$, the CYK recognizer accepts $w$ if and only if
$w$ belongs to the language of $g$.

Formalized by `Cslib.Language.cykAccepts_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYK.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYK.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html#cyk-accepts-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Cocke–Younger–Kasami recognizer](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/the-cocke-younger-kasami-recognizer)
