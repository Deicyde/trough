---
declaration: section
origin: cited
lean: Cslib.Language.marks, Cslib.Language.ogden_of_bound, Cslib.Language.pumping_of_bound, Cslib.Language.IsContextFree.ogden
statement: formalized
proof: formalized
---

# Ogden's lemma

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/ogden-s-lemma/index.html).

## Number of marked letters

A marked word over an alphabet $T$ is a word whose letters are
pairs $(a, b)$ with $a \in T$ and $b$ a Boolean; the letter $(a, b)$ is marked when $b$ is true.
The number of marked letters of a marked word $w$ is the number of letters of $w$ that are
marked, counted with multiplicity.

Formalized by `Cslib.Language.marks`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Ogden.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Ogden.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/ogden-s-lemma/index.html#marks).

## Ogden's lemma for a grammar, with an explicit bound

Let $g$ be a context-free grammar
over an alphabet $T$ and let $R$, $K$, $n$ be natural numbers with $R \ge 2$ such that the
right-hand side of every production of $g$ has length at most $R$, some list of at most $K$
nonterminals contains the left-hand side of every production of $g$, and $R^{K+1} \le n$. A
marked word is a word whose letters are pairs $(a, b)$ with $a \in T$ and $b$ a Boolean, the
letter being marked when $b$ is true; its underlying word is the word of first components. Then
every marked word $w$ whose underlying word lies in the language of $g$ and which has at least
$n$ marked letters can be written as $w = uvxyz$ with marked words $u, v, x, y, z$ such that $vy$
has at least one marked letter, $vxy$ has at most $n$ marked letters, and for every natural
number $i$ the underlying word of $u v^i x y^i z$ lies in the language of $g$, where $v^i$ is the
concatenation of $i$ copies of $v$.

Formalized by `Cslib.Language.ogden_of_bound`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Ogden.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Ogden.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/ogden-s-lemma/index.html#ogden-of-bound).

## The pumping lemma for a grammar, with an explicit bound

Let $g$ be a context-free grammar
over an alphabet $T$ and let $R$, $K$, $n$ be natural numbers with $R \ge 2$ such that the
right-hand side of every production of $g$ has length at most $R$, some list of at most $K$
nonterminals contains the left-hand side of every production of $g$, and $R^{K+1} \le n$. Then
every word $w$ in the language of $g$ of length at least $n$ can be written as $w = uvxyz$ with
words $u, v, x, y, z$ over $T$ such that $vy$ is nonempty, $vxy$ has length at most $n$, and
$u v^i x y^i z$ lies in the language of $g$ for every natural number $i$, where $v^i$ is the
concatenation of $i$ copies of $v$.

It follows from Ogden's lemma with every letter marked.

Formalized by `Cslib.Language.pumping_of_bound`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Ogden.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Ogden.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/ogden-s-lemma/index.html#pumping-of-bound).

## Ogden's lemma

Let $L$ be a context-free language over an alphabet $T$. A marked word is a
word whose letters are pairs $(a, b)$ with $a \in T$ and $b$ a Boolean, the letter being marked
when $b$ is true; its underlying word is the word of first components. Then there is a natural
number $n > 0$ such that every marked word $w$ whose underlying word lies in $L$ and which has at
least $n$ marked letters can be written as $w = uvxyz$ with marked words $u, v, x, y, z$ such that
$vy$ has at least one marked letter, $vxy$ has at most $n$ marked letters, and for every natural
number $i$ the underlying word of $u v^i x y^i z$ lies in $L$, where $v^i$ is the concatenation
of $i$ copies of $v$.

Formalized by `Cslib.Language.IsContextFree.ogden`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Ogden.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Ogden.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/ogden-s-lemma/index.html#ogden).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ogden's lemma](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/ogden-s-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/ogden-s-lemma)
