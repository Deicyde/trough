---
declaration: theorem
origin: cited
lean: AgrawalConjecture.agrawal_conjecture, AgrawalConjecture.agrawal_conjecture.variants.popovych
statement: formalized
---

# Agrawal's conjecture

> Agrawal's conjecture is a stronger version of the theorem that forms the basis
> of the AKS primality test. If true, it would significantly improve the
> efficiency of primality testing.
>
> The conjecture states that for coprime $n$ and $r$, if the polynomial congruence
> $(X-1)^n \equiv X^n-1 \pmod{n, X^r-1}$ holds, then $n$ is either prime or $n^2 \equiv 1 \pmod{r}$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Agrawal%27s_conjecture)
> - [AIM Math](https://aimath.org/WWN/primesinp/articles/html/50a/)
> - [Paper](https://eprint.iacr.org/2009/008.pdf)

*Quoted from [FormalConjectures/Wikipedia/Agrawal.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Agrawal.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `AgrawalConjecture.agrawal_conjecture`

Open: stated without proof.

> **Agrawal's Primality Conjecture.**
>
> Does the congruence $(X-1)^n \equiv X^n - 1 \pmod{n, X^r-1}$ imply
> $n$ is prime (with a specific exception for $n^2 \equiv 1 \pmod{r}$)?
>
> While the "if" direction is a known theorem, the "only if" direction
> remains a conjecture.

```lean
theorem agrawal_conjecture :
    ∀ (n r : ℕ), n > 1 → r > 0 → n.gcd r = 1 →
      let R := Polynomial (ZMod n)
      let X : R := Polynomial.X
      let I : Ideal R := Ideal.span ({X^r - 1} : Set R)
      Ideal.Quotient.mk I ((X - 1)^n) = Ideal.Quotient.mk I (X^n - 1) →
      (n.Prime ∨ (n^2 : ZMod r) = 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Agrawal.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Agrawal.lean#L52).

## `AgrawalConjecture.agrawal_conjecture.variants.popovych`

Open: stated without proof.

> **Roman B. Popovych Conjecture.**
> A stronger version of Agrawal's conjecture, which also considers the congruence
> $(X+2)^n \equiv X^n + 2 \pmod{n, X^r-1}$.
> If both congruences hold, then $n$ is either prime or $n^2 \equiv 1 \pmod{r}$.
> This variant was proposed by Roman B. Popovych in 2018.

```lean
theorem agrawal_conjecture.variants.popovych :
  ∀ (n r : ℕ), n > 1 → r > 0 → n.gcd r = 1 →
    let R := Polynomial (ZMod n)
    let X : R := Polynomial.X
    let I : Ideal R := Ideal.span ({X^r - 1} : Set R)
    Ideal.Quotient.mk I ((X - 1)^n) = Ideal.Quotient.mk I (X^n - 1) →
    Ideal.Quotient.mk I ((X + 2)^n) = Ideal.Quotient.mk I (X^n + 2) →
    (n.Prime ∨ (n^2 : ZMod r) = 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Agrawal.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Agrawal.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Agrawal.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Agrawal.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Agrawal%27s_conjecture)
