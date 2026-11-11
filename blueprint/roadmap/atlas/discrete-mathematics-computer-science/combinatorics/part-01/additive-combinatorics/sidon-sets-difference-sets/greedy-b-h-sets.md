---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.GreedyBhFourthWanted.IsNextGreedyBh, MathlibExt.Combinatorics.GreedyBhFourthWanted.IsFourthGreedyBh, MathlibExt.Combinatorics.GreedyBhFourthWanted.fourthValue, MathlibExt.Combinatorics.GreedyBhFourthWanted.isFourthGreedyBh_fourthValue, MathlibExt.Combinatorics.GreedyBhFourthWanted.fourthValue_le_of_isFourthGreedyBh, MathlibExt.Combinatorics.GreedyBhFourthWanted.isFourthGreedyBh_le_fourthValue
statement: formalized
---

# Greedy B_h-sets

6 results, 3 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/greedy-b-h-sets/index.html).

## Next term of a greedy $B_h$-set

Let $h$ and $a$ be natural numbers and $A$ a set of natural
numbers. Then $a$ is the next greedy $B_h$ choice after $A$ if $a$ is greater than every element
of $A$, the set $A \cup \{a\}$ is a $B_h$-set, and for every natural number $b < a$ that is
greater than every element of $A$, the set $A \cup \{b\}$ is not a $B_h$-set.

Formalized by `MathlibExt.Combinatorics.GreedyBhFourthWanted.IsNextGreedyBh`, a definition declared in [WantedExt/Combinatorics/GreedyBhFourthWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreedyBhFourthWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/greedy-b-h-sets/index.html#is-next-greedy-bh).

## Fourth positive term of the greedy $B_h$-set

For natural numbers $h$ and $a$, we say that
$a$ is the fourth positive element $a_4(h)$ of the greedy $B_h$-set if $1$ is the next greedy
$B_h$ choice after $\{0\}$, $h + 1$ is the next greedy $B_h$ choice after $\{0, 1\}$,
$h^2 + h + 1$ is the next greedy $B_h$ choice after $\{0, 1, h + 1\}$, and $a$ is the next
greedy $B_h$ choice after $\{0, 1, h + 1, h^2 + h + 1\}$.

Formalized by `MathlibExt.Combinatorics.GreedyBhFourthWanted.IsFourthGreedyBh`, a definition declared in [WantedExt/Combinatorics/GreedyBhFourthWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreedyBhFourthWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/greedy-b-h-sets/index.html#is-fourth-greedy-bh).

## Quasipolynomial for the fourth greedy $B_h$ term

For a natural number $h$, the value
$v(h)$ is $(h^3 + 3h^2 + 3h + 1)/2$ if $h$ is odd and $(h^3 + 2h^2 + 3h + 2)/2$ if $h$ is even.

Both numerators are even, so the divisions are exact.

Formalized by `MathlibExt.Combinatorics.GreedyBhFourthWanted.fourthValue`, a definition declared in [WantedExt/Combinatorics/GreedyBhFourthWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreedyBhFourthWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/greedy-b-h-sets/index.html#fourth-value).

## Formula for the fourth greedy $B_h$ term

For every integer $h \ge 1$, the fourth positive
element $a_4(h)$ of the greedy $B_h$-set is $(h^3 + 3h^2 + 3h + 1)/2$ if $h$ is odd and
$(h^3 + 2h^2 + 3h + 2)/2$ if $h$ is even.

## Sources

- Melvyn B. Nathanson and Kevin O'Bryant, "The Fourth Positive Element in the Greedy `B_h`-Set", Theorem 1.

Stated but not proved: `MathlibExt.Combinatorics.GreedyBhFourthWanted.isFourthGreedyBh_fourthValue` is written with `theorem_wanted` in [WantedExt/Combinatorics/GreedyBhFourthWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreedyBhFourthWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/greedy-b-h-sets/index.html#is-fourth-greedy-bh-fourth-value).

## Lower bound for the fourth greedy $B_h$ term

Let $h$ and $a$ be natural numbers with
$h \ge 2$. If $a$ is the fourth positive element $a_4(h)$ of the greedy $B_h$-set, then
$a \ge v(h)$, where $v(h) = (h^3 + 3h^2 + 3h + 1)/2$ if $h$ is odd and
$v(h) = (h^3 + 2h^2 + 3h + 2)/2$ if $h$ is even.

## Sources

- Melvyn B. Nathanson and Kevin O'Bryant, "The Fourth Positive Element in the Greedy `B_h`-Set", Lemma 2.

Stated but not proved: `MathlibExt.Combinatorics.GreedyBhFourthWanted.fourthValue_le_of_isFourthGreedyBh` is written with `theorem_wanted` in [WantedExt/Combinatorics/GreedyBhFourthWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreedyBhFourthWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/greedy-b-h-sets/index.html#fourth-value-le-of-is-fourth-greedy-bh).

## Upper bound for the fourth greedy $B_h$ term

Let $h$ and $a$ be natural numbers with
$h \ge 1$. If $a$ is the fourth positive element $a_4(h)$ of the greedy $B_h$-set, then
$a \le v(h)$, where $v(h) = (h^3 + 3h^2 + 3h + 1)/2$ if $h$ is odd and
$v(h) = (h^3 + 2h^2 + 3h + 2)/2$ if $h$ is even.

## Sources

- Melvyn B. Nathanson and Kevin O'Bryant, "The Fourth Positive Element in the Greedy `B_h`-Set", Lemma 3.

Stated but not proved: `MathlibExt.Combinatorics.GreedyBhFourthWanted.isFourthGreedyBh_le_fourthValue` is written with `theorem_wanted` in [WantedExt/Combinatorics/GreedyBhFourthWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreedyBhFourthWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/greedy-b-h-sets/index.html#is-fourth-greedy-bh-le-fourth-value).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Greedy B_h-sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/greedy-b-h-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/greedy-b-h-sets)
