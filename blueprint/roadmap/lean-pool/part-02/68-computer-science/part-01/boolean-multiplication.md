---
declaration: theorem
origin: cited
lean: UnrestrictedBooleanMul.N4.mc_mul_four
statement: formalized
proof: formalized
---

# Exact Boolean multiplicative complexity of four-term polynomial multiplication

> Proves that multiplying two binary polynomials with n coefficients needs exactly 0, 1, 3, 6, and 9 AND gates for n = 0, 1, 2, 3, and 4, with XOR and constants free and arbitrary reuse of earlier nonlinear wires. The main lower bound excludes every eight-gate circuit for n = 4. Develops Boolean algebraic normal forms equivalent to all Boolean functions, a general circuit model, dimension bounds, circuit rewiring, a Reed-Muller minimum-weight theorem, and exterior-algebra and jet arguments controlling nonlinear feedback.

*Quoted from the card [LeanPool/projects/boolean-multiplication.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/boolean-multiplication.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`UnrestrictedBooleanMul.mc_mul_zero`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/SmallCases.html#UnrestrictedBooleanMul.mc_mul_zero) (theorem), declared in [LeanPool/BooleanMultiplication/SmallCases.lean, line 367](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanMultiplication/SmallCases.lean#L367): “The empty polynomial multiplication map needs zero AND gates.” Its source, as the card gives it: “Proposition 2.3; the n = 0 target has no output coordinates.”
- [`UnrestrictedBooleanMul.mc_mul_one`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/SmallCases.html#UnrestrictedBooleanMul.mc_mul_one) (theorem), declared in [LeanPool/BooleanMultiplication/SmallCases.lean, line 370](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanMultiplication/SmallCases.lean#L370): “Multiplying two one-coefficient binary polynomials needs exactly one AND gate.” Its source, as the card gives it: “Proposition 2.3.”
- [`UnrestrictedBooleanMul.mc_mul_two`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/SmallCases.html#UnrestrictedBooleanMul.mc_mul_two) (theorem), declared in [LeanPool/BooleanMultiplication/SmallCases.lean, line 373](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanMultiplication/SmallCases.lean#L373): “Multiplying two two-coefficient binary polynomials needs exactly three AND gates.” Its source, as the card gives it: “Proposition 2.3.”
- [`UnrestrictedBooleanMul.mc_mul_three`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/N3.html#UnrestrictedBooleanMul.mc_mul_three) (theorem), declared in [LeanPool/BooleanMultiplication/N3.lean, line 494](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanMultiplication/N3.lean#L494): “Multiplying two three-coefficient binary polynomials needs exactly six AND gates.” Its source, as the card gives it: “Proposition 2.4; the lower bound is proved internally.”
- [`UnrestrictedBooleanMul.N4.mc_mul_four`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/N4/Main.html#UnrestrictedBooleanMul.N4.mc_mul_four) (theorem; a main declaration), declared in [LeanPool/BooleanMultiplication/N4/Main.lean, line 62](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanMultiplication/N4/Main.lean#L62): “Multiplying two four-coefficient binary polynomials needs exactly nine AND gates, allowing free XOR, constants, and unrestricted nonlinear reuse.” Its source, as the card gives it: “Theorem 9.1.”
- [`UnrestrictedBooleanMul.N4.no_eight_gate_circuit`](https://leanpool.github.io/lean-pool/LeanPool/BooleanMultiplication/N4/Main.html#UnrestrictedBooleanMul.N4.no_eight_gate_circuit) (theorem), declared in [LeanPool/BooleanMultiplication/N4/Main.lean, line 33](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanMultiplication/N4/Main.lean#L33): “No eight-AND circuit with free XOR, constants, and arbitrary nonlinear reuse computes all seven output coefficients of the product of two four-coefficient binary polynomials.” Its source, as the card gives it: “Theorem 9.1, lower bound.”

## Project

- Authors: Gregory Morse.
- Source: *Unrestricted Boolean Multiplicative Complexity of Four-Term Binary Polynomial Multiplication: Rational Places, Hasse Jets, and the Failure of Nonlinear Feedback*, [arXiv:2608.30238v1](https://arxiv.org/abs/2608.30238v1), [https://github.com/GregoryMorse/unrestricted-boolean-mul/tree/79a801760668f52bb00a9e1a406e841375c58a6d](https://github.com/GregoryMorse/unrestricted-boolean-mul/tree/79a801760668f52bb00a9e1a406e841375c58a6d).
- Project repository: [GregoryMorse/unrestricted-boolean-mul](https://github.com/GregoryMorse/unrestricted-boolean-mul), at commit [79a80176](https://github.com/GregoryMorse/unrestricted-boolean-mul/tree/79a801760668f52bb00a9e1a406e841375c58a6d).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 68Q06, 68Q17, 68W30, 15A75, 94D10.
- In Lean Pool: [LeanPool/BooleanMultiplication](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanMultiplication), from the card [LeanPool/projects/boolean-multiplication.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/boolean-multiplication.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/boolean-multiplication.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/boolean-multiplication.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BooleanMultiplication](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanMultiplication)
