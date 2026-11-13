---
declaration: theorem
origin: cited
lean: Green62.green_62
statement: formalized
---

# Ben Green's Open Problem 62

> Let $p$ be a large prime, and let $A$ be the set of all primes less than $p$.
> Is every $x \in \{1, \ldots, p-1\}$ congruent to some product $a_1 a_2$ where $a_1, a_2 \in A$?
>
> This is a problem of Erdős, Odlyzko, and Sárközy [105] from 1987.
>
> *Reference:* [Ben Green's Open Problem 62](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.62)

*Quoted from [FormalConjectures/GreensOpenProblems/62.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/62.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green62.green_62`

Open: stated without proof.

> Let $p$ be a large prime, and let $A$ be the set of all primes less than $p$.
> Is every $x \in \{1, \ldots, p-1\}$ congruent to some product $a_1 a_2$ where $a_1, a_2 \in A$?

```lean
theorem green_62 :
    ∀ᶠ p in atTop, p.Prime →
      let A := (Finset.range p).filter Nat.Prime
      ∀ x : ℕ, 1 ≤ x ∧ x < p →
        ∃ a₁ ∈ A, ∃ a₂ ∈ A, (x : ZMod p) = (a₁ * a₂ : ZMod p)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/62.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/62.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/62.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/62.lean)
- [Ben Green's Open Problem 62](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.62)
