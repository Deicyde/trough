---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.BuchiSquareSequenceBoundWanted.IsBuchiSequence, MathlibExt.NumberTheory.BuchiSquareSequenceBoundWanted.IsTrivial, MathlibExt.NumberTheory.BuchiSquareSequenceBoundWanted.conjecture, MathlibExt.NumberTheory.BuchiSquareSequenceBoundWanted.conjecture_holds
statement: formalized
---

# Büchi's problem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/b-chi-s-problem/index.html).

## Büchi sequences

Let $M$ be a natural number. A sequence of integers
$u_0, u_1, u_2, \dots$ is a Büchi sequence of length $M$ when the second differences of its
squares equal $2$ along its first $M$ terms, that is,
$u_{j+2}^2 - 2u_{j+1}^2 + u_j^2 = 2$ for every $j$ with $j + 2 < M$.

Only the terms $u_j$ with $j < M$ are constrained.

Formalized by `MathlibExt.NumberTheory.BuchiSquareSequenceBoundWanted.IsBuchiSequence`, a definition declared in [WantedExt/NumberTheory/BuchiSquareSequenceBoundWanted.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BuchiSquareSequenceBoundWanted.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/b-chi-s-problem/index.html#is-buchi-sequence).

## Trivial sequences in Büchi's problem

Let $M$ be a natural number. A sequence of
integers $u_0, u_1, u_2, \dots$ is trivial at length $M$ when there is an integer $x$ with
$u_j^2 = (x + j)^2$ for every $j < M$; equivalently, after changing the signs of some of its
terms, its first $M$ terms are the consecutive integers $x, x + 1, \dots, x + M - 1$.

Formalized by `MathlibExt.NumberTheory.BuchiSquareSequenceBoundWanted.IsTrivial`, a definition declared in [WantedExt/NumberTheory/BuchiSquareSequenceBoundWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BuchiSquareSequenceBoundWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/b-chi-s-problem/index.html#is-trivial).

## Büchi's square-sequence conjecture

There is a natural number $M \ge 5$ such that
every integer Büchi sequence of length $M$ is trivial: for every sequence of integers
$u_0, u_1, u_2, \dots$ with $u_{j+2}^2 - 2u_{j+1}^2 + u_j^2 = 2$ for all $j$ with
$j + 2 < M$, there is an integer $x$ with $u_j^2 = (x + j)^2$ for all $j < M$.

Formalized by `MathlibExt.NumberTheory.BuchiSquareSequenceBoundWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/BuchiSquareSequenceBoundWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BuchiSquareSequenceBoundWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/b-chi-s-problem/index.html#conjecture).

## Resolution of Büchi's square-sequence conjecture

There is a natural number $M \ge 5$
such that every integer Büchi sequence of length $M$ is trivial: for every sequence of
integers $u_0, u_1, u_2, \dots$ with $u_{j+2}^2 - 2u_{j+1}^2 + u_j^2 = 2$ for all $j$ with
$j + 2 < M$, there is an integer $x$ with $u_j^2 = (x + j)^2$ for all $j < M$.

Stanley Yao Xiao (arXiv:2412.16740v3, Jun 2025) proves unconditionally that five integer
squares with constant second difference $2$ are consecutive (Theorem 1.3), so the statement
holds with $M = 5$; the earlier length-8 bound was Vojta's conditional result under
Bombieri–Lang.

## Sources

- Stanley Yao Xiao, Hilbert's tenth problem for systems of diagonal quadratic forms, and Büchi's problem, arXiv:2412.16740v3 (2025), https://arxiv.org/abs/2412.16740v3.

Stated but not proved: `MathlibExt.NumberTheory.BuchiSquareSequenceBoundWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/BuchiSquareSequenceBoundWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BuchiSquareSequenceBoundWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/b-chi-s-problem/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Büchi's problem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/b-chi-s-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/b-chi-s-problem)
