---
declaration: section
origin: cited
lean: MetaMathlibExt.bijective_finset_sum_iff_eq_two_pow, MetaMathlibExt.bijective_nonadjacent_finset_sum_iff_eq_fib, MetaMathlibExt.card_zeckendorfBinary_lt_sum_two_pow, MetaMathlibExt.AscLexLT, MetaMathlibExt.ascLexLT_example, MetaMathlibExt.IsImmediatePredecessor, MetaMathlibExt.IsImmediateSuccessor, MetaMathlibExt.IsZeckendorfCollection
statement: formalized
---

# Distribution of Zeckendorf expressions

91 results, 45 proved and 46 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html).

## Powers of two are the only binary fundamental sequence

Let
$H \colon \mathbb{N} \to \mathbb{N}$ be a strictly increasing sequence of positive integers. Then
every natural number (including $0$) equals $\sum_{k \in s} H_k$ for exactly one finite set
$s \subseteq \mathbb{N}$ if and only if $H_k = 2^k$ for all $k$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 1.

Stated but not proved: `MetaMathlibExt.bijective_finset_sum_iff_eq_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#bijective-finset-sum-iff-eq-two-pow).

## The Fibonacci numbers are the only Zeckendorf fundamental sequence

Let
$H \colon \mathbb{N} \to \mathbb{N}$ be a strictly increasing sequence of positive integers, and
call a finite set $s \subseteq \mathbb{N}$ nonadjacent if $k \in s$ implies $k + 1 \notin s$.
Then every natural number (including $0$) equals $\sum_{k \in s} H_k$ for exactly one nonadjacent
finite set $s$ if and only if $H_k = F_{k+2}$ for all $k$, where $F_0 = 0$, $F_1 = 1$ and
$F_{n+2} = F_{n+1} + F_n$ are the Fibonacci numbers.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 1.

Stated but not proved: `MetaMathlibExt.bijective_nonadjacent_finset_sum_iff_eq_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#bijective-nonadjacent-finset-sum-iff-eq).

## Duality formula for binary expansions without adjacent ones

For $x \in \mathbb{N}$ let
$z(x)$ be the number of $n < x$ whose binary expansion has no two adjacent digits equal to $1$.
For a finite set $A \subseteq \mathbb{N}$, put $\bar A = A$ if there is no $j$ with
$j, j + 1 \in A$, and otherwise $\bar A = \{k \in A : k \ge j\}$, where $j$ is the largest index
with $j, j + 1 \in A$. Then $z\bigl(\sum_{k \in A} 2^k\bigr) = \sum_{k \in \bar A} F_{k+2}$,
where $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$ are the Fibonacci numbers.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 2.

Stated but not proved: `MetaMathlibExt.card_zeckendorfBinary_lt_sum_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#card-zeckendorf-binary-lt-sum-two-pow).

## Ascending lexicographic order

For coefficient functions
$\mu, \nu \colon \mathbb{N} \to \mathbb{N}$ with finite support, $\mu \lt _a \nu$ means that there
is an index $k$ with $\mu_k < \nu_k$ and $\mu_j = \nu_j$ for all $j > k$: at the largest index
where they differ, $\mu$ is smaller.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.2).

Formalized by `MetaMathlibExt.AscLexLT`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#asc-lex-lt).

## Example of the ascending lexicographic order

Write $(a_0, a_1, a_2, a_3, a_4)$ for the
coefficient function with finite support whose entry at index $i \le 4$ is $a_i$ and whose other
entries are $0$. Then $(1, 2, 10, 3, 7) \lt _a (1, 3, 1, 4, 7)$ in the ascending lexicographic
order: the largest index where they differ is $3$, where $3 < 4$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.2, example).

Formalized by `MetaMathlibExt.ascLexLT_example`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#asc-lex-lt-example).

## Immediate predecessor

Let $E$ be a collection of finitely supported coefficient functions
$\mathbb N \to \mathbb N$, and let $\lt _a$ be the ascending lexicographic order. A finitely supported
coefficient function $\mu$ is the immediate predecessor of $\nu$ in $E$ if $\mu \in E$,
$\mu \lt _a \nu$, and every $\xi \in E$ with $\xi \lt _a \nu$ satisfies $\xi = \mu$ or $\xi \lt _a \mu$.
That is, $\mu$ is the largest element of $E$ that is $\lt _a \nu$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.2).

Formalized by `MetaMathlibExt.IsImmediatePredecessor`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-immediate-predecessor).

## Immediate successor

Let $E$ be a collection of finitely supported coefficient functions
$\mathbb N \to \mathbb N$, and let $\lt _a$ be the ascending lexicographic order. A finitely supported
coefficient function $\nu$ is the immediate successor of $\mu$ in $E$ if $\nu \in E$,
$\mu \lt _a \nu$, and every $\xi \in E$ with $\mu \lt _a \xi$ satisfies $\xi = \nu$ or $\nu \lt _a \xi$.
That is, $\nu$ is the smallest element of $E$ that is $>_a \mu$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.2).

Formalized by `MetaMathlibExt.IsImmediateSuccessor`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-immediate-successor).

## Zeckendorf collections

Index coefficient functions from $1$, let $\beta^n$ be the basis
coefficient function with entry $1$ at index $n$, and for a coefficient function $\mu$ let
$\operatorname{res}_n(\mu)$ keep the entries of $\mu$ at indices $\le n$ and
$\operatorname{res}^n(\mu)$ keep those at indices $\ge n$, the other entries being $0$. A set $E$
of finitely supported coefficient functions $\mathbb N \to \mathbb N$ is a Zeckendorf collection
when it contains $0$ and $\beta^n$ for every $n \ge 1$, every $\mu \in E$ has only finitely many
elements of $E$ below it in the ascending lexicographic order $\lt _a$, and for every $\mu \in E$
and every immediate successor $\tilde\mu$ of $\mu$ in $E$ with $\tilde\mu \ne \beta^1 + \mu$
there is an index $n \ge 2$ such that $\operatorname{res}_{n-1}(\mu)$ is the immediate
predecessor of $\beta^n$ in $E$ and $\tilde\mu = \beta^n + \operatorname{res}^n(\mu)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.2).

Formalized by `MetaMathlibExt.IsZeckendorfCollection`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-zeckendorf-collection).

## Zeckendorf collections contain zero

Every Zeckendorf collection $E$ of finitely supported
coefficient functions $\mathbb N \to \mathbb N$ contains the zero coefficient function.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.2).

Formalized by `MetaMathlibExt.IsZeckendorfCollection.zero_mem`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zero-mem).

## The maximal $L$-block $\theta^{m+1}$

Let $L = (e_1, \dots, e_N)$ be a list of natural
numbers and $m \in \mathbb N$, with indices of coefficient functions starting at $0$. The maximal
$L$-block $\theta^{m+1}$ is the finitely supported coefficient function whose entry at each index
$i < m$ is $e_j$, where $j - 1 = (m - 1 - i) \bmod N$, and whose entries at the indices $i \ge m$
are $0$ (every entry is $0$ when $L$ is empty).

In the paper's one-based indexing, $\theta^n = \mathrm{rev}_{n-1}(\beta^*)$, where $\beta^*$ is
the coefficient function with $\beta^*_k = e_j$ for $k \equiv j \pmod N$ and
$\mathrm{rev}_{n-1}(\beta^*)$ lists the first $n - 1$ entries of $\beta^*$ in reverse order,
followed by zeros.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 10 (arXiv:2308.12872v1, Section 2.2).

Formalized by `MetaMathlibExt.periodicTheta`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#periodic-theta).

## The maximal block $\theta^4$ in the Fibonacci case

For $L = (1, 0)$, the maximal $L$-block
$\theta^4$ is $(1, 0, 1)$: its entries at indices $0$, $1$, $2$ are $1$, $0$, $1$, and all its
entries from index $3$ on are $0$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 10 (arXiv:2308.12872v1, Section 2.2).

Formalized by `MetaMathlibExt.periodicTheta_one_zero_three`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#periodic-theta-one-zero-three).

## L-blocks

Let $L$ be a list of natural numbers, and for each $m$ let $\theta^{m+1}$ be the
maximal $L$-block, which vanishes from index $m$ on (indices are zero-based). A finitely supported
coefficient function $\zeta$ is an $L$-block with support interval $[s, m - 1]$ if $1 \le m$,
$s < m$, and either $s = 0$ and $\zeta = \theta^{m+1}$, or $\zeta_i = \theta^{m+1}_i$ for every
$i > s$, $\zeta_s < \theta^{m+1}_s$ and $\zeta_i = 0$ for every $i < s$.

In the paper's indexing this is a block at index $n - 1$ with $n = m + 1 \ge 2$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 10 (arXiv:2308.12872v1, Section 2.2).

Formalized by `MetaMathlibExt.IsLBlock`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-lblock).

## Periodic Zeckendorf collection

For a list $L$ of natural numbers, the periodic Zeckendorf
collection determined by $L$ is the set of finitely supported coefficient functions $\mu$ that
can be written as a sum $\mu = \zeta_1 + \dots + \zeta_r$ of finitely many $L$-blocks
$\zeta_1, \dots, \zeta_r$ (possibly none, which gives $\mu = 0$) whose support intervals are
pairwise disjoint.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 4 and the definition following it (arXiv:2308.12872v1, Section 2.2).

Formalized by `MetaMathlibExt.periodicZeckendorfCollection`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#periodic-zeckendorf-collection).

## Evaluation of a coefficient function at an integer sequence

For a sequence $H$ of
natural numbers and a finitely supported coefficient function
$\varepsilon \colon \mathbb{N} \to \mathbb{N}$, the evaluation of $\varepsilon$ at $H$ is the
natural number $\mathrm{eval}_H(\varepsilon) = \sum_{k \ge 0} \varepsilon_k H_k$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 1 (arXiv:2308.12872v1, Section 1).

Formalized by `MetaMathlibExt.zeckendorfEval`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-eval).

## Zeckendorf collections are determined by their immediate predecessors

Index
coefficient functions from $0$, and for $m \in \mathbb N$ let $\beta^{(m)}$ be the coefficient
function with entry $1$ at index $m$ and $0$ elsewhere. Suppose that for each $m \ge 1$ a finitely
supported coefficient function $\theta^{(m)}$ is given whose entry at index $m - 1$ is nonzero and
whose entries at all indices $j \ge m$ are $0$. Then there is a unique Zeckendorf collection $E$
such that, for every $m \ge 1$, $\theta^{(m)}$ is the immediate predecessor of $\beta^{(m)}$ in
$E$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 3 (arXiv:2308.12872v1, Section 2.2, quoting Chang 2021).

Stated but not proved: `MetaMathlibExt.existsUnique_zeckendorfCollection` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#exists-unique-zeckendorf-collection).

## Periodic collections are Zeckendorf collections

Let $L = (e_1, \dots, e_N)$ be a list of
natural numbers with $N \ge 2$ and $e_1 \ne 0$, and let $E$ be the periodic Zeckendorf collection
determined by $L$ (the sums of finitely many $L$-blocks with pairwise disjoint support
intervals). Index coefficient functions from $1$ and let $\beta^n$ be the basis coefficient
function with entry $1$ at index $n$. Then $E$ is a Zeckendorf collection, and for every
$n \ge 2$ the immediate predecessor of $\beta^n$ in $E$ is the maximal $L$-block $\theta^n$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 4 (arXiv:2308.12872v1, Section 2.2, quoting Chang 2021).

Stated but not proved: `MetaMathlibExt.isZeckendorfCollection_periodic` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-zeckendorf-collection-periodic).

## Fundamental sequences of Zeckendorf collections

Let $E$ be a Zeckendorf collection and
index coefficient functions and sequences from $0$. Suppose that, for each $m \ge 1$,
$\theta^{(m)}$ is the immediate predecessor in $E$ of the coefficient function with entry $1$ at
index $m$ and $0$ elsewhere. For a sequence $H$ write $\mathrm{eval}_H(\mu) = \sum_k \mu_k H_k$.
Then there is a unique strictly increasing sequence $H$ of positive integers such that
$\mathrm{eval}_H$ is a bijection from $E$ onto $\mathbb N$. Moreover, every such $H$ satisfies
$H_m = H_0 + \mathrm{eval}_H(\theta^{(m)})$ for all $m \ge 1$, and for all $\mu, \nu \in E$,
$\mu \lt _a \nu$ (that is, $\mu_k < \nu_k$ at the largest index $k$ where $\mu$ and $\nu$ differ)
if and only if $\mathrm{eval}_H(\mu) < \mathrm{eval}_H(\nu)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 5 (arXiv:2308.12872v1, Section 2.2, quoting Chang 2021).

Stated but not proved: `MetaMathlibExt.existsUnique_zeckendorf_fundamentalSequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#exists-unique-zeckendorf-fundamental-seq).

