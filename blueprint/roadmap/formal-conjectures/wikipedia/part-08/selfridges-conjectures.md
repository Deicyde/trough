---
declaration: theorem
origin: cited
lean: Selfridge.selfridge_conjecture, Selfridge.selfridge_conjecture.variants.exist_pseudo_counterexample, Selfridge.selfridge_conjecture.variants.pseudo_counterexample, Selfridge.selfridge_conjecture.variants.pseudo_counterexample', Selfridge.selfridge_seq_conjecture, Selfridge.selfridge_seq_conjecture.variants.sufficient_condition
statement: formalized
---

# Selfridge's conjectures

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/John_Selfridge#Selfridge's_conjecture_about_primality_testing)

*Quoted from [FormalConjectures/Wikipedia/Selfridge.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Selfridge.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 2 open, 1 solved and 3 textbook results.

## `Selfridge.selfridge_conjecture`

Open: stated without proof.

> **PSW conjecture** (Selfridge's test)
> Let $p$ be an odd number, with $p \equiv \pm 2 \pmod{5}$, $2^{p-1} \equiv 1 \pmod{p}$
> and $F_{p+1} \equiv 0 \pmod{p}$, then $p$ is a prime number.

```lean
theorem selfridge_conjecture (p : ℕ) (hp : IsSelfridge p) : p.Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Selfridge.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Selfridge.lean#L73).

## `Selfridge.selfridge_conjecture.variants.exist_pseudo_counterexample`

Textbook result, proved here.

> Selfridge's test variant:
> Let $p$ be an odd number, with $p \equiv \pm 1 \pmod{5}$, $2^{p-1} \equiv 1 \pmod{p}$
> and $F_{p-1} \equiv 0 \pmod{p}$, then $p$ is a prime number.
>
> This test does not work.

```lean
theorem selfridge_conjecture.variants.exist_pseudo_counterexample :
    ∃ n > 1, IsPseudoSelfridge n ∧ ¬ n.Prime
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Selfridge.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Selfridge.lean#L84).

## `Selfridge.selfridge_conjecture.variants.pseudo_counterexample`

Textbook result, proved here.

> Selfridge's test variant:
> Let $p$ be an odd number, with $p \equiv \pm 1 \pmod{5}$, $2^{p-1} \equiv 1 \pmod{p}$
> and $F_{p-1} \equiv 0 \pmod{p}$, then $p$ is a prime number.
>
> The number $6601$ is a conterexample to this test satisfying $6601 ≡ 1 \mod 5$

```lean
theorem selfridge_conjecture.variants.pseudo_counterexample :
    IsPseudoSelfridge 6601 ∧ ¬ (6601).Prime ∧ 6601 ≡ 1 [MOD 5]
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Selfridge.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Selfridge.lean#L98).

## `Selfridge.selfridge_conjecture.variants.pseudo_counterexample'`

Textbook result, proved here.

> Selfridge's test variant:
> Let $p$ be an odd number, with $p \equiv \pm 1 \pmod{5}$, $2^{p-1} \equiv 1 \pmod{p}$
> and $F_{p-1} \equiv 0 \pmod{p}$, then $p$ is a prime number.
>
> The number $30889$ is a conterexample to this test satisfying $30889 ≡ - 1 \mod 5$

```lean
theorem selfridge_conjecture.variants.pseudo_counterexample' :
    IsPseudoSelfridge 30889 ∧ ¬ (30889).Prime ∧ 30889 ≡ 4 [MOD 5]
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Selfridge.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Selfridge.lean#L111).

## `Selfridge.selfridge_seq_conjecture`

Open: stated without proof.

> Selfridge conjectured that the number of prime factors of the `n`-th Fermat number does not grow
> monotonically in $n$.

```lean
theorem selfridge_seq_conjecture : ¬ Monotone fermatFactors
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Selfridge.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Selfridge.lean#L136).

## `Selfridge.selfridge_seq_conjecture.variants.sufficient_condition`

Proved here.

> Selfridge conjectured that the number of prime factors of the `n`-th Fermat number does not grow
> monotonically in $n$.
>
> A sufficient condition for this conjecture to hold is that there exists a Fermat prime larger than
> 65537.

```lean
theorem selfridge_seq_conjecture.variants.sufficient_condition (n : ℕ) (hn : Prime n.fermatNumber)
    (hn' : n ≥ 5) : type_of% selfridge_seq_conjecture
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Selfridge.lean, line 147](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Selfridge.lean#L147).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Selfridge.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Selfridge.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/John_Selfridge#Selfridge's_conjecture_about_primality_testing)
