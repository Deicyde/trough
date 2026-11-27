---
declaration: theorem
origin: cited
lean: SixExponentials.SX.six_exponentials_of_numberField, SixExponentials.exists_transcendental_exp, SixExponentials.six_exponentials_theorem
statement: formalized
proof: formalized
---

# The six exponentials theorem of Lang and Ramachandra

> Proves the six exponentials theorem in the general form of Lang and Ramachandra: for d complex numbers x₁, …, x_d linearly independent over ℚ and l complex numbers y₁, …, y_l linearly independent over ℚ, with d + l < d l, at least one of the numbers exp(xᵢ yⱼ) is transcendental; more precisely, for every subfield K of ℂ of finite degree over ℚ some exp(xᵢ yⱼ) lies outside K. The classical six exponentials theorem is the case d = 2, l = 3. The proof is Schneider's method relative to a number field: Siegel's lemma gives an exponential polynomial with integer coefficients, not all zero, vanishing on a box of lattice points ∑ mⱼ yⱼ; a Cauchy estimate with zeros, played against Liouville's inequality, extends the vanishing from each box to the next; and an exponential polynomial vanishing on the whole lattice has zero coefficients by Dedekind's independence of characters. The pool's roy-strong-six project proves Roy's strong six exponentials theorem, whose hypotheses are linear independence over the algebraic numbers rather than over ℚ and whose proof goes through Philippon's multiplicity estimate; this project assumes only ℚ-independence, covers every (d, l) with d + l < d l, and gives the elementary auxiliary-function proof.

*Quoted from the card [LeanPool/projects/six-exponentials.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/six-exponentials.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SixExponentials.SX.six_exponentials_of_numberField`](https://leanpool.github.io/lean-pool/LeanPool/SixExponentials/NumberField.html#SixExponentials.SX.six_exponentials_of_numberField) (theorem; a main declaration), declared in [LeanPool/SixExponentials/NumberField.lean, line 33](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SixExponentials/NumberField.lean#L33): “If d + l < d l, x₁, …, x_d are complex numbers linearly independent over ℚ, y₁, …, y_l are complex numbers linearly independent over ℚ, and K is a subfield of ℂ of finite degree over ℚ, then some exp(xᵢ yⱼ) does not lie in K.” Its source, as the card gives it: “Lang 1966, chapter II; Ramachandra 1968 (number-field form)”
- [`SixExponentials.exists_transcendental_exp`](https://leanpool.github.io/lean-pool/LeanPool/SixExponentials/Main.html#SixExponentials.exists_transcendental_exp) (theorem; a main declaration), declared in [LeanPool/SixExponentials/Main.lean, line 31](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SixExponentials/Main.lean#L31): “If d + l < d l and the families x₁, …, x_d and y₁, …, y_l of complex numbers are each linearly independent over ℚ, then some exp(xᵢ yⱼ) is transcendental over ℚ.” Its source, as the card gives it: “Lang 1966, chapter II; Ramachandra 1968”
- [`SixExponentials.six_exponentials_theorem`](https://leanpool.github.io/lean-pool/LeanPool/SixExponentials/Statement.html#SixExponentials.six_exponentials_theorem) (theorem; a main declaration), declared in [LeanPool/SixExponentials/Statement.lean, line 28](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SixExponentials/Statement.lean#L28): “If x₁, x₂ are complex numbers linearly independent over ℚ and y₁, y₂, y₃ are complex numbers linearly independent over ℚ, then at least one of the six numbers exp(xᵢ yⱼ) is transcendental over ℚ.” Its source, as the card gives it: “Lang 1966, chapter II; Ramachandra 1968 (six exponentials theorem)”

## Project

- Authors: Carlo Perassi.
- Source: *Introduction to Transcendental Numbers, chapter II* by Serge Lang, S. Lang, Introduction to Transcendental Numbers, Addison-Wesley, 1966, chapter II; K. Ramachandra, Contributions to the theory of transcendental numbers I, Acta Arithmetica 14 (1968), 65–72..
- Project repository: [carlok/six-exponentials-lean](https://github.com/carlok/six-exponentials-lean), at commit [b42d65be](https://github.com/carlok/six-exponentials-lean/tree/b42d65be65fc4e4a7cea3ba965aabea8f1df8028).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11J81, 68V20.
- In Lean Pool: [LeanPool/SixExponentials](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SixExponentials), from the card [LeanPool/projects/six-exponentials.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/six-exponentials.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/six-exponentials.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/six-exponentials.yaml)
- [Lean Pool at bb99e52c: LeanPool/SixExponentials](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SixExponentials)
