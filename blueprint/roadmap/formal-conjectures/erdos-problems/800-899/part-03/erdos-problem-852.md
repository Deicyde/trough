---
declaration: theorem
origin: cited
lean: Erdos852.erdos_852.parts.i, Erdos852.erdos_852.parts.ii, Erdos852.erdos_852.variants.tendsto_atTop
statement: formalized
---

# Erdős Problem 852

> *References:*
> - [erdosproblems.com/852](https://www.erdosproblems.com/852)
> - [Er85c] Erdős, P., *On some of my problems in number theory I would most like to see solved*.
>   Number theory (Ootacamund, 1984) (1985), 74-84.
> - [A001223](https://oeis.org/A001223)
> - [A053597](https://oeis.org/A053597)
> - [A078515](https://oeis.org/A078515)

*Quoted from [FormalConjectures/ErdosProblems/852.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/852.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/852](https://www.erdosproblems.com/852).

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 2 test statements, counted here but not shown.

## `Erdos852.erdos_852.parts.i`

Open: stated without proof.

> Let $d_n = p_{n+1} - p_n$, where $p_n$ is the $n$th prime. Let $h(x)$ be maximal such that for
> some $n < x$ the numbers $d_n, d_{n+1}, \ldots, d_{n+h(x)-1}$ are all distinct [Er85c]. Estimate
> $h(x)$. In particular, is it true that
> $$h(x) > (\log x)^c$$
> for some constant $c > 0$?
>
> The statement avoids defining $h$. Since $h(x)$ is the longest such run, $h(x) > y$ holds exactly
> when some $n < x$ starts a run of $H > y$ distinct gaps. We state the question this way, with $x$
> real. We read it as asking for one $c > 0$ such that the inequality holds for all large $x$.
>
> The primes are indexed from $p_0 = 2$, as in `primeGap`. Shifting the index by one does not change
> the question.

```lean
theorem erdos_852.parts.i :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ x : ℝ in atTop,
      ∃ n : ℕ, (n : ℝ) < x ∧ ∃ H : ℕ, (Real.log x) ^ c < (H : ℝ) ∧ DistinctGapRun n H
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/852.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/852.lean#L81).

## `Erdos852.erdos_852.parts.ii`

Open: stated without proof.

> Let $d_n = p_{n+1} - p_n$, where $p_n$ is the $n$th prime. Let $h(x)$ be maximal such that for
> some $n < x$ the numbers $d_n, d_{n+1}, \ldots, d_{n+h(x)-1}$ are all distinct [Er85c]. Estimate
> $h(x)$. In particular, is it true that
> $$h(x) = o(\log x)?$$
>
> The statement avoids defining $h$. It says that for every $\varepsilon > 0$ and all large real $x$,
> every run of $H$ distinct gaps $d_n, \ldots, d_{n+H-1}$ with $n < x$ satisfies
> $H \leq \varepsilon \log x$. This is $h(x) \leq \varepsilon \log x$, because $h(x)$ is the longest
> such run.
>
> The indexing is as in `Erdos852.erdos_852.parts.i`.

```lean
theorem erdos_852.parts.ii :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ x : ℝ in atTop,
      ∀ n : ℕ, (n : ℝ) < x → ∀ H : ℕ, DistinctGapRun n H → (H : ℝ) ≤ ε * Real.log x
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/852.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/852.lean#L100).

## `Erdos852.erdos_852.variants.tendsto_atTop`

Solved: stated here without proof.

> Brun's sieve implies $h(x) \to \infty$ as $x \to \infty$ (remark on
> [erdosproblems.com/852](https://www.erdosproblems.com/852)).
>
> That is, for every $H$ and all large $x$ there is some $n < x$ such that $d_n, \ldots, d_{n+H-1}$
> are all distinct. Since more values of $n$ are allowed as $x$ grows, this holds exactly when, for
> every $H$, some $n$ has $d_n, \ldots, d_{n+H-1}$ all distinct.
>
> This also follows from `Erdos6.erdos_6.variants.increasing`, because strictly increasing prime
> gaps are distinct.

```lean
theorem erdos_852.variants.tendsto_atTop :
    ∀ H : ℕ, ∀ᶠ x : ℝ in atTop, ∃ n : ℕ, (n : ℝ) < x ∧ DistinctGapRun n H
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/852.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/852.lean#L117).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/852.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/852.lean)
- [erdosproblems.com/852](https://www.erdosproblems.com/852)
