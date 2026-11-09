---
declaration: theorem
origin: cited
lean: OeisA179537.conjecture1, OeisA179537.conjecture2, OeisA179537.conjecture3, OeisA179537.conjecture4
statement: formalized
---

# Central binomial sum $a(n) = \sum_{k=0}^n \binom{n}{k}^2 \binom{n-k}{k}^2 (-16)^k$

> The sequence is defined by
> $$a(n) = \sum_{k=0}^n \binom{n}{k}^2 \binom{n-k}{k}^2 (-16)^k.$$
>
> *References:*
> - [A179537](https://oeis.org/A179537)
> - Z.-W. Sun, "Open Conjectures on Congruences", arXiv preprint
>   [arXiv:0911.5665](https://arxiv.org/abs/0911.5665) [math.NT], 2009-2011.

*Quoted from [FormalConjectures/OEIS/179537.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/179537.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 5 test statements, counted here but not shown.

## `OeisA179537.conjecture1`

Open: stated without proof.

> If $p$ is a prime with $(p/7) = 1$ and $p = x^2 + 7y^2$ with $x, y$ integers, then
> $\sum_{k=0}^{p-1} (-1)^k a(k) \equiv 4x^2 - 2p \pmod{p^2}$.
> - _Zhi-Wei Sun_, Jul 17 2010

```lean
theorem conjecture1 (p : ℕ) [Fact p.Prime] (hp7 : p ≠ 7)
    (h_leg : letI : Fact (Nat.Prime 7) := ⟨by decide⟩; legendreSym 7 p = 1)
    (x y : ℤ) (h_sq : (p : ℤ) = x ^ 2 + 7 * y ^ 2) :
    (∑ k ∈ Finset.range p, (-1 : ℤ) ^ k * a k) ≡
      4 * x ^ 2 - 2 * (p : ℤ) [ZMOD (p : ℤ) ^ 2]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/179537.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/179537.lean#L65).

## `OeisA179537.conjecture2`

Open: stated without proof.

> If $p$ is a prime with $(p/7) = -1$, then
> $\sum_{k=0}^{p-1} (-1)^k a(k) \equiv 0 \pmod{p^2}$.
> - _Zhi-Wei Sun_, Jul 17 2010

```lean
theorem conjecture2 (p : ℕ) [Fact p.Prime] (hp7 : p ≠ 7)
    (h_leg : letI : Fact (Nat.Prime 7) := ⟨by decide⟩; legendreSym 7 p = -1) :
    (∑ k ∈ Finset.range p, (-1 : ℤ) ^ k * a k) ≡ 0 [ZMOD (p : ℤ) ^ 2]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/179537.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/179537.lean#L78).

## `OeisA179537.conjecture3`

Open: stated without proof.

> $\sum_{k=0}^{n-1} (42k + 37) (-1)^k a(k) \equiv 0 \pmod n$ for all $n \ge 1$.
> - _Zhi-Wei Sun_, Jul 17 2010

```lean
theorem conjecture3 (n : ℕ) (hn : 1 ≤ n) :
    (n : ℤ) ∣ ∑ k ∈ Finset.range n, ((42 * (k : ℤ) + 37) * (-1 : ℤ) ^ k * a k)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/179537.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/179537.lean#L88).

## `OeisA179537.conjecture4`

Open: stated without proof.

> $\sum_{k=0}^{p-1} (42k + 37) (-1)^k a(k) \equiv p(21(p/7) + 16) \pmod{p^2}$ for any prime $p \ne 7$.
> - _Zhi-Wei Sun_, Jul 17 2010

```lean
theorem conjecture4 (p : ℕ) [Fact p.Prime] (_hp7 : p ≠ 7) :
    letI : Fact (Nat.Prime 7) := ⟨by decide⟩
    (∑ k ∈ Finset.range p, ((42 * (k : ℤ) + 37) * (-1 : ℤ) ^ k * a k)) ≡
      (p : ℤ) * (21 * legendreSym 7 p + 16) [ZMOD (p : ℤ) ^ 2]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/179537.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/179537.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/179537.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/179537.lean)
- [A179537](https://oeis.org/A179537)
