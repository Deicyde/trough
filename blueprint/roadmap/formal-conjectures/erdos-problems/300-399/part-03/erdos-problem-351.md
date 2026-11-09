---
declaration: theorem
origin: cited
lean: Erdos351.erdos_351, Erdos351.erdos_351.variants.X, Erdos351.erdos_351.variants.X_sq
statement: formalized
---

# Erdős Problem 351

> *Reference:* [erdosproblems.com/351](https://www.erdosproblems.com/351)

*Quoted from [FormalConjectures/ErdosProblems/351.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/351.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/351](https://www.erdosproblems.com/351).

The file states 3 research or textbook statements: 3 solved.

## `Erdos351.erdos_351`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos351.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos351.lean).

> Let $p(x) \in \mathbb{Q}[x]$ be a non-constant rational polynomial with positive leading
> coefficient. Is it true that
>
> $$A=\{ p(n)+1/n : n \in \mathbb{N}\}$$
>
> is strongly complete,
> in the sense that, for any finite set $B$,
>
> $$\left\{\sum_{a \in X} a : X \subseteq A \setminus B, X \textrm{ is finite}\right\}$$
>
> contains all sufficiently large integers?

```lean
theorem erdos_351 :
    ∀ P : ℚ[X], 0 < P.natDegree → 0 < P.leadingCoeff → HasCompleteImage P
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/351.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/351.lean#L58).

## `Erdos351.erdos_351.variants.X`

Solved: stated here without proof.

> Let $p(x) = x \in \mathbb{Q}[x]$. It has been shown that
>
> $$A=\{ p(n)+1/n : n \in \mathbb{N}\}$$
>
> is strongly complete, in the sense that, for any finite set $B$,
>
> $$\left\{\sum_{a \in X} a : X \subseteq A \setminus B, X \textrm{ is finite}\right\}$$
>
> contains all sufficiently large integers.

```lean
protected theorem erdos_351.variants.X : HasCompleteImage X
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/351.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/351.lean#L70).

## `Erdos351.erdos_351.variants.X_sq`

Solved: stated here without proof.

> Let $p(x) = x ^ 2 \in \mathbb{Q}[x]$. It has been shown that
>
> $$A=\{ p(n)+1/n : n \in \mathbb{N}\}$$
>
> is strongly complete, in the sense that, for any finite set $B$,
>
> $$\left\{\sum_{a \in X} a : X \subseteq A \setminus B, X \textrm{ is finite}\right\}$$
>
> contains all sufficiently large integers.

```lean
theorem erdos_351.variants.X_sq : HasCompleteImage (X ^ 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/351.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/351.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/351.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/351.lean)
- [erdosproblems.com/351](https://www.erdosproblems.com/351)
