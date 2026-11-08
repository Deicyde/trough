---
declaration: theorem
origin: cited
lean: LocalComplexGeometry.localAnalyticNullstellensatz
statement: formalized
proof: formalized
---

# Foundational local complex-analytic geometry

> Develops a common Lean foundation for several classical local theorems in several complex variables: complex-analytic Weierstrass preparation with full germ uniqueness, Noetherianity of holomorphic-germ rings, finite projection for hypersurface germs, the holomorphic constant-rank normal form, and the finite-family local analytic Nullstellensatz. The imported development also exposes the arbitrary-ideal Nullstellensatz and regular level-set, submersion, and immersion consequences.

*Quoted from the card [LeanPool/projects/local-complex-geometry.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/local-complex-geometry.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LocalComplexGeometry.localAnalyticNullstellensatz`](https://leanpool.github.io/lean-pool/LeanPool/LocalComplexGeometry/Palomar.html#LocalComplexGeometry.localAnalyticNullstellensatz) (theorem; a main declaration), declared in [LeanPool/LocalComplexGeometry/Palomar.lean, line 458](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LocalComplexGeometry/Palomar.lean#L458): “If a finite family of functions analytic at the origin has common zero set locally contained in the zero set of another analytic function, then a positive power of the latter is locally an analytic linear combination of the family.”
- [`LocalComplexGeometry.holomorphicGerm_isNoetherian`](https://leanpool.github.io/lean-pool/LeanPool/LocalComplexGeometry/Palomar.html#LocalComplexGeometry.holomorphicGerm_isNoetherian) (theorem), declared in [LeanPool/LocalComplexGeometry/Palomar.lean, line 37](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LocalComplexGeometry/Palomar.lean#L37): “For every finite complex dimension, including dimension zero, the local ring of holomorphic germs at the origin is Noetherian.”
- [`LocalComplexGeometry.hypersurface_finiteProjection`](https://leanpool.github.io/lean-pool/LeanPool/LocalComplexGeometry/Palomar.html#LocalComplexGeometry.hypersurface_finiteProjection) (theorem), declared in [LeanPool/LocalComplexGeometry/Palomar.lean, line 315](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LocalComplexGeometry/Palomar.lean#L315): “A nonzero hypersurface germ vanishing at the origin admits a linear coordinate change whose local quotient is finite free over the base germ ring, together with an explicit prepared equation and a proper, surjective finite-fiber projection of the local zero set.”
- [`LocalComplexGeometry.holomorphic_constantRank_normalForm`](https://leanpool.github.io/lean-pool/LeanPool/LocalComplexGeometry/Palomar.html#LocalComplexGeometry.holomorphic_constantRank_normalForm) (theorem), declared in [LeanPool/LocalComplexGeometry/Palomar.lean, line 410](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LocalComplexGeometry/Palomar.lean#L410): “An analytic map of locally constant complex rank is locally equivalent, through analytic source and target coordinates, to the standard rank projection.”
- [`ClassicalComplexWPT.classicalComplexWeierstrassPreparation`](https://leanpool.github.io/lean-pool/LeanPool/LocalComplexGeometry/ClassicalComplexWPT/Main.html#ClassicalComplexWPT.classicalComplexWeierstrassPreparation) (theorem), declared in [LeanPool/LocalComplexGeometry/ClassicalComplexWPT/Main.lean, line 32](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LocalComplexGeometry/ClassicalComplexWPT/Main.lean#L32): “A complex-analytic germ of exact order in one distinguished variable factors uniquely into a nonvanishing analytic unit and a monic Weierstrass polynomial whose analytic coefficient germs vanish at the origin.” Its source, as the card gives it: “BochaoKong/classical-complex-wpt, commit b4a7273fe5c9752753c52e10494097569089642d (2026-08-28).”
- [`LocalComplexGeometry.analyticNullstellensatz_ideal`](https://leanpool.github.io/lean-pool/LeanPool/LocalComplexGeometry/Nullstellensatz/Main.html#LocalComplexGeometry.analyticNullstellensatz_ideal) (theorem), declared in [LeanPool/LocalComplexGeometry/Nullstellensatz/Main.lean, line 35](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LocalComplexGeometry/Nullstellensatz/Main.lean#L35): “For every ideal of the local holomorphic-germ ring, the ideal of germs vanishing on its local zero set equals its radical.”
- [`LocalComplexGeometry.holomorphic_regularLevelSet_parametrization`](https://leanpool.github.io/lean-pool/LeanPool/LocalComplexGeometry/Analytic/LevelSet.html#LocalComplexGeometry.holomorphic_regularLevelSet_parametrization) (theorem), declared in [LeanPool/LocalComplexGeometry/Analytic/LevelSet.lean, line 112](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LocalComplexGeometry/Analytic/LevelSet.lean#L112): “Near a regular point, the level set of a holomorphic map admits an analytic parametrization with an analytic local inverse on the level set.”

## Project

- Authors: BochaoKong.
- Source: *Foundational theorems in local complex-analytic geometry* by BochaoKong.
- Project repository: [BochaoKong/nullstellensatz](https://github.com/BochaoKong/nullstellensatz), at commit [02969724](https://github.com/BochaoKong/nullstellensatz/tree/029697242294aea7989bf5d391199696a43490df).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 32A05, 32A10, 32B05, 32C25, 13E05.
- In Lean Pool: [LeanPool/LocalComplexGeometry](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LocalComplexGeometry), from the card [LeanPool/projects/local-complex-geometry.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/local-complex-geometry.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/local-complex-geometry.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/local-complex-geometry.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LocalComplexGeometry](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LocalComplexGeometry)
