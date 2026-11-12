---
declaration: section
origin: cited
lean: OAI.SquareDifference.power_saving
statement: formalized
proof: formalized
---

# 182. Power savings for intersective polynomial differences and prime arguments

3 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For every fixed intersective integer polynomial *h* of degree *k* ≥ 2 with positive leading coefficient, proves that a subset of $\{1,\ldots,N\}$ avoiding nonzero values $h(1),h(2),\ldots$ as differences has size $O_h(N^{1-c_k})$, with $c_k\gt 0$ depending only on degree. Here intersective means having a root modulo every modulus. For prime arguments, a power saving also holds when *h* has a unit root modulo every modulus, with exponent allowed to depend on *h*.

## A power saving for intersective polynomial differences with an exponent depending only on the degree

An integer polynomial is intersective if it has a root modulo every positive integer. For each degree *k* ≥ 2, we prove that there is an exponent $c_k\gt 0$ such that every set $A\subseteq\{1,\ldots,N\}$ whose differences avoid all nonzero values $h(1),h(2),\ldots$, where *h* is an intersective polynomial of degree *k* with positive leading coefficient, satisfies $|A|=O_h(N^{1-c_k})$. The implied constant may depend on *h*, but the power-saving exponent depends only on its degree.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/power-saving-intersective-polynomial-differences.pdf).

## A Power Saving for Polynomial Differences at Prime Arguments

Let *h* be a fixed integer polynomial of degree at least two with positive leading coefficient, having a unit root modulo every positive integer. We prove that any set $A\subseteq\{1,\ldots,N\}$ whose differences avoid all nonzero values $h(p)$ at primes satisfies $|A|\le C_hN^{1-c_h}$, where $c_h\gt 0$ and $C_h\ge1$ depend only on *h*. Thus the local unit-root condition gives a fixed power saving even when polynomial arguments are restricted to primes. The proof uses the companion zero-free half-plane theorem for Dirichlet *L*-functions to obtain the required prime-distribution estimates.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/prime-argument-polynomial-differences.pdf).

## A power saving for square-difference-free sets

We prove that there are absolute constants *c* > 0 and *C* < ∞ such that every set $A\subseteq\{1,\ldots,N\}$ with no nonzero square difference satisfies $|A|\le C N^{1-c}$. This answers the fixed-power question posed by Green and Sawhney.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves a fixed power saving for sets with no nonzero square difference. There are absolute constants $c>0$ and $C$ such that every $A\subseteq\{1,\ldots,N\}$ satisfying $a-b\ne m^2$ for all $a,b\in A$ and integers $m\ge1$ has $|A|\le C N^{1-c}$. The bound is uniform for every integer $N\ge1$.

## Lean: Power saving for square-difference-free sets

Stated in [SquareDifference.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SquareDifference.lean).

```lean
theorem power_saving :
    ∃ c C : ℝ, 0 < c ∧ ∀ N : ℕ, 1 ≤ N → ∀ A : Finset ℤ,
      A ⊆ Finset.Icc 1 (N : ℤ) → SquareDifference.IsSquareDifferenceFree A →
        (A.card : ℝ) ≤ C * (N : ℝ) ^ (1 - c)
```

Proved in [lean/OAI/Combinatorics/SquareDifference/Main.lean, line 83](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/SquareDifference/Main.lean#L83).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/182.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/182.md)
