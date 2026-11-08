---
declaration: theorem
origin: cited
lean: MinModulus.nmin_eq, MinModulus.elementaryAbelianTwoGroups_optimal
statement: formalized
proof: formalized
---

# Minimum modulus for the unique multiset-sum problem

> Formalizes the exact minimum modulus `N_min(n) = 2^n - 2^{floor(log_2 n)}` for the unique multiset-sum problem on the super-increasing residue set `{2^i - 1 : 0 <= i < n}`, and proves the sharp elementary-abelian-2-group lower bound `k >= n - 1` for unique multiset sums in `(Z/2Z)^k`.

*Quoted from the card [LeanPool/projects/min-modulus-unique-multiset-sum.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/min-modulus-unique-multiset-sum.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`MinModulus.nmin_eq`](https://leanpool.github.io/lean-pool/LeanPool/MinModulusUniqueMultisetSum/UniqueSums.html#MinModulus.nmin_eq) (theorem; a main declaration), declared in [LeanPool/MinModulusUniqueMultisetSum/UniqueSums.lean, line 935](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinModulusUniqueMultisetSum/UniqueSums.lean#L935): “Proves that among moduli `N >= 2` the least one making the super-increasing residue set `{2^i - 1 : 0 <= i < n}` valid for the unique multiset-sum problem is `2^n - 2^{floor(log_2 n)}`, for every `n >= 2` (stated as `IsLeast`).”
- [`MinModulus.elementaryAbelianTwoGroups_optimal`](https://leanpool.github.io/lean-pool/LeanPool/MinModulusUniqueMultisetSum/ElemAbelian2.html#MinModulus.elementaryAbelianTwoGroups_optimal) (theorem; a main declaration), declared in [LeanPool/MinModulusUniqueMultisetSum/ElemAbelian2.lean, line 163](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinModulusUniqueMultisetSum/ElemAbelian2.lean#L163): “Proves that if `g_0, ..., g_{n-1}` in `(Z/2Z)^k` have unique multiset sums, then `k >= n - 1`: an elementary abelian 2-group admitting such a family has order at least `2^(n - 1)`.”

## Project

- Authors: José A. R. Fonollosa.
- Source: *Minimum modulus for the unique multiset-sum problem, with an application to computing the permanent* by José A. R. Fonollosa, [arXiv:2607.08366](https://arxiv.org/abs/2607.08366).
- Project repository: [jarfo/min-modulus](https://github.com/jarfo/min-modulus).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11B75, 05D99.
- In Lean Pool: [LeanPool/MinModulusUniqueMultisetSum](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinModulusUniqueMultisetSum), from the card [LeanPool/projects/min-modulus-unique-multiset-sum.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/min-modulus-unique-multiset-sum.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/min-modulus-unique-multiset-sum.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/min-modulus-unique-multiset-sum.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MinModulusUniqueMultisetSum](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinModulusUniqueMultisetSum)
