---
declaration: theorem
origin: cited
lean: Erdos226.erdos_226
statement: formalized
---

# Erdős Problem 226

> *References:*
> - [erdosproblems.com/226](https://www.erdosproblems.com/226)
> - [BaSc70] Barth, K. F. and Schneider, W. J., *Entire functions mapping
>   countable dense subsets of the reals onto each other monotonically*.
>   J. London Math. Soc. (2) (1970), 620--626.
> - [BaSc71] Barth, K. F. and Schneider, W. J., *Entire functions mapping
>   arbitrary countable dense sets and their complements onto each other*.
>   J. London Math. Soc. (2) (1971/72), 482--488.
> - [Ha74] Hayman, W. K., *Research problems in function theory: new problems*.
>   (1974), 155--180.

*Quoted from [FormalConjectures/ErdosProblems/226.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/226.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/226](https://www.erdosproblems.com/226).

The file states 1 research or textbook statement: 1 solved.

## `Erdos226.erdos_226`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos226.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos226.lean).

> Is there an entire non-linear function $f$ such that, for all $x\in\mathbb{R}$, $x$ is rational if and only if $f(x)$ is?
>
> Barth and Schneider [BaSc70] proved the stronger result for countable dense subsets of
> $\mathbb{R}$.

```lean
theorem erdos_226 :
    ∃ F : ℂ → ℂ, Differentiable ℂ F ∧ (∀ x : ℝ, (F x).im = 0) ∧
      (∀ g : AffineMap ℝ ℝ ℝ, (fun x : ℝ => (F x).re) ≠ g) ∧
      PreservesRationality (fun x : ℝ => (F x).re)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/226.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/226.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/226.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/226.lean)
- [erdosproblems.com/226](https://www.erdosproblems.com/226)
