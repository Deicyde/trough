---
declaration: section
origin: cited
lean: Cslib.Language.EncodedCFG.symOk, Cslib.Language.EncodedCFG.ruleOk, Cslib.Language.EncodedCFG.genStep, Cslib.Language.EncodedCFG.generating, Cslib.Language.EncodedCFG.isEmptyB, Cslib.Language.EncodedCFG.genStep_generating_subset, Cslib.Language.EncodedCFG.exists_derives_of_forall, Cslib.Language.EncodedCFG.exists_derives_of_mem_iterate
statement: formalized
proof: formalized
---

# Emptiness of context-free grammars

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html).

## The procedure

## Acceptable symbols

Given a list $G$ of natural numbers and a symbol $s$ of an encoded
grammar over an alphabet $T$, which is either a nonterminal $i \in \mathbb{N}$ or a terminal in
$T$, $s$ is acceptable when it is a terminal or a nonterminal that occurs in $G$. The test
returns a Boolean.

Formalized by `Cslib.Language.EncodedCFG.symOk`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#sym-ok).

## Acceptable productions

Given a list $G$ of nonterminals (natural numbers), the test
accepts an encoded production $(A, \rho)$ when every symbol of $\rho$ is acceptable: a
terminal always is, and a nonterminal is when it belongs to $G$. So the production is accepted
exactly when every nonterminal occurring in $\rho$ belongs to $G$.

Formalized by `Cslib.Language.EncodedCFG.ruleOk`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#rule-ok).

## One round of the generating-nonterminal computation

Let a list of productions be given,
each a pair of a nonterminal $A \in \mathbb{N}$ and a right-hand side made of nonterminals and
terminals, together with a list $G$ of nonterminals. One round returns, in order, the left-hand
sides of those productions in whose right-hand side every nonterminal belongs to $G$.

Formalized by `Cslib.Language.EncodedCFG.genStep`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#gen-step).

## Generating nonterminals

For an encoded grammar $g$, start from the empty list of
nonterminals and, in each round, replace the current list $G$ by the list of left-hand sides of
those productions of $g$ whose right-hand sides contain no nonterminal outside $G$. The
generating nonterminals of $g$ are the list obtained after as many rounds as $g$ has productions.

Every nonterminal in this list derives a terminal word, and the start nonterminal is in it
whenever the grammar generates some word.

Formalized by `Cslib.Language.EncodedCFG.generating`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#generating).

## The emptiness test for context-free grammars

For an encoded grammar $g$, the test returns
true exactly when the start nonterminal of $g$ is not among the generating nonterminals of $g$.

Formalized by `Cslib.Language.EncodedCFG.isEmptyB`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#is-empty-b).

## The generating nonterminals are closed under one more round

For an encoded grammar $g$,
one more round of the generating-nonterminal computation, applied to the productions of $g$ and
the generating nonterminals of $g$, yields only generating nonterminals of $g$: every left-hand
side of a production of $g$ whose right-hand side has all its nonterminals among the generating
nonterminals of $g$ is itself a generating nonterminal of $g$.

Formalized by `Cslib.Language.EncodedCFG.genStep_generating_subset`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#gen-step-generating-subset).

## Sentential forms of productive nonterminals derive terminal words

In a context-free
grammar $G$, if every nonterminal occurring in a sentential form $u$ derives some terminal word,
then $u$ derives some terminal word.

Formalized by `Cslib.Language.EncodedCFG.exists_derives_of_forall`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#exists-derives-of-forall).

## Soundness of the productive-nonterminal iteration

Let $g$ be an encoded context-free
grammar. A round sends a list $H$ of nonterminals to the left-hand sides of those productions of
$g$ in whose right-hand side every nonterminal belongs to $H$. For every $k \ge 0$, every
nonterminal obtained after $k$ rounds starting from the empty list derives some terminal word in
the context-free grammar that $g$ denotes.

Formalized by `Cslib.Language.EncodedCFG.exists_derives_of_mem_iterate`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#exists-derives-of-mem-iterate).

## A sentential form containing an empty nonterminal denotes the empty language

Let $T$ be
an alphabet and $N$ a set of nonterminals, and let $V$ assign a language over $T$ to each
nonterminal. A sentential form $X_1 \cdots X_m$ over $T$ and $N$ denotes under $V$ the
concatenation $L_1 \cdots L_m$, where $L_t = V(X_t)$ if $X_t$ is a nonterminal and $L_t = \{X_t\}$
if $X_t$ is a terminal; the empty form denotes $\{\varepsilon\}$. Let $A \in N$ with
$V(A) = \emptyset$. Then every sentential form over $T$ and $N$ in which $A$ occurs denotes the
empty language under $V$.

