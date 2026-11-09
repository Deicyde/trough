---
declaration: theorem
origin: cited
lean: CarmichaelTotient.carmichealTotientFor_odd, CarmichaelTotient.charmichaelTotient, CarmichaelTotient.carchimaelTotient_bound
statement: formalized
---

# Carmichael's totient function conjecture

> For every positive natural number $n$, there exists a natural number $m$ with $m ≠ n$, such that
> $φ(n) = φ(m)$ where $φ$ is the Euler totient function.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Carmichael%27s_totient_function_conjecture)
> - [F1998] Kevin Ford. The distribution of totients. https://arxiv.org/abs/1104.3264

*Quoted from [FormalConjectures/Wikipedia/CarmichaelTotient.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CarmichaelTotient.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result. It also has 1 test statement, counted here but not shown.

## `CarmichaelTotient.carmichealTotientFor_odd`

Textbook result, proved here.

> For every odd number $n$, $φ(2n) = φ(n)$

```lean
theorem carmichealTotientFor_odd {n : ℕ} (hn : Odd n) : CarmichaelTotientFor n
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CarmichaelTotient.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CarmichaelTotient.lean#L51).

## `CarmichaelTotient.charmichaelTotient`

Open: stated without proof.

> *Carmichael's totient function conjecture*: For every positive natural number $n$,
> there exists a natural number $m$ with $m ≠ n$, such that $φ(n) = φ(m)$.

```lean
theorem charmichaelTotient :
    ∀ ⦃n : ℕ⦄, 0 < n → CarmichaelTotientFor n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CarmichaelTotient.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CarmichaelTotient.lean#L59).

## `CarmichaelTotient.carchimaelTotient_bound`

Solved: stated here without proof.

> In Theorem 6 in [F1998], Kevin Ford proves that the smallest counterexample to
> Carmichael's totient function conjecture must be $≥ 10 ^ (10 ^ 10)$

```lean
theorem carchimaelTotient_bound {n : ℕ} (hn : 0 < n) (hn' : n < 10 ^ (10 ^ 10)) :
    CarmichaelTotientFor n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CarmichaelTotient.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CarmichaelTotient.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/CarmichaelTotient.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CarmichaelTotient.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Carmichael%27s_totient_function_conjecture)
