---
declaration: theorem
origin: cited
lean: Emirp.infinitude_question
statement: formalized
---

# Emirps

> An emirp is a prime whose decimal reversal is a different prime. It is unknown whether there are
> infinitely many emirps.
>
> *References:*
> * [Wikipedia, Emirp](https://en.wikipedia.org/wiki/Emirp)
> * [OEIS A006567](https://oeis.org/A006567)

*Quoted from [FormalConjectures/Wikipedia/Emirp.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Emirp.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 8 test statements, counted here but not shown.

## `Emirp.infinitude_question`

Open: stated without proof.

> [Wikipedia's article on emirps](https://en.wikipedia.org/wiki/Emirp) states: "It is not known
> whether there are infinitely many emirps."

```lean
theorem infinitude_question :
    {p : ℕ | IsEmirp p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Emirp.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Emirp.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Emirp.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Emirp.lean)
- [Wikipedia, Emirp](https://en.wikipedia.org/wiki/Emirp)
