---
declaration: section
origin: cited
lean: OAI.CannonRelease.cannon
statement: formalized
proof: formalized
---

# 246. Cannon's conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Every word-hyperbolic group with boundary homeomorphic to $S^{2}$ admits a proper cocompact isometric action on hyperbolic three-space with finite kernel, proving Cannon's conjecture. Every torsion-free such group is therefore the fundamental group of a closed hyperbolic three-manifold.

## A Modulus Proof of Cannon’s Conjecture

We prove that every hyperbolic group whose boundary is homeomorphic to the two-sphere admits a proper cocompact isometric action on hyperbolic three-space with finite kernel. This resolves Cannon's conjecture positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Cannon's conjecture asks whether a hyperbolic group with boundary homeomorphic to the two-sphere acts geometrically on hyperbolic three-space. The formalization proves that such a group admits an isometric action on $\mathbb H^3$ that is proper and cocompact and has finite kernel. Hyperbolicity is expressed through uniformly thin geodesic triangles in a Cayley graph, and the boundary hypothesis is a homeomorphism with $S^2$.

## Lean: Cannon's geometric-action conclusion

Stated in [CannonGeometricAction.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CannonGeometricAction.lean).

```lean
theorem cannon (G : Type u) [Group G] [TopologicalSpace G] [DiscreteTopology G]
    (D : CayleyData G) (hthin : D.ThinTriangles)
    (hsphere : Nonempty (Boundary D ≃ₜ SphereTwo)) :
    ∃ ρ : G →* H3Isom, ProperAction ρ ∧ CocompactAction ρ ∧
      (ρ.ker : Set G).Finite
```

Proved in [lean/OAI/Geometry/Cannon/Main.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/Cannon/Main.lean#L23).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/246.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/246.md)