## Criterion for one Zeckendorf collection to contain another

Let $E$ and $\tilde E$ be
Zeckendorf collections. For $n \ge 2$ let $\beta^n$ be the basis coefficient function with entry
$1$ at position $n$ (positions counted from $1$) and $0$ elsewhere, and let $\hat\beta^n$ be the
immediate predecessor of $\beta^n$ in $E$ (the largest element of $E$ that is $\lt _a \beta^n$ in the
ascending lexicographic order). Then $E \subseteq \tilde E$ if and only if
$\hat\beta^n \in \tilde E$ for all $n \ge 2$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 1 (arXiv:2308.12872v1, Section 2.2).

Stated but not proved: `MetaMathlibExt.zeckendorfCollection_subset_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-collection-subset-iff).

## Counting function of a subcollection

For a set $E$ of finitely supported coefficient
functions $\mu : \mathbb{N} \to \mathbb{N}$, a sequence $H : \mathbb{N} \to \mathbb{N}$ and a
real number $x$, $z(x)$ is the number of natural numbers $n < x$ of the form
$n = \sum_k \mu_k H_k$ for some $\mu \in E$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 1 and Section 3 (arXiv:2308.12872v1, Sections 1 and 3.2).

Formalized by `MetaMathlibExt.subcollectionCount`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#subcollection-count).

## The counting function $z$ vanishes for $x \le 0$

Let $E$ be a set of finitely supported
coefficient functions and $H$ a sequence of natural numbers, and for real $x$ let $z(x)$ be the
number of natural numbers $n < x$ of the form $n = \sum_k \mu_k H_k$ with $\mu \in E$. Then
$z(x) = 0$ for every real $x \le 0$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 3 (arXiv:2308.12872v1, Section 3.2).

Formalized by `MetaMathlibExt.subcollectionCount_of_nonpos`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#subcollection-count-of-nonpos).

## Power-law bounds for the subcollection count

Let $L$ and $\tilde L$ be lists of natural
numbers of length at least $2$ with nonzero first entries, and let $E$ and $\tilde E$ be the
periodic Zeckendorf collections they determine, with $E$ a proper subset of $\tilde E$. Let
$\tilde H$ be a strictly increasing sequence of positive integers such that
$\mu \mapsto \sum_k \mu_k \tilde H_k$ is a bijection from $\tilde E$ onto $\mathbb N$, and let
$z(x)$ be the number of natural numbers $n < x$ of the form $\sum_k \mu_k \tilde H_k$ with
$\mu \in E$. Then there are reals $\gamma$, $a$ and $b$ with $0 < \gamma < 1$, $a > 0$ and $b > 0$
such that $a < z(x) / x^\gamma < b$ for all sufficiently large real $x$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 1 (arXiv:2308.12872v1, Section 1, with the standing assumption of Section 3 that `E` is a proper subcollection).

Stated but not proved: `MetaMathlibExt.exists_rpow_bounds_subcollectionCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#exists-rpow-bounds-subcollection-count).

## Limsup of the count of binary expansions without adjacent ones

For real $x$ let $z(x)$
be the number of natural numbers $n < x$ (including $0$) whose binary expansion has no two
adjacent $1$s, let $\varphi$ be the golden ratio and let $\gamma = \log_2 \varphi$. Then
$\limsup_{x \to \infty} z(x) / x^{\gamma} = 3^{\gamma} (\varphi + 2) / 5$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 1, Equation (1) (arXiv:2308.12872v1, Section 1).

Stated but not proved: `MetaMathlibExt.limsup_zeckendorfBinaryCount_div_rpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#limsup-zeckendorf-binary-count-div-rpow).

## Liminf of the count of binary expansions without adjacent ones

For real $x$ let $z(x)$
be the number of natural numbers $n < x$ (including $0$) whose binary expansion has no two
adjacent $1$s, let $\varphi$ be the golden ratio and let $\gamma = \log_2 \varphi$. Then
$\liminf_{x \to \infty} z(x) / x^{\gamma} = (3\varphi + 1) / 5$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 1, Equation (1) (arXiv:2308.12872v1, Section 1).

Stated but not proved: `MetaMathlibExt.liminf_zeckendorfBinaryCount_div_rpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#liminf-zeckendorf-binary-count-div-rpow).

## Asymptotic form of the subcollection count

Let $L$ and $\tilde L$ be lists of natural
numbers of length at least $2$ with nonzero first entries, and let $E$ and $\tilde E$ be the
periodic Zeckendorf collections they determine, with $E$ a proper subset of $\tilde E$. Let
$\tilde H$ be a strictly increasing sequence of positive integers such that
$\mu \mapsto \sum_k \mu_k \tilde H_k$ is a bijection from $\tilde E$ onto $\mathbb N$, and let
$z(x)$ be the number of natural numbers $n < x$ of the form $\sum_k \mu_k \tilde H_k$ with
$\mu \in E$. Then there are reals $\gamma$ and $\tilde\varphi$ with $0 < \gamma < 1$ and
$\tilde\varphi > 1$, and a continuous function $\Phi : \mathbb R \to \mathbb R$, such that
$z(x) \sim x^\gamma \Phi(\{\log_{\tilde\varphi} x\})$ as $x \to \infty$, where $\{t\}$ is the
fractional part of $t$, and $\Phi$ is differentiable at almost every point of $(0, 1)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 2 (arXiv:2308.12872v1, Section 1).

