---
declaration: section
origin: cited
lean: OAI.MatrixMultiplication.complex_omega_le_nine_quarters, OAI.MatrixMultiplication.complex_alpha_gt_93_div_200, OAI.MatrixMultiplication.complex_rectangular_omega_lt_523_div_250, OAI.MatrixAllFields.MatrixMultiplication.AllFieldMain.omega_lt_source_constant
statement: formalized
proof: formalized
---

# 107. Matrix multiplication with exponent at most 9/4

3 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves $\omega\le9/4$ over ℂ, giving $O_\varepsilon(n^{9/4+\varepsilon})$ arithmetic operations for square matrix multiplication. In characteristic zero, some inner dimension $n^{a}$ with *a* > 0.465 permits $n^{2+o(1)}$ rectangular multiplication. Further square bounds give *ω* < 2.258 outside finitely many positive characteristics and *ω* < 2.371054886006746 over every fixed field.

## An Upper Bound of 9/4 for the Matrix Multiplication Exponent

We prove that the exponent of matrix multiplication over the complex numbers is at most 9/4.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf).

## Complex Matrix Multiplication Below 2.258 and Rectangular Bounds

Over every field of characteristic zero, we prove that the square matrix-multiplication exponent satisfies *ω* < 2.258, the dual exponent satisfies *α* > 0.465, and $\omega(1,0.709,1)\lt 2.092$. The strict square and *k* = 0.709 rectangular bounds also hold over every field except possibly in one finite set of positive characteristics, in the arithmetic-operation model.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf), secondary writeup; the Lean below formalizes results from it.

## Staggered extraction for exact matrix multiplication over every field

We prove that the arithmetic exponent of square matrix multiplication over every fixed field satisfies *ω* < 2.371054886006746. This includes every positive characteristic.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized results bound the complex matrix-multiplication exponent by $\omega(\mathbb C)\le9/4$, the dual exponent by $\alpha>0.465$, and the rectangular exponent at aspect ratio $0.709$ by $\omega(\mathbb C;1,0.709,1)<2.092$. The dual exponent is the supremum of rectangular aspect ratios attainable with exponent $2$. The arithmetic model counts additions, subtractions, and multiplications in finite division-free programs, with arbitrary positive exponent slack. The square bound implies the paper's weaker $2.258$ headline bound.

The formalized result gives the unconditional bound $\omega(F)<2.371054886006746$ for every field $F$, including finite fields and fields of positive characteristic. The exponent counts additions, subtractions, and multiplications in finite division-free arithmetic programs, with arbitrary positive exponent slack. No numerical inequalities remain as hypotheses. The result concerns arithmetic complexity, rather than bit complexity or practical crossover sizes.

## Lean: Complex square, dual, and rectangular exponent bounds

```lean
theorem complex_omega_le_nine_quarters :
    Arithmetic.omega ℂ ≤ (9 : ℝ) / 4
```

Stated in [MatrixMultiplication.lean, line 118](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatrixMultiplication.lean#L118). Proved in [lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean#L14). formalization.yaml lists it as one of the repository's main results.

```lean
theorem complex_alpha_gt_93_div_200 :
    (93 : ℝ) / 200 < Arithmetic.complexAlpha
```

Stated in [MatrixMultiplication.lean, line 122](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatrixMultiplication.lean#L122). Proved in [lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean#L19). formalization.yaml lists it as one of the repository's main results.

```lean
theorem complex_rectangular_omega_lt_523_div_250 :
    Arithmetic.rectangularOmega ℂ ((709 : ℝ) / 1000) < (523 : ℝ) / 250
```

Stated in [MatrixMultiplication.lean, line 126](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatrixMultiplication.lean#L126). Proved in [lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean#L25). formalization.yaml lists it as one of the repository's main results.

## Lean: Matrix-multiplication exponent over every field

```lean
theorem omega_lt_source_constant (F : Type u) [Field F] :
    Arithmetic.omega F < (2371054886006746 : ℝ) / 10 ^ 15 ∧
    (2371054886006746 : ℝ) / 10 ^ 15 < (2371056 : ℝ) / 10 ^ 6
```

Stated in [MatrixFields.lean, line 109](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatrixFields.lean#L109). Proved in [lean/OAI/LinearAlgebra/MatrixFields/Conclusions/AllFieldsBound.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/LinearAlgebra/MatrixFields/Conclusions/AllFieldsBound.lean#L17). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/107.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/107.md)
