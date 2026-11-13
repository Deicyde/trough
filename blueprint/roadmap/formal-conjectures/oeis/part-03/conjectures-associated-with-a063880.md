---
declaration: theorem
origin: cited
lean: OeisA63880.mod_216_of_a, OeisA63880.powerful_of_isPrimitiveTerm, OeisA63880.unique_primitive_108, OeisA63880.a_of_primitive_mul_squarefree, OeisA63880.exists_primitive_of_a
statement: formalized
---

# Conjectures associated with A063880

> A063880 lists numbers $n$ such that $\sigma(n) = 2 \cdot \text{usigma}(n)$, where $\sigma(n)$ is the
> sum of all divisors and $\text{usigma}(n)$ is the sum of unitary divisors.
>
> Equivalently, these are numbers whose unitary and non-unitary divisors have equal sum.
>
> The conjectures state that all members satisfy $n \equiv 108 \pmod{216}$, and that all
> primitive terms (those whose proper divisors aren't in the sequence) are powerful numbers,
> with $108$ being the only primitive term.
>
> *References:*
> - [A063880](https://oeis.org/A063880)

*Quoted from [FormalConjectures/OEIS/63880.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/63880.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open, 1 solved and 2 textbook results. It also has 4 test statements and 6 API statements, counted here but not shown.

## `OeisA63880.mod_216_of_a`

Open: stated without proof.

> All members of the sequence satisfy $n \equiv 108 \pmod{216}$.

```lean
theorem mod_216_of_a {n : ℕ} (h : A n) : n % 216 = 108
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/63880.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/63880.lean#L86).

## `OeisA63880.powerful_of_isPrimitiveTerm`

Textbook result, proved here.

> All primitive terms are powerful numbers: if `p` divided `n` exactly once, then `n / p` would
> also be in the sequence.

```lean
theorem powerful_of_isPrimitiveTerm {n : ℕ} (h : IsPrimitiveTerm n) : n.Powerful
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/63880.lean, line 205](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/63880.lean#L205).

## `OeisA63880.unique_primitive_108`

Open: stated without proof.

> $108$ is the only primitive term.

```lean
theorem unique_primitive_108 {n : ℕ} (h : IsPrimitiveTerm n) : n = 108
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/63880.lean, line 220](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/63880.lean#L220).

## `OeisA63880.a_of_primitive_mul_squarefree`

Textbook result, proved here.

> If $m$ is a primitive term and $s$ is squarefree with $\gcd(m, s) = 1$, then $m \cdot s$
> is in the sequence.

```lean
theorem a_of_primitive_mul_squarefree (m s : ℕ) (hm : IsPrimitiveTerm m)
    (hs : Squarefree s) (hcoprime : m.Coprime s) : A (m * s)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/63880.lean, line 226](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/63880.lean#L226).

## `OeisA63880.exists_primitive_of_a`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA63880_exists_primitive_of_a.lean#L491](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_OeisA63880_exists_primitive_of_a.lean#L491).

> Non-primitive terms have the form $m \cdot s$ where $m$ is primitive and $s$ is
> squarefree with $\gcd(m, s) = 1$.

```lean
theorem exists_primitive_of_a {n : ℕ} (h : A n) :
    ∃ m s, IsPrimitiveTerm m ∧ Squarefree s ∧ m.Coprime s ∧ n = m * s
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/63880.lean, line 234](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/63880.lean#L234).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/63880.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/63880.lean)
- [A063880](https://oeis.org/A063880)
