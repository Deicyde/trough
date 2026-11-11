---
declaration: section
origin: cited
lean: MetaMathlibExt.BothLettersInfinite, MetaMathlibExt.letterPosition, MetaMathlibExt.relativePosition, MetaMathlibExt.letterPosition_one_of_head, MetaMathlibExt.relativePosition_one_of_head_ab, MetaMathlibExt.exists_word_letterPosition_eq_iff, MetaMathlibExt.eq_iff_relativePosition_eq, MetaMathlibExt.exists_word_relativePosition_eq_of_monotone
statement: formalized
---

# Relative position in binary words

63 results, 13 proved and 50 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html).

## Binary words in which both letters occur infinitely often

An infinite word
$w = \ell_0 \ell_1 \ell_2 \cdots$ over the letters $a$ and $b$ belongs to the set $\mathcal{W}$ when
both letters occur infinitely often in it, that is, when there are infinitely many positions $i$
with $\ell_i = a$ and infinitely many positions $i$ with $\ell_i = b$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 2 (definition of `𝒲`).

Formalized by `MetaMathlibExt.BothLettersInfinite`, a definition declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#both-letters-infinite).

## Position function of a letter

For an infinite binary word $w = \ell_0 \ell_1 \cdots$,
a letter $\alpha$ and $n \ge 1$, $p_\alpha(n)$ is the position of the $n$-th occurrence of $\alpha$
in $w$, counting positions from $0$; that is, $p_\alpha(n)$ is the $n$-th smallest index $i$ with
$\ell_i = \alpha$.

By convention $p_\alpha(n) = 0$ when $\alpha$ occurs fewer than $n$ times in $w$, and
$p_\alpha(0) = p_\alpha(1)$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 2 (definition of position functions).

Formalized by `MetaMathlibExt.letterPosition`, a definition declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position).

## Relative position function

Let $w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite word over
$\{a, b\}$, and for a letter $\alpha$ and $n \ge 1$ let $p_\alpha(n)$ be the position (counting
from $0$) of the $n$-th occurrence of $\alpha$ in $w$, or $0$ if $\alpha$ occurs fewer than $n$
times. The relative position function of $w$ is the integer-valued function
$r(n) = p_b(n) - p_a(n)$, $n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 2 (definition of the relative position function).

Formalized by `MetaMathlibExt.relativePosition`, a definition declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position).

## Position of the first occurrence of the initial letter

If an infinite binary word $w$
starts with the letter $\alpha$, then the first occurrence of $\alpha$ in $w$ is at position $0$,
that is, $p_\alpha(1) = 0$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 2 (definition of position functions).

Formalized by `MetaMathlibExt.letterPosition_one_of_head`, a theorem declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-one-of-head).

## Relative position of a word starting with $ab$

If an infinite word $w$ over $\{a, b\}$
starts with $ab$, then its relative position function satisfies $r(1) = 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 2 (definition of the relative position function).

Formalized by `MetaMathlibExt.relativePosition_one_of_head_ab`, a theorem declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-one-of-head-ab).

## Characterization of the position functions

Let $p$ be a function from the natural
numbers to the natural numbers. There is an infinite word $w$ over the letters $a$ and $b$ that
starts with $a$, in which both letters occur infinitely often, and whose position function for
$a$ satisfies $p_a(n) = p(n)$ for all $n \ge 1$, if and only if $p(n) < p(n+1)$ for all $n \ge 1$,
$p(1) = 0$, and $p(n+1) - p(n) > 1$ for infinitely many $n \ge 1$. Likewise, there is an infinite
word over $a$ and $b$ that starts with $a$, in which both letters occur infinitely often, and
whose position function for $b$ satisfies $p_b(n) = p(n)$ for all $n \ge 1$, if and only if
$p(n) < p(n+1)$ for all $n \ge 1$, $p(1) > 0$, and $p(n+1) - p(n) > 1$ for infinitely many
$n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 4 (`jis-2025-25.1.5-lem-4`).

Stated but not proved: `MetaMathlibExt.exists_word_letterPosition_eq_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#exists-word-letter-position-eq-iff).

## The relative position function determines the word

Let $w$ and $w'$ be infinite words
over the letters $a$ and $b$ in each of which both letters occur infinitely often, and let $r_w$
and $r_{w'}$ be their relative position functions. Then $w = w'$ if and only if
$r_w(n) = r_{w'}(n)$ for every $n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 5 (`jis-2025-25.1.5-lem-5`).

Stated but not proved: `MetaMathlibExt.eq_iff_relativePosition_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#eq-iff-relative-position-eq).

## Non-decreasing functions as relative position functions

Let $r$ be a function from the
natural numbers to the natural numbers with $r(n) \ge 1$ and $r(n) \le r(n+1)$ for every
$n \ge 1$. Then there is an infinite word $w$ over the letters $a$ and $b$ that starts with $a$,
in which both letters occur infinitely often, and whose relative position function satisfies
$r_w(n) = r(n)$ for every $n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 8 (`jis-2025-25.1.5-lem-8`).

Stated but not proved: `MetaMathlibExt.exists_word_relativePosition_eq_of_monotone` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#exists-word-relative-position-eq-of-mono).

## Non-increasing functions as relative position functions

Let $r$ be a function from the
natural numbers to the integers with $r(1) < 0$ and $r(n+1) \le r(n)$ for every $n \ge 1$. Then
there is an infinite word $w$ over the letters $a$ and $b$ that starts with $b$, in which both
letters occur infinitely often, and whose relative position function satisfies $r_w(n) = r(n)$
for every $n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Corollary 9 (`jis-2025-25.1.5-cor-9`).

Stated but not proved: `MetaMathlibExt.exists_word_relativePosition_eq_of_antitone` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#exists-word-relative-position-eq-of-anti).

## Runs of one letter and gaps between letter positions

Let $w = \ell_0 \ell_1 \ell_2 \cdots$
be an infinite word over the letters $a$ and $b$ in which both letters occur infinitely often and
$\ell_0 = a$. For a letter $\alpha$ and $n \ge 1$, let $p_\alpha(n)$ be the position of the $n$-th
occurrence of $\alpha$ in $w$, counting positions from $0$. Let $k \ge 1$. Then the following are
equivalent: there is $i$ with $\ell_{i+j} = b$ for all $0 \le j < k$ (the block $b^k$ occurs in
$w$); there is $n \ge 1$ with $p_a(n+1) - p_a(n) > k$; and there is $n \ge 1$ with
$p_b(n+j+1) - p_b(n+j) = 1$ for all $0 \le j < k - 1$. Moreover, there is $i$ with
$\ell_{i+j} = a$ for all $0 \le j < k$ (the block $a^k$ occurs in $w$) if and only if there is
$n \ge 1$ with $p_a(n+j+1) - p_a(n+j) = 1$ for all $0 \le j < k - 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 13 (`jis-2025-25.1.5-lem-13`).

Stated but not proved: `MetaMathlibExt.subword_run_iff_letterPosition_diff` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#subword-run-iff-letter-position-diff).

## Monotonicity of the relative position function and runs of letters

Let $w$ be an
infinite word over $\{a, b\}$ that starts with $a$ and in which both letters occur infinitely
often, let $r$ be its relative position function, and write $\Delta r(n) = r(n+1) - r(n)$. A
factor of $w$ is a block of consecutive letters. (a) If $r(n) < r(n+1)$ for all $n \ge 1$, then
$bb$ is not a factor of $w$. (b) If $bb$ is not a factor of $w$, then $r(n) \le r(n+1)$ for all
$n \ge 1$. (c) For every $k \ge 0$, if $b^k$ is a factor of $w$, then there is $n \ge 0$ with
$\Delta r(n+j) \le 0$ for all $1 \le j \le k - 1$. (d) For every $k \ge 0$, if $a^k$ is a factor
of $w$, then there is $n \ge 0$ with $\Delta r(n+j) \ge 0$ for all $1 \le j \le k - 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 14 (`jis-2025-25.1.5-lem-14`).

Stated but not proved: `MetaMathlibExt.relativePosition_monotonicity_runs` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-monotonicity-runs).

## Relative position increments without long runs of b

