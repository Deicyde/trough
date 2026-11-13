---
declaration: theorem
origin: cited
lean: Erdos793.erdos_793, Erdos793.erdos_793.variants.constant
statement: formalized
---

# Erdős Problem 793

> *References:*
> - [erdosproblems.com/793](https://www.erdosproblems.com/793)
> - [Er38] Erdős, P., *On sequences of integers no one of which divides the product of two others
>   and on related problems*. Tomsk. Gos. Univ. Ucen Zap. (1938), 74-82.
> - [Er69] Erdős, Paul, *Some applications of graph theory to number theory*. The Many Facets of
>   Graph Theory (Proc. Conf., Western Mich. Univ., Kalamazoo, Mich., 1968) (1969), 77-82.
> - [Er70b] Erdős, P., *Some applications of graph theory to number theory*. Proc. Second Chapel Hill
>   Conf. on Combinatorial Mathematics and its Applications (Univ. North Carolina, Chapel Hill, N.C.,
>   1970) (1970), 136-145.

*Quoted from [FormalConjectures/ErdosProblems/793.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/793.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/793](https://www.erdosproblems.com/793).

The file states 2 research or textbook statements: 2 solved.

## `Erdos793.erdos_793`

Solved: stated here without proof.

> Let $F(n)$ be the maximum possible size of a subset $A \subseteq \{1, \ldots, n\}$ such that
> $a \nmid bc$ whenever $a, b, c \in A$ with $a \neq b$ and $a \neq c$. Is there a constant $c$ such
> that
>
> $$F(n) = \pi(n) + (c + o(1)) n^{2/3} (\log n)^{-2}?$$
>
> A problem of Erdős [Er69, Er70b], who proved in [Er38] that
> $F(n) = \pi(n) + O(n^{2/3} (\log n)^{-2})$. The answer is yes, with $c = 27/2$: this was proved by
> GPT-5.6 Sol (prompted by Chojecki), refining the argument of [Er38]; see
> `erdos_793.variants.constant`.

```lean
theorem erdos_793 :
    ∃ c : ℝ, Tendsto (fun n : ℕ ↦ ((F n : ℝ) - Nat.primeCounting n) /
      ((n : ℝ) ^ ((2 : ℝ) / 3) / (log n) ^ 2)) atTop (𝓝 c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/793.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/793.lean#L64).

## `Erdos793.erdos_793.variants.constant`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos793.lean#L25](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos793.lean#L25).

> The constant in Problem 793 is $c = 27/2$, i.e.
>
> $$F(n) = \pi(n) + \left(\frac{27}{2} + o(1)\right) \frac{n^{2/3}}{(\log n)^2}.$$
>
> Formalised by van Doorn and Aristotle, following the proof of GPT-5.6 Sol.

```lean
theorem erdos_793.variants.constant :
    Tendsto (fun n : ℕ ↦ ((F n : ℝ) - Nat.primeCounting n) /
      ((n : ℝ) ^ ((2 : ℝ) / 3) / (log n) ^ 2)) atTop (𝓝 (27 / 2))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/793.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/793.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/793.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/793.lean)
- [erdosproblems.com/793](https://www.erdosproblems.com/793)
