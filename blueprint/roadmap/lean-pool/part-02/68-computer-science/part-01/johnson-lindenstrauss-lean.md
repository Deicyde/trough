---
declaration: theorem
origin: cited
lean: JL.johnson_lindenstrauss, JL.johnson_lindenstrauss_pointset
statement: formalized
proof: formalized
---

# The Johnson–Lindenstrauss Lemma and Quantized JL

> Formalizes the Johnson–Lindenstrauss lemma end to end — a Gaussian random projection preserves pairwise distances of a finite point set up to a (1 ± ε) factor, so a distortion-ε embedding of any m-point set exists once k is logarithmic in m — together with the quantized JL (QJL) one-bit sign sketch: unbiasedness of the asymmetric 1-bit estimator and its sub-Gaussian distortion bound.

*Quoted from the card [LeanPool/projects/johnson-lindenstrauss-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/johnson-lindenstrauss-lean.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`JL.johnson_lindenstrauss`](https://leanpool.github.io/lean-pool/LeanPool/JohnsonLindenstraussLean/Lemma.html#JL.johnson_lindenstrauss) (theorem; a main declaration), declared in [LeanPool/JohnsonLindenstraussLean/Lemma.lean, line 62](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JohnsonLindenstraussLean/Lemma.lean#L62): “The abstract probabilistic-method union bound — if the summed per-pair distortion-failure probability is below one, a distortion-preserving map exists.”
- [`JL.johnson_lindenstrauss_pointset`](https://leanpool.github.io/lean-pool/LeanPool/JohnsonLindenstraussLean/EndToEnd.html#JL.johnson_lindenstrauss_pointset) (theorem; a main declaration), declared in [LeanPool/JohnsonLindenstraussLean/EndToEnd.lean, line 65](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JohnsonLindenstraussLean/EndToEnd.lean#L65): “The end-to-end Johnson–Lindenstrauss lemma — a Gaussian random projection into k dimensions embeds any m-point set with (1 ± ε) distortion once k is logarithmic in m.” Its source, as the card gives it: “S. Dasgupta, A. Gupta, An elementary proof of a theorem of Johnson and Lindenstrauss, Random Structures and Algorithms 22 (2003), 60-65, doi:10.1002/rsa.10073.”
- [`JL.qjlEstimator_unbiased`](https://leanpool.github.io/lean-pool/LeanPool/JohnsonLindenstraussLean/QJL.html#JL.qjlEstimator_unbiased) (theorem), declared in [LeanPool/JohnsonLindenstraussLean/QJL.lean, line 257](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JohnsonLindenstraussLean/QJL.lean#L257): “The QJL asymmetric 1-bit estimator is unbiased for the normalized inner product between key and query.” Its source, as the card gives it: “A. Zandieh, M. Daliri, I. Han, QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead, AAAI 2025, arXiv:2406.03482.”
- [`JL.qjlEstimator_concentration_exp`](https://leanpool.github.io/lean-pool/LeanPool/JohnsonLindenstraussLean/QJLDistortion.html#JL.qjlEstimator_concentration_exp) (theorem), declared in [LeanPool/JohnsonLindenstraussLean/QJLDistortion.lean, line 594](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JohnsonLindenstraussLean/QJLDistortion.lean#L594): “Sub-Gaussian distortion bound for the QJL 1-bit estimator: deviation at least ε has probability at most 2·exp(-m·ε²/(π·‖q‖²)).” Its source, as the card gives it: “A. Zandieh, M. Daliri, I. Han, QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead, AAAI 2025, arXiv:2406.03482.”

## Project

- Authors: claytomode.
- Source: *Extensions of Lipschitz mappings into a Hilbert space* by William B. Johnson, Joram Lindenstrauss, [doi:10.1090/conm/026/737400](https://doi.org/10.1090/conm/026/737400).
- Project repository: [claytomode/johnson-lindenstrauss-lean](https://github.com/claytomode/johnson-lindenstrauss-lean).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 68W20, 60G15, 68P05.
- In Lean Pool: [LeanPool/JohnsonLindenstraussLean](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JohnsonLindenstraussLean), from the card [LeanPool/projects/johnson-lindenstrauss-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/johnson-lindenstrauss-lean.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/johnson-lindenstrauss-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/johnson-lindenstrauss-lean.yaml)
- [Lean Pool at 2b205bf9: LeanPool/JohnsonLindenstraussLean](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JohnsonLindenstraussLean)