Formalized by `Cslib.Language.EncodedCFG.evalForm_eq_zero_of_mem`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#eval-form-eq-zero-of-mem).

## Completeness of the generating-nonterminal computation

If an encoded grammar $g$
generates some word $w$, then the start nonterminal of $g$ is among the generating nonterminals
of $g$ computed by the emptiness procedure.

Formalized by `Cslib.Language.EncodedCFG.start_mem_generating_of_mem_language`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#start-mem-generating-of-mem-language).

## Correctness of the emptiness test

For every encoded context-free grammar $g$, the
emptiness test returns true on $g$ if and only if the language of $g$ is empty.

Formalized by `Cslib.Language.EncodedCFG.isEmptyB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#is-empty-b-iff).

## Emptiness of context-free grammars is computable

Let $T$ be an alphabet with decidable
equality and a primitive recursive encoding into the natural numbers. The predicate on encoded
context-free grammars $g$ over $T$ that holds exactly when the language of $g$ is empty is a
computable predicate.

Formalized by `Cslib.Language.EncodedCFG.computablePred_language_eq_zero`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#computable-pred-language-eq-zero).

## Emptiness of context-free grammars is decidable

For every alphabet $T$ with decidable
equality and a primitive recursive encoding, the property of an encoded context-free grammar $g$
over $T$ that the language of $g$ is empty is decidable by a multi-stack machine. This is Sipser,
Theorem 4.8: the problem $E_{\mathrm{CFG}}$ is decidable.

Formalized by `Cslib.Language.EncodedCFG.tm2Decidable_language_eq_zero`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#tm2-decidable-language-eq-zero).

## Factor of a word

For a word $w = w_0 w_1 \cdots w_{n-1}$ and natural numbers $i$ and
$j$, the factor of $w$ from position $i$ to position $j$ is obtained by dropping the first $i$
letters of $w$ and keeping at most the first $j - i$ letters of the rest, where $j - i$ is $0$
when $j \le i$. For $i \le j \le n$ it is $w_i w_{i+1} \cdots w_{j-1}$.

Formalized by `Cslib.Language.EncodedCFG.factor`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#factor).

## Splitting a factor

Let $w$ be a word and $i \le j \le |w|$, and write $w[i, j)$ for the
factor of $w$ from position $i$ to position $j$. If $w[i, j) = uv$, then $i + |u| \le j$,
$w[i, i + |u|) = u$ and $w[i + |u|, j) = v$.

Formalized by `Cslib.Language.EncodedCFG.factor_eq_append`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#factor-eq-append).

## Fitting a symbol at a position

Write $\langle s, t \rangle$ for the pairing bijection
$\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ given by $\langle s, t \rangle = t^2 + s$ if $s < t$
and $\langle s, t \rangle = s^2 + s + t$ otherwise. Given a word $w$, a list $R$ of items, a
list $S$ of positions and an encoded symbol $X$, the test at a position $i$ succeeds when either
$X$ is a terminal $a$, $i + 1 \in S$ and the letter of $w$ at position $i$ (counting from $0$)
is $a$; or $X$ is a nonterminal $B$ and some $k \in S$ has
$\langle B, \langle i, k \rangle \rangle \in R$.

In use, $S$ holds the positions where the rest of the right-hand side can start.

Formalized by `Cslib.Language.EncodedCFG.symFits`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#sym-fits).

## Start positions of a right-hand side

Write $\langle s, t \rangle$ for the pairing
bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ given by $\langle s, t \rangle = t^2 + s$
if $s < t$ and $\langle s, t \rangle = s^2 + s + t$ otherwise. Given a word $w$, a list $R$ of
items (natural numbers), a position $j$ and an encoded right-hand side $X_1 \cdots X_m$, a
position $i$ is a start when there are positions $i = p_0, p_1, \ldots, p_m = j$ with
$p_0, \ldots, p_{m-1} \le |w|$ such that for each $l = 1, \ldots, m$: if $X_l$ is a terminal
$a$, then $p_l = p_{l-1} + 1$ and the letter of $w$ at position $p_{l-1}$ (counting from $0$)
is $a$; if $X_l$ is a nonterminal $B$, then $R$ contains the code
$\langle B, \langle p_{l-1}, p_l \rangle \rangle$. The starts are computed from the right, one
symbol at a time, by the symbol-fitting test; for the empty right-hand side the only start is
$j$.

Formalized by `Cslib.Language.EncodedCFG.starts`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#starts).

## One round of the membership procedure

Write $\langle s, t \rangle$ for the pairing
bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ given by $\langle s, t \rangle = t^2 + s$
if $s < t$ and $\langle s, t \rangle = s^2 + s + t$ otherwise. Given an encoded grammar $g$, a
word $w$ and a list $R$ of items found so far, the round lists, for every production
$A \to \rho$ of $g$, every position $j \le |w|$ and every start $i$ of $\rho$ for the factor of
$w$ ending at $j$ given $R$, the code $\langle A, \langle i, j \rangle \rangle$ of the item
$(A, i, j)$.

Formalized by `Cslib.Language.EncodedCFG.memStep`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#mem-step).

## Candidate items for membership

For an encoded grammar $g$ and a word $w$, the candidate
items are the triples $(A, i, j)$, encoded as natural numbers by pairing, where $A$ is the
left-hand side of a production of $g$ and $i, j \le |w|$; each triple is listed once for every
production whose left-hand side is $A$.

Formalized by `Cslib.Language.EncodedCFG.items`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#items).

## Items found by the membership procedure

Let $g$ be an encoded context-free grammar and
$w = w_0 \cdots w_{n-1}$ a word. An item is a triple $(A, i, j)$ of natural numbers, coded as a
natural number by nested pairing. A round sends a list $R$ of items to the items $(A, i, j)$ such
that $A \to X_1 \cdots X_m$ is a production of $g$, $j \le n$, and there are positions
$i = k_0, k_1, \ldots, k_m = j$, each at most $n$, such that for every $t$ with $1 \le t \le m$,
either $X_t$ is the terminal $w_{k_{t-1}}$ and $k_t = k_{t-1} + 1$, or $X_t$ is a nonterminal $B$
with $(B, k_{t-1}, k_t)$ in $R$. The items found are the result of applying the round $M$ times
to the empty list, where $M$ is $(n + 1)^2$ times the length of the list of productions of $g$.

Formalized by `Cslib.Language.EncodedCFG.found`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#found).

## The membership test for context-free grammars

For an encoded grammar $g$ with start
nonterminal $S$ and a word $w$, the test returns true exactly when the item $(S, 0, |w|)$ is
among the items found for $g$ and $w$.

Formalized by `Cslib.Language.EncodedCFG.memLanguageB`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#mem-language-b).

## Sound items

Write $\langle s, t \rangle$ for the pairing bijection
$\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ given by $\langle s, t \rangle = t^2 + s$ if $s < t$
and $\langle s, t \rangle = s^2 + s + t$ otherwise. Given an encoded grammar $g$ and a word $w$,
a natural number $x$ is a sound item when $x = \langle A, \langle i, j \rangle \rangle$ for some
$A$, $i$, $j$ with $i \le j \le |w|$ such that the nonterminal $A$ yields, in the decoded
grammar of $g$, the factor of $w$ from position $i$ to position $j$.

Formalized by `Cslib.Language.EncodedCFG.SoundItem`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#sound-item).

## Completeness of the start positions

Let $g$ be an encoded context-free grammar over an
alphabet $T$ with decidable equality, let $w$ be a word over $T$, and let $\rho$ be an encoded
right-hand side whose decoding yields a word $u$ in the grammar that $g$ denotes. If
$i \le j \le |w|$ and $u$ is the factor of $w$ from position $i$ to position $j$, then $i$ is a
start position of $\rho$ at $j$ for the word $w$ and the list of items found by the membership
procedure on $g$ and $w$.

Formalized by `Cslib.Language.EncodedCFG.mem_starts_of_yields`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 528](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L528). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#mem-starts-of-yields).

## Correctness of the membership test

For every encoded context-free grammar $g$ and every
word $w$, the membership test returns true on $g$ and $w$ if and only if $w$ belongs to the
language of $g$.

Formalized by `Cslib.Language.EncodedCFG.memLanguageB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#mem-language-b-iff).

