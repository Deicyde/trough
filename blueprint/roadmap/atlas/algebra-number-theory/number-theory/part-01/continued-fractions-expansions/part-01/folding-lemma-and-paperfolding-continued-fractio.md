---
declaration: section
origin: cited
lean: MetaMathlibExt.finiteContFrac, MetaMathlibExt.finiteContFrac_cons, MetaMathlibExt.finiteContFrac_singleton, MetaMathlibExt.finiteContFrac_one_two_two, MetaMathlibExt.finiteContFrac_add_inv_mul_den_sq, MetaMathlibExt.finiteContFrac_zero_merge, MetaMathlibExt.finiteContFrac_neg_block, MetaMathlibExt.paperfoldingSumTerm
statement: formalized
---

# Folding lemma and paperfolding continued fractions

19 results, 13 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html).

## Value of a finite continued fraction

For a finite list $a_0, a_1, \dots, a_t$ of integers
(possibly zero or negative), the value $[a_0; a_1, \dots, a_t]$ is the rational number
$a_0 + 1/(a_1 + 1/(\cdots + 1/a_t))$, computed from the right: the empty list has value $0$, and
the list $a_0, a_1, \dots, a_t$ has value $a_0 + v^{-1}$, where $v$ is the value of the list
$a_1, \dots, a_t$. In particular $[a] = a + 0^{-1} = a$; here and at any vanishing intermediate
denominator, $0^{-1}$ is taken to be $0$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Lemma 13 (bracket notation).

Formalized by `MetaMathlibExt.finiteContFrac`, a definition declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#finite-cont-frac).

## Recursion for finite continued fractions

For every integer $a$ and all integers
$l_1, \dots, l_n$ with $n \ge 0$, $[a; l_1, \dots, l_n] = a + [l_1; l_2, \dots, l_n]^{-1}$, where
the empty continued fraction (the case $n = 0$) has value $0$ and $0^{-1}$ is taken to be $0$
whenever $[l_1; l_2, \dots, l_n] = 0$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Lemma 13 (bracket notation).

Formalized by `MetaMathlibExt.finiteContFrac_cons`, a theorem declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#finite-cont-frac-cons).

## Continued fraction of length one

For every integer $a$, the finite continued fraction
$[a]$ has value $a$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Lemma 13 (bracket notation).

Formalized by `MetaMathlibExt.finiteContFrac_singleton`, a theorem declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#finite-cont-frac-singleton).

## The continued fraction $(1; 2, 2)$

The finite continued fraction $[1; 2, 2]$ has value
$7/5$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Lemma 13 (bracket notation).

Formalized by `MetaMathlibExt.finiteContFrac_one_two_two`, a theorem declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#finite-cont-frac-one-two-two).

## Folding lemma for finite continued fractions

Let $a_0$ be an integer, let $t$ be even
and let $a_1, \dots, a_t$ be integers with $a_i \ge 1$ for every $i$, and let $q$ be the
denominator in lowest terms of the value $[a_0; a_1, \dots, a_t]$ of the finite continued
fraction. Then for every integer $x \ge 1$,
$[a_0; a_1, \dots, a_t] + 1/(x q^2) = [a_0; a_1, \dots, a_t, x, -a_t, \dots, -a_1]$.

For positive partial quotients, $q$ is the continuant $q_t$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Lemma 13, equation (`eq:fold`) (`jis-2026-26.3.6-lem-13`).

