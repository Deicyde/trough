---
declaration: section
origin: cited
lean: Cslib.Language.IsContextFree.add, Cslib.Language.IsContextFree.mul, Cslib.Language.IsContextFree.kstar, Cslib.Language.IsContextFree.pow, Cslib.Language.IsContextFree.of_finite, Cslib.Language.IsContextFree.of_length_le, Cslib.Language.IsContextFree.homImage, Cslib.Language.IsContextFree.inf_dfa_accepts
statement: formalized
proof: formalized
---

# Closure properties of context-free languages

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html).

## Closure of context-free languages under union

If $L$ and $M$ are context-free languages
over the same alphabet, then their union $L \cup M$ is context-free.

Formalized by `Cslib.Language.IsContextFree.add`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Closure.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Closure.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#add).

## Closure of context-free languages under concatenation

If $L$ and $M$ are context-free
languages over the same alphabet, then their concatenation $LM = \{uv : u \in L,\ v \in M\}$ is
context-free.

Formalized by `Cslib.Language.IsContextFree.mul`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Closure.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Closure.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#mul).

## Closure of context-free languages under Kleene star

If $L$ is a context-free language,
then its Kleene star $L^*$ is context-free.

Formalized by `Cslib.Language.IsContextFree.kstar`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Closure.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Closure.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#kstar).

## Powers of a context-free language are context-free

If $L$ is a context-free language,
then for every natural number $n$ the power $L^n$, the concatenation of $n$ copies of $L$ (with
$L^0$ the language containing only the empty word), is context-free.

Formalized by `Cslib.Language.IsContextFree.pow`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Closure.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Closure.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#pow).

## Finite languages are context-free

Every finite language is context-free.

Formalized by `Cslib.Language.IsContextFree.of_finite`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Closure.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Closure.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#of-finite).

## Languages of bounded word length are context-free

Over a finite alphabet, if $n$ is a
natural number and every word of a language $L$ has length at most $n$, then $L$ is
context-free.

Formalized by `Cslib.Language.IsContextFree.of_length_le`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Closure.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Closure.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#of-length-le).

## Context-free languages are closed under homomorphic images

Let $T$ and $T'$ be alphabets,
$L$ a context-free language over $T$, and $\varphi$ a map sending each letter of $T$ to a word
over $T'$. Then the language of all words $\varphi(a_1) \cdots \varphi(a_n)$ with
$a_1 \cdots a_n \in L$ is context-free.

A grammar for it replaces every terminal $a$ in every production by the word $\varphi(a)$.

Formalized by `Cslib.Language.IsContextFree.homImage`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Hom.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Hom.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#hom-image).

## Intersection of a context-free language with the language of a DFA

If $L$ is a
context-free language over an alphabet $T$ and $M$ is a deterministic finite automaton over $T$
with finitely many states, then the intersection of $L$ with the language accepted by $M$ is
context-free.

Formalized by `Cslib.Language.IsContextFree.inf_dfa_accepts`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InterRegular.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InterRegular.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#inf-dfa-accepts).

## Intersection of a context-free language with a regular language

If $L$ is a context-free
language and $R$ a regular language over the same alphabet, then $L \cap R$ is context-free.

No finite-alphabet assumption is needed: the grammar built in the proof only mentions terminals
that occur in the productions of the original grammar.

Formalized by `Cslib.Language.IsContextFree.inf_isRegular`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InterRegular.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/InterRegular.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#inf-is-regular).

## Context-free languages are closed under letter maps

Let $L$ be a context-free language
over an alphabet $T$ and let $f \colon T \to T'$ be a map of alphabets. Then the image of $L$
under $f$, the language $\{f(a_1) \cdots f(a_n) \mid a_1 \cdots a_n \in L\}$ over $T'$, is
context-free.

Formalized by `Cslib.Language.IsContextFree.map`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Map.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Map.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#map).

## Letter numbering for the substitution grammar

For a context-free grammar $g$ and a
letter $a$, the number of $a$ is the position (counted from $0$) of the first occurrence of $a$
in the list of terminals occurring in the productions of $g$, or the length of that list when $a$
does not occur in it.

Formalized by `Cslib.Language.Substitution.code`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#code).

## Letter decoding for the substitution grammar

For a context-free grammar $g$ and a natural
number $k$, the letter with number $k$ is the entry at position $k$ (counted from $0$) of the list
of terminals occurring in the productions of $g$; there is no such letter when $k$ is at least the
length of that list.

Formalized by `Cslib.Language.Substitution.decode`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#decode).

## Substituting the symbols of a grammar

