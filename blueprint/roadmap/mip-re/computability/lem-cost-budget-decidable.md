---
declaration: lemma
origin: cited
lean: MIPRE.Cost.Machine.stepCostD, MIPRE.Cost.Machine.stepCostD_toData, MIPRE.Cost.Machine.costStep, MIPRE.Cost.Machine.costStep_iterate, MIPRE.Cost.Machine.evalForCostD, MIPRE.Cost.Machine.evalForCostD_eq_some, MIPRE.Cost.Machine.haltsWithin_of_evalForCostD, MIPRE.Cost.Machine.haltsWithin_iff_evalForCostD, MIPRE.Cost.Machine.haltsWithinB, MIPRE.Cost.Machine.primrec_haltsWithinB, MIPRE.Cost.decidableHaltsWithin
statement: formalized
proof: formalized
---

# Halting within a cost budget is decidable

Whether a program of the cost model halts on a given input within a given cost is a primitive recursive predicate of the program, the input and the cost; in particular it is decidable.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Carry the cost along the run. The cost the evaluation machine charges at a step is a function of the configuration alone, so it is a function of the encoded configuration too (`Machine.stepCostD`, dispatching on the same seven program tags and four frame tags as the step function itself, and primitive recursive for the same reason); iterating the step function paired with the running total, from the initial configuration and total $0$, therefore computes the pair (configuration, accumulated cost) at every step (`costStep_iterate`). A derivation of cost $t$ is a machine run of at most $3t$ steps, so $3k + 1$ iterations suffice to reach the end of every run of cost at most $k$; and once the end is reached nothing more is charged, a final configuration being fixed by the step function and free. So the test is: iterate $3k + 1$ times, and report success if the configuration reached is final *and* the total is at most $k$ (`evalForCostD`). Completeness is the step count above; soundness is that the total at a final configuration is the cost of the derivation that reached it, which is the backward direction of the machine–derivation correspondence together with the freeness of the steps after the end.

## Lean

Formalized as [`MIPRE.Cost.Machine.stepCostD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.stepCostD), [`MIPRE.Cost.Machine.stepCostD_toData`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.stepCostD_toData), [`MIPRE.Cost.Machine.costStep`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.costStep), [`MIPRE.Cost.Machine.costStep_iterate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.costStep_iterate), [`MIPRE.Cost.Machine.evalForCostD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.evalForCostD), [`MIPRE.Cost.Machine.evalForCostD_eq_some`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.evalForCostD_eq_some), [`MIPRE.Cost.Machine.haltsWithin_of_evalForCostD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.haltsWithin_of_evalForCostD), [`MIPRE.Cost.Machine.haltsWithin_iff_evalForCostD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.haltsWithin_iff_evalForCostD), [`MIPRE.Cost.Machine.haltsWithinB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.haltsWithinB), [`MIPRE.Cost.Machine.primrec_haltsWithinB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Machine.primrec_haltsWithinB), [`MIPRE.Cost.decidableHaltsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.decidableHaltsWithin).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 508](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L508)
