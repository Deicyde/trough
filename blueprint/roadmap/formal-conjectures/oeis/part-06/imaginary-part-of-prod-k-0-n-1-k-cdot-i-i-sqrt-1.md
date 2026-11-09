---
declaration: theorem
origin: cited
lean: OeisA105751.prime_divides_some_term, OeisA105751.conjecture, OeisA105751.conjecture.variants.moll_p_mod_4_eq_1
statement: formalized
---

# Imaginary part of $\prod_{k=0}^n (1 + k \cdot i)$, $i = \sqrt{-1}$

> *References:*
> - [A105751](https://oeis.org/A105751)

*Quoted from [FormalConjectures/OEIS/105751.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105751.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result. It also has 5 test statements, counted here but not shown.

## `OeisA105751.prime_divides_some_term`

Textbook result, stated without proof.

> Numerical calculation suggests that a similar division holds in this case.
> Type 1: primes p that do not divide any element of the sequence {$a(n)$}.
> In this case, unlike in A105750, the set of type 1 primes is empty;
> that is, every prime p divides some term of this sequence.
>
> Note: The triangular number n*(n+1)/2 divides $a(n)$ (see A164652).
> In particular, if $p$ is an odd prime then $p$ divides $a(p)$. For $p=2$, $2$ divides $a(4)=-40$.

```lean
theorem prime_divides_some_term (p : ℕ) (hp : p.Prime) :
    ∃ n : ℕ, a n ≠ 0 ∧ (p : ℤ) ∣ a n
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/105751.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105751.lean#L72).

## `OeisA105751.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a105751-two-adic/blob/a9692d90078c4dff1478acaaa70be2fba06a3ef9/lean/OeisA105751TwoAdicFC.lean#L980-L985](https://github.com/KitaKen1/oeis-a105751-two-adic/blob/a9692d90078c4dff1478acaaa70be2fba06a3ef9/lean/OeisA105751TwoAdicFC.lean#L980-L985).

> Moll's conjecture 5.5 extends to this sequence and takes the form:
> (i) the $2$-adic valuation $\nu_2(a(n)) \sim n/4$ as n -> oo.

```lean
theorem conjecture :
    Tendsto (fun n ↦ (4 : ℚ) * (padicValInt 2 (a n) : ℚ) / (n : ℚ)) atTop (nhds 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/105751.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105751.lean#L84).

## `OeisA105751.conjecture.variants.moll_p_mod_4_eq_1`

Open: stated without proof.

> Moll's conjecture 5.5 extends to this sequence and takes the form:
> (ii) for the other primes of type $2$, the p-adic valuation
> $\nu_p(a(n)) \sim n/(p - 1)$ as $n \rightarrow \infty$.
>
> (Type 2 primes consists of primes p == 1 (mod 4))

```lean
theorem conjecture.variants.moll_p_mod_4_eq_1 {p : ℕ} (hp : p.Prime) (h_mod : p % 4 = 1) :
    Tendsto (fun n ↦ ((p - 1 : ℚ) * (padicValInt p (a n) : ℚ)) / (n : ℚ)) atTop (nhds 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/105751.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105751.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/105751.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/105751.lean)
- [A105751](https://oeis.org/A105751)
