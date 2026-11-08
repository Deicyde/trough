---
declaration: theorem
origin: cited
lean: GranvilleMoore.not_pow_succ_dvd_det_mooreMatrix_iff
statement: formalized
proof: formalized
---

# Integer Moore determinants and iterated Fermat quotients

> Proves Granville's integrality and congruence formulas for iterated Fermat quotients at odd primes, including the exceptional order p - 1. For 1 ≤ d ≤ p and integers x_j prime to p, it proves that the nonzero integer Moore determinant det(x_j^(p^i)) is divisible by p^C(d+1,3), and that the next power does not divide it exactly when the Fermat quotients q_p(x_j) are pairwise distinct modulo p. The development supplies polynomial coefficient identities, denominator-clearing and valuation estimates, a determinant reduction ladder, and weighted Vandermonde formulas over general commutative rings.

*Quoted from the card [LeanPool/projects/granville-moore.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/granville-moore.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`GranvilleMoore.exists_intCast_iteratedFermatQuot`](https://leanpool.github.io/lean-pool/LeanPool/GranvilleMoore/MasterExpansion.html#GranvilleMoore.exists_intCast_iteratedFermatQuot) (theorem), declared in [LeanPool/GranvilleMoore/MasterExpansion.lean, line 412](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GranvilleMoore/MasterExpansion.lean#L412): “For an odd prime p, an integer x not divisible by p, any j ≤ p - 1, and any k, the iterated Fermat quotient F^(j)\_k(x) is an integer.” Its source, as the card gives it: “Upstream README, first main result; attributed there to Granville.”
- [`GranvilleMoore.dvd_factorial_mul_sub_mul_pow`](https://leanpool.github.io/lean-pool/LeanPool/GranvilleMoore/MasterExpansion.html#GranvilleMoore.dvd_factorial_mul_sub_mul_pow) (theorem), declared in [LeanPool/GranvilleMoore/MasterExpansion.lean, line 477](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GranvilleMoore/MasterExpansion.lean#L477): “Under the same prime and unit hypotheses, for j ≤ p - 2 and any k, j! F^(j)\_k(x) is congruent to x q_p(x)^j modulo p, where q_p(x) = (x^(p-1) - 1)/p.” Its source, as the card gives it: “Upstream README, second main result.”
- [`GranvilleMoore.dvd_factorial_mul_sub_exceptional`](https://leanpool.github.io/lean-pool/LeanPool/GranvilleMoore/MasterExpansion.html#GranvilleMoore.dvd_factorial_mul_sub_exceptional) (theorem), declared in [LeanPool/GranvilleMoore/MasterExpansion.lean, line 710](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GranvilleMoore/MasterExpansion.lean#L710): “For an odd prime p and an integer x not divisible by p, (p-1)! F^(p-1)\_0(x) is congruent to x q_p(x)^(p-1) - x q_p(x) modulo p.” Its source, as the card gives it: “Upstream README, exceptional congruence.”
- [`GranvilleMoore.pow_dvd_det_mooreMatrix`](https://leanpool.github.io/lean-pool/LeanPool/GranvilleMoore/MooreDeterminant.html#GranvilleMoore.pow_dvd_det_mooreMatrix) (theorem), declared in [LeanPool/GranvilleMoore/MooreDeterminant.lean, line 334](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GranvilleMoore/MooreDeterminant.lean#L334): “For an odd prime p, 1 ≤ d ≤ p, and integers x_j not divisible by p with nonzero Moore determinant, p^C(d+1,3) divides det(x_j^(p^i)).” Its source, as the card gives it: “Upstream README, Moore determinant lower bound, in divisibility form.”
- [`GranvilleMoore.not_pow_succ_dvd_det_mooreMatrix_iff`](https://leanpool.github.io/lean-pool/LeanPool/GranvilleMoore/MooreDeterminant.html#GranvilleMoore.not_pow_succ_dvd_det_mooreMatrix_iff) (theorem; a main declaration), declared in [LeanPool/GranvilleMoore/MooreDeterminant.lean, line 356](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GranvilleMoore/MooreDeterminant.lean#L356): “Under those determinant hypotheses, its p-adic valuation is exactly C(d+1,3) if and only if the integer Fermat quotients q_p(x_j) have pairwise distinct residues modulo p. The Lean statement expresses exactness as failure of divisibility by p^(C(d+1,3)+1).” Its source, as the card gives it: “Upstream README, equality criterion, including d = p.”

## Project

- Authors: Ken Ono.
- Source: *The p-divisibility of the integer Moore determinant and iterated Fermat quotients*.
- Project repository: [AxiomMath/GranvilleMoore](https://github.com/AxiomMath/GranvilleMoore), at commit [16181f1f](https://github.com/AxiomMath/GranvilleMoore/tree/16181f1f6a46d3001c1011c8947df13bcede948c).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11A07, 11C20, 15A15.
- In Lean Pool: [LeanPool/GranvilleMoore](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GranvilleMoore), from the card [LeanPool/projects/granville-moore.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/granville-moore.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/granville-moore.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/granville-moore.yaml)
- [Lean Pool at 2b205bf9: LeanPool/GranvilleMoore](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GranvilleMoore)
