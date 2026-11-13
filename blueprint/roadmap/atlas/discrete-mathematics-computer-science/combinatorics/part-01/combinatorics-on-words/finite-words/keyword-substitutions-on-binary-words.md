---
declaration: section
origin: cited
lean: MetaMathlibExt.KeywordApplicable, MetaMathlibExt.keywordSimpleMap, MetaMathlibExt.keywordSimpleMap_of_not_applicable, MetaMathlibExt.keywordSimpleMap_apply_of_applicable, MetaMathlibExt.KeywordEquiv, MetaMathlibExt.keywordEquiv_refl, MetaMathlibExt.keywordGraph, MetaMathlibExt.keywordGraph_adj
statement: formalized
---

# Keyword substitutions on binary words

21 results, 12 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html).

## Applicability of a keyword

Let $a = a_0 a_1 \cdots a_m$ be a binary keyword of length
$m + 1$ and $u = u_0 u_1 \cdots u_{n-1}$ a binary word of length $n$. The keyword $a$ is
applicable to $u$ at the ($0$-indexed) letter $i$ when $i + m < n$ and the subword
$u_i u_{i+1} \cdots u_{i+m}$ of $u$ equals $a$ or the letterwise negation of $a$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.1 (definition of substitutions involving the keyword).

Formalized by `MetaMathlibExt.KeywordApplicable`, a definition declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-applicable).

## Simple map

Let $a$ be a keyword, a binary word of length $m + 1$, and let
$i \in \mathbb{N}$. The simple map $\varphi_i$ sends a binary word $u$ of length $n$ to the word
obtained by negating the letters of $u$ at positions $i, \dots, i + m$ (positions counted from
$0$) if $a$ is applicable to $u$ at letter $i$, that is, if $i + m < n$ and the subword of $u$ at
positions $i, \dots, i + m$ equals $a$ or its letterwise negation $\neg a$; otherwise
$\varphi_i(u) = u$.

The paper counts letters from $1$, so its simple map $\varphi_i$ is $\varphi_{i-1}$ in this
numbering.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.1 (simple maps).

Formalized by `MetaMathlibExt.keywordSimpleMap`, a definition declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-simple-map).

## A simple map that is not applicable is the identity

Let $a$ be a keyword and $u$ a binary
word. If $a$ is not applicable to $u$ at letter $i$, then the simple map $\varphi_i$ of $a$ leaves
$u$ unchanged: $\varphi_i(u) = u$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.1 (simple maps).

Formalized by `MetaMathlibExt.keywordSimpleMap_of_not_applicable`, a theorem declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-simple-map-of-not-applicable).

## An applicable simple map negates its window

Let $a$ be a keyword of length $m + 1$ and $u$
a binary word of length $n$, and suppose that $a$ is applicable to $u$ at letter $i$. Then the
simple map $\varphi_i$ of $a$ negates the letters of $u$ at positions $i, \dots, i + m$ and leaves
every other letter unchanged: for every position $j$, $\varphi_i(u)_j = \neg u_j$ if
$i \le j \le i + m$, and $\varphi_i(u)_j = u_j$ otherwise.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.1 (simple maps).

Formalized by `MetaMathlibExt.keywordSimpleMap_apply_of_applicable`, a theorem declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-simple-map-apply-of-applicable).

## Keyword equivalence of binary words

Let $a$ be a binary keyword of length $m + 1$.
Two binary words $u$ and $v$ of length $n$ satisfy $u \sim_a v$ when some finite composition
of simple maps of $a$, possibly the empty composition, sends $u$ to $v$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.1 (equivalence relation induced by the keyword).

Formalized by `MetaMathlibExt.KeywordEquiv`, a definition declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-equiv).

## Reflexivity of keyword equivalence

For every binary keyword $a$ and every binary word
$u$, we have $u \sim_a u$: the empty composition of simple maps sends $u$ to itself.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.1 (equivalence relation induced by the keyword).

