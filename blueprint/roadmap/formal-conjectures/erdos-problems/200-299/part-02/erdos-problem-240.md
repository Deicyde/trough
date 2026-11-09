---
declaration: theorem
origin: cited
lean: Erdos240.erdos_240, Erdos240.erdos_240.variants.tijdeman_epsilon, Erdos240.erdos_240.variants.finite, Erdos240.erdos_240.variants.tijdeman_finite
statement: formalized
---

# Erdős Problem 240

> *References:*
> - [erdosproblems.com/240](https://www.erdosproblems.com/240)
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
>   [PDF](https://www.renyi.hu/~p_erdos/1965-17.pdf)
> - [Po18] Pólya, Georg, *Zur arithmetischen Untersuchung der Polynome*. Math. Z. (1918), 143-148.
> - [Ti73] Tijdeman, R., *On integers with many small prime factors*. Compositio Math. 26 (1973),
>   319-330. [numdam](https://www.numdam.org/item/CM_1973__26_3_319_0/)

*Quoted from [FormalConjectures/ErdosProblems/240.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/240.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/240](https://www.erdosproblems.com/240).

The file states 4 research or textbook statements: 4 solved.

## `Erdos240.erdos_240`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos240.lean#L1817](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos240.lean#L1817).

> Is there an infinite set of primes $P$ such that if $\{a_1\lt a_2\lt \cdots\}$ is the set of integers
> divisible only by primes in $P$ then $\lim a_{i+1}-a_i=\infty$?
>
> The answer is yes, proved by Tijdeman [Ti73, Theorem 7]. The question was asked to Erdős by
> Wintner [Er65b, p. 218]. See also Erdős Problem 368.

```lean
theorem erdos_240 :
    ∃ P : Set ℕ, P.Infinite ∧ P ⊆ {p : ℕ | p.Prime} ∧
      Tendsto (fun i ↦ a P (i + 1) - a P i) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/240.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/240.lean#L60).

## `Erdos240.erdos_240.variants.tijdeman_epsilon`

Solved: stated here without proof.

> Tijdeman [Ti73] resolved this question, proving that, for any $\epsilon>0$, there exists an
> infinite set of primes $P$ such that, with $a_i$ defined as above,
> $$a_{i+1}-a_i \gg a_i^{1-\epsilon}.$$
> ([Ti73, Theorem 7] is stated for $0\lt \epsilon<1$; for $\epsilon\geq 1$ the bound is trivial.)

```lean
theorem erdos_240.variants.tijdeman_epsilon (ε : ℝ) (hε : 0 < ε) :
    ∃ P : Set ℕ, P.Infinite ∧ P ⊆ {p : ℕ | p.Prime} ∧
      (fun i ↦ (a P i : ℝ) ^ (1 - ε)) =O[atTop] (fun i ↦ ((a P (i + 1) - a P i : ℕ) : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/240.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/240.lean#L72).

## `Erdos240.erdos_240.variants.finite`

Solved: stated here without proof.

> The limit is infinite for a finite set of primes, which follows from a theorem of Pólya [Po18],
> that if $f(n)$ is a quadratic integer polynomial without repeated roots then as
> $n\to \infty$ the largest prime factor of $f(n)$ also approaches infinity.
> Erdős [Er65b, p. 218] also credits this to Pólya.
>
> Here $P$ is nonempty: for $P=\emptyset$ the set of integers is $\{1\}$ and there are no gaps.

```lean
theorem erdos_240.variants.finite {P : Set ℕ} (hP : P.Finite) (hne : P.Nonempty)
    (hpr : P ⊆ {p : ℕ | p.Prime}) :
    Tendsto (fun i ↦ a P (i + 1) - a P i) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/240.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/240.lean#L86).

## `Erdos240.erdos_240.variants.tijdeman_finite`

Solved: stated here without proof.

> Tijdeman [Ti73] proved that, if $P$ is a finite set of primes, then
> $$a_{i+1}-a_i \gg \frac{a_i}{(\log a_i)^C}$$
> for some constant $C>0$ depending on $P$.
>
> [Ti73, Theorem 1 and its Corollary] state this for the integers composed of all primes at most
> $p$; it follows for every finite set of primes, since a subset of these integers has larger gaps.

```lean
theorem erdos_240.variants.tijdeman_finite {P : Set ℕ} (hP : P.Finite) (hne : P.Nonempty)
    (hpr : P ⊆ {p : ℕ | p.Prime}) :
    ∃ C : ℝ, 0 < C ∧
      (fun i ↦ (a P i : ℝ) / Real.log (a P i : ℝ) ^ C) =O[atTop]
        (fun i ↦ ((a P (i + 1) - a P i : ℕ) : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/240.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/240.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/240.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/240.lean)
- [erdosproblems.com/240](https://www.erdosproblems.com/240)
