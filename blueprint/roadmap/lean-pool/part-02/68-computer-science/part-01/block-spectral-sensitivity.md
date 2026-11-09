---
declaration: theorem
origin: cited
lean: BSLambda.Final.exists_bs_gt_lam_rpow
statement: formalized
proof: formalized
---

# Block sensitivity can exceed spectral sensitivity squared

> Constructs a total Boolean function on 14011 blocks of 144 bits with block sensitivity at least 14011 and squared spectral sensitivity at most U = 7149 + 2 sqrt(150108). Proves the strict separation lambda(f)^2.12 < bs(f), multiplicativity of spectral sensitivity under arbitrary block composition, and an exponential lower bound with factor 14011/U > 1.768 for the self-composed family. Includes reusable finite product probability, an asymmetric Lovasz local lemma, partial Boolean assignments, certificate-family spectral bounds, and a Paley doubly regular tournament. The formalized explicit exponent is 2.12; the exact logarithmic exponent is also retained.

*Quoted from the card [LeanPool/projects/block-spectral-sensitivity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/block-spectral-sensitivity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`BSLambda.Final.exists_bs_gt_lam_rpow`](https://leanpool.github.io/lean-pool/LeanPool/BlockSpectralSensitivity/Main.html#BSLambda.Final.exists_bs_gt_lam_rpow) (theorem; a main declaration), declared in [LeanPool/BlockSpectralSensitivity/Main.lean, line 297](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BlockSpectralSensitivity/Main.lean#L297): “There exists a total Boolean function on ZMod 14011 times Fin 144 whose block sensitivity strictly exceeds its spectral sensitivity raised to the real exponent 2.12.” Its source, as the card gives it: “Upstream Main.lean; bs_lambda.txt Sections 5-12 and 14.”
- [`BSLambda.Final.exists_counterexample`](https://leanpool.github.io/lean-pool/LeanPool/BlockSpectralSensitivity/Main.html#BSLambda.Final.exists_counterexample) (theorem), declared in [LeanPool/BlockSpectralSensitivity/Main.lean, line 305](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BlockSpectralSensitivity/Main.lean#L305): “There exists a gate labelling whose certificate-union indicator f has bs(f) at least 14011, lambda(f)^2 at most U = 7149 + 2 sqrt(150108), and lambda(f)^alpha at most bs(f), where alpha = 2 log(14011)/log(U) > 2.” Its source, as the card gives it: “Upstream Main.lean; bs_lambda.txt Sections 5-12 and 14.”
- [`BSLambda.Final.exists_ratio_blowup`](https://leanpool.github.io/lean-pool/LeanPool/BlockSpectralSensitivity/Main.html#BSLambda.Final.exists_ratio_blowup) (theorem), declared in [LeanPool/BlockSpectralSensitivity/Main.lean, line 316](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BlockSpectralSensitivity/Main.lean#L316): “A single gate labelling yields, for every natural m, an m-fold self-composition F_m satisfying (14011/U)^m \* lambda(F_m)^2 <= bs(F_m). The auxiliary theorem ratio_gt proves 14011/U > 1.768.” Its source, as the card gives it: “Upstream Main.lean; bs_lambda.txt Section 14, division-free bound.”
- [`BSLambda.lam_comp`](https://leanpool.github.io/lean-pool/LeanPool/BlockSpectralSensitivity/Spectral/Multiplicative.html#BSLambda.lam_comp) (theorem), declared in [LeanPool/BlockSpectralSensitivity/Spectral/Multiplicative.lean, line 512](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BlockSpectralSensitivity/Spectral/Multiplicative.lean#L512): “For any Boolean functions on finite coordinate types, spectral sensitivity of their block composition equals the product of their spectral sensitivities, including the degenerate cases.” Its source, as the card gives it: “Upstream Spectral/Multiplicative.lean; composition theorem used in Section 14.”
- [`BSLambda.LLL.pr_avoid_pos`](https://leanpool.github.io/lean-pool/LeanPool/BlockSpectralSensitivity/LLL/Asymmetric.html#BSLambda.LLL.pr_avoid_pos) (theorem), declared in [LeanPool/BlockSpectralSensitivity/LLL/Asymmetric.lean, line 228](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BlockSpectralSensitivity/LLL/Asymmetric.lean#L228): “In a finite uniform product of nonempty alphabets, events supported on specified coordinate sets have positive probability of all being avoided if each event probability is at most its weight times the product of one minus the weights of its dependent neighbours, with every weight strictly between zero and one.” Its source, as the card gives it: “Upstream LLL/Asymmetric.lean; asymmetric local lemma in Section 10.”

## Project

- Authors: Alex Meiburg.
- Source: *Block Sensitivity can exceed Spectral Sensitivity Squared*, [arXiv:2608.00851](https://arxiv.org/abs/2608.00851).
- Project repository: [Timeroot/BS_Lam](https://github.com/Timeroot/BS_Lam), at commit [7bd39a8d](https://github.com/Timeroot/BS_Lam/tree/7bd39a8d41ee7910d3296d0477ad18f8fff9d870).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q17, 05D40, 05C50.
- In Lean Pool: [LeanPool/BlockSpectralSensitivity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BlockSpectralSensitivity), from the card [LeanPool/projects/block-spectral-sensitivity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/block-spectral-sensitivity.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/block-spectral-sensitivity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/block-spectral-sensitivity.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BlockSpectralSensitivity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BlockSpectralSensitivity)
