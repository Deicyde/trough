---
declaration: theorem
origin: cited
lean: Erdos322.erdos_322
statement: formalized
---

# Erdős Problem 322

> *References:*
> - [erdosproblems.com/322](https://www.erdosproblems.com/322)
> - [Er36] Erdős, Paul, *On the Representation of an Integer as the Sum of k k-th Powers*. J. London
>   Math. Soc. (1936), 133-136.
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.
> - [Ma36] Mahler, Kurt, *Note on Hypothesis K of Hardy and Littlewood*. J. London Math. Soc. (1936),
>   136-138.

*Quoted from [FormalConjectures/ErdosProblems/322.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/322.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/322](https://www.erdosproblems.com/322).

The file states 1 research or textbook statement: 1 open.

## `Erdos322.erdos_322`

Open: stated without proof.

> Let $k\geq 3$ and $A\subset \mathbb{N}$ be the set of $k$th powers. What is the order of growth of $1_A^{(k)}(n)$, i.e. the number of representations of $n$ as the sum of $k$ many $k$th powers? Does there exist some $c>0$ and infinitely many $n$ such that $$1_A^{(k)}(n) >n^c?$$

```lean
theorem erdos_322 :
    ∀ k : ℕ, 3 ≤ k → ∃ c > (0 : ℝ),
      {n : ℕ | (n : ℝ) ^ c < representationCount k n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/322.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/322.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/322.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/322.lean)
- [erdosproblems.com/322](https://www.erdosproblems.com/322)
