---
declaration: theorem
origin: cited
lean: Erdos1029.erdos_1029
statement: formalized
---

# Erdős Problem 1029

> *References:*
> - [erdosproblems.com/1029](https://www.erdosproblems.com/1029)
> - [Er93] Erdős, Paul, Some of my favorite solved and unsolved problems in graph theory.
>   Quaestiones Math. (1993), 333-350.
> - [ErSz35] Erdős, P. and Szekeres, G., A combinatorial problem in geometry. Compos. Math. (1935),
>   463-470.
> - [Sp75] Spencer, J., Ramsey's theorem - a new lower bound. J. Combin. Theory Ser. A (1975),
>   108-115.

*Quoted from [FormalConjectures/ErdosProblems/1029.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1029.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1029](https://www.erdosproblems.com/1029).

The file states 1 research or textbook statement: 1 open.

## `Erdos1029.erdos_1029`

Open: stated without proof.

> If $R(k)$ is the Ramsey number for $K_k$, the minimal $n$ such that every $2$-colouring of the edges
> of $K_n$ contains a monochromatic copy of $K_k$, then
>
> $$\frac{R(k)}{k2^{k/2}}\to \infty.$$
>
> In [Er93] Erdős offers $100 for a proof of this and $1000 for a disproof, but says 'this last offer
> is to some extent phoney: I am sure that this is true (but I have been wrong before).'

```lean
theorem erdos_1029 :
    Tendsto (fun k : ℕ ↦ (SimpleGraph.diagonalRamsey k : ℝ) /
      ((k : ℝ) * (2 : ℝ) ^ ((k : ℝ) / 2))) atTop atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1029.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1029.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1029.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1029.lean)
- [erdosproblems.com/1029](https://www.erdosproblems.com/1029)
