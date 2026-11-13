---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.ClauseSatisfied, MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.IsKSATFunction, MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.IsPositiveUnateIn, MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.IsNegativeUnateIn, MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.IsUnate, MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.countKSATFunctions, MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.countUnateKSATFunctions, MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.conjecture
statement: formalized
---

# Enumeration of k-SAT functions

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html).

## Satisfied clause

Let $n \in \mathbb{N}$. A clause on $n$ variables is a finite set $C$ of
literals $(i, b)$, where $i \in \{0, \dots, n - 1\}$ is a variable and $b \in \{\mathrm{true},
\mathrm{false}\}$. An assignment $x : \{0, \dots, n - 1\} \to \{\mathrm{true}, \mathrm{false}\}$
satisfies $C$ if $x_i = b$ for some literal $(i, b) \in C$.

## Sources

- [OWR-10252930-018], `k`-SAT clause semantics.

Formalized by `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.ClauseSatisfied`, a definition declared in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#clause-satisfied).

## $k$-SAT function

Let $k, n \in \mathbb{N}$. A Boolean function
$f : \{\mathrm{true}, \mathrm{false}\}^n \to \{\mathrm{true}, \mathrm{false}\}$ is a $k$-SAT
function on $n$ variables if there is a finite set $S$ of clauses on $n$ variables such that each
clause in $S$ has at most $k$ literals, no two of them on the same variable, and for every
assignment $x$, $f(x) = \mathrm{true}$ if and only if $x$ satisfies every clause in $S$.

## Sources

- [OWR-10252930-018], `k`-SAT functions.

Formalized by `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.IsKSATFunction`, a definition declared in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#is-ksatfunction).

## Positively unate variable

Let $f : \{\mathrm{true}, \mathrm{false}\}^n \to
\{\mathrm{true}, \mathrm{false}\}$ be a Boolean function and $i$ one of its $n$ variables. Then
$f$ is positively unate in $i$ if for all assignments $x$ and $y$ that agree at every variable
other than $i$ and have $x_i = \mathrm{false}$ and $y_i = \mathrm{true}$, $f(x) = \mathrm{true}$
implies $f(y) = \mathrm{true}$. Equivalently, switching $i$ from false to true never switches
the value of $f$ from true to false.

## Sources

- [OWR-10252930-018], unate.

Formalized by `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.IsPositiveUnateIn`, a definition declared in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#is-positive-unate-in).

## Negatively unate variable

Let $f : \{\mathrm{true}, \mathrm{false}\}^n \to
\{\mathrm{true}, \mathrm{false}\}$ be a Boolean function and $i$ one of its $n$ variables. Then
$f$ is negatively unate in $i$ if for all assignments $x$ and $y$ that agree at every variable
other than $i$ and have $x_i = \mathrm{false}$ and $y_i = \mathrm{true}$, $f(y) = \mathrm{true}$
implies $f(x) = \mathrm{true}$. Equivalently, switching $i$ from false to true never switches
the value of $f$ from false to true.

## Sources

- [OWR-10252930-018], unate.

Formalized by `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.IsNegativeUnateIn`, a definition declared in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#is-negative-unate-in).

## Unate Boolean function

A Boolean function $f : \{\mathrm{true}, \mathrm{false}\}^n \to
\{\mathrm{true}, \mathrm{false}\}$ is unate if, for every variable $i$, $f$ is positively unate
in $i$ or negatively unate in $i$.

## Sources

- [OWR-10252930-018], unate.

Formalized by `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.IsUnate`, a definition declared in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#is-unate).

## Number of $k$-SAT functions

For natural numbers $k$ and $n$, the number of Boolean
functions $f : \{\mathrm{true}, \mathrm{false}\}^n \to \{\mathrm{true}, \mathrm{false}\}$ that are
$k$-SAT functions on $n$ variables.

## Sources

- [OWR-10252930-018], enumeration of `k`-SAT functions.

Formalized by `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.countKSATFunctions`, a definition declared in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#count-ksatfunctions).

## Number of unate $k$-SAT functions

For natural numbers $k$ and $n$, the number of Boolean
functions $f : \{\mathrm{true}, \mathrm{false}\}^n \to \{\mathrm{true}, \mathrm{false}\}$ that are
$k$-SAT functions on $n$ variables and are unate.

## Sources

- [OWR-10252930-018], typical structure (unate).

Formalized by `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.countUnateKSATFunctions`, a definition declared in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#count-unate-ksatfunctions).

## Bollobás–Brightwell–Leader conjecture for $k$

For a natural number $k$, the proposition
that if $k \ge 2$, then the number of unate $k$-SAT functions on $n$ Boolean variables divided by
the number of $k$-SAT functions on $n$ Boolean variables tends to $1$ as $n \to \infty$; that is,
a $1 - o(1)$ fraction of the $k$-SAT functions on $n$ variables is unate.

## Sources

- [OWR-10252930-018], DOI 10.4171/owr/2022/22, arXiv:2107.09233.

Formalized by `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#conjecture).

## Bollobás–Brightwell–Leader conjecture for all $k$

The proposition that for every natural
number $k \ge 2$, the number of unate $k$-SAT functions on $n$ Boolean variables divided by the
number of $k$-SAT functions on $n$ Boolean variables tends to $1$ as $n \to \infty$.

Formalized by `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.conjectureAllK`, a definition declared in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#conjecture-all-k).

## Nearly all $k$-SAT functions are unate

For every natural number $k \ge 2$, the number of
unate $k$-SAT functions on $n$ Boolean variables divided by the number of $k$-SAT functions on
$n$ Boolean variables tends to $1$ as $n \to \infty$; that is, the Bollobás–Brightwell–Leader
conjecture holds for every $k$.

Balogh, Dong, Lidický, Mani and Zhao prove this as Theorem 1.1 of arXiv:2209.04894. They use a
DNF convention with exactly $k$ distinct variables per clause, which gives the same counts as the
CNF, at-most-$k$ convention here for $n \ge k$ (negation preserves unateness).

## Sources

- J. Balogh, D. Dong, B. Lidický, N. Mani, Y. Zhao, Nearly all k-SAT functions are unate, STOC 2023; J. Eur. Math. Soc. (2026), arXiv:2209.04894, https://arxiv.org/abs/2209.04894.

Stated but not proved: `MathlibExt.Combinatorics.BollobasBrightwellLeaderUnateDensityWanted.conjectureAllK_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/BollobasBrightwellLeaderUnateDensityWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html#conjecture-all-k-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Enumeration of k-SAT functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/enumeration-of-k-sat-functions)
