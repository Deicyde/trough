---
declaration: theorem
origin: cited
lean: Erdos624.erdos_624
statement: formalized
---

# Erdős Problem 624

> *Reference:* [erdosproblems.com/624](https://www.erdosproblems.com/624)

*Quoted from [FormalConjectures/ErdosProblems/624.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/624.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/624](https://www.erdosproblems.com/624).

The file states 1 research or textbook statement: 1 open.

## `Erdos624.erdos_624`

Open: stated without proof.

> Let $X$ be a finite set of size $n$ and $H(n)$ be such that there is a function
> $f:\{A : A\subseteq X\}\to X$ so that for every $Y\subseteq X$ with $\lvert Y\rvert \geq H(n)$
> we have $\left\{ f(A) : A\subseteq Y\right\}=X$.
> Prove that $H(n)-\log_2 n \to \infty$.

```lean
theorem erdos_624 :
    atTop.Tendsto (fun n : ℕ => H n - Real.logb 2 (n : ℝ)) atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/624.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/624.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/624.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/624.lean)
- [erdosproblems.com/624](https://www.erdosproblems.com/624)
