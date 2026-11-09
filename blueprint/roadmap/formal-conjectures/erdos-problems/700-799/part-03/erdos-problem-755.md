---
declaration: theorem
origin: cited
lean: Erdos755.erdos_755, Erdos755.erdos_755.variants.any_size_cdl
statement: formalized
---

# Erdős Problem 755

> *References:*
> - [erdosproblems.com/755](https://www.erdosproblems.com/755)
> - [ErPu75] Erdős, Paul and Purdy, George, Some extremal problems in geometry. III.
>   (1975), 291--308.
> - [Er94b] Erdős, Paul, Some problems in number theory, combinatorics and
>   combinatorial geometry. Math. Pannon. (1994), 261--269.
> - [CDL25b] Clemen, Felix Christian, Dumitrescu, Adrian, and Liu, Dingyuan,
>   The number of regular simplices in higher dimensions. arXiv:2507.19841 (2025).

*Quoted from [FormalConjectures/ErdosProblems/755.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/755.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/755](https://www.erdosproblems.com/755).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos755.erdos_755`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos755.lean#L1344](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos755.lean#L1344).

> Erdős asked whether every $n$-point set in
> $\mathbb{R}^6$ spans at most $(1/27 + o(1)) n^3$ unit equilateral triangles.
>
> Clemen, Dumitrescu, and Liu [CDL25b] proved the stronger any-size statement
> $T_6(n) = (1/27 + o(1)) n^3$. The unit-triangle upper bound follows as a
> corollary, since unit equilateral triangles are a subset of equilateral
> triangles of any positive side length: $T_\mathrm{unit} \leq T_\mathrm{anysize}$.

```lean
theorem erdos_755 :
    ∃ o : ℕ → ℝ,
      o =o[atTop] (fun _ : ℕ => (1 : ℝ)) ∧
        ∀ᶠ n in atTop,
          (TUnit 6 n : ℝ) ≤ ((1 / 27 : ℝ) + o n) * (n : ℝ) ^ 3
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/755.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/755.lean#L94).

## `Erdos755.erdos_755.variants.any_size_cdl`

Solved: stated here without proof.

> Clemen, Dumitrescu, and Liu [CDL25b] proved the stronger version where
> equilateral triangles of all positive side lengths are counted.

```lean
theorem erdos_755.variants.any_size_cdl :
    (fun n : ℕ => (TAnySize 6 n : ℝ)) ~[atTop]
      (fun n : ℕ => (1 / 27 : ℝ) * (n : ℝ) ^ 3)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/755.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/755.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/755.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/755.lean)
- [erdosproblems.com/755](https://www.erdosproblems.com/755)
