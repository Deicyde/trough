---
declaration: theorem
origin: cited
lean: Green32.green_32, Green32.green_32.variants.sh20_general, Green32.green_32.variants.sh20_sqrt, Green32.green_32.variants.szemeredi_regime, Green32.green_32.variants.dirichlet_regime, Green32.green_32.variants.log_regime, Green32.green_32.variants.finite_field
statement: formalized
---

# Green's Open Problem 32

> *Reference:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.32)
> - [Sh20] Shakan, George. "A Large Gap in a Dilate of a Set." SIAM Journal on Discrete Mathematics
>   34.4 (2020): 2553-2555.

*Quoted from [FormalConjectures/GreensOpenProblems/32.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/32.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 2 open and 5 solved. It also has 5 test statements, counted here but not shown.

## `Green32.green_32`

Open: stated without proof.

> Let $p$ be a prime and let $A \subset \mathbb{Z}/p\mathbb{Z}$ be a set of size $\lfloor \sqrt{p} \rfloor$.
> Is there a dilate of $A$ containing a gap of length $100\sqrt{p}$?

```lean
theorem green_32 :
    HasLargeGapDilate (fun p ↦ Real.sqrt p)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/32.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/32.lean#L86).

## `Green32.green_32.variants.sh20_general`

Solved: stated here without proof.

> [Sh20, Theorem 1] implies a gap of at least $\lfloor 2p/|A| - 2 \rfloor$.

```lean
theorem green_32.variants.sh20_general :
    ∀ (p : ℕ), p.Prime → -- Theorem 1 is for any prime p, not just asymptotically
      ∀ A : Finset (ZMod p), 1 < A.card →
      ∃ c : (ZMod p)ˣ, HasGap (c • A) ⌊2 * (p : ℝ) / A.card - 2⌋₊
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/32.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/32.lean#L92).

## `Green32.green_32.variants.sh20_sqrt`

Solved: stated here without proof.

> [Sh20] has used the polynomial method to show that this is true with 100 replaced by 2 [Gr24].
>
> Note: More precisely [Sh20, Theorem 1] implies a gap of at least $\lfloor 2p/|A| - 2 \rfloor$.
> For a set $A$ of size $\lfloor \sqrt{p} \rfloor$, this guarantees a gap of at least
> $\lfloor 2\sqrt{p} \rfloor - 2$.

```lean
theorem green_32.variants.sh20_sqrt :
    ∀ᶠ p in atTop, p.Prime →
      ∀ A : Finset (ZMod p), A.card = ⌊Real.sqrt p⌋₊ →
      ∃ c : (ZMod p)ˣ, HasGap (c • A) (⌊2 * Real.sqrt p⌋₊ - 2)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/32.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/32.lean#L106).

## `Green32.green_32.variants.szemeredi_regime`

Solved: stated here without proof.

> In the regime $\omega(p) \sim c p$, this is Szemerédi's theorem [Gr24].

```lean
theorem green_32.variants.szemeredi_regime :
    ∀ c, 0 < c ∧ c < 1 → ∀ ω : ℕ → ℝ, ω ~[atTop] (fun p ↦ c * p) →
      HasLargeGapDilate ω
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/32.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/32.lean#L114).

## `Green32.green_32.variants.dirichlet_regime`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Green32_green_32_variants_dirichlet_regime.lean#L260](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Green32_green_32_variants_dirichlet_regime.lean#L260).

> In the regime $\omega(p) \le c \log p$, this is basically Dirichlet's lower bound for the size of
> Bohr sets [Gr24].
>
> The lower bound $101 \le \omega(p)$ makes the set size $\lfloor \omega(p) \rfloor$ exceed $100$.
> With only $100 < \omega(p)$, a function with $100 < \omega(p) < 101$ asks for sets of size $100$
> with a gap of length $p - 1$ in some dilate, which is impossible.

```lean
theorem green_32.variants.dirichlet_regime :
    ∃ c > 0, ∀ ω : ℕ → ℝ, (∀ᶠ p in atTop, 101 ≤ ω p ∧ ω p ≤ c * Real.log p) →
      HasLargeGapDilate ω
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/32.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/32.lean#L129).

## `Green32.green_32.variants.log_regime`

Open: stated without proof.

> Even what happens in the regime $\omega(p) \sim 10 \log p$ is unclear [Gr24].

```lean
theorem green_32.variants.log_regime :
    (∀ ω : ℕ → ℝ, ω ~[atTop] (fun p ↦ 10 * Real.log p) →
      HasLargeGapDilate ω)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/32.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/32.lean#L136).

## `Green32.green_32.variants.finite_field`

Solved: stated here without proof.

> Tom Sanders' finite field variant [Gr24].
> If $N = 2^n$ and $A$ is a subset of size $\lfloor \sqrt{N} \rfloor$, then $A^c$ contains a coset of
> size at least $100\sqrt{N}$ for sufficiently large $n$.

```lean
theorem green_32.variants.finite_field :
    ∀ᶠ n in atTop,
      ∀ A : Finset (𝔽₂ n), A.card = ⌊Real.sqrt (2^n : ℝ)⌋₊ →
      HasCosetHole A ⌊100 * Real.sqrt (2^n : ℝ)⌋₊
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/32.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/32.lean#L161).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/32.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/32.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.32)
