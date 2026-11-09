---
declaration: theorem
origin: cited
lean: Erdos100.erdos_100, Erdos100.erdos_100.variants.strong, Erdos100.erdos_100.variants.kanold, Erdos100.erdos_100.variants.guth_katz, Erdos100.erdos_100_piepmeyer
statement: formalized
---

# Erdős Problem 100

> *References:*
> * [erdosproblems.com/100](https://www.erdosproblems.com/100)
> * [Kanold\](No references found)
> * [GuKa15\](Guth, Larry and Katz, Nets Hawk, On the Erd\H{o}s distinct distances problem in the plane. Ann. of Math. (2) (2015), 155-190.)
> * [Piepmeyer\](No references found)

*Quoted from [FormalConjectures/ErdosProblems/100.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/100.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/100](https://www.erdosproblems.com/100).

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Erdos100.erdos_100`

Open: stated without proof.

> Is the diameter of $A$ at least $Cn$ for some constant $C > 0$?

```lean
theorem erdos_100 :
    ∃ C > (0 : ℝ), ∀ᶠ n in atTop, ∀ A : Finset ℝ²,
      A.card = n →
      DistancesSeparated A →
      diam (A : Set ℝ²) > C * n
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/100.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/100.lean#L44).

## `Erdos100.erdos_100.variants.strong`

Open: stated without proof.

> Stronger conjecture: diameter $\geq n - 1$ for sufficiently large $n$.

```lean
theorem erdos_100.variants.strong :
    ∀ᶠ n in atTop, ∀ A : Finset ℝ²,
      A.card = n →
      DistancesSeparated A →
      diam (A : Set ℝ²) ≥ n - 1
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/100.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/100.lean#L53).

## `Erdos100.erdos_100.variants.kanold`

Solved: stated here without proof.

> From [Kanold]: diameter $\geq n^{3/4}$.
> TODO: find reference

```lean
theorem erdos_100.variants.kanold :
    ∃ C > (0 : ℝ), ∀ᶠ n in atTop, ∀ A : Finset ℝ²,
      A.card = n →
      DistancesSeparated A →
      diam (A : Set ℝ²) ≥ (n : ℝ) ^ (3 / 4 : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/100.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/100.lean#L63).

## `Erdos100.erdos_100.variants.guth_katz`

Solved: stated here without proof.

> From [GuKa15]: diameter $\gg n / \log n$.

```lean
theorem erdos_100.variants.guth_katz :
    ∃ C > (0 : ℝ), ∀ᶠ n in atTop, ∀ A : Finset ℝ²,
      A.card = n →
      DistancesSeparated A →
      diam (A : Set ℝ²) ≥ C * n / log n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/100.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/100.lean#L72).

## `Erdos100.erdos_100_piepmeyer`

Solved: stated here; a Lean proof is at [https://github.com/theaustinhatfield/formal-conjectures/blob/solve-erdos-100-piepmeyer/FormalConjectures/ErdosProblems/100.lean](https://github.com/theaustinhatfield/formal-conjectures/blob/solve-erdos-100-piepmeyer/FormalConjectures/ErdosProblems/100.lean).

> From [Piepmeyer]: 9 points with diameter $< 5$.
> TODO: find reference

```lean
theorem erdos_100_piepmeyer :
    ∃ A : Finset ℝ², A.card = 9 ∧ DistancesSeparated A ∧
      diam (A : Set ℝ²) < 5
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/100.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/100.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/100.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/100.lean)
- [erdosproblems.com/100](https://www.erdosproblems.com/100)