Let $w = \ell_0 \ell_1 \ell_2 \cdots$
be an infinite word over the letters $a$ and $b$ in which both letters occur infinitely often and
whose first letter $\ell_0$ is $a$. Let $p_b$ be its position function for the letter $b$, let $r$
be its relative position function, and write $\Delta s(n) = s(n+1) - s(n)$. Let $k$ be a natural
number such that $w$ contains no $k$ consecutive letters $b$, that is, there is no $i$ with
$\ell_{i+j} = b$ for all $j < k$. Then $|\Delta r(n) - \Delta p_b(n)| \le k$ for every $n \ge 1$.
Moreover, $|\Delta r(n)|$ is bounded over $n \ge 1$ if and only if $\Delta p_b(n)$ is bounded over
$n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 15 (`jis-2025-25.1.5-lem-15`).

Stated but not proved: `MetaMathlibExt.abs_relativePosition_diff_sub_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#abs-relative-position-diff-sub-le).

## Periodicity of a word and of the gaps between occurrences of its letters

Let
$w = w_0 w_1 w_2 \cdots$ be an infinite binary word over $\{a, b\}$ that starts with $a$ and in
which both letters occur infinitely often. Let $p_\alpha(n)$ be the position (counted from $0$)
of the $n$-th occurrence of the letter $\alpha$ in $w$, and $\Delta p_\alpha(n) =
p_\alpha(n+1) - p_\alpha(n)$. Call a sequence $s$ periodic if there is $q > 0$ with
$s(n + q) = s(n)$ for all $n \ge 1$. The following are equivalent: $w$ is periodic, that is,
$w_{i+q} = w_i$ for some $q > 0$ and all $i \ge 0$; $\Delta p_a$ is periodic; $\Delta p_a$ and
$\Delta p_b$ are both periodic. Moreover, if $w = u^\omega$ for a nonempty finite word $u$ with
$k$ letters $a$ and $j$ letters $b$, then $\Delta p_a(n + k) = \Delta p_a(n)$ and
$\Delta p_b(n + j) = \Delta p_b(n)$ for all $n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 16 (`jis-2025-25.1.5-lem-16`).

Stated but not proved: `MetaMathlibExt.periodic_iff_letterPosition_diff_periodic` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#periodic-iff-letter-position-diff-period).

## Periodicity of the relative position differences

Let $w = w_0 w_1 w_2 \cdots$ be an
infinite word over $\{a, b\}$ in which both letters occur infinitely often, let $p_a(n)$ and
$p_b(n)$ be the positions of the $n$-th $a$ and the $n$-th $b$ in $w$, let
$r(n) = p_b(n) - p_a(n)$, and let $\Delta r(n) = r(n + 1) - r(n)$. If $w$ is purely periodic
(there is $q > 0$ with $w_{i + q} = w_i$ for all $i \ge 0$), then there is $q > 0$ with
$\Delta r(n + q) = \Delta r(n)$ for all $n \ge 1$. Moreover, if $w = uuu\cdots$ for a nonempty
finite word $u$ containing $k$ letters $a$ and $j$ letters $b$, then
$\Delta r(n + \operatorname{lcm}(k, j)) = \Delta r(n)$ for all $n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Corollary 17 (`jis-2025-25.1.5-cor-17`).

Stated but not proved: `MetaMathlibExt.relativePosition_diff_periodic_of_periodic` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-diff-periodic-of-perio).

## Bounds on position functions for words with bounded runs

Let $w$ be an infinite binary
word over $\{a, b\}$ that starts with $a$ and in which both letters occur infinitely often, and
let $c \ge 0$ be an integer such that every block of consecutive equal letters of $w$ has length
at most $c$. Write $p_\alpha(n)$ for the position (counted from $0$) of the $n$-th occurrence of
the letter $\alpha$ in $w$, and $r(n) = p_b(n) - p_a(n)$. Then for every $n \ge 1$,
$p_a(n) \le (c+1)(n-1)$, $p_b(n) \le (c+1)n - 1$ and $c(1-n) + 1 \le r(n) \le cn$.

The paper prints the lower bound $(1-c)n + 1 \le r(n)$, which is false: for $w = (abb)^\omega$
and $c = 2$, $r(4) = 5 - 9 = -4 < -3$. The bound $c(1-n) + 1$ is the one derived in the paper's
proof. Stating the result for every bound $c$ of the runs is equivalent to stating it for the
longest run.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 25 (`jis-2025-25.1.5-lem-25`).

Stated but not proved: `MetaMathlibExt.letterPosition_le_of_run_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-le-of-run-le).

## Linear bounds for words with bounded runs

Let $w$ be an infinite binary word over the
letters $a$ and $b$ in which both letters occur infinitely often, and let $c$ be a natural number
such that every block of consecutive equal letters of $w$ has length at most $c$. Let $p_a(n)$
and $p_b(n)$ be the positions (counting from $0$) of the $n$-th $a$ and the $n$-th $b$ in $w$, and
let $r(n) = p_b(n) - p_a(n)$. Then for every $n \ge 1$, $p_a(n) \le (c+1)n - 1$,
$p_b(n) \le (c+1)n - 1$ and $-cn \le r(n) \le cn$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Corollary 27 (`jis-2025-25.1.5-cor-27`).

Stated but not proved: `MetaMathlibExt.letterPosition_le_of_run_le'` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-le-of-run-le-2).

## Deleting the first occurrence of a letter

Let $w = \ell_0 \ell_1 \ell_2 \cdots$ be an
infinite word over the letters $a$ and $b$, let $\alpha$ be a letter, and let $p$ be the position
(counted from $0$) of the first occurrence of $\alpha$ in $w$, with $p = 0$ if $\alpha$ does not
occur in $w$. The word $D_\alpha(w)$ has letter $\ell_i$ at each position $i < p$ and letter
$\ell_{i+1}$ at each position $i \ge p$. So $D_\alpha(w)$ is $w$ with its first $\alpha$ deleted,
and, when $\alpha$ does not occur in $w$, it is $w$ with its first letter deleted.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 2 (definition of the deletion operators `D_a`, `D_b`).

Formalized by `MetaMathlibExt.deleteFirst`, a definition declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#delete-first).

## The deletion operator

For an infinite word $w$ over the letters $a$ and $b$, the word
$D(w)$ is $D_a(D_b(w))$, where $D_\alpha$ deletes the first occurrence of the letter $\alpha$
(and deletes the first letter of a word in which $\alpha$ does not occur): first apply $D_b$,
then $D_a$. When both letters occur in $w$, $D(w)$ is $w$ with its first $b$ and its first $a$
deleted.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 2 (definition of the deletion operator `D`).

Formalized by `MetaMathlibExt.deletion`, a definition declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#deletion).

## Deleting a leading letter

Let $w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite word
over the letters $a$ and $b$, let $\alpha$ be a letter, and let $D_\alpha$ be the operator that
deletes the first occurrence of $\alpha$ from a word (and deletes the first letter of a word in
which $\alpha$ does not occur). If $\ell_0 = \alpha$, then $D_\alpha$ shifts $w$ by one:
$D_\alpha(w) = \ell_1 \ell_2 \ell_3 \cdots$, that is, the letter of $D_\alpha(w)$ at each
position $i$ is $\ell_{i+1}$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 2 (definition of the deletion operators).

Formalized by `MetaMathlibExt.deleteFirst_of_head`, a theorem declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#delete-first-of-head).

## Letter-counting function

Let $w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite binary
word, $\alpha$ a letter and $m$ a natural number. The counting function $\#_\alpha(m)$ is the
number of indices $i < m$ with $\ell_i = \alpha$, that is, the number of letters $\alpha$ among
the first $m$ letters $\ell_0, \dots, \ell_{m-1}$ of $w$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 3 (definition of the counting function).

Formalized by `MetaMathlibExt.letterCount`, a definition declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-count).

## The letter-counting function at zero

For every infinite binary word $w$ and every
letter $\alpha$, $\#_\alpha(0) = 0$, where $\#_\alpha(m)$ is the number of letters $\alpha$ among
the first $m$ letters of $w$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 3 (definition of the counting function).

