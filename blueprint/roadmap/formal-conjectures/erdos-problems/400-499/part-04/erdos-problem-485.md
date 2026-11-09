---
declaration: theorem
origin: cited
lean: Erdos485.erdos_485
statement: formalized
---

# Erdős Problem 485

> *References:*
> - [erdosproblems.com/485](https://www.erdosproblems.com/485)
> - [Re47] Rényi, A., *On the minimal number of terms of the square of a polynomial*. Hungarica Acta
>   Math. (1947), 30-34.
> - [Er49b] Erdős, P., *On the number of terms of the square of a polynomial*. Nieuw Arch. Wiskunde
>   (2) (1949), 63-65.
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Ha74] Hayman, W. K., *Research problems in function theory: new problems*. (1974), 155--180.
> - [Sc87] Schinzel, A., *On the number of terms of a power of a polynomial*. Acta Arith. (1987),
>   55-70.
> - [ScZa09] Schinzel, Andrzej and Zannier, Umberto, *On the number of terms of a power of a
>   polynomial*. Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl. (2009), 95-98.

*Quoted from [FormalConjectures/ErdosProblems/485.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/485.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/485](https://www.erdosproblems.com/485).

The file states 1 research or textbook statement: 1 solved.

## `Erdos485.erdos_485`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos485.lean#L39](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos485.lean#L39).

> Let $f(k)$ be the minimum number of terms in $P(x)^2$, where $P \in \mathbb{Q}[x]$ ranges over all
> polynomials with exactly $k$ non-zero terms. Is it true that $f(k) \to \infty$ as $k \to \infty$?
>
> A conjecture of Erdős and Rényi (this is Problem 4.4 in [Ha74], attributed to Erdős); the
> function was first investigated by Rényi and Rédei [Re47], and Erdős [Er49b] proved that
> $f(k) < k^{1-c}$ for some $c > 0$. The answer is yes: Schinzel [Sc87] proved
> $f(k) > \log \log k / \log 2$, and Schinzel and Zannier [ScZa09] improved this to
> $f(k) \gg \log k$.

```lean
theorem erdos_485 : Tendsto f atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/ErdosProblems/485.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/485.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/485.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/485.lean)
- [erdosproblems.com/485](https://www.erdosproblems.com/485)
