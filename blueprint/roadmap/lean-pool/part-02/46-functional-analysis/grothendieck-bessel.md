---
declaration: theorem
origin: cited
lean: GrothendieckBessel.main
statement: formalized
proof: formalized
---

# Grothendieck's theorem for Bessel sequences

> Every Bessel sequence with bound one in a complex Hilbert space has its Gram kernel represented by correlations of measurable functions bounded by one on the unit interval. The proof includes real and complex finite matrix decompositions, a Ball--Prodromou argument, and a countable moment-measure construction followed by standard Borel realization.

*Quoted from the card [LeanPool/projects/grothendieck-bessel.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/grothendieck-bessel.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`GrothendieckBessel.main`](https://leanpool.github.io/lean-pool/LeanPool/GrothendieckBessel.html#GrothendieckBessel.main) (theorem; a main declaration), declared in [LeanPool/GrothendieckBessel.lean, line 57](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrothendieckBessel.lean#L57): “Every countable Bessel sequence with bound one in a complex Hilbert space admits measurable functions on the unit interval, pointwise bounded by one, whose Lebesgue correlations equal its Gram kernel.”
- [`GrothendieckBessel.countable_unit_interval_realization`](https://leanpool.github.io/lean-pool/LeanPool/GrothendieckBessel/UnitIntervalRealization.html#GrothendieckBessel.countable_unit_interval_realization) (theorem), declared in [LeanPool/GrothendieckBessel/UnitIntervalRealization.lean, line 117](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrothendieckBessel/UnitIntervalRealization.lean#L117): “Every complex kernel on a countable index type whose finite quadratic forms are Hermitian positive contractions has a bounded measurable realization on the unit interval with exactly the prescribed correlations.”
- [`OlevskiiGram.hasRealConvexDecomposition`](https://leanpool.github.io/lean-pool/LeanPool/GrothendieckBessel/BallProdromou.html#OlevskiiGram.hasRealConvexDecomposition) (theorem), declared in [LeanPool/GrothendieckBessel/BallProdromou.lean, line 1716](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrothendieckBessel/BallProdromou.lean#L1716): “Every finite real symmetric matrix between zero and the identity is a finite convex combination of rank-one matrices formed from vectors in the coordinate unit cube.”

## Project

- Authors: Lukas Liehr, Mitchell A. Taylor, Peiyang Yu.
- Source: *Grothendieck's theorem for Bessel sequences* by Lukas Liehr, Mitchell A. Taylor, Peiyang Yu, [arXiv:2608.12280](https://arxiv.org/abs/2608.12280), [https://github.com/lukasliehr/GrothendieckBessel/tree/f1ad1c7680bce2b1ab4218a02bddd694fb57062a](https://github.com/lukasliehr/GrothendieckBessel/tree/f1ad1c7680bce2b1ab4218a02bddd694fb57062a).
- Project repository: [lukasliehr/GrothendieckBessel](https://github.com/lukasliehr/GrothendieckBessel), at commit [f1ad1c76](https://github.com/lukasliehr/GrothendieckBessel/tree/f1ad1c7680bce2b1ab4218a02bddd694fb57062a).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 46B15, 46B25, 46C05.
- In Lean Pool: [LeanPool/GrothendieckBessel](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrothendieckBessel), from the card [LeanPool/projects/grothendieck-bessel.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/grothendieck-bessel.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/grothendieck-bessel.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/grothendieck-bessel.yaml)
- [Lean Pool at 2b205bf9: LeanPool/GrothendieckBessel](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrothendieckBessel)
