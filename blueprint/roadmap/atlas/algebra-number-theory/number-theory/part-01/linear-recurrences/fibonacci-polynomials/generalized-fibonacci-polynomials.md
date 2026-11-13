---
declaration: section
origin: cited
lean: MetaMathlibExt.generalizedFibonacciPolynomial, MetaMathlibExt.generalizedFibonacciPolynomial_zero, MetaMathlibExt.generalizedFibonacciPolynomial_one, MetaMathlibExt.generalizedFibonacciPolynomial_add_two
statement: formalized
proof: formalized
---

# Generalized Fibonacci polynomials

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/generalized-fibonacci-polynomials/index.html).

## Generalized Fibonacci polynomials

Given polynomials $p_0, p_1, d, g \in \mathbb{Z}[X]$,
the generalized Fibonacci polynomial sequence $(G_n)_{n \ge 0}$ in $\mathbb{Z}[X]$ is defined by
$G_0 = p_0$, $G_1 = p_1$ and $G_{n+2} = d \, G_{n+1} + g \, G_n$ for every natural number $n$.

Formalized by `MetaMathlibExt.generalizedFibonacciPolynomial`, a definition declared in [MathlibExt/NumberTheory/GeneralizedFibonacciPolynomial.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibonacciPolynomial.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/generalized-fibonacci-polynomials/index.html#generalized-fibonacci-polynomial).

## Index-zero term of a generalized Fibonacci polynomial sequence

For all polynomials
$p_0, p_1, d, g \in \mathbb{Z}[X]$, the generalized Fibonacci polynomial sequence $(G_n)$ with
initial terms $p_0, p_1$ and recurrence coefficients $d, g$ has $G_0 = p_0$.

Formalized by `MetaMathlibExt.generalizedFibonacciPolynomial_zero`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibonacciPolynomial.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibonacciPolynomial.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/generalized-fibonacci-polynomials/index.html#generalized-fibonacci-polynomial-zero).

## Index-one term of a generalized Fibonacci polynomial sequence

For all polynomials
$p_0, p_1, d, g \in \mathbb{Z}[X]$, the generalized Fibonacci polynomial sequence $(G_n)$ with
initial terms $p_0, p_1$ and recurrence coefficients $d, g$ has $G_1 = p_1$.

Formalized by `MetaMathlibExt.generalizedFibonacciPolynomial_one`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibonacciPolynomial.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibonacciPolynomial.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/generalized-fibonacci-polynomials/index.html#generalized-fibonacci-polynomial-one).

## Recurrence for generalized Fibonacci polynomials

For all polynomials $p_0, p_1, d, g$
in $\mathbb{Z}[X]$ and every natural number $n$, the generalized Fibonacci polynomial sequence
$(G_m)$ with initial terms $p_0, p_1$ and recurrence coefficients $d, g$ satisfies
$G_{n+2} = d \, G_{n+1} + g \, G_n$.

Formalized by `MetaMathlibExt.generalizedFibonacciPolynomial_add_two`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibonacciPolynomial.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibonacciPolynomial.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/generalized-fibonacci-polynomials/index.html#generalized-fibonacci-polynomial-add-two).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Fibonacci polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/generalized-fibonacci-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/generalized-fibonacci-polynomials)
