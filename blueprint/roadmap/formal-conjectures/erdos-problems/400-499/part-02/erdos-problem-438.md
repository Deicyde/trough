---
declaration: theorem
origin: cited
lean: Erdos438.erdos_438
statement: formalized
---

# Erdős Problem 438

> *References:*
> - [erdosproblems.com/438](https://www.erdosproblems.com/438)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [Er80c] Erdős, Paul, *Nine little known problems in combinatorial number theory*. Normat (1980),
>   155-164, 180.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [LOS83] Lagarias, J. C. and Odlyzko, A. M. and Shearer, J. B., *On the density of sequences of
>   integers the sum of no two of which is a square. II. General sequences*. J. Combin. Theory Ser. A
>   (1983), 123-139.
> - [KLS02] Khalfalah, A. and Lodha, S. and Szemerédi, E., *Tight bound for the density of sequence
>   of integers the sum of no two of which is a perfect square*. Discrete Math. (2002), 243-255.

*Quoted from [FormalConjectures/ErdosProblems/438.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/438.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/438](https://www.erdosproblems.com/438).

The file states 1 research or textbook statement: 1 solved.

## `Erdos438.erdos_438`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos438.lean#L46](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos438.lean#L46).

> How large can $A \subseteq \{1, \ldots, N\}$ be if $A + A$ contains no square numbers?
>
> A problem of Erdős [Er80, Er80c, ErGr80]. Taking all integers $\equiv 1 \pmod 3$ gives
> $|A| \ge N/3$, and Massias observed that all integers
> $\equiv 1, 5, 9, 13, 14, 17, 21, 25, 26, 29, 30 \pmod{32}$ give $|A| \ge \frac{11}{32} N$.
> Lagarias, Odlyzko and Shearer [LOS83] proved that $11/32$ is sharp for the modular version of the
> problem, and Khalfalah, Lodha and Szemerédi [KLS02] proved that it is sharp in general: the
> maximal such $A$ satisfies $|A| \le (\frac{11}{32} + o(1)) N$.

```lean
theorem erdos_438 :
    Tendsto (fun N : ℕ ↦ (extremalSize N : ℝ) / (N : ℝ)) atTop (𝓝 ((11 : ℝ) / 32))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/438.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/438.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/438.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/438.lean)
- [erdosproblems.com/438](https://www.erdosproblems.com/438)
