---
declaration: theorem
origin: cited
lean: SharpSymmetryBounds.sharp_bounds, SharpSymmetryBounds.rotation_bound_sharp, SharpSymmetryBounds.full_bound_sharp, SharpSymmetryBounds.equality_classification, SharpSymmetryBounds.family_attains_bound
statement: formalized
proof: formalized
---

# Sharp symmetry bounds for real plane algebraic curves

> Let C be an infinite real plane algebraic curve defined by a polynomial of degree d ≥ 2 that is irreducible over the complex numbers, and suppose C is not a circle. The project proves that the group of Euclidean symmetries of C (Mathlib isometries of ℂ mapping C onto itself) is finite, that its orientation-preserving part is cyclic of order at most max(d, 2d − 4), and that the full group has order at most 2d. Both bounds are attained in every degree d ≥ 2. For d ≥ 5 the curves attaining the rotation bound are classified: up to an orientation-preserving similarity they are the curves Re(z^(d−2)(|z|² + α)) = 0 with |α| = 1 and α not real, and conversely every such curve with d − 2 ≥ 3 attains the bound. The rotation bound uses the coefficient-weight criterion of Lebmeir and Richter-Gebert; the bound 2d sharpens the auxiliary bound 4d of Pach and de Zeeuw, and the quintic Re(z³(|z|² + i)) = 0, with six rotations, is a counterexample to the degree restriction in Lemma 9 of Alcázar, Lávička and Vršek (arXiv:1801.09962v1). This is Theorem 1 of the author's note; the note's second theorem is not included.

*Quoted from the card [LeanPool/projects/sharp-symmetry-bounds.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/sharp-symmetry-bounds.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SharpSymmetryBounds.sharp_bounds`](https://leanpool.github.io/lean-pool/LeanPool/SharpSymmetryBounds/Theorem1.html#SharpSymmetryBounds.sharp_bounds) (theorem; a main declaration), declared in [LeanPool/SharpSymmetryBounds/Theorem1.lean, line 100](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SharpSymmetryBounds/Theorem1.lean#L100): “For a real plane polynomial f of degree d ≥ 2, irreducible over ℂ, whose real zero set C is infinite and not a circle, the Euclidean symmetries of C form a finite set, the orientation-preserving ones are the powers of a single isometry and number at most max(d, 2d − 4), and all of them number at most 2d.” Its source, as the card gives it: “Note, Theorem 1 (bounds)”
- [`SharpSymmetryBounds.rotation_bound_sharp`](https://leanpool.github.io/lean-pool/LeanPool/SharpSymmetryBounds/Theorem1.html#SharpSymmetryBounds.rotation_bound_sharp) (theorem; a main declaration), declared in [LeanPool/SharpSymmetryBounds/Theorem1.lean, line 122](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SharpSymmetryBounds/Theorem1.lean#L122): “In every degree d ≥ 2 there is such a curve with exactly max(d, 2d − 4) orientation-preserving symmetries.” Its source, as the card gives it: “Note, Theorem 1 (sharpness of the rotation bound)”
- [`SharpSymmetryBounds.full_bound_sharp`](https://leanpool.github.io/lean-pool/LeanPool/SharpSymmetryBounds/Theorem1.html#SharpSymmetryBounds.full_bound_sharp) (theorem; a main declaration), declared in [LeanPool/SharpSymmetryBounds/Theorem1.lean, line 130](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SharpSymmetryBounds/Theorem1.lean#L130): “In every degree d ≥ 2 there is such a curve with exactly 2d Euclidean symmetries.” Its source, as the card gives it: “Note, Theorem 1 (sharpness of the full bound)”
- [`SharpSymmetryBounds.equality_classification`](https://leanpool.github.io/lean-pool/LeanPool/SharpSymmetryBounds/Theorem1.html#SharpSymmetryBounds.equality_classification) (theorem; a main declaration), declared in [LeanPool/SharpSymmetryBounds/Theorem1.lean, line 138](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SharpSymmetryBounds/Theorem1.lean#L138): “If d ≥ 5 and the curve has exactly 2d − 4 orientation-preserving symmetries, then an orientation-preserving similarity z ↦ a z + b maps it onto Re(z^(d−2)(|z|² + α)) = 0 for some α with |α| = 1 and nonzero imaginary part.” Its source, as the card gives it: “Note, Theorem 1 (equality case, d ≥ 5)”
- [`SharpSymmetryBounds.family_attains_bound`](https://leanpool.github.io/lean-pool/LeanPool/SharpSymmetryBounds/Theorem1.html#SharpSymmetryBounds.family_attains_bound) (theorem; a main declaration), declared in [LeanPool/SharpSymmetryBounds/Theorem1.lean, line 149](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SharpSymmetryBounds/Theorem1.lean#L149): “For m ≥ 3 and α with nonzero imaginary part, the curve Re(z^m(|z|² + α)) = 0 is the real zero set of a polynomial of degree m + 2, irreducible over ℂ, with infinite real locus, not a circle, and with exactly 2m orientation-preserving symmetries.” Its source, as the card gives it: “Note, Theorem 1 (converse)”

## Project

- Authors: Carlo Perassi.
- Source: *Sharp symmetry bounds for real algebraic curves (working note, 2026), Theorem 1* by Carlo Perassi, Background: P. Lebmeir and J. Richter-Gebert, Rotations, translations and symmetry detection for complexified curves, Computer Aided Geometric Design 25 (2008), 707–719, Section 4 (doi:10.1016/j.cagd.2008.09.004); J. Pach and F. de Zeeuw, Distinct distances on algebraic curves in the plane, arXiv:1308.0177v3, Lemma 2.6; J. G. Alcázar, M. Lávička and J. Vršek, Symmetries and similarities of planar algebraic curves using harmonic polynomials, arXiv:1801.09962v1, Lemma 9., [https://github.com/carlok/curve-symmetry-lean/blob/18d3984fd32e7482b98bc0ac42753e8508d236dd/sharp_symmetry_bounds.pdf](https://github.com/carlok/curve-symmetry-lean/blob/18d3984fd32e7482b98bc0ac42753e8508d236dd/sharp_symmetry_bounds.pdf).
- Project repository: [carlok/sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean), at commit [26deee2e](https://github.com/carlok/sharp-symmetry-bounds-lean/tree/26deee2e033ee17037c051e2ce7c9c739e4b0d59).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 14H50, 14P05, 51N20, 68V20.
- In Lean Pool: [LeanPool/SharpSymmetryBounds](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SharpSymmetryBounds), from the card [LeanPool/projects/sharp-symmetry-bounds.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/sharp-symmetry-bounds.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/sharp-symmetry-bounds.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/sharp-symmetry-bounds.yaml)
- [Lean Pool at bb99e52c: LeanPool/SharpSymmetryBounds](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SharpSymmetryBounds)
