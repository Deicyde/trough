---
declaration: theorem
origin: cited
lean: Erdos123.erdos_123, Erdos123.erdos_123.variants.erdos_lewin_3_5_7, Erdos123.erdos_123.variants.powers_2_3, Erdos123.erdos_123.variants.powers_2_3_5_snug
statement: formalized
---

# Erdős Problem 123

> *References:*
> - [erdosproblems.com/123](https://www.erdosproblems.com/123)
> - [ChYu23b] Chen, Yong-Gao and Yu, Wang-Xing, On {$d$}-complete sequences of integers, {II}. Acta
>   Arith. (2023), 161--181.
> - [Er92b] Erdős, Paul, Some of my favourite problems in various branches of combinatorics.
>   Matematiche (Catania) (1992), 231-240.
> - [Er97] Erdős, Paul, Problems in number theory. New Zealand J. Math. (1997), 155-160.
> - [Er97e] Erdős, Paul, Some of my favourite unsolved problems. Math. Japon. (1997), 527-537.
> - [ErLe96] Erdős, P. and Lewin, Mordechai, $d$-complete sequences of integers. Math. Comp. (1996),
>   837-840.
> - [MaCh16] Ma, Mi-Mi and Chen, Yong-Gao, On {$d$}-complete sequences of integers. J. Number Theory
>   (2016), 1--12.

*Quoted from [FormalConjectures/ErdosProblems/123.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/123.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/123](https://www.erdosproblems.com/123).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos123.erdos_123`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/a28a04b6b8ce43d5260a7466677c1f23833bfc38/src/latest/ErdosProblems/Erdos123.lean](https://github.com/plby/lean-proofs/blob/a28a04b6b8ce43d5260a7466677c1f23833bfc38/src/latest/ErdosProblems/Erdos123.lean).

> Let $a, b, c$ be three integers which are pairwise coprime. Is every large integer
> the sum of distinct integers of the form $a^k b^l c^m$ ($k, l, m ≥ 0$), none of which
> divide any other?
>
> Equivalently: is the set $\{a^k b^l c^m : k, l, m \geq 0\}$ d-complete?
>
> Note: For this not to reduce to the two-integer case, we need the integers
> to be greater than one and distinct.
>
> The prize of \$250 is offered by Erdős in [Er97] and [Er97e] for a 'proof or disproof'.
>
> The main problem was resolved in the affirmative by GPT 5.6 (prompted by Snyder).
>
> This was formalized in Lean by Alexeev.

```lean
theorem erdos_123 : ∀ a > 1, ∀ b > 1, ∀ c > 1, PairwiseCoprime a b c →
    IsDComplete (↑(powers a) * ↑(powers b) * ↑(powers c))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/123.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/123.lean#L92).

## `Erdos123.erdos_123.variants.erdos_lewin_3_5_7`

Solved: stated here without proof.

> Erdős and Lewin [ErLe96] proved this conjecture when $a = 3$, $b = 5$, and $c = 7$.

```lean
theorem erdos_123.variants.erdos_lewin_3_5_7 :
    IsDComplete (↑(powers 3) * ↑(powers 5) * ↑(powers 7))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/123.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/123.lean#L99).

## `Erdos123.erdos_123.variants.powers_2_3`

Solved: stated here without proof.

> A simpler case: the set of numbers of the form $2^k 3^l$ ($k, l ≥ 0$) is d-complete.
>
> This was initially conjectured by Erdős in 1992, who called it a "nice and difficult"
> problem, but it was quickly proven by Jansen and others using a simple inductive argument:
> - If $n = 2m$ is even, apply the inductive hypothesis to $m$ and double all summands.
> - If $n$ is odd, let $3^k$ be the largest power of $3$ with $3^k ≤ n$, and apply the
>   inductive hypothesis to $n - 3^k$ (which is even).

```lean
theorem erdos_123.variants.powers_2_3 : IsDComplete (↑(powers 2) * ↑(powers 3))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/123.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/123.lean#L112).

## `Erdos123.erdos_123.variants.powers_2_3_5_snug`

Open: stated without proof.

> In [Er92b] Erdős makes the stronger conjecture (for $a=2$, $b=3$, and $c=5$) that, for any
> $\epsilon>0$, all large integers $n$ can be written as the sum of distinct integers
> $b_1\lt \cdots \lt b_t$ of the form $2^k3^l5^m$ where $b_t<(1+\epsilon)b_1$.

```lean
theorem erdos_123.variants.powers_2_3_5_snug :
    ∀ ε > 0, ∀ᶠ n in atTop,
      ∃ A : Finset ℕ, (A : Set ℕ) ⊆ ↑(powers 2) * ↑(powers 3) * ↑(powers 5) ∧ IsSnug ε A ∧
        ∑ x ∈ A, x = n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/123.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/123.lean#L120).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/123.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/123.lean)
- [erdosproblems.com/123](https://www.erdosproblems.com/123)
