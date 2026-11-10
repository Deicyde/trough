---
declaration: theorem
origin: cited
lean: Green9.green_9_i, Green9.green_9_ii, Green9.green_9_iii
statement: formalized
---

# Green's Open Problem 9

> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.9)
> - [BlSi20] Bloom, Thomas F., and Olof Sisask. "Breaking the logarithmic barrier in Roth's theorem on
>   arithmetic progressions." arXiv preprint arXiv:2007.03528 (2020).

*Quoted from [FormalConjectures/GreensOpenProblems/9.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/9.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Green9.green_9_i`

Solved: stated here without proof.

> Problem 9 (i): is $r_3(N) \ll N(\log N)^{-10}$?
>
> Solved in [BlSi20].

```lean
theorem green_9_i :
    (fun (N : ℕ) ↦ (r 3 N : ℝ)) ≪ fun (N : ℕ) ↦ (N : ℝ) * (Real.log N) ^ (-10 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/GreensOpenProblems/9.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/9.lean#L47).

## `Green9.green_9_ii`

Open: stated without proof.

> Problem 9 (ii): is $r_5(N) \ll N(\log N)^{-c}$?

```lean
theorem green_9_ii :
    ∃ c > (0 : ℝ), (fun (N : ℕ) ↦ (r 5 N : ℝ))
      ≪ fun (N : ℕ) ↦ (N : ℝ) * (Real.log N) ^ (-c)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/GreensOpenProblems/9.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/9.lean#L55).

## `Green9.green_9_iii`

Open: stated without proof.

> Problem 9 (iii): is $r_4(\mathbf{F}_5^n) \ll N^{1-c}$, where $N=5^n$?

```lean
theorem green_9_iii :
    ∃ c > (0 : ℝ), (fun (n : ℕ) ↦ ((Finset.univ : Finset (𝔽₅ n)).maxAPFreeCard 4 : ℝ))
      ≪ fun (n : ℕ) ↦ ((5 : ℝ) ^ n) ^ (1 - c)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/GreensOpenProblems/9.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/9.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/9.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/9.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.9)
