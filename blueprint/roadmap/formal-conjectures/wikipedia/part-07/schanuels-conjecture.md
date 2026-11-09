---
declaration: theorem
origin: cited
lean: Schanuel.schanuel_conjecture
statement: formalized
---

# Schanuel's Conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Schanuel%27s_conjecture)

*Quoted from [FormalConjectures/Wikipedia/Schanuel.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Schanuel.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Schanuel.schanuel_conjecture`

Open: stated without proof.

> Given any set of $n$ complex numbers $\{z_1, ..., z_n\}$ that are linearly independent over
> $\mathbb{Q}$, the field extension $\mathbb{Q}(z_1, ..., z_n, e^{z_1}, ..., e^{z_n})$
> has transcendence degree at least $n$ over $\mathbb{Q}$.

```lean
theorem schanuel_conjecture (n : ℕ) (z : Fin n → ℂ) (h : LinearIndependent ℚ z) :
    n ≤ Algebra.trdeg ℚ (adjoin ℚ (Set.range z ∪ Set.range (cexp ∘ z)))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Schanuel.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Schanuel.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Schanuel.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Schanuel.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Schanuel%27s_conjecture)
