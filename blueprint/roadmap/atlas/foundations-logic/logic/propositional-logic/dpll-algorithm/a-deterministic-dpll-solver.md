---
declaration: section
origin: cited
lean: Cslib.Algorithms.SAT.DPLL.firstUnit, Cslib.Algorithms.SAT.DPLL.firstVariable, Cslib.Algorithms.SAT.DPLL.clauseSatisfied, Cslib.Algorithms.SAT.DPLL.formulaSatisfied, Cslib.Algorithms.SAT.DPLL.decideWithFuel, Cslib.Algorithms.SAT.DPLL.dpll
statement: formalized
proof: formalized
---

# A deterministic DPLL solver

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/a-deterministic-dpll-solver/index.html).

## First unit literal

For a CNF formula $\varphi$, read as a list of clauses, this returns
the literal $\ell$ of the first clause of $\varphi$ that consists of the single literal $\ell$,
and returns nothing when no clause of $\varphi$ has exactly one literal.

Formalized by `Cslib.Algorithms.SAT.DPLL.firstUnit`, a definition declared in [CSLibExt/Algorithms/SAT/DPLL/Solver.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/DPLL/Solver.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/a-deterministic-dpll-solver/index.html#first-unit).

## First variable of a CNF formula

For a CNF formula $\varphi$, read as a list of clauses,
this returns the variable of the first literal of the first nonempty clause of $\varphi$, that
is, the first variable occurring in $\varphi$ in source order, and returns nothing when every
clause of $\varphi$ is empty (in particular when $\varphi$ has no clauses).

Formalized by `Cslib.Algorithms.SAT.DPLL.firstVariable`, a definition declared in [CSLibExt/Algorithms/SAT/DPLL/Solver.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/DPLL/Solver.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/a-deterministic-dpll-solver/index.html#first-variable).

## Boolean clause satisfaction check

For an assignment $v$ of Boolean values to the
variables $0, 1, 2, \ldots$ and a clause $C$, whose literals are pairs $(x, b)$ of a variable
$x$ and a polarity $b$, this Boolean is true exactly when some literal $(x, b)$ of $C$ satisfies
$v(x) = b$.

Formalized by `Cslib.Algorithms.SAT.DPLL.clauseSatisfied`, a definition declared in [CSLibExt/Algorithms/SAT/DPLL/Solver.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/DPLL/Solver.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/a-deterministic-dpll-solver/index.html#clause-satisfied).

## Boolean formula satisfaction check

For an assignment $v$ of Boolean values to the
variables $0, 1, 2, \ldots$ and a CNF formula $\varphi$, this Boolean is true exactly when every
clause of $\varphi$ passes the Boolean clause satisfaction check for $v$, that is, every clause
contains a literal $(x, b)$ with $v(x) = b$.

Formalized by `Cslib.Algorithms.SAT.DPLL.formulaSatisfied`, a definition declared in [CSLibExt/Algorithms/SAT/DPLL/Solver.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/DPLL/Solver.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/a-deterministic-dpll-solver/index.html#formula-satisfied).

## DPLL with a fuel budget

Given a natural number $n$ (the fuel) and a CNF formula
$\varphi$, the procedure returns a Boolean value. Literals are pairs $(x, b)$ of a variable $x$
and a polarity $b$. With fuel $0$ the procedure returns true exactly when $\varphi$ has no
clauses. With fuel $n + 1$ it returns true if $\varphi$ has no clauses, and otherwise returns
false if some clause of $\varphi$ is empty. Otherwise, if some clause of $\varphi$ consists of
a single literal, it takes the first such literal $\ell$ in source order and returns the result
of the procedure with fuel $n$ on the restriction of $\varphi$ by $\ell$. Otherwise, if some
variable occurs in $\varphi$, it takes the first such variable $x$ in source order and returns
true exactly when the procedure with fuel $n$ returns true on the restriction of $\varphi$ by
$(x, \mathrm{true})$ or on the restriction of $\varphi$ by $(x, \mathrm{false})$; if no variable
occurs, it returns false.

The restriction of $\varphi$ by a literal $(x, b)$ deletes every clause containing $(x, b)$ and
removes every literal with variable $x$ from the remaining clauses. A decision branches on both
polarities, a unit literal gives a single recursive call, and no satisfying assignment is
returned.

Formalized by `Cslib.Algorithms.SAT.DPLL.decideWithFuel`, a definition declared in [CSLibExt/Algorithms/SAT/DPLL/Solver.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/DPLL/Solver.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/a-deterministic-dpll-solver/index.html#decide-with-fuel).

## The DPLL procedure

On a CNF formula $\varphi$, the DPLL procedure runs DPLL with fuel
equal to the number of distinct variables occurring in $\varphi$ and returns its Boolean result.

Formalized by `Cslib.Algorithms.SAT.DPLL.dpll`, a definition declared in [CSLibExt/Algorithms/SAT/DPLL/Solver.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/SAT/DPLL/Solver.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/a-deterministic-dpll-solver/index.html#dpll).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: A deterministic DPLL solver](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/dpll-algorithm/a-deterministic-dpll-solver/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/dpll-algorithm/a-deterministic-dpll-solver)
