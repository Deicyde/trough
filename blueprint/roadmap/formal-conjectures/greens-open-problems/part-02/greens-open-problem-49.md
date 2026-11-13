---
declaration: theorem
origin: cited
lean: Green49.green_49
statement: formalized
---

# Green's Open Problem 49

> Also known as the *Marton's conjecture* or the *Polynomial Freiman-Ruzsa conjecture (PFR)*.
>
> *References:*
> - [Gr24] [Ben Green's 100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.49)
> - [Aa19] Aaronson, James. "A counterexample to a strong variant of the Polynomial Freiman-Ruzsa conjecture." arXiv preprint arXiv:1902.00353 (2019).
> - [Fa00] I. Farah, Approximate homomorphisms. II. Group homomorphisms, Combinatorica 20 (2000), no. 1, 47–60.
> - [GGM25] W. T. Gowers, B. J. Green, F. Manners and T. C. Tao, On a conjecture of Marton, Ann. of Math. (2) 201 (2025), no. 2, 515–549.
> - [Gr05] B. J. Green, Finite field models in additive combinatorics, Surveys in combinatorics 2005, 1–27, London Math. Soc. Lecture Note Ser., 327, Cambridge Univ. Press, Cambridge, 2005.
> - [GrTa10] B. J. Green and T. C. Tao An equivalence between inverse sumset theorems and inverse conjectures for the U3 norm, Math. Proc. Cambridge Philos. Soc. 149 (2010), no. 1, 1–19.
> - [Lo12] S. Lovett, Equivalence of polynomial conjectures in additive combinatorics, Combinatorica 32 (2012), no. 5, 607–618.
> - [LoRe17] S. Lovett and O. Regev, A counterexample to a strong variant of the Polynomial Freiman Ruzsa conjecture in Euclidean space, Discrete Anal.(2017), Paper No. 8, 6 pp.
> - [Ma19] F. R. W. M. Manners, Formulations of the PFR conjecture over Z, Math. Proc. Cambridge Philos. Soc. 166 (2019), no. 2, 243–245.
> - [Sa12] T. Sanders, On the Bogolyubov-Ruzsa lemma, Anal. PDE 5 (2012), no. 3, 627–655.
> - [Ta08] T. C. Tao, A counterexample to a strong polynomial Freiman-Ruzsa conjecture, blog post November 2008, available at http://tinyurl.com/36j6hyxv.

*Quoted from [FormalConjectures/GreensOpenProblems/49.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/49.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Green49.green_49`

Solved: stated here without proof.

> Suppose that $A \subset \mathbb{F}_2^n$ is a set with $|A + A| \leq K|A|$. Is it true that $A$
> is covered by $K^{O(1)}$ translates of a subspace of size $\leq |A|$?
>
> Solved by [GGM25], with at most $2K^{12}$ translates. The factor $2$ cannot be omitted: for
> $A = \mathbb{F}_2^n \setminus \{0\}$ one has $K = 2^n / (2^n - 1)$, so $K^C \to 1$ as
> $n \to \infty$, while every subspace of size at most $|A|$ is proper and two translates are needed.

```lean
theorem green_49 :
    ∃ C > 0,
      ∀ n (A : Finset (𝔽₂ n)), A.Nonempty →
      ∀ K ≥ (1 : ℝ), (#(A + A) : ℝ) ≤ K * #A →
        ∃ (W : Submodule (ZMod 2) (𝔽₂ n)) (T : Finset (𝔽₂ n)),
          Nat.card W ≤ #A ∧
          (#T : ℝ) ≤ 2 * K ^ C ∧
          (A : Set (𝔽₂ n)) ⊆ T + W
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/49.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/49.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/49.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/49.lean)
- [Ben Green's 100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.49)
