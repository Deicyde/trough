---
declaration: theorem
origin: cited
lean: Erdos1082.erdos_1082.parts.i, Erdos1082.erdos_1082.parts.ii
statement: formalized
---

# Erdős Problem 1082

> *Reference:* [erdosproblems.com/1082](https://www.erdosproblems.com/1082)

*Quoted from [FormalConjectures/ErdosProblems/1082.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1082.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1082](https://www.erdosproblems.com/1082).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos1082.erdos_1082.parts.i`

Open: stated without proof.

> Let $A\subset \mathbb{R}^2$ be a set of $n$ points with no three on a line.
> Does $A$ determine at least $\lfloor n/2\rfloor$ distinct distances?

```lean
theorem erdos_1082.parts.i : ∀ (A : Finset ℝ²) (hA_n3c : NonTrilinear (A : Set ℝ²)),
    A.card / 2 ≤ distinctDistances A
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1082.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1082.lean#L37).

## `Erdos1082.erdos_1082.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/0aca4d71095301c0fd2dca32611b7addb2ea735c/FormalConjectures/ErdosProblems/1082.lean#L291](https://github.com/google-deepmind/formal-conjectures/blob/0aca4d71095301c0fd2dca32611b7addb2ea735c/FormalConjectures/ErdosProblems/1082.lean#L291).

> Let $A\subset \mathbb{R}^2$ be a set of $n$ points with no three on a line.
> Must there exist a single point from which there are at least $\lfloor n/2\rfloor$ distinct
> distances?
>
> This question has been answered negatively by Xichuan in the
> [comments](https://www.erdosproblems.com/forum/thread/1082), who gave a set of $42$ points in
> $\mathbb{R}^2$, with no three on a line, such that each point determines only $20$ distinct distances.
>
> A smaller counterexample has been formalised here: it comprised of $8$ points, where each point only
> determines $3$ distances.
>
> This counterexample has originally been found by Heiko Harborth.

```lean
theorem erdos_1082.parts.ii :
    ¬ ∀ (A : Finset ℝ²) (hA : A.Nonempty) (hA_n3c : NonTrilinear (A : Set ℝ²)),
    ∃ (a : ℝ²) (ha : a ∈ A), A.card / 2 ≤ distinctDistancesFrom A a
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1082.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1082.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1082.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1082.lean)
- [erdosproblems.com/1082](https://www.erdosproblems.com/1082)
