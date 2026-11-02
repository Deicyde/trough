---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: PiLp.normedSpace
mathlib_file: Mathlib/Analysis/Normed/Lp/PiLp.lean
---

# Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$

The product of finitely many normed spaces is a normed space, with the `L^p` norm.

```lean
PiLp.normedSpace.{u_1, u_2, u_4} (p : ENNReal) (𝕜 : Type u_1) {ι : Type u_2} (β : ι → Type u_4)
  [hp : Fact (1 ≤ p)] [Fintype ι] [NormedField 𝕜] [(i : ι) → SeminormedAddCommGroup (β i)]
  [(i : ι) → NormedSpace 𝕜 (β i)] : NormedSpace 𝕜 (PiLp p β)
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `PiLp.normedSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Lp/PiLp.html#PiLp.normedSpace)
- [Source of `PiLp.normedSpace` in Mathlib/Analysis/Normed/Lp/PiLp.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Lp/PiLp.lean#L846)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L427)
