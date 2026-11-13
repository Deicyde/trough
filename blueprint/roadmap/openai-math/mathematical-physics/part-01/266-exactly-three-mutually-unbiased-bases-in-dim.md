---
declaration: section
origin: cited
lean: OAI.MUB6.fourier_and_family_bound, OAI.HadamardSix.rowRatio_cubeFiber_sum_zero
statement: formalized
proof: formalized
---

# 266. Exactly three mutually unbiased bases in dimension six

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves $N(6)=3$, resolving Zauner's dimension-six mutually unbiased bases conjecture: three such bases exist in ℂ$^{6}$, but four cannot. The exclusion is a complete certified computation under the stated binary64 arithmetic and compiler conditions. An independent companion proves the Matolcsi–Ruzsa–Weiner Fourier-vanishing conjecture for order-six complex Hadamard matrices outside Tao's cubic equivalence class.

## The maximum number of mutually unbiased bases in dimension six

We prove that the maximum number of mutually unbiased orthonormal bases in ℂ$^{6}$ is three, resolving Zauner's dimension-six MUB conjecture. The upper bound is computer-assisted: under the stated binary64 arithmetic and compiler conditions, a complete execution of the documented verification pipeline excludes four arbitrary complex bases.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf); the Lean below formalizes results from it.

## Exact Fourier certificates for complex Hadamard matrices of order six

We prove the Fourier-vanishing conjecture of Matolcsi, Ruzsa, and Weiner: every complex Hadamard matrix of order six outside Tao's cubic equivalence class has a vanishing character sum at every permutation of $(1,1,1,-1,-1,-1)$. We also give an exact certificate excluding seven mutually unbiased bases in ℂ$^{6}$; by Weiner's completion theorem, this yields an upper bound of five. Both certificates use only integer and rational arithmetic, and the complete verifier is included.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The paper claims that at most three mutually unbiased orthonormal bases exist in $\mathbb C^6$. The linked formalization proves a weaker family bound: every family in its mutually unbiased bases model has at most five members. It also proves a Fourier character-sum vanishing statement for order-six complex Hadamard matrices not equivalent to the Tao matrix, uniformly over coordinate permutations.

The selected statement does not establish the paper's upper bound of three or its computer-assisted exclusion of four arbitrary bases.

The linked formalization proves a cancellation lemma used in the order-six complex Hadamard analysis. Let $H$ and its entrywise square both be complex Hadamard matrices, and fix two distinct rows. If the cubes of their six entrywise ratios take only two distinct values, then the sum of the row-ratio terms over either specified cube fiber is zero.

This is a supporting Fourier cancellation statement. The paper's full character-sum vanishing theorem and its mutually unbiased bases bound are outside this selected statement.

## Lean: Order-six Hadamard Fourier vanishing and a five-basis upper bound

```lean
theorem fourier_and_family_bound :
    (∀ H : CMatrix, IsHadamard H → ¬Equivalent H tao →
      ∀ π : Equiv.Perm Coord, g H (permuteCharge π alpha) = 0) ∧
    (∀ n : ℕ, Attainable n → n ≤ 5)
```

Stated in [MUBSix.lean, line 56](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MUBSix.lean#L56). Proved in [lean/OAI/Analysis/MutuallyUnbiased/Main.lean, line 22](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/MutuallyUnbiased/Main.lean#L22).

## Lean: Cube-fiber cancellation for order-six Hadamard row ratios

```lean
lemma rowRatio_cubeFiber_sum_zero {H : Matrix6} (hH : IsComplexHadamard H)
    (hs : IsComplexHadamard (entrywiseSquare H)) {i j : Index} (hij : i ≠ j)
    (a b : ℂ) (hne : a ≠ b)
    (hab : ∀ k, rowRatio H i j k ^ 3 = a ∨ rowRatio H i j k ^ 3 = b) :
    ∑ k ∈ cubeFiber (rowRatio H i j) a, H i k * star (H j k) = 0
```

Stated in [HadamardCubeFiber.lean, line 28](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HadamardCubeFiber.lean#L28). Proved in [lean/OAI/LinearAlgebra/Hadamard/CubeFibers.lean, line 172](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/LinearAlgebra/Hadamard/CubeFibers.lean#L172).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/266.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/266.md)