Stated but not proved: `MetaMathlibExt.exists_isEquivalent_subcollectionCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#exists-is-equivalent-subcollection-count).

## Growth of fundamental sequences

Let $L$ and $\tilde L$ be lists of natural numbers of
length at least $2$ with nonzero first entries, and let $E$ and $\tilde E$ be the periodic
Zeckendorf collections they determine, with $E$ a proper subset of $\tilde E$. Let $H$ and
$\tilde H$ be strictly increasing sequences of positive integers, indexed from $0$, such that
$\mu \mapsto \sum_k \mu_k H_k$ is a bijection from $E$ onto $\mathbb N$ and
$\mu \mapsto \sum_k \mu_k \tilde H_k$ is a bijection from $\tilde E$ onto $\mathbb N$. Then there
are reals $\alpha > 0$, $\tilde\alpha > 0$, $\varphi$, $\tilde\varphi$ and $r$ with
$1 < \varphi < \tilde\varphi$ and $0 < r < 1$ such that, as $n \to \infty$,
$H_n - \alpha \varphi^n = O(\varphi^{nr})$, $\tilde H_n - \tilde\alpha \tilde\varphi^n =
O(\tilde\varphi^{nr})$ and, with $\gamma = \log_{\tilde\varphi} \varphi$,
$H_n / \tilde H_n^{\gamma} \to \alpha / \tilde\alpha^{\gamma}$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 7 (arXiv:2308.12872v1, Section 3.1).

Stated but not proved: `MetaMathlibExt.fundamentalSequence_div_rpow_tendsto` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#fundamental-sequence-div-rpow-tendsto).

## Reduction lemma for counting a subcollection

Let $E \subseteq \tilde E$ be Zeckendorf
collections, and let $\tilde H$ be a strictly increasing sequence of positive integers such that
$\varepsilon \mapsto \sum_k \varepsilon_k \tilde H_k$ is a bijection from $\tilde E$ onto
$\mathbb{N}$. For a natural number $x$ let $R(x)$ be the set of natural numbers $n < x$ of the
form $n = \sum_k \varepsilon_k \tilde H_k$ with $\varepsilon \in E$. Let $\mu \in \tilde E$ be
nonzero, suppose that $\mu$ has an immediate predecessor $\check\mu$ in $E$ (the largest element
of $E$ that is $\lt _a \mu$ in the ascending lexicographic order), and suppose that $\check\mu$ has
an immediate successor $\bar\mu$ in $E$ (the smallest element of $E$ that is $>_a \check\mu$).
Then $R(\sum_k \mu_k \tilde H_k) = R(\sum_k \bar\mu_k \tilde H_k)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 7 (arXiv:2308.12872v1, Section 3.2, with the paper's definition of `μ̌` and `μ̄` there).

Stated but not proved: `MetaMathlibExt.subcollectionLT_eval_eq_eval_bar` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#subcollection-lt-eval-eq-eval-bar).

## Duality formula

Let $E \subseteq \tilde E$ be Zeckendorf collections. Let $H$ and
$\tilde H$ be strictly increasing sequences of positive integers such that
$\mu \mapsto \sum_k \mu_k H_k$ is a bijection from $E$ onto $\mathbb N$ and
$\mu \mapsto \sum_k \mu_k \tilde H_k$ is a bijection from $\tilde E$ onto $\mathbb N$. For real
$x$, let $z(x)$ be the number of natural numbers $n < x$ of the form $n = \sum_k \nu_k \tilde H_k$
with $\nu \in E$. Let $\mu \in \tilde E$ be nonzero, let $\check\mu$ be the immediate predecessor
of $\mu$ in $E$ (the largest element of $E$ below $\mu$ in the ascending lexicographic order), and
let $\bar\mu$ be the immediate successor of $\check\mu$ in $E$. Then
$z\left(\sum_k \mu_k \tilde H_k\right) = \sum_k \bar\mu_k H_k$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 8 (arXiv:2308.12872v1, Section 3.2).

Stated but not proved: `MetaMathlibExt.subcollectionCount_eval_eq_eval_bar` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#subcollection-count-eval-eq-eval-bar).

## Descending lexicographic order

For coefficient functions
$\varepsilon, \varepsilon' \colon \mathbb{N} \to \mathbb{N}$, $\varepsilon \lt _d \varepsilon'$
means that there is an index $k$ with $\varepsilon_k < \varepsilon'_k$ and
$\varepsilon_j = \varepsilon'_j$ for all $j < k$: at the smallest index where they differ,
$\varepsilon$ is smaller.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.3).

Formalized by `MetaMathlibExt.DescLexLT`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#desc-lex-lt).

## The maximal $L^*$-block

**The maximal $L^*$-block.** Let $L = (e_1, \dots, e_N)$ be a list of natural numbers and $s$
an index, with indices starting at $0$. The maximal $L^*$-block starting at $s$ is the
coefficient function whose entry at index $i$ is $0$ for $i < s$, and $e_j$ for $i \ge s$, where
$j - 1 = (i - s) \bmod N$ (every entry is $0$ when $L$ is empty). It is the paper's
$\bar\beta^{s+1}$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.3).

Formalized by `MetaMathlibExt.maxLStarBlock`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#max-lstar-block).

## The maximal block $\bar\beta^2$ for $L = (2, 3, 0)$

For $L = (2, 3, 0)$, the maximal
$L^*$-block starting at index $1$ (indices start at $0$; the paper's $\bar\beta^2$) has entries
$0, 2, 3, 0, 2$ at the indices $0, 1, 2, 3, 4$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.3, example).

Formalized by `MetaMathlibExt.maxLStarBlock_example`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#max-lstar-block-example).

## Proper $L^*$-blocks

**Proper $L^*$-blocks.** Let $L$ be a list of natural numbers, index coefficient functions
from $1$, and let $\bar\beta^s$ be the maximal $L^*$-block starting at index $s$. For $s \ge 1$,
a function $\zeta : \mathbb N \to \mathbb N$ is a proper $L^*$-block with support interval
$[s, k]$ when $s \le k$, $\zeta_i = \bar\beta^s_i$ for all $i < k$, $\zeta_k < \bar\beta^s_k$,
and $\zeta_i = 0$ for all $i > k$. Since $\bar\beta^s$ vanishes below $s$, so does $\zeta$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.3).

Formalized by `MetaMathlibExt.IsProperLStarBlock`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-proper-lstar-block).

## Sums of disjoint proper $L^\ast$-blocks

Let $L$ be a list of natural numbers, and for
each $s$ let $\bar\beta^{s+1}$ be the maximal $L^*$-block starting at (zero-based) index $s$. Let
$I$ be a finite or infinite set of pairs $(s, k)$ of natural numbers. A coefficient function
$\varepsilon : \mathbb N \to \mathbb N$ is the sum of the disjoint proper $L^*$-blocks with
support intervals $[s, k]$, $(s, k) \in I$, if $s \le k$ for every $(s, k) \in I$, the intervals
$[s, k]$ of distinct pairs in $I$ are pairwise disjoint, for every $(s, k) \in I$ we have
$\varepsilon_i = \bar\beta^{s+1}_i$ whenever $s \le i < k$ and
$\varepsilon_k < \bar\beta^{s+1}_k$, and $\varepsilon_i = 0$ for every index $i$ that lies in
none of the intervals.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.3).

Formalized by `MetaMathlibExt.IsLStarBlockSum`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-lstar-block-sum).

## The periodic collection $E^*$

**The periodic collection $E^*$.** For a list $L$ of natural numbers, $E^*$ is the set of
nonzero coefficient functions $\varepsilon : \mathbb{N} \to \mathbb{N}$ that are sums of finitely
or infinitely many disjoint proper $L^*$-blocks, that is, the $\varepsilon \ne 0$ that are
$L^*$-block sums over some set of support intervals. It is the collection $E^*$ for the interval
$(0, 1)$ determined by $L$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.3).

Formalized by `MetaMathlibExt.lStarCollection`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#l-star-collection).

## The zero function is not in the periodic Zeckendorf collection for $(0, 1)$

For every
list $L$ of natural numbers, the zero coefficient function $\mathbb{N} \to \mathbb{N}$ does not
belong to the periodic Zeckendorf collection $E^*$ for the interval $(0, 1)$ determined by $L$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.3).

Formalized by `MetaMathlibExt.zero_notMem_lStarCollection`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zero-not-mem-l-star-collection).

## Real Zeckendorf expansions

Let $L = (e_1, \dots, e_N)$ be a list of natural numbers with
$N \ge 2$ and $e_1 \ne 0$, and let $E^*$ be its $L^*$-collection; indices of coefficient functions
and sequences start at $0$. There is a unique strictly decreasing sequence $(Q_m)_{m \ge 0}$ in
$(0, 1)$ such that $\varepsilon \mapsto \sum_k \varepsilon_k Q_k$ is a bijection from $E^*$ onto
$(0, 1)$. Moreover, every such sequence $Q$ has the following properties: for
$\varepsilon, \delta \in E^*$, $\varepsilon \lt _d \delta$ (that is, $\varepsilon_k < \delta_k$ at
the smallest index $k$ where $\varepsilon$ and $\delta$ differ) if and only if
$\sum_k \varepsilon_k Q_k < \sum_k \delta_k Q_k$; for every $m$, $Q_m = \sum_k \bar\beta_k Q_k$,
where $\bar\beta$ is the maximal $L^*$-block starting at index $m + 1$; and if $\omega > 0$
satisfies $-1 + \sum_{k=1}^{N-1} e_k \omega^k + (1 + e_N) \omega^N = 0$, then
$Q_m = \omega^{m+1}$ for every $m$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 6 (arXiv:2308.12872v1, Section 2.3, quoting Chang 2021).

Stated but not proved: `MetaMathlibExt.existsUnique_lStar_fundamentalSequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#exists-unique-l-star-fundamental-sequenc).

## The coefficient function $\inf(\varepsilon)$

Let $L$ be a list of natural numbers and
$\varepsilon : \mathbb{N} \to \mathbb{N}$ a coefficient function, with indices starting at $0$.
If $\varepsilon$ has a last nonzero entry, at index $c$, then $\inf(\varepsilon)$ agrees with
$\varepsilon$ at the indices $i < c$, equals $\varepsilon_c - 1$ at $c$, and agrees with the
maximal $L^*$-block starting at index $c + 1$ at the indices $i > c$. Otherwise, that is, when
$\varepsilon$ has infinite support or is zero, $\inf(\varepsilon) = \varepsilon$.

In the paper's one-based indexing the last nonzero entry sits at index $c + 1$, and
$\inf(\varepsilon) = \operatorname{res}_{c+1}(\varepsilon) - \beta^{c+1} + \bar\beta^{c+2}$,
where $\operatorname{res}_{c+1}(\varepsilon)$ keeps the entries of $\varepsilon$ at the indices
at most $c + 1$, $\beta^{c+1}$ has a single entry $1$ at index $c + 1$ and zeros elsewhere, and
$\bar\beta^{c+2}$ is the maximal $L^*$-block starting at index $c + 2$ (all in paper indices).

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.3).

Formalized by `MetaMathlibExt.lStarInf`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#l-star-inf).

## $\inf(\varepsilon) = \varepsilon$ for infinite support

Let $L$ be a list of natural
numbers and $\varepsilon : \mathbb{N} \to \mathbb{N}$ a coefficient function with infinitely many
nonzero entries (for every $c$ there is $i > c$ with $\varepsilon_i \ne 0$). Then
$\inf(\varepsilon) = \varepsilon$, where $\inf$ is taken with respect to $L$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2 (arXiv:2308.12872v1, Section 2.3).

Formalized by `MetaMathlibExt.lStarInf_of_infinite_support`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#l-star-inf-of-infinite-support).

## $\varepsilon$ and $\inf(\varepsilon)$ have the same value

Let $L$ be a list of natural
numbers of length at least $2$ with nonzero first entry, let $E^*$ be the set of nonzero
coefficient functions $\mathbb N \to \mathbb N$ that are sums of finitely or infinitely many
disjoint proper $L^*$-blocks, and let $Q$ be a strictly decreasing sequence in $(0, 1)$ such that
$\varepsilon \mapsto \sum_k \varepsilon_k Q_k$ is a bijection from $E^*$ onto $(0, 1)$; indices
start at $0$. For $\varepsilon \in E^*$ define $\inf(\varepsilon)$ as follows: if $\varepsilon$
has infinitely many nonzero entries, then $\inf(\varepsilon) = \varepsilon$; otherwise, with $c$
the largest index such that $\varepsilon_c \ne 0$, $\inf(\varepsilon)$ agrees with $\varepsilon$
at the indices below $c$, has entry $\varepsilon_c - 1$ at index $c$, and agrees at the indices
above $c$ with the maximal $L^*$-block starting at index $c + 1$. Then every
$\varepsilon \in E^*$ satisfies $\sum_k \varepsilon_k Q_k = \sum_k \inf(\varepsilon)_k Q_k$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 4 (arXiv:2308.12872v1, Section 2.3).

Stated but not proved: `MetaMathlibExt.tsum_lStarInf_mul_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#tsum-l-star-inf-mul-eq).

## Nearby expansions share long prefixes

Let $L$ be a list of natural numbers of length at
least $2$ with nonzero first entry, let $E^*$ be its $L^*$-collection, and let $Q$ be a strictly
decreasing sequence in $(0, 1)$ such that $\varepsilon \mapsto \sum_k \varepsilon_k Q_k$ is a
bijection from $E^*$ onto $(0, 1)$; indices start at $0$. Let $\varepsilon \in E^*$, put
$x = \sum_k \varepsilon_k Q_k$, and let $n \in \mathbb N$. Define $\inf(\varepsilon)$ as follows:
if $\varepsilon$ has infinitely many nonzero entries, then $\inf(\varepsilon) = \varepsilon$;
otherwise, with $c$ the largest index such that $\varepsilon_c \ne 0$, $\inf(\varepsilon)$ agrees
with $\varepsilon$ at indices below $c$, has entry $\varepsilon_c - 1$ at index $c$, and agrees
at indices above $c$ with the maximal $L^*$-block starting at index $c + 1$. Then there is
$\delta > 0$ such that every $\varepsilon' \in E^*$ with
$x < \sum_k \varepsilon'_k Q_k < x + \delta$ satisfies $\varepsilon'_i = \varepsilon_i$ for all
$i \le n$, and every $\varepsilon' \in E^*$ with $x - \delta < \sum_k \varepsilon'_k Q_k < x$
satisfies $\varepsilon'_i = \inf(\varepsilon)_i$ for all $i \le n$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 5 (arXiv:2308.12872v1, Section 2.3).

Stated but not proved: `MetaMathlibExt.exists_prefix_eq_of_lStar_near` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#exists-prefix-eq-of-l-star-near).

## Proper blocks below a maximal block

Let $L = (e_1, \dots, e_N)$ with $N \ge 2$ and
$e_1 \ne 0$, let $\varepsilon \colon \mathbb{N} \to \mathbb{N}$ and $b \in \mathbb{N}$ with
$\varepsilon_i = 0$ for all $i < b$, and let $\bar\beta$ be the maximal $L^*$-block starting at
index $b$. Then $\varepsilon \lt _d \bar\beta$ in the descending lexicographic order if and only if
there is $k \ge b$ such that the function equal to $\varepsilon_i$ for $i \le k$ and to $0$ for
$i > k$ is a proper $L^*$-block with support interval $[b, k]$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 8 (arXiv:2308.12872v1, Section 3.3).

Stated but not proved: `MetaMathlibExt.descLexLT_maxLStarBlock_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#desc-lex-lt-max-lstar-block-iff).

## Decomposing $L^*$-blocks into $\tilde L^*$-blocks

