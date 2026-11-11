---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem477Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem477Wanted.conjecture_holds, MathlibExt.NumberTheory.ErdosProblem31Wanted.conjecture_holds
statement: formalized
---

# Additive complements

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-complements/index.html).

## Erdős Problem 477

The statement that there are a polynomial $f$ with integer
coefficients of degree at least $2$ and a set $A$ of integers such that for every integer $n$
there is exactly one pair $(a, b)$ with $a \in A$, $b = f(k)$ for some integer $k$, and
$n = a + b$. Only the pair is required to be unique, not the integer $k$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem477Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem477Wanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem477Wanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-complements/index.html#conjecture).

## Erdős Problem 477 has a positive answer

There are a polynomial $f$ with integer
coefficients of degree at least $2$ and a set $A$ of integers such that for every integer $n$
there is exactly one pair $(a, b)$ with $a \in A$, $b = f(k)$ for some integer $k$, and
$n = a + b$.

Contrary to Erdős and Graham's expectation, GPT (prompted independently by L. Price and
pipeline-math) proved that such a set $A$ exists for $f(k) = k^d$ with every even $d \ge 6$, so
$f(k) = k^6$ is a witness.

## Sources

- T. F. Bloom, Erdős Problem #477, erdosproblems.com (live page, LaTeX source and forum threads read 2026-10-22), https://www.erdosproblems.com/477.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem477Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem477Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem477Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-complements/index.html#conjecture-holds).

## Lorentz's theorem on additive complements (Erdős Problem 31)

For every infinite set
$A$ of natural numbers there is a set $B$ of natural numbers of natural density $0$ such that
every sufficiently large natural number lies in $A + B = \{a + b \mid a \in A,\ b \in B\}$.

Resolved true: Proved by Lorentz [Lo54]. Source: George G. Lorentz, On a problem of additive
number theory, Proceedings of the American Mathematical Society 5 (1954), 838–841,
https://doi.org/10.1090/s0002-9939-1954-0063389-3. Moved from
`OpenConjectures/NumberTheory/ErdosProblem31`.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem31Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem31Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem31Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-complements/index.html#conjecture-holds-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Additive complements](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-complements/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/additive-complements)
