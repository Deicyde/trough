---
declaration: theorem
origin: cited
lean: MeasureTheory.Lp_Burkholder_inequality_martingaleTransform
statement: formalized
proof: formalized
---

# Burkholder Martingale Transform Inequality

> Formalizes Burkholder's sharp Lp inequality for real-valued martingale transforms: if `f` is a discrete martingale and `w` a predictable multiplier bounded by `1`, then the Lp norm of the transform `w ⋆ₘ f` is at most `(pStar p - 1)` times the Lp norm of `f`, where `pStar p` is the maximum of `p` and its conjugate exponent. The proof builds the Burkholder special function as a majorant of the relevant payoff in each exponent regime (`1 < p < 2`, `p = 2`, `p > 2`).

*Quoted from the card [LeanPool/projects/burkholder.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/burkholder.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`MeasureTheory.Lp_Burkholder_inequality_martingaleTransform`](https://leanpool.github.io/lean-pool/LeanPool/Burkholder/MartingaleTransforms.html#MeasureTheory.Lp_Burkholder_inequality_martingaleTransform) (theorem; a main declaration), declared in [LeanPool/Burkholder/MartingaleTransforms.lean, line 1382](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Burkholder/MartingaleTransforms.lean#L1382): “The sharp Lp Burkholder inequality: for a discrete martingale `f` and a predictable multiplier `w` with `|w n| ≤ 1`, the Lp norm of the martingale transform `(w ⋆ₘ f) n` is bounded by `(pStar p - 1)` times the Lp norm of `f n`.”
- [`MeasureTheory.martingaleTransform_martingale`](https://leanpool.github.io/lean-pool/LeanPool/Burkholder/MartingaleTransforms.html#MeasureTheory.martingaleTransform_martingale) (theorem), declared in [LeanPool/Burkholder/MartingaleTransforms.lean, line 210](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Burkholder/MartingaleTransforms.lean#L210): “The martingale transform of a martingale by a strongly predictable bounded multiplier is itself a martingale.”
- [`Majorants.exists_majorant_p_g_1`](https://leanpool.github.io/lean-pool/LeanPool/Burkholder/Majorants.html#Majorants.exists_majorant_p_g_1) (theorem), declared in [LeanPool/Burkholder/Majorants.lean, line 47](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Burkholder/Majorants.lean#L47): “For every exponent `p > 1` there exists a Burkholder majorant, the special function dominating the payoff and driving the inequality.”

## Project

- Authors: Daniel Smania.
- Source: *Boundary value problems and sharp inequalities for martingale transforms* by Donald L. Burkholder, [doi:10.1214/aop/1176993220](https://doi.org/10.1214/aop/1176993220).
- Project repository: [SmaniaD/Burkholder](https://github.com/SmaniaD/Burkholder).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60G42.
- In Lean Pool: [LeanPool/Burkholder](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Burkholder), from the card [LeanPool/projects/burkholder.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/burkholder.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/burkholder.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/burkholder.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Burkholder](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Burkholder)
