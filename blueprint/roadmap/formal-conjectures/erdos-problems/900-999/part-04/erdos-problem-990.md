---
declaration: theorem
origin: cited
lean: Erdos990.erdos_990, Erdos990.erdos_990.variants.erdos_turan, Erdos990.erdos_990.variants.hayman, Erdos990.erdos_990.variants.counterexample
statement: formalized
---

# Erdős Problem 990

> *References:*
> - [erdosproblems.com/990](https://www.erdosproblems.com/990)
> - [APSSV26b] B. Alexeev, M. Putterman, M. Sawhney, M. Sellke, and G. Valiant, *Short proofs in
>   combinatorics, probability, and number theory II*. arXiv:2604.06609 (2026).
> - [ErTu50] Erdős, P. and Turán, P., *On the distribution of roots of polynomials*. Ann. of Math. (2)
>   (1950), 105-119.
> - [Ha72b] Hayman, W. K., *Angular value distribution of power series with gaps*. Proc. London Math.
>   Soc. (3) (1972), 590-624.

*Quoted from [FormalConjectures/ErdosProblems/990.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/990.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/990](https://www.erdosproblems.com/990).

The file states 4 research or textbook statements: 4 solved.

## `Erdos990.erdos_990`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos990.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos990.lean).

> Let $f=a_0+\cdots+a_dx^d\in \mathbb{C}[x]$ be a polynomial. Is it true that, if $f$ has roots
> $z_1,\ldots,z_d$ with corresponding arguments $\theta_1,\ldots,\theta_d\in [0,2\pi]$, then for all
> intervals $I\subseteq [0,2\pi]$
>
> $$
> \left\lvert (\# \theta_i \in I) - \frac{\lvert I\rvert}{2\pi}d\right\rvert \ll
> \left(n\log M\right)^{1/2},
> $$
>
> where $n$ is the number of non-zero coefficients of $f$ and
>
> $$
> M=\frac{\lvert a_0\rvert+\cdots +\lvert a_d\rvert}{(\lvert a_0\rvert\lvert a_d\rvert)^{1/2}}.
> $$
>
> An internal OpenAI model (see [APSSV26b]) has disproved the conjecture, constructing, for every
> $n\geq 1$, a polynomial $f$ with $n$ non-zero coefficients such that $M<3$ and with a positive real
> zero of multiplicity $n-1$, whence letting $I=[0,c/d]$ for a suitably small $c>0$,
>
> $$
> \left\lvert (\# \theta_i \in I) - \frac{\lvert I\rvert}{2\pi}d\right\rvert \geq n-1.
> $$

```lean
theorem erdos_990 :
    ¬ ∃ C : ℝ, ∀ f : ℂ[X], f.coeff 0 ≠ 0 → ∀ α β : ℝ, 0 ≤ α → α ≤ β → β ≤ 2 * π →
      |(rootArgCount f (Set.Icc α β) : ℝ) - (β - α) / (2 * π) * (f.natDegree : ℝ)| ≤
        C * Real.sqrt ((f.support.card : ℝ) * Real.log (M f))
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/990.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/990.lean#L80).

## `Erdos990.erdos_990.variants.erdos_turan`

Solved: stated here without proof.

> Erdős and Turán [ErTu50] proved such an upper bound with $n$ replaced by $d$.

```lean
theorem erdos_990.variants.erdos_turan :
    ∃ C : ℝ, ∀ f : ℂ[X], f.coeff 0 ≠ 0 → ∀ α β : ℝ, 0 ≤ α → α ≤ β → β ≤ 2 * π →
      |(rootArgCount f (Set.Icc α β) : ℝ) - (β - α) / (2 * π) * (f.natDegree : ℝ)| ≤
        C * Real.sqrt ((f.natDegree : ℝ) * Real.log (M f))
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/990.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/990.lean#L90).

## `Erdos990.erdos_990.variants.hayman`

Solved: stated here without proof.

> Hayman [Ha72b] proved
>
> $$
> \left\lvert (\# \theta_i \in I) - \frac{\lvert I\rvert}{2\pi}d\right\rvert \leq n-1,
> $$
>
> and noted this is essentially sharp since $f(x)=(x^{p}-1)^{n-1}$ has $n$ non-zero coefficients and
> has $1$ as a positive real zero of multiplicity $n-1$ (although for this $f$ the parameter $M$
> becomes very large).

```lean
theorem erdos_990.variants.hayman :
    ∀ f : ℂ[X], f.coeff 0 ≠ 0 → ∀ α β : ℝ, 0 ≤ α → α ≤ β → β ≤ 2 * π →
      |(rootArgCount f (Set.Icc α β) : ℝ) - (β - α) / (2 * π) * (f.natDegree : ℝ)| ≤
        (f.support.card : ℝ) - 1
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/990.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/990.lean#L106).

## `Erdos990.erdos_990.variants.counterexample`

Solved: stated here without proof.

> An internal OpenAI model (see [APSSV26b]) has disproved the conjecture, constructing, for every
> $n\geq 1$, a polynomial $f$ with $n$ non-zero coefficients such that $M<3$ and with a positive real
> zero of multiplicity $n-1$.

```lean
theorem erdos_990.variants.counterexample :
    ∀ n : ℕ, 1 ≤ n → ∃ f : ℂ[X], f.coeff 0 ≠ 0 ∧ f.support.card = n ∧ M f < 3 ∧
      ∃ x : ℝ, 0 < x ∧ f.rootMultiplicity (x : ℂ) = n - 1
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/990.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/990.lean#L118).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/990.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/990.lean)
- [erdosproblems.com/990](https://www.erdosproblems.com/990)
