---
declaration: theorem
origin: cited
lean: Erdos220.erdos_220
statement: formalized
---

# Erdős Problem 220

> *References:*
> - [erdosproblems.com/220](https://www.erdosproblems.com/220)
> - [Er40] Erdős, P., *The difference of consecutive primes*. Duke Math. J. (1940), 438--441.
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971)
>   (1973), 117-138.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [MoVa86] Montgomery, H. L. and Vaughan, R. C., *On the distribution of reduced residues*. Ann. of
>   Math. (2) (1986), 311-333.
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.

*Quoted from [FormalConjectures/ErdosProblems/220.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/220.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/220](https://www.erdosproblems.com/220).

The file states 1 research or textbook statement: 1 solved.

## `Erdos220.erdos_220`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos220.lean#L39](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos220.lean#L39).

> Let $n \geq 1$ and
>
> $$A = \{a_1 < \cdots < a_{\phi(n)}\} = \{1 \leq m < n : (m, n) = 1\}.$$
>
> Is it true that
>
> $$\sum_{1 \leq k < \phi(n)} (a_{k+1} - a_k)^2 \ll \frac{n^2}{\phi(n)}?$$
>
> A problem of Erdős [Er40, Er73, ErGr80], which is discussed in problem B40 of Guy's collection
> [Gu04]. The answer is yes, as proved by Montgomery and Vaughan [MoVa86], who in fact proved that
> $\sum_{1 \leq k < \phi(n)} (a_{k+1} - a_k)^\gamma \ll n^\gamma / \phi(n)^{\gamma - 1}$ for every
> $\gamma \geq 1$.

```lean
theorem erdos_220 :
    ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, 1 ≤ n →
      (sumSquaredGaps (sortedTotatives n) : ℝ) ≤ C * (n : ℝ) ^ 2 / (n.totient : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/220.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/220.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/220.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/220.lean)
- [erdosproblems.com/220](https://www.erdosproblems.com/220)