**Decomposing $L^*$-blocks into $\tilde L^*$-blocks.** Let $L$ and $\tilde L$ be lists of
natural numbers of length at least $2$ with nonzero first entries whose periodic Zeckendorf
collections satisfy $E \subsetneq \tilde E$. If $\zeta$ is a nonzero proper $L^*$-block with
support interval $[i, b]$, then $\zeta$ is a sum of disjoint proper $\tilde L^*$-blocks whose
support intervals all lie in $[0, b]$, one of which has support interval $[a, b]$ for some $a$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 9 (arXiv:2308.12872v1, Section 3.3).

Stated but not proved: `MetaMathlibExt.exists_lStarBlockSum_of_properLStarBlock` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#exists-l-star-block-sum-of-proper-lstar).

## The tail of an $L^\ast$-block decomposition lies in $\tilde E^\ast$

Let $L$ and
$\tilde L$ be lists of natural numbers of length at least $2$ with nonzero first entries, such
that the periodic Zeckendorf collection $E$ of $L$ is a proper subset of the periodic Zeckendorf
collection $\tilde E$ of $\tilde L$, and let $\tilde E^*$ be the set of nonzero coefficient
functions $\mathbb N \to \mathbb N$ that are sums of finitely or infinitely many disjoint proper
$\tilde L^*$-blocks. Indices start at $0$. Let $\varepsilon \in \tilde E^*$ and $b \in \mathbb N$,
let $\eta$ agree with $\varepsilon$ at the indices $i < b$ and vanish at the indices $i \ge b$,
and let $\mu$ vanish at the indices $i < b$ and agree with $\varepsilon$ at the indices $i \ge b$.
Suppose that for some set $I$ of pairs $(s, k)$ with $k < b$, $\eta$ is the sum of the disjoint
proper $L^*$-blocks with support intervals $[s, k]$, $(s, k) \in I$, and that $\mu = \bar\beta$
or $\bar\beta \lt _d \mu$, where $\bar\beta$ is the maximal $L^*$-block starting at index $b$ (the
paper's $\bar\beta^{b+1}$) and $\lt _d$ is the descending lexicographic order. Then
$\mu \in \tilde E^*$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Corollary 2 (arXiv:2308.12872v1, Section 3.3).

Stated but not proved: `MetaMathlibExt.mem_lStarCollection_of_lStarBar_decomposition` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#mem-l-star-collection-of-l-star-bar-deco).

## Shifted maximal blocks scale geometrically

Let $L = (e_1, \dots, e_N)$ and $\tilde L$ be
lists of natural numbers of length at least $2$ with nonzero first entries, and let $\tilde Q$ be
a strictly decreasing sequence with values in $(0, 1)$ such that
$\varepsilon \mapsto \sum_k \varepsilon_k \tilde Q_k$ is a bijection from $\tilde E^*$, the
periodic Zeckendorf collection for $(0, 1)$ determined by $\tilde L$, onto $(0, 1)$. For
$s \in \mathbb{N}$ let $\bar\beta_s$ be the maximal $L^*$-block starting at index $s$: it is $0$
at indices $i < s$ and $e_j$ at indices $i \ge s$ with $j - 1 \equiv i - s \pmod N$. Then
$\sum_k (\bar\beta_s)_k \tilde Q_k = \tilde Q_0^{\,s} \sum_k (\bar\beta_0)_k \tilde Q_k$ for every
$s \in \mathbb{N}$.

Indices are zero-based: $\bar\beta_s$ is the paper's $\bar\beta^{s+1}$ and $\tilde Q_0$ is its
$\tilde Q_1 = \tilde\omega$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 16 (arXiv:2308.12872v1, Section 4.1).

Stated but not proved: `MetaMathlibExt.tsum_maxLStarBlock_mul_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#tsum-max-lstar-block-mul-eq).

## Number of proper $L^*$-blocks with a given support interval

**Number of proper $L^*$-blocks with a given support interval.** Let
$L = (e_1, \dots, e_N)$ be a list of natural numbers with $N \ge 2$ and $e_1 \ne 0$, let $s \le k$
be natural numbers, and let $j$ be the integer with $1 \le j \le N$ and
$k - s + 1 \equiv j \pmod N$. Then there are exactly $e_j$ proper $L^*$-blocks with support
interval $[s, k]$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 15 (arXiv:2308.12872v1, Section 4.1).

Stated but not proved: `MetaMathlibExt.ncard_properLStarBlock` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#ncard-proper-lstar-block).

## Number of $L^*$-block sums of length $n$

**Number of $L^*$-block sums of length $n$.** For a list $L$ of natural numbers and $n \ge 0$,
with coefficient functions indexed from $1$, $C_n$ is the number of functions
$\varepsilon : \mathbb N \to \mathbb N$ that are sums of disjoint proper $L^*$-blocks with
support intervals inside $[1, n]$. The zero function (the empty sum) is counted, so $C_0 = 1$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 4 (arXiv:2308.12872v1, Section 4.1).

Formalized by `MetaMathlibExt.lStarBlockSumCount`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#l-star-block-sum-count).

## The empty block-sum count

For every list $L$ of natural numbers, $C_0 = 1$, where $C_n$
is the number of sums of disjoint proper $L^*$-blocks with support intervals inside $[1, n]$:
for $n = 0$ the zero function is the only such sum.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 4 (arXiv:2308.12872v1, Section 4.1, `S_0 = {0}`).

Formalized by `MetaMathlibExt.lStarBlockSumCount_zero`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#l-star-block-sum-count-zero).

## Recurrence for the number of $L^*$-block sums

**Recurrence for the number of $L^*$-block sums.** Let $L = (e_1, \dots, e_N)$ be a list of
natural numbers with $N \ge 2$ and $e_1 \ne 0$, index coefficient functions from $1$, and let
$C_n$ be the number of functions $\mathbb N \to \mathbb N$ that are sums of disjoint proper
$L^*$-blocks with support intervals inside $[1, n]$. Then $C_k = \sum_{j=1}^{k} e_j C_{k-j}$ for
$1 \le k \le N$, and $C_n = \sum_{k=1}^{N-1} e_k C_{n-k} + (1 + e_N) C_{n-N}$ for $n \ge N + 1$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 4 (arXiv:2308.12872v1, Section 4.1).

Stated but not proved: `MetaMathlibExt.lStarBlockSumCount_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#l-star-block-sum-count-recurrence).

## Generating function of the $L^\ast$-block-sum counts

Let $L = (e_1, \dots, e_N)$ be a
list of natural numbers with $N \ge 2$ and $e_1 \ne 0$. For each $k$ let $C_k$ be the number of
coefficient functions that are sums of disjoint proper $L^*$-blocks with support intervals inside
$[1, k]$ (the zero function included), and put
$f(x) = 1 - \sum_{k=1}^{N-1} e_k x^k - (1 + e_N) x^N$. Then there is a real $r > 0$ such that for
every real $x$ with $-r < x < r$ the series $\sum_{k \ge 0} C_k x^k$ converges absolutely, with
sum $(1 - x^N) / f(x)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 5 (arXiv:2308.12872v1, Section 4.1).

Stated but not proved: `MetaMathlibExt.hasSum_lStarBlockSumCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#has-sum-l-star-block-sum-count).

## Periodic Zeckendorf pairs

Two lists $L$ and $\tilde L$ of natural numbers form a periodic
Zeckendorf pair when both have length at least $2$ and a nonzero first entry, and the periodic
Zeckendorf collection $E$ determined by $L$ is a proper subset of the periodic Zeckendorf
collection $\tilde E$ determined by $\tilde L$.

This is the standing assumption of Sections 3 and 4 of the source.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 3.1.

Formalized by `MetaMathlibExt.IsPeriodicZeckendorfPair`, a structure declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-periodic-zeckendorf-pair).

## Periodic Zeckendorf pairs are nested

If the lists $L$ and $\tilde L$ form a periodic
Zeckendorf pair, then the periodic Zeckendorf collection determined by $L$ is contained in the
periodic Zeckendorf collection determined by $\tilde L$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 3.1.

Formalized by `MetaMathlibExt.IsPeriodicZeckendorfPair.subset`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 640](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L640). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#subset).

## Evaluation of a coefficient function at a real sequence

For a real sequence $Q$ and a
coefficient function $\varepsilon \colon \mathbb{N} \to \mathbb{N}$, not necessarily finitely
supported, the evaluation $\sum \varepsilon Q$ is the sum of the series
$\sum_{k \ge 0} \varepsilon_k Q_k$, taken to be $0$ when the series is not absolutely summable.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2.1.

Formalized by `MetaMathlibExt.zeckendorfRealEval`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-real-eval).

## Evaluating the zero coefficient function

For every real sequence $Q$, the evaluation of
the zero coefficient function at $Q$ is $0$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Section 2.1.

Formalized by `MetaMathlibExt.zeckendorfRealEval_zero`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-real-eval-zero).

## Fundamental sequence of an $L^\ast$-collection

Let $L$ be a list of natural numbers with
$L^*$-collection $E^*$. A real sequence $(Q_n)_{n \ge 0}$ is a fundamental sequence of $E^*$ if
it is strictly decreasing, $0 < Q_n < 1$ for every $n$, and the map
$\varepsilon \mapsto \sum_k \varepsilon_k Q_k$ is a bijection from $E^*$ onto the open interval
$(0, 1)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 6 and Definition 18.

Formalized by `MetaMathlibExt.IsLStarFundamentalSequence`, a structure declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-lstar-fundamental-sequence).

## Fundamental sequences of $E^*$ are positive

**Fundamental sequences of $E^*$ are positive.** Let $L$ be a list of natural numbers and let
$Q$ be a fundamental sequence of the collection $E^*$ determined by $L$. Then $Q_n > 0$ for every
$n$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 6.

Formalized by `MetaMathlibExt.IsLStarFundamentalSequence.pos`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 672](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L672). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#pos).

## Reversal of the first $n$ entries

For $n \in \mathbb N$ and a coefficient function
$\varepsilon : \mathbb N \to \mathbb N$, $\mathrm{rev}_n(\varepsilon)$ is the finitely supported
coefficient function whose entry at index $j$ is $\varepsilon(n - 1 - j)$ for $j < n$ and $0$
for $j \ge n$ (indices start at $0$). In the paper's one-based indexing this is
$\mathrm{rev}_n(\varepsilon) = (\varepsilon_n, \dots, \varepsilon_1)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 5.

Formalized by `MetaMathlibExt.zeckendorfRev`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-rev).

## Reversal of the first three entries

For every coefficient function
$\varepsilon : \mathbb N \to \mathbb N$, $\mathrm{rev}_3(\varepsilon)$ is the finitely supported
coefficient function with entries $\varepsilon(2)$, $\varepsilon(1)$, $\varepsilon(0)$ at
indices $0$, $1$, $2$ and $0$ at every other index. In the paper's one-based indexing,
$\mathrm{rev}_3(\varepsilon) = (\varepsilon_3, \varepsilon_2, \varepsilon_1)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 5.

Formalized by `MetaMathlibExt.zeckendorfRev_three`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 688](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L688). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-rev-three).

## The coefficient function $\bar\mu$

Let $E$ be a set of finitely supported coefficient
functions $\mathbb{N} \to \mathbb{N}$ and $\mu$ a finitely supported coefficient function. If
$\mu$ has an immediate predecessor $\check\mu$ in $E$ (the largest element of $E$ that is
$\lt _a \mu$ in the ascending lexicographic order) and $\check\mu$ has an immediate successor in
$E$ (the smallest element of $E$ that is $>_a \check\mu$), then $\bar\mu$ is that immediate
successor; otherwise $\bar\mu = 0$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 20.

Formalized by `MetaMathlibExt.zeckendorfBar`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 699](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L699). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-bar).

## The bar of a coefficient function is a successor of its predecessor

Let $E$ be a set of
finitely supported coefficient functions $\mathbb{N} \to \mathbb{N}$ and $\mu$ a finitely supported
coefficient function. Call $\nu$ an immediate predecessor of $\mu$ in $E$ if it is a largest
element of $E$ that is $\lt _a \mu$ in the ascending lexicographic order, and call $\xi$ an immediate
successor of $\nu$ in $E$ if it is a smallest element of $E$ that is $>_a \nu$. Let $\bar\mu$ be an
immediate successor in $E$ of an immediate predecessor of $\mu$ in $E$ if such a pair exists, and
$\bar\mu = 0$ otherwise. If some immediate predecessor of $\mu$ in $E$ has an immediate successor
in $E$, then $\bar\mu$ is the immediate successor in $E$ of some immediate predecessor of $\mu$ in
$E$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 20.

Formalized by `MetaMathlibExt.zeckendorfBar_spec`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 708](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-bar-spec).

## The closure $\bar E^*$ of $E^*$

**The closure $\bar E^*$ of $E^*$.** Let $L$ be a list of natural numbers, $E^*$ the collection
determined by $L$, and index coefficient functions from $1$. The collection $\bar E^*$ consists
of the elements of $E^*$ together with every function $\varepsilon : \mathbb N \to \mathbb N$ for
which there is an index $b \ge 0$ such that the function agreeing with $\varepsilon$ at the
indices $\le b$ and vanishing elsewhere is a sum of disjoint proper $L^*$-blocks with support
intervals inside $[1, b]$, and $\varepsilon_i = \bar\beta^{b+1}_i$ for all $i \ge b + 1$, where
$\bar\beta^{b+1}$ is the maximal $L^*$-block starting at index $b + 1$. These extra functions
have the form $\sum_m \zeta^m + \bar\beta^{b+1}$ with proper $L^*$-blocks $\zeta^m$; the case
$b = 0$ gives $\bar\beta^1$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 22.

Formalized by `MetaMathlibExt.lStarClosure`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#l-star-closure).

## $\bar\beta^1$ lies in $\bar E^*$

**$\bar\beta^1$ lies in $\bar E^*$.** For every list $L$ of natural numbers, the maximal
$L^*$-block starting at index $0$ (the paper's $\bar\beta^1$) belongs to the collection $\bar E^*$
determined by $L$. This is the case of the definition of $\bar E^*$ with no proper blocks, in
which the maximal block starts at index $0$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 22.

Formalized by `MetaMathlibExt.maxLStarBlock_zero_mem_lStarClosure`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 728](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L728). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#max-lstar-block-zero-mem-l-star-closure).

## The map $\overline{\mathrm{rev}}$

Fix a list $L$, and let $E$ be its periodic Zeckendorf
collection, $\bar\beta^1$ the maximal $L^*$-block starting at index $0$, $\lt _d$ the descending
lexicographic order, $\mathrm{rev}_n$ the reversal of the first $n$ entries, and $\bar\mu$ the
bar of a finitely supported $\mu$ relative to $E$. For a coefficient function
$\varepsilon : \mathbb N \to \mathbb N$, if $\varepsilon \lt _d \bar\beta^1$ fails then
$\overline{\mathrm{rev}}(\varepsilon) = \bar\beta^1$. If $\varepsilon \lt _d \bar\beta^1$, then
for each index $i$ the entry of $\overline{\mathrm{rev}}(\varepsilon)$ at $i$ is the eventual
value, as $n \to \infty$, of the entry of $\mathrm{rev}_n(\overline{\mathrm{rev}_n(\varepsilon)})$
at $i$ when that entry is eventually constant, and $0$ when it is not.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 23.

Formalized by `MetaMathlibExt.zeckendorfRevBar`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 739](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L739). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-rev-bar).

## $\overline{\mathrm{rev}}$ of a function not below $\bar\beta^1$

Let $L$ be a list of
natural numbers, let $\bar\beta^1$ be the maximal $L^*$-block starting at index $0$, let $\lt _d$ be
the descending lexicographic order, and let $\overline{\mathrm{rev}}$ be the map determined by
$L$. For every coefficient function $\varepsilon : \mathbb N \to \mathbb N$ such that
$\varepsilon \lt _d \bar\beta^1$ fails, $\overline{\mathrm{rev}}(\varepsilon) = \bar\beta^1$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 23.

Formalized by `MetaMathlibExt.zeckendorfRevBar_of_not_descLexLT`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 751](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L751). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-rev-bar-of-not-desc-lex-lt).

## The function $\delta_1^\ast$

Let $L$ and $\tilde L$ be lists of natural numbers and $Q$
and $\tilde Q$ real sequences with first terms $\omega = Q_0$ and $\tilde\omega = \tilde Q_0$
(indices start at $0$), and put $\gamma = \log_{\tilde\omega} \omega$. Let $\tilde E^*$ be the
collection $E^*$ determined by $\tilde L$, let $\overline{\mathrm{rev}}$ be the map determined by
$L$, and write $\sum \varepsilon R = \sum_k \varepsilon_k R_k$ for the evaluation of a coefficient
function $\varepsilon$ at a real sequence $R$. For real $y$: if some $\varepsilon \in \tilde E^*$
satisfies $\sum \varepsilon \tilde Q = y$, then
$\delta_1^*(y) = \sum \overline{\mathrm{rev}}(\varepsilon) Q / y^\gamma$ for a chosen such
$\varepsilon$; otherwise $\delta_1^*(y) = 0$.

In the paper $\delta_1^*$ is used on $[\tilde\omega, 1)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 23.

Formalized by `MetaMathlibExt.zeckendorfDeltaStarOne`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 760](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L760). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-delta-star-one).

## The function $\delta^*$

**The function $\delta^*$.** Let $L$ and $\tilde L$ be lists and $Q$ and $\tilde Q$ real
sequences, let $\tilde\omega$ be the first term of $\tilde Q$, and let $\delta_1^*$ be the function
$\delta_1^*$ of $L$, $\tilde L$, $Q$, $\tilde Q$. For real $y$: if some natural number $m$
satisfies $\tilde\omega^{m+1} \le y < \tilde\omega^m$, then
$\delta^*(y) = \delta_1^*(y / \tilde\omega^m)$ for a chosen such $m$; otherwise
$\delta^*(y) = 0$.

When $0 < \tilde\omega < 1$, the intervals $[\tilde\omega^{m+1}, \tilde\omega^m)$ partition
$(0, 1)$, so $m$ is unique and $\delta^*$ vanishes outside $(0, 1)$. The printed Definition 23
reduces $y$ by powers of the first term $\omega$ of $Q$; since $\delta_1^*$ lives on
$[\tilde\omega, 1)$, Proposition 2 and Equation (12) evaluate $\delta^*$ on $[\tilde\omega, 1)$ as
$\delta_1^*$, and the proof of Theorem 9 glues
$\delta_1^*(\tilde\omega) = \lim_{x \to 1^-} \delta_1^*(x)$, the reduction is by powers of
$\tilde\omega$ (Notation 1).

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 23.

Formalized by `MetaMathlibExt.zeckendorfDeltaStar`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 772](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L772). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-delta-star).

## $\delta^*$ agrees with $\delta_1^*$ on $(\tilde\omega, 1)$

**$\delta^*$ agrees with $\delta_1^*$ on $[\tilde\omega, 1)$.** Let $L$ and $\tilde L$ be lists
and $Q$ and $\tilde Q$ real sequences such that the first term $\tilde\omega$ of $\tilde Q$
satisfies $0 < \tilde\omega < 1$. Then for every real $y$ with $\tilde\omega \le y < 1$, the
functions $\delta^*$ and $\delta_1^*$ of $L$, $\tilde L$, $Q$, $\tilde Q$ agree at $y$:
$\delta^*(y) = \delta_1^*(y)$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 23.

Formalized by `MetaMathlibExt.zeckendorfDeltaStar_of_mem_Ico`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 781](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L781). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-delta-star-of-mem-ico).

## The generic exponent

Let $Q$ and $\tilde Q$ be real sequences with first terms $\omega$
and $\tilde\omega$, and put $\gamma = \log_{\tilde\omega} \omega$. The generic exponent $p$ of $Q$
and $\tilde Q$ is the smallest positive integer $p$ with $\gamma \tilde\omega^{p-1} < \omega^p$,
and $p = 0$ if no positive integer satisfies this inequality.

In the paper, $p$ is the exponent of the generic upper bound of the function $\delta^*$
(Definition 25).

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 25.

Formalized by `MetaMathlibExt.zeckendorfGenericExponent`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 797](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L797). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-generic-exponent).

## The generic exponent satisfies its defining inequality

Let $Q$ and $\tilde Q$ be real
sequences with first terms $\omega$ and $\tilde\omega$, put $\gamma = \log_{\tilde\omega} \omega$,
and let $p$ be the generic exponent of $Q$ and $\tilde Q$. If some positive integer $q$ satisfies
$\gamma \tilde\omega^{q-1} < \omega^q$, then $p$ is positive and
$\gamma \tilde\omega^{p-1} < \omega^p$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Definition 25.

Formalized by `MetaMathlibExt.zeckendorfGenericExponent_spec`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 804](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L804). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-generic-exponent-spec).

## The set $U$ of evaluations of $\tilde E^* \setminus \bar E^*$

**The set $U$ of evaluations of $\tilde E^* \setminus \bar E^*$.** For lists $L$ and
$\tilde L$ and a real sequence $\tilde Q$, let $\tilde E^*$ be the $\tilde L^*$-collection and
$\bar E^*$ the closure collection of $L$. The set $U \subseteq \mathbb R$ is the image of
$\tilde E^* \setminus \bar E^*$ under the evaluation
$\varepsilon \mapsto \sum_k \varepsilon_k \tilde Q_k$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Notation 2.

Formalized by `MetaMathlibExt.zeckendorfSmoothSet`, a definition declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 815](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L815). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-smooth-set).

## Membership in the set $U$

Let $L$ and $\tilde L$ be lists of natural numbers and let
$\tilde Q = (\tilde Q_k)$ be a sequence of real numbers. Let $\tilde E^*$ be the collection $E^*$
determined by $\tilde L$, let $\bar E^*$ be the closure $\bar E^*$ determined by $L$, and let $U$
be the image of $\tilde E^* \setminus \bar E^*$ under the map
$\varepsilon \mapsto \sum_k \varepsilon_k \tilde Q_k$. A real number $x$ lies in $U$ if and only if
$x = \sum_k \varepsilon_k \tilde Q_k$ for some $\varepsilon \in \tilde E^*$ with
$\varepsilon \notin \bar E^*$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Notation 2.

Formalized by `MetaMathlibExt.mem_zeckendorfSmoothSet_iff`, a theorem declared in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 822](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L822). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#mem-zeckendorf-smooth-set-iff).

## Reversals characterize the nonzero elements of $\bar E^\ast$

Let $L$ be a list of natural
numbers of length at least $2$ with nonzero first entry, let $E$ be the periodic Zeckendorf
collection determined by $L$, and let $\bar E^*$ be the closure of the collection $E^*$ determined
by $L$. For $n \in \mathbb N$ and a coefficient function $\varepsilon : \mathbb N \to \mathbb N$,
let $\mathrm{rev}_n(\varepsilon)$ be the finitely supported coefficient function whose first $n$
entries are the first $n$ entries of $\varepsilon$ in reverse order and whose other entries are
$0$. Then a nonzero coefficient function $\varepsilon : \mathbb N \to \mathbb N$ satisfies
$\mathrm{rev}_n(\varepsilon) \in E$ for every $n \in \mathbb N$ if and only if
$\varepsilon \in \bar E^*$.

This reads the source's Lemma 3 for nonzero $\varepsilon$ and counts $\bar\beta^1$, the maximal
$L^*$-block starting at the first index, as an element of $\bar E^*$. As printed (no
$\varepsilon \ne 0$, decompositions with at least one block) the lemma fails at
$\varepsilon = 0$, since $\mathrm{rev}_n(0) = 0 \in E$, and at $\varepsilon = \bar\beta^1$,
since $\mathrm{rev}_n(\bar\beta^1)$ is the maximal $L$-block $\theta^{n+1}$, which lies in $E$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 3.

Stated but not proved: `MetaMathlibExt.forall_zeckendorfRev_mem_iff_mem_lStarClosure` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 833](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L833). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#forall-zeckendorf-rev-mem-iff-mem-l-star).

## Decomposition along $L^*$-blocks (Corollary 1)

**Decomposition along $L^*$-blocks (Corollary 1).** Let $L$ and $\tilde L$ be a periodic
Zeckendorf pair, let $E^*$ and $\tilde E^*$ be the collections determined by $L$ and $\tilde L$,
and let $\varepsilon \in \tilde E^*$. Index coefficient functions from $1$. For $b \ge 0$, let
$\eta_b$ agree with $\varepsilon$ at the indices $\le b$ and vanish elsewhere, and let
$\mu_b = \varepsilon - \eta_b$. Call $b$ a decomposition index of $\varepsilon$ if $\eta_b$ is a
sum of disjoint proper $L^*$-blocks with support intervals inside $[1, b]$ and
$\bar\beta^{b+1} \le_d \mu_b$, where $\bar\beta^{b+1}$ is the maximal $L^*$-block starting at
index $b + 1$ and $\le_d$ means equal or smaller in the descending lexicographic order. Then
$\varepsilon \in E^*$ if and only if $\varepsilon$ has no decomposition index, and if
$\varepsilon \notin E^*$, then $\varepsilon$ has exactly one decomposition index.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Corollary 1.

Stated but not proved: `MetaMathlibExt.lStarBar_decomposition` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 845](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L845). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#l-star-bar-decomposition).

## Lemma 10: $\mathrm{rev}_n$ of the bar of $\mathrm{rev}_n(\varepsilon)$

Let
$(L, \tilde L)$ be a periodic Zeckendorf pair, $E$ the periodic Zeckendorf collection of $L$, and
$E^*$ and $\tilde E^*$ the $L^*$- and $\tilde L^*$-collections. Indices start at $0$. Write $\lt _d$
for the descending lexicographic order, $\bar\beta^{s+1}$ for the maximal $L^*$-block starting at
index $s$, $\mathrm{rev}_n$ for the reversal of the first $n$ entries, $\bar\mu$ for the bar of a
finitely supported $\mu$ relative to $E$, and $\mathrm{res}_n(\varepsilon)$ for $\varepsilon$
with every entry at an index $\ge n$ replaced by $0$. Let $\varepsilon \in \tilde E^*$ with
$\varepsilon \lt _d \bar\beta^1$. If $\varepsilon \in E^*$, then
$\mathrm{rev}_n(\overline{\mathrm{rev}_n(\varepsilon)}) = \mathrm{res}_n(\varepsilon)$ for every
$n \ge 1$. Moreover, let $b \ge 1$ be such that $\mathrm{res}_b(\varepsilon)$ is a sum of
disjoint proper $L^*$-blocks whose support intervals consist of indices below $b$, and such that
the coefficient function $\mu$ obtained from $\varepsilon$ by replacing every entry at an index
below $b$ by $0$ satisfies $\mu = \bar\beta^{b+1}$ or $\bar\beta^{b+1} \lt _d \mu$. Then for all
sufficiently large $n$, $\mathrm{rev}_n(\overline{\mathrm{rev}_n(\varepsilon)})$ equals
$\mathrm{res}_b(\varepsilon) + \beta^b$ if $\bar\beta^{b+1} \lt _d \mu$, where $\beta^b$ has entry
$1$ at index $b - 1$ and $0$ elsewhere, and equals $\mathrm{res}_n(\varepsilon)$ otherwise.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 10.

Stated but not proved: `MetaMathlibExt.zeckendorfRev_bar_zeckendorfRev_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 863](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L863). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-rev-bar-zeckendorf-rev-eq).

