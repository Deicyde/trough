---
declaration: theorem
origin: cited
lean: Erdos237.erdos_237, Erdos237.erdos_237.variants.infinite, Erdos237.erdos_237.variants.pow_two
statement: formalized
---

# Erdős Problem 237

> *References:*
> - [erdosproblems.com/237](https://www.erdosproblems.com/237)
> - [ChDi22] Chen, Y.-G. and Ding, Y., *On a conjecture of Erdős*.
>   [arXiv:2201.10727](https://arxiv.org/abs/2201.10727) (2022).
> - [Er50] Erdős, P., *On integers of the form $2^k+p$ and some related problems*.
>   Summa Brasil. Math. (1950), 113-123.

*Quoted from [FormalConjectures/ErdosProblems/237.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/237.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/237](https://www.erdosproblems.com/237).

The file states 3 research or textbook statements: 3 solved.

## `Erdos237.erdos_237`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos237b.lean#L55](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos237b.lean#L55).

> Let $A\subseteq \mathbb{N}$ be a set such that $\lvert A\cap \{1,\ldots,N\}\rvert \gg \log N$ for
> all large $N$. Let $f(n)$ count the number of solutions to $n=p+a$ for $p$ prime and $a\in A$. Is
> it true that $\limsup f(n)=\infty$?
>
> The answer is yes, as proved by Chen and Ding [ChDi22].
>
> Here `A` may contain $0$. This changes each $f(n)$ by at most one, so it does not affect the
> answer.

```lean
theorem erdos_237 : ∀ A : Set ℕ,
    (fun N : ℕ ↦ Real.log N) =O[atTop] (fun N ↦ ((A ∩ .Icc 1 N).ncard : ℝ)) →
    limsup (fun n ↦ (f A n : ℕ∞)) atTop = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/237.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/237.lean#L57).

## `Erdos237.erdos_237.variants.infinite`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos237b.lean#L55](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos237b.lean#L55).

> Chen and Ding [ChDi22] proved that the assumption
> $\lvert A\cap \{1,\ldots,N\}\rvert \gg \log N$ can be replaced with the assumption that $A$ is
> infinite.

```lean
theorem erdos_237.variants.infinite (A : Set ℕ) (hA : A.Infinite) :
    limsup (fun n ↦ (f A n : ℕ∞)) atTop = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/237.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/237.lean#L70).

## `Erdos237.erdos_237.variants.pow_two`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos237b.lean#L55](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos237b.lean#L55).

> Erdős [Er50] proved the case $A=\{2^k : k\geq 0\}$.

```lean
theorem erdos_237.variants.pow_two :
    limsup (fun n ↦ (f (Set.range (2 ^ ·)) n : ℕ∞)) atTop = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/237.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/237.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/237.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/237.lean)
- [erdosproblems.com/237](https://www.erdosproblems.com/237)
