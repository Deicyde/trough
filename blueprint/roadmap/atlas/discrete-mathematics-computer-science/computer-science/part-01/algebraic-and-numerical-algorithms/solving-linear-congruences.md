---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver, Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_ret, Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_mem_iff, Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_nodup, Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_length, Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_empty_iff, Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_time_bounds
statement: formalized
proof: formalized
---

# Solving linear congruences

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences/index.html).

## Modular linear equation solver

Given natural numbers $a > 0$ and $n > 0$ and an integer
$b$, the solver solves $a x \equiv b \pmod{n}$ following CLRS. Let $d = \gcd(a, n)$ and let $y$ be
the coefficient of $a$ in the Bézout identity $d = n u + a y$ computed by the extended Euclidean
algorithm on $(n, a)$. If $d \mid b$, it returns the array $[x_0, x_1, \dots, x_{d-1}]$, where
$x_i = \bigl((y \cdot (b / d)) \bmod n + i \cdot (n / d)\bigr) \bmod n$ and $r \bmod n$ denotes the
least nonnegative residue of $r$; otherwise it returns the empty array.

Its cost is $6s + 1 + 4 + 3d$ when $d \mid b$ and $6s + 1$ otherwise, where $s$ is the number of
times the Euclidean algorithm, started from $(r, r') = (n, a)$, replaces $(r, r')$ by
$(r' \bmod r, r)$ before $r$ becomes $0$: six arithmetic operations per such step, one
divisibility test, four setup operations and three operations per returned residue.

Formalized by `Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver`, a definition declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences/index.html#modular-linear-equation-solver).

## Output of the modular linear equation solver

Let $a > 0$ and $n > 0$ be natural numbers,
$b$ an integer, $d = \gcd(a, n)$, and $y$ the coefficient of $a$ in the Bézout identity
$d = n u + a y$ computed by the extended Euclidean algorithm on $(n, a)$. If $d \mid b$, the list
returned by the modular linear equation solver on $a$, $b$, $n$ is $[x_0, x_1, \dots, x_{d-1}]$
with $x_i = \bigl((y \cdot (b / d)) \bmod n + i \cdot (n / d)\bigr) \bmod n$, where $r \bmod n$
denotes the least nonnegative residue of $r$; otherwise it is the empty list.

Formalized by `Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences/index.html#modular-linear-equation-solver-ret).

## The solver returns exactly the solutions below $n$

Let $a > 0$ and $n > 0$ be natural
numbers and $b$ an integer. A natural number $x$ occurs in the output of the modular linear
equation solver on $a$, $b$, $n$ if and only if $x < n$ and $a x \equiv b \pmod{n}$.

Formalized by `Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_mem_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences/index.html#modular-linear-equation-solver-mem-iff).

## The solver returns no repeated residues

For natural numbers $a > 0$ and $n > 0$ and an
integer $b$, the entries of the output of the modular linear equation solver on $a$, $b$, $n$ are
pairwise distinct.

Formalized by `Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences/index.html#modular-linear-equation-solver-nodup).

## Number of residues returned by the solver

For natural numbers $a > 0$ and $n > 0$ and an
integer $b$, the output of the modular linear equation solver on $a$, $b$, $n$ has $\gcd(a, n)$
entries if $\gcd(a, n)$ divides $b$, and no entries otherwise.

Formalized by `Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_length`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences/index.html#modular-linear-equation-solver-length).

## The solver returns nothing exactly when $\gcd(a, n) \nmid b$

For natural numbers $a > 0$
and $n > 0$ and an integer $b$, the modular linear equation solver on $a$, $b$, $n$ returns the
empty array if and only if $\gcd(a, n)$ does not divide $b$.

Formalized by `Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_empty_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences/index.html#modular-linear-equation-solver-empty-iff).

## Cost bounds for the modular linear equation solver

Let $a > 0$ and $n > 0$ be natural
numbers, $b$ an integer and $d = \gcd(a, n)$, and put $c = 4 + 3d$ if $d \mid b$ and $c = 0$
otherwise. The cost $T$ of the modular linear equation solver on $a$, $b$, $n$ satisfies
$1 + c \le T \le 6(2 \lfloor \log_2 n \rfloor + 2) + 1 + c$.

The cost counts arithmetic events, so this is the $O(\log n + \gcd(a, n))$ bound of the source.

Formalized by `Cslib.Algorithms.Lean.ModularLinearEquation.modularLinearEquationSolver_time_bounds`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/ModularLinearEquation.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences/index.html#modular-linear-equation-solver-time-boun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Solving linear congruences](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/solving-linear-congruences)
