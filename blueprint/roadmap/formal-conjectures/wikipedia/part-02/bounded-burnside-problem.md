---
declaration: theorem
origin: cited
lean: BoundedBurnsideProblem.bounded_burnside_problem
statement: formalized
---

# Bounded Burnside problem

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Burnside_problem#Bounded_Burnside_problem)
> - [NA68] P. S. Novikov, S. I. Adian. "Infinite periodic groups I-III."
>   _Izv. Akad. Nauk SSSR Ser. Mat._ 32 (1968).
> - [Ad79] S. I. Adian. _The Burnside Problem and Identities in Groups._ Springer, 1979.
> - [Iv94] S. V. Ivanov. "The free Burnside groups of sufficiently large exponents."
>   _Internat. J. Algebra Comput._ 4 (1994), 1-308.
> - [Ly96] I. G. Lysënok. "Infinite Burnside groups of even exponent."
>   _Izv. Ross. Akad. Nauk Ser. Mat._ 60 (1996), 3-224.

*Quoted from [FormalConjectures/Wikipedia/BoundedBurnsideProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BoundedBurnsideProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `BoundedBurnsideProblem.bounded_burnside_problem`

Solved: stated here without proof.

> Let $G$ be a finitely generated group, and assume there exists $n$ such that for every $g$ in $G$,
> $g^n = 1$. Must $G$ be finite?
>
> The answer is negative. Novikov and Adian proved that for every odd $n > 4381$ there exist
> infinite, finitely generated groups of exponent $n$ [NA68]; Adian later reduced this to odd
> $n > 665$ [Ad79]. The even case is harder: Ivanov proved $B(m, n)$ infinite for $m > 1$ and
> even $n \ge 2^{48}$ divisible by $2^9$ [Iv94], and Lysënok improved this to $m > 1$ and
> $n \ge 8000$ [Ly96]. Any such group, for example the free Burnside group $B(2, 667)$,
> refutes the statement below.
>
> Note this concerns only the universally quantified question stated here, which a single
> counterexample closes. The classification of which free Burnside groups $B(m, n)$ are finite
> remains open, with $B(2, 5)$ the best known open case.

```lean
theorem bounded_burnside_problem :
    ¬ ∀ (G : Type) [Group G] (fin_gen : Group.FG G)
      (n : ℕ) (hn : n > 0) (bounded : ∀ g : G, g^n = 1), Finite G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/BoundedBurnsideProblem.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BoundedBurnsideProblem.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BoundedBurnsideProblem.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BoundedBurnsideProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Burnside_problem#Bounded_Burnside_problem)