## Membership for context-free grammars is decidable

For every alphabet $T$ with decidable
equality and a primitive recursive encoding, the property of a pair $(g, w)$, where $g$ is an
encoded context-free grammar over $T$ and $w$ is a word over $T$, that $w$ is in the language of
$g$ is decidable by a multi-stack machine. This is Sipser, Theorem 4.7: the problem
$A_{\mathrm{CFG}}$ is decidable.

Formalized by `Cslib.Language.EncodedCFG.tm2Decidable_mem_language`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 699](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L699). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#tm2-decidable-mem-language).

## Right-hand side length bound

For an encoded grammar $g$, the length bound is the maximum
of $2$ and the lengths of the right-hand sides of the productions of $g$.

Formalized by `Cslib.Language.EncodedCFG.lenBound`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 718](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L718). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#len-bound).

## Pumping bound of an encoded grammar

For an encoded grammar $g$, let $L$ be the length
bound of $g$, the larger of $2$ and the largest length of a right-hand side of a production of
$g$, and let $K$ be the number of distinct left-hand sides of the productions of $g$. The
pumping bound of $g$ is $L^{K+1}$.

With this bound, Ogden's lemma with every letter marked gives the pumping lemma for the decoded
grammar.

Formalized by `Cslib.Language.EncodedCFG.pumpBound`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 723](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L723). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#pump-bound).

