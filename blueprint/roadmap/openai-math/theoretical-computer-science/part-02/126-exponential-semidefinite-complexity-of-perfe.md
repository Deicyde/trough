---
declaration: section
origin: cited
lean: OAI.PerfectMatchingPSD.affine_lift_lower_bound, OAI.PerfectMatchingPSD.main
statement: formalized
proof: formalized
---

# 126. Exponential semidefinite complexity of perfect matching

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that every exact semidefinite lift of the perfect matching polytope has exponential size, answering Rothvoss's polynomial-size lift question negatively. The bound holds even for the positive semidefinite rank of its odd-cut slack matrix after any fixed shift $0\lt \rho\lt 1$, allowing arbitrary real positive semidefinite factors.

## Exponential PSD rank of positively shifted matching matrices

For every fixed $0\lt \rho\lt 1$, the matrix indexed by odd vertex sets *U* and perfect matchings *M* of $K_{n}$, with entries $|M\cap\delta(U)|-1+\rho$, has real positive semidefinite rank $2^{\Omega(n)}$ as even *n* tends to infinity. Here $\delta(U)$ is the edge cut of *U*. Consequently, every exact semidefinite lift of the perfect matching polytope has exponential size.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/shifted-matching-psd.pdf); the Lean below formalizes results from it.

## The Lean formalization

The paper proves exponential PSD-rank lower bounds for positively shifted matching matrices. The linked formalization records the related superpolynomial lower bounds: for every fixed $C>0$, the PSD rank of the selected perfect-matching slack matrix exceeds $n^C$ for all sufficiently large even $n$. Every exact affine semidefinite lift of the perfect-matching polytope likewise requires matrix size greater than $n^C$.

These selected statements give superpolynomial growth. They do not state the paper's exponential bound for every fixed positive shift.

## Lean: Superpolynomial lower bound for affine semidefinite lifts

Stated in [MatchingAffineLift.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatchingAffineLift.lean).

```lean
theorem affine_lift_lower_bound :
    ∀ C : ℝ, 0 < C → ∃ n₀ : ℕ, 4 ≤ n₀ ∧
      ∀ n : ℕ, n₀ ≤ n → Even n → ∀ r : ℕ,
        HasAffineLift n r → (n : ℝ) ^ C < (r : ℝ)
```

Proved in [lean/OAI/Combinatorics/MatchingPSD/AffineLift.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/MatchingPSD/AffineLift.lean#L11).

## Lean: Superpolynomial PSD rank for the perfect-matching slack matrix

Stated in [MatchingPSD.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatchingPSD.lean).

```lean
theorem main : MainClaim
```

Proved in [lean/OAI/Combinatorics/MatchingPSD/Main.lean, line 53](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/MatchingPSD/Main.lean#L53).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/126.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/126.md)
