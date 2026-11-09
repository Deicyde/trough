---
declaration: theorem
origin: cited
lean: Kourovka.«1.40».kourovka_1_40
statement: formalized
---

# Conjecture 1.40

> by Sh. S. Kemkhadze
>
> Is a group a nilgroup if it is the product of two normal nilsubgroups?
>
> Here a nilgroup (Engel group) is a group in which every element is an Engel
> element. This is the Engel-group analogue of Fitting's theorem, which
> guarantees that the product of two normal nilpotent subgroups is nilpotent.
>
> *Reference:* [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v40)

*Quoted from [FormalConjectures/Kourovka/1_40.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_40.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Kourovka.«1.40».kourovka_1_40`

Open: stated without proof.

> Is a group a nilgroup if it is the product of two normal nilsubgroups?
>
> Since $H$ and $K$ are normal, the product $HK$ coincides with the join
> $H \sqcup K$, so "$G$ is the product of $H$ and $K$" is stated as
> $H \sqcup K = G$.

```lean
theorem kourovka_1_40 :
    ∀ (G : Type) [Group G] (H K : Subgroup G),
      H.Normal → K.Normal → IsEngelGroup H → IsEngelGroup K → H ⊔ K = ⊤ →
      IsEngelGroup G
```

Category `research open`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/1_40.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_40.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Kourovka/1_40.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Kourovka/1_40.lean)
- [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v40)
