---
declaration: theorem
origin: cited
lean: OeisA179524.conjecture1, OeisA179524.conjecture2, OeisA179524.conjecture3, OeisA179524.conjecture4, OeisA179524.conjecture5
statement: formalized
---

# Central binomial sum $a(n) = \sum_{k=0}^n (-4)^k \binom{n}{k}^2 \binom{n-k}{k}^2$

> The sequence is defined by
>
> $$a(n) = \sum_{k=0}^n (-4)^k \binom{n}{k}^2 \binom{n-k}{k}^2.$$
>
> *References:*
> - [A179524](https://oeis.org/A179524)
> - Z.-W. Sun, "Open Conjectures on Congruences", arXiv preprint
>   [arXiv:0911.5665](https://arxiv.org/abs/0911.5665) [math.NT], 2009-2011.

*Quoted from [FormalConjectures/OEIS/179524.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/179524.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 5 test statements, counted here but not shown.

## `OeisA179524.conjecture1`

Open: stated without proof.

> If $p$ is a prime with $p \equiv 1, 9 \pmod{20}$ and $p = x^2 + 5y^2$ with $x, y$ integers,
> then $\sum_{k=0}^{p-1} a(k) \equiv 4x^2 - 2p \pmod{p^2}$.
> - _Zhi-Wei Sun_, Jul 01 2010

```lean
theorem conjecture1 (p : ℕ) (hp : p.Prime)
    (h_mod : (p : ℤ) ≡ 1 [ZMOD 20] ∨ (p : ℤ) ≡ 9 [ZMOD 20])
    (x y : ℤ) (h_sq : (p : ℤ) = x ^ 2 + 5 * y ^ 2) :
    ∑ k ∈ Finset.range p, a k ≡ 4 * x ^ 2 - 2 * (p : ℤ) [ZMOD (p : ℤ) ^ 2]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/179524.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/179524.lean#L60).

## `OeisA179524.conjecture2`

Open: stated without proof.

> If $p$ is a prime with $p \equiv 3, 7 \pmod{20}$ and $2p = x^2 + 5y^2$ with $x, y$ integers,
> then $\sum_{k=0}^{p-1} a(k) \equiv 2x^2 - 2p \pmod{p^2}$.
> - _Zhi-Wei Sun_, Jul 01 2010

```lean
theorem conjecture2 (p : ℕ) (hp : p.Prime)
    (h_mod : (p : ℤ) ≡ 3 [ZMOD 20] ∨ (p : ℤ) ≡ 7 [ZMOD 20])
    (x y : ℤ) (h_sq : 2 * (p : ℤ) = x ^ 2 + 5 * y ^ 2) :
    ∑ k ∈ Finset.range p, a k ≡ 2 * x ^ 2 - 2 * (p : ℤ) [ZMOD (p : ℤ) ^ 2]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/179524.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/179524.lean#L72).

## `OeisA179524.conjecture3`

Open: stated without proof.

> If $p$ is a prime with $p \equiv 11, 13, 17, 19 \pmod{20}$,
> then $\sum_{k=0}^{p-1} a(k) \equiv 0 \pmod{p^2}$.
> - _Zhi-Wei Sun_, Jul 01 2010

```lean
theorem conjecture3 (p : ℕ) (hp : p.Prime)
    (h_mod : (p : ℤ) ≡ 11 [ZMOD 20] ∨ (p : ℤ) ≡ 13 [ZMOD 20] ∨
      (p : ℤ) ≡ 17 [ZMOD 20] ∨ (p : ℤ) ≡ 19 [ZMOD 20]) :
    ∑ k ∈ Finset.range p, a k ≡ 0 [ZMOD (p : ℤ) ^ 2]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/179524.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/179524.lean#L84).

## `OeisA179524.conjecture4`

Open: stated without proof.

> $\sum_{k=0}^{n-1}(20k+17)a(k) \equiv 0 \pmod n$ for all $n=1,2,3,\dots$.
> - _Zhi-Wei Sun_, Jul 01 2010

```lean
theorem conjecture4 (n : ℕ) (hn : 1 ≤ n) :
    (n : ℤ) ∣ ∑ k ∈ Finset.range n, ((20 * (k : ℤ) + 17) * a k)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/179524.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/179524.lean#L95).

## `OeisA179524.conjecture5`

Open: stated without proof.

> $\sum_{k=0}^{p-1}(20k+17)a(k) \equiv p(10(-1/p)+7) \pmod{p^2}$ for any odd prime $p$.
> - _Zhi-Wei Sun_, Jul 01 2010

```lean
theorem conjecture5 (p : ℕ) [hp : Fact p.Prime] (_hp2 : p ≠ 2) :
    (∑ k ∈ Finset.range p, ((20 * (k : ℤ) + 17) * a k)) ≡
      (p : ℤ) * (10 * legendreSym p (-1) + 7) [ZMOD (p : ℤ) ^ 2]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/179524.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/179524.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/179524.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/179524.lean)
- [A179524](https://oeis.org/A179524)
