---
declaration: theorem
origin: cited
lean: Komlos.discrepancy_le_of_forall_sum_sq_le_one
statement: formalized
proof: formalized
---

# The Komlós and Beck–Fiala bounds with constant 36

> Proves that finitely many real vectors of Euclidean norm at most one admit signs whose sum has every coordinate bounded by 36, and deduces the Beck–Fiala discrepancy bound 36 times the square root of the maximum vertex degree for finite hypergraphs. The Karingula–Lovett splitting argument is supported by reusable finite-distribution, total-variation, transport, convex-hull, and matrix-discrepancy infrastructure. The near-invariant distribution uses discrete squared tent weights, and real vectors are handled by coordinatewise truncation toward zero.

*Quoted from the card [LeanPool/projects/komlos.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/komlos.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Komlos.discrepancy_le_of_forall_sum_sq_le_one`](https://leanpool.github.io/lean-pool/LeanPool/Komlos/Main.html#Komlos.discrepancy_le_of_forall_sum_sq_le_one) (theorem; a main declaration), declared in [LeanPool/Komlos/Main.lean, line 57](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Komlos/Main.lean#L57): “For a real matrix with arbitrary finite row and column index types, if each column has sum of squared entries at most one, its minimum signed-column discrepancy is at most 36.” Its source, as the card gives it: “Theorem 1.2, matrix form.”
- [`Komlos.exists_isColouring_forall_abs_sum_apply_le`](https://leanpool.github.io/lean-pool/LeanPool/Komlos/Main.html#Komlos.exists_isColouring_forall_abs_sum_apply_le) (theorem), declared in [LeanPool/Komlos/Main.lean, line 102](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Komlos/Main.lean#L102): “Any finite family of vectors in a finite-dimensional real Euclidean space, each of norm at most one, admits signs in {-1, 1} whose signed sum has absolute value at most 36 in every coordinate.” Its source, as the card gives it: “Theorem 1.2.”
- [`Hypergraph.exists_isColouring_forall_abs_finsum_le`](https://leanpool.github.io/lean-pool/LeanPool/Komlos/BeckFiala.html#Hypergraph.exists_isColouring_forall_abs_finsum_le) (theorem), declared in [LeanPool/Komlos/BeckFiala.lean, line 77](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Komlos/BeckFiala.lean#L77): “If a hypergraph has finitely many vertices and each vertex belongs to at most t edges, there is a {-1, 1} colouring of all vertices whose sum on each edge has absolute value at most 36 times sqrt(t).” Its source, as the card gives it: “Beck–Fiala consequence discussed in Section 1.”
- [`Komlos.exists_isColouring_mean_add_sum_mem_convexHull`](https://leanpool.github.io/lean-pool/LeanPool/Komlos/SignedSums.html#Komlos.exists_isColouring_mean_add_sum_mem_convexHull) (theorem), declared in [LeanPool/Komlos/SignedSums.lean, line 34](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Komlos/SignedSums.lean#L34): “For a finitely supported probability distribution on any real module and n vectors, if translation by six times each vector has total variation distance at most one third, some signed sum added to the mean belongs to the convex hull of the distribution's support.” Its source, as the card gives it: “Lemma 1.4, generalized to arbitrary real modules.”
- [`Komlos.exists_nearInvariant`](https://leanpool.github.io/lean-pool/LeanPool/Komlos/NearInvariant.html#Komlos.exists_nearInvariant) (theorem), declared in [LeanPool/Komlos/NearInvariant.lean, line 70](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Komlos/NearInvariant.lean#L70): “Every positive-denominator integer grid in finite-dimensional real coordinate space admits a finitely supported mean-zero probability distribution in [-6, 6]^d whose total variation distance under any grid translation of Euclidean norm at most one is at most one third.” Its source, as the card gives it: “Lemma 1.5, using discrete squared tent weights.”

## Project

- Authors: Gabriel Dahia.
- Source: *An elementary proof of the Komlós conjecture* by Sankeerth Rao Karingula, Shachar Lovett, [https://eccc.weizmann.ac.il/report/2026/188/](https://eccc.weizmann.ac.il/report/2026/188/).
- Project repository: [gdahia/Komlos](https://github.com/gdahia/Komlos), at commit [d8028574](https://github.com/gdahia/Komlos/tree/d802857449234318d557361b1dbb0a27e0258528).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11K38, 05C65, 05D40.
- In Lean Pool: [LeanPool/Komlos](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Komlos), from the card [LeanPool/projects/komlos.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/komlos.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/komlos.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/komlos.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Komlos](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Komlos)
