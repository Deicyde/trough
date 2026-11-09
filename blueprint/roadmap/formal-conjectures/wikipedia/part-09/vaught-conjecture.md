---
declaration: theorem
origin: cited
lean: VaughtConjecture.vaught_conjecture
statement: formalized
---

# Vaught conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Vaught_conjecture)

*Quoted from [FormalConjectures/Wikipedia/VaughtConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/VaughtConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `VaughtConjecture.vaught_conjecture`

Open: stated without proof.

> The Vaught conjecture states that for a countable language L and a complete L-Theory T
> the number of countable models of T (up to isomorphism) is finite, $\aleph_0$ or $2^{\aleph_0}$.

```lean
theorem vaught_conjecture {L : FirstOrder.Language} (hL : Countable L.Symbols)
                          {T : L.Theory} (hT : T.IsComplete) :
  numberOfCountableModels T ≤ Cardinal.aleph0 ∨ numberOfCountableModels T = Cardinal.continuum
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/Wikipedia/VaughtConjecture.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/VaughtConjecture.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/VaughtConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/VaughtConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Vaught_conjecture)
