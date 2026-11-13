---
declaration: theorem
origin: cited
lean: Erdos900.erdos_900
statement: formalized
---

# Erdős Problem 900

> *References:*
> - [erdosproblems.com/900](https://www.erdosproblems.com/900)
> - [AKS81] Ajtai, Miklós and Komlós, János and Szemerédi, Endre, *The longest path in a random
>   graph*. Combinatorica 1 (1981), 1--12.
> - [Er78] Erdős, Paul, *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Proceedings of the Ninth Southeastern Conference on Combinatorics, Graph Theory, and
>   Computing (1978), 29-40. [PDF](https://www.renyi.hu/~p_erdos/1978-36.pdf)

*Quoted from [FormalConjectures/ErdosProblems/900.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/900.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/900](https://www.erdosproblems.com/900).

The file states 1 research or textbook statement: 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos900.erdos_900`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos900.lean#L950](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos900.lean#L950).

> There is a function $f:(1/2,\infty)\to \mathbb{R}$ such that $f(c)\to 0$ as $c\to 1/2$ and
> $f(c)\to 1$ as $c\to \infty$ and every random graph with $n$ vertices and $cn$ edges has (with
> high probability) a path of length at least $f(c)n$.
>
> Conjectured by Erdős [Er78, p. 32] and proved by Ajtai, Komlós, and Szemerédi [AKS81]. We take
> the uniform random graph with $\lfloor cn\rfloor$ edges, count the length of a path in edges, read
> "with high probability" as probability tending to $1$ as $n\to\infty$, and require $f(c)>0$ for
> every $c>1/2$ (a path of linear length). The linked formal proof uses the same uniform model,
> written as uniformly random $0/1$ vectors of weight $\lfloor cn\rfloor$ indexed by the pairs of
> vertices.

```lean
theorem erdos_900 :
    ∃ f : ℝ → ℝ, (∀ c : ℝ, 1 / 2 < c → 0 < f c) ∧
      Tendsto f (𝓝[>] (1 / 2)) (𝓝 0) ∧ Tendsto f atTop (𝓝 1) ∧
      ∀ c : ℝ, 1 / 2 < c → Tendsto (fun n : ℕ ↦
        uniformEdgeProbability n ⌊c * n⌋₊ (HasLongPath n (f c))) atTop (𝓝 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/900.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/900.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/900.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/900.lean)
- [erdosproblems.com/900](https://www.erdosproblems.com/900)