Formalized by `MetaMathlibExt.letterCount_zero`, a theorem declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-count-zero).

## Recursion for the letter-counting function

Let $w = \ell_0 \ell_1 \ell_2 \cdots$ be an
infinite binary word, $\alpha$ a letter and $m$ a natural number, and let $\#_\alpha(m)$ be the
number of letters $\alpha$ among $\ell_0, \dots, \ell_{m-1}$. Then $\#_\alpha(m+1)$ equals
$\#_\alpha(m) + 1$ if $\ell_m = \alpha$, and $\#_\alpha(m)$ otherwise.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 3 (definition of the counting function).

Formalized by `MetaMathlibExt.letterCount_succ`, a theorem declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-count-succ).

## Reconstruction of a binary word from its relative position function

Let $w$ be an
infinite binary word over $\{a, b\}$ in which both letters occur infinitely often, let $p_a(n)$
and $p_b(n)$ be the positions (counted from $0$) of the $n$-th $a$ and the $n$-th $b$ in $w$, and
let $r(n) = p_b(n) - p_a(n)$. If $r(1) > 0$ then $p_a(1) = 0$ and $p_b(1) = r(1)$; if $r(1) < 0$
then $p_a(1) = -r(1)$ and $p_b(1) = 0$. For every $n \ge 1$, let $k_{n+1}$ be the least natural
number different from all of $p_a(1), \dots, p_a(n), p_b(1), \dots, p_b(n)$. If $r(n+1) > 0$ then
$p_a(n+1) = k_{n+1}$ and $p_b(n+1) = k_{n+1} + r(n+1)$; if $r(n+1) < 0$ then
$p_a(n+1) = k_{n+1} - r(n+1)$ and $p_b(n+1) = k_{n+1}$.

The paper states this as an algorithm; here its output is stated as equalities with the true
positions. Since $r(1) \ne 0$, the paper's "otherwise" in the first step is the case $r(1) < 0$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 6 (`jis-2025-25.1.5-lem-6`).

Stated but not proved: `MetaMathlibExt.letterPosition_reconstruction` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-reconstruction).

## Reflection of binary words and relative position

Let $\mathcal{W}$ be the set of
infinite words over $\{a, b\}$ in which both letters occur infinitely often, and let
$a\mathcal{W}$ and $b\mathcal{W}$ be its words that begin with $a$ and with $b$. For a word $w$
let $\bar w$ be its reflection, obtained by exchanging $a$ and $b$ at every position, and let
$r_w(n) = p_b(n) - p_a(n)$ be its relative position function, where $p_a(n)$ and $p_b(n)$ are
the positions of the $n$-th $a$ and the $n$-th $b$ in $w$. Then (a) the map $w \mapsto \bar w$
sends $a\mathcal{W}$ onto $b\mathcal{W}$ and $b\mathcal{W}$ onto $a\mathcal{W}$; and (b) for all
$w, w' \in \mathcal{W}$, $\bar w = w'$ if and only if $r_w(n) = -r_{w'}(n)$ for every $n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Proposition 11 (`jis-2025-25.1.5-prop-11`).

Stated but not proved: `MetaMathlibExt.reflection_image_and_relativePosition` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#reflection-image-and-relative-position).

## Periodicity of the gaps between the $b$'s

Let $w$ be an infinite binary word over the
letters $a$ and $b$ in which both letters occur infinitely often, let $p_b(n)$ be the position
(counting from $0$) of the $n$-th $b$ in $w$, and let $\Delta p_b(n) = p_b(n+1) - p_b(n)$. Let
$D_a$ delete the first $a$ of a word, and let $v = D_a^{p_b(1)}(w)$, the word $w$ with its initial
run of $a$'s deleted. Then there is $q > 0$ with $\Delta p_b(n + q) = \Delta p_b(n)$ for all
$n \ge 1$ if and only if there is $q > 0$ such that, for every $i \ge 0$, the letters of $v$ at
positions $i + q$ and $i$ are equal.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 19 (`jis-2025-25.1.5-lem-19`).

Stated but not proved: `MetaMathlibExt.letterPosition_diff_periodic_iff_deleteFirst_periodic` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-diff-periodic-iff-delete).

## Prepending an equilibrious word is undone by deletion

Let $u$ be a finite word in the
letters $a$ and $b$ of length $2k$. Then $u$ is equilibrious, that is, $a$ and $b$ occur equally
often in $u$, if and only if $D^k(uw) = w$ for every infinite binary word $w$ in which both
letters occur infinitely often, where $D$ deletes the first $b$ and the first $a$ of a word.

Here $a$ and $b$ play the roles of the letters $0$ and $1$ in the definition of equilibrious
words.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 21 (`jis-2025-25.1.5-lem-21`).

Stated but not proved: `MetaMathlibExt.isEquilibriousWord_iff_deletion_iterate_prepend` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#is-equilibrious-word-iff-deletion-iterat).

## Prepending an equilibrious word shifts the position functions

Let $u$ be a finite word
over $\{a, b\}$ of length $2k$ that is equilibrious (it contains as many letters $a$ as letters
$b$), and let $w$ be an infinite binary word in which both letters occur infinitely often. For a
word $v$, write $p_{\alpha,v}(n)$ for the position (counted from $0$) of the $n$-th occurrence of
the letter $\alpha$ in $v$, and $r_v(n) = p_{b,v}(n) - p_{a,v}(n)$. Then for every $n \ge 1$ the
concatenation $uw$ satisfies $p_{a,uw}(n+k) = p_{a,w}(n) + 2k$, $p_{b,uw}(n+k) = p_{b,w}(n) + 2k$
and $r_{uw}(n+k) = r_w(n)$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 22 (`jis-2025-25.1.5-lem-22`).

Stated but not proved: `MetaMathlibExt.letterPosition_prepend_equilibrious` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-prepend-equilibrious).

## Position functions of a cloned word

Let $w$ be an infinite binary word over the
letters $a$ and $b$ in which both letters occur infinitely often, let $k$ be a natural number,
and let $\varphi_k(w)$ be the word whose letter at position $i$ is the letter of $w$ at position
$\lfloor i/k \rfloor$ (for $k \ge 1$, the word obtained from $w$ by repeating each letter $k$
times). For a word $v$ and a letter $\alpha$, let $p_{\alpha,v}(n)$ be the position (counting
from $0$) of the $n$-th occurrence of $\alpha$ in $v$, and let $r_v(n) = p_{b,v}(n) - p_{a,v}(n)$.
Then for all natural numbers $m$ and $j$ with $1 \le j \le k$,
$p_{a,\varphi_k(w)}(mk+j) = k\,p_{a,w}(m+1) + j - 1$,
$p_{b,\varphi_k(w)}(mk+j) = k\,p_{b,w}(m+1) + j - 1$ and
$r_{\varphi_k(w)}(mk+j) = k\,r_w(m+1)$.

The paper takes $k \ge 2$; the identities hold for $k = 1$ ($\varphi_1$ is the identity) and are
vacuous for $k = 0$, so no bound on $k$ is assumed.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 24 (`jis-2025-25.1.5-lem-24`).

Stated but not proved: `MetaMathlibExt.letterPosition_clone` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-clone).

## Letter frequency and growth of letter positions

Let $w = \ell_0 \ell_1 \ell_2 \cdots$ be
an infinite word over the letters $a$ and $b$ in which both letters occur infinitely often, and
let $\alpha$ be a letter. Write $\#_\alpha(m)$ for the number of occurrences of $\alpha$ among
$\ell_0, \ldots, \ell_{m-1}$, and for $n \ge 1$ write $p_\alpha(n)$ for the position of the
$n$-th occurrence of $\alpha$ in $w$, counting positions from $0$. Then (a) for every real $d$
with $0 < d \le 1$, $\#_\alpha(m)/m \to d$ as $m \to \infty$ if and only if
$p_\alpha(n)/n \to 1/d$ as $n \to \infty$; and (b) $\#_\alpha(m)/m \to 0$ as $m \to \infty$ if and
only if $p_\alpha(n)/n \to \infty$ as $n \to \infty$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 28 (`jis-2025-25.1.5-lem-28`).

