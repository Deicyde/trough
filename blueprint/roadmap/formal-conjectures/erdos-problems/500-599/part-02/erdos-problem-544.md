---
declaration: theorem
origin: cited
lean: Erdos544.erdos_544.parts.i, Erdos544.erdos_544.parts.ii
statement: formalized
---

# Erdős Problem 544

> *References:*
> - [erdosproblems.com/544](https://www.erdosproblems.com/544)

*Quoted from [FormalConjectures/ErdosProblems/544.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/544.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/544](https://www.erdosproblems.com/544).

The file states 2 research or textbook statements: 2 open.

## `Erdos544.erdos_544.parts.i`

Open: stated without proof.

> Show that
> $$R(3,k+1)-R(3,k)\to\infty$$
> as $k\to \infty$.
>
> A problem of Erdős and Sós.
> This problem is #8 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_544.parts.i :
    Tendsto (fun k : ℕ ↦ (SimpleGraph.classicalRamsey 3 (k + 1) : ℝ) -
      (SimpleGraph.classicalRamsey 3 k : ℝ)) atTop atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/544.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/544.lean#L42).

## `Erdos544.erdos_544.parts.ii`

Open: stated without proof.

> Similarly, prove or disprove that
> $$R(3,k+1)-R(3,k)=o(k).$$

```lean
theorem erdos_544.parts.ii :
    (fun k : ℕ ↦ (SimpleGraph.classicalRamsey 3 (k + 1) : ℝ) -
      (SimpleGraph.classicalRamsey 3 k : ℝ)) =o[atTop] (fun k : ℕ ↦ (k : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/544.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/544.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/544.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/544.lean)
- [erdosproblems.com/544](https://www.erdosproblems.com/544)
