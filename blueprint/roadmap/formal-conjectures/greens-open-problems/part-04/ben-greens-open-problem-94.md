---
declaration: theorem
origin: cited
lean: Green94.green_94_outer_measure, Green94.green_94
statement: formalized
---

# Ben Green's Open Problem 94

> *Reference:*
> - [Ben Green's Open Problem 94](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.94)
> - [erdosproblems.com/120](https://www.erdosproblems.com/120)
> - [OAI26a] OpenAI, *The dyadic case of the Erdős similarity conjecture*.
>   OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/paper.pdf

*Quoted from [FormalConjectures/GreensOpenProblems/94.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/94.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `Green94.green_94_outer_measure`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/153d79d6c82c76fe1bee860742af800840c974d9/FormalConjectures/GreensOpenProblems/94.lean#L174](https://github.com/google-deepmind/formal-conjectures/blob/153d79d6c82c76fe1bee860742af800840c974d9/FormalConjectures/GreensOpenProblems/94.lean#L174).

> Let `A ⊂ R` be a set of positive outer measure. Does $A$ contain an affine copy of `{1, 1/2, 1/4, . . . }`?
>
> The answer is "no".

```lean
theorem green_94_outer_measure :
   ¬ ∀ A : Set ℝ,
   volume A > 0 →
   ∃ a b : ℝ, a ≠ 0 ∧ ∀ n : ℕ, a * (1 / 2^n) + b ∈ A
```

Category `research solved`; AMS [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/GreensOpenProblems/94.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/94.lean#L44).

## `Green94.green_94`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MeasureTheory/DyadicAvoidance/Main.lean#L103](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MeasureTheory/DyadicAvoidance/Main.lean#L103).

> Let `A ⊂ R` be a set of positive measure. Does $A$ contain an affine copy of `{1, 1/2, 1/4, . . . }`?
>
> The answer is "no": there are compact sets of measure arbitrarily close to $1$ in $[0, 1]$
> that contain no affine copy of $\{2^{-n} : n \geq 1\}$. This was proved by an internal OpenAI
> model in September 2026 [OAI26a]; see the linked Lean proof.

```lean
theorem green_94 :
   ¬ ∀ A : Set ℝ,
   MeasurableSet A ∧ volume A > 0 →
   ∃ a b : ℝ, a ≠ 0 ∧ ∀ n : ℕ, a * (1 / 2^n) + b ∈ A
```

Category `research solved`; AMS [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/GreensOpenProblems/94.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/94.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/94.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/94.lean)
- [Ben Green's Open Problem 94](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.94)
