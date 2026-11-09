---
declaration: theorem
origin: cited
lean: ArithmeticTriangleRemovalInVectorSpaces.exists_subset_card_sdiff_add_le_forall_add_ne_zero, ArithmeticTriangleRemovalInVectorSpaces.card_le_rpow_one_sub_c_mul, ArithmeticTriangleRemovalInVectorSpaces.div_pow_rpow_C_mul_sq_le_card_triangles, ArithmeticTriangleRemovalInVectorSpaces.le_rpow_C_sub_of_forall_exists_subset
statement: formalized
proof: formalized
---

# A tight bound for Green's arithmetic triangle removal lemma in vector spaces

> Proves the arithmetic triangle removal lemma in F_p^n with the polynomial bound of Fox and Lovász. If X × Y × Z contains fewer than (ε/3)^(C_p) N^2 solutions of x + y + z = 0, where N = p^n, C_p = 1 + 1/c_p and c_p is the Kleinberg–Sawin–Speyer exponent, then removing at most εN elements leaves none. Also proves the Kleinberg–Sawin–Speyer slice-rank bound p^((1 - c_p) n) on multicolored sum-free families, the lower bound (m/N)^(C_p) N^2 on the number of triangles spanned by m vertex-disjoint triangles, and that the exponent C_p is optimal, with an explicit threshold ε₀. The tightness construction formalizes Pebody's coupling theorem for decreasing mass functions and the Kleinberg–Sawin–Speyer construction of large multicolored sum-free families, using Behrend's three-term-progression-free sets.

*Quoted from the card [LeanPool/projects/arithmetic-triangle-removal-in-vector-spaces.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/arithmetic-triangle-removal-in-vector-spaces.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ArithmeticTriangleRemovalInVectorSpaces.exists_subset_card_sdiff_add_le_forall_add_ne_zero`](https://leanpool.github.io/lean-pool/LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.html#ArithmeticTriangleRemovalInVectorSpaces.exists_subset_card_sdiff_add_le_forall_add_ne_zero) (theorem; a main declaration), declared in [LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.lean, line 76](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.lean#L76): “For a prime p, ε ≥ 0 and X, Y, Z ⊆ F_p^n, if fewer than (ε/3)^(C_p) p^(2n) triples (x, y, z) ∈ X × Y × Z satisfy x + y + z = 0, then there are X' ⊆ X, Y' ⊆ Y, Z' ⊆ Z with |X \\ X'| + |Y \\ Y'| + |Z \\ Z'| ≤ ε p^n such that no triple in X' × Y' × Z' sums to zero.” Its source, as the card gives it: “Theorem 1.”
- [`ArithmeticTriangleRemovalInVectorSpaces.card_le_rpow_one_sub_c_mul`](https://leanpool.github.io/lean-pool/LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.html#ArithmeticTriangleRemovalInVectorSpaces.card_le_rpow_one_sub_c_mul) (theorem; a main declaration), declared in [LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.lean, line 54](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.lean#L54): “For a prime p, a finite family of triples (x_i, y_i, z_i) in F_p^n with x_i + y_j + z_k = 0 exactly when i = j = k has at most p^((1 - c_p) n) members, where p^(1 - c_p) is the infimum over 0 < x < 1 of x^(-(p-1)/3) (1 + x + ... + x^(p-1)).” Its source, as the card gives it: “Theorem 2 (Kleinberg, Sawin and Speyer).”
- [`ArithmeticTriangleRemovalInVectorSpaces.div_pow_rpow_C_mul_sq_le_card_triangles`](https://leanpool.github.io/lean-pool/LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.html#ArithmeticTriangleRemovalInVectorSpaces.div_pow_rpow_C_mul_sq_le_card_triangles) (theorem; a main declaration), declared in [LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.lean, line 64](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.lean#L64): “For a prime p and X, Y, Z ⊆ F_p^n, if X × Y × Z contains m vertex-disjoint triples summing to zero, then it contains at least (m/N)^(C_p) N^2 triples summing to zero, where N = p^n.” Its source, as the card gives it: “Theorem 3.”
- [`ArithmeticTriangleRemovalInVectorSpaces.le_rpow_C_sub_of_forall_exists_subset`](https://leanpool.github.io/lean-pool/LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.html#ArithmeticTriangleRemovalInVectorSpaces.le_rpow_C_sub_of_forall_exists_subset) (theorem; a main declaration), declared in [LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.lean, line 189](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArithmeticTriangleRemovalInVectorSpaces/ZMod.lean#L189): “For a prime p, η > 0 and 0 < ε < ε₀(p, η), every δ such that, in every dimension n, fewer than δ p^(2n) zero-sum triples can be destroyed by removing ε p^n elements, satisfies δ ≤ ε^(C_p - η); ε₀ is an explicit function of p and η.” Its source, as the card gives it: “Theorem 1, second part, via the construction of Section 3.”

## Project

- Authors: Gabriel Dahia.
- Source: *A tight bound for Green's arithmetic triangle removal lemma in vector spaces* by Jacob Fox, László Miklós Lovász, [arXiv:1606.01230](https://arxiv.org/abs/1606.01230).
- Project repository: [gdahia/ArithmeticTriangleRemovalInVectorSpaces](https://github.com/gdahia/ArithmeticTriangleRemovalInVectorSpaces), at commit [3bddc92e](https://github.com/gdahia/ArithmeticTriangleRemovalInVectorSpaces/tree/3bddc92e8027badc994ba8993f7c625e60c7b13a).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11B30, 05D40, 11T99.
- In Lean Pool: [LeanPool/ArithmeticTriangleRemovalInVectorSpaces](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArithmeticTriangleRemovalInVectorSpaces), from the card [LeanPool/projects/arithmetic-triangle-removal-in-vector-spaces.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/arithmetic-triangle-removal-in-vector-spaces.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/arithmetic-triangle-removal-in-vector-spaces.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/arithmetic-triangle-removal-in-vector-spaces.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ArithmeticTriangleRemovalInVectorSpaces](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArithmeticTriangleRemovalInVectorSpaces)
