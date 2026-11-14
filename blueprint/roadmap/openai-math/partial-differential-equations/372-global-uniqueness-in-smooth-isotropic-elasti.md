---
declaration: section
origin: cited
lean: OAI.Elasticity.global_uniqueness
statement: formalized
proof: formalized
---

# 372. Global uniqueness in smooth isotropic elasticity

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that full static boundary displacement-to-traction data determine both smooth real Lamé moduli on every bounded connected smooth domain in ℝ$^{3}$, provided *μ* > 0 and $3\lambda+2\mu\gt 0$ on the closure. Neither analyticity, proximity to constant coefficients nor prior knowledge near the boundary is required.

## Global Uniqueness for the Smooth Isotropic Elasticity Inverse Problem

We prove that the full static displacement-to-traction map uniquely determines both real smooth Lamé moduli on every bounded connected smooth domain in ℝ$^{3}$, provided *μ* > 0 and $3\lambda+2\mu\gt 0$ on the closure. This resolves the smooth three-dimensional isotropic elastic Calderón uniqueness problem under these positivity assumptions.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves global uniqueness in the three-dimensional static isotropic elasticity inverse problem. On a bounded connected smooth domain, let two pairs of smooth real Lamé moduli satisfy $\mu>0$ and $3\lambda+2\mu>0$ on the closure. If their full displacement-to-traction maps agree, then both Lamé moduli agree throughout the domain. The selected statement is uniqueness; it does not supply a reconstruction algorithm.

## Lean: Global uniqueness of smooth isotropic Lamé moduli

```lean
theorem global_uniqueness : MainClaim
```

Stated in [ElasticityUniqueness.lean, line 103](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ElasticityUniqueness.lean#L103). Proved in [lean/OAI/MathematicalPhysics/Elasticity/Uniqueness.lean, line 94](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Elasticity/Uniqueness.lean#L94).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/372.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/372.md)