## Fixed points of $\overline{\mathrm{rev}}$ in $\tilde E^*$

**Fixed points of $\overline{\mathrm{rev}}$ in $\tilde E^*$.** Let $L$ and $\tilde L$ be
lists of natural numbers of length at least $2$ with nonzero first entries, such that the
periodic Zeckendorf collection $E$ of $L$ is a proper subset of the periodic Zeckendorf
collection $\tilde E$ of $\tilde L$. Let $\tilde E^*$ be the collection $E^*$ determined by
$\tilde L$, and let $\bar E^*$ and $\overline{\mathrm{rev}}$ be taken with respect to $L$. Then
for every $\varepsilon \in \tilde E^*$, $\varepsilon \in \bar E^*$ if and only if
$\overline{\mathrm{rev}}(\varepsilon) = \varepsilon$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 11.

Stated but not proved: `MetaMathlibExt.mem_lStarClosure_iff_zeckendorfRevBar_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 883](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L883). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#mem-l-star-closure-iff-zeckendorf-rev-ba).

## $\overline{\mathrm{rev}}$ of the reversal of an element of $\tilde E$ (Lemma 12)

Let $L$
and $\tilde L$ form a periodic Zeckendorf pair, let $E$ and $\tilde E$ be the periodic Zeckendorf
collections determined by $L$ and $\tilde L$, and index coefficient functions from $0$. Let
$\mu \in \tilde E$ and $t \ge 1$ be such that $\mu_{t-1} \ne 0$ and $\mu_j = 0$ for all $j \ge t$.
Let $\overline{\mathrm{rev}}$ be the map determined by $L$, $\bar\beta^1$ the maximal $L^*$-block
starting at index $0$, $\mathrm{rev}_t$ the reversal of the first $t$ entries, $\bar\mu$ the bar
of $\mu$ relative to $E$, $\lt _a$ the ascending lexicographic order, and $\theta^{t+1}$ the maximal
$L$-block that vanishes from index $t$ on. If $\mu = \theta^{t+1}$ or $\mu \lt _a \theta^{t+1}$,
then $\overline{\mathrm{rev}}(\mathrm{rev}_t(\mu)) = \mathrm{rev}_t(\bar\mu)$; if
$\theta^{t+1} \lt _a \mu$, then $\overline{\mathrm{rev}}(\mathrm{rev}_t(\mu)) = \bar\beta^1$.

In the paper $t$ is the order of $\mu$, and $\theta^{t+1}$ appears as the immediate predecessor
$\hat\beta^{t+1}$ in $E$ of the basis function $\beta^{t+1}$, whose only nonzero entry is a $1$
at index $t$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 12.

Stated but not proved: `MetaMathlibExt.zeckendorfRevBar_zeckendorfRev_of_order` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 894](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L894). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-rev-bar-zeckendorf-rev-of-ord).

## Transition from the subcollection count to $\delta^\ast$

Let $L$ and $\tilde L$ form a
periodic Zeckendorf pair, with periodic Zeckendorf collections $E \subsetneq \tilde E$, and let
$Q$ and $\tilde Q$ be fundamental sequences of the $L^*$-collection $E^*$ and the
$\tilde L^*$-collection $\tilde E^*$. Put $\omega = Q_0$, $\tilde\omega = \tilde Q_0$ and
$\gamma = \log_{\tilde\omega} \omega$, and let $\delta^*$ be the function determined by $L$,
$\tilde L$, $Q$ and $\tilde Q$. Let $H$ and $\tilde H$ be strictly increasing sequences of
positive integers such that $\mu \mapsto \sum_k \mu_k H_k$ is a bijection from $E$ onto
$\mathbb N$ and $\mu \mapsto \sum_k \mu_k \tilde H_k$ is a bijection from $\tilde E$ onto
$\mathbb N$, and suppose $H_n \omega^n \to \alpha$ and
$\tilde H_n \tilde\omega^n \to \tilde\alpha$ as $n \to \infty$. For each natural number $x$ let
$\mu_x \in \tilde E$ satisfy $\sum_k (\mu_x)_k \tilde H_k = x$, let $n_x$ be one more than the
largest index in the support of $\mu_x$ ($n_x = 0$ if $\mu_x = 0$), and let $z(x)$ be the number
of natural numbers $n < x$ of the form $\sum_k \mu_k \tilde H_k$ with $\mu \in E$. Then, as
$x \to \infty$ through the natural numbers, $z(x) / x^\gamma$ is asymptotically equivalent to
$\delta^*(y_x) \, \alpha / \tilde\alpha^\gamma$, where $y_x = \sum_k \rho_k \tilde Q_k$ and
$\rho = \operatorname{rev}_{n_x}(\mu_x)$ lists the first $n_x$ entries of $\mu_x$ in reverse order.

Indices are zero-based.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 2.

Stated but not proved: `MetaMathlibExt.isEquivalent_subcollectionCount_div_rpow_deltaStar` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 908](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L908). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-equivalent-subcollection-count-div-rp).

## Lemma 13: behaviour of $\overline{\mathrm{rev}}$ near a point

Let $(L, \tilde L)$ be a
periodic Zeckendorf pair, let $E^*$ and $\tilde E^*$ be the $L^*$- and $\tilde L^*$-collections,
$\bar E^*$ the closure collection of $L$, $\overline{\mathrm{rev}}$ the map determined by $L$,
$\inf$ the $L^*$-infimum map, and $\tilde Q$ a fundamental sequence of $\tilde E^*$. For
$\eta \in \tilde E^*$ write $x(\eta) = \sum_k \eta_k \tilde Q_k$, and let
$\varepsilon \in \tilde E^*$. If $\varepsilon \notin \bar E^*$, there is $\delta > 0$ such that
$\overline{\mathrm{rev}}(\varepsilon') = \overline{\mathrm{rev}}(\varepsilon)$ for every
$\varepsilon' \in \tilde E^*$ with $|x(\varepsilon') - x(\varepsilon)| < \delta$. If
$\varepsilon \in \bar E^* \setminus E^*$, there is $\delta > 0$ such that
$\inf(\overline{\mathrm{rev}}(\varepsilon')) = \overline{\mathrm{rev}}(\varepsilon)$ for every
$\varepsilon' \in \tilde E^*$ with $x(\varepsilon) < x(\varepsilon') < x(\varepsilon) + \delta$,
and for every $n$ there is $\delta > 0$ such that $\overline{\mathrm{rev}}(\varepsilon')$ and
$\overline{\mathrm{rev}}(\varepsilon)$ agree at all indices $i < n$ for every
$\varepsilon' \in \tilde E^*$ with $x(\varepsilon) - \delta < x(\varepsilon') < x(\varepsilon)$.
If $\varepsilon \in E^*$, then for every $n$ there is $\delta > 0$ such that
$\overline{\mathrm{rev}}(\varepsilon')$ and $\overline{\mathrm{rev}}(\varepsilon)$ agree at all
indices $i < n$ for every $\varepsilon' \in \tilde E^*$ with
$|x(\varepsilon') - x(\varepsilon)| < \delta$. Indices start at $0$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 13.

Stated but not proved: `MetaMathlibExt.zeckendorfRevBar_eventually_near` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 932](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L932). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-rev-bar-eventually-near).

## Infinitely many unit reductions stay in the $L^\ast$-closure

Let
$L = (e_1, \dots, e_N)$ be a list of natural numbers with $N \ge 2$ and $e_1 \ne 0$, and let
$E^* \subseteq \bar E^*$ be the $L^*$-collection and the $L^*$-closure determined by $L$. Let
$\varepsilon \in \bar E^*$, and suppose it is not the case that $\varepsilon \in E^*$ and
$\varepsilon$ has finite support. Then there are infinitely many indices $r$ such that
$\varepsilon_r \ge 1$ and the coefficient function obtained from $\varepsilon$ by lowering its
entry at $r$ by one lies in $\bar E^*$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 14.

Stated but not proved: `MetaMathlibExt.infinite_setOf_sub_single_mem_lStarClosure` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 955](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L955). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#infinite-set-of-sub-single-mem-l-star-cl).

## Proposition 3: $U$ is a disjoint union of open intervals

Let $(L, \tilde L)$ be a
periodic Zeckendorf pair, $E^*$ and $\tilde E^*$ the $L^*$- and $\tilde L^*$-collections,
$\bar E^*$ the closure collection of $L$, and $\tilde Q$ a fundamental sequence of $\tilde E^*$.
Write $x(\eta) = \sum_k \eta_k \tilde Q_k$, $\tilde\omega = \tilde Q_0$, and $\bar\beta^{b+1}$
for the maximal $L^*$-block starting at index $b$ (indices start at $0$), and let
$U = \{x(\varepsilon) : \varepsilon \in \tilde E^* \setminus \bar E^*\}$. Call a pair
$(b, \eta)$ with $b \in \mathbb N$ and $\eta : \mathbb N \to \mathbb N$ admissible if $\eta$ is a
sum of disjoint proper $L^*$-blocks whose support intervals consist of indices below $b$ and
$\eta + \bar\beta^{b+1} \notin E^*$. Then $U$ is the union, over all admissible pairs
$(b, \eta)$, of the open intervals $(x(\eta + \bar\beta^{b+1}), x(\eta) + \tilde\omega^b)$; the
intervals of two distinct admissible pairs are disjoint; and $U$ is open and measurable.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 3.

Stated but not proved: `MetaMathlibExt.zeckendorfSmoothSet_eq_iUnion` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 967](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L967). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-smooth-set-eq-i-union).

## Continuity and local monotonicity of $\delta^{\ast}$

Let $L$ and $\tilde L$ form a
periodic Zeckendorf pair, let $Q$ be a fundamental sequence of the collection $E^*$ determined by
$L$, and let $\tilde Q$ be a fundamental sequence of the collection $\tilde E^*$ determined by
$\tilde L$. Then the function $\delta^*$ built from $L, \tilde L, Q, \tilde Q$ is continuous on
$(0, 1)$, and at each point $x$ of the smooth set $U$ of $L, \tilde L, \tilde Q$ it is
differentiable and strictly decreasing on some neighbourhood of $x$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 9.

Stated but not proved: `MetaMathlibExt.continuousOn_zeckendorfDeltaStar` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 989](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L989). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#continuous-on-zeckendorf-delta-star).

## $\delta^*$ is not differentiable at the evaluations of $\bar E^*$

**$\delta^*$ is not differentiable at the evaluations of $\bar E^*$.** Let $L$ and $\tilde L$
be lists of natural numbers of length at least $2$ with nonzero first entries whose periodic
Zeckendorf collections $E$ and $\tilde E$ satisfy $E \subsetneq \tilde E$. Let $Q$ be a fundamental
sequence of the collection $E^*$ determined by $L$, let $\tilde Q$ be a fundamental sequence of the
collection $\tilde E^*$ determined by $\tilde L$, and let $\delta^*$ be the function determined by
$L$, $\tilde L$, $Q$ and $\tilde Q$. For every $\varepsilon$ in the closure $\bar E^*$ determined
by $L$, $\delta^*$ is not differentiable at $\sum_k \varepsilon_k \tilde Q_k$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 10.

Stated but not proved: `MetaMathlibExt.not_differentiableAt_zeckendorfDeltaStar` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1000](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1000). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#not-differentiable-at-zeckendorf-delta-s).

## The smooth set $U$ has Lebesgue measure $1$

Let $L$ and $\tilde L$ form a periodic
Zeckendorf pair, let $\tilde E^*$ be the collection $E^*$ determined by $\tilde L$, let $\tilde Q$
be a fundamental sequence of $\tilde E^*$, and let $\bar E^*$ be the closure determined by $L$.
Let $U$ be the image of $\tilde E^* \setminus \bar E^*$ under the evaluation
$\varepsilon \mapsto \sum_k \varepsilon_k \tilde Q_k$. Then $U$ has Lebesgue measure $1$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 11.

Stated but not proved: `MetaMathlibExt.volume_zeckendorfSmoothSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1009](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1009). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#volume-zeckendorf-smooth-set).

