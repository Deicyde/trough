---
declaration: theorem
origin: cited
lean: DirichletDivisorProblem.divisor_error_dirichlet, DirichletDivisorProblem.dirichlet_divisor_problem, DirichletDivisorProblem.divisor_error_hardy
statement: formalized
---

# Dirichlet divisor problem

> Let $d(n)$ be the number of divisors of $n$ and $D(x) = \sum_{n \le x} d(n)$ the divisor
> summatory function. Dirichlet's hyperbola method gives
>
> $$D(x) = x \log x + (2\gamma - 1) x + \Delta(x), \qquad \Delta(x) = O(x^{1/2}),$$
>
> where $\gamma$ is the Euler–Mascheroni constant. The **Dirichlet divisor problem** asks for the
> infimum $\theta$ of exponents with $\Delta(x) = O(x^{\theta})$. It is conjectured that
> $\theta = 1/4$, i.e. $\Delta(x) = O(x^{1/4 + \varepsilon})$ for every $\varepsilon > 0$. Hardy
> showed $\theta \ge 1/4$, so the conjecture would be sharp. Huxley's bound
> $\theta \le 131/416 \approx 0.3149$ [Hu03] is now historical: the best known upper bound is
> $\theta \le 0.314483\ldots$, due to Li and Yang [LY23]. The problem remains open.
>
> *References:*
> - [Wikipedia: Divisor summatory function](https://en.wikipedia.org/wiki/Divisor_summatory_function)
> - [Wikipedia: Dirichlet divisor problem](https://en.wikipedia.org/wiki/Divisor_summatory_function#Dirichlet's_divisor_problem)
> - [Di49] P. G. L. Dirichlet, *Über die Bestimmung der mittleren Werthe in der Zahlentheorie*,
>   Abhandl. Königl. Preuss. Akad. Wiss. (1849), 69-83.
> - [Ha16] G. H. Hardy, *On Dirichlet's divisor problem*, Proc. London Math. Soc. (1916), 1-25.
> - [Hu03] M. N. Huxley, *Exponential sums and lattice points III*, Proc. London Math. Soc.
>   (2003), 591-609.
> - [LY23] X. Li, X. Yang, *An improvement on Gauss's circle problem and Dirichlet's divisor
>   problem*, [arXiv:2308.14859](https://arxiv.org/abs/2308.14859) (2023), Theorem 1.2.

*Quoted from [FormalConjectures/Wikipedia/DirichletDivisorProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DirichletDivisorProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result. It also has 1 test statement, counted here but not shown.

## `DirichletDivisorProblem.divisor_error_dirichlet`

Textbook result, stated without proof.

> Dirichlet's bound [Di49]: $\Delta(x) = O(x^{1/2})$.

```lean
theorem divisor_error_dirichlet :
    divisorError =O[atTop] fun x => Real.sqrt x
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DirichletDivisorProblem.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DirichletDivisorProblem.lean#L70).

## `DirichletDivisorProblem.dirichlet_divisor_problem`

Open: stated without proof.

> The Dirichlet divisor problem: is it true that $\Delta(x) = O(x^{1/4 + \varepsilon})$ for every
> $\varepsilon > 0$? (Equivalently, is the infimum of admissible exponents equal to $1/4$?)

```lean
theorem dirichlet_divisor_problem :
    ∀ ε > (0 : ℝ), divisorError =O[atTop] fun x => x ^ ((1 : ℝ) / 4 + ε)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DirichletDivisorProblem.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DirichletDivisorProblem.lean#L79).

## `DirichletDivisorProblem.divisor_error_hardy`

Solved: stated here without proof.

> Hardy's lower bound [Ha16]: $\Delta(x)$ is not $o(x^{1/4})$, so the exponent $1/4$ in the
> Dirichlet divisor problem cannot be improved.

```lean
theorem divisor_error_hardy :
    ¬ (divisorError =o[atTop] fun x => x ^ ((1 : ℝ) / 4))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DirichletDivisorProblem.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DirichletDivisorProblem.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/DirichletDivisorProblem.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DirichletDivisorProblem.lean)
- [Wikipedia: Divisor summatory function](https://en.wikipedia.org/wiki/Divisor_summatory_function)