Formalized by `MetaMathlibExt.keywordEquiv_refl`, a theorem declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-equiv-refl).

## Substitution graph

Let $a$ be a keyword, a binary word of length $m + 1$, and let
$n \ge 0$. The substitution graph $\mathcal{G}_n^{(a)}$ is the simple graph on the binary words of
length $n$ in which distinct words $u$ and $v$ are adjacent when $\varphi_i(u) = v$ or
$\varphi_i(v) = u$ for some $i \in \mathbb{N}$, where $\varphi_i$ is the simple map of $a$ at
letter $i$. Equivalently, $u$ and $v$ are adjacent when one is obtained from the other by
replacing an occurrence of $a$ by $\neg a$ or an occurrence of $\neg a$ by $a$, where $\neg a$ is
the letterwise negation of $a$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 3.2 (graph structure within equivalence classes).

Formalized by `MetaMathlibExt.keywordGraph`, a definition declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-graph).

## Adjacency in the keyword substitution graph

Let $a$ be a binary keyword and let $u$
and $v$ be binary words of length $n$. Then $u$ and $v$ are adjacent in the graph
$\mathcal{G}_n^{(a)}$ if and only if $u \ne v$ and some simple map $\varphi_i$ of $a$ sends $u$
to $v$ or sends $v$ to $u$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 3.2 (graph structure within equivalence classes).

Formalized by `MetaMathlibExt.keywordGraph_adj`, a theorem declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-graph-adj).

## Action of a list of simple maps

Let $a$ be a keyword and, for $j \in \mathbb{N}$, let
$\varphi_j$ be the simple map of $a$ at letter $j$. A list $[j_1, \dots, j_r]$ of natural numbers
acts on a binary word $u$ of length $n$ by
$u \mapsto \varphi_{j_r}(\cdots(\varphi_{j_1}(u))\cdots)$: the head of the list acts first, and
the empty list acts as the identity.

The paper writes this list as $(\varphi_{j_r}, \dots, \varphi_{j_1})$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.2 (action by lists of simple maps).

Formalized by `MetaMathlibExt.keywordListApply`, a definition declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-list-apply).

## Lists of simple maps acting completely

Let $a$ be a binary keyword and $u$ a binary
word. A list $[j_1, \dots, j_r]$ of indices acts completely on $u$ when applying the simple maps
$\varphi_{j_1}, \varphi_{j_2}, \dots, \varphi_{j_r}$ of $a$ in this order changes the word at
every step: with $u_0 = u$ and $u_q = \varphi_{j_q}(u_{q-1})$, we have $u_q \ne u_{q-1}$ for
$1 \le q \le r$. In particular the empty list acts completely on every word.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.2 (action by lists of simple maps).

Formalized by `MetaMathlibExt.KeywordActsCompletely`, a definition declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-acts-completely).

## The empty list of simple maps acts trivially

For every keyword $a$ and every binary word
$u$, applying the empty list of simple maps of $a$ to $u$ returns $u$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.2 (action by lists of simple maps).

Formalized by `MetaMathlibExt.keywordListApply_nil`, a theorem declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-list-apply-nil).

## Complete action of a one-element list

For a binary keyword $a$, an index $j$ and a
binary word $u$, the one-element list $[j]$ acts completely on $u$ if and only if the simple map
$\varphi_j$ of $a$ changes $u$, that is, $\varphi_j(u) \ne u$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Section 2.2 (action by lists of simple maps).

Formalized by `MetaMathlibExt.keywordActsCompletely_singleton`, a theorem declared in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-acts-completely-singleton).

## Keyword classes are counted by partial sums of $m$-step Fibonacci numbers

