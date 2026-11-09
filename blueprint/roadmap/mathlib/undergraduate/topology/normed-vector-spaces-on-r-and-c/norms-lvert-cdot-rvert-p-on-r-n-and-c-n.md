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
- [Source of `PiLp.normedSpace` in Mathlib/Analysis/Normed/Lp/PiLp.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Normed/Lp/PiLp.lean#L862)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L427)
