---
declaration: theorem
origin: cited
lean: Erdos564.erdos_564
statement: formalized
---

# Erdős Problem 564

> *Reference:* [erdosproblems.com/564](https://www.erdosproblems.com/564)

*Quoted from [FormalConjectures/ErdosProblems/564.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/564.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/564](https://www.erdosproblems.com/564).

The file states 1 research or textbook statement: 1 open.

## `Erdos564.erdos_564`

Open: stated without proof.

> Let $R_3(n)$ be the minimal $m$ such that if the edges of the $3$-uniform hypergraph on $m$
> vertices are $2$-coloured then there is a monochromatic copy of the complete $3$-uniform
> hypergraph on $n$ vertices.
>
> Is there some constant $c>0$ such that
> $$ R_3(n) \geq 2^{2^{cn}}? $$

```lean
theorem erdos_564 :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (2 : ℝ) ^ (2 : ℝ) ^ (c * n) ≤ hypergraphRamsey 3 n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/564.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/564.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/564.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/564.lean)
- [erdosproblems.com/564](https://www.erdosproblems.com/564)