Stated but not proved: `MetaMathlibExt.tendsto_letterCount_div_iff_tendsto_letterPosition_div` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#tendsto-letter-count-div-iff-tendsto-let).

## Upper and lower densities of a letter from its position function

Let $w$ be an infinite
binary word in which both letters occur infinitely often and let $\alpha$ be a letter. Write
$\#_\alpha(m)$ for the number of occurrences of $\alpha$ among the first $m$ letters of $w$, and
$p_\alpha(n)$ for the position (counted from $0$) of the $n$-th occurrence of $\alpha$. Then
$\limsup_{m \to \infty} \#_\alpha(m)/m = \limsup_{n \to \infty} n/p_\alpha(n)$ and
$\liminf_{m \to \infty} \#_\alpha(m)/m = \liminf_{n \to \infty} n/p_\alpha(n)$.

Both sequences are bounded, so these are the classical upper and lower limits in $\mathbb{R}$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Corollary 29 (`jis-2025-25.1.5-cor-29`).

Stated but not proved: `MetaMathlibExt.limsup_liminf_letterCount_div` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#limsup-liminf-letter-count-div).

## Letter frequencies and the growth of the position functions

Let $w$ be an infinite
binary word over the letters $a$ and $b$ in which both letters occur infinitely often, and let
$0 < d < 1$. For a letter $\alpha$, let $\#_\alpha(m)$ be the number of letters $\alpha$ among the
first $m$ letters of $w$, and let $p_\alpha(n)$ be the position (counting from $0$) of the $n$-th
occurrence of $\alpha$ in $w$. Then the following are equivalent: $\#_b(m)/m \to d$ as
$m \to \infty$; $\#_a(m)/m \to 1 - d$; $p_b(n)/n \to 1/d$ as $n \to \infty$;
$p_a(n)/n \to 1/(1 - d)$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 30 (`jis-2025-25.1.5-thm-30`).

Stated but not proved: `MetaMathlibExt.letter_frequency_tfae` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-frequency-tfae).

## Relative position of a word with given letter frequency

Let
$w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite word over the letters $a$ and $b$. Let $\#_b(m)$
be the number of letters $b$ among $\ell_0, \ldots, \ell_{m-1}$, and for $n \ge 1$ let
$r(n) = p_b(n) - p_a(n)$, where $p_\alpha(n)$ is the position of the $n$-th occurrence of the
letter $\alpha$ in $w$, counting positions from $0$. If $0 < d < 1$ and $\#_b(m)/m \to d$ as
$m \to \infty$, then $r(n)/n \to 1/d - 1/(1-d)$ as $n \to \infty$.

Such a word contains both letters infinitely often, so no separate hypothesis that both letters
occur infinitely often is needed.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Corollary 31 (`jis-2025-25.1.5-cor-31`).

Stated but not proved: `MetaMathlibExt.tendsto_relativePosition_div_of_frequency` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#tendsto-relative-position-div-of-frequen).

## The frequency of $b$ from the growth of the relative position

Let $w$ be an infinite
binary word in which both letters $a$ and $b$ occur infinitely often, let $r$ be its relative
position function, and suppose that $r(n)/n$ converges to $L$ in the extended real line
$[-\infty, \infty]$. Let $\#_b(m)$ be the number of letters $b$ among the first $m$ letters of
$w$. Then $\#_b(m)/m$ converges, and its limit, the frequency of $b$ in $w$, is $0$ if
$L = \infty$, $1$ if $L = -\infty$, $1/2$ if $L = 0$, and
$(2 + L - \sqrt{4 + L^2})/(2L)$ if $L$ is a nonzero real number.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Proposition 33 (`jis-2025-25.1.5-prop-33`).

Stated but not proved: `MetaMathlibExt.frequency_of_tendsto_relativePosition_div` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#frequency-of-tendsto-relative-position-d).

## Mean values of the position functions

Let $w$ be an infinite word over $\{a, b\}$ in
which both letters occur infinitely often, with letter position functions $p_a$, $p_b$ and
relative position function $r$, and consider the sequences $r(n)/n$, $p_b(n)/n$ and $p_a(n)/n$
in the extended reals $[-\infty, \infty]$. If one of the three sequences converges, then so do
the other two. If $p_b(n)/n \to p$ and $p_a(n)/n \to q$, then $1/p + 1/q = 1$, where
$1/\infty = 0$. If $r(n)/n \to x$ with $x$ real, then
$p_b(n)/n \to (2 + x + \sqrt{4 + x^2})/2$ and $p_a(n)/n \to (2 - x + \sqrt{4 + x^2})/2$. If
$r(n)/n \to \infty$, then $p_b(n)/n \to \infty$ and $p_a(n)/n \to 1$; if $r(n)/n \to -\infty$,
then $p_b(n)/n \to 1$ and $p_a(n)/n \to \infty$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 34 (`jis-2025-25.1.5-thm-34`).

Stated but not proved: `MetaMathlibExt.relativePosition_letterPosition_mean_values` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-letter-position-mean-v).

## Image of an infinite word under a substitution

Let $\varrho$ be a substitution on the
letters $a$ and $b$, sending each letter to a finite word and extended to finite words by
concatenation, and let $w = \ell_0 \ell_1 \ell_2 \cdots$ and $v$ be infinite binary words. Then
$v$ is the image $\varrho(w)$ of $w$ when, for every $m$, the finite word
$\varrho(\ell_0 \cdots \ell_{m-1})$ is a prefix of $v$, and these words are arbitrarily long:
for every $N$ there is an $m$ such that $\varrho(\ell_0 \cdots \ell_{m-1})$ has length at least
$N$. A word $w$ that is its own image $\varrho(w)$ is a fixed point of $\varrho$.

Without the length condition an erasing substitution, such as the one sending both letters to
the empty word, would make every infinite word an image of every other.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 1 (binary substitutions as homomorphisms of words) and Section 3 (images `ϱ(w)`).

Formalized by `MetaMathlibExt.IsSubstitutionImage`, a definition declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#is-substitution-image).

## Every word is fixed by the identity substitution

Every infinite binary word $w$ is
its own image under the identity substitution $a \mapsto a$, $b \mapsto b$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Section 1 (binary substitutions as homomorphisms of words).

Formalized by `MetaMathlibExt.isSubstitutionImage_id`, a theorem declared in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#is-substitution-image-id).

## Letter frequencies of a substitution image

Let $\mu$ be a substitution sending the
letters $a$ and $b$ to nonempty finite words, extended to words by concatenation, such that both
$a$ and $b$ occur in $\mu(a)\mu(b)$. For a word $x$ and a letter $\alpha$ write $\#_\alpha(x, m)$
for the number of letters $\alpha$ among the first $m$ letters of $x$; for a finite word $u$
write $|u|$ for its length and $|u|_\alpha$ for the number of letters $\alpha$ in it. Let $w$ be
an infinite binary word in which both letters occur infinitely often, let $v = \mu(w)$, suppose
that $\#_a(w, m)/m \to f$ for a real number $f$, and let $L = |\mu(a)|\,f + |\mu(b)|\,(1 - f)$.
Then

