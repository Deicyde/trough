---
declaration: theorem
origin: cited
lean: Erdos1030.erdos_1030
statement: formalized
---

# Erdős Problem 1030

> *References:*
> - [erdosproblems.com/1030](https://www.erdosproblems.com/1030)
> - [BEFS89] Burr, S. and Erdős, P. and Faudree, R. J. and Schelp, R. H., On the difference between
>   consecutive Ramsey numbers. Utilitas Math. (1989), 115-118.

*Quoted from [FormalConjectures/ErdosProblems/1030.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1030.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1030](https://www.erdosproblems.com/1030).

The file states 1 research or textbook statement: 1 open.

## `Erdos1030.erdos_1030`

Open: stated without proof.

> Let $R(k,l)$ be the usual Ramsey number: the smallest $n$ such that if the edges of $K_n$ are
> coloured red and blue then there exists either a red $K_k$ or a blue $K_l$.
>
> Prove the existence of some $c>0$ such that
> $$\lim_{k\to \infty}\frac{R(k+1,k)}{R(k,k)}> 1+c.$$
>
> A problem of Erdős and Sós.

```lean
theorem erdos_1030 :
    ∃ c > (0 : ℝ), ∃ L : ℝ,
      Tendsto (fun k : ℕ ↦
        (SimpleGraph.classicalRamsey (k + 1) k : ℝ) /
          (SimpleGraph.classicalRamsey k k : ℝ)) atTop (nhds L) ∧
      L > 1 + c
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1030.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1030.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1030.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1030.lean)
- [erdosproblems.com/1030](https://www.erdosproblems.com/1030)
