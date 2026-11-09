---
declaration: theorem
origin: cited
lean: Erdos578.erdos_578, Erdos578.erdos_578.variants.riordan
statement: formalized
---

# Erdős Problem 578

> *References:*
> - [erdosproblems.com/578](https://www.erdosproblems.com/578)
> - [Ri00] Riordan, Oliver, *Spanning subgraphs of random graphs*.
>   Combin. Probab. Comput. (2000), 125-148. [DOI](https://doi.org/10.1017/S0963548399004150)

*Quoted from [FormalConjectures/ErdosProblems/578.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/578.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/578](https://www.erdosproblems.com/578).

The file states 2 research or textbook statements: 2 solved.

## `Erdos578.erdos_578`

Solved: stated here without proof.

> If $G$ is a random graph on $2^d$ vertices, including each edge with probability $1/2$, then $G$
> almost surely contains a copy of $Q_d$ (the $d$-dimensional hypercube with $2^d$ vertices and
> $d2^{d-1}$ many edges).
>
> A conjecture of Erdős and Bollobás. Solved by Riordan [Ri00], who in fact proved this with any
> edge-probability $>1/4$.
>
> Here almost surely means that the probability tends to $1$ as $d\to\infty$.

```lean
theorem erdos_578 :
    Tendsto (fun d : ℕ =>
      binomialRandom (Fin d → Bool) ⟨1 / 2, by norm_num⟩
        {G | (hypercube d).IsContained G}) atTop (nhds 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/578.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/578.lean#L46).

## `Erdos578.erdos_578.variants.riordan`

Solved: stated here without proof.

> For every fixed edge-probability $p>1/4$, the probability that a random graph on $2^d$
> vertices contains a copy of $Q_d$ tends to $1$ as $d\to\infty$. Proved by Riordan [Ri00].

```lean
theorem erdos_578.variants.riordan (p : unitInterval) (hp : (1 : ℝ) / 4 < p) :
    Tendsto (fun d : ℕ =>
      binomialRandom (Fin d → Bool) p {G | (hypercube d).IsContained G})
      atTop (nhds 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/578.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/578.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/578.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/578.lean)
- [erdosproblems.com/578](https://www.erdosproblems.com/578)
