---
declaration: theorem
origin: cited
lean: AVenhance.anomalous_dissipation_full
statement: formalized
proof: formalized
---

# Anomalous diffusion by fractal homogenization

> For each positive Hölder exponent below one third, constructs a divergence-free periodic drift on the two-dimensional torus exhibiting anomalous dissipation for every mean-zero periodic H1 initial datum. The same drift admits uniform Hölder time estimates along a sequence of diffusivity intervals and two distinct vanishing-diffusivity limits for an explicit nonempty class of smooth data. Includes weak existence and uniqueness, Sobolev and Fourier/Galerkin infrastructure, flow derivatives, quantitative homogenization, and the multiscale construction. The no-selection result is the corrected version documented upstream, not the printed generality of the original paper's Proposition 5.5.

*Quoted from the card [LeanPool/projects/anomalous-diffusion-fractal-homogenization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/anomalous-diffusion-fractal-homogenization.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`AVenhance.anomalous_dissipation_full`](https://leanpool.github.io/lean-pool/LeanPool/AnomalousDiffusion/AVenhance/Statements/FullTheorem/AnomalousDissipationFull.html#AVenhance.anomalous_dissipation_full) (theorem; a main declaration), declared in [LeanPool/AnomalousDiffusion/AVenhance/Statements/FullTheorem/AnomalousDissipationFull.lean, line 49](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AnomalousDiffusion/AVenhance/Statements/FullTheorem/AnomalousDissipationFull.lean#L49): “For every alpha strictly between zero and one third, one periodic, divergence-free drift has joint spatial and temporal alpha-Hölder regularity and continuity into the spatial Hölder class. It exhibits anomalous dissipation with a positive rate depending only on the initial L2-to-gradient ratio, uniform Hölder-in-time L2 bounds along diffusivity intervals accumulating at zero, and two distinct transport limits along separated diffusivity sequences for a smooth mean-zero data class containing arbitrarily high cosine modes.” Its source, as the card gives it: “Upstream Statements/FullTheorem/AnomalousDissipationFull.lean and CITATION.cff, date-released 2026-10-02; the pinned completion commit is fad71d10bff031522cc598a37770238248186964, with committer timestamp 2026-10-02 16:04:04 UTC. Anomalous dissipation is the dimension-two case of Theorem 1.1 of arXiv:2305.05048; uniform time regularity and no-selection use upstream's documented corrections to Sections 5.4 and 5.5. The README explicitly records predominantly AI-produced proofs under the authors' supervision.”
- [`AVenhance.anomalous_dissipation`](https://leanpool.github.io/lean-pool/LeanPool/AnomalousDiffusion/AVenhance/Statements/Roots/AnomalousDissipation.html#AVenhance.anomalous_dissipation) (theorem), declared in [LeanPool/AnomalousDiffusion/AVenhance/Statements/Roots/AnomalousDissipation.lean, line 26](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AnomalousDiffusion/AVenhance/Statements/Roots/AnomalousDissipation.lean#L26): “For every positive alpha below one third there exists a periodic, divergence-free alpha-Hölder drift and a rate function taking values in (0,1], depending only on the initial L2-to-gradient ratio, such that the limsup as positive diffusivity tends to zero of integrated gradient dissipation is at least the squared rate times the initial L2 energy, for every mean-zero periodic H1 datum and corresponding weak solutions.”
- [`AVenhance.weak_wellposed`](https://leanpool.github.io/lean-pool/LeanPool/AnomalousDiffusion/AVenhance/Statements/Roots/WeakWellposed.html#AVenhance.weak_wellposed) (theorem), declared in [LeanPool/AnomalousDiffusion/AVenhance/Statements/Roots/WeakWellposed.lean, line 21](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AnomalousDiffusion/AVenhance/Statements/Roots/WeakWellposed.lean#L21): “Every bounded measurable periodic drift with positive diffusivity and periodic-cell L2 initial datum has a weak solution, unique up to spatial almost-everywhere equality at every time in [0,1].”

## Project

- Authors: Scott Armstrong, Vlad Vicol.
- Source: *Anomalous diffusion by fractal homogenization, Lean formalization*, [arXiv:2305.05048](https://arxiv.org/abs/2305.05048), [https://github.com/scottnarmstrong/AVAnomalousDiffusion/tree/fad71d10bff031522cc598a37770238248186964](https://github.com/scottnarmstrong/AVAnomalousDiffusion/tree/fad71d10bff031522cc598a37770238248186964).
- Project repository: [scottnarmstrong/AVAnomalousDiffusion](https://github.com/scottnarmstrong/AVAnomalousDiffusion), at commit [fad71d10](https://github.com/scottnarmstrong/AVAnomalousDiffusion/tree/fad71d10bff031522cc598a37770238248186964).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35B27, 35Q35, 76F30.
- In Lean Pool: [LeanPool/AnomalousDiffusion](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AnomalousDiffusion), from the card [LeanPool/projects/anomalous-diffusion-fractal-homogenization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/anomalous-diffusion-fractal-homogenization.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/anomalous-diffusion-fractal-homogenization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/anomalous-diffusion-fractal-homogenization.yaml)
- [Lean Pool at 2b205bf9: LeanPool/AnomalousDiffusion](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AnomalousDiffusion)
