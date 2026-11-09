---
declaration: theorem
origin: cited
lean: Erdos503.erdos_503, Erdos503.erdos_503.variants.R2, Erdos503.erdos_503.variants.R3, Erdos503.erdos_503.variants.upper_bound, Erdos503.erdos_503.variants.lower_bound
statement: formalized
---

# Erdős Problem 503

> *Reference:* [erdosproblems.com/503](https://www.erdosproblems.com/503)

*Quoted from [FormalConjectures/ErdosProblems/503.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/503.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/503](https://www.erdosproblems.com/503).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos503.erdos_503`

Open: stated without proof.

> What is the size of the largest $A \subseteq \mathbb{R}^n$ such that every three points from $A$
> determine an isosceles triangle? That is, for any three points $x$, $y$, $z$ from $A$, at least two
> of the distances $|x - y|$, $|y - z|$, $|x - z|$ are equal.

```lean
theorem erdos_503 (n : ℕ) :
    IsGreatest {(A.ncard) | (A : Set (ℝ^n)) (hA : A.IsIsosceles)} erdos_503.answer
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/503.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/503.lean#L40).

## `Erdos503.erdos_503.variants.R2`

Solved: stated here without proof.

> When $n = 2$, the answer is 6 (due to Kelly [ErKe47] - an alternative proof is given by Kovács [Ko24c]).
>
> [ErKe47] Erdős, Paul and Kelly, L. M., Elementary Problems and Solutions: Solutions: E735. Amer. Math. Monthly (1947), 227-229.
> [Ko24c] Z. Kovács, A note on Erdős's mysterious remark. arXiv:2412.05190 (2024).

```lean
theorem erdos_503.variants.R2 :
    IsGreatest {(A.ncard) | (A : Set ℝ²) (hA : A.IsIsosceles)} 6
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/503.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/503.lean#L51).

## `Erdos503.erdos_503.variants.R3`

Solved: stated here without proof.

> When $n = 3$, the answer is 8 (due to Croft [Cr62]).
>
> [Cr62] Croft, H. T., $9$-point and $7$-point configurations in $3$-space. Proc. London Math. Soc. (3) (1962), 400-424.

```lean
theorem erdos_503.variants.R3 :
    IsGreatest {(A.ncard) | (A : Set ℝ³) (hA : A.IsIsosceles)} 8
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/503.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/503.lean#L61).

## `Erdos503.erdos_503.variants.upper_bound`

Solved: stated here without proof.

> The best upper bound known in general is due to Blokhius [Bl84] who showed that
> $$
> |A| \leq \binom{n + 2}{2}
> $$
>
> [Bl84] Blokhuis, A., Few-distance sets. (1984), iv+70.

```lean
theorem erdos_503.variants.upper_bound (n : ℕ) :
    ∀ m ∈ {(A.ncard) | (A : Set (ℝ^n)) (hA : A.IsIsosceles)}, m ≤ (n + 2).choose 2
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/503.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/503.lean#L74).

## `Erdos503.erdos_503.variants.lower_bound`

Solved: stated here without proof.

> Alweiss has observed a lower bound of $\binom{n + 1}{2}$ follows from considering the subset of
> $\mathbb{R}^{n + 1}$ formed of all vectors $e_i + e_j$ where $e_i$, $e_j$ are distinct coordinate
> vectors. This set can be viewed as a subset of some $\mathbb{R}^n$, and is easily checked to have
> the required property.
>
> The bound is stated as the existence of such a set and not as a bound on the `sSup` of the sizes:
> in `ℕ` the `sSup` of an unbounded set is `0`, so the latter would also assert that the sizes are
> bounded, which is the content of `erdos_503.variants.upper_bound`.

```lean
theorem erdos_503.variants.lower_bound (n : ℕ) :
    ∃ m ∈ {(A.ncard) | (A : Set (ℝ^n)) (hA : A.IsIsosceles)}, (n + 1).choose 2 ≤ m
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/503.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/503.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/503.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/503.lean)
- [erdosproblems.com/503](https://www.erdosproblems.com/503)
