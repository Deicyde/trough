---
declaration: theorem
origin: cited
lean: Lemoine.lemoine_conjecture, Lemoine.lemoine_conjecture_extension
statement: formalized
---

# Lemoine's conjectures

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/%C3%89mile_Lemoine#Lemoine's_conjecture_and_extensions)
> - [Ki85] Kiltinen, J. and Young P. (1985). Goldbach, Lemoine, and a Know/Don't Know Problem.

*Quoted from [FormalConjectures/Wikipedia/Lemoine.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Lemoine.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `Lemoine.lemoine_conjecture`

Open: stated without proof.

> For all odd integers $n ≥ 7$ there are prime numbers $p,q$ such that $n = p+2q$.

```lean
theorem lemoine_conjecture (n : ℕ) (hn : 6 < n) (odd : Odd n) :
    ∃ (p q : ℕ), p.Prime ∧ q.Prime ∧ p + 2 * q = n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Lemoine.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Lemoine.lean#L39).

## `Lemoine.lemoine_conjecture_extension`

Open: stated without proof.

> For all odd integers $n ≥ 9$ there are odd prime numbers $p,q,r,s$ and natural numbers $a,b$
> such that $p+2q = n$, $2+pq = 2^a+r$, $2p+q = 2^b+s$

```lean
theorem lemoine_conjecture_extension (n : ℕ) (hn : 8 < n) (odd : Odd n) :
    ∃ (p q r s a b : ℕ), OddPrime p ∧ OddPrime q ∧ OddPrime r ∧ OddPrime s ∧
    p + 2 * q = n ∧ 2 + p * q = 2 ^ a + r ∧ 2 * p + q = 2 ^ b + s
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Lemoine.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Lemoine.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Lemoine.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Lemoine.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/%C3%89mile_Lemoine#Lemoine's_conjecture_and_extensions)