## Local minima of $\delta^\ast$ at finitely supported points

Let $L$ and $\tilde L$ form a
periodic Zeckendorf pair, let $Q$ and $\tilde Q$ be fundamental sequences of the $L^*$-collection
$E^*$ and the $\tilde L^*$-collection $\tilde E^*$, and let $\delta^*$ be the function determined
by $L$, $\tilde L$, $Q$ and $\tilde Q$. If $\varepsilon \in E^*$ has finite support, then
$\delta^*$ has a local minimum at $\sum_k \varepsilon_k \tilde Q_k$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 6.

Stated but not proved: `MetaMathlibExt.isLocalMin_zeckendorfDeltaStar_of_finite` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1017](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1017). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-local-min-zeckendorf-delta-star-of-fi).

## $\delta^*$ has no local extremum at infinite expansions in $E^*$

**$\delta^*$ has no local extremum at infinite expansions in $E^*$.** Let $L$ and $\tilde L$ be
lists of natural numbers of length at least $2$ with nonzero first entries whose periodic
Zeckendorf collections satisfy $E \subsetneq \tilde E$. Let $Q$ be a fundamental sequence of the
collection $E^*$ determined by $L$, let $\tilde Q$ be a fundamental sequence of the collection
$\tilde E^*$ determined by $\tilde L$, and let $\delta^*$ be the function determined by $L$,
$\tilde L$, $Q$ and $\tilde Q$. If $\varepsilon \in E^*$ has infinitely many nonzero entries, then
$\delta^*$ has neither a local minimum nor a local maximum at $\sum_k \varepsilon_k \tilde Q_k$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 7.

