---
declaration: theorem
origin: cited
lean: OeisA228304.conjecture_1, OeisA228304.conjecture_2
statement: formalized
---

# Alternating sum of fourth powers of binomial coefficients

> The sequence is defined by
>
> $$a(n) = \sum_{k=0}^n \binom{n}{k}^4 (-1)^k.$$
>
> *References:*
> - [A228304](https://oeis.org/A228304)
> - [arXiv:2608.11941](https://arxiv.org/abs/2608.11941)

*Quoted from [FormalConjectures/OEIS/228304.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228304.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 5 test statements, counted here but not shown.

## `OeisA228304.conjecture_1`

Solved: stated here without proof.

> Conjecture: Let $p$ be any odd prime, and let $A(p)$ be the $p \times p$ determinant with
> $(i,j)$-entry equal to $a(i+j)$ for all $i, j = 0, \dots, p-1$. Then
> $A(p) \equiv (-1)^{(p-1)/2} \pmod p$.
>
> Proved in [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture_1 (p : ℕ) (hp : p.Prime) (hodd : p ≠ 2) :
    let A : Matrix (Fin p) (Fin p) ℤ := fun i j => a (i.val + j.val)
    A.det ≡ (-1 : ℤ) ^ ((p - 1) / 2) [ZMOD p]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228304.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228304.lean#L72).

## `OeisA228304.conjecture_2`

Solved: stated here without proof.

> Conjecture: Let $p$ be any odd prime, and let $C(p)$ be the $p \times p$ determinant with
> $(i,j)$-entry equal to $c(i+j)$ for all $i, j = 0, \dots, p-1$. Then $C(p) \equiv 1 \pmod p$.
>
> Proved in [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture_2 (p : ℕ) (hp : p.Prime) (hodd : p ≠ 2) :
    let C : Matrix (Fin p) (Fin p) ℤ := fun i j => c (i.val + j.val)
    C.det ≡ 1 [ZMOD p]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228304.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228304.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/228304.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228304.lean)
- [A228304](https://oeis.org/A228304)
