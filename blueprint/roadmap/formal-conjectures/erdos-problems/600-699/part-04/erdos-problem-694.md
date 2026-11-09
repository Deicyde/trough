---
declaration: theorem
origin: cited
lean: Erdos694.erdos_694, Erdos694.erdos_694.variants.carmichael, Erdos694.erdos_694.variants.inf_unique
statement: formalized
---

# Erdős Problem 694

> *Reference:* [erdosproblems.com/694](https://www.erdosproblems.com/694)

*Quoted from [FormalConjectures/ErdosProblems/694.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/694.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/694](https://www.erdosproblems.com/694).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos694.erdos_694`

Solved: stated here without proof.

> Let $f_\max(n)$ be the largest $m$ such that $\phi(m) = n$, and
> $f_\min(n)$ be the smallest such $m$, where $\phi$ is Euler's
> totient function. Investigate
>
> $$
>   \max_{n\leq x}\frac{f_\max(n)}{f_\min(n)}.
> $$
>
> GPT-5.5 Pro (prompted by Price) has proved (see also the comments for a summary) that
>
> $$
> \max_{n\leq x}\frac{f_{\max}(n)}{f_{\min}(n)}=(e^\gamma+o(1))\log\log x.
> $$
>
> A Lean formalisation of the reduction exists, conditional on Mertens' product theorem and
> Linnik's theorem; see the
> [formal proof](https://github.com/Shashi456/erdos-formalizations/blob/main/Erdos/P694/Proof.lean).
>
> The extrema are only required on nonempty fibres of the totient (values such as $3$ have no
> preimage), and the identity is asked for sufficiently large $x$: at $x = 1$ the maximum is
> $f_\max(1) / f_\min(1) = 2$ while $\log \log 1 = 0$.

```lean
theorem erdos_694 : ∀ᵉ (fmax : ℕ → ℕ) (fmin : ℕ → ℕ),
      (∀ n, (∃ m, Nat.totient m = n) → IsGreatest (Nat.totient ⁻¹' {n}) (fmax n)) →
      (∀ n, (∃ m, Nat.totient m = n) → IsLeast (Nat.totient ⁻¹' {n}) (fmin n)) →
      ∃ o : ℕ → ℝ, Tendsto o atTop (𝓝 0) ∧
        ∀ᶠ x : ℕ in atTop,
          sSup { (fmax n : ℝ) / fmin n | (n : ℕ) (_ : n ≤ x) (_ : ∃ m, Nat.totient m = n) } =
            (exp eulerMascheroniConstant + o x) * log (log (x : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/694.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/694.lean#L54).

## `Erdos694.erdos_694.variants.carmichael`

Open: stated without proof.

> Carmichael has asked whether there is an integer $n$ for which $\phi(m) = n$ has
> exactly one solution, that is $\frac{f_\max(n)}{f_\min(n)} = 1$.

```lean
theorem erdos_694.variants.carmichael :
    ∃ n > 0, ∃! m, Nat.totient m = n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/694.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/694.lean#L68).

## `Erdos694.erdos_694.variants.inf_unique`

Solved: stated here without proof.

> Erdős has proved that if there exists an integer $n$ for which $\phi(m) = n$ has
> exactly one solution, then there must be infinitely many such $n$.

```lean
theorem erdos_694.variants.inf_unique (h : ∃ n > 0, ∃! m, Nat.totient m = n) :
    { n | ∃! m, Nat.totient m = n }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/694.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/694.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/694.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/694.lean)
- [erdosproblems.com/694](https://www.erdosproblems.com/694)
