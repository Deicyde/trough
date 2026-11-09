---
declaration: theorem
origin: cited
lean: Erdos1148.erdos_1148, Erdos1148.erdos_1148.variants.lower_bound, Erdos1148.erdos_1148.variants.weaker
statement: formalized
---

# Erdős Problem 1148

> *References:*
> - [erdosproblems.com/1148](https://www.erdosproblems.com/1148)
> - [Ch26] P. Chojecki, [Bounded Representations by $x^2 + y^2 - z^2$](https://www.ulam.ai/research/erdos1148-full.pdf) (2026)
> - [Va99] Various, Some of Paul's favorite problems. Booklet produced for the conference "Paul Erdős
>   and his mathematics", Budapest, July 1999 (1999).

*Quoted from [FormalConjectures/ErdosProblems/1148.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1148.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1148](https://www.erdosproblems.com/1148).

The file states 3 research or textbook statements: 2 solved and 1 textbook result.

## `Erdos1148.erdos_1148`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1148.lean#L238](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1148.lean#L238).

> Can every large integer $n$ be written as $n=x^2+y^2-z^2$ with $\max(x^2,y^2,z^2)\leq n$?
>
> This was proved affirmatively by Chojecki [Ch26], using a Duke-type equidistribution theorem.
> A Lean formalisation of the reduction (conditional on a Duke-type equidistribution theorem) exists;
> see the [forum discussion](https://www.erdosproblems.com/forum/thread/1148#post-4849). The linked
> formal proof (plby/lean-proofs) removes the Duke hypothesis; it is stated over `ℤ`, as
> `∃ N, ∀ n ≥ N, ∃ x y z : ℤ, n = x ^ 2 + y ^ 2 - z ^ 2 ∧ max (x ^ 2) (max (y ^ 2) (z ^ 2)) ≤ n`,
> which gives the statement below by taking absolute values.

```lean
theorem erdos_1148 : ∀ᶠ n in atTop, Erdos1148Prop n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1148.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1148.lean#L56).

## `Erdos1148.erdos_1148.variants.lower_bound`

Textbook result, proved here.

> The integer $6563$ cannot be written as $x^2 + y^2 - z^2$ with $\max(x^2, y^2, z^2) \leq 6563$.

```lean
theorem erdos_1148.variants.lower_bound : ¬ Erdos1148Prop 6563
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1148.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1148.lean#L79).

## `Erdos1148.erdos_1148.variants.weaker`

Solved: stated here without proof.

> [Va99] reports this is 'obvious' if we replace $\leq n$ with $\leq n+2\sqrt{n}$.

```lean
theorem erdos_1148.variants.weaker : ∀ n, erdos_1148_weaker_prop n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1148.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1148.lean#L95).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1148.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1148.lean)
- [erdosproblems.com/1148](https://www.erdosproblems.com/1148)