Stated but not proved: `MetaMathlibExt.not_isLocalExtr_zeckendorfDeltaStar_of_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1028](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1028). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#not-is-local-extr-zeckendorf-delta-star).

## Strict local maxima of $\delta^{\ast}$ at the closure points

Let $L$ and $\tilde L$ form a
periodic Zeckendorf pair, let $Q$ be a fundamental sequence of the collection $E^*$ determined by
$L$, and let $\tilde Q$ be a fundamental sequence of the collection $\tilde E^*$ determined by
$\tilde L$. Let $\varepsilon \in \bar E^* \setminus E^*$, where $\bar E^*$ is the closure
collection of $L$, and put $x = \sum_k \varepsilon_k \tilde Q_k$. Then, for the function
$\delta^*$ built from $L, \tilde L, Q, \tilde Q$, we have $\delta^*(y) < \delta^*(x)$ for all
$y \ne x$ sufficiently close to $x$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Proposition 8.

Stated but not proved: `MetaMathlibExt.eventually_zeckendorfDeltaStar_lt_of_mem_lStarClosure` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1040](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1040). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#eventually-zeckendorf-delta-star-lt-of-m).

## Classification of the local extrema of $\delta^\ast$

Let $L$ and $\tilde L$ form a
periodic Zeckendorf pair, let $Q$ and $\tilde Q$ be fundamental sequences of the $L^*$-collection
$E^*$ and the $\tilde L^*$-collection $\tilde E^*$, let $\bar E^*$ be the $L^*$-closure, and let
$\delta^*$ be the function determined by $L$, $\tilde L$, $Q$ and $\tilde Q$. For a coefficient
function $\varepsilon$ write $x_\varepsilon = \sum_k \varepsilon_k \tilde Q_k$. Then (i) for every
$\varepsilon \in \tilde E^*$ such that either $\varepsilon \notin \bar E^*$, or
$\varepsilon \in E^*$ and $\varepsilon$ has infinite support, $\delta^*$ has neither a local
minimum nor a local maximum at $x_\varepsilon$; (ii) for every $\varepsilon \in E^*$ with finite
support, $\delta^*$ has a local minimum at $x_\varepsilon$; and (iii) for every
$\varepsilon \in \bar E^* \setminus E^*$, $\delta^*$ has a local maximum at $x_\varepsilon$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 12.

Stated but not proved: `MetaMathlibExt.isLocalExtr_zeckendorfDeltaStar_classification` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1053](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1053). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-local-extr-zeckendorf-delta-star-clas).

## Generic upper bound for $\delta^*$ (Lemma 17)

**Generic upper bound for $\delta^*$ (Lemma 17).** Let $L$ and $\tilde L$ be lists of length at
least $2$ with nonzero first entries whose periodic Zeckendorf collections satisfy
$E \subsetneq \tilde E$, and let $Q$ and $\tilde Q$ be fundamental sequences of the collections
$E^*$ and $\tilde E^*$ of $L$ and $\tilde L$. Write $\omega$ and $\tilde\omega$ for the first terms
of $Q$ and $\tilde Q$, $\gamma = \log_{\tilde\omega} \omega$, $p$ for the generic exponent of $Q$
and $\tilde Q$, $\delta^*$ for the function $\delta^*$ of $L$, $\tilde L$, $Q$, $\tilde Q$,
$\overline{\mathrm{rev}}$ for the reversal map of $L$ (Definition 23), $\varepsilon_k$ for the
$k$th entry of a coefficient function $\varepsilon$ ($k \ge 1$), and
$\sum \varepsilon Q = \sum_{k \ge 1} \varepsilon_k Q_k$ (so that $Q_1 = \omega$). Then
$\delta^*(\sum \varepsilon \tilde Q) < (\omega / \tilde\omega)^p / \gamma$ for every
$\varepsilon \in \tilde E^*$, and every $\varepsilon \in \tilde E^*$ with
$\sum \varepsilon \tilde Q \ge \tilde\omega$ satisfies
$\delta^*(\sum \varepsilon \tilde Q) <
\sum \overline{\mathrm{rev}}(\varepsilon) Q / \sum \varepsilon \tilde Q <
(\omega / \tilde\omega)^p / \gamma$.

Without $\sum \varepsilon \tilde Q \ge \tilde\omega$ (the normalization $\varepsilon_1 \ge 1$ that
the proof of Lemma 17 assumes) the middle bound fails: for $L = (1, 0)$, $\tilde L = (1, 1)$ (so
$p = 2$) and $\varepsilon = \beta^4$ (a single $1$ in the fourth entry),
$\overline{\mathrm{rev}}(\varepsilon) = \varepsilon$ and the middle quotient is
$16 \omega^4 = 2.33436\ldots$, while $(\omega / \tilde\omega)^2 / \gamma = 2.20076\ldots$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 17.

Stated but not proved: `MetaMathlibExt.zeckendorfDeltaStar_lt_genericBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1073](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1073). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-delta-star-lt-generic-bound).

