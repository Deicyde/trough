---
declaration: theorem
origin: cited
lean: OeisA79727.conjecture1, OeisA79727.conjecture2, OeisA79727.conjecture3, OeisA79727.conjecture4
statement: formalized
---

# $a(n) = \sum_{k=0}^n \binom{2k}{k}^3$

> The sequence $a(n) = 1 + \binom{2}{1}^3 + \binom{4}{2}^3 + \cdots + \binom{2n}{n}^3$:
> $$a(n) = \sum_{k=0}^n \binom{2k}{k}^3$$
>
> *References:*
> - [A079727](https://oeis.org/A079727)

*Quoted from [FormalConjectures/OEIS/79727.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/79727.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 5 test statements, counted here but not shown.

## `OeisA79727.conjecture1`

Open: stated without proof.

> Conjecture 1 (Peter Bala, 2024):
> If prime $p$ is in A003625 then $a(p^2) \equiv 8 + p^2 \pmod{p^3}$.

```lean
theorem conjecture1 (p : ℕ) (hp : OeisA3625.A p) :
    a (p ^ 2) ≡ 8 + p ^ 2 [MOD p ^ 3]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/79727.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/79727.lean#L68).

## `OeisA79727.conjecture2`

Open: stated without proof.

> Conjecture 2 (Peter Bala, 2024):
> If prime $p$ is in A003625 then $a(p(p-1)) \equiv p^2 \pmod{p^3}$.

```lean
theorem conjecture2 (p : ℕ) (hp : OeisA3625.A p) :
    a (p * (p - 1)) ≡ p ^ 2 [MOD p ^ 3]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/79727.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/79727.lean#L77).

## `OeisA79727.conjecture3`

Open: stated without proof.

> Conjecture 3 (Peter Bala, 2024):
> If prime $p$ is in A003625 then $a((p^2-1)/2) \equiv p^2 \pmod{p^4}$.

```lean
theorem conjecture3 (p : ℕ) (hp : OeisA3625.A p) :
    a ((p ^ 2 - 1) / 2) ≡ p ^ 2 [MOD p ^ 4]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/79727.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/79727.lean#L86).

## `OeisA79727.conjecture4`

Open: stated without proof.

> Conjecture 4 (Peter Bala, 2024):
> If $n$ is a product of distinct primes from A003625 then $a((n-1)/2)$ is divisible by $n^2$.

```lean
theorem conjecture4 (S : Finset ℕ) (hS : ∀ p ∈ S, OeisA3625.A p) :
    (∏ p ∈ S, p) ^ 2 ∣ a ((∏ p ∈ S, p - 1) / 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/79727.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/79727.lean#L95).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/79727.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/79727.lean)
- [A079727](https://oeis.org/A079727)
