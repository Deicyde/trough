---
declaration: theorem
origin: cited
lean: Green61.green_61
statement: formalized
---

# Ben Green's Open Problem 61

> *Reference:* [Ben Green's Open Problem 61](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8 Problem 61)
>
> This problem was originally considered by Erdős and Newman.

*Quoted from [FormalConjectures/GreensOpenProblems/61.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/61.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green61.green_61`

Open: stated without proof.

> Suppose that $A + A$ contains the first $n$ squares. Is $|A| \geq n^{1 - o(1)}$?
>
> It is known that necessarily $|A| \geq n^{2/3 - o(1)}$, whilst in the other direction there do
> exist such $A$ with $|A| \ll_C n / \log^C n$ for any $C$.

```lean
theorem green_61 :
    ∃ f : ℕ → ℝ, Tendsto f atTop (𝓝 0) ∧
      ∀ n : ℕ, n ≥ 1 → ∀ (A : Finset ℕ),
        (Finset.Icc 1 n).image (· ^ 2) ⊆ A + A →
          (n : ℝ) ^ (1 - f n) ≤ A.card
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/61.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/61.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/61.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/61.lean)
- [https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8)
