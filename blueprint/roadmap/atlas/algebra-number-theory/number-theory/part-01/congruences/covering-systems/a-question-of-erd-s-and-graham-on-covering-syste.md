---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosGrahamCoveringWanted.not_covering_of_nonintersecting, MathlibExt.NumberTheory.ErdosGrahamCoveringWanted.one_le_sum_inv_moduli
statement: formalized
---

# A question of Erdős and Graham on covering systems

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/a-question-of-erd-s-and-graham-on-covering-syste/index.html).

## Non-intersecting integers admit no covering system of divisor form

Let $n$ be a natural
number and let $D$ be the finite set of divisors of $n$ greater than $1$, taken empty when $n = 0$.
Call $n$ non-intersecting if there are integers $a_d$, one for each natural number $d$, such that
for all distinct natural numbers $d, d' > 1$ dividing $n$ (every $d$ divides $0$), if the classes
$a_d \pmod d$ and $a_{d'} \pmod{d'}$ have an integer in common, then $d$ and $d'$ are coprime. If
$n$ is non-intersecting, then there are no integers $b_d$ for $d \in D$ such that every integer
lies in the class $b_d \pmod d$ for some $d \in D$.

The families $(a_d)$ and $(b_d)$ are independent; in particular, no family of classes
$a_d \pmod d$ for $d \in D$ with the coprime-overlap property covers the integers.

## Sources

- Sarosh Adenwalla, "A Question of Erdős and Graham on Covering Systems", Theorem 3.2.

Stated but not proved: `MathlibExt.NumberTheory.ErdosGrahamCoveringWanted.not_covering_of_nonintersecting` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosGrahamCoveringWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosGrahamCoveringWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/a-question-of-erd-s-and-graham-on-covering-syste/index.html#not-covering-of-nonintersecting).

## Covering systems have reciprocal-moduli sum at least one

Let $d_1, \dots, d_t$ be
positive integers and $a_1, \dots, a_t$ integers such that every integer $z$ satisfies
$z \equiv a_i \pmod{d_i}$ for some $i$. Then $\sum_{i=1}^t 1/d_i \ge 1$.

## Sources

- Sarosh Adenwalla, "A Question of Erdős and Graham on Covering Systems", Lemma 2.2.

Stated but not proved: `MathlibExt.NumberTheory.ErdosGrahamCoveringWanted.one_le_sum_inv_moduli` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosGrahamCoveringWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosGrahamCoveringWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/a-question-of-erd-s-and-graham-on-covering-syste/index.html#one-le-sum-inv-moduli).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: A question of Erdős and Graham on covering systems](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/a-question-of-erd-s-and-graham-on-covering-syste/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/congruences/covering-systems/a-question-of-erd-s-and-graham-on-covering-syste)
