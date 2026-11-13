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

*Quoted from [FormalConjectures/Kourovka/1_35c.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/1_35c.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Kourovka.«1.35c».kourovka_1_35c`

Open: stated without proof.

> Do there exist simple pro-orderable groups?

```lean
theorem kourovka_1_35c :
    ∃ (G : Type) (_ : Group G), IsSimpleGroup G ∧ ProOrderable G
```

Category `research open`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/1_35c.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/1_35c.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Kourovka/1_35c.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/1_35c.lean)
- [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v46)
