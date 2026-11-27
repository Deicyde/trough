---
declaration: theorem
origin: cited
lean: Giambelli.diagramSchurPoly_eq_det_hook, Giambelli.schurPoly_eq_det_hook, Giambelli.giambelli_jt'
statement: formalized
proof: formalized
---

# Giambelli's identity for Schur polynomials

> Proves Giambelli's identity s_λ = det(s\_(α_i | β_j))\_{i,j`<`d}, expressing the Schur polynomial of a Young diagram with Durfee square of side d and Frobenius coordinates (α | β) as the determinant of the hook Schur polynomials, for Tau Ceti's Schur polynomials of Young diagrams (alphabet Fin N) and of partitions (any finite alphabet). The identity is first proved for Jacobi–Trudi determinants det(h\_{λ_i − i + j}) of any pair of symbols h, e with H(X)E(−X) = 1, by multiplying by a unitriangular matrix of e's, expanding along the resulting unit rows and using Frobenius complementarity; it is then specialized through Tau Ceti's Jacobi–Trudi identity. The explicit hook formula s\_(a | b) = Σ\_{r ≤ a} (−1)^r h\_{a−r} e\_{b+1+r} is included. Giambelli's identity is classical (Macdonald, Symmetric Functions and Hall Polynomials, Ch. I §3, Example 9). This is a port of the formalization in DataDotFoundation/RMTlib; the Lean proofs were produced with AI (Claude). Motivated by arXiv:1201.4478 (Dehaye), which uses Giambelli's identity in the Frobenius–Schur form of Olshanski–Regev–Vershik (§7.1.4). This project proves the classical Schur form.

*Quoted from the card [LeanPool/projects/giambelli.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/giambelli.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Giambelli.diagramSchurPoly_eq_det_hook`](https://leanpool.github.io/lean-pool/LeanPool/Giambelli/Schur.html#Giambelli.diagramSchurPoly_eq_det_hook) (theorem; a main declaration), declared in [LeanPool/Giambelli/Schur.lean, line 160](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Giambelli/Schur.lean#L160): “Giambelli's identity. For a Young diagram μ with Durfee square of side d and Frobenius coordinates (α_0, …, α\_{d−1} | β_0, …, β\_{d−1}), the Schur polynomial of μ in N variables is the determinant of the d × d matrix of hook Schur polynomials s\_(α_i | β_j).” Its source, as the card gives it: “Macdonald, Symmetric Functions and Hall Polynomials, Ch. I §3, Example 9.”
- [`Giambelli.schurPoly_eq_det_hook`](https://leanpool.github.io/lean-pool/LeanPool/Giambelli/Schur.html#Giambelli.schurPoly_eq_det_hook) (theorem; a main declaration), declared in [LeanPool/Giambelli/Schur.lean, line 173](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Giambelli/Schur.lean#L173): “Giambelli's identity for the Schur polynomial of a partition in any finite alphabet, with the hooks taken as partitions.” Its source, as the card gives it: “Macdonald, Symmetric Functions and Hall Polynomials, Ch. I §3, Example 9.”
- [`Giambelli.giambelli_jt'`](https://leanpool.github.io/lean-pool/LeanPool/Giambelli/Basic.html#Giambelli.giambelli_jt') (theorem; a main declaration), declared in [LeanPool/Giambelli/Basic.lean, line 541](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Giambelli/Basic.lean#L541): “Giambelli's identity for Jacobi–Trudi determinants det(h\_{λ_i − i + j}) of any pair of symbols h, e vanishing in negative degree with e_0 = 1 and H(X)E(−X) = 1.”
- [`Giambelli.diagramSchurPoly_hookDiagram`](https://leanpool.github.io/lean-pool/LeanPool/Giambelli/Schur.html#Giambelli.diagramSchurPoly_hookDiagram) (theorem), declared in [LeanPool/Giambelli/Schur.lean, line 147](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Giambelli/Schur.lean#L147): “The hook Schur polynomial s\_(a | b) equals Σ\_{r ≤ a} (−1)^r h\_{a−r} e\_{b+1+r}.”
- [`Giambelli.det_unitRows`](https://leanpool.github.io/lean-pool/LeanPool/Giambelli/Basic.html#Giambelli.det_unitRows) (theorem), declared in [LeanPool/Giambelli/Basic.lean, line 84](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Giambelli/Basic.lean#L84): “A determinant whose last rows are unit vectors equals a signed minor on the remaining columns.”

## Project

- Authors: Paul-Olivier Dehaye.
- Source: *Symmetric Functions and Hall Polynomials (2nd ed.), Chapter I, Section 3, Example 9* by I. G. Macdonald, [https://github.com/DataDotFoundation/RMTlib/blob/ac695b1/RMTlib/Symmetric/Giambelli.lean](https://github.com/DataDotFoundation/RMTlib/blob/ac695b1/RMTlib/Symmetric/Giambelli.lean).
- Project repository: [DataDotFoundation/RMTlib](https://github.com/DataDotFoundation/RMTlib), at commit ac695b1.
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”. The card's note: “The Lean proofs were produced with Claude (Anthropic) in DataDotFoundation/RMTlib and ported to the Lean Pool toolchain with Claude, reusing Tau Ceti's Jacobi–Trudi identity and h–e convolution.”
- License: Apache-2.0.
- MSC2020: 05E05, 15A15.
- In Lean Pool: [LeanPool/Giambelli](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Giambelli), from the card [LeanPool/projects/giambelli.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/giambelli.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/giambelli.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/giambelli.yaml)
- [Lean Pool at bb99e52c: LeanPool/Giambelli](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Giambelli)
