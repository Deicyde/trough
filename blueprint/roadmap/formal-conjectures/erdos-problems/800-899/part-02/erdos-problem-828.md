---
declaration: theorem
origin: cited
lean: Erdos828.erdos_828, Erdos828.erdos_828.variants.lehmer_conjecture, Erdos828.erdos_828.variants.phi_dvd_self_iff_pow2_pow3
statement: formalized
---

# Erdős Problem 828

> *Reference:* [erdosproblems.com/828](https://www.erdosproblems.com/828)

*Quoted from [FormalConjectures/ErdosProblems/828.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/828.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/828](https://www.erdosproblems.com/828).

The file states 3 research or textbook statements: 2 open and 1 textbook result.

## `Erdos828.erdos_828`

Open: stated without proof.

> Is it true that, for any $a \in \mathbb{Z}$, there are infinitely many $n$ such that
>
> $$\phi(n) | n + a$$
>
> ?

```lean
theorem erdos_828 : ∀ a : ℤ, Set.Infinite {n : ℕ | ↑(φ n) ∣ n + a}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/828.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/828.lean#L37).

## `Erdos828.erdos_828.variants.lehmer_conjecture`

Open: stated without proof.

> When $n > 1$, Lehmer conjectured that $\phi(n) | n - 1$ if and only if $n$ is prime.

```lean
theorem erdos_828.variants.lehmer_conjecture : ∀ n > 1, φ n ∣ n - 1 ↔ Prime n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/828.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/828.lean#L44).

## `Erdos828.erdos_828.variants.phi_dvd_self_iff_pow2_pow3`

Textbook result, stated without proof. A Lean proof is at [https://github.com/XC0R/formal-conjectures/blob/d252395a9c80fc8eca30d9e5feb6e3b0bc7fc612/FormalConjectures/ErdosProblems/828.lean#L49](https://github.com/XC0R/formal-conjectures/blob/d252395a9c80fc8eca30d9e5feb6e3b0bc7fc612/FormalConjectures/ErdosProblems/828.lean#L49).

> It is an easy exercise to show that $\phi(n) | n$ if and only if $n = 0, 1$ or $n = 2^a 3^b$ for
> some $a > 0$.

```lean
theorem erdos_828.variants.phi_dvd_self_iff_pow2_pow3 {n : ℕ} :
    φ n ∣ n ↔ n ≤ 1 ∨ ∃ᵉ (a > 0) (b), n = 2 ^ a * 3 ^ b
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/828.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/828.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/828.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/828.lean)
- [erdosproblems.com/828](https://www.erdosproblems.com/828)
