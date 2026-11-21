---
declaration: theorem
origin: cited
lean: Green55.green_55
statement: formalized
---

# Ben Green's Open Problem 55

> *Reference:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.55)
> - [Au14] T. Austin, Partial difference equations over compact Abelian groups, I: modules of solutions,
>   https://arxiv.org/abs/1305.7269.
> - [GrTa10] Green, Benjamin, and Terence Tao. "Linear equations in primes."
>   Annals of mathematics (2010): 1753-1850.
> - [GTZ12] Green, Ben, Terence Tao, and Tamar Ziegler. "An inverse theorem for the Gowers $U^{s+1}[N]$-norm."
>   Annals of Mathematics (2012): 1231-1372.

*Quoted from [FormalConjectures/GreensOpenProblems/55.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/55.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green55.green_55`

Open: stated without proof.

> The diagonal-direction inverse question [Gr24, Problem 55; Au14, §1.3].
>
> Let $p$ be an odd prime and suppose that $f : \mathbb{F}_p^n \times \mathbb{F}_p^n \to \mathbb{C}$
> is a function bounded pointwise by 1. Suppose that
> $\mathbb{E}_h \lVert \Delta_{(h,h)} f \rVert_{\square}^4 \geq \delta$.
>
> Does $f$ correlate with a function of the form
> $a(x)b(y)c(x-y)e_p(B(x,y))$, where $B$ is bilinear and
> $e_p(t) = \exp(2\pi i t/p)$?
>
> NOTE: here "correlate" means that the inner product is at least $C(\delta) > 0$, see [GTZ12, Conjecture 1.2].

```lean
theorem green_55 :
    ∀ (p : ℕ) [Fact p.Prime] (hp : p ≠ 2), ∃ C : ℝ → ℝ, (∀ δ > 0, 0 < C δ) ∧
      ∀ (δ : ℝ) (hδ : 0 < δ) (n : ℕ)

      -- Edge case: avoid the trivial truth  $|f(0,0)| \leq 1$ if n = 0 (single point domain)
      (hn : 1 ≤ n)

      (f : 𝔽ₚⁿ × 𝔽ₚⁿ → ℂ)
      (hf : ∀ x, ‖f x‖ ≤ 1)

      -- Since f is 1-bounded, and since the box norm counts bounded configurations, the expectation
      -- of the box norm will never exceed 1. If $\delta > 1$, `h_bound` is vacuously false,
      -- rendering the entire implication trivially true.
      (hδ_le : δ ≤ 1)

      (h_bound : (1 / (p^n : ℝ)) * ∑ h : 𝔽ₚⁿ, boxNorm4 (multiplicativeDerivative (h, h) f) ≥ δ),
      ∃ (a b c : 𝔽ₚⁿ → ℂ) (B : 𝔽ₚⁿ →ₗ[ZMod p] 𝔽ₚⁿ →ₗ[ZMod p] ZMod p),

        -- Common assumption for inverse Gowers norm theorems, prevents trivial solutions by
        -- arbitrarily scaling one of the functions (and thus the correlation).
        (∀ x, ‖a x‖ ≤ 1) ∧ (∀ x, ‖b x‖ ≤ 1) ∧ (∀ x, ‖c x‖ ≤ 1) ∧

        ‖(1 / (p^(2*n) : ℝ)) * ∑ x : 𝔽ₚⁿ, ∑ y : 𝔽ₚⁿ,
          f (x, y) * star (a x * b y * c (x - y) * ZMod.stdAddChar (B x y))‖ ≥ C δ
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/55.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/55.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/55.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/55.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.55)
