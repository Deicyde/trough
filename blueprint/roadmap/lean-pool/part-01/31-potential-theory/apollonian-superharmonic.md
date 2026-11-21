---
declaration: theorem
origin: cited
lean: ApollonianSuperharmonic.IntegerSuperharmonicCharacterization, ApollonianSuperharmonic.BandOdometerTheorem, ApollonianSuperharmonic.IntegralityTiling, ApollonianSuperharmonic.LambdaTiling, ApollonianSuperharmonic.BandLatticeEquality
statement: formalized
proof: formalized
---

# Apollonian classification of integer superharmonic matrices

> Characterizes quadratic growths of integer-valued functions on the square lattice with discrete Laplacian at most one by the downsets of matrices associated to circles in the Apollonian band packing, together with nonpositive-trace matrices. Constructs maximal periodic odometers and rotationally symmetric lattice tilings, and identifies the tiling and integrality lattices.

*Quoted from the card [LeanPool/projects/apollonian-superharmonic.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/apollonian-superharmonic.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ApollonianSuperharmonic.IntegerSuperharmonicCharacterization`](https://leanpool.github.io/lean-pool/LeanPool/ApollonianSuperharmonic/IntegerSuperharmonicCharacterization.html#ApollonianSuperharmonic.IntegerSuperharmonicCharacterization) (theorem; a main declaration), declared in [LeanPool/ApollonianSuperharmonic/IntegerSuperharmonicCharacterization.lean, line 30](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/ApollonianSuperharmonic/IntegerSuperharmonicCharacterization.lean#L30): “A real symmetric two-by-two matrix admits an integer-valued lattice function with its quadratic growth and discrete Laplacian at most one if and only if it is below a band-circle matrix in the positive-semidefinite order or has nonpositive trace.”
- [`ApollonianSuperharmonic.BandOdometerTheorem`](https://leanpool.github.io/lean-pool/LeanPool/ApollonianSuperharmonic/BandOdometerTheorem.html#ApollonianSuperharmonic.BandOdometerTheorem) (theorem; a main declaration), declared in [LeanPool/ApollonianSuperharmonic/BandOdometerTheorem.lean, line 29](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/ApollonianSuperharmonic/BandOdometerTheorem.lean#L29): “Every band-circle matrix has an integer superharmonic representative with the integrality-lattice cocycle identity, maximal among functions above it with discrete Laplacian at most one, up to a bounded difference.”
- [`ApollonianSuperharmonic.IntegralityTiling`](https://leanpool.github.io/lean-pool/LeanPool/ApollonianSuperharmonic/IntegralityTiling.html#ApollonianSuperharmonic.IntegralityTiling) (theorem; a main declaration), declared in [LeanPool/ApollonianSuperharmonic/IntegralityTiling.lean, line 26](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/ApollonianSuperharmonic/IntegralityTiling.lean#L26): “Every band circle admits a quarter-turn-symmetric lattice tile whose integrality-lattice translates tile the plane, with six neighboring tiles except for circles of curvature one.”
- [`ApollonianSuperharmonic.LambdaTiling`](https://leanpool.github.io/lean-pool/LeanPool/ApollonianSuperharmonic/LambdaTiling.html#ApollonianSuperharmonic.LambdaTiling) (theorem; a main declaration), declared in [LeanPool/ApollonianSuperharmonic/LambdaTiling.lean, line 27](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/ApollonianSuperharmonic/LambdaTiling.lean#L27): “Every band circle admits the analogous symmetric tiling by translates along its recursively defined tiling lattice.”
- [`ApollonianSuperharmonic.BandLatticeEquality`](https://leanpool.github.io/lean-pool/LeanPool/ApollonianSuperharmonic/BandLatticeEquality.html#ApollonianSuperharmonic.BandLatticeEquality) (theorem; a main declaration), declared in [LeanPool/ApollonianSuperharmonic/BandLatticeEquality.lean, line 25](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/ApollonianSuperharmonic/BandLatticeEquality.lean#L25): “For each band circle the recursively defined tiling lattice equals the lattice of integer vectors sent to integer vectors by its circle matrix.”

## Project

- Authors: Wesley Pegden.
- Source: *The Apollonian structure of integer superharmonic matrices*, [arXiv:1309.3267](https://arxiv.org/abs/1309.3267).
- Project repository: [wpegden/superharmonic](https://github.com/wpegden/superharmonic), at commit [45094b21](https://github.com/wpegden/superharmonic/tree/45094b210503f117502dec51caf737e96da221f8).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 31C20, 52C15, 60G50.
- In Lean Pool: [LeanPool/ApollonianSuperharmonic](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/ApollonianSuperharmonic), from the card [LeanPool/projects/apollonian-superharmonic.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/apollonian-superharmonic.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/apollonian-superharmonic.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/apollonian-superharmonic.yaml)
- [Lean Pool at 307e3125: LeanPool/ApollonianSuperharmonic](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/ApollonianSuperharmonic)
