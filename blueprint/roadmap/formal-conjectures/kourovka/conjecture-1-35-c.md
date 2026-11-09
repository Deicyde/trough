---
declaration: theorem
origin: cited
lean: Kourovka.«1.35c».kourovka_1_35c
statement: formalized
---

# Conjecture 1.35(c)

> by A. I. Mal'cev and L. Fuchs
>
> *Reference:* [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v46)

*Quoted from [FormalConjectures/Kourovka/1_35c.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_35c.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Kourovka.«1.35c».kourovka_1_35c`

Open: stated without proof.

> Do there exist simple pro-orderable groups?

```lean
theorem kourovka_1_35c :
    ∃ (G : Type) (_ : Group G), IsSimpleGroup G ∧ ProOrderable G
```

Category `research open`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/1_35c.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_35c.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Kourovka/1_35c.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_35c.lean)
- [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v46)
