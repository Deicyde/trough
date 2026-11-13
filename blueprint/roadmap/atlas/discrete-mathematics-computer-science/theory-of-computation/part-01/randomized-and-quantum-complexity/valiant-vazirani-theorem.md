---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.ValiantVazirani.satDec', MetaMathlibExt.Complexity.KeyTheorems.ValiantVazirani.uniqueSatDec, MetaMathlibExt.Complexity.KeyTheorems.ValiantVazirani.valiant_vazirani
statement: formalized
---

# Valiant–Vazirani theorem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/valiant-vazirani-theorem/index.html).

## SAT with a unary variable count as a decision problem

A bitstring $x$ is a yes-instance
exactly when bitstring decoding of $x$, as a pair of a list of booleans and a CNF formula,
succeeds and returns a pair $(u, \varphi)$ such that, writing $m$ for the length of $u$, every
variable occurring in $\varphi$ is less than $m$ and some assignment of booleans to the variables
$0, \dots, m - 1$ satisfies $\varphi$ once it is extended by assigning false to every variable
$v \ge m$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ValiantVazirani.satDec'`, a definition declared in [WantedExt/Complexity/KeyTheorems/ValiantVaziraniWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/ValiantVaziraniWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/valiant-vazirani-theorem/index.html#sat-dec).

## UniqueSAT with a unary variable count as a decision problem

A bitstring $x$ is a
yes-instance exactly when bitstring decoding of $x$, as a pair of a list of booleans and a CNF
formula, succeeds and returns a pair $(u, \varphi)$ such that, writing $m$ for the length of $u$,
every variable occurring in $\varphi$ is less than $m$ and exactly one assignment of booleans to
the variables $0, \dots, m - 1$ satisfies $\varphi$ once it is extended by assigning false to
every variable $v \ge m$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ValiantVazirani.uniqueSatDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/ValiantVaziraniWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/ValiantVaziraniWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/valiant-vazirani-theorem/index.html#unique-sat-dec).

## Valiant-Vazirani: SAT reduces to UniqueSAT

There are a polynomial $p$ with
natural-number coefficients and a polynomial-time computable function $R$ from pairs of
bitstrings to bitstrings such that, for every bitstring $x$ of length $n$: if $x$ is not in SAT,
then for every bitstring $r$ of length $p(n)$ the bitstring $R(x, r)$ is in neither SAT nor
UniqueSAT; and if $x$ is in SAT, then the number $N$ of bitstrings $r$ of length $p(n)$ for which
$R(x, r)$ is in UniqueSAT satisfies $8(n + 1) N \ge 2^{p(n)}$.

Here SAT and UniqueSAT are the bitstring decision problems for CNF formulas with the variable
count given in unary.

## Sources

- L. G. Valiant and V. V. Vazirani, "NP is as easy as detecting unique solutions", Theoretical Computer Science 47 (1986), 85-93 (STOC 1985).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.ValiantVazirani.valiant_vazirani` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/ValiantVaziraniWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/ValiantVaziraniWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/valiant-vazirani-theorem/index.html#valiant-vazirani).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Valiant–Vazirani theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/valiant-vazirani-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/valiant-vazirani-theorem)
