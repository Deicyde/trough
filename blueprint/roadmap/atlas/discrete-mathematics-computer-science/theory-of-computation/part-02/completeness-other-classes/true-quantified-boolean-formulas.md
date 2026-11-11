---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.TQBFPSPACEComplete.EvalQBF, MetaMathlibExt.Complexity.KeyTheorems.TQBFPSPACEComplete.tqbfDec, MetaMathlibExt.Complexity.KeyTheorems.TQBFPSPACEComplete.tqbf_pspace_complete
statement: formalized
---

# True quantified Boolean formulas

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/true-quantified-boolean-formulas/index.html).

## Evaluation of a quantified CNF formula

Let $\varphi$ be a CNF formula, let
$a : \mathbb{N} \to \{\mathrm{true}, \mathrm{false}\}$ be an assignment, and let $Q$ be a
quantifier prefix, a list of pairs $(e, v)$ of a flag $e$ (true for $\exists$, false for
$\forall$) and a variable $v \in \mathbb{N}$. Write $a[v \mapsto b]$ for the assignment that
agrees with $a$ except that it sends $v$ to $b$. With the empty prefix, the formula holds under
$a$ when $a$ satisfies $\varphi$. With a prefix whose first entry is $(e, v)$ and whose remaining
entries form $Q'$, it holds under $a$ when, if $e$ is true, the formula with prefix $Q'$ holds
under $a[v \mapsto \mathrm{true}]$ or under $a[v \mapsto \mathrm{false}]$, and, if $e$ is false,
the formula with prefix $Q'$ holds under both $a[v \mapsto \mathrm{true}]$ and
$a[v \mapsto \mathrm{false}]$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.TQBFPSPACEComplete.EvalQBF`, a definition declared in [WantedExt/Complexity/KeyTheorems/TQBFPSPACECompleteWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/TQBFPSPACECompleteWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/true-quantified-boolean-formulas/index.html#eval-qbf).

## TQBF as a decision problem

The TQBF decision problem accepts a bitstring $x$ exactly when
$x$ decodes, under the canonical bitstring encoding, to a pair $(Q, \varphi)$, where $Q$ is a
quantifier prefix, a list of $m$ pairs $(e_1, v_1), \dots, (e_m, v_m)$ of a flag $e_i$ (true for
$\exists$, false for $\forall$) and a variable $v_i \in \mathbb{N}$, and $\varphi$ is a CNF
formula, such that $v_1, \dots, v_m$ are $0, 1, \dots, m - 1$ in some order, every variable
occurring in $\varphi$ is less than $m$, and the quantified formula with prefix $Q$ and matrix
$\varphi$ holds under the assignment that sends every variable to false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.TQBFPSPACEComplete.tqbfDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/TQBFPSPACECompleteWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/TQBFPSPACECompleteWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/true-quantified-boolean-formulas/index.html#tqbf-dec).

## TQBF is PSPACE-complete

The TQBF decision problem, of true quantified Boolean formulas
with a CNF matrix, lies in the class PSPACE of decision problems, and every decision problem in
PSPACE has a polynomial-time many-one reduction to it.

## Sources

- L. J. Stockmeyer and A. R. Meyer, "Word problems requiring exponential time", Proceedings of the Fifth Annual ACM Symposium on Theory of Computing (STOC 1973), 1-9; C. H. Papadimitriou, Computational Complexity, 1994, Theorem 7.4.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.TQBFPSPACEComplete.tqbf_pspace_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/TQBFPSPACECompleteWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/TQBFPSPACECompleteWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/true-quantified-boolean-formulas/index.html#tqbf-pspace-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: True quantified Boolean formulas](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/true-quantified-boolean-formulas/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/true-quantified-boolean-formulas)
