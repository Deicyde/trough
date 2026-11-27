---
declaration: theorem
origin: cited
lean: HubbardMoments.secondMomentHubbardWeighted, HubbardMoments.schriefferWolffHubbard, HubbardMoments.doubledPeierlsPhase, HubbardMoments.fourHopPermutations
statement: formalized
proof: formalized
---

# Spectral moments of the projected Hubbard configuration graph

> Constructs finite fermion creation and annihilation matrices and the projected Hubbard hopping operator. Proves the weighted second-moment formula for Hermitian hopping, the vanishing of the Schrieffer–Wolff cross term on triangle-free graphs, the doubled Peierls phase of the second-order pair hop, and the classification of permutations induced by four closed hard-core hops. Includes finite-population moment identities and torus calculations used in the paper.

*Quoted from the card [LeanPool/projects/hubbard-spectral-moments.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/hubbard-spectral-moments.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`HubbardMoments.secondMomentHubbardWeighted`](https://leanpool.github.io/lean-pool/LeanPool/HubbardMoments/Main.html#HubbardMoments.secondMomentHubbardWeighted) (theorem; a main declaration), declared in [LeanPool/HubbardMoments/Main.lean, line 208](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HubbardMoments/Main.lean#L208): “In a nonempty no-double-occupancy spin sector with n particles on N sites, N at least two, the projected hopping matrix for Hermitian bond amplitudes has normalized second moment n(N-n)/(N(N-1)) times the sum of squared moduli of the off-diagonal hopping amplitudes.”
- [`HubbardMoments.schriefferWolffHubbard`](https://leanpool.github.io/lean-pool/LeanPool/HubbardMoments/Main.html#HubbardMoments.schriefferWolffHubbard) (theorem; a main declaration), declared in [LeanPool/HubbardMoments/Main.lean, line 200](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HubbardMoments/Main.lean#L200): “For the Hubbard hopping operator on a triangle-free graph, the cross term between projected hopping and the virtual operator vanishes when the projected states have no double occupation and the intermediate states each contain a doubly occupied site.”
- [`HubbardMoments.doubledPeierlsPhase`](https://leanpool.github.io/lean-pool/LeanPool/HubbardMoments/Main.html#HubbardMoments.doubledPeierlsPhase) (theorem; a main declaration), declared in [LeanPool/HubbardMoments/Main.lean, line 87](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HubbardMoments/Main.lean#L87): “Evaluating the second-order two-particle effective matrix element for a pair hopping to an adjacent site gives 2t²/U with twice the single-hop phase.”
- [`HubbardMoments.fourHopPermutations`](https://leanpool.github.io/lean-pool/LeanPool/HubbardMoments/Main.html#HubbardMoments.fourHopPermutations) (theorem; a main declaration), declared in [LeanPool/HubbardMoments/Main.lean, line 164](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HubbardMoments/Main.lean#L164): “A closed walk of four single-particle hops with exclusion can induce only the identity, a transposition or a three-cycle.”

## Project

- Authors: Daniel Souza.
- Source: *Spectral Moments of the Projected Hubbard Configuration Graph: Connectivity, Exchange, and Virtual Doublons* by Daniel Souza, [arXiv:2611.19929](https://arxiv.org/abs/2611.19929), [https://github.com/zhineos/hubbard-spectral-moments/tree/66d5104785daae03e2f91bbb681aa0fbcea1e6d4/lean](https://github.com/zhineos/hubbard-spectral-moments/tree/66d5104785daae03e2f91bbb681aa0fbcea1e6d4/lean).
- Project repository: [zhineos/hubbard-spectral-moments](https://github.com/zhineos/hubbard-spectral-moments), at commit [66d51047](https://github.com/zhineos/hubbard-spectral-moments/tree/66d5104785daae03e2f91bbb681aa0fbcea1e6d4).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 81V70, 05C50, 82B20.
- In Lean Pool: [LeanPool/HubbardMoments](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HubbardMoments), from the card [LeanPool/projects/hubbard-spectral-moments.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/hubbard-spectral-moments.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/hubbard-spectral-moments.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/hubbard-spectral-moments.yaml)
- [Lean Pool at bb99e52c: LeanPool/HubbardMoments](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/HubbardMoments)
