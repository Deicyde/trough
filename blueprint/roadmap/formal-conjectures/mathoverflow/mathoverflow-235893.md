---
declaration: theorem
origin: cited
lean: Mathoverflow235893.mathoverflow_235893, Mathoverflow235893.mathoverflow_260589
statement: formalized
---

# Mathoverflow 235893

> *Reference:* [mathoverflow/235893](https://mathoverflow.net/questions/235893)
> asked by user [*Willie Wong*](https://mathoverflow.net/users/3948/willie-wong)

*Quoted from [FormalConjectures/Mathoverflow/235893.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/235893.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 6 test statements, counted here but not shown.

## `Mathoverflow235893.mathoverflow_235893`

Open: stated without proof.

> Assume for $n>1$, $f:\mathbb{R}^n\to\mathbb{R}^n$ is a bijection, where $\mathbb{R}^n$ is equipped
> with the standard topology. Does the connectedness of (the induced power set map) $f$ imply
> that of $f^{-1}$?

```lean
theorem mathoverflow_235893 :
    ∀ n > 1, ∀ (f : ℝ^n ≃ ℝ^n), IsConnectedMap f → IsConnectedMap f.symm
```

Category `research open`; AMS [26 Real functions](../by-subject/part-01/26-real-functions/README.md), [54 General topology](../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Mathoverflow/235893.lean, line 207](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/235893.lean#L207).

## `Mathoverflow235893.mathoverflow_260589`

Solved: stated here without proof.

> There exists a connected bijection ℝ → ℝ^2 where the inverse is not connected,
> proven in [mathoverflow/260589](https://mathoverflow.net/questions/260589) by user
> [Gro-Tsen](https://mathoverflow.net/users/17064/gro-tsen).

```lean
theorem mathoverflow_260589 :
    ∃ f : ℝ ≃ ℝ^2, IsConnectedMap f ∧ ¬ IsConnectedMap f.symm
```

Category `research solved`; AMS [26 Real functions](../by-subject/part-01/26-real-functions/README.md), [54 General topology](../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Mathoverflow/235893.lean, line 217](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/235893.lean#L217).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/235893.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/235893.lean)
- [mathoverflow/235893](https://mathoverflow.net/questions/235893)
