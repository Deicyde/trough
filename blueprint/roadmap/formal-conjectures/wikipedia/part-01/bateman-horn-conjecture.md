---
declaration: theorem
origin: cited
lean: BatemanHornConjecture.bateman_horn_conjecture
statement: formalized
---

# Bateman-Horn Conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Bateman%E2%80%93Horn_conjecture)

*Quoted from [FormalConjectures/Wikipedia/BatemanHornConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BatemanHornConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `BatemanHornConjecture.bateman_horn_conjecture`

Open: stated without proof.

> **The Bateman-Horn Conjecture**
> Given a finite collection of distinct irreducible polynomials non-constant $f_1, f_2, \dots, f_k \in \mathbb{Z}[x]$
> with positive leading coefficients that satisfy the Schinzel condition, the number
> of positive integers $n \leq x$ for which all polynomials $f_i$ are simultaneously prime is
> asymptotic to:
>
> $$\frac{C}{D} \frac{x}{(\log x)^k}$$
>
> where $D = \prod_i \deg(f_i)$ and $C$ is the Bateman-Horn constant given by the convergent
> infinite product:
>
> $$C = \prod_{p\in\mathbb{P}} (1 - 1/p)^{-k} (1 - \omega_p/p)$$
>
> Here $\omega_p$ is the number of residue classes modulo $p$ for which at least one polynomial
> vanishes. The product is only conditionally convergent: it is the limit as $N \to \infty$ of the
> partial products over the primes $p < N$.
>
> The Schinzel condition ensures that for each prime $p$, there exists some integer $n$
> such that $p$ does not divide the product $f_1(n) f_2(n) \dotsb f_k(n)$, which guarantees the
> infinite product converges to a positive value.

```lean
theorem bateman_horn_conjecture
    (polys : Finset ℤ[X])
    (h_nonempty : polys.Nonempty)
    (h_irreducible : ∀ f ∈ polys, BunyakovskyCondition f)
    (h_compat : SchinzelCondition polys) :
    ∃ C : ℝ, 0 < C ∧ Tendsto (BatemanHornPartialProduct polys) atTop (𝓝 C) ∧
      (fun x : ℝ => (CountSimultaneousPrimes polys x : ℝ)) ~[atTop]
        (fun x : ℝ => C / DegreesProduct polys * x / (Real.log x) ^ polys.card)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/BatemanHornConjecture.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BatemanHornConjecture.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BatemanHornConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BatemanHornConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Bateman%E2%80%93Horn_conjecture)
