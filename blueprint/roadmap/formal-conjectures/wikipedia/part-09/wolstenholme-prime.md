---
declaration: theorem
origin: cited
lean: WolstenholmePrime.wolstenholme_theorem, WolstenholmePrime.wolstenholme_bernoulli, WolstenholmePrime.wolstenholme_harmonic, WolstenholmePrime.wolstenholme_prime_infinite
statement: formalized
---

# Wolstenholme Prime

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Wolstenholme_prime)

*Quoted from [FormalConjectures/Wikipedia/WolstenholmePrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WolstenholmePrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 textbook results. It also has 2 test statements, counted here but not shown.

## `WolstenholmePrime.wolstenholme_theorem`

Textbook result, stated without proof. A Lean proof is at [https://github.com/mo271/formal-conjectures/blob/d833ed31d82693f10bed7a4c9ac329545b556a03/FormalConjectures/Wikipedia/WolstenholmePrime.lean#L34](https://github.com/mo271/formal-conjectures/blob/d833ed31d82693f10bed7a4c9ac329545b556a03/FormalConjectures/Wikipedia/WolstenholmePrime.lean#L34).

> Wolstenholme's theorem states that any prime $p > 3$ satisfies $\binom{2p-1}{p-1} \equiv 1 (\pmod{p^3})$.
>
> Formal proof linked here provided by AlphaProof.
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Wolstenholme%27s_theorem)

```lean
theorem wolstenholme_theorem (p : ℕ) (h : p > 3) (hp : Nat.Prime p) :
    (2 * p - 1).choose (p - 1) ≡ 1 [MOD p ^ 3]
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WolstenholmePrime.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WolstenholmePrime.lean#L39).

## `WolstenholmePrime.wolstenholme_bernoulli`

Textbook result, stated without proof.

> Equivalently, a prime $p > 7$ is a Wolstenholme prime if it divides the numerator of the Bernoulli number $B_{p-3}$.

```lean
theorem wolstenholme_bernoulli (p : ℕ) : IsWolstenholmePrime p ↔
    (p > 7) ∧ Nat.Prime p ∧ ↑p ∣ (bernoulli' (p - 3)).num
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WolstenholmePrime.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WolstenholmePrime.lean#L71).

## `WolstenholmePrime.wolstenholme_harmonic`

Textbook result, stated without proof.

> Another equivalent definition is that a prime $p > 7$ is a Wolstenholme prime
> if it $p^3$ divides the numerator of the harmonic number $H_{p-1}$.

```lean
theorem wolstenholme_harmonic (p : ℕ) : IsWolstenholmePrime p ↔
    (p > 7) ∧ Nat.Prime p ∧ ↑(p ^ 3) ∣ (harmonic (p - 1)).num
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WolstenholmePrime.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WolstenholmePrime.lean#L80).

## `WolstenholmePrime.wolstenholme_prime_infinite`

Open: stated without proof.

> It is conjectured that there are infinitely many Wolstenholme primes.
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Wolstenholme_prime#Expected_number_of_Wolstenholme_primes)

```lean
theorem wolstenholme_prime_infinite :
    {p : ℕ | IsWolstenholmePrime p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WolstenholmePrime.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WolstenholmePrime.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/WolstenholmePrime.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/WolstenholmePrime.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Wolstenholme_prime)