## The words of a given length over a list of letters

For a list $A$ of letters and a
natural number $n$, the list obtained from the list whose only entry is the empty word by $n$
rounds, each of which replaces every word $w$, in order, by the words $a w$ for the letters $a$
of $A$, in order. Its entries are exactly the words of length $n$ all of whose letters occur in
$A$.

Formalized by `Cslib.Language.EncodedCFG.wordsOver`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#words-over).

## The terminals of an encoded grammar

For an encoded context-free grammar $g$ over an
alphabet $T$ with decidable equality, the list of the terminals that occur in the right-hand
sides of the productions of $g$, each listed once.

Listing each terminal once keeps the enumeration of the words over these terminals free of
repetitions.

Formalized by `Cslib.Language.EncodedCFG.terminals`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 780](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L780). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#terminals).

## The infiniteness test

Let $g$ be an encoded grammar and $N$ its pumping bound. The test
returns true exactly when some word $w$ whose letters all occur as terminals in the productions
of $g$, with $N \le |w| < 2N$, is accepted by the membership test for $g$.

Formalized by `Cslib.Language.EncodedCFG.infiniteB`, a definition declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 821](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L821). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#infinite-b).

## Letters of generated words occur in the productions

If a word $w$ is generated by an
encoded grammar $g$, then every letter of $w$ is among the terminals of $g$, that is, it occurs
in the right-hand side of some production of $g$.

Formalized by `Cslib.Language.EncodedCFG.mem_terminals_of_mem_language`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 848](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L848). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#mem-terminals-of-mem-language).

## Pumping lemma for encoded grammars

Let $g$ be an encoded grammar with pumping bound
$N$. Every word $w$ generated by $g$ with $|w| \ge N$ can be written as $w = uvxyz$ with $vy$
nonempty and $|vxy| \le N$, such that $u v^i x y^i z$ is generated by $g$ for every natural
number $i$, including $i = 0$.

Formalized by `Cslib.Language.EncodedCFG.pumping_pumpBound`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 861](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L861). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#pumping-pump-bound).

## Long words make a context-free language infinite

If the language of an encoded grammar
$g$ contains a word whose length is at least the pumping bound of $g$, then the language of $g$
is infinite.

Formalized by `Cslib.Language.EncodedCFG.infinite_of_mem_of_le`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 875](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L875). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#infinite-of-mem-of-le).

## Context-free pumping down below twice the pumping bound

Let $g$ be an encoded
context-free grammar, let $L$ be the largest of $2$ and the lengths of the right-hand sides of
the productions of $g$, let $K$ be the number of distinct left-hand sides of these productions,
and let $N = L^{K+1}$ be the pumping bound of $g$. For every word $w$ in the language of $g$ with
$|w| \ge N$, there is a word $v$ in the language of $g$ with $N \le |v| < 2N$.

Formalized by `Cslib.Language.EncodedCFG.exists_mem_le_lt`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 895](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L895). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#exists-mem-le-lt).

## Correctness of the infiniteness test

For every encoded context-free grammar $g$, the
infiniteness test returns true on $g$ if and only if the language of $g$ is infinite.

Formalized by `Cslib.Language.EncodedCFG.infiniteB_iff`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 916](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L916). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#infinite-b-iff).

## Infiniteness of context-free languages is decidable

For every alphabet $T$ with decidable
equality and a primitive recursive encoding, the property of an encoded context-free grammar $g$
over $T$ that the language of $g$ is infinite is decidable by a multi-stack machine. This is the
problem $\mathrm{INFINITE}_{\mathrm{CFG}}$.

Formalized by `Cslib.Language.EncodedCFG.tm2Decidable_language_infinite`, a theorem declared in [CSLibExt/Computability/Decidability/ContextFree.lean, line 987](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ContextFree.lean#L987). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html#tm2-decidable-language-infinite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Emptiness of context-free grammars](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/emptiness-of-context-free-grammars)