Stated but not proved: `MetaMathlibExt.finiteContFrac_add_inv_mul_den_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#finite-cont-frac-add-inv-mul-den-sq).

## A zero partial quotient merges its neighbours

For all integers $a$ and $b$ and all finite
lists of integers $u_1, \dots, u_m$ and $v_1, \dots, v_n$ ($m, n \ge 0$), the finite continued
fractions satisfy $[u_1, \dots, u_m, a, 0, b, v_1, \dots, v_n] =
[u_1, \dots, u_m, a + b, v_1, \dots, v_n]$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Lemma 13, equation (`eq:normzero`) (`jis-2026-26.3.6-lem-13`).

Stated but not proved: `MetaMathlibExt.finiteContFrac_zero_merge` is written with `theorem_wanted` in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#finite-cont-frac-zero-merge).

## Normalizing a negated block

Let $x \ge 0$ be an integer, let $t \ge 2$ and let
$a_1, \dots, a_t$ be integers with $a_i \ge 1$ for every $i$. Then for every finite list of
integers $b_1, \dots, b_m$ ($m \ge 0$), the finite continued fractions satisfy
$[b_1, \dots, b_m, x, -a_t, -a_{t-1}, \dots, -a_1] =
[b_1, \dots, b_m, x - 1, 1, a_t - 1, a_{t-1}, \dots, a_1]$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Lemma 13, equation (`eq:normnegblock`) (`jis-2026-26.3.6-lem-13`).

Stated but not proved: `MetaMathlibExt.finiteContFrac_neg_block` is written with `theorem_wanted` in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#finite-cont-frac-neg-block).

## Terms of the paperfolding sums

For a sequence $x = (x_k)_{k \ge 0}$ of natural numbers,
the real numbers $s_k$ are defined by $s_0 = 1$ and $s_{k+1} = s_k^2 / x_k$, where the quotient is
read as $0$ when $x_k = 0$. They are the terms of the sums $S = \sum_k s_k$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Section 5, equation (`eq:sumform`).

Formalized by `MetaMathlibExt.paperfoldingSumTerm`, a definition declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#paperfolding-sum-term).

## First term of the paperfolding sums

For every sequence $x$ of natural numbers, the term
$s_0$ of the paperfolding sum terms defined by $x$ equals $1$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Section 5, equation (`eq:sumform`).

Formalized by `MetaMathlibExt.paperfoldingSumTerm_zero`, a theorem declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#paperfolding-sum-term-zero).

## Recursion for the paperfolding sum terms

For every sequence $x$ of natural numbers and
every $k \in \mathbb{N}$, the paperfolding sum terms defined by $x$ satisfy
$s_{k+1} = s_k^2 / x_k$, where the quotient is read as $0$ when $x_k = 0$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Section 5, equation (`eq:sumform`).

Formalized by `MetaMathlibExt.paperfoldingSumTerm_succ`, a theorem declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#paperfolding-sum-term-succ).

## Second term of the paperfolding sums

For every sequence $x$ of natural numbers with
$x_0 = 2$, the term $s_1$ of the paperfolding sum terms defined by $x$ equals $1/2$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Section 5, equation (`eq:sumform`).

Formalized by `MetaMathlibExt.paperfoldingSumTerm_one`, a theorem declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#paperfolding-sum-term-one).

## Interleaving creases into a Cloitre word

Given a sequence $c : \mathbb{N} \to \mathbb{N}$
and a start index $j$, the crease interleaving of a finite word $w$ of natural numbers reads $w$
from left to right as letters $(2)$ and $(1, 1)$ and inserts $c_j, c_{j+1}, c_{j+2}, \dots$ after
the successive letters. Precisely, the empty word gives the empty word; a word $2, w'$ gives
$2, c_j$ followed by the interleaving of $w'$ from index $j + 1$; a word $1, 1, w'$ gives
$1, 1, c_j$ followed by the interleaving of $w'$ from index $j + 1$; and any other nonempty word
$a, w'$ gives $a$ followed by the interleaving of $w'$ from the same index $j$.

The last case is unreachable on the approximants $A_k$ of Cloitre's sequence.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Theorem 14 (Cloitre's sequence occurs one `[1, 1]` or `[2]` at a time, interleaved with crease terms).

Formalized by `MetaMathlibExt.cloitreCreaseInterleave`, a definition declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#cloitre-crease-interleave).

## Crease interleaving of the Cloitre approximant $A_2$

For every sequence
$c : \mathbb{N} \to \mathbb{N}$, the crease interleaving by $c$, from start index $1$, of the
approximant $A_2 = (1, 1, 2, 1, 1, 1, 1)$ of Cloitre's sequence is
$(1, 1, c_1, 2, c_2, 1, 1, c_3, 1, 1, c_4)$: each of the four letters $(1, 1)$, $(2)$, $(1, 1)$,
$(1, 1)$ of $A_2$ is followed by its crease $c_1$, $c_2$, $c_3$, $c_4$ in turn.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Theorem 14.

Formalized by `MetaMathlibExt.cloitreCreaseInterleave_cloitreApprox_two`, a theorem declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#cloitre-crease-interleave-cloitre-approx).

## Continued-fraction words of the paperfolding sums

For a sequence $x = (x_k)_{k \ge 0}$ of
natural numbers, the finite words $A_k$ of natural numbers are defined by $A_0 = (1, 1)$ and
$A_{k+1} = A_k \, (x_{k+1} - 1) \, A_k^r$: the concatenation of $A_k$, the single letter
$\max(x_{k+1} - 1, 0)$ and the mirror image $A_k^r$ of $A_k$. The mirror image of a word reverses
it and then replaces a leading $2$ by $1, 1$, or two leading letters $1, 1$ by $2$, leaving any
other word unchanged.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Corollary 15.

Formalized by `MetaMathlibExt.paperfoldingContFracWord`, a definition declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#paperfolding-cont-frac-word).

## The second paperfolding continued-fraction word

For every sequence $x$ of natural numbers,
the continued-fraction word $A_1$ defined by $x$ is $(1, 1, \max(x_1 - 1, 0), 2)$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Corollary 15.

Formalized by `MetaMathlibExt.paperfoldingContFracWord_one`, a theorem declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#paperfolding-cont-frac-word-one).

## The paperfolding continued-fraction word $A_2$ for constant $x_k = 6$

Let $x_k = 6$
for every $k$, and let $A_0 = (1, 1)$ and $A_{k+1} = A_k\,(x_{k+1} - 1)\,A_k^r$, where the
mirror image $A^r$ of a word $A$ is obtained by reversing $A$ and then replacing a leading $2$
by $1, 1$, or two leading letters $1, 1$ by $2$, leaving any other word unchanged. Then
$A_2 = (1, 1, 5, 2, 5, 1, 1, 5, 1, 1)$.

This is the start of the paper's expansion of $6 \sum_{k \ge 0} 12^{-2^k}$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Corollary 15 and Section 6.

Formalized by `MetaMathlibExt.paperfoldingContFracWord_const_six_two`, a theorem declared in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#paperfolding-cont-frac-word-const-six-tw).

## Continued fraction of a paperfolding sum in Cloitre and ruler order

Let
$x = (x_k)_{k \ge 0}$ be natural numbers with $x_0 = 2$ and $x_k \ge 2$ for all $k$, let $s_k$ be
the paperfolding sum terms defined by $x$, and let $S = \sum_{k \ge 0} s_k$, with continued
fraction expansion $[a_0; a_1, a_2, \ldots]$. For $j \ge 1$ let $c_j = x_{\nu_2(j) + 1} - 1$, where
$\nu_2(j)$ is the exponent of $2$ in $j$. Then $a_0 = 1$, and for every $k$ the partial quotients
$a_1, a_2, \ldots$ begin with the word obtained from the $k$-th approximant $A_k$ of Cloitre's
sequence by splitting $A_k$ from the left into letters $1, 1$ and $2$ and inserting $c_j$ after
its $j$-th letter, for every $j$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Theorem 14 (`jis-2026-26.3.6-thm-14`).

Stated but not proved: `MetaMathlibExt.paperfoldingSum_contFrac_cloitre_ruler` is written with `theorem_wanted` in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#paperfolding-sum-cont-frac-cloitre-ruler).

## Continued fraction of a paperfolding sum via the words $A_k$

Let $x = (x_k)_{k \ge 0}$ be
natural numbers with $x_0 = 2$ and $x_k \ge 2$ for all $k$, let $s_k$ be the paperfolding sum
terms defined by $x$, and let $S = \sum_{k \ge 0} s_k$, with continued fraction expansion
$[a_0; a_1, a_2, \ldots]$. Let $A_k$ be the continued-fraction words defined by $x$, so that
$A_0 = (1, 1)$ and $A_{k+1} = A_k \, (x_{k+1} - 1) \, A_k^r$, where the mirror image $A^r$ of a
word $A$ is obtained by reversing $A$ and then replacing a leading $2$ by $1, 1$, or two leading
letters $1, 1$ by $2$, leaving any other word unchanged. Then $a_0 = 1$, and for every $k$ the
partial quotients $a_1, a_2, \ldots$ begin with the word $A_k$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Corollary 15 (`jis-2026-26.3.6-cor-15`).

Stated but not proved: `MetaMathlibExt.paperfoldingSum_contFrac_recursion` is written with `theorem_wanted` in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#paperfolding-sum-cont-frac-recursion).

## Digit frequencies in Cloitre's approximants

Let $A_k$ be the $k$-th approximant of
Cloitre's sequence. As $k \to \infty$, the proportion of entries of $A_k$ equal to $1$ tends to
$2/3$, and the proportion of entries equal to $2$ tends to $1/3$.

## Sources

- Daniel J. Hoyt, *The Self-Describing Paperfolding Sequence in Continued Fractions*, Journal of Integer Sequences 29 (2026), Article 26.3.6, Theorem 17 (`jis-2026-26.3.6-thm-17`).

Stated but not proved: `MetaMathlibExt.tendsto_cloitreApprox_count_div_length` is written with `theorem_wanted` in [WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ContinuedFractionFoldingWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html#tendsto-cloitre-approx-count-div-length).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Folding lemma and paperfolding continued fractions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/folding-lemma-and-paperfolding-continued-fractio)
