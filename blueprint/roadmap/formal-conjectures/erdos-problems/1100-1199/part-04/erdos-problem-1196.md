---
declaration: theorem
origin: cited
lean: Erdos1196.erdos_1196
statement: formalized
---

# Erdős Problem 1196

> *Reference:* [erdosproblems.com/1196](https://www.erdosproblems.com/1196)

*Quoted from [FormalConjectures/ErdosProblems/1196.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1196.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1196](https://www.erdosproblems.com/1196).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1196.erdos_1196`

Solved: stated here; a Lean proof is at [https://github.com/math-inc/Erdos1196/blob/02fba13be7487cc51315f68d8fa7ef277633d3c8/PrimitiveSetsAboveX/FormalConjecturesErdos1196.lean](https://github.com/math-inc/Erdos1196/blob/02fba13be7487cc51315f68d8fa7ef277633d3c8/PrimitiveSetsAboveX/FormalConjecturesErdos1196.lean).

> Is it true that, for any $x$, if $A\subset [x,\infty)$ is a primitive set of integers (so that no distinct elements of $A$ divide each other) then
>
> $$\sum_{a\in A}\frac{1}{a\log a}< 1+o(1),$$
>
> where the $o(1)$ term $\to 0$ as $x\to \infty$?
> -

```lean
theorem erdos_1196 :
    ∃ o : ℕ → ℝ, o =o[Filter.atTop] (1 : ℕ → ℝ) ∧ ∀ x > (0 : ℕ), ∀ A ⊆ Set.Ici x, IsPrimitive A →
       ∑' (a : A), (1 / ((a.val : ℝ).log * a)) < 1 + o x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1196.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1196.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1196.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1196.lean)
- [erdosproblems.com/1196](https://www.erdosproblems.com/1196)
