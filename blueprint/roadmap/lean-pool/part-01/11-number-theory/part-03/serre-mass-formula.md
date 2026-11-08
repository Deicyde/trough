---
declaration: theorem
origin: cited
lean: MassFormula.tsum_one_div_q_pow_c
statement: formalized
proof: formalized
---

# Serre's mass formula for totally ramified local-field extensions

> Proves both of Serre's mass formulas for totally ramified separable extensions of a nonarchimedean local field of any positive degree, together with the discriminant bound, tame-ramification criterion, finiteness dichotomy, convergence, and automorphism-weighted orbit count. The proof develops Eisenstein monogenicity, quantitative Newton-Hensel lifting, local constancy of root counts, and Haar measures of lattices over discrete valuation rings.

*Quoted from the card [LeanPool/projects/serre-mass-formula.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/serre-mass-formula.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`MassFormula.tsum_one_div_q_pow_c`](https://leanpool.github.io/lean-pool/LeanPool/MassFormula/First.html#MassFormula.tsum_one_div_q_pow_c) (theorem; a main declaration), declared in [LeanPool/MassFormula/First.lean, line 2794](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MassFormula/First.lean#L2794): “For every nonarchimedean local field K with residue-field cardinality q and every positive integer n, the sum of q^(-c(L)) over the totally ramified degree-n subextensions L of a separable closure of K is n, where c(L) is the discriminant exponent minus n plus one.”
- [`MassFormula.tsum_one_div_w_mul_q_pow_c`](https://leanpool.github.io/lean-pool/LeanPool/MassFormula/Second.html#MassFormula.tsum_one_div_w_mul_q_pow_c) (theorem), declared in [LeanPool/MassFormula/Second.lean, line 98](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MassFormula/Second.lean#L98): “For every nonarchimedean local field K, positive n, and set of representatives of K-isomorphism classes of totally ramified separable degree-n extensions, the sum of 1/(|Aut_K(L)| q^c(L)) is one.”
- [`MassFormula.sigma_infinite_iff`](https://leanpool.github.io/lean-pool/LeanPool/MassFormula/Finiteness.html#MassFormula.sigma_infinite_iff) (theorem), declared in [LeanPool/MassFormula/Finiteness.lean, line 345](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MassFormula/Finiteness.lean#L345): “For positive n, the set of totally ramified separable degree-n subextensions is infinite exactly when K and its residue field have the same characteristic p and p divides n.”
- [`MassFormula.sub_one_le_d`](https://leanpool.github.io/lean-pool/LeanPool/MassFormula/Discriminant.html#MassFormula.sub_one_le_d) (theorem), declared in [LeanPool/MassFormula/Discriminant.lean, line 670](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MassFormula/Discriminant.lean#L670): “For positive n, the discriminant exponent of a totally ramified degree-n extension is at least n-1.”
- [`MassFormula.c_eq_zero_iff`](https://leanpool.github.io/lean-pool/LeanPool/MassFormula/Tame.html#MassFormula.c_eq_zero_iff) (theorem), declared in [LeanPool/MassFormula/Tame.lean, line 145](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MassFormula/Tame.lean#L145): “For positive n and a totally ramified degree-n extension, the wild discriminant exponent vanishes exactly when the residue characteristic does not divide n.”
- [`MassFormula.summable_one_div_q_pow_c`](https://leanpool.github.io/lean-pool/LeanPool/MassFormula/Convergence.html#MassFormula.summable_one_div_q_pow_c) (theorem), declared in [LeanPool/MassFormula/Convergence.lean, line 45](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MassFormula/Convergence.lean#L45): “For positive n, the real-valued series of the unweighted mass terms is summable.”
- [`MassFormula.ncard_isomorphic_mul_w`](https://leanpool.github.io/lean-pool/LeanPool/MassFormula/Orbit.html#MassFormula.ncard_isomorphic_mul_w) (theorem), declared in [LeanPool/MassFormula/Orbit.lean, line 129](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MassFormula/Orbit.lean#L129): “For a nonarchimedean local field K and a totally ramified separable extension L of positive degree n, the number of K-isomorphic copies of L inside a separable closure, multiplied by |Aut_K(L)|, is n.”

## Project

- Authors: Hyeon Seung-Hyeon.
- Source: *Une «formule de masse» pour les extensions totalement ramifiées de degré donné d'un corps local* by Jean-Pierre Serre, [https://gallica.bnf.fr/ark:/12148/bpt6k6234149b/f323.item](https://gallica.bnf.fr/ark:/12148/bpt6k6234149b/f323.item).
- Project repository: [0stellensatz/MassFormula](https://github.com/0stellensatz/MassFormula), at commit [7fa41a62](https://github.com/0stellensatz/MassFormula/tree/7fa41a621f724f110183904d3fd19c6730a932ad).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11S15, 11S05.
- In Lean Pool: [LeanPool/MassFormula](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MassFormula), from the card [LeanPool/projects/serre-mass-formula.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/serre-mass-formula.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/serre-mass-formula.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/serre-mass-formula.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MassFormula](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MassFormula)