Let
$m, n \ge 1$ and let $F_0, F_1, F_2, \dots$ be the $m$-step Fibonacci numbers: $F_0 = 1$,
$F_k = 2^{k-1}$ for $1 \le k \le m - 1$, and $F_k = F_{k-1} + F_{k-2} + \dots + F_{k-m}$ for
$k \ge m$. Then for every binary keyword $a$ of length $m + 1$, the number of equivalence
classes of the relation $\sim_a$ on binary words of length $n$ is $F_0 + F_1 + \dots + F_n$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Theorem 1 (`jis-2025-25.6.6-thm-1`).

Stated but not proved: `MetaMathlibExt.card_quot_keywordEquiv_eq_sum_mStepFibonacci` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#card-quot-keyword-equiv-eq-sum-m-step-fi).

## Keyword equivalence is stable under concatenation

Let $a$ be a binary keyword, let $u$
and $v$ be binary words of length $n$, and let $w$ be a binary word of length $n'$. Writing $xy$
for the concatenation of words $x$ and $y$, we have $u \sim_a v$ if and only if
$uw \sim_a vw$, and $u \sim_a v$ if and only if $wu \sim_a wv$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Lemma 6 (`jis-2025-25.6.6-lem-6`).

Stated but not proved: `MetaMathlibExt.keywordEquiv_append_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-equiv-append-iff).

## Parity of the smallest index in a non-commuting list

Let $a$ be a binary keyword of
length $m + 1$, let $n$ and $i$ be natural numbers with $i < n$, and for each index $k$ let
$\varphi_k$ be the simple map of $a$ at letter $k$ on binary words of length $n$. Let
$l = [j_1, \dots, j_r]$ be a list of indices that are all greater than $i$, and let
$\varphi_l = \varphi_{j_r} \circ \dots \circ \varphi_{j_1}$ be the map that applies
$\varphi_{j_1}$ first. Suppose that $\varphi_i \circ \varphi_l \ne \varphi_l \circ \varphi_i$
as maps on words of length $n$, and that the list $[i, j_1, \dots, j_r, i]$, applied from left
to right, acts completely on some word of length $n$ (each map in turn changes the word). Then
every entry $j$ of $l$ with $j \le j'$ for all entries $j'$ of $l$ occurs an even number of
times in $l$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Lemma 8 (`jis-2025-25.6.6-lem-8`).

Stated but not proved: `MetaMathlibExt.even_count_min_of_keywordActsCompletely` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#even-count-min-of-keyword-acts-completel).

## Recurrence for partial sums of $m$-step Fibonacci numbers

Let $m \ge 1$ and let
$F : \mathbb{N} \to \mathbb{N}$ satisfy $F(0) = 1$, $F(k) = 2^{k-1}$ for $1 \le k \le m - 1$,
and $F(k) = F(k-1) + \cdots + F(k-m)$ for $k \ge m$ (the $m$-step Fibonacci numbers). Then a
real sequence $(S_n)_{n \ge 0}$ satisfies $S_n = F(0) + F(1) + \cdots + F(n)$ for all $n$ if
and only if $S_n = 2^n$ for $0 \le n \le m$ and $S_n = 2 S_{n-1} - S_{n-m-1}$ for $n \ge m + 1$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Lemma 9 (`jis-2025-25.6.6-lem-9`).

Stated but not proved: `MetaMathlibExt.sum_mStepFibonacci_iff_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#sum-m-step-fibonacci-iff-recurrence).

## Keywords with equally many singleton classes

Let $a$ and $b$ be binary keywords of
length $m + 1$. The relations $\sim_a$ and $\sim_b$ have the same number of one-element
equivalence classes on binary words of length $n$ for every $n \ge 0$ if and only if, for every
$i$ with $1 \le i \le m + 1$, the following holds for $a$ exactly when it holds for $b$: the
prefix of length $i$ of the keyword equals its suffix of length $i$ or the letterwise negation
of that suffix.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Proposition 10 (`jis-2025-25.6.6-prop-10`).

