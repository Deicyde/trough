---
declaration: theorem
origin: cited
lean: Green47.green_47, Green47.green_47.variants.finite_exceptions
statement: formalized
---

# Green's Open Problem 47

> *References:*
> - [Gr24] [Ben Green's 100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.47)
> - [GH14] Green, Ben, and Adam J. Harper. "Inverse questions for the large sieve."
>   Geometric and Functional Analysis 24.4 (2014): 1167-1203.
> - [HV09] Helfgott, Harald Andrés, and Akshay Venkatesh. "How small must ill-distributed sets be."
>   Analytic number theory 2 (2009): 224-234.
> - [Wa12] Walsh, Miguel N. "The inverse sieve problem in high dimensions." (2012): 2001-2022.
> - [Wa14] Walsh, Miguel N. "The algebraicity of ill-distributed sets."
>   Geometric and Functional Analysis 24.3 (2014): 959-967.

*Quoted from [FormalConjectures/GreensOpenProblems/47.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/47.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Green47.green_47`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/green-47-exact-containment-counterexample/blob/d6912b65cd04463ca81d2e7dfb52367718a3e3b2/lean/Green47ExactContainmentFC.lean#L19-L25](https://github.com/KitaKen1/green-47-exact-containment-counterexample/blob/d6912b65cd04463ca81d2e7dfb52367718a3e3b2/lean/Green47ExactContainmentFC.lean#L19-L25).

> Suppose that a large sieve process leaves a set of quadratic size. Is that set quadratic?
>
> The following very particular instance is probably the simplest [Gr24]:
> Suppose that $A \subset \mathbb{N}$ is a set with the property that
> $|A \pmod p| \leqslant \frac{1}{2}(p + 1)$ for all sufficiently large $p$.
> Is it true that either $|A \cap [X]| \ll X^{1/2} / \log^{100} X$, or $A$ is contained in the
> image of $\mathbb{Z}$ under a quadratic map $\phi : \mathbb{Q} \to \mathbb{Q}$?

```lean
theorem green_47 :
    ¬ ∀ A : Set ℕ,
      (∀ᶠ p in atTop, Nat.Prime p → Set.ncard (Set.image (fun a : ℕ => (a : ZMod p)) A) ≤ (p + 1) / 2) →
      ((fun X : ℕ => ((A ∩ Set.Iic X).ncard : ℝ)) ≪ (fun X : ℕ => Real.sqrt (X : ℝ) / (Real.log (X : ℝ)) ^ 100))
      ∨ (∃ P : Polynomial ℚ, P.degree = 2 ∧ ∀ a ∈ A, ∃ z : ℤ, (a : ℚ) = P.eval (z : ℚ))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/47.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/47.lean#L53).

## `Green47.green_47.variants.finite_exceptions`

Open: stated without proof.

> In Green and Harper's formulation [GH14, Conjecture 1.7], the quadratic containment
> is allowed to fail on a finite subset of $A$.

```lean
theorem green_47.variants.finite_exceptions :
    ∀ A : Set ℕ,
      (∀ᶠ p in atTop, Nat.Prime p → Set.ncard (Set.image (fun a : ℕ => (a : ZMod p)) A) ≤ (p + 1) / 2) →
      ((fun X : ℕ => ((A ∩ Set.Iic X).ncard : ℝ)) ≪ (fun X : ℕ => Real.sqrt (X : ℝ) / (Real.log (X : ℝ)) ^ 100))
      ∨ (∃ P : Polynomial ℚ, P.degree = 2 ∧ {a ∈ A | ¬∃ z : ℤ, (a : ℚ) = P.eval (z : ℚ)}.Finite)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/47.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/47.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/47.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/47.lean)
- [Ben Green's 100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.47)
