---
declaration: section
origin: cited
lean: MetaMathlibExt.positionalColoredCompositionCount, MetaMathlibExt.positionalColoredCompositionCount_zero, MetaMathlibExt.colorTwoRestrictedCompositions_eq_even, MetaMathlibExt.odd_eq_choose_two_colorCompositions, MetaMathlibExt.odd_eq_ternaryStrings_avoiding, MetaMathlibExt.even_eq_ternaryStrings_avoiding, MetaMathlibExt.even_succ_eq_sum_runLength_prod, MetaMathlibExt.odd_eq_sum_runLength_prod
statement: formalized
---

# Positional colored compositions

10 results, 2 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html).

## Positional colored compositions

For natural numbers $m$, $k$ and $\ell$, $c_{m,k}(\ell)$
is the number of $(m, k)$-colored compositions of $\ell$: compositions of $\ell$ in which every
part whose position, counted from $1$, is congruent to $k$ modulo $m$ gets one of $p$ colors,
where $p$ is the part, and the other parts are uncolored. Equivalently, $c_{m,k}(\ell)$ is the
sum, over all compositions $(p_1, \dots, p_r)$ of $\ell$, of the product of the parts $p_i$ with
$i \equiv k \pmod m$.

The paper takes $m \ge 1$. For $m = 0$, congruence modulo $0$ is equality, so only the part at
position exactly $k$ is colored.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Definition 1.

Formalized by `MetaMathlibExt.positionalColoredCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#positional-colored-composition-count).

## Colored compositions of zero

For all natural numbers $m$ and $k$, $c_{m,k}(0) = 1$: the
only composition of $0$ is the empty one.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Definition 1.

Formalized by `MetaMathlibExt.positionalColoredCompositionCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#positional-colored-composition-count-zer).

## Avoiding color 2 counts even colored compositions

For every $k \ge 0$, the number of
$n$-color compositions of $k$ that do not use the color $2$ equals the number
$e(k) = c_{2,0}(k)$ of even colored compositions of $k$, in which only the parts at even
positions are colored. In such an $n$-color composition a part $p \ge 2$ has the $p - 1$ colors
other than $2$ and a part $1$ has its single color, so their number is the sum, over all
compositions $(p_1, \dots, p_r)$ of $k$, of $\prod_i q(p_i)$, where $q(1) = 1$ and
$q(p) = p - 1$ for $p \ge 2$.

The paper states this for positive $k$; at $k = 0$ both sides equal $1$.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Theorem 1.

Stated but not proved: `MetaMathlibExt.colorTwoRestrictedCompositions_eq_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#color-two-restricted-compositions-eq-eve).

## Odd colored compositions and binomial-color compositions

For every $k \ge 1$, the number
$o(k) = c_{2,1}(k)$ of odd colored compositions of $k$, in which only the parts at odd positions
are colored, equals the sum, over all compositions $(p_1, \dots, p_r)$ of $k + 1$, of
$\prod_i \binom{p_i}{2}$; that is, the number of compositions of $k + 1$ in which a part $p$ has
$\binom{p}{2}$ colors.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Theorem 2.

Stated but not proved: `MetaMathlibExt.odd_eq_choose_two_colorCompositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#odd-eq-choose-two-color-compositions).

## Odd colored compositions and ternary strings

For every $k \ge 1$, the number
$o(k) = c_{2,1}(k)$ of odd colored compositions of $k$, in which only the parts at odd positions
are colored, equals the number of strings of length $k - 1$ over the alphabet $\{0, 1, 2\}$ that
contain neither $01$ nor $12$ as two consecutive letters.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Corollary 1.

Stated but not proved: `MetaMathlibExt.odd_eq_ternaryStrings_avoiding` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#odd-eq-ternary-strings-avoiding).

## Even colored compositions and ternary strings

For every $k \ge 0$, the number
$e(k) = c_{2,0}(k)$ of even colored compositions of $k$, in which only the parts at even
positions are colored, equals the number of strings of length $k$ over the alphabet
$\{0, 1, 2\}$ that contain neither $01$ nor $12$ as two consecutive letters, do not begin with
$2$ and do not end with $0$.

At $k = 0$ both sides equal $1$, the empty string being counted.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Theorem 3.

Stated but not proved: `MetaMathlibExt.even_eq_ternaryStrings_avoiding` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#even-eq-ternary-strings-avoiding).

## Even colored compositions and runs in binary strings

For every $k \ge 0$, the number
$e(k + 1) = c_{2,0}(k + 1)$ of even colored compositions of $k + 1$, in which only the parts at
even positions are colored, equals the sum, over all binary strings of length $k$, of the
product of the lengths of the maximal runs of $1$s in the string; a string without a $1$
contributes the empty product $1$.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Theorem 4.

Stated but not proved: `MetaMathlibExt.even_succ_eq_sum_runLength_prod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#even-succ-eq-sum-run-length-prod).

## Odd colored compositions and runs in binary strings

For every $k \ge 1$, the number
$o(k) = c_{2,1}(k)$ of odd colored compositions of $k$, in which only the parts at odd positions
are colored, equals the sum, over the binary strings of length $k$ whose first letter is $1$, of
the product of the lengths of the maximal runs of $1$s in the string.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Theorem 5.

Stated but not proved: `MetaMathlibExt.odd_eq_sum_runLength_prod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#odd-eq-sum-run-length-prod).

## A recurrence for positional colored compositions

For natural numbers $m$, $k$ and $\ell$
with $m \ge 1$, $m \nmid k$ and $\ell \ge 1$,
$c_{m,k+1}(\ell + 1) = c_{m,k+1}(\ell) + c_{m,k}(\ell)$.

The paper prints the hypotheses $k \ge 1$, $\ell \ge 2$ and $1 \le m \le \ell - 1$, which allow
$m \mid k$; there the identity fails: for $m = 1$, $k = 1$ and $\ell = 2$ one has
$c_{1,2}(3) = 8$ but $c_{1,2}(2) + c_{1,1}(2) = 6$. The paper's argument (remove a first part
$1$ or decrease the first part) needs the first part to be uncolored, which is the condition
$m \nmid k$.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Theorem 6.

Stated but not proved: `MetaMathlibExt.positionalColoredCompositionCount_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#positional-colored-composition-count-suc).

## Even colored compositions and 321-avoiding separable permutations

For every $k \ge 0$,
the number $e(k) = c_{2,0}(k)$ of even colored compositions of $k$, in which only the parts at
even positions are colored, equals the number of permutations of $\{1, \dots, k\}$ that avoid
the patterns $321$, $2413$ and $3142$, that is, the number of $321$-avoiding separable
permutations of $\{1, \dots, k\}$.

At $k = 0$ both sides equal $1$.

## Sources

- Andrew Li and Hua Wang, *Combinatorics of Positional Colored Compositions*, INTEGERS 26 (2026), Article A49, Theorem 7.

Stated but not proved: `MetaMathlibExt.even_eq_card_separable_321_avoiding` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PositionalColoredCompositionsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html#even-eq-card-separable-321-avoiding).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Positional colored compositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/positional-colored-compositions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-compositions/positional-colored-compositions)
