---
declaration: section
origin: cited
lean: Cslib.Logic.PL.BDD.VarsLT, Cslib.Logic.PL.BDD.satCountFrom, Cslib.Logic.PL.BDD.satCount, Cslib.Logic.PL.BDD.countModels, Cslib.Logic.PL.BDD.countModels_congr, Cslib.Logic.PL.BDD.satCountFrom_eq_countModels, Cslib.Logic.PL.BDD.satCount_eq_countModels
statement: formalized
proof: formalized
---

# Counting satisfying assignments of a BDD

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd/index.html).

## Variables below a bound

For a natural number $m$, a diagram has its variables below $m$
when every variable tested at a node of the diagram is less than $m$.

Formalized by `Cslib.Logic.PL.BDD.VarsLT`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Count.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Count.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd/index.html#vars-lt).

## One-pass satisfy-count from a variable

For natural numbers $m$ and $n$ and a diagram $t$,
the satisfy-count $c_m(n, t)$ of $t$ from $n$ with bound $m$ is defined by recursion on $t$: a
leaf $\mathrm{true}$ gives $2^{m - n}$, a leaf $\mathrm{false}$ gives $0$, and a node testing the
variable $v$ with child $t_0$ for false and child $t_1$ for true gives
$2^{v - n} (c_m(v + 1, t_0) + c_m(v + 1, t_1))$. Here $m - n$ and $v - n$ are truncated
subtraction, equal to $0$ when the difference would be negative.

For $t$ ordered from $n$ whose tested variables are all below $m$, $c_m(n, t)$ is the number of
assignments to the variables $n, \dots, m - 1$ that make $t$ true.

Formalized by `Cslib.Logic.PL.BDD.satCountFrom`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Count.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Count.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd/index.html#sat-count-from).

## Satisfy-count

For a natural number $m$ and a diagram $t$, the satisfy-count of $t$ below
$m$ is the one-pass satisfy-count $c_m(0, t)$ of $t$ from the variable $0$ with bound $m$.

When $t$ is ordered from $0$ and every variable it tests is below $m$, this is the number of
assignments to the variables $0, \dots, m - 1$ that make $t$ true.

Formalized by `Cslib.Logic.PL.BDD.satCount`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Count.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Count.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd/index.html#sat-count).

## Model count by enumeration

An assignment is a map $\sigma$ from the variables, which are
natural numbers, to the truth values $\mathrm{false}$ and $\mathrm{true}$. For a list
$x_1, \dots, x_k$ of variables, a function $f$ from assignments to truth values, and an assignment
$\sigma$, the model count of $f$ over $x_1, \dots, x_k$ from $\sigma$ is the number of tuples
$(b_1, \dots, b_k) \in \{\mathrm{false}, \mathrm{true}\}^k$ such that $f$ is true at the assignment
obtained from $\sigma$ by setting $x_1$ to $b_1$, then $x_2$ to $b_2$, and so on up to setting
$x_k$ to $b_k$, a later setting overriding an earlier one of the same variable.

When $x_1, \dots, x_k$ are distinct, this is the number of assignments that agree with $\sigma$
outside $x_1, \dots, x_k$ and make $f$ true.

Formalized by `Cslib.Logic.PL.BDD.countModels`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Count.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Count.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd/index.html#count-models).

## Congruence for the model count

Let $x_1, \dots, x_k$ be a list of variables, $f$ and $g$
functions from assignments to truth values, and $\sigma$ an assignment. If $f(\tau) = g(\tau)$ for
every assignment $\tau$ such that $\tau(x) = \sigma(x)$ for every variable $x$ not in the list,
then the model counts of $f$ and of $g$ over $x_1, \dots, x_k$ from $\sigma$ are equal.

Formalized by `Cslib.Logic.PL.BDD.countModels_congr`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Count.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Count.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd/index.html#count-models-congr).

## The satisfy-count from a variable counts models

Let $m$ and $n$ be natural numbers and
$t$ a diagram ordered from $n$ (every tested variable is at least $n$, and tested variables
strictly increase along every path) in which every tested variable is below $m$. Then for every
assignment $\sigma$, the one-pass satisfy-count $c_m(n, t)$ of $t$ from $n$ with bound $m$ equals
the model count of the function $\tau \mapsto t(\tau)$ over the variables $n, n + 1, \dots, m - 1$
from $\sigma$ (no variables when $m \le n$), where $t(\tau)$ is the value of $t$ under $\tau$.

Formalized by `Cslib.Logic.PL.BDD.satCountFrom_eq_countModels`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Count.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Count.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd/index.html#sat-count-from-eq-count-models).

## Correctness of the satisfy-count

Let $m$ be a natural number and $t$ a diagram ordered
from $0$ (tested variables strictly increase along every path) in which every tested variable is
below $m$. Then for every assignment $\sigma$, the satisfy-count of $t$ below $m$ equals the model
count of the function $\tau \mapsto t(\tau)$ over the variables $0, 1, \dots, m - 1$ from
$\sigma$, where $t(\tau)$ is the value of $t$ under $\tau$. In other words, it is the number of
assignments to the variables $0, \dots, m - 1$ that make $t$ true.

Formalized by `Cslib.Logic.PL.BDD.satCount_eq_countModels`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Count.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Count.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd/index.html#sat-count-eq-count-models).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counting satisfying assignments of a BDD](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/binary-decision-diagrams/counting-satisfying-assignments-of-a-bdd)
