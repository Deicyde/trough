---
declaration: theorem
origin: cited
lean: ModuleCat.projectiveDimension_add_depth_eq_depth
statement: formalized
proof: formalized
---

# The Auslander–Buchsbaum formula

For a nonzero finite module `M` of finite projective
dimension over a Noetherian local ring `R`, `projectiveDimension M + depth M = depth R`.
Stacks, Proposition 10.111.1 (090V).

```lean
ModuleCat.projectiveDimension_add_depth_eq_depth.{v, u} {R : Type u} [CommRing R] [IsLocalRing R]
  [IsNoetherianRing R] [Small.{v, u} R] (M : ModuleCat R) [Module.Finite R ↑M] [Nontrivial ↑M]
  (hM : CategoryTheory.projectiveDimension M ≠ ⊤) :
  CategoryTheory.projectiveDimension M + ↑(IsLocalRing.depth M) = ↑(IsLocalRing.depth ↧R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ModuleCat.projectiveDimension_add_depth_eq_depth`](https://taucetiproject.org/docs/TauCeti/RingTheory/Depth/AuslanderBuchsbaum.html#ModuleCat.projectiveDimension_add_depth_eq_depth).

## Sources

- [Tau Ceti documentation: `ModuleCat.projectiveDimension_add_depth_eq_depth`](https://taucetiproject.org/docs/TauCeti/RingTheory/Depth/AuslanderBuchsbaum.html#ModuleCat.projectiveDimension_add_depth_eq_depth)
- [Source of `ModuleCat.projectiveDimension_add_depth_eq_depth` in TauCeti/RingTheory/Depth/AuslanderBuchsbaum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Depth/AuslanderBuchsbaum.lean#L151)
- [Tau Ceti roadmap status: Purity of the branch locus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PurityOfBranchLocus/STATUS.md)
