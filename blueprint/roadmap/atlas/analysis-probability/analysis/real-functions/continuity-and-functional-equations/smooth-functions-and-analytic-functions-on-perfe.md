---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook17Point1Wanted.IsPerfectSet, MathlibExt.Analysis.ScottishBook17Point1Wanted.ScottishBookProblem17Point1Claim, MathlibExt.Analysis.ScottishBook17Point1Wanted.continuousFunctionPerfectAnalytic_refuted
statement: formalized
---

# Smooth functions and analytic functions on perfect sets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/smooth-functions-and-analytic-functions-on-perfe/index.html).

## Perfect sets of real numbers

A set $s \subseteq \mathbb{R}$ is perfect if it is closed,
nonempty, and has no isolated points: every $x \in s$ lies in the closure of $s \setminus \{x\}$.

Formalized by `MathlibExt.Analysis.ScottishBook17Point1Wanted.IsPerfectSet`, a definition declared in [WantedExt/Analysis/ScottishBook17Point1Wanted.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook17Point1Wanted.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/smooth-functions-and-analytic-functions-on-perfe/index.html#is-perfect-set).

## Ulam's problem on analytic agreement on a perfect set

Ulam's Problem 17.1 from the Scottish Book: for every continuous `f` on
`[0, 1]`, do there exist a perfect set `C` in `[0, 1]` and an analytic
function `φ` with `f x = φ x` for every `x ∈ C`? The claim is stated for
`C ^ ∞` functions, which is the case refuted by Zahorski's construction.

Formalized by `MathlibExt.Analysis.ScottishBook17Point1Wanted.ScottishBookProblem17Point1Claim`, a definition declared in [WantedExt/Analysis/ScottishBook17Point1Wanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook17Point1Wanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/smooth-functions-and-analytic-functions-on-perfe/index.html#scottish-book-problem17-point1-claim).

## Zahorski's negative answer to Ulam's perfect set problem

Problem 17.1 is false: the answer is negative. Source: S. Ulam, Problem 17.1
of the Scottish Book; Z. Zahorski gave a negative answer by constructing a
`C ^ ∞` function that agrees with every real-analytic function on at most
finitely many points, so no nonempty perfect set `C` can work for it: Z.
Zahorski, "Sur l'ensemble des points singuliers d'une fonction d'une
variable reelle admettant les derivees de tous les ordres", Fund. Math. 34
(1947), 183-245. The 2026 survey "90+ years of the Scottish Book"
(arXiv:2603.27867) confirms the negative solution.

Stated but not proved: `MathlibExt.Analysis.ScottishBook17Point1Wanted.continuousFunctionPerfectAnalytic_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook17Point1Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook17Point1Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/smooth-functions-and-analytic-functions-on-perfe/index.html#continuous-function-perfect-analytic-ref).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smooth functions and analytic functions on perfect sets](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/smooth-functions-and-analytic-functions-on-perfe/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/smooth-functions-and-analytic-functions-on-perfe)
