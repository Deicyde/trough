---
declaration: section
origin: cited
lean: Cslib.Language.YieldsH, Cslib.Language.YieldsH.mono, Cslib.Language.YieldsH.of_yields, Cslib.Language.Yields.of_yieldsH, Cslib.Language.YieldsH.append, Cslib.Language.YieldsH.append_inv, Cslib.Language.List.length_le_of_yieldsH, Cslib.Language.exists_minimal_yieldsH
statement: formalized
proof: formalized
---

# Pumping lemma for context-free languages

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html).

## Height-bounded derivations

Let $g$ be a context-free grammar. For a sentential form
$\alpha$ (a list of terminals and nonterminals of $g$), a terminal word $w$ and a natural number
$n$, say that $\alpha$ yields $w$ at height $n$ when this follows from three rules: the empty form
yields the empty word at every height $n$; if $\alpha$ yields $w$ at height $n$, then for every
terminal $a$ the form $a\alpha$ yields $aw$ at height $n$; and if $A \to \beta$ is a production of
$g$, $\beta$ yields $w_1$ at height $n$ and $\alpha$ yields $w_2$ at height $m$, then $A\alpha$
yields $w_1 w_2$ at height $\max(n + 1, m)$.

Thus $n$ bounds the height of a derivation forest, the number of nonterminal expansions along
its longest path; terminals and empty forests contribute nothing.

Formalized by `Cslib.Language.YieldsH`, an inductive type declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#yields-h).

## Raising the height bound of a yield

Let $g$ be a context-free grammar. If a sentential
form $\alpha$ yields the terminal word $w$ through a derivation forest of height at most $n$,
and $n \le m$, then $\alpha$ yields $w$ through a derivation forest of height at most $m$.

Formalized by `Cslib.Language.YieldsH.mono`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#mono).

## Every yield has a height bound

Let $g$ be a context-free grammar. If a sentential form
$\alpha$ yields the terminal word $w$, then there is a natural number $n$ such that $\alpha$
yields $w$ through a derivation forest of height at most $n$.

Formalized by `Cslib.Language.YieldsH.of_yields`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#of-yields).

## Height-bounded yields are yields

Let $g$ be a context-free grammar. If a sentential
form $\alpha$ yields the terminal word $w$ through a derivation forest of height at most $n$,
then $\alpha$ yields $w$.

Formalized by `Cslib.Language.Yields.of_yieldsH`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#of-yields-h).

## Concatenating height-bounded yields

Let $g$ be a context-free grammar. If a sentential
form $u$ yields the terminal word $w_1$ through a derivation forest of height at most $n$, and
a sentential form $v$ yields the terminal word $w_2$ through one of height at most $m$, then the
concatenation $uv$ yields $w_1 w_2$ through a derivation forest of height at most
$\max(n, m)$.

Formalized by `Cslib.Language.YieldsH.append`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#append).

## Splitting a height-bounded yield at a concatenation

Let $g$ be a context-free grammar
and $u$, $v$ sentential forms of $g$. If the concatenation $uv$ yields the terminal word $w$
through a derivation forest of height at most $n$, then there are terminal words $w_1$, $w_2$
with $w = w_1 w_2$ such that $u$ yields $w_1$ and $v$ yields $w_2$, each through a derivation
forest of height at most $n$.

Formalized by `Cslib.Language.YieldsH.append_inv`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#append-inv).

## Length bound for height-bounded yields

Let $g$ be a context-free grammar and $R$ a
natural number such that every production of $g$ has an output of length at most $R$. If a
sentential form $\alpha$ yields the terminal word $w$ through a derivation forest of height at
most $n$, then $|w| \le |\alpha| \cdot \max(2, R)^n$.

Formalized by `Cslib.Language.List.length_le_of_yieldsH`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#length-le-of-yields-h).

## Minimal-height derivation forests exist

Let $g$ be a context-free grammar. If a
sentential form $\alpha$ yields the terminal word $w$, then there is a natural number $n$ such
that $\alpha$ yields $w$ through a derivation forest of height at most $n$, but through no
derivation forest of height at most $m$ for any $m < n$.

Formalized by `Cslib.Language.exists_minimal_yieldsH`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#exists-minimal-yields-h).

## Derivation contexts

Let $g$ be a context-free grammar, let $A$ and $B$ be nonterminals of
$g$, and let $l$ and $r$ be words over the terminal alphabet. Then $(l, r)$ is a derivation
context from $A$ to $B$ when, for every terminal word $w$ that the nonterminal $B$ yields in $g$,
the nonterminal $A$ yields the word $l w r$ in $g$.

This is the language-inclusion form of a one-hole derivation context; it is what pumping
iteration uses, and it holds vacuously when $B$ yields nothing.

Formalized by `Cslib.Language.YieldsContext`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#yields-context).

## A production gives derivation contexts

Let $g$ be a context-free grammar and
$A \to \alpha_1 B \alpha_2$ a production of $g$, where $B$ is a nonterminal and $\alpha_1$,
$\alpha_2$ are sentential forms. If $\alpha_1$ yields the terminal word $l$ and $\alpha_2$ yields
the terminal word $r$, then for every terminal word $w$ yielded by $B$ the word $l w r$ is
yielded by $A$; that is, $(l, r)$ is a derivation context from $A$ to $B$.

Formalized by `Cslib.Language.YieldsContext.of_rule`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#of-rule).

## Pumping through a self-context

Let $g$ be a context-free grammar, $A$ a nonterminal and
$l$, $r$, $x$ terminal words. Suppose that for every terminal word $w$ yielded by $A$ the word
$l w r$ is also yielded by $A$, and that $A$ yields $x$. Then for every natural number $i$ the
nonterminal $A$ yields $l^i x r^i$, where $l^i$ and $r^i$ denote the concatenations of $i$
copies of $l$ and of $r$.

Formalized by `Cslib.Language.YieldsContext.iterate`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#iterate).

## Pumping lemma for context-free languages

For every context-free language $L$ over an
alphabet $T$ there is a natural number $n > 0$ such that every word $w \in L$ with $|w| \ge n$
can be written as $w = uvxyz$ with words $u, v, x, y, z$ over $T$ such that $vy$ is nonempty,
$|vxy| \le n$, and $u v^i x y^i z \in L$ for every natural number $i$, where $v^i$ and $y^i$
denote the concatenations of $i$ copies of $v$ and of $y$.

Formalized by `Cslib.Language.IsContextFree.pumping`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Pumping.lean, line 652](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Pumping.lean#L652). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html#pumping).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pumping lemma for context-free languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/pumping-lemma-for-context-free-languages)
