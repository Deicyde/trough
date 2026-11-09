---
declaration: theorem
origin: cited
lean: Erdos978.erdos_978.variants.sub_one, Erdos978.erdos_978.parts.i, Erdos978.erdos_978.variants.sub_two, Erdos978.erdos_978.variants.allow_fixed_divisors, Erdos978.erdos_978.parts.ii, Erdos978.erdos_978.parts.iii
statement: formalized
---

# Erdős Problem 978

> *Reference:*
>  - [erdosproblems.com/978](https://www.erdosproblems.com/978)
>  - [Ho67] Hooley, C., On the power free values of polynomials. Mathematika (1967), 21--26.
>  - [Br11] Browning, T. D., Power-free values of polynomials. Arch. Math. (Basel) (2011), 139--150.
>  - [Er53] Erdős, P., Arithmetical properties of polynomials. J. London Math. Soc. (1953), 416--425.
>  - [OAI26a] OpenAI, *Squarefree values of quartics and power-free values of polynomials*. OpenAI
>    Math Release preprint (2026).
>    https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf

*Quoted from [FormalConjectures/ErdosProblems/978.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/978.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/978](https://www.erdosproblems.com/978).

The file states 6 research or textbook statements: 6 solved.

## `Erdos978.erdos_978.variants.sub_one`

Solved: stated here without proof.

> Let `f ∈ ℤ[X]` be an irreducible polynomial with positive leading coefficient. Suppose that the
> degree `k` of `f` is larger than `2` and is not equal to a power of `2`. Then the set of `n` such
> that `f n` is `(k - 1)`-th power free is infinite, and this is proved in [Er53].

```lean
theorem erdos_978.variants.sub_one {f : ℤ[X]} (hi : Irreducible f) (hd : 2 < f.natDegree)
    (hp : ∀ (x : ℕ), f.natDegree ≠ 2 ^ x) (hlc : 0 < f.leadingCoeff) :
    {n : ℕ | Powerfree (f.natDegree - 1) (f.eval (n : ℤ))}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/978.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/978.lean#L43).

## `Erdos978.erdos_978.parts.i`

Solved: stated here without proof.

> Let `f ∈ ℤ[X]` be an irreducible polynomial with positive leading coefficient. Suppose that the
> degree `k` of `f` is larger than `2`, is not equal to a power of `2`, and `f n` has no fixed
> `(k - 1)`-th power divisors other than `1`. Then the set of `n` such that `f n` is `(k - 1)`-th
> power free has positive density, and this is proved in [Ho67].

```lean
theorem erdos_978.parts.i {f : ℤ[X]} (hi : Irreducible f) (hd : 2 < f.natDegree)
    (hp2 : ∀ (x : ℕ), f.natDegree ≠ 2 ^ x) (hlc : 0 < f.leadingCoeff)
    (hp : ∀ (p : ℕ), p.Prime → ∃ n : ℕ, ¬ (p : ℤ) ^ (f.natDegree - 1) ∣ f.eval (n : ℤ)) :
    HasPosDensity {n : ℕ | Powerfree (f.natDegree - 1) (f.eval (n : ℤ))}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/978.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/978.lean#L53).

## `Erdos978.erdos_978.variants.sub_two`

Solved: stated here without proof.

> If the degree `k` of `f` is larger than or equal to `9`, and `f n` has no fixed `(k - 2)`-th
> power divisors other than `1`, then the set of `n` such that `f n` is `(k - 2)`-th power free has
> infinitely many elements. This result is proved in [Br11].

```lean
theorem erdos_978.variants.sub_two {f : ℤ[X]} (hi : Irreducible f) (hd : 9 ≤ f.natDegree)
    (hp : ∀ (p : ℕ), p.Prime → ∃ n : ℕ, ¬ (p : ℤ) ^ (f.natDegree - 2) ∣ f.eval (n : ℤ)) :
    {n : ℕ | Powerfree (f.natDegree - 2) (f.eval (n : ℤ))}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/978.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/978.lean#L63).

## `Erdos978.erdos_978.variants.allow_fixed_divisors`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/3b5d6ac2555cd63b83d418c29ff040876be9dee0/FormalConjectures/ErdosProblems/978.lean#L64](https://github.com/mo271/formal-conjectures/blob/3b5d6ac2555cd63b83d418c29ff040876be9dee0/FormalConjectures/ErdosProblems/978.lean#L64).

> If $k > 3$ (and $k \neq 2^l$), then are there infinitely many $n$ for which $f(n)$ is
> $(k-2)$-power-free?
>
> This was disproved by the DeepMind prover agent.

```lean
theorem erdos_978.variants.allow_fixed_divisors :
    ¬ ∀ {f : ℤ[X]}, Irreducible f → f.natDegree > 3 →
    (¬ ∃ l : ℕ, f.natDegree = 2 ^ l) → 0 < f.leadingCoeff →
    (¬ ∃ p : ℕ, p.Prime ∧ ∀ n : ℕ, (p : ℤ) ^ (f.natDegree - 1) ∣ f.eval (n : ℤ)) →
    {n : ℕ | Powerfree (f.natDegree - 2) (f.eval (n : ℤ))}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/978.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/978.lean#L77).

## `Erdos978.erdos_978.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/PowerFree/Main.lean#L144](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/PowerFree/Main.lean#L144).

> If $k>3$ (and $k \neq 2^l$), and for all primes $p$ there exists $n$ such that $p^{k-2}\nmid f(n)$,
> then are there infinitely many $n$ for which $f(n)$ is $(k-2)$-power-free?
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean proof,
> which gives positive density and does not need $k \neq 2^l$ or a positive leading coefficient.

```lean
theorem erdos_978.parts.ii :
    ∀ {f : ℤ[X]}, Irreducible f → f.natDegree > 3 →
    (¬ ∃ l : ℕ, f.natDegree = 2 ^ l) → 0 < f.leadingCoeff →
    (∀ (p : ℕ), p.Prime → ∃ n : ℕ, ¬ (p : ℤ) ^ (f.natDegree - 2) ∣ f.eval (n : ℤ)) →
    {n : ℕ | Powerfree (f.natDegree - 2) (f.eval (n : ℤ))}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/978.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/978.lean#L94).

## `Erdos978.erdos_978.parts.iii`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/PowerFree/Main.lean#L144](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/PowerFree/Main.lean#L144).

> Does `n ^ 4 + 2` represent infinitely many squarefree numbers?
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean proof,
> which gives positive density for every irreducible quartic with no fixed square divisor.

```lean
theorem erdos_978.parts.iii : {n : ℕ | Squarefree (n ^ 4 + 2)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/978.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/978.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/978.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/978.lean)
- [erdosproblems.com/978](https://www.erdosproblems.com/978)
