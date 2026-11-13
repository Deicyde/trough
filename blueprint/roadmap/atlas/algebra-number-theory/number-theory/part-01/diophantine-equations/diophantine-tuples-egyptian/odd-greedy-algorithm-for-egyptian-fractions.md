---
declaration: section
origin: cited
lean: MetaMathlibExt.IsOddGreedyChoice, MetaMathlibExt.IsOddGreedyChoice.pos_r, MetaMathlibExt.IsOddGreedyChoice.pos_d, MetaMathlibExt.IsOddGreedyChoice.odd, MetaMathlibExt.IsOddGreedyChoice.inv_le, MetaMathlibExt.IsOddGreedyChoice.min, MetaMathlibExt.IsOddGreedyChoice.unique, MetaMathlibExt.isOddGreedyChoice_iff
statement: formalized
---

# Odd greedy algorithm for Egyptian fractions

10 results, 8 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html).

## Odd greedy choice

For a rational number $r$ and a natural number $d$, $d$ is the odd
greedy choice at $r$ when $r > 0$, $d$ is positive and odd, $1/d \le r$, and $d \le e$ for every
positive odd natural number $e$ with $1/e \le r$. Equivalently, $1/d$ is the largest unit
fraction with odd denominator that does not exceed $r$.

Formalized by `MetaMathlibExt.IsOddGreedyChoice`, a definition declared in [MathlibExt/NumberTheory/OddGreedyChoice.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/OddGreedyChoice.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#is-odd-greedy-choice).

## The odd greedy choice needs a positive remainder

If $d$ is the odd greedy choice at a
rational number $r$, then $r > 0$.

Formalized by `MetaMathlibExt.IsOddGreedyChoice.pos_r`, a theorem declared in [MathlibExt/NumberTheory/OddGreedyChoice.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/OddGreedyChoice.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#pos-r).

## The odd greedy choice is positive

If $d$ is the odd greedy choice at a rational number
$r$, then $d > 0$.

Formalized by `MetaMathlibExt.IsOddGreedyChoice.pos_d`, a theorem declared in [MathlibExt/NumberTheory/OddGreedyChoice.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/OddGreedyChoice.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#pos-d).

## The odd greedy choice is odd

If $d$ is the odd greedy choice at a rational number $r$,
then $d$ is odd.

Formalized by `MetaMathlibExt.IsOddGreedyChoice.odd`, a theorem declared in [MathlibExt/NumberTheory/OddGreedyChoice.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/OddGreedyChoice.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#odd).

## The odd greedy unit fraction does not exceed the remainder

If $d$ is the odd greedy
choice at a rational number $r$, then $1/d \le r$.

Formalized by `MetaMathlibExt.IsOddGreedyChoice.inv_le`, a theorem declared in [MathlibExt/NumberTheory/OddGreedyChoice.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/OddGreedyChoice.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#inv-le).

## The odd greedy choice is minimal

If $d$ is the odd greedy choice at a rational number
$r$, then $d \le e$ for every positive odd natural number $e$ with $1/e \le r$.

Formalized by `MetaMathlibExt.IsOddGreedyChoice.min`, a theorem declared in [MathlibExt/NumberTheory/OddGreedyChoice.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/OddGreedyChoice.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#min).

## Uniqueness of the odd greedy choice

If $d$ and $d'$ are both odd greedy choices at the
same rational number $r$, then $d = d'$.

Formalized by `MetaMathlibExt.IsOddGreedyChoice.unique`, a theorem declared in [MathlibExt/NumberTheory/OddGreedyChoice.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/OddGreedyChoice.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#unique).

## Characterization of the odd greedy choice

A natural number $d$ is the odd greedy choice
at a rational number $r$ if and only if $r > 0$ and $d$ is the least element of the set of
positive odd natural numbers $e$ with $1/e \le r$.

Formalized by `MetaMathlibExt.isOddGreedyChoice_iff`, a theorem declared in [MathlibExt/NumberTheory/OddGreedyChoice.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/OddGreedyChoice.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#is-odd-greedy-choice-iff).

## Even sums of odd unit fractions have even numerator

Let $m$ be an even natural number
and let $d_1, \dots, d_m$ be odd natural numbers. If integers $a$ and $b$ with $b \ne 0$ satisfy
$a/b = \sum_{i=1}^{m} 1/d_i$, then $a$ is even.

## Sources

- Joel Louwsma and Joseph Martino, "Rational Numbers with Two-Term Odd Greedy Expansion", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.OddGreedyExpansionWanted.even_num_of_even_sum_unit_fractions` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddGreedyExpansionWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddGreedyExpansionWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#even-num-of-even-sum-unit-fractions).

## Odd greedy choice at a fraction

Let $n$ and $d$ be positive natural numbers and let $x_1$
be an odd natural number. Then $x_1$ is the odd greedy choice at $n/d$ (the first denominator of
the odd greedy expansion of $n/d$) if and only if $d \le n x_1$ and $n x_1 < d + 2n$, that is,
$0 \le n x_1 - d < 2n$ in the integers.

## Sources

- Joel Louwsma and Joseph Martino, "Rational Numbers with Two-Term Odd Greedy Expansion", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.OddGreedyExpansionWanted.isOddGreedyChoice_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddGreedyExpansionWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OddGreedyExpansionWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html#is-odd-greedy-choice-iff-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Odd greedy algorithm for Egyptian fractions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/odd-greedy-algorithm-for-egyptian-fractions)