## Monotonicity of the ratio under steep increments

Let $L$ and $\tilde L$ form a periodic
Zeckendorf pair, let $Q$ be a fundamental sequence of the collection $E^*$ determined by $L$, and
let $\tilde Q$ be a fundamental sequence of the collection $\tilde E^*$ determined by $\tilde L$.
Put $\omega = Q_0$, $\tilde\omega = \tilde Q_0$ and $\gamma = \log_{\tilde\omega} \omega$, and let
$p$ be the generic exponent of $Q, \tilde Q$. Let $\varepsilon \in \tilde E^*$ with
$x = \sum_k \varepsilon_k \tilde Q_k \ge \tilde\omega$, and put
$y = \sum_k \overline{\mathrm{rev}}(\varepsilon)_k Q_k$, with $\overline{\mathrm{rev}}$ taken
with respect to $L$. If $\Delta x > 0$, $\Delta y > 0$ and
$(\omega / \tilde\omega)^p \le \Delta y / \Delta x$, then
$y / x^\gamma < (y + \Delta y) / (x + \Delta x)^\gamma$.

The hypothesis $x \ge \tilde\omega$ follows the reading of Lemma 17. As printed (for all
$\varepsilon \in \tilde E^*$) the lemma fails for $L = (1, 0)$, $\tilde L = (1, 1)$, $\varepsilon$
the coefficient function with a single $1$ at index $3$ ($x = 1/16$, $y = \omega^4$,
$y / x^\gamma = 1$), $\Delta x = 10^{-8}$ and $\Delta y = (\omega / \tilde\omega)^2 \Delta x$: the
right side is $0.99999999364\ldots$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 18.

Stated but not proved: `MetaMathlibExt.div_rpow_lt_add_div_add_rpow_of_genericBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1091](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1091). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#div-rpow-lt-add-div-add-rpow-of-generic).

## Monotonicity of the ratio under fundamental increments (Corollary 3)

Let $L$ and
$\tilde L$ form a periodic Zeckendorf pair, let $Q$ be a fundamental sequence of the collection
$E^*$ determined by $L$, and let $\tilde Q$ be a fundamental sequence of the collection
$\tilde E^*$ determined by $\tilde L$; indices start at $0$. Put $\omega = Q_0$,
$\tilde\omega = \tilde Q_0$ and $\gamma = \log_{\tilde\omega} \omega$, let $p$ be the generic
exponent of $Q$ and $\tilde Q$, let $\delta^*$ be the function $\delta^*$ of $L$, $\tilde L$, $Q$,
$\tilde Q$, and let $\overline{\mathrm{rev}}$ be the map determined by $L$. Let
$\varepsilon \in \tilde E^*$ with $x = \sum_k \varepsilon_k \tilde Q_k \ge \tilde\omega$, put
$y = \sum_k \overline{\mathrm{rev}}(\varepsilon)_k Q_k$, and let $m$ be a natural number with
$p \le m + 1$. Then $\delta^*(x) = y / x^\gamma$ and
$y / x^\gamma < (y + Q_m) / (x + \tilde Q_m)^\gamma$.

The hypothesis $x \ge \tilde\omega$ follows the reading of Lemma 17; in the paper's one-based
indexing $Q_m$ is $Q_n$ with $n = m + 1 \ge p$. As printed (for all $\varepsilon \in \tilde E^*$)
the corollary fails for $L = (1, 0)$, $\tilde L = (1, 1)$, $n = p = 2$ and
$\varepsilon = \beta^{11} + \beta^{13}$ (single ones in the paper's entries $11$ and $13$), for
which $\overline{\mathrm{rev}}(\varepsilon) = \varepsilon$: the left side $1.18363\ldots$ exceeds
the right side $1.01645\ldots$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Corollary 3.

Stated but not proved: `MetaMathlibExt.zeckendorfDeltaStar_lt_add_fundamental` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-delta-star-lt-add-fundamental).

## Where $\delta^\ast$ can attain its maximum

Let $L$ and $\tilde L$ be lists of natural
numbers forming a periodic Zeckendorf pair, let $N$ be the length of $L$, let $E^*$ and
$\tilde E^*$ be the collections determined by $L$ and $\tilde L$, let $\bar E^*$ be the closure
of $E^*$, and let $Q$ and $\tilde Q$ be fundamental sequences of $E^*$ and $\tilde E^*$. Let
$\delta^*$ be the function $\delta^*$ of $L$, $\tilde L$, $Q$, $\tilde Q$, and let $p$ be the
generic exponent of $Q$ and $\tilde Q$. Indices start at $0$: put $\omega = Q_0$ and
$\tilde\omega = \tilde Q_0$, write $\sum \varepsilon \tilde Q = \sum_k \varepsilon_k \tilde Q_k$
for a coefficient function $\varepsilon : \mathbb N \to \mathbb N$, and for $s \in \mathbb N$ let
$\bar\beta_s$ be the maximal $L^*$-block starting at index $s$. First, if $y \in (0, 1)$ and
$\delta^*(x) \le \delta^*(y)$ for all $x \in (0, 1)$, then $y = \sum \varepsilon \tilde Q$ for
some $\varepsilon \in \bar E^*$ with $\varepsilon \notin E^*$. Second, let $\ell \ge 1$ be a
natural number and let $\eta : \mathbb N \to \mathbb N$ be a sum of disjoint proper $L^*$-blocks
(possibly none) whose support intervals $[s, k]$ all satisfy $k < \ell - 1$. If
$\delta^*(x) \le \delta^*\bigl(\sum (\eta + \bar\beta_{\ell - 1}) \tilde Q\bigr)$ for all
$x \in (0, 1)$, then

$$
\ell < \max\left(2,\ p + 1 +
\frac{N \ln(1 / \omega) + \ln\left(1 - \sum \bar\beta_0 \tilde Q + \tilde\omega^N\right)}
{\ln(1 / \tilde\omega) - \ln(1 / \omega)}\right).
$$

In the source's one-based indexing $\bar\beta_s$ is $\bar\beta^{s+1}$, so the blocks
$\zeta^m$ of $\eta$ lie inside $[1, \ell - 1]$, the point is
$\sum (\sum_m \zeta^m + \bar\beta^\ell) \tilde Q$, and with $\varphi = 1 / \omega$,
$\tilde\varphi = 1 / \tilde\omega$ and $\rho = \sum \bar\beta^1 \tilde Q$ the right side is the
source's $\max\{2, p^*\}$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 13.

Stated but not proved: `MetaMathlibExt.isMaxOn_zeckendorfDeltaStar_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#is-max-on-zeckendorf-delta-star-bound).

## Where $\delta^*$ attains its minimum

**Where $\delta^*$ attains its minimum.** Let $L$ and $\tilde L$ be lists of natural numbers
of length at least $2$ with nonzero first entries whose periodic Zeckendorf collections satisfy
$E \subsetneq \tilde E$. Let $Q$ and $\tilde Q$ be fundamental sequences of the $L^*$-collections
$E^*$ of $L$ and $\tilde E^*$ of $\tilde L$, let $\delta^*$ be the function on $(0, 1)$ built from
$L$, $\tilde L$, $Q$ and $\tilde Q$, and let $p$ be the generic exponent of $Q$ and $\tilde Q$.
Indices start at $0$. Then there is $\varepsilon \in E^*$ with $\varepsilon_i = 0$ for every
$i \ge \max(2, p) - 1$ such that $\delta^*(\sum_k \varepsilon_k \tilde Q_k) \le \delta^*(y)$ for
all $y \in (0, 1)$. Moreover, if $p \le 2$, then $\delta^*(\tilde Q_0) \le \delta^*(y)$ for all
$y \in (0, 1)$ and $\delta^*(\tilde Q_0) = 1$.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Theorem 14.

Stated but not proved: `MetaMathlibExt.exists_isMinOn_zeckendorfDeltaStar` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#exists-is-min-on-zeckendorf-delta-star).

## Shifting a unit one entry down increases $\delta^*$ (Lemma 19)

**Shifting a unit one entry down increases $\delta^*$ (Lemma 19).** Let $N \ge 3$, let
$L = (1, \dots, 1, 0)$ ($N - 1$ ones followed by $0$, the $N$th order Zeckendorf collection) and
$\tilde L = (N - 1, \dots, N - 1)$ ($N$ entries, the base-$N$ collection), and let $Q$ and
$\tilde Q$ be fundamental sequences of the collections $E^*$ and $\tilde E^*$ of $L$ and
$\tilde L$. Write $\varepsilon_k$ for the $k$th entry of a coefficient function ($k \ge 1$),
$\beta^k$ for the coefficient function with a single $1$ in entry $k$,
$\sum \varepsilon \tilde Q = \sum_k \varepsilon_k \tilde Q_k$, $\delta^*$ for the function
$\delta^*$ of $L$, $\tilde L$, $Q$, $\tilde Q$, and $p$ for the generic exponent of $Q$ and
$\tilde Q$. Then $p = 1$ if $N \ge 4$. Moreover, let $\varepsilon \in E^*$ with
$\varepsilon_1 \ge 1$ and let $n \ge 3$ with $\varepsilon_n = 1$. If some decomposition of
$\varepsilon$ as a sum of disjoint proper $L^*$-blocks has a block whose support interval ends at
entry $n - 1$, then $\varepsilon' = \varepsilon + \beta^{n-1} - \beta^n$ lies in $E^*$ and
$\delta^*(\sum \varepsilon \tilde Q) < \delta^*(\sum \varepsilon' \tilde Q)$.

As printed, $p = 1$ fails for $N = 3$: with $\omega$ and $\tilde\omega$ the first terms of $Q$ and
$\tilde Q$ and $\gamma = \log_{\tilde\omega} \omega$, $\gamma = 0.55467\ldots$ exceeds
$\omega = 0.54368\ldots$, so $p = 2$. The inequality
$\delta^*(\sum \varepsilon \tilde Q) < \delta^*(\sum \varepsilon' \tilde Q)$ fails without
$\varepsilon_1 \ge 1$ (the normalization used where the paper applies it): $\varepsilon = \beta^4$
and $\varepsilon' = \beta^3$ give the value $1$ on both sides.

## Sources

- Sungkon Chang, *Distribution of Zeckendorf Expressions*, INTEGERS 25 (2025), Article A25, Lemma 19.

Stated but not proved: `MetaMathlibExt.zeckendorfDeltaStar_lt_shift_baseN` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean, line 1166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ZeckendorfBinaryExpansionWanted.lean#L1166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html#zeckendorf-delta-star-lt-shift-base-n).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distribution of Zeckendorf expressions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/numeration-automatic/distribution-of-zeckendorf-expressions)
