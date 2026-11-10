---
declaration: theorem
origin: cited
lean: ErdosMoser.erdos_moser_conjecture
statement: formalized
---

# The Erdős–Moser equation

> For positive integers $k$ and $m$, let
>
> $$S_k(m)=1^k+2^k+\cdots+(m-1)^k.$$
>
> The Erdős–Moser conjecture says that $S_k(m)=m^k$ has only the solution
> $(k,m)=(1,3)$.
>
> *References:*
> * [Wikipedia: Erdős–Moser equation](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Moser_equation)
> * B. C. Kellner,
>   [On stronger conjectures that imply the Erdős–Moser conjecture](https://arxiv.org/abs/1003.1646)

*Quoted from [FormalConjectures/Wikipedia/ErdosMoser.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ErdosMoser.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 3 test statements, counted here but not shown.

## `ErdosMoser.erdos_moser_conjecture`

Open: stated without proof.

> The only positive solution of $S_k(m)=m^k$ is $(k,m)=(1,3)$.

```lean
theorem erdos_moser_conjecture :
    ∀ k m : ℕ, 0 < k → 0 < m → powerSum k m = m ^ k → k = 1 ∧ m = 3
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ErdosMoser.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ErdosMoser.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ErdosMoser.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ErdosMoser.lean)
- [Wikipedia: Erdős–Moser equation](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Moser_equation)
