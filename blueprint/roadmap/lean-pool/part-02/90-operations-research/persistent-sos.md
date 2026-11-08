---
declaration: theorem
origin: cited
lean: PersistentSOS.persistent_failure, PersistentSOS.unique_persistent_failure
statement: formalized
proof: formalized
---

# Persistent failure of quartic sum-of-squares exactness

> Constructs explicit rational cubics in fourteen real variables whose Euclidean quartic regularizations have a strict ordinary sum-of-squares gap for every positive regularization, quadratic, and cubic parameter. A companion construction has a unique global minimizer and a positive-definite Hessian there. Exact moment certificates and a general SOS degree bridge certify the gap for arbitrary finite sums of squares of real polynomials.

*Quoted from the card [LeanPool/projects/persistent-sos.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/persistent-sos.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`PersistentSOS.persistent_failure`](https://leanpool.github.io/lean-pool/LeanPool/PersistentSOS/Main.html#PersistentSOS.persistent_failure) (theorem; a main declaration), declared in [LeanPool/PersistentSOS/Main.lean, line 88](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PersistentSOS/Main.lean#L88): “For every positive sigma, a, and b, the explicit fourteen-variable quartic sigma/4 times the Euclidean norm to the fourth power minus a/2 times the squared norm minus b times the displayed cubic has the stated attained global minimum, and subtracting that minimum is not an ordinary finite sum of squares of real polynomials.”
- [`PersistentSOS.unique_persistent_failure`](https://leanpool.github.io/lean-pool/LeanPool/PersistentSOS/UniqueMain.html#PersistentSOS.unique_persistent_failure) (theorem; a main declaration), declared in [LeanPool/PersistentSOS/UniqueMain.lean, line 60](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PersistentSOS/UniqueMain.lean#L60): “For all three positive parameters, the companion quartic has exactly one global minimizer, its actual polynomial Hessian is positive definite there, and its shift by the attained minimum is not an ordinary sum of squares.”
- [`PersistentSOS.quantitative_sos_gap`](https://leanpool.github.io/lean-pool/LeanPool/PersistentSOS/Main.html#PersistentSOS.quantitative_sos_gap) (theorem), declared in [LeanPool/PersistentSOS/Main.lean, line 54](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PersistentSOS/Main.lean#L54): “For positive sigma and a and any real b, every ordinary sum-of-squares lower bound is at most the stated minimum-value expression minus b times 753357629/500000000000 times the cube of the stated radius. When b is positive, that expression is the attained global minimum.”
- [`PersistentSOS.sphere_moment_gap`](https://leanpool.github.io/lean-pool/LeanPool/PersistentSOS/Main.html#PersistentSOS.sphere_moment_gap) (theorem), declared in [LeanPool/PersistentSOS/Main.lean, line 97](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PersistentSOS/Main.lean#L97): “An explicit linear functional on real polynomials has normalized radial moments, is nonnegative on all quadratic squares, annihilates the quadratic sphere localizers, and evaluates the cubic to 500753357629/500000000000, strictly above its sphere maximum of one.”

## Project

- Authors: JD Jones.
- Source: *Persistent SOS failure with an explicit unique global minimizer* by JD Jones.
- Project repository: [JD-Jones-ASES/persistent-sos](https://github.com/JD-Jones-ASES/persistent-sos), at commit [d432ff9a](https://github.com/JD-Jones-ASES/persistent-sos/tree/d432ff9a67594cc0fa7a7af1913320b46d2a86db).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, and its notice file gives no copyright line for it.
- MSC2020: 90C22, 90C26, 14P10.
- In Lean Pool: [LeanPool/PersistentSOS](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PersistentSOS), from the card [LeanPool/projects/persistent-sos.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/persistent-sos.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/persistent-sos.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/persistent-sos.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PersistentSOS](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PersistentSOS)
