---
declaration: theorem
origin: cited
lean: ConwaySoifer.ten_triangle_cover_lower_bound
statement: formalized
proof: formalized
---

# Conway–Soifer covering conjecture for n = 3

> Proves that ten congruent closed equilateral triangles covering a filled equilateral triangle of side three have common side at least one, with arbitrary positions, rotations and overlaps. Consequently ten unit triangles cannot cover a triangle of side 3 + ε for ε > 0. Includes reusable finite halfspace and ray-endpoint geometry, orientation-independent support and area bounds, and verified Bernstein polynomial interval checkers. Four derived contact cases and 100 kernel-checked certificates close the proof without a certificate hypothesis.

*Quoted from the card [LeanPool/projects/conway-soifer-three.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/conway-soifer-three.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`ConwaySoifer.ten_triangle_cover_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/ConwaySoifer.html#ConwaySoifer.ten_triangle_cover_lower_bound) (theorem; a main declaration), declared in [LeanPool/ConwaySoifer.lean, line 640](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConwaySoifer.lean#L640): “Any ten congruent closed equilateral triangles covering the filled equilateral target of side three have common side at least one. Positions, rotations and overlaps are unrestricted.” Its source, as the card gives it: “Public v1.0.0 release, 2026-09-11T17:12:25Z; upstream README and Geometry/Basic.lean.”
- [`ConwaySoifer.no_ten_unit_triangle_cover`](https://leanpool.github.io/lean-pool/LeanPool/ConwaySoifer.html#ConwaySoifer.no_ten_unit_triangle_cover) (theorem), declared in [LeanPool/ConwaySoifer.lean, line 643](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConwaySoifer.lean#L643): “For every ε > 0, ten closed equilateral triangles of side one cannot cover the filled equilateral target of side 3 + ε, regardless of position or rotation.” Its source, as the card gives it: “Upstream public theorem and its proved scaling corollary.”

## Project

- Authors: Vladislav Kuznetsov.
- Source: *The Conway–Soifer conjecture for n = 3: a Lean formalization*, [doi:10.5281/zenodo.22712658](https://doi.org/10.5281/zenodo.22712658), [https://github.com/AnanasClassic/conway-soifer-n3-lean/tree/b71b1d22b6f7ebb0f0173fc70a66075f44c86ce6](https://github.com/AnanasClassic/conway-soifer-n3-lean/tree/b71b1d22b6f7ebb0f0173fc70a66075f44c86ce6).
- Project repository: [AnanasClassic/conway-soifer-n3-lean](https://github.com/AnanasClassic/conway-soifer-n3-lean), at commit [b71b1d22](https://github.com/AnanasClassic/conway-soifer-n3-lean/tree/b71b1d22b6f7ebb0f0173fc70a66075f44c86ce6).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 52C15, 51M16.
- In Lean Pool: [LeanPool/ConwaySoifer](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConwaySoifer), from the card [LeanPool/projects/conway-soifer-three.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/conway-soifer-three.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/conway-soifer-three.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/conway-soifer-three.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ConwaySoifer](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ConwaySoifer)
