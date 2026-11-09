---
declaration: theorem
origin: cited
lean: Green33.green_33
statement: formalized
---

# Ben Green's Open Problem 33

> *References:*
> - [Gr24] [Ben Green's Open Problem 33](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.33)
> - [CaHa20] Caprace, Pierre-Emmanuel, and Pierre de la Harpe. "Groups with irreducibly unfaithful
>   subsets for unitary representations." Confluentes Mathematici 12.1 (2020): 31-68.
> - [CrLe07] Croot, Ernie, and Vsevolod F. Lev. "Open problems in additive combinatorics."
>   Additive combinatorics 43.207-233 (2007): 1.

*Quoted from [FormalConjectures/GreensOpenProblems/33.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/33.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `Green33.green_33`

Open: stated without proof.

> Are there infinitely many $q$ for which there is a set $A \subset \mathbb{Z}/q\mathbb{Z}$,
> $|A| = (\sqrt{2} + o(1))q^{1/2}$, with $A + A = \mathbb{Z}/q\mathbb{Z}$? [Gr24]

```lean
theorem green_33 :
    ∀ ε : ℝ, 0 < ε →
      ∃ᶠ q : ℕ+ in atTop,
        ∃ A : Finset (ZMod q),
          A + A = Finset.univ ∧
          |((A.card : ℝ) / Real.sqrt q - Real.sqrt 2)| < ε
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/33.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/33.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/33.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/33.lean)
- [Ben Green's Open Problem 33](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.33)