Let $g$ be a context-free grammar over $T$ with
nonterminals $N_g$, and let $e$ assign to each letter $a \in T$ an encoded grammar $e(a)$ over
$T'$. Each symbol of $g$ becomes a nonterminal in $N_g \sqcup (\mathbb{N} \times \mathbb{N})$: a
nonterminal $B$ of $g$ becomes $B$ in the left part, and a terminal $a$ becomes the pair $(k, n)$,
where $k$ is the number of $a$ (the position, counted from $0$, of the first occurrence of $a$ in
the list of terminals occurring in the productions of $g$, or the length of that list when $a$
does not occur in it) and $n$ is the start nonterminal of $e(a)$.

Formalized by `Cslib.Language.Substitution.substSymbol`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#subst-symbol).

## Main production of the substitution grammar

Let $g$ be a context-free grammar over $T$
with nonterminals $N_g$, and let $e$ assign to each letter $a \in T$ an encoded grammar $e(a)$
over $T'$. A production $A \to \alpha$ over $T$ with nonterminals in $N_g$ gives the production
$A \to \alpha'$ over $T'$ with nonterminals in $N_g \sqcup (\mathbb{N} \times \mathbb{N})$, where
$A$ is taken in the left part and $\alpha'$ is obtained from $\alpha$ by replacing each
nonterminal $B$ by $B$ in the left part and each terminal $a$ by the nonterminal $(k, n)$; here
$k$ is the number of $a$ (the position, counted from $0$, of the first occurrence of $a$ in the
list of terminals occurring in the productions of $g$, or the length of that list when $a$ does
not occur in it) and $n$ is the start nonterminal of $e(a)$.

Formalized by `Cslib.Language.Substitution.mainRule`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#main-rule).

## Letter productions of the substitution grammar

Let $g$ be a context-free grammar over
$T$ with nonterminals $N_g$, let $a \in T$ have number $k$ (the position, counted from $0$, of the
first occurrence of $a$ in the list of terminals occurring in the productions of $g$, or the
length of that list when $a$ does not occur in it), and let $n \to w$ be a production over $T'$
whose nonterminals are natural numbers. It gives the production $(k, n) \to w'$ with
nonterminals in $N_g \sqcup (\mathbb{N} \times \mathbb{N})$, where $w'$ keeps the terminals of $w$
and replaces each nonterminal $m$ by $(k, m)$.

Formalized by `Cslib.Language.Substitution.subRule`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#sub-rule).

## Productions of the substitution grammar

Let $g$ be a context-free grammar over $T$, and
let $e$ assign to each letter $a \in T$ an encoded grammar $e(a)$ over $T'$. The productions of
the substitution grammar are the main productions obtained from the productions of $g$, together
with, for each terminal $a$ occurring in a production of $g$, the letter productions for $a$
obtained from the productions of $e(a)$.

Formalized by `Cslib.Language.Substitution.rules`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#rules).

## The substitution grammar

Let $g$ be a context-free grammar over $T$ with nonterminals
$N_g$ and start symbol $S$, and let $e$ assign to each letter $a \in T$ an encoded grammar $e(a)$
over $T'$. The substitution grammar is the context-free grammar over $T'$ with nonterminals
$N_g \sqcup (\mathbb{N} \times \mathbb{N})$, start symbol $S$ taken in the left part, and the
productions of the substitution grammar for $g$ and $e$.

Formalized by `Cslib.Language.Substitution.grammar`, an abbreviation declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#grammar).

## Intended languages of the substitution grammar

Let $g$ be a context-free grammar over
$T$ with nonterminals $N_g$, let $e$ assign to each letter $a \in T$ an encoded grammar $e(a)$
over $T'$, and let $s$ assign to each letter $a \in T$ a language $s(a)$ over $T'$. Each element
of $N_g \sqcup (\mathbb{N} \times \mathbb{N})$, the nonterminals of the substitution grammar, is
assigned a language over $T'$. A nonterminal $B \in N_g$ is assigned the substitution of $s$
into the language generated by $g$ from $B$. A pair $(k, n)$ is assigned, when $k$ is less than
the length of the list of terminals occurring in the productions of $g$ and $a$ is the entry at
position $k$ of that list (counted from $0$), the language generated from the nonterminal $n$ by
the grammar that $e(a)$ denotes, and the empty language otherwise.

Formalized by `Cslib.Language.Substitution.val`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#val).

## Derivations keep the terminals among those of the grammar

Let $g$ be a context-free
grammar and let the sentential form $u$ derive $v$ in $g$ in zero or more steps. If every terminal
occurring in $u$ occurs in some production of $g$, then every terminal occurring in $v$ occurs in
some production of $g$.

Formalized by `Cslib.Language.Substitution.mem_grammarTerminals_of_derives`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#mem-grammar-terminals-of-derives).

## Context-free languages are closed under substitution by context-free languages

**Context-free languages are closed under substitution by context-free languages.**

Formalized by `Cslib.Language.IsContextFree.substitution`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Substitution.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Substitution.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html#substitution).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Closure properties of context-free languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/closure-properties-of-context-free-languages)
