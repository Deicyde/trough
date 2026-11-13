---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem539Wanted.IsCofactorLowerBound, MathlibExt.NumberTheory.ErdosProblem539Wanted.cofactorThreshold, MathlibExt.NumberTheory.ErdosProblem539Wanted.conjecture, MathlibExt.NumberTheory.ErdosProblem539Wanted.conjecture_holds
statement: formalized
---

# Quotients a/gcd(a, b) in sets of integers

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/quotients-a-gcd-a-b-in-sets-of-integers/index.html).

## Cofactor lower bound

For natural numbers $n$ and $m$, $m$ is a cofactor lower bound for
$n$ when, for every set $A$ of exactly $n$ positive integers, the set
$\{a/\gcd(a,b) : a, b \in A\}$ has at least $m$ elements.

Members of $A$ are required to be positive since the quotient $a/\gcd(a,b)$ is undefined at
$a = b = 0$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem539Wanted.IsCofactorLowerBound`, a definition declared in [WantedExt/NumberTheory/ErdosProblem539Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem539Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/quotients-a-gcd-a-b-in-sets-of-integers/index.html#is-cofactor-lower-bound).

## Erdős cofactor threshold

For a natural number $n$, the cofactor threshold $h(n)$ is the
largest natural number $m$ such that for every set $A$ of exactly $n$ positive integers, the set
$\{a/\gcd(a,b) : a, b \in A\}$ has at least $m$ elements.

Formalized by `MathlibExt.NumberTheory.ErdosProblem539Wanted.cofactorThreshold`, a definition declared in [WantedExt/NumberTheory/ErdosProblem539Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem539Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/quotients-a-gcd-a-b-in-sets-of-integers/index.html#cofactor-threshold).

## Statement of Erdős Problem 539

Let $h(n)$ denote the cofactor threshold of $n$. The
statement is that $\sqrt{n} = O(h(n))$ as $n \to \infty$, that is, there are a real constant $C$
and an $n_0$ such that $\sqrt{n} \le C\,h(n)$ for all natural numbers $n \ge n_0$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem539Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem539Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem539Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/quotients-a-gcd-a-b-in-sets-of-integers/index.html#conjecture).

## Erdős Problem 539: square-root lower bound for the cofactor threshold

For a natural number
$n$, let $h(n)$ be the largest natural number $m$ such that for every set $A$ of exactly $n$
positive integers, the set $\{a/\gcd(a,b) : a, b \in A\}$ has at least $m$ elements. Then
$\sqrt{n} = O(h(n))$ as $n \to \infty$: there are a real constant $C$ and an $n_0$ such that
$\sqrt{n} \le C\,h(n)$ for all natural numbers $n \ge n_0$.

This lower bound was proved by Erdős and Szemerédi. The open problem of determining the exact
order of growth of $h(n)$ is not part of this statement.

## Sources

- J. Schmitt, T. Gehrunger, J. Dekoninck, G. Bérczi, U. Kreitner, L. Price, D. Holmes, ProofCouncil: An LLM Agent for Solving Open Mathematical Problems, arXiv:2607.09474 (2026), https://arxiv.org/abs/2607.09474.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem539Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem539Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem539Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/quotients-a-gcd-a-b-in-sets-of-integers/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quotients a/gcd(a, b) in sets of integers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/quotients-a-gcd-a-b-in-sets-of-integers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/additive-number-theory/quotients-a-gcd-a-b-in-sets-of-integers)
