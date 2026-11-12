---
declaration: section
origin: cited
lean: OAI.EuclideanSteinitzBergstrom.main
statement: formalized
proof: formalized
---

# 097. The Euclidean Steinitz–Bergström bound

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that any finite sequence in the Euclidean unit ball of ℝ$^{d}$ admits signs keeping every partial sum within $C\sqrt d$, independently of length. Consequently every zero-sum family can be reordered with the same bound on unsigned partial sums. A matching lower bound gives the optimal order $S_2(d)=\Theta(\sqrt d)$.

## The Euclidean Steinitz–Bergström theorem

Every prescribed-order finite sequence of vectors in the Euclidean unit ball of ℝ$^{d}$ has one signing for which every signed prefix has norm at most $C\sqrt d$, with *C* absolute and independent of the sequence length. Consequently, every indexed zero-sum family of unit-ball vectors admits an ordering with the same bound for its unsigned partial sums. This determines the Euclidean Steinitz constant up to absolute factors, $S_2(d)=\Theta(\sqrt d)$, and resolves the Euclidean Steinitz–Bergström conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result gives the Euclidean Steinitz–Bergström bound with one absolute constant $C$. For every finite family of vectors in the unit ball of $\mathbb R^d$, signs can be chosen so that every prefix in the prescribed order has norm at most $C\sqrt d$. When the vector sum is zero, a permutation makes every unsigned prefix satisfy the same bound. Repeated and zero vectors are included. The result is existential and does not supply an online algorithm.

## Lean: Euclidean signed and reordered prefix bounds

Stated in [SteinitzBergstrom.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SteinitzBergstrom.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main : ∃ C : ℝ, SignedPrefixBound C ∧ OrderingPrefixBound C
```

Proved in [lean/OAI/Analysis/Steinitz/Main.lean, line 111](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Steinitz/Main.lean#L111).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/097.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/097.md)
