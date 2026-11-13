---
declaration: theorem
origin: cited
lean: Erdos486.erdos_486
statement: formalized
---

# Erdős Problem 486: Logarithmic density for sets avoiding modular subsets

> *References:*
> * [erdosproblems.com/486](https://www.erdosproblems.com/486)
> * [Wa26] Wang, S., *A proposed solution to Erdős Problem 486* (2026),
>   https://github.com/ShouqiaoW/erdos/blob/main/486/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/486.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/486.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/486](https://www.erdosproblems.com/486).

The file states 1 research or textbook statement: 1 solved.

## `Erdos486.erdos_486`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos486.lean#L20](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos486.lean#L20); a Lean proof is at [https://github.com/Konamiu/formal-conjectures/blob/c69df0584ca9767090f5a68c8f09f1ff3c93ab80/FormalConjectures/ErdosProblems/486.lean#L39](https://github.com/Konamiu/formal-conjectures/blob/c69df0584ca9767090f5a68c8f09f1ff3c93ab80/FormalConjectures/ErdosProblems/486.lean#L39).

> Let $A \subseteq \mathbb{N}$, and for each $n \in A$ choose some
> $X_n \subseteq \mathbb{Z}/n\mathbb{Z}$. Let
> $B = \{m \in \mathbb{N} : m \not\in X_n \pmod{n} \text{ for all } n \in A \text{ with } m > n\}$.
> Must $B$ have a logarithmic density?
>
> The set $A$ is encoded by taking $X_n = \emptyset$ for $n \notin A$. Only positive moduli
> $n$ are considered, since $\mathbb{Z}/0\mathbb{Z} = \mathbb{Z}$ would allow $B$ to be an
> arbitrary set.
>
> The answer is no: Wang [Wa26] (with GPT-5.6) constructed a congruence system whose survivor set
> $B$ has lower logarithmic density at most $177/200$ and upper logarithmic density at least
> $49/50$. The first linked formal proof establishes this for the real-cutoff normalisation
> $\frac{1}{\log x}\sum_{m < x, m \in B} \frac{1}{m}$ with the moduli restricted to $A$; the
> second derives the statement below (`Set.HasLogDensity`, all moduli) from it.

```lean
theorem erdos_486 :
    ¬ ∀ X : (n : ℕ) → Set (ZMod n),
      ∃ d, {m : ℕ | ∀ n, 0 < n → n < m → (m : ZMod n) ∉ X n}.HasLogDensity d
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/486.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/486.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/486.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/486.lean)
- [erdosproblems.com/486](https://www.erdosproblems.com/486)
