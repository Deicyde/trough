---
declaration: theorem
origin: cited
lean: Kourovka.«19.25».kourovka_19_25
statement: formalized
---

# Conjecture 19.25

> by B. Curtin, G. R. Pourgholi
>
> *Reference:* [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v40)
>
> - [vDJMM26] W. van Doorn, E. Judin, P. Monticone and D. Morrison,
>   *On Some Problems from the Kourovka Notebook*,
>   [arXiv:2607.17477v1](https://arxiv.org/abs/2607.17477v1), Theorem 4.1.

*Quoted from [FormalConjectures/Kourovka/19_25.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/19_25.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Kourovka.«19.25».kourovka_19_25`

Solved: stated here without proof.

> Let $G$ and $H$ be finite groups of the same order with
> $\sum_{g \in G} \phi(|g|) = \sum_{h \in H} \phi(|h|)$,
> where $\phi$ is the Euler totient function. Suppose that $G$ is simple. Is
> $H$ necessarily simple?
>
> The answer is negative by [vDJMM26, Theorem 4.1]. The groups
> $G = \operatorname{PSU}(3,3)$ and $H = C_6 \times S_4 \times (C_7 \rtimes C_6)$
> both have order $6048$ and totient sum $23984$, but only $G$ is simple.
> In the semidirect product, a generator of $C_6$ acts on $C_7$ by multiplication
> by $3$ modulo $7$.

```lean
theorem kourovka_19_25 :
    ¬ ∀ (G H : Type) [Group G] [Group H] [Fintype G] [Fintype H],
       Fintype.card G = Fintype.card H →
       ∑ g : G, φ (orderOf g) = ∑ h : H, φ (orderOf h) →
       IsSimpleGroup G → IsSimpleGroup H
```

Category `research solved`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/19_25.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/19_25.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Kourovka/19_25.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/19_25.lean)
- [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v40)
