---
declaration: theorem
origin: cited
lean: Erdos942.erdos_942, Erdos942.erdos_942.variants.limsup, Erdos942.erdos_942.variants.density
statement: formalized
---

# Erdős Problem 942

> *Reference:* [erdosproblems.com/942](https://www.erdosproblems.com/942)

*Quoted from [FormalConjectures/ErdosProblems/942.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/942.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/942](https://www.erdosproblems.com/942).

The file states 3 research or textbook statements: 1 open and 2 textbook results.

## `Erdos942.erdos_942`

Open: stated without proof.

> Is there some constant $c > 0$ such that $h(n) < (\log n)^{c + o(1)}$ and, for infinitely many $n$,
> $h(n) > (\log n)^{c - o(1)}$.

```lean
theorem erdos_942 : ∃ c > 0, ∃ (o : ℕ → ℝ), o =o[atTop] (1 : ℕ → ℝ) ∧
    (∀ᶠ n in atTop, erdos_942.h n < (Real.log n) ^ (c + o n)) ∧
    {n | erdos_942.h n > (Real.log n) ^ (c - o n)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/942.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/942.lean#L42).

## `Erdos942.erdos_942.variants.limsup`

Textbook result, stated without proof.

> It is not hard to prove that $\limsup h(n) = \infty$.

```lean
theorem erdos_942.variants.limsup :
    atTop.limsup (((fun (n : ℕ) ↦ (n : ℕ∞)) ∘ erdos_942.h)) = ⊤
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/942.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/942.lean#L51).

## `Erdos942.erdos_942.variants.density`

Textbook result, stated without proof.

> It is not hard to prove that the density $\delta_l$ of integers for which $h(n) = l$ exists
> and satisfies
>
> $$\sum_l \delta_l = 1$$
>
> .

```lean
theorem erdos_942.variants.density :
    ∃ δ : ℕ → ℝ, ∀ l, {n | erdos_942.h n = l}.HasDensity (δ l) ∧
    ∑' l, δ l = 1
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/942.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/942.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/942.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/942.lean)
- [erdosproblems.com/942](https://www.erdosproblems.com/942)
