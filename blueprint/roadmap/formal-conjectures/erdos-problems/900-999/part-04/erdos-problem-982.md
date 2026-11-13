---
declaration: theorem
origin: cited
lean: Erdos982.erdos_982, Erdos982.erdos_982.variants.concyclic
statement: formalized
---

# Erdős Problem 982

> *Reference:* [erdosproblems.com/982](https://www.erdosproblems.com/982)

*Quoted from [FormalConjectures/ErdosProblems/982.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/982.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/982](https://www.erdosproblems.com/982).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos982.erdos_982`

Open: stated without proof.

> If $n$ distinct points in $\mathbb{R}^2$ form a convex polygon then some vertex has at least
> $\lfloor\frac{n}{2}\rfloor$ different distances to other vertices.

```lean
theorem erdos_982 (n : ℕ) (hn : 3 ≤ n) (p : Fin n → ℝ²) (hp : Function.Injective p)
    (hp' : EuclideanGeometry.IsConvexPolygon p) :
    ∃ (i : Fin n), { d : ℝ | ∃ j : Fin n, j ≠ i ∧ d = dist (p i) (p j) }.ncard ≥ n / 2
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/982.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/982.lean#L37).

## `Erdos982.erdos_982.variants.concyclic`

Solved: stated here; a Lean proof is at [https://github.com/arex1337/formal-conjectures-proofs/blob/3b7d581c75fd00e482deabfb20675cf3ccfaf49f/Erdos982/GeneralCircle.lean](https://github.com/arex1337/formal-conjectures-proofs/blob/3b7d581c75fd00e482deabfb20675cf3ccfaf49f/Erdos982/GeneralCircle.lean).

> For distinct points on a common circle, every vertex has at least
> $\lfloor\frac{n}{2}\rfloor$ different distances to the other vertices.
> This does not require convexity or the assumption $3 \leq n$.

```lean
theorem erdos_982.variants.concyclic {n : ℕ} (p : Fin n → ℝ²) (hp : Function.Injective p)
    (c : ℝ²) (R : ℝ) (hR : ∀ j, dist (p j) c = R) (i : Fin n) :
    { d : ℝ | ∃ j : Fin n, j ≠ i ∧ d = dist (p i) (p j) }.ncard ≥ n / 2
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/982.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/982.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/982.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/982.lean)
- [erdosproblems.com/982](https://www.erdosproblems.com/982)
