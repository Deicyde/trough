---
declaration: theorem
origin: cited
lean: Erdos1003.erdos_1003, Erdos1003.erdos_1003.variants.Icc, Erdos1003.erdos_1003.variants.eps87
statement: formalized
---

# Erdős Problem 1003

> *Reference:* [erdosproblems.com/1003](https://www.erdosproblems.com/1003)

*Quoted from [FormalConjectures/ErdosProblems/1003.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1003.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1003](https://www.erdosproblems.com/1003).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos1003.erdos_1003`

Open: stated without proof.

> Are there infinitely many solutions to $\phi(n) = \phi(n+1)$, where $\phi$ is the Euler totient
> function?

```lean
theorem erdos_1003 : Set.Infinite {n | φ n = φ (n + 1)}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1003.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1003.lean#L38).

## `Erdos1003.erdos_1003.variants.Icc`

Open: stated without proof.

> Erdős [Er85e] says that, presumably, for every $k \geq 1$ the equation
>
> $$\phi(n) = \phi(n+1) = \cdots = \phi (n+k)$$
>
> has infinitely many solutions.
>
> [Er85e] Erdős, P., _Some problems and results in number theory_. Number theory and combinatorics. Japan 1984 (Tokyo, Okayama and Kyoto, 1984) (1985), 65-87.

```lean
theorem erdos_1003.variants.Icc :
    ∀ k ≥ 1, {n | ∀ i ∈ Set.Icc 1 k, φ n = φ (n + i)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1003.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1003.lean#L48).

## `Erdos1003.erdos_1003.variants.eps87`

Solved: stated here without proof.

> Erdős, Pomerance, and Sárközy [EPS87] proved that for all large $x$, the number
> of $n \leq x$ with $\phi(n) = \phi(n+1)$ is at most
>
> $$\frac{x}{\exp((\log x)^{1/3})}$$
>
> .
>
> [EPS87] Erd\H os, Paul and Pomerance, Carl and S\'ark\"ozy, Andr\'as, _On locally repeated values of certain arithmetic functions_. {II}. Proc. Amer. Math. Soc. (1987), 1--7.

```lean
theorem erdos_1003.variants.eps87 :  ∀ᶠ x in atTop,
    {(n : ℕ) | (n ≤ x) ∧ φ n = φ (n + 1)}.ncard ≤
      x / Real.exp ((x.log) ^ ((1 : ℝ) / 3))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1003.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1003.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1003.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1003.lean)
- [erdosproblems.com/1003](https://www.erdosproblems.com/1003)
