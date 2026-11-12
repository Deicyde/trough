---
declaration: section
origin: cited
lean: OAI.SmallCM.candidate_ring_properties
statement: formalized
proof: formalized
---

# 195. A counterexample to the small Cohen–Macaulay module conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a three-dimensional complete Noetherian normal local domain over ℂ with no nonzero finitely generated maximal Cohen–Macaulay module. A three-dimensional local domain essentially of finite type over ℂ has the same property, disproving the domain form of the small Cohen–Macaulay module conjecture.

## A Complete Local Domain without a Small Cohen–Macaulay Module

We construct a three-dimensional complete Noetherian normal local domain containing ℂ, with residue field ℂ, that has no nonzero finitely generated maximal Cohen–Macaulay module. This disproves the domain form of the small Cohen–Macaulay module conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The small Cohen–Macaulay module conjecture asks whether every complete Noetherian local domain has a nonzero finitely generated maximal Cohen–Macaulay module. The linked formalization verifies only the ring-theoretic candidate: there exists a three-dimensional complete Noetherian integrally closed local domain over $\mathbb C$ whose residue field is $\mathbb C$.

The proof uses a constructed completed surface cone. The resulting existence statement gives only the ring properties above; it does not assert the absence of small Cohen–Macaulay modules.

The paper's main counterexample requires that no nonzero finitely generated module over the ring has depth three. That conclusion, the numerical obstruction used to prove it, and the counterexample essentially of finite type are outside this comparison. The candidate's ring properties alone do not establish the counterexample.

## Lean: Ring-theoretic properties of the completed surface-cone candidate

Stated in [SurfaceConeCandidateSupport.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SurfaceConeCandidateSupport.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem candidate_ring_properties :
    ∃ (R : Type) (_ : CommRing R) (_ : IsDomain R) (_ : IsNoetherianRing R)
      (_ : IsIntegrallyClosed R) (_ : IsLocalRing R) (_ : Algebra ℂ R),
      IsAdicComplete (IsLocalRing.maximalIdeal R) R ∧
      ringKrullDim R = 3 ∧
      Function.Bijective (algebraMap ℂ (IsLocalRing.ResidueField R))
```

Proved in [lean/OAI/AlgebraicGeometry/SurfaceCones/CandidateRing.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/AlgebraicGeometry/SurfaceCones/CandidateRing.lean#L16).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/195.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/195.md)
