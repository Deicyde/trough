---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem351Wanted.EP351.StronglyComplete, MathlibExt.NumberTheory.ErdosProblem351Wanted.EP351.ErdosSet351, MathlibExt.NumberTheory.ErdosProblem351Wanted.EP351.StrongCompletenessQuestion, MathlibExt.NumberTheory.ErdosProblem351Wanted.StrongCompletenessQuestion_holds
statement: formalized
---

# Strongly complete sequences

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/strongly-complete-sequences/index.html).

## Strongly complete sets

## Strongly complete sets of rationals

A set $A$ of rational numbers is strongly complete
when, for every finite set $B$ of rational numbers, there is an integer $N_0$ such that every
integer $m \ge N_0$ is the sum of the elements of some finite subset of $A \setminus B$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem351Wanted.EP351.StronglyComplete`, a definition declared in [WantedExt/NumberTheory/ErdosProblem351Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem351Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/strongly-complete-sequences/index.html#strongly-complete).

## Polynomial values plus reciprocals

For a polynomial $p$ with rational coefficients,
$A_p$ is the set of rational numbers $p(n) + 1/n$, where $n$ ranges over the positive
integers.

Formalized by `MathlibExt.NumberTheory.ErdosProblem351Wanted.EP351.ErdosSet351`, a definition declared in [WantedExt/NumberTheory/ErdosProblem351Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem351Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/strongly-complete-sequences/index.html#erdos-set351).

## The strong completeness statement of Erdős Problem 351

This is the proposition that for
every polynomial $p$ with rational coefficients and positive leading coefficient, the set $A_p$
of rational numbers $p(n) + 1/n$, where $n$ ranges over the positive integers, is strongly
complete.

Formalized by `MathlibExt.NumberTheory.ErdosProblem351Wanted.EP351.StrongCompletenessQuestion`, a definition declared in [WantedExt/NumberTheory/ErdosProblem351Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem351Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/strongly-complete-sequences/index.html#strong-completeness-question).

## Strong completeness of polynomial values plus reciprocals (Erdős Problem 351)

For every
polynomial $p$ with rational coefficients and positive leading coefficient, let $A_p$ be the set
of rational numbers $p(n) + 1/n$, where $n$ ranges over the positive integers. Then $A_p$ is
strongly complete: for every finite set $B$ of rational numbers there is an integer $N_0$ such
that every integer $m \ge N_0$ is the sum of the elements of some finite subset of
$A_p \setminus B$.

Resolved true: The maintained Erdős Problems page marks Problem 351 proved in the affirmative
and records that the positive solution follows from the positive solution of Problem 283.

## Sources

- plby/lean-proofs, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/Util/PolynomialEgyptianSums.lean#L10266.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem351Wanted.StrongCompletenessQuestion_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem351Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem351Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/strongly-complete-sequences/index.html#strong-completeness-question-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strongly complete sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/strongly-complete-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/additive-number-theory/strongly-complete-sequences)
