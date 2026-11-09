---
declaration: theorem
origin: cited
lean: GrahamLPT.lpt_le_optMakespan, GrahamLPT.lpt_eq_bound_iff_graham
statement: formalized
proof: formalized
---

# Sharp list-scheduling and longest-processing-time bounds

> Formalizes identical-machine scheduling for arbitrary finite job sets with real processing times. Proves Graham's sharp list-scheduling and LPT approximation bounds, constructs their tight instances, characterizes all positive instances attaining the LPT bound, and establishes the supremum for every sufficiently large fixed job count.

*Quoted from the card [LeanPool/projects/graham-lpt.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/graham-lpt.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`GrahamLPT.listSchedule_le_optMakespan`](https://leanpool.github.io/lean-pool/LeanPool/GrahamLPT/ListBound.html#GrahamLPT.listSchedule_le_optMakespan) (theorem), declared in [LeanPool/GrahamLPT/ListBound.lean, line 60](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrahamLPT/ListBound.lean#L60): “For nonnegative processing times on m nonzero identical machines, every list schedule has makespan at most (2 - 1/m) times the optimal makespan.”
- [`GrahamLPT.lpt_le_optMakespan`](https://leanpool.github.io/lean-pool/LeanPool/GrahamLPT/LPTBound.html#GrahamLPT.lpt_le_optMakespan) (theorem; a main declaration), declared in [LeanPool/GrahamLPT/LPTBound.lean, line 69](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrahamLPT/LPTBound.lean#L69): “For nonnegative processing times on m nonzero identical machines, every longest-processing-time-first schedule has makespan at most (4/3 - 1/(3m)) times the optimal makespan.”
- [`GrahamLPT.isLeast_lpt_ratio`](https://leanpool.github.io/lean-pool/LeanPool/GrahamLPT/Ratio.html#GrahamLPT.isLeast_lpt_ratio) (theorem), declared in [LeanPool/GrahamLPT/Ratio.lean, line 53](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrahamLPT/Ratio.lean#L53): “For each nonzero machine count, 4/3 - 1/(3m) is the least universal approximation factor for LPT, over all finite nonnegative real job sets.”
- [`GrahamLPT.lpt_eq_bound_iff_graham`](https://leanpool.github.io/lean-pool/LeanPool/GrahamLPT/LPTForm.html#GrahamLPT.lpt_eq_bound_iff_graham) (theorem; a main declaration), declared in [LeanPool/GrahamLPT/LPTForm.lean, line 58](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrahamLPT/LPTForm.lean#L58): “For at least two machines and a nonempty set of positive-length jobs, an LPT schedule attains Graham's bound exactly if the instance is a positive scalar multiple and permutation of Graham's 2m + 1 jobs.”
- [`GrahamLPT.isLUB_lpt_ratio_of_card`](https://leanpool.github.io/lean-pool/LeanPool/GrahamLPT/FixedCount.html#GrahamLPT.isLUB_lpt_ratio_of_card) (theorem), declared in [LeanPool/GrahamLPT/FixedCount.lean, line 247](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrahamLPT/FixedCount.lean#L247): “For a nonzero machine count and every fixed job count n at least 2m + 1, the supremum of LPT-to-optimum makespan ratios over positive instances with n jobs remains 4/3 - 1/(3m).”
- [`GrahamLPT.exists_isLPTSchedule`](https://leanpool.github.io/lean-pool/LeanPool/GrahamLPT/Basic.html#GrahamLPT.exists_isLPTSchedule) (theorem), declared in [LeanPool/GrahamLPT/Basic.lean, line 319](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrahamLPT/Basic.lean#L319): “Every finite real job-length vector on a nonzero number of machines admits an LPT schedule.”
- [`GrahamLPT.exists_listSchedule_le`](https://leanpool.github.io/lean-pool/LeanPool/GrahamLPT/ListOptimum.html#GrahamLPT.exists_listSchedule_le) (theorem), declared in [LeanPool/GrahamLPT/ListOptimum.lean, line 160](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrahamLPT/ListOptimum.lean#L160): “Every assignment of nonnegative-length jobs is matched or improved by a list schedule in some ordering of the jobs.”

## Project

- Authors: JD Jones.
- Source: *Graham's bounds for list scheduling and LPT on identical machines* by JD Jones, [https://github.com/JD-Jones-ASES/graham-lpt-lean/tree/c8ed035b407cc554faf4b68df0cf3edc70058977](https://github.com/JD-Jones-ASES/graham-lpt-lean/tree/c8ed035b407cc554faf4b68df0cf3edc70058977).
- Project repository: [JD-Jones-ASES/graham-lpt-lean](https://github.com/JD-Jones-ASES/graham-lpt-lean), at commit [c8ed035b](https://github.com/JD-Jones-ASES/graham-lpt-lean/tree/c8ed035b407cc554faf4b68df0cf3edc70058977).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 68M20, 90B35, 68W25.
- In Lean Pool: [LeanPool/GrahamLPT](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrahamLPT), from the card [LeanPool/projects/graham-lpt.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/graham-lpt.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/graham-lpt.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/graham-lpt.yaml)
- [Lean Pool at 2b205bf9: LeanPool/GrahamLPT](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GrahamLPT)
