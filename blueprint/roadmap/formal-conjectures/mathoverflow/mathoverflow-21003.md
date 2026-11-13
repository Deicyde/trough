---
declaration: theorem
origin: cited
lean: Mathoverflow21003.mathoverflow_21003
statement: formalized
---

# Mathoverflow 21003

> Is there any polynomial $f(x, y) \in \mathbb{Q}[x, y]$ such that
> $f : \mathbb{Q} \times \mathbb{Q} \rightarrow \mathbb{Q}$ is a bijection?
>
> *Reference:* [mathoverflow/21003](https://mathoverflow.net/questions/21003)
> asked by user [*Z.H.*](https://mathoverflow.net/users/5098/z-h)

*Quoted from [FormalConjectures/Mathoverflow/21003.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/21003.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Mathoverflow21003.mathoverflow_21003`

Open: stated without proof.

> Is there any polynomial $f(x, y) \in \mathbb{Q}[x, y]$ such that
> $f : \mathbb{Q} \times \mathbb{Q} \rightarrow \mathbb{Q}$ is a bijection?

```lean
theorem mathoverflow_21003 :
    ∃ f : MvPolynomial (Fin 2) ℚ, Function.Bijective fun x ↦ f.eval x
```

Category `research open`; AMS [12 Field theory and polynomials](../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Mathoverflow/21003.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/21003.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/21003.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/21003.lean)
- [mathoverflow/21003](https://mathoverflow.net/questions/21003)
