---
declaration: theorem
origin: cited
lean: Erdos418.erdos_418, Erdos418.erdos_418.variants.conditional, Erdos418.erdos_418.variants.odd_noncototient, Erdos418.erdos_418.variants.sigma, Erdos418.erdos_418.variants.soln, Erdos418.erdos_418.variants.density
statement: formalized
---

# Erdős Problem 418

> *References:*
> - [erdosproblems.com/418](https://www.erdosproblems.com/418)
> - [Wikipedia: Noncototient](https://en.wikipedia.org/wiki/Noncototient)
> - [BaLu05] Banks, William D. and Luca, Florian, Nonaliquots and {R}obbins numbers. Colloq. Math.
>   (2005), 27--32.
> - [BrSc95] Browkin, J. and Schinzel, A., On integers not of the form {$n-\phi(n)$}. Colloq. Math.
>   (1995), 55-58.
> - [ChZh11] Chen, Yong-Gao and Zhao, Qing-Qing, Nonaliquot numbers. Publ. Math. Debrecen (2011),
>   439--442.
> - [Er73b] Erdős, P., \"Über die Zahlen der Form $\sigma (n)-n$ und $n-\phi(n)$. Elem. Math.
>   (1973), 83-86.
> - [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.
> - [PoPo16] Pollack, Paul and Pomerance, Carl, Some problems of Erdős on the sum-of-divisors
>   function. Trans. Amer. Math. Soc. Ser. B (2016), 1-26.

*Quoted from [FormalConjectures/ErdosProblems/418.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/418.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/418](https://www.erdosproblems.com/418).

The file states 6 research or textbook statements: 2 open and 4 solved. It also has 1 test statement, counted here but not shown.

## `Erdos418.erdos_418`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos418.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos418.lean).

> Are there infinitely many integers not of the form $n - \phi(n)$?
>
> Asked by Erdős and Sierpiński. Numbers not of the form we call non-cototients.
>
> Browkin and Schinzel [BrSc95] provided an affirmative answer to this question, proving that any
> integer of the shape $2^{k}\cdot 509203$ for $k\geq 1$ is a non-cototient.
>
> This is discussed in problem B36 of Guy's collection [Gu04].
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_418 : { (n - n.totient : ℕ) | n }ᶜ.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/418.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/418.lean#L59).

## `Erdos418.erdos_418.variants.conditional`

Proved here.

> It follows from a slight strengthening of the Goldbach conjecture that every odd number can be
> written as $n - \phi(n)$.
> In particular, we assume that every even number greater than 6 can be written as the sum of two
> *distinct* primes, in contrast to the usual Goldbach conjecture that every even number greater than
> 2 can be written as the sum of two primes.

```lean
theorem erdos_418.variants.conditional
    (goldbach : ∀ (n : ℕ), 6 < n → Even n → ∃ p q, p ≠ q ∧ p.Prime ∧ q.Prime ∧ n = p + q)
    (m : ℕ) (h : Odd m) :
    ∃ n, m + n.totient = n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/418.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/418.lean#L70).

## `Erdos418.erdos_418.variants.odd_noncototient`

Open: stated without proof.

> The **Odd Noncototient Conjecture**: every non-cototient is even. Equivalently, every odd natural
> number is of the form $n - \phi(n)$ for some $n$.
>
> This is the unconditional form of `erdos_418.variants.conditional`, which derives the odd case from a
> strengthening of the Goldbach conjecture. See [Wikipedia: Noncototient].

```lean
theorem erdos_418.variants.odd_noncototient :
    { (n - n.totient : ℕ) | n }ᶜ ⊆ { k | Even k }
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/418.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/418.lean#L99).

## `Erdos418.erdos_418.variants.sigma`

Solved: stated here without proof.

> Erdős [Er73b] has shown that a positive density set of natural numbers cannot be written as
> $\sigma(n)-n$ (numbers not of this form are called nonaliquot, or sometimes untouchable).
>
> Here "positive density" means positive lower density: Banks and Luca [BaLu05] proved that the
> set of nonaliquots has lower density at least $1/48$, Chen and Zhao [ChZh11] improved this to
> $0.06$, and it is not known whether the natural density of the nonaliquots exists (Pollack and
> Pomerance [PoPo16] give a heuristic predicting its value).

```lean
theorem erdos_418.variants.sigma :
    0 < { (σ 1 n - n : ℕ) | n }ᶜ.lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/418.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/418.lean#L122).

## `Erdos418.erdos_418.variants.soln`

Solved: stated here without proof.

> A solution to erdos_418 was shown by Browkin and Schinzel [BrSc95] by showing that any integer of
> the form $2^(k + 1)\cdot 509203$ is not of the form $n - \phi(n)$.

```lean
theorem erdos_418.variants.soln :
    { 2 ^ (k + 1) * 509203 | k } ⊆ { (n - n.totient : ℕ) | n }ᶜ
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/418.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/418.lean#L131).

## `Erdos418.erdos_418.variants.density`

Open: stated without proof.

> It is open whether the set of non-cototients has positive (lower) density.

```lean
theorem erdos_418.variants.density :
    0 < { (n - n.totient : ℕ) | n }ᶜ.lowerDensity
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/418.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/418.lean#L139).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/418.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/418.lean)
- [erdosproblems.com/418](https://www.erdosproblems.com/418)
