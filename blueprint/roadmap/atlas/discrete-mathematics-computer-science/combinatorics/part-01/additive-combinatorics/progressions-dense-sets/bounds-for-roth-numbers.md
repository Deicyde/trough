---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.RothNumberLogPowerErdosProblem140Wanted.rothNumberLogPowerDecay, MathlibExt.Combinatorics.RothNumberLogPowerErdosProblem140Wanted.rothNumberLogPowerDecay_holds
statement: formalized
---

# Bounds for Roth numbers

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/bounds-for-roth-numbers/index.html).

## Roth numbers below every power of the logarithm (Erdős Problem 140)

The statement that
for every real $C > 0$ there is a real constant $K$ such that $r_3(N) \le K N / (\log N)^C$ for
every natural number $N \ge 2$, where $r_3(N)$ is the largest size of a subset of
$\{0, 1, \dots, N - 1\}$ containing no non-trivial three-term arithmetic progression.

Formalized by `MathlibExt.Combinatorics.RothNumberLogPowerErdosProblem140Wanted.rothNumberLogPowerDecay`, a definition declared in [WantedExt/Combinatorics/RothNumberLogPowerErdosProblem140Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RothNumberLogPowerErdosProblem140Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/bounds-for-roth-numbers/index.html#roth-number-log-power-decay).

## Kelley–Meka: Roth numbers are below every power of the logarithm

For every real $C > 0$
there is a real constant $K$ such that $r_3(N) \le K N / (\log N)^C$ for every natural number
$N \ge 2$, where $r_3(N)$ is the largest size of a subset of $\{0, 1, \dots, N - 1\}$ containing no
non-trivial three-term arithmetic progression.

This follows from the theorem of Kelley and Meka that for some $\beta > 0$ every subset of
$\{1, \dots, N\}$ of size at least $2^{-O((\log N)^\beta)} N$ contains a non-trivial three-term
progression, which gives $r_3(N) \le N \exp(-c (\log N)^\beta)$ for some $c > 0$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #140, https://www.erdosproblems.com/140 (status PROVED (LEAN)); resolution: Z. Kelley and R. Meka, Strong bounds for 3-progressions, FOCS 2023, arXiv:2302.05537, abstract: every A ⊆ {1, …, N} with |A| ≥ 2^{-O((log N)^β)} N contains a non-trivial 3-term progression; erdosproblems.com/140, https://arxiv.org/abs/2302.05537.

Stated but not proved: `MathlibExt.Combinatorics.RothNumberLogPowerErdosProblem140Wanted.rothNumberLogPowerDecay_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RothNumberLogPowerErdosProblem140Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RothNumberLogPowerErdosProblem140Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/bounds-for-roth-numbers/index.html#roth-number-log-power-decay-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounds for Roth numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/bounds-for-roth-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/bounds-for-roth-numbers)