Stated but not proved: `MetaMathlibExt.card_singleton_classes_eq_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#card-singleton-classes-eq-iff).

## When two simple maps commute

Let $a$ be a keyword of length $m + 1$ and let $n$ be a
natural number. Let $i < j$ be natural numbers with $j + m < n$, and put $\Delta = j - i$. The
simple maps $\varphi_i$ and $\varphi_j$ of $a$ on binary words of length $n$ satisfy
$\varphi_i \circ \varphi_j = \varphi_j \circ \varphi_i$ if and only if $\Delta \ge m + 1$, or the
prefix of $a$ of length $m + 1 - \Delta$ differs both from the suffix of $a$ of length
$m + 1 - \Delta$ and from the letterwise negation of that suffix.

In the paper's numbering, which counts letters from $1$, the hypothesis reads $i < j \le n - m$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Proposition 12 (`jis-2025-25.6.6-prop-12`).

Stated but not proved: `MetaMathlibExt.keywordSimpleMap_comm_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-simple-map-comm-iff).

## Keyword symmetries of the substitution graph

Let $a = a_0 a_1 \cdots a_m$ be a keyword of
length $m + 1$ and let $n \ge 0$. Write $\neg a$ for the letterwise negation of $a$,
$\rho(a) = a_m a_{m-1} \cdots a_0$ for its reversal, and $\bar a$ for its seminegation, which keeps
$a_t$ for even $t$ and negates $a_t$ for odd $t$. Then the substitution graphs satisfy
$\mathcal{G}_n^{(a)} = \mathcal{G}_n^{(\neg a)}$, and $\mathcal{G}_n^{(a)}$ is isomorphic both to
$\mathcal{G}_n^{(\rho(a))}$ and to $\mathcal{G}_n^{(\bar a)}$.

In the paper's numbering, which counts letters from $1$, the seminegation negates the letters in
even positions. The paper states this for $n \ge 1$; it also holds at $n = 0$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Proposition 15 (`jis-2025-25.6.6-prop-15`).

Stated but not proved: `MetaMathlibExt.keywordGraph_neg_rev_seminegation` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-graph-neg-rev-seminegation).

## Intertwining bijections preserve distances in the substitution graph

Let $a$ and $b$ be
keywords of length $m + 1$, and write $\varphi_i^{(a)}$ and $\varphi_i^{(b)}$ for the simple maps
of $a$ and $b$ at letter $i$ on binary words of length $n$. Let $f$ be a bijection of the set of
binary words of length $n$ and $\sigma$ a permutation of the positions $\{0, \dots, n - 1\}$, and
suppose that $f(\varphi_i^{(a)}(u)) = \varphi_{\sigma(i)}^{(b)}(f(u))$ for every word $u$ and
every position $i$. Then for all words $u$ and $v$ of length $n$, the extended graph distance
(possibly $\infty$) between $u$ and $v$ in the substitution graph $\mathcal{G}_n^{(a)}$ equals the
extended graph distance between $f(u)$ and $f(v)$ in $\mathcal{G}_n^{(b)}$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Lemma 16 (`jis-2025-25.6.6-lem-16`).

Stated but not proved: `MetaMathlibExt.keywordGraph_edist_eq_of_intertwining` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-graph-edist-eq-of-intertwining).

## The substitution graph is bipartite

For every keyword $a$ of length $m + 1$ and every
$n \ge 0$, the substitution graph $\mathcal{G}_n^{(a)}$ on binary words of length $n$ is
bipartite.

The paper states this for $n \ge 1$; it also holds at $n = 0$.

## Sources

- Erik Bates, Blan Morrison, Mason Rogers, Arianna Serafini and Anav Sood, *A New Combinatorial Interpretation of Partial Sums of m-Step Fibonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.6.6, Proposition 17 (`jis-2025-25.6.6-prop-17`).

Stated but not proved: `MetaMathlibExt.keywordGraph_isBipartite` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/KeywordSubstitutionClassesWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html#keyword-graph-is-bipartite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Keyword substitutions on binary words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/keyword-substitutions-on-binary-words)