$$\frac{\#_a(v, m)}{m} \to \frac{|\mu(a)|_a\,f + |\mu(b)|_a\,(1 - f)}{L}, \qquad
\frac{\#_b(v, m)}{m} \to \frac{|\mu(a)|_b\,f + |\mu(b)|_b\,(1 - f)}{L}.$$

The paper allows erasing substitutions, but then the formula fails: for $\mu(a)$ empty,
$\mu(b) = ab$ and $w$ with $b$ exactly at the perfect squares, the frequency of $a$ in $w$ is $1$
and $\mu(w) = (ab)^\omega$ has frequency of $a$ equal to $1/2$, while $L = 0$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 35 (`jis-2025-25.1.5-thm-35`).

Stated but not proved: `MetaMathlibExt.frequency_substitution_image` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 542](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L542). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#frequency-substitution-image).

## Integer matrices with the golden eigenvector

Let $\tau = (1 + \sqrt 5)/2$ be the golden
ratio and $\tau' = (1 - \sqrt 5)/2$ its conjugate, and let $M$ be a $2 \times 2$ integer matrix.
Then $(\tau, 1)^T$ is a right eigenvector of $M$, that is, $M (\tau, 1)^T = c\,(\tau, 1)^T$ for
some real number $c$, if and only if

$$M = \begin{pmatrix} m + n & m \\ m & n \end{pmatrix}$$

for some integers $m$ and $n$. In that case the characteristic polynomial of $M$ is
$(X - (n + m\tau))(X - (n + m\tau'))$, so the eigenvalues of $M$ are $n + m\tau$ and
$n + m\tau'$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 39 (`jis-2025-25.1.5-lem-39`).

Stated but not proved: `MetaMathlibExt.golden_eigenvector_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#golden-eigenvector-iff).

## Integer matrices with a Pisa eigenvector

Let $j, m \ge 1$ be integers, let
$\tau_{j,m} = (j + \sqrt{j^2 + 4m})/2$, and let $M$ be a $2 \times 2$ integer matrix.
(a) If $j^2 + 4m$ is not a perfect square, then $(\tau_{j,m}, 1)^T$ is a right eigenvector of $M$
over $\mathbb{R}$ if and only if $M$ has rows $(t + sj, ms)$ and $(s, t)$ for some integers $s, t$.
(b) If $j^2 + 4m = r^2$ with $r$ a natural number, then $(\tau_{j,m}, 1)^T$ is a right
eigenvector of $M$ over $\mathbb{R}$ if and only if $M$ has rows $(s, t)$ and $(u, v)$ with
$u(j+r)^2 + 2(v-s)(j+r) - 4t = 0$.

In (b) $r$ is the nonnegative root, as the paper's proof uses $\tau_{j,m} = (j + r)/2$. For the
negative root the printed statement fails: for $j = 1$, $m = 2$, $r = -3$, the matrix $M$ with
rows $(0, 0)$ and $(1, 1)$ satisfies $u(j+r)^2 + 2(v-s)(j+r) - 4t = 4 - 4 - 0 = 0$, but
$\tau_{1,2} = 2$ and $M (2, 1)^T = (0, 3)^T$ is not a multiple of $(2, 1)^T$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 63 (`jis-2025-25.1.5-thm-63`).

Stated but not proved: `MetaMathlibExt.pisa_eigenvector_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#pisa-eigenvector-iff).

## Integer matrices with a metallic-mean eigenvector

Let $k \ge 1$ be an integer, let
$\tau_k = (k + \sqrt{k^2 + 4})/2$ and $\tau_k' = (k - \sqrt{k^2 + 4})/2$, and let $M$ be a
$2 \times 2$ integer matrix. Then $(\tau_k, 1)^T$ is a right eigenvector of $M$ over $\mathbb{R}$
if and only if $M$ has rows $(km + n, m)$ and $(m, n)$ for some integers $m, n$. For such $M$ the
characteristic polynomial of $M$ is $(X - (n + m\tau_k))(X - (n + m\tau_k'))$, so the eigenvalues
of $M$ are $n + m\tau_k$ and $n + m\tau_k'$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 66 (`jis-2025-25.1.5-lem-66`).

Stated but not proved: `MetaMathlibExt.metallic_eigenvector_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 599](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#metallic-eigenvector-iff).

## Position differences in the Fibonacci word

Let $f = \ell_0 \ell_1 \ell_2 \cdots =
abaab\cdots$ be the Fibonacci word, the infinite Fibonacci word with each $0$ written as $a$
and each $1$ as $b$. Let $p_a(n)$ and $p_b(n)$ be the positions (counted from $0$) of the
$n$-th $a$ and the $n$-th $b$ in $f$, and let $r(n) = p_b(n) - p_a(n)$. Then for every $n \ge 1$:
$p_a(n+1) - p_a(n)$ is $2$ if $\ell_{n-1} = a$ and $1$ if $\ell_{n-1} = b$;
$p_b(n+1) - p_b(n)$ is $3$ if $\ell_{n-1} = a$ and $2$ if $\ell_{n-1} = b$; and $r(n) = n$.

The printed statement gives the codings $(1, 2)$ and $(2, 3)$ instead, which are false:
$p_a$ takes the values $0, 2, 3, 5, \ldots$, so $p_a(2) - p_a(1) = 2$ while $f$ starts with
$a$. The codings above are the ones derived in the paper's proof.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 38 (`jis-2025-25.1.5-thm-38`).

Stated but not proved: `MetaMathlibExt.fibonacciWord_letterPosition_diff` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 618](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L618). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#fibonacci-word-letter-position-diff).

## Relative position of the deleted Fibonacci word

Let $f = abaababaabaab\cdots$ be the
Fibonacci word, the fixed point of $a \mapsto ab$, $b \mapsto a$. Let $D(f)$ be the word obtained
from $f$ by deleting its first $b$ and then the first $a$ of the result, and for an infinite
word $v$ over $\{a, b\}$ let $r_v(n) = p_b(n) - p_a(n)$, where $p_a(n)$ and $p_b(n)$ are the
positions of the $n$-th $a$ and the $n$-th $b$ in $v$. Then $r_{D(f)}(n) = n + 1$ for every
$n \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 43 (`jis-2025-25.1.5-thm-43`).

Stated but not proved: `MetaMathlibExt.relativePosition_deletion_fibonacciWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-deletion-fibonacci-wor).

## Relative position of iterated deletions of the Fibonacci word

Let
$f = abaababaabaab\cdots$ be the Fibonacci word, the fixed point of $a \mapsto ab$,
$b \mapsto a$. Let $D$ be the operator on infinite words over $\{a, b\}$ that deletes the first
$b$ and then the first $a$ of the result, and for such a word $v$ let
$r_v(n) = p_b(n) - p_a(n)$, where $p_a(n)$ and $p_b(n)$ are the positions of the $n$-th $a$ and
the $n$-th $b$ in $v$. Then for every natural number $k$ there is an $N$ such that
$r_{D^k(f)}(n) = n + k$ for all $n > N$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 44 (`jis-2025-25.1.5-thm-44`).

Stated but not proved: `MetaMathlibExt.relativePosition_deletion_iterate_fibonacciWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 639](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L639). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-deletion-iterate-fibon).

## The Fibonacci switch

Let $f = abaab\cdots$ be the Fibonacci word, the infinite
Fibonacci word with each $0$ written as $a$ and each $1$ as $b$, and let $\mu$ be the
substitution $a \mapsto aab$, $b \mapsto ab$. Then $D(f)$ is the image $\mu(f)$ of $f$ under
$\mu$, where $D$ deletes the first $b$ and the first $a$ of a word.

In the paper's description, $\mu(f)$ is the word obtained from $f$ by replacing each level-2
supertile $aba$ by $aab$ and keeping each $ab$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 45 (`jis-2025-25.1.5-thm-45`).

Stated but not proved: `MetaMathlibExt.fibonacci_switch` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#fibonacci-switch).

## Gap codings single out the Fibonacci word among words starting with $a$

Let
$w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite binary word over the letters $a$ and $b$ in which
both letters occur infinitely often and $\ell_0 = a$. For a letter $\alpha$ let $p_\alpha(n)$ be
the position (counting from $0$) of the $n$-th occurrence of $\alpha$ in $w$ and
$\Delta p_\alpha(n) = p_\alpha(n+1) - p_\alpha(n)$. Call $\Delta p_a$ and $\Delta p_b$ codings of
$w$ if there are maps $\sigma_a, \sigma_b$ from $\{a, b\}$ to the natural numbers with
$\Delta p_a(n) = \sigma_a(\ell_{n-1})$ and $\Delta p_b(n) = \sigma_b(\ell_{n-1})$ for all
$n \ge 1$, and injective codings if moreover $\sigma_a$ and $\sigma_b$ are injective. Let
$f = abaab\cdots$ be the infinite Fibonacci word written with $a$ for $0$ and $b$ for $1$. Then
$\Delta p_a$ and $\Delta p_b$ are codings of $w$ if and only if $w = f$ or $w = (ab)^\omega$, and
they are injective codings of $w$ if and only if $w = f$.

The second part drops the paper's word "aperiodic": for $(ab)^\omega$ the sequences $\Delta p_a$
and $\Delta p_b$ are constant, so they are not injective codings, and the characterization holds
for every such $w$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 46 (`jis-2025-25.1.5-thm-46`).

Stated but not proved: `MetaMathlibExt.letterPosition_diff_codings_iff_fibonacci` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-diff-codings-iff-fibonac).

## Gap codings single out the reflected Fibonacci word among words starting with $b$

Let
$w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite binary word over the letters $a$ and $b$ in which
both letters occur infinitely often and $\ell_0 = b$. For a letter $\alpha$ let $p_\alpha(n)$ be
the position (counting from $0$) of the $n$-th occurrence of $\alpha$ in $w$ and
$\Delta p_\alpha(n) = p_\alpha(n+1) - p_\alpha(n)$. Call $\Delta p_a$ and $\Delta p_b$ codings of
$w$ if there are maps $\sigma_a, \sigma_b$ from $\{a, b\}$ to the natural numbers with
$\Delta p_a(n) = \sigma_a(\ell_{n-1})$ and $\Delta p_b(n) = \sigma_b(\ell_{n-1})$ for all
$n \ge 1$, and injective codings if moreover $\sigma_a$ and $\sigma_b$ are injective. Let
$\bar f = babba\cdots$ be the infinite Fibonacci word written with $b$ for $0$ and $a$ for $1$
(the Fibonacci word $f = abaab\cdots$ with $a$ and $b$ exchanged). Then $\Delta p_a$ and
$\Delta p_b$ are codings of $w$ if and only if $w = \bar f$ or $w = (ba)^\omega$, and they are
injective codings of $w$ if and only if $w = \bar f$.

The second part drops the paper's word "aperiodic": for $(ba)^\omega$ the sequences $\Delta p_a$
and $\Delta p_b$ are constant, so they are not injective codings.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Corollary 48 (`jis-2025-25.1.5-cor-48`).

Stated but not proved: `MetaMathlibExt.letterPosition_diff_codings_iff_fibonacci_reflect` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 683](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L683). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-diff-codings-iff-fibonac-2).

## The Fibonacci word and its reflection are the words isomorphic to their gap sequences

Let $w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite binary word over the letters $a$ and $b$ in
which both letters occur infinitely often. For a letter $\alpha$ let $p_\alpha(n)$ be
the position (counting from $0$) of the $n$-th occurrence of $\alpha$ in $w$ and
$\Delta p_\alpha(n) = p_\alpha(n+1) - p_\alpha(n)$. Call $\Delta p_a$ and $\Delta p_b$ codings of
$w$ if there are maps $\sigma_a, \sigma_b$ from $\{a, b\}$ to the natural numbers with
$\Delta p_a(n) = \sigma_a(\ell_{n-1})$ and $\Delta p_b(n) = \sigma_b(\ell_{n-1})$ for all
$n \ge 1$, and injective codings if moreover $\sigma_a$ and $\sigma_b$ are injective. Let
$f = abaab\cdots$ be the infinite Fibonacci word written with $a$ for $0$ and $b$ for $1$, and
$\bar f$ the word $f$ with $a$ and $b$ exchanged. Then $\Delta p_a$ and $\Delta p_b$ are injective
codings of $w$ if and only if $w = f$ or $w = \bar f$.

The paper's word "aperiodic" is dropped, as in Theorem 46 and Corollary 48.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Corollary 49 (`jis-2025-25.1.5-cor-49`).

Stated but not proved: `MetaMathlibExt.letterPosition_diff_isomorphic_iff_fibonacci` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 703](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L703). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#letter-position-diff-isomorphic-iff-fibo).

## Fibonacci and iccanobiF iterates of a

Let $\varrho_F$ be the Fibonacci substitution
$a \mapsto ab$, $b \mapsto a$ and let $\varrho_F'$ be the iccanobiF substitution $a \mapsto ba$,
$b \mapsto a$, acting on finite words over the letters $a$ and $b$; thus $\varrho_F^m(a)$ is the
finite Fibonacci word $f_m$ with each $0$ written as $a$ and each $1$ as $b$. Then for every
$n \ge 1$, $ab\,\varrho_F^{2n}(a) = (\varrho_F')^{2n}(a)\,ba$ and
$ba\,\varrho_F^{2n-1}(a) = (\varrho_F')^{2n-1}(a)\,ab$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Proposition 51 (`jis-2025-25.1.5-prop-51`).

Stated but not proved: `MetaMathlibExt.fibonacci_iccanobiF_conjugate_a` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 717](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L717). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#fibonacci-iccanobi-f-conjugate-a).

## Conjugacy of the Fibonacci and iccanobiF iterates of $b$

Let $\varrho_F'$ be the
iccanobiF substitution $a \mapsto ba$, $b \mapsto a$, extended to finite words by concatenation,
and for each $k$ let $g_k$ be the finite Fibonacci word $f_k$ with each $0$ written as $a$ and
each $1$ as $b$. For every $n \ge 1$,

$$ab\,g_{2n} = (\varrho_F')^{2n+1}(b)\,ba, \qquad ba\,g_{2n-1} = (\varrho_F')^{2n}(b)\,ab.$$

Since $g_k = \varrho_F^k(a) = \varrho_F^{k+1}(b)$ for the Fibonacci substitution $\varrho_F$
($a \mapsto ab$, $b \mapsto a$), this says $ab\,\varrho_F^{2n+1}(b) = (\varrho_F')^{2n+1}(b)\,ba$
and $ba\,\varrho_F^{2n}(b) = (\varrho_F')^{2n}(b)\,ab$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Proposition 52 (`jis-2025-25.1.5-prop-52`).

Stated but not proved: `MetaMathlibExt.fibonacci_iccanobiF_conjugate_b` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 732](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L732). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#fibonacci-iccanobi-f-conjugate-b).

## The iccanobiF iterates approximate $abf$ and $baf$

Let $f = abaab\cdots$ be the
Fibonacci word, the infinite Fibonacci word with each $0$ written as $a$ and each $1$ as $b$,
and let $\varrho_F'$ be the iccanobiF substitution $a \mapsto ba$, $b \mapsto a$, extended to
finite words by concatenation. For every $n \ge 0$, the word $(\varrho_F')^{2n}(a)$ is a prefix
of the infinite word $abf$ and $(\varrho_F')^{2n}(b)$ is a prefix of $baf$, and for every $N$
there is an $n$ such that $(\varrho_F')^{2n}(a)$ and $(\varrho_F')^{2n}(b)$ both have length at
least $N$. Moreover, the relative position functions of $abf$ and $baf$ satisfy
$r_{abf}(1) = 1$, $r_{baf}(1) = -1$ and $r_{abf}(n) = r_{baf}(n) = n - 1$ for every $n \ge 2$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 53 (`jis-2025-25.1.5-thm-53`).

Stated but not proved: `MetaMathlibExt.iccanobiF_fixed_points` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 748](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L748). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#iccanobi-f-fixed-points).

## Relative positions of the Fibonacci word with an equilibrious word prepended

Let
$f = abaab\cdots$ be the infinite Fibonacci word with $0$ read as $a$ and $1$ as $b$, let $j \ge 0$,
let $u$ be a finite word over $\{a, b\}$ of length $2j$ in which $a$ and $b$ occur equally often
(an equilibrious word), and let $r$ be the relative position function of the concatenation $uf$.
Then $r(n) = n - j$ for all $n > j$. If moreover $u = (ab)^j$, then $r(n) = 1$ for all
$1 \le n \le j$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 55 (`jis-2025-25.1.5-thm-55`).

Stated but not proved: `MetaMathlibExt.relativePosition_prepend_equilibrious_fibonacci` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 766](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L766). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-prepend-equilibrious-f).

## Position identities for the extended Pisa substitution

Let $k \ge 1$, $l \ge 0$ and
$m \ge 1$ be natural numbers, let $\sigma$ be the substitution $a \mapsto a^k b a^l$,
$b \mapsto a^m$, and let $w$ be a one-sided fixed point of $\sigma$ (so $\sigma(w) = w$) that
begins with $a$. For an infinite word $v$ over $\{a, b\}$ and $n \ge 1$, let $p_a(n)$ and
$p_b(n)$ be the positions (counted from $0$) of the $n$-th $a$ and the $n$-th $b$ in $v$, and let
$r(n) = p_b(n) - p_a(n)$. Then for $v = w$ and every $n \ge 1$,

$$p_b(n) = m\,p_a(n) + (k + l + 1 - m)n + m - l - 1$$

and

$$r(n) = (m - 1)p_a(n) + (k + l + 1 - m)n + m - l - 1.$$

Moreover, every infinite word $v$ over $\{a, b\}$ in which both letters occur infinitely often
and whose functions $r$ and $p_a$ satisfy the second identity for all $n \ge 1$ equals $w$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 57 (`jis-2025-25.1.5-thm-57`).

Stated but not proved: `MetaMathlibExt.pisa_letterPosition_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 781](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L781). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#pisa-letter-position-identity).

## Relative position of the extended Pisa fixed point via the positions of $b$

Let
$k \ge 1$, $l \ge 0$ and $m \ge 1$ be natural numbers, let $\sigma$ be the substitution
$a \mapsto a^k b a^l$, $b \mapsto a^m$, and let $w$ be a one-sided fixed point of $\sigma$ (so
$\sigma(w) = w$) that begins with $a$. Let $p_a(n)$ and $p_b(n)$ be the positions (counted from
$0$) of the $n$-th $a$ and the $n$-th $b$ in $w$, and let $r(n) = p_b(n) - p_a(n)$. Then for
every $n \ge 1$,

$$r(n) = \frac{m - 1}{m}\,p_b(n) + \frac{k + l + 1 - m}{m}\,n + \frac{m - l - 1}{m}.$$

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Corollary 58 (`jis-2025-25.1.5-cor-58`).

Stated but not proved: `MetaMathlibExt.pisa_relativePosition_of_letterPosition_b` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 800](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#pisa-relative-position-of-letter-positio).

## Letter frequencies and mean positions of primitive fixed points

Let $\varrho$ be a
substitution on the letters $a, b$ with substitution matrix $M$, where $M_{11} = |\varrho(a)|_a$,
$M_{12} = |\varrho(b)|_a$, $M_{21} = |\varrho(a)|_b$ and $M_{22} = |\varrho(b)|_b$ ($|v|_x$ is
the number of letters $x$ in $v$). Suppose $\varrho$ is primitive (some power of $M$ has all
entries positive), and let $u > 0$ and $\lambda$ be real numbers with
$M (u, 1)^T = \lambda (u, 1)^T$. Let $w$ be a one-sided fixed point of $\varrho$ (so
$\varrho(w) = w$) in which both letters occur infinitely often. Let $N_a(n)$ and $N_b(n)$ be the
numbers of letters $a$ and $b$ among the first $n$ letters of $w$, let $p_a(n)$ and $p_b(n)$ be
the positions of the $n$-th $a$ and the $n$-th $b$ in $w$, and let $r(n) = p_b(n) - p_a(n)$.
Then, as $n \to \infty$, $N_a(n)/n \to u/(u + 1)$, $N_b(n)/n \to 1/(u + 1)$,
$p_a(n)/n \to 1 + 1/u$, $p_b(n)/n \to u + 1$ and $r(n)/n \to u - 1/u$, and each of these five
limits lies in the subfield $\mathbb{Q}(\lambda)$ of $\mathbb{R}$.

A positive eigenvector of a primitive matrix belongs to its Perron–Frobenius eigenvalue, so
$(u, 1)^T$ is a right Perron–Frobenius eigenvector of $M$ and $\lambda$ is its eigenvalue.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 32 (`jis-2025-25.1.5-lem-32`).

Stated but not proved: `MetaMathlibExt.primitive_fixed_point_mean_values` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 819](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L819). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#primitive-fixed-point-mean-values).

## Relative position asymptotic to $n$ and the golden ratio

Let $\varrho$ be a substitution
on the letters $a, b$ with substitution matrix $M$, where $M_{11} = |\varrho(a)|_a$,
$M_{12} = |\varrho(b)|_a$, $M_{21} = |\varrho(a)|_b$ and $M_{22} = |\varrho(b)|_b$ ($|v|_x$ is
the number of letters $x$ in $v$), and suppose $\varrho$ is primitive (some power of $M$ has all
entries positive). Let $w$ be a one-sided fixed point of $\varrho$ (so $\varrho(w) = w$) in which
both letters occur infinitely often, let $p_a(n)$ and $p_b(n)$ be the positions of the $n$-th $a$
and the $n$-th $b$ in $w$, and let $r(n) = p_b(n) - p_a(n)$. Then $r(n)/n \to 1$ as
$n \to \infty$ if and only if $(\varphi, 1)^T$ is an eigenvector of $M$, where
$\varphi = (1 + \sqrt 5)/2$ is the golden ratio.

Since $(\varphi, 1)^T$ is positive, this is the same as being a right Perron–Frobenius
eigenvector of $M$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Lemma 41 (`jis-2025-25.1.5-lem-41`).

Stated but not proved: `MetaMathlibExt.primitive_relativePosition_div_tendsto_one_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 844](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L844). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#primitive-relative-position-div-tendsto).

## Frequency and position criteria for an eigenvector of a primitive substitution

Let
$j \ge 1$ and $m \ge 1$ be natural numbers with $m \ne j + 1$, and let
$\tau = (j + \sqrt{j^2 + 4m})/2$. Let
$\varrho$ be a substitution on the letters $a, b$ with substitution matrix $M$, where
$M_{11} = |\varrho(a)|_a$, $M_{12} = |\varrho(b)|_a$, $M_{21} = |\varrho(a)|_b$ and
$M_{22} = |\varrho(b)|_b$ ($|v|_x$ is the number of letters $x$ in $v$). Suppose $\varrho$ is
primitive (some power of $M$ has all entries positive), and let $w$ be a one-sided fixed point
of $\varrho$ (so $\varrho(w) = w$). Let $N_a(n)$ and $N_b(n)$ be the numbers of letters $a$ and
$b$ among the first $n$ letters of $w$, let $p_a(n)$ and $p_b(n)$ be the positions (counted from
$0$) of the $n$-th $a$ and the $n$-th $b$ in $w$, and let $r(n) = p_b(n) - p_a(n)$. Then the
following are equivalent, all limits taken as $n \to \infty$:
(i) $N_a(n)/n \to (\tau - m)/(j + 1 - m)$;
(ii) $N_b(n)/n \to (j + 1 - \tau)/(j + 1 - m)$;
(iii) $p_a(n)/n \to 1 + (\tau - j)/m$;
(iv) $p_b(n)/n \to \tau + 1$;
(v) $r(n)/n \to ((m - 1)\tau + j)/m$;
(vi) $p_a(n)/n$ converges to some real number $q$ and $r(n)/n \to (m - 1)q + j + 1 - m$;
(vii) $(\tau, 1)^T$ is an eigenvector of $M$.

The hypothesis $m \ne j + 1$ is added to the paper's statement: for $m = j + 1$ one has
$\tau = j + 1 = m$, so (i) and (ii) read $0/0$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Proposition 62 (`jis-2025-25.1.5-prop-62`).

Stated but not proved: `MetaMathlibExt.pisa_frequency_tfae` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 865](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L865). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#pisa-frequency-tfae).

## Words with linear relative position function

For integers $k, l, m \ge 0$ write
$\sigma_{k,l,m}$ for the substitution $a \mapsto a^k b a^l$, $b \mapsto a^m$, and for a binary
word $v$ let $r_v(n) = p_{b,v}(n) - p_{a,v}(n)$, where $p_{\alpha,v}(n)$ is the position (counted
from $0$) of the $n$-th occurrence of the letter $\alpha$ in $v$.
(a) For every $j \ge 1$, the word $v = (a^j b^j)^\omega$ has $r_v(n) = j$ for all $n \ge 1$.
(b) For integers $0 \le j < k$, every fixed point $w$ of $\sigma_{k-j,j,1}$ that starts with $a$
has $r_w(n) = kn - j$ for all $n \ge 1$.
(c) For every $k \ge 1$, if $w$ is a fixed point of $\sigma_{1,k-1,1}$ that starts with $a$ and
$D(w)$ is the word $w$ with its first $a$ and its first $b$ deleted, then $r_{D(w)}(n) = kn + 1$
for all $n \ge 1$.

The paper writes $k \ge 0$ in (c), but $\sigma_{1,k-1,1}$ needs $k \ge 1$.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 64 (`jis-2025-25.1.5-thm-64`).

Stated but not proved: `MetaMathlibExt.linear_relativePosition_examples` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 890](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L890). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#linear-relative-position-examples).

## Eventually linear relative position functions with positive slope

Let $k \ge 1$, $q$
and $c$ be integers with $0 \le c \le k - 1$, and put $j = qk - c$. Let $w$ be an infinite word
over $\{a, b\}$ that starts with $a$ and is a fixed point of the Pisa substitution
$\sigma_{k-c,c,1}$, given by $a \mapsto a^{k-c} b a^c$ and $b \mapsto a$. For an infinite word $v$
write $r_v$ for its relative position function, and let $D$ be the deletion operator, which
deletes the first $b$ and then the first $a$ of a word. (a) If $q \ge 0$, then
$r_{D^q(w)}(n) = kn + j$ for all sufficiently large $n$. (b) If $q < 0$, then for every finite
word $u$ over $\{a, b\}$ of length $-2q$ in which $a$ and $b$ occur equally often (an
equilibrious word), $r_{uw}(n) = kn + j$ for all sufficiently large $n$.

The paper takes $w$ to be the fixed point of $\sigma_{1,k-1,1}$ for every $c$, which is false
unless $c = k - 1$: for $k = 2$ and $j = 2$ ($q = 1$, $c = 0$) that fixed point has
$r_{D(w)}(n) = 2n + 1$ (Theorem 64(c)), not $2n + 2$. The substitution $\sigma_{k-c,c,1}$ is the
one Theorem 64(b) provides ($r_w(n) = kn - c$), from which $D$ (with $r_{D(w)}(n) = r_w(n+1)$
for words that start with $ab$ or $ba$ and contain both letters infinitely often) and
equilibrious prefixes (Lemma 22) shift the index by $q$, giving every progression $kn + j$ with
$k \ge 1$; for $c = k - 1$ it is the paper's $\sigma_{1,k-1,1}$. The paper writes $k \ge 0$, but
the range $0 \le c \le k - 1$ is then empty.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Proposition 65 (`jis-2025-25.1.5-prop-65`).

Stated but not proved: `MetaMathlibExt.relativePosition_eventually_eq_linear` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 920](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L920). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-eventually-eq-linear).

## Primitive substitutions with asymptotically linear relative position

Let $\varrho$ be a
substitution on the letters $a, b$ with substitution matrix $M$, where $M_{11} = |\varrho(a)|_a$,
$M_{12} = |\varrho(b)|_a$, $M_{21} = |\varrho(a)|_b$ and $M_{22} = |\varrho(b)|_b$ ($|v|_x$ is
the number of letters $x$ in $v$). Suppose $\varrho$ is primitive (some power of $M$ has all
entries positive), and let $w$ be a one-sided fixed point of $\varrho$ (so $\varrho(w) = w$) in
which both letters occur infinitely often. Let $p_a(n)$ and $p_b(n)$ be the positions of the
$n$-th $a$ and the $n$-th $b$ in $w$, let $r(n) = p_b(n) - p_a(n)$, let $k \ge 1$ be a natural
number and let $\tau = (k + \sqrt{k^2 + 4})/2$. With all limits taken as $n \to \infty$:
(a) the following are equivalent: $r(n)/n \to k$; $(\tau, 1)^T$ is an eigenvector of $M$;
$M$ has rows $(km + t, m)$ and $(m, t)$ for some natural numbers $m \ge 1$ and $t \ge 0$.
(b) the following are equivalent: $r(n)/n \to -k$; $(1, \tau)^T$ is an eigenvector of $M$;
$M$ has rows $(t, m)$ and $(m, km + t)$ for some natural numbers $m \ge 1$ and $t \ge 0$.
(c) the following are equivalent: $r(n)/n \to 0$; $(1, 1)^T$ is an eigenvector of $M$;
$M_{11} + M_{12} = M_{21} + M_{22}$.

These vectors are positive, so being an eigenvector of the primitive matrix $M$ is the same as
being its right Perron–Frobenius eigenvector.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 67 (`jis-2025-25.1.5-thm-67`).

Stated but not proved: `MetaMathlibExt.primitive_asymptotically_linear_classification` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 942](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L942). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#primitive-asymptotically-linear-classifi).

## Relative positions of a word made of $ab$ and $ba$ blocks

Let
$w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite word over $\{a, b\}$ such that every block
$\ell_{2i} \ell_{2i+1}$ ($i \ge 0$) is $ab$ or $ba$, and let $r$ be its relative position
function. Then for every $n \ge 1$, $r(n) = 1$ if $\ell_{2n-2} = a$ and $r(n) = -1$ if
$\ell_{2n-2} = b$.

The block condition forces both letters to occur infinitely often, so no separate hypothesis on
$w$ is needed.

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Proposition 69 (`jis-2025-25.1.5-prop-69`).

Stated but not proved: `MetaMathlibExt.relativePosition_of_dimers` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 980](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L980). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-of-dimers).

## Characterization of the Thue–Morse word by its relative positions

Let
$w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite word over $\{a, b\}$ that starts with $a$ and in
which both letters occur infinitely often, and let $r$ be its relative position function. Then
$r(n) = 1$ when $\ell_{n-1} = a$ and $r(n) = -1$ when $\ell_{n-1} = b$, for all $n \ge 1$, if and
only if $w$ is the Thue–Morse word $t = abbabaab\cdots$ (the Thue–Morse sequence with $0$ read as
$a$ and $1$ as $b$).

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 70 (`jis-2025-25.1.5-thm-70`).

Stated but not proved: `MetaMathlibExt.relativePosition_self_coding_iff_thueMorse` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 990](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L990). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-self-coding-iff-thue-m).

## Characterization of the Thue–Morse word among words starting with $abba$

Let
$w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite word over $\{a, b\}$ that begins with $abba$ and in
which both letters occur infinitely often, and let $r$ be its relative position function. Then
there is an injective map $\sigma \colon \{a, b\} \to \mathbb{Z}$ with $r(n) = \sigma(\ell_{n-1})$
for all $n \ge 1$ if and only if $w$ is the Thue–Morse word $t = abbabaab\cdots$ (the Thue–Morse
sequence with $0$ read as $a$ and $1$ as $b$).

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Corollary 71 (`jis-2025-25.1.5-cor-71`).

Stated but not proved: `MetaMathlibExt.relativePosition_isomorphic_iff_thueMorse` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 1000](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L1000). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-isomorphic-iff-thue-mo).

## Characterization of the cloned Thue–Morse words by their relative positions

Let $k > 1$
be an integer, let $w = \ell_0 \ell_1 \ell_2 \cdots$ be an infinite word over $\{a, b\}$ that starts
with $a$ and in which both letters occur infinitely often, and let $r$ be its relative position
function. Then $r(n) = k$ when $\ell_{n-1} = a$ and $r(n) = -k$ when $\ell_{n-1} = b$, for all
$n \ge 1$, if and only if $w = \varphi_k(t)$, the word whose letter at position $i$ is
$t_{\lfloor i/k \rfloor}$, where $t = abbabaab\cdots$ is the Thue–Morse word (the Thue–Morse
sequence with $0$ read as $a$ and $1$ as $b$).

## Sources

- Michael Coons, Christopher Ramsey and Nicolae Strungaru, *Relative Position in Binary Substitutions*, Journal of Integer Sequences 28 (2025), Article 25.1.5, Theorem 72 (`jis-2025-25.1.5-thm-72`).

Stated but not proved: `MetaMathlibExt.relativePosition_self_coding_iff_clone_thueMorse` is written with `theorem_wanted` in [WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean, line 1012](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RelativePositionBinaryWordsWanted.lean#L1012). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html#relative-position-self-coding-iff-clone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Relative position in binary words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/relative-position-in-binary-words)
