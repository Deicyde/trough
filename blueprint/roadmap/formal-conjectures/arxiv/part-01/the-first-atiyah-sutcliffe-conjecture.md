---
declaration: theorem
origin: cited
lean: AtiyahSutcliffe.conjecture_one
statement: formalized
---

# The first Atiyah--Sutcliffe conjecture

> Atiyah and Sutcliffe associate a homogeneous binary polynomial to each point
> in a configuration of distinct points in Euclidean three-space. Their first
> conjecture says that these polynomials are always linearly independent.
>
> *References:*
> - M. F. Atiyah and P. M. Sutcliffe,
>   [The Geometry of Point Particles](https://doi.org/10.1098/rspa.2001.0913)
> - Marcin Mazur and Bogdan V. Petrenko,
>   [On the conjectures of Atiyah and Sutcliffe](https://arxiv.org/abs/1102.4662)

*Quoted from [FormalConjectures/Arxiv/1102.4662/AtiyahSutcliffe.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1102.4662/AtiyahSutcliffe.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `AtiyahSutcliffe.conjecture_one`

Open: stated without proof.

> [Atiyah–Sutcliffe Conjecture 1](https://doi.org/10.1098/rspa.2001.0913), stated as
> Conjecture 1.1 in [Mazur–Petrenko](https://arxiv.org/abs/1102.4662): the configuration
> polynomials are linearly independent.

```lean
theorem conjecture_one {n : ℕ} (x : Fin n → Point) (hx : Function.Injective x) :
    LinearIndependent ℂ (pointPolynomial x)
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [70 Mechanics of particles and systems](../../by-subject/part-02/70-mechanics-of-particles-and-systems/README.md). Declared in [FormalConjectures/Arxiv/1102.4662/AtiyahSutcliffe.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1102.4662/AtiyahSutcliffe.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/1102.4662/AtiyahSutcliffe.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1102.4662/AtiyahSutcliffe.lean)
- [The Geometry of Point Particles](https://doi.org/10.1098/rspa.2001.0913)
