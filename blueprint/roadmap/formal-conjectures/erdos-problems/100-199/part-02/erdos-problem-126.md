---
declaration: theorem
origin: cited
lean: Erdos126.erdos_126, Erdos126.erdos_126.variants.IsBigO, Erdos126.erdos_126.variants.isLittleO
statement: formalized
---

# Erdős Problem 126

> *Reference:* [erdosproblems.com/126](https://www.erdosproblems.com/126)

*Quoted from [FormalConjectures/ErdosProblems/126.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/126.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/126](https://www.erdosproblems.com/126).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos126.erdos_126`

Solved: stated here; a Lean proof is at [https://github.com/tadamcz/erdos126/blob/2516785fe6bbc43e979cf6029c976d9f998a7fba/Erdos126/Resolutions/Erdos126_132usd_25h.lean#L3053](https://github.com/tadamcz/erdos126/blob/2516785fe6bbc43e979cf6029c976d9f998a7fba/Erdos126/Resolutions/Erdos126_132usd_25h.lean#L3053).

> Let $f(n)$ be maximal such that if $A\subseteq\mathbb{N}$ has $|A| = n$ then
> $\prod_{a\neq b\in A}(a + b)$ has at least $f(n)$ distinct prime factors.
> Is it true that $\frac{f(n)}{\log n} \to\infty$?
>
> The answer is yes, and a machine-checked proof is available.

```lean
theorem erdos_126 : ∀ (f : ℕ → ℕ), IsMaximalAddFactorsCard f →
    Tendsto (fun n => f n / Real.log n) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/126.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/126.lean#L48).

## `Erdos126.erdos_126.variants.IsBigO`

Solved: stated here without proof.

> Erdős and Turán proved [ErTu34] in their first joint paper that
> $$
>   \log n \ll f(n) \ll \frac{n}{\log n}
> $$
>
> [ErTu34] Erdős, Paul and Turan, Paul, _On a Problem in the Elementary Theory of Numbers_. Amer. Math. Monthly (1934), 608-611.

```lean
theorem erdos_126.variants.IsBigO
    (f : ℕ → ℕ)
    (hf : IsMaximalAddFactorsCard f) :
    ((fun (n : ℕ) => Real.log n) =O[atTop] fun (n : ℕ) => (f n : ℝ)) ∧
      (fun (n : ℕ) => (f n : ℝ)) =O[atTop] fun (n : ℕ) => n / Real.log n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/126.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/126.lean#L61).

## `Erdos126.erdos_126.variants.isLittleO`

Open: stated without proof.

> Erdős says that $f(n) = o(\frac{n}{\log n})$ has never been proved.

```lean
theorem erdos_126.variants.isLittleO
    (f : ℕ → ℕ)
    (hf : IsMaximalAddFactorsCard f) :
    (fun (n : ℕ) => (f n : ℝ)) =o[atTop] (fun (n : ℕ) => n / Real.log n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/126.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/126.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/126.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/126.lean)
- [erdosproblems.com/126](https://www.erdosproblems.com/126)
