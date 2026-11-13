---
declaration: theorem
origin: cited
lean: Erdos964.erdos_964, Erdos964.erdos_964.variants.eberhard
statement: formalized
---

# Erdős Problem 964

> *References:*
> - [erdosproblems.com/964](https://www.erdosproblems.com/964)
> - [Er86b] Erdős, P., *Some problems on number theory*. Proceedings of the seventeenth Southeastern
>   international conference on combinatorics, graph theory, and computing (Boca Raton, Fla.,
>   1986), Congr. Numer. 54 (1986), 225-244.
> - [Eb25] Eberhard, S., *Ratios of consecutive values of the divisor function*.
>   [arXiv:2505.00727](https://arxiv.org/abs/2505.00727) (2025).

*Quoted from [FormalConjectures/ErdosProblems/964.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/964.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/964](https://www.erdosproblems.com/964).

The file states 2 research or textbook statements: 2 solved. It also has 1 API statement, counted here but not shown.

## `Erdos964.erdos_964`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos964.lean#L1559](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos964.lean#L1559).

> Let $\tau(n)$ count the number of divisors of $n$. Is the sequence
>
> $$\frac{\tau(n+1)}{\tau(n)}$$
>
> everywhere dense in $(0,\infty)$?
>
> The answer is yes, proved by Eberhard [Eb25].

```lean
theorem erdos_964 : Set.Ioi (0 : ℝ) ⊆ closure (tauRatio '' Set.Ici 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/964.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/964.lean#L60).

## `Erdos964.erdos_964.variants.eberhard`

Solved: stated here without proof.

> Eberhard [Eb25] proved that the ratios $\tau(n+1)/\tau(n)$ attain every positive rational value
> infinitely many times. Since the positive rationals are dense in $(0,\infty)$, this implies
> `erdos_964`.

```lean
theorem erdos_964.variants.eberhard (q : ℚ) (hq : 0 < q) :
    {n : ℕ | 0 < n ∧ tauRatio n = q}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/964.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/964.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/964.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/964.lean)
- [erdosproblems.com/964](https://www.erdosproblems.com/964)
