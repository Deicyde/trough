---
declaration: theorem
origin: cited
lean: UnrestrictedBooleanMul.N4.mc_mul_four
statement: formalized
proof: formalized
---

# Exact Boolean multiplicative complexity of four-term polynomial multiplication

> Proves that multiplying two binary polynomials with n coefficients needs exactly 0, 1, 3, 6, and 9 AND gates for n = 0, 1, 2, 3, and 4, with XOR and constants free and arbitrary reuse of earlier nonlinear wires. The main lower bound excludes every eight-gate circuit for n = 4. Develops Boolean algebraic normal forms equivalent to all Boolean functions, a general circuit model, dimension bounds, circuit rewiring, a Reed-Muller minimum-weight theorem, and exterior-algebra and jet arguments controlling nonlinear feedback.

*Quoted from the card [LeanPool/projects/boolean-multiplication.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/boolean-multiplication.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`UnrestrictedBooleanMul.mc_mul_zero`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/SmallCases.html#UnrestrictedBooleanMul.mc_mul_zero) (theorem), declared in [LeanPool/BooleanMultiplication/SmallCases.lean, line 367](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BooleanMultiplication/SmallCases.lean#L367): “The empty polynomial multiplication map needs zero AND gates.” Its source, as the card gives it: “Proposition 2.3; the n = 0 target has no output coordinates.”
- [`UnrestrictedBooleanMul.mc_mul_one`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/SmallCases.html#UnrestrictedBooleanMul.mc_mul_one) (theorem), declared in [LeanPool/BooleanMultiplication/SmallCases.lean, line 370](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BooleanMultiplication/SmallCases.lean#L370): “Multiplying two one-coefficient binary polynomials needs exactly one AND gate.” Its source, as the card gives it: “Proposition 2.3.”
- [`UnrestrictedBooleanMul.mc_mul_two`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/SmallCases.html#UnrestrictedBooleanMul.mc_mul_two) (theorem), declared in [LeanPool/BooleanMultiplication/SmallCases.lean, line 373](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BooleanMultiplication/SmallCases.lean#L373): “Multiplying two two-coefficient binary polynomials needs exactly three AND gates.” Its source, as the card gives it: “Proposition 2.3.”
- [`UnrestrictedBooleanMul.mc_mul_three`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/N3.html#UnrestrictedBooleanMul.mc_mul_three) (theorem), declared in [LeanPool/BooleanMultiplication/N3.lean, line 494](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BooleanMultiplication/N3.lean#L494): “Multiplying two three-coefficient binary polynomials needs exactly six AND gates.” Its source, as the card gives it: “Proposition 2.4; the lower bound is proved internally.”
- [`UnrestrictedBooleanMul.N4.mc_mul_four`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/N4/Main.html#UnrestrictedBooleanMul.N4.mc_mul_four) (theorem; a main declaration), declared in [LeanPool/BooleanMultiplication/N4/Main.lean, line 62](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BooleanMultiplication/N4/Main.lean#L62): “Multiplying two four-coefficient binary polynomials needs exactly nine AND gates, allowing free XOR, constants, and unrestricted nonlinear reuse.” Its source, as the card gives it: “Theorem 9.1.”
- [`UnrestrictedBooleanMul.N4.no_eight_gate_circuit`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/N4/Main.html#UnrestrictedBooleanMul.N4.no_eight_gate_circuit) (theorem), declared in [LeanPool/BooleanMultiplication/N4/Main.lean, line 33](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BooleanMultiplication/N4/Main.lean#L33): “No eight-AND circuit with free XOR, constants, and arbitrary nonlinear reuse computes all seven output coefficients of the product of two four-coefficient binary polynomials.” Its source, as the card gives it: “Theorem 9.1, lower bound.”

## Project

- Authors: Gregory Morse.
- Source: *Unrestricted Boolean Multiplicative Complexity of Four-Term Binary Polynomial Multiplication: Rational Places, Hasse Jets, and the Failure of Nonlinear Feedback*, [arXiv:2608.30238v1](https://arxiv.org/abs/2608.30238v1).
- The card's note on its source: “The complete Lean release predates the arXiv v1 submission of 2026-08-31T04:45:12Z. The selected September 22 commit corrects release metadata; eligibility rests on the complete August 31 Lean release at 2ebc0cf42039e4b5de84cb7f9d97cad4791c669d. The August 29 release contained computational artifacts, not the Lean formalization. The author discloses GPT-5.6 Sol for original research and proof development, Opus 5 as a critical referee, and Codex for release preparation. Gregory Morse directed and reviewed the work and assumes responsibility. AI provenance records the proof-producing agent workflow; human direction alone is not classified as mixed formalization. The complete upstream MIT notice is retained in LeanPool/BooleanMultiplication.lean. Only the published n <= 4 dependency closure is imported; no n = 5 or n = 6 claim is made.”
- Project repository: [GregoryMorse/unrestricted-boolean-mul](https://github.com/GregoryMorse/unrestricted-boolean-mul), at commit [79a80176](https://github.com/GregoryMorse/unrestricted-boolean-mul/tree/79a801760668f52bb00a9e1a406e841375c58a6d).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 68Q06, 68Q17, 68W30, 15A75, 94D10.
- In Lean Pool: [LeanPool/BooleanMultiplication](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BooleanMultiplication), from the card [LeanPool/projects/boolean-multiplication.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/boolean-multiplication.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/boolean-multiplication.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/boolean-multiplication.yaml)
- [Lean Pool at 701389c0: LeanPool/BooleanMultiplication](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BooleanMultiplication)
