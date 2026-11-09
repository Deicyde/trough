---
declaration: theorem
origin: cited
lean: Mersenne.new_mersenne_conjecture, Mersenne.new_mersenne_conjecture_of_prime, Mersenne.new_mersenne_conjecture.variants.prime, Mersenne.infinitely_many_mersenne_primes, Mersenne.catalans_mersenne_conjecture
statement: formalized
---

# Conjectures about Mersenne primes

> *References:*
> - [Wikipedia: Mersenne conjectures](https://en.wikipedia.org/wiki/Mersenne_conjectures)
> - [Wikipedia: Catalan's Mersenne conjecture](https://en.wikipedia.org/wiki/Catalan%27s_Mersenne_conjecture)
> - [MathWorld: Catalan-Mersenne Number](https://mathworld.wolfram.com/Catalan-MersenneNumber.html)

*Quoted from [FormalConjectures/Wikipedia/Mersenne.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mersenne.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 4 open and 1 textbook result.

## `Mersenne.new_mersenne_conjecture`

Open: stated without proof.

> For any odd natural number `p` if two of the following conditions hold,
> then all three must hold:
> 1. $2^p-1$ is prime
> 2. $(2^p+1)/3$ is prime
> 3. Exists a number `k` such that $p = 2^k \\pm 1$ or $p = 4^k \\pm 3$

```lean
theorem new_mersenne_conjecture (p : ℕ) (hp : Odd p) :
    NewMersenneConjectureStatement p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mersenne.lean#L80).

## `Mersenne.new_mersenne_conjecture_of_prime`

Textbook result, proved here.

> It suffices to check this conjecture for odd primes. The statement fails at `p = 2`:
> `mersenne 2 = 3` is prime and `2 = 2 ^ 0 + 1`, but `2` gives no Wagstaff prime.

```lean
theorem new_mersenne_conjecture_of_prime :
    (∀ p, p.Prime → Odd p → NewMersenneConjectureStatement p) →
    ∀ p, Odd p → NewMersenneConjectureStatement p
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mersenne.lean#L87).

## `Mersenne.new_mersenne_conjecture.variants.prime`

Open: stated without proof.

> The New Mersenne Conjecture statement holds for odd primes.

```lean
theorem new_mersenne_conjecture.variants.prime (p : ℕ) (hp : p.Prime) (h : Odd p) :
    NewMersenneConjectureStatement p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mersenne.lean#L127).

## `Mersenne.infinitely_many_mersenne_primes`

Open: stated without proof.

> Are there infinitely many Mersenne primes?

```lean
theorem infinitely_many_mersenne_primes :
  Set.Infinite { p : ℕ | (mersenne p).Prime }
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mersenne.lean#L135).

## `Mersenne.catalans_mersenne_conjecture`

Open: stated without proof.

> The first five Catalan-Mersenne numbers $c_0, \ldots, c_4$ are known to be prime.
> Catalan conjectured that they are prime "up to a certain limit".
> Are all Catalan-Mersenne numbers $c_n$ with $n \geq 5$ prime?

```lean
theorem catalans_mersenne_conjecture :
    ∀ n ≥ 5, Nat.Prime (catalanMersenne n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Mersenne.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mersenne.lean#L145).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Mersenne.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Mersenne.lean)
- [Wikipedia: Mersenne conjectures](https://en.wikipedia.org/wiki/Mersenne_conjectures)
