---
declaration: section
origin: cited
lean: MetaMathlibExt.nagell_ljunggren_cube_no_solution_of_mod_six_eq_five, MetaMathlibExt.nagell_ljunggren_cube_no_solution, MetaMathlibExt.nagell_ljunggren_solutions_of_conditions, MetaMathlibExt.nagell_ljunggren_exponent_structure, MetaMathlibExt.nagell_ljunggren_cube_of_five_dvd
statement: formalized
---

# Nagell–Ljunggren equation

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/nagell-ljunggren-equation/index.html).

## The Nagell–Ljunggren cube equation for $n \equiv 5 \pmod 6$

Let $n$ be a natural
number with $n \equiv 5 \pmod 6$. Then there are no integers $x$ and $y$ with
$x \equiv 2, 3, 5$ or $6 \pmod 9$ such that $x^n - 1 = (x - 1) y^3$. Since such an $x$ is not
$1$, this says that $(x^n - 1)/(x - 1) = y^3$ has no such integer solution.

## Sources

- Tran Duc Son, *A Note on the Nagell–Ljunggren Equation (xⁿ - 1)/(x - 1) = y³*, INTEGERS 26 (2026), Article A104, Theorem 2.

Stated but not proved: `MetaMathlibExt.nagell_ljunggren_cube_no_solution_of_mod_six_eq_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/NagellLjunggrenCubeResiduesWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NagellLjunggrenCubeResiduesWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/nagell-ljunggren-equation/index.html#nagell-ljunggren-cube-no-solution-of-mod).

## The Nagell–Ljunggren cube equation for $x \equiv 2, 3, 5, 6 \pmod 9$

Let $n \ge 3$ be a
natural number. Then there are no integers $x$ and $y$ with $x \equiv 2, 3, 5$ or $6 \pmod 9$
such that $x^n - 1 = (x - 1) y^3$. Since such an $x$ is not $1$, this says that
$(x^n - 1)/(x - 1) = y^3$ has no such integer solution.

The bound $n \ge 3$ is the classical range $n > 2$ of the Nagell–Ljunggren equation; for $n = 1$
every $x$ gives the solution $y = 1$.

## Sources

- Tran Duc Son, *A Note on the Nagell–Ljunggren Equation (xⁿ - 1)/(x - 1) = y³*, INTEGERS 26 (2026), Article A104, Corollary 1.

Stated but not proved: `MetaMathlibExt.nagell_ljunggren_cube_no_solution` is written with `theorem_wanted` in [WantedExt/NumberTheory/NagellLjunggrenCubeResiduesWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NagellLjunggrenCubeResiduesWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/nagell-ljunggren-equation/index.html#nagell-ljunggren-cube-no-solution).

## Ljunggren's theorem on the Nagell–Ljunggren equation

Let $x$ and $y$ be integers and
$n$ and $q$ natural numbers with $|x| > 1$, $y > 1$, $n > 2$ and $q \ge 2$, and suppose that
$x^n - 1 = (x - 1) y^q$, that is, $(x^n - 1)/(x - 1) = y^q$ (as $x \ne 1$). If $q = 2$, or
$3 \mid n$, or $4 \mid n$, or $q = 3$ and $n \not\equiv 5 \pmod 6$, then $(x, y, n, q)$ is one
of $(3, 11, 5, 2)$, $(7, 20, 4, 2)$, $(18, 7, 3, 3)$ and $(-19, 7, 3, 3)$.

## Sources

- Tran Duc Son, *A Note on the Nagell–Ljunggren Equation (xⁿ - 1)/(x - 1) = y³*, INTEGERS 26 (2026), Article A104, Theorem 1, quoting Ljunggren.

Stated but not proved: `MetaMathlibExt.nagell_ljunggren_solutions_of_conditions` is written with `theorem_wanted` in [WantedExt/NumberTheory/NagellLjunggrenCubeResiduesWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NagellLjunggrenCubeResiduesWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/nagell-ljunggren-equation/index.html#nagell-ljunggren-solutions-of-conditions).

## Structure of a further solution of the Nagell–Ljunggren equation

Let $x, y, n, q$ be
natural numbers with $x \ge 2$, $y \ge 2$, $n \ge 3$ and $q \ge 2$ such that
$(x^n - 1)/(x - 1) = y^q$, and suppose that $(x, y, n, q)$ is none of the known solutions
$(3, 11, 5, 2)$, $(7, 20, 4, 2)$ and $(18, 7, 3, 3)$. Then the least prime divisor of $n$ is at
least $29$, $n$ has at most four prime factors counted with multiplicity, $n$ is prime if
$q = 3$, and $n = q$ if $q \mid n$.

The source attributes the result to Bugeaud and Mihăilescu and to its references [2], [4].

## Sources

- Tran Duc Son, *On the Nagell--Ljunggren Equation \frac{x^{5}-1}{x-1}=y^{3}*, INTEGERS 26 (2026), Article A44, Theorem 2.

Stated but not proved: `MetaMathlibExt.nagell_ljunggren_exponent_structure` is written with `theorem_wanted` in [WantedExt/NumberTheory/NagellLjunggrenFiveCubeWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NagellLjunggrenFiveCubeWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/nagell-ljunggren-equation/index.html#nagell-ljunggren-exponent-structure).

## The Nagell–Ljunggren cube equation when $5 \mid n$

There are no natural numbers
$x \ge 2$, $y \ge 2$ and $n \ge 3$ with $5 \mid n$ such that $(x^n - 1)/(x - 1) = y^3$.

## Sources

- Tran Duc Son, *On the Nagell--Ljunggren Equation \frac{x^{5}-1}{x-1}=y^{3}*, INTEGERS 26 (2026), Article A44, Corollary 1.

Stated but not proved: `MetaMathlibExt.nagell_ljunggren_cube_of_five_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/NagellLjunggrenFiveCubeWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NagellLjunggrenFiveCubeWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/nagell-ljunggren-equation/index.html#nagell-ljunggren-cube-of-five-dvd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nagell–Ljunggren equation](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/nagell-ljunggren-equation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/nagell-ljunggren-equation)
