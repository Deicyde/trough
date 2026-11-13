---
declaration: section
origin: cited
lean: Cslib.Decidability.not_tm2Decidable_halting, Cslib.Decidability.tm2Recognizable_halting, Cslib.Decidability.not_tm2CoRecognizable_halting, Cslib.Decidability.exists_not_tm2Decidable_tm2HaltsOn, Cslib.Decidability.rice_tm2, Cslib.Decidability.manyOneReducible_iff_exists_tm2, Cslib.Decidability.tm2Decidable_of_manyOneReducible, Cslib.Decidability.tm2Recognizable_of_manyOneReducible
statement: formalized
proof: formalized
---

# Halting problem and Rice's theorem

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html).

## The halting problem is undecidable by multi-stack machines

For every $n \in \mathbb{N}$,
no multi-stack machine decides whether a partial recursive code halts on input $n$.

Formalized by `Cslib.Decidability.not_tm2Decidable_halting`, a theorem declared in [CSLibExt/Computability/Decidability/Undecidable.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Undecidable.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#not-tm2-decidable-halting).

## The halting problem is recognizable by multi-stack machines

For every
$n \in \mathbb{N}$, the set of partial recursive codes whose program halts on input $n$ is
recognizable by a multi-stack machine.

Formalized by `Cslib.Decidability.tm2Recognizable_halting`, a theorem declared in [CSLibExt/Computability/Decidability/Undecidable.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Undecidable.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#tm2-recognizable-halting).

## The halting problem is not co-recognizable by multi-stack machines

For every
$n \in \mathbb{N}$, the set of partial recursive codes whose program halts on input $n$ is not
co-recognizable by a multi-stack machine: no multi-stack machine halts on exactly the codes
whose program does not halt on input $n$.

Formalized by `Cslib.Decidability.not_tm2CoRecognizable_halting`, a theorem declared in [CSLibExt/Computability/Decidability/Undecidable.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Undecidable.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#not-tm2-co-recognizable-halting).

## Some multi-stack machine has an undecidable halting set

There is a multi-stack machine
$M$, with a bijection between its input alphabet and the Booleans, such that no multi-stack
machine decides, for $n \in \mathbb{N}$, whether $M$ halts when started on the binary
representation of $n$ (written in $M$'s input alphabet through the bijection).

The halting set of a code interpreter on input $0$ is r.e., hence the halting set of a
multi-stack machine, and deciding it would decide the halting problem.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_tm2HaltsOn`, a theorem declared in [CSLibExt/Computability/Decidability/Undecidable.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Undecidable.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#exists-not-tm2-decidable-tm2-halts-on).

## Rice's theorem for multi-stack machines

Let $C$ be a set of partial functions
$\mathbb{N} \to \mathbb{N}$. If a multi-stack machine decides, for each partial recursive code,
whether the function the code computes lies in $C$, then for all partial recursive functions
$f$ and $g$, $f \in C$ implies $g \in C$.

Formalized by `Cslib.Decidability.rice_tm2`, a theorem declared in [CSLibExt/Computability/Decidability/Undecidable.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Undecidable.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#rice-tm2).

## Mapping reductions are computed by multi-stack machines

Let $p$ and $q$ be predicates on
primitive recursively encodable types $\alpha$ and $\beta$, and write $\langle x \rangle \in
\mathbb{N}$ for the code of $x$. Then $p$ is many-one reducible to $q$ if and only if there is a
function $f : \alpha \to \beta$ with $p(a) \iff q(f(a))$ for all $a \in \alpha$, together with a
function $F : \mathbb{N} \to \mathbb{N}$ that a multi-stack machine computes on binary
representations and that satisfies $F(\langle a \rangle) = \langle f(a) \rangle$ for all
$a \in \alpha$.

Formalized by `Cslib.Decidability.manyOneReducible_iff_exists_tm2`, a theorem declared in [CSLibExt/Computability/Decidability/Undecidable.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Undecidable.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#many-one-reducible-iff-exists-tm2).

## Decidability transfers along mapping reductions

Let $p$ and $q$ be predicates on
primitive recursively encodable types $\alpha$ and $\beta$. If $p$ is many-one reducible to $q$
and $q$ is decidable by a multi-stack machine, then $p$ is decidable by a multi-stack machine.

Formalized by `Cslib.Decidability.tm2Decidable_of_manyOneReducible`, a theorem declared in [CSLibExt/Computability/Decidability/Undecidable.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Undecidable.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#tm2-decidable-of-many-one-reducible).

## Recognizability transfers along mapping reductions

Let $p$ and $q$ be predicates on
primitive recursively encodable types $\alpha$ and $\beta$. If $p$ is many-one reducible to $q$
and $q$ is recognizable by a multi-stack machine, then $p$ is recognizable by a multi-stack
machine.

Formalized by `Cslib.Decidability.tm2Recognizable_of_manyOneReducible`, a theorem declared in [CSLibExt/Computability/Decidability/Undecidable.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Undecidable.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#tm2-recognizable-of-many-one-reducible).

## Rice's theorem for partial recursive codes

Let $C$ be a set of partial functions
$\mathbb{N} \rightharpoonup \mathbb{N}$, and suppose there are partial recursive functions
$f \in C$ and $g \notin C$. Then the property of a partial recursive code $c$ that the partial
function computed by $c$ belongs to $C$ is not decidable by a multi-stack Turing machine.

Formalized by `Cslib.Decidability.not_tm2Decidable_of_nontrivial`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#not-tm2-decidable-of-nontrivial).

## Rice's theorem for languages

Let $P$ be a set of subsets of $\mathbb{N}$, and suppose
there are partial recursive codes $c_1$ and $c_2$ such that the domain of $c_1$ (the set of
inputs on which it halts) belongs to $P$ and the domain of $c_2$ does not. Then the property of a
partial recursive code $c$ that the domain of $c$ belongs to $P$ is not decidable by a
multi-stack Turing machine.

Formalized by `Cslib.Decidability.not_tm2Decidable_language`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#not-tm2-decidable-language).

## Acceptance by a code

A partial recursive code $c$ accepts a natural number $n$ when $c$
halts on input $n$ with output $0$. Acceptance is a predicate on pairs $(c, n)$; it is the analogue
of Sipser's $A_{\mathrm{TM}}$, where a machine may halt without accepting.

Formalized by `Cslib.Decidability.Accepts`, a definition declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#accepts).

## Halting of a code on an input

A partial recursive code $c$ halts on a natural number $n$
when its evaluation at $n$ is defined. Halting is a predicate on pairs $(c, n)$; it is the analogue
of Sipser's $\mathrm{HALT}_{\mathrm{TM}}$.

Formalized by `Cslib.Decidability.Halts`, a definition declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#halts).

## A code that halts only on zero

There is a partial recursive code $z$ that on input $0$
halts with output $0$ and on every input $x \ne 0$ does not halt.

Formalized by `Cslib.Decidability.exists_code_zero_or_loop`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#exists-code-zero-or-loop).

## Acceptance reduces to halting

Say a partial recursive code $c$ accepts a natural number
$n$ when $c$ halts on input $n$ with output $0$. Acceptance many-one reduces to halting: there is
a computable map $f$ from pairs $(c, n)$ of a partial recursive code and a natural number to such
pairs, such that for every pair $(c, n)$, the code $c$ accepts $n$ if and only if, writing
$f(c, n) = (c', n')$, the code $c'$ halts on $n'$.

The reduction runs the code, then loops unless the output is $0$.

Formalized by `Cslib.Decidability.manyOneReducible_accepts_halts`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#many-one-reducible-accepts-halts).

## Halting reduces to acceptance

Say a partial recursive code $c$ accepts a natural number
$n$ when $c$ halts on input $n$ with output $0$. Halting many-one reduces to acceptance: there is
a computable map $f$ from pairs $(c, n)$ of a partial recursive code and a natural number to such
pairs, such that for every pair $(c, n)$, the code $c$ halts on $n$ if and only if, writing
$f(c, n) = (c', n')$, the code $c'$ accepts $n'$.

The reduction runs the code, then outputs $0$.

Formalized by `Cslib.Decidability.manyOneReducible_halts_accepts`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#many-one-reducible-halts-accepts).

## Halting is undecidable

No multi-stack Turing machine decides, for pairs $(c, n)$ of a
partial recursive code and a natural number, whether $c$ halts on $n$.

Formalized by `Cslib.Decidability.not_tm2Decidable_halts`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#not-tm2-decidable-halts).

## Acceptance is undecidable

No multi-stack Turing machine decides, for pairs $(c, n)$ of a
partial recursive code and a natural number, whether $c$ accepts $n$, that is, halts on $n$ with
output $0$.

This is Sipser's Theorem 4.11, with partial recursive codes in place of Turing machines.

Formalized by `Cslib.Decidability.not_tm2Decidable_accepts`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#not-tm2-decidable-accepts).

## Unary language of a set of naturals

For a set $S \subseteq \mathbb{N}$, the unary
language of $S$ is the language over the one-letter alphabet $\{\ast\}$ consisting of the words
whose length lies in $S$.

Formalized by `Cslib.Decidability.unaryLang`, a definition declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#unary-lang).

## Codes with a regular halting set

A partial recursive code $c$ has a regular halting set
when the unary language of its domain (the set of inputs on which $c$ halts), that is, the
language of the words over a one-letter alphabet whose length lies in the domain of $c$, is
regular.

This is a domain analogue of Sipser's $\mathrm{REGULAR}_{\mathrm{TM}}$, which asks about the
accepted words instead.

Formalized by `Cslib.Decidability.RegularDomainCode`, a definition declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#regular-domain-code).

## The unary squares are not regular

The unary language of the perfect squares, the set of
words over a one-letter alphabet whose length is $m^2$ for some $m \in \mathbb{N}$, is not regular.

The proof uses the pumping lemma: if a DFA with $N$ states accepted this language, pumping the word
of length $N^2$ by a block of length between $1$ and $N$ would give a length strictly between $N^2$
and $(N + 1)^2$.

Formalized by `Cslib.Decidability.not_isRegular_unaryLang_squares`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#not-is-regular-unary-lang-squares).

## Partial function of the halting-to-regularity reduction

For a partial recursive code
$c$ and natural numbers $n$ and $x$, the value at $((c, n), x)$ is $0$ if $x$ is a perfect
square; otherwise it is defined exactly when $c$ halts on input $n$, and then it is $0$.

Formalized by `Cslib.Decidability.regularRedFun`, a definition declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#regular-red-fun).

## A single code for the regularity reduction function

For a pair $q = (c, n)$ of a partial
recursive code and a natural number, let $g_q$ be the partial function on $\mathbb{N}$ that on
input $x$ halts with output $0$ if $x$ is a perfect square, and otherwise runs $c$ on $n$ and,
if that halts, outputs $0$ (and is undefined if it does not). Write $\ulcorner q \urcorner$ for
the standard encoding of $q$ as a natural number, and $\langle a, b \rangle$ for the standard
pairing of natural numbers $a$ and $b$. There is a partial recursive code $U$ such that for every
such pair $q$ and every $x \in \mathbb{N}$, the value of $U$ at
$\langle \ulcorner q \urcorner, x \rangle$ equals $g_q(x)$ as a partial value: one is defined
exactly when the other is, and then they agree.

Formalized by `Cslib.Decidability.exists_code_regularRedFun`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#exists-code-regular-red-fun).

## Halting reduces to regularity of halting sets

There is a computable map $f$ from pairs
$(c, n)$ of a partial recursive code and a natural number to partial recursive codes such that for
every pair $(c, n)$, the code $c$ halts on $n$ if and only if the halting set of $f(c, n)$ (the set
of inputs on which it halts), read as a unary language, is regular. That is, halting many-one
reduces to regularity of halting sets.

The construction follows Sipser's proof of Theorem 5.3: $f(c, n)$ halts on every perfect square,
and on every input if $c$ halts on $n$.

Formalized by `Cslib.Decidability.manyOneReducible_halts_regularDomain`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#many-one-reducible-halts-regular-domain).

## Regularity of halting sets is undecidable

For a partial recursive code $c$, let
$\operatorname{dom}(c) \subseteq \mathbb{N}$ be the set of inputs on which $c$ halts. The
property of $c$ that the unary language $\{w \in \{\ast\}^* : |w| \in \operatorname{dom}(c)\}$
is regular is not decidable by a multi-stack Turing machine.

Formalized by `Cslib.Decidability.not_tm2Decidable_regularDomain`, a theorem declared in [CSLibExt/Computability/Decidability/Reductions.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Reductions.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html#not-tm2-decidable-regular-domain).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Halting problem and Rice's theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/computability/halting-problem-and-rice-s-theorem)
