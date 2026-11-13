---
declaration: theorem
origin: cited
lean: Green45.green_45
statement: formalized
---

# Ben Green's Open Problem 45

> Can we pick residue classes $a_p \pmod{p}$, one for each prime $p \leq N$,
> such that every integer $\leq N$ lies in at least 10 of them?
>
> *References:*
> - [Ben Green's Open Problem 45](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.45)
> - [erdosproblems.com/689](https://www.erdosproblems.com/689)
>
> The version of this problem with $10$ replaced by $2$ is `Erdos689.erdos_689` in
> `FormalConjectures.ErdosProblems.«689»`.

*Quoted from [FormalConjectures/GreensOpenProblems/45.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/45.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green45.green_45`

Open: stated without proof.

> Can we pick residue classes $a_p \pmod{p}$, one for each prime $p \leq N$, such that every
> integer $\leq N$ lies in at least $10$ of them?
>
> Erdős remarks that he does not know how to answer it with $10$ replaced by $2$;
> this is `Erdos689.erdos_689`.

```lean
theorem green_45 :
    ∀ᶠ N in .atTop, ∃ a : ℕ → ℕ, ∀ m ∈ Finset.Icc 1 N,
      10 ≤ (Finset.Icc 1 N |>.filter fun p => p.Prime ∧ a p ≡ m [MOD p]).card
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/45.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/45.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/45.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/45.lean)
- [Ben Green's Open Problem 45](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.45)
