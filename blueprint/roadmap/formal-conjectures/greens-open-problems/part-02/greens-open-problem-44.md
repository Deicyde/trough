---
declaration: theorem
origin: cited
lean: Green44.green_44, Green44.green_44.variants.less_than_sqrt
statement: formalized
---

# Green's Open Problem 44

> *References:*
> - [Gr24] [Ben Green's 100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.44)
> - [Er80] Erdős, Paul. "A survey of problems in combinatorial number theory."
>   Annals of Discrete Mathematics 6 (1980): 89-115.

*Quoted from [FormalConjectures/GreensOpenProblems/44.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/44.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Green44.green_44`

Open: stated without proof.

> Sieve $[N]$ by removing half the residue classes mod $p_i$, for primes
> $2 \leqslant p_1 < p_2 < \dots < p_{1000} < N^{9/10}$. Does the remaining set have size at most
> $\frac{1}{10} N$?
>
> We interpret "half the residue classes" as $\lfloor p_i / 2 \rfloor$.

```lean
theorem green_44 :
    ∀ (N : ℕ) (p : Fin 1000 → ℕ) (A : (i : Fin 1000) → Finset (ZMod (p i))),
      let remaining := (Finset.Icc 1 N).filter (fun x => ∀ i, (x : ZMod (p i)) ∉ A i)
      (∀ i, (p i).Prime) →
      StrictMono p →
      (p 999) ^ 10 < N ^ 9 →
      (∀ i, (A i).card = (p i) / 2) →
      10 * remaining.card ≤ N
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/44.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/44.lean#L43).

## `Green44.green_44.variants.less_than_sqrt`

Solved: stated here without proof.

> The answer is affirmative if the primes are all less than $N^{1/2}$, by the large sieve. [Gr24]

```lean
theorem green_44.variants.less_than_sqrt :
    ∀ (N : ℕ) (p : Fin 1000 → ℕ) (A : (i : Fin 1000) → Finset (ZMod (p i))),
      let remaining := (Finset.Icc 1 N).filter (fun x => ∀ i, (x : ZMod (p i)) ∉ A i)
      (∀ i, (p i).Prime) →
      StrictMono p →
      (p 999) ^ 2 < N →
      (∀ i, (A i).card = (p i) / 2) →
      10 * remaining.card ≤ N
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/44.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/44.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/44.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/44.lean)
- [Ben Green's 100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.44)
