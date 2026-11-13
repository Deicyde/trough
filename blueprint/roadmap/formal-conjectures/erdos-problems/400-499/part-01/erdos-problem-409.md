---
declaration: theorem
origin: cited
lean: Erdos409.erdos_409.parts.i, Erdos409.erdos_409.parts.i.isTheta, Erdos409.erdos_409.parts.i.isBigO, Erdos409.erdos_409.parts.i.isLittleO, Erdos409.erdos_409.parts.ii, Erdos409.erdos_409.parts.iii, Erdos409.erdos_409.variants.sigma, Erdos409.erdos_409.variants.sigma_termination, Erdos409.erdos_409.variants.sigma_isTheta, Erdos409.erdos_409.variants.sigma_isBigO, Erdos409.erdos_409.variants.sigma_isLittleO, Erdos409.erdos_409.variants.sigma_prime_termination
statement: formalized
---

# Erdős Problem 409

> *Reference:* [erdosproblems.com/409](https://www.erdosproblems.com/409)

*Quoted from [FormalConjectures/ErdosProblems/409.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/409](https://www.erdosproblems.com/409).

The file states 12 research or textbook statements: 12 open. It also has 1 test statement, counted here but not shown.

## `Erdos409.erdos_409.parts.i`

Open: stated without proof.

> How many iterations of $n\mapsto\phi(n) + 1$ are needed before a prime is reached?

```lean
theorem erdos_409.parts.i (n : ℕ) (hn : 0 < n) :
    IsLeast { i | (φ · + 1)^[i] n |>.Prime } erdos_409.parts.i.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L42).

## `Erdos409.erdos_409.parts.i.isTheta`

Open: stated without proof.

> Let $c(n)$ be the minimum number of iterations of $n\mapsto\phi(n) + 1$ before a prime
> is reached. What is $\Theta(c(n))$?

```lean
theorem erdos_409.parts.i.isTheta (c : ℕ → ℕ)
    (h : ∀ n > 0, IsLeast { i | (φ · + 1)^[i] n |>.Prime } (c n)) :
    (fun n => (c n : ℝ)) =Θ[atTop] erdos_409.parts.i.isTheta.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L84).

## `Erdos409.erdos_409.parts.i.isBigO`

Open: stated without proof.

> Let $c(n)$ be the minimum number of iterations of $n\mapsto\phi(n) + 1$ before a prime
> is reached. Find the simplest function $g(n)$ such that $c(n) = O(g(n))$?

```lean
theorem erdos_409.parts.i.isBigO (c : ℕ → ℕ)
    (h : ∀ n > 0, IsLeast { i | (φ · + 1)^[i] n |>.Prime } (c n)) :
    (fun n => (c n : ℝ)) =O[atTop] erdos_409.parts.i.isBigO.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L96).

## `Erdos409.erdos_409.parts.i.isLittleO`

Open: stated without proof.

> Let $c(n)$ be the minimum number of iterations of $n\mapsto\phi(n) + 1$ before a prime
> is reached. Find the simplest function $g(n)$ such that $c(n) = o(g(n))$?

```lean
theorem erdos_409.parts.i.isLittleO (c : ℕ → ℕ)
    (h : ∀ n > 0, IsLeast { i | (φ · + 1)^[i] n |>.Prime } (c n)) :
    (fun n => (c n : ℝ)) =o[atTop] erdos_409.parts.i.isLittleO.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L108).

## `Erdos409.erdos_409.parts.ii`

Open: stated without proof.

> Can infinitely many $n$ reach the same prime under the iteration $n\mapsto\phi(n) + 1$?

```lean
theorem erdos_409.parts.ii :
    ∃ (p : ℕ) (hp : p.Prime), { n | ∃ i, (φ · + 1)^[i] n = p }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L117).

## `Erdos409.erdos_409.parts.iii`

Open: stated without proof.

> What is the density of $n$ which reach any fixed prime under the iteration $n\mapsto\phi(n) + 1$?

```lean
theorem erdos_409.parts.iii (p : ℕ) (h : p.Prime) :
    { n | ∃ i, (φ · + 1)^[i] n = p }.HasDensity erdos_409.parts.iii.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L127).

## `Erdos409.erdos_409.variants.sigma`

Open: stated without proof.

> If the iteration $n\mapsto\sigma(n) - 1$ starting at $n > 1$ reaches a prime, how many
> iterations are needed before a prime is reached?

```lean
theorem erdos_409.variants.sigma (n : ℕ) (hn : n > 1)
    (hterm : ∃ i, (σ 1 · - 1)^[i] n |>.Prime) :
    IsLeast { i | (σ 1 · - 1)^[i] n |>.Prime } erdos_409.variants.sigma.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L140).

## `Erdos409.erdos_409.variants.sigma_termination`

Open: stated without proof.

> If $n > 1$ then the iteration $n\mapsto\sigma(n) - 1$ necessarily reaches a prime.
> Note: this is open — it is not clear that the σ iteration always terminates,
> since it is non-decreasing (unlike the φ iteration which is strictly decreasing).

```lean
theorem erdos_409.variants.sigma_termination (n : ℕ) (hn : n > 1) :
    ∃ i, (σ 1 · - 1)^[i] n |>.Prime
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L149).

## `Erdos409.erdos_409.variants.sigma_isTheta`

Open: stated without proof.

> Let $c(n)$ be the minimum number of iterations of $n\mapsto\sigma(n) - 1$ before a prime
> is reached. What is $\Theta(c(n))$?

```lean
theorem erdos_409.variants.sigma_isTheta (c : ℕ → ℕ)
    (h : ∀ n > 1, IsLeast { i | (σ 1 · - 1)^[i] n |>.Prime } (c n)) :
    (fun n => (c n : ℝ)) =Θ[atTop] erdos_409.variants.sigma_isTheta.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L162).

## `Erdos409.erdos_409.variants.sigma_isBigO`

Open: stated without proof.

> Let $c(n)$ be the minimum number of iterations of $n\mapsto\sigma(n) - 1$ before a prime
> is reached. Find the simplest function $g(n)$ such that $c(n) = O(g(n))$?

```lean
theorem erdos_409.variants.sigma_isBigO (c : ℕ → ℕ)
    (h : ∀ n > 1, IsLeast { i | (σ 1 · - 1)^[i] n |>.Prime } (c n)) :
    (fun n => (c n : ℝ)) =O[atTop] erdos_409.variants.sigma_isBigO.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 174](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L174).

## `Erdos409.erdos_409.variants.sigma_isLittleO`

Open: stated without proof.

> Let $c(n)$ be the minimum number of iterations of $n\mapsto\sigma(n) - 1$ before a prime
> is reached. Find the simplest function $g(n)$ such that $c(n) = o(g(n))$?

```lean
theorem erdos_409.variants.sigma_isLittleO (c : ℕ → ℕ)
    (h : ∀ n > 1, IsLeast { i | (σ 1 · - 1)^[i] n |>.Prime } (c n)) :
    (fun n => (c n : ℝ)) =o[atTop] erdos_409.variants.sigma_isLittleO.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 186](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L186).

## `Erdos409.erdos_409.variants.sigma_prime_termination`

Open: stated without proof.

> Is it true that iterates of $n\mapsto\sigma(n) - 1$ always reach a prime?

```lean
theorem erdos_409.variants.sigma_prime_termination :
    ∀ n > 1, ∃ i, (σ 1 · - 1)^[i] n |>.Prime
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/409.lean, line 195](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean#L195).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/409.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/409.lean)
- [erdosproblems.com/409](https://www.erdosproblems.com/409)
