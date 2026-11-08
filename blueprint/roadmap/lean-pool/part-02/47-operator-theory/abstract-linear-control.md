---
declaration: theorem
origin: cited
lean: AbstractLinearControl.ALCS.zero_class
statement: formalized
proof: formalized
---

# Continuity and zero-class properties of abstract linear control systems

> Proves that every abstract linear control system with bounded L-infinity inputs between real or complex Banach spaces is zero-class, and hence has continuous input-response trajectories. No integral representation or reflexivity assumption is required. Includes finite-p continuity, a finite-p system with constant response norm, and a scalar zero-class system without integral representation or Orlicz-heart admissibility. Reusable infrastructure includes Phillips' lemma, strongly continuous semigroup bounds, half-line Lp concatenation and shifts, invariant Hahn-Banach extensions, and periodic invariant means.

*Quoted from the card [LeanPool/projects/abstract-linear-control.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/abstract-linear-control.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`AbstractLinearControl.ALCS.zero_class`](https://leanpool.github.io/lean-pool/LeanPool/AbstractLinearControl/ZeroClass.html#AbstractLinearControl.ALCS.zero_class) (theorem; a main declaration), declared in [LeanPool/AbstractLinearControl/ZeroClass.lean, line 682](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AbstractLinearControl/ZeroClass.lean#L682): “For every abstract linear control system with L-infinity inputs between real or complex Banach spaces, the norms of its input-response operators tend to zero as time tends to zero from the right.” Its source, as the card gives it: “Theorem 1.5 of version 2, completed in Lean on 2026-10-03.”
- [`AbstractLinearControl.ALCS.continuousOn_Phi`](https://leanpool.github.io/lean-pool/LeanPool/AbstractLinearControl/ContinuityLinfty.html#AbstractLinearControl.ALCS.continuousOn_Phi) (theorem), declared in [LeanPool/AbstractLinearControl/ContinuityLinfty.lean, line 65](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AbstractLinearControl/ContinuityLinfty.lean#L65): “For every bounded input of such a system, its input-response trajectory is continuous on the nonnegative half-line.” Its source, as the card gives it: “Corollary 1.6.”
- [`AbstractLinearControl.ALCS.continuousOn_Phi_of_ne_top`](https://leanpool.github.io/lean-pool/LeanPool/AbstractLinearControl/ContinuityFiniteP.html#AbstractLinearControl.ALCS.continuousOn_Phi_of_ne_top) (theorem), declared in [LeanPool/AbstractLinearControl/ContinuityFiniteP.lean, line 131](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AbstractLinearControl/ContinuityFiniteP.lean#L131): “For every abstract linear control system with finite exponent p at least one and complete state space, each Lp input has a continuous input-response trajectory on the nonnegative half-line.” Its source, as the card gives it: “Proposition 1.3.”
- [`AbstractLinearControl.exists_system_norm_Phi_eq_one`](https://leanpool.github.io/lean-pool/LeanPool/AbstractLinearControl/Examples/FinitePNotZeroClass.html#AbstractLinearControl.exists_system_norm_Phi_eq_one) (theorem), declared in [LeanPool/AbstractLinearControl/Examples/FinitePNotZeroClass.lean, line 489](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AbstractLinearControl/Examples/FinitePNotZeroClass.lean#L489): “For every finite exponent p at least one, there exist real Banach input and state spaces and an abstract linear control system whose input-response operator has norm one at every positive time.” Its source, as the card gives it: “Proposition 3.1.”
- [`AbstractLinearControl.ExoticMean.Counterexample.no_representation`](https://leanpool.github.io/lean-pool/LeanPool/AbstractLinearControl/Examples/NoRepresentation.html#AbstractLinearControl.ExoticMean.Counterexample.no_representation) (theorem), declared in [LeanPool/AbstractLinearControl/Examples/NoRepresentation.lean, line 496](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AbstractLinearControl/Examples/NoRepresentation.lean#L496): “There exists a scalar abstract linear control system with identity semigroup and response norm equal to time, which has no integral representation and is not admissible for any of the formalized Young-function Orlicz hearts.” Its source, as the card gives it: “Proposition 3.3; formal Young functions include the paper's class.”
- [`AbstractLinearControl.Phillips.full`](https://leanpool.github.io/lean-pool/LeanPool/AbstractLinearControl/Background/Phillips.html#AbstractLinearControl.Phillips.full) (theorem), declared in [LeanPool/AbstractLinearControl/Background/Phillips.lean, line 665](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AbstractLinearControl/Background/Phillips.lean#L665): “For a pointwise null sequence of bounded linear functionals on real or complex bounded sequences, each sequence of atomic coefficients is absolutely summable, its sum of norms tends to zero, and its diagonal coefficient tends to zero.” Its source, as the card gives it: “Lemma 2.2.”

## Project

- Authors: Frédéric Marbach, GPT-6 Pro, Claude Opus 5.5.
- Source: *Continuity of solutions to abstract linear control systems*, [https://github.com/frederic-marbach/alcs/tree/bda56576f8b2730b73a55f273511c80fabbe56f4](https://github.com/frederic-marbach/alcs/tree/bda56576f8b2730b73a55f273511c80fabbe56f4).
- Project repository: [frederic-marbach/alcs](https://github.com/frederic-marbach/alcs), at commit [bda56576](https://github.com/frederic-marbach/alcs/tree/bda56576f8b2730b73a55f273511c80fabbe56f4).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 47D06, 93C25, 46E30.
- In Lean Pool: [LeanPool/AbstractLinearControl](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AbstractLinearControl), from the card [LeanPool/projects/abstract-linear-control.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/abstract-linear-control.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/abstract-linear-control.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/abstract-linear-control.yaml)
- [Lean Pool at 2b205bf9: LeanPool/AbstractLinearControl](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AbstractLinearControl)
