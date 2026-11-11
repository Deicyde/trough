---
declaration: section
origin: cited
lean: Cslib.Algorithms.SAT.DPLL.decideWithFuel_eq_true_iff, Cslib.Algorithms.SAT.DPLL.dpll_eq_true_iff
statement: formalized
proof: formalized
---

# Correctness of the DPLL solver

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/correctness-of-the-dpll-solver/index.html).

## Correctness of DPLL with sufficient fuel

Let $\varphi$ be a CNF formula and let $n$ be a
natural number at least the number of distinct variables occurring in $\varphi$. Then DPLL with
fuel $n$ returns true on $\varphi$ if and only if $\varphi$ is satisfiable.

Formalized by `Cslib.Algorithms.SAT.DPLL.decideWithFuel_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/SAT/DPLL/Correctness.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DPLL/Correctness.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/correctness-of-the-dpll-solver/index.html#decide-with-fuel-eq-true-iff).

## Correctness of DPLL

For every CNF formula $\varphi$, the DPLL procedure returns true on
$\varphi$ if and only if $\varphi$ is satisfiable.

Formalized by `Cslib.Algorithms.SAT.DPLL.dpll_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/SAT/DPLL/Correctness.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DPLL/Correctness.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/correctness-of-the-dpll-solver/index.html#dpll-eq-true-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Correctness of the DPLL solver](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/correctness-of-the-dpll-solver/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/propositional-logic/dpll-algorithm/correctness-of-the-dpll-solver)
