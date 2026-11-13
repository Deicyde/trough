---
declaration: section
origin: cited
lean: MetaMathlibExt.IsDiophantine, MetaMathlibExt.IsDiophantineSet, MetaMathlibExt.isDiophantine_univ, MetaMathlibExt.isDiophantine_empty, MathlibExt.NumberTheory.DPRMWanted.dprm_theorem
statement: formalized
proof: formalized
---

# Diophantine sets and Hilbert's tenth problem

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/diophantine-sets-and-hilbert-s-tenth-problem/index.html).

## Diophantine sets

Let $\varphi : A \to R$ be a ring homomorphism of commutative rings and
let $k \in \mathbb{N}$. Polynomials with coefficients in $A$ are evaluated at points with
coordinates in $R$ by first mapping their coefficients into $R$ by $\varphi$. A subset
$S \subseteq R^k$ is Diophantine over $R$ with coefficients from $A$ through $\varphi$ when there
are $n \in \mathbb{N}$ and a finite set $P$ of polynomials with coefficients in $A$ in the
variables $x_1, \dots, x_k, y_1, \dots, y_n$ such that for every $x \in R^k$, $x \in S$ if and
only if there is $y \in R^n$ with $p(x, y) = 0$ for all $p \in P$.

Formalized by `MetaMathlibExt.IsDiophantine`, a definition declared in [MathlibExt/Logic/Diophantine.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Logic/Diophantine.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/diophantine-sets-and-hilbert-s-tenth-problem/index.html#is-diophantine).

## Diophantine subsets of a ring

Let $\varphi : A \to R$ be a ring homomorphism of commutative
rings. A subset $S \subseteq R$ is Diophantine over $R$ with coefficients from $A$ through $\varphi$
when the set $\{(s) : s \in S\} \subseteq R^1$ of one-coordinate points with coordinate in $S$ is a
Diophantine subset of $R^1$ over $R$ with coefficients from $A$ through $\varphi$.

Formalized by `MetaMathlibExt.IsDiophantineSet`, a definition declared in [MathlibExt/Logic/Diophantine.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Logic/Diophantine.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/diophantine-sets-and-hilbert-s-tenth-problem/index.html#is-diophantine-set).

## The whole space is Diophantine

Let $\varphi : A \to R$ be a ring homomorphism of
commutative rings. For every $k \in \mathbb{N}$, the whole space $R^k$ is Diophantine over $R$ with
coefficients from $A$ through $\varphi$.

It is cut out by the empty set of polynomials, with no auxiliary variables.

Formalized by `MetaMathlibExt.isDiophantine_univ`, a theorem declared in [MathlibExt/Logic/Diophantine.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Logic/Diophantine.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/diophantine-sets-and-hilbert-s-tenth-problem/index.html#is-diophantine-univ).

## The empty set is Diophantine

Let $\varphi : A \to R$ be a ring homomorphism of commutative
rings, with $R$ nontrivial. For every $k \in \mathbb{N}$, the empty subset of $R^k$ is Diophantine
over $R$ with coefficients from $A$ through $\varphi$.

It is cut out by the constant polynomial $1$.

Formalized by `MetaMathlibExt.isDiophantine_empty`, a theorem declared in [MathlibExt/Logic/Diophantine.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Logic/Diophantine.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/diophantine-sets-and-hilbert-s-tenth-problem/index.html#is-diophantine-empty).

## Davis–Putnam–Robinson–Matiyasevich theorem

A set $S$ of natural numbers is recursively
enumerable if and only if it is Diophantine, that is, there is a polynomial $p$ with integer
coefficients such that $n \in S$ exactly when $p(n, t_1, \dots, t_k) = 0$ for some natural numbers
$t_1, \dots, t_k$.

## Sources

- M. Davis, H. Putnam, J. Robinson, The decision problem for exponential Diophantine equations, Ann. of Math. 74 (1961); Y. Matiyasevich, Enumerable sets are Diophantine, Dokl. Akad. Nauk SSSR 191 (1970) 279–282; textbook in Matiyasevich, Hilbert's Tenth Problem

Formalized by `MathlibExt.NumberTheory.DPRMWanted.dprm_theorem`, a theorem declared in [MathlibExt/NumberTheory/DPRM.lean, line 2201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DPRM.lean#L2201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/diophantine-sets-and-hilbert-s-tenth-problem/index.html#dprm-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diophantine sets and Hilbert's tenth problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/undecidable-problems/diophantine-sets-and-hilbert-s-tenth-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/undecidable-problems/diophantine-sets-and-hilbert-s-tenth-problem)
