---
declaration: section
origin: cited
lean: MetaMathlibExt.hadamard_zero_one_determinant_bound, MathlibExt.LinearAlgebra.Matrix.VanDerWaerdenWanted.van_der_waerden_permanent
statement: formalized
proof: formalized
---

# Special matrices: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/index.html).

Classes of matrices defined by their structure or entries: Toeplitz, Hankel and circulant matrices, Hadamard and sign matrices, combinatorial matrices, nonnegative, doubly stochastic and totally positive matrices.

## Hadamard bound for zero-one determinants

Let $n \ge 1$ and let $B$ be an $n \times n$
real matrix each of whose entries is $0$ or $1$. Then

$$|\det B| \le 2^{-n} (n+1)^{(n+1)/2}.$$

The bound comes from bordering and signing $2B$ to obtain an $(n+1) \times (n+1)$ matrix with
entries $\pm 1$ whose determinant is $2^n \det B$, and applying Hadamard's determinant inequality.

## Sources

- Richard P. Brent and Adam B. Yedidia, "Computation of Maximal Determinants of Binary Circulant Matrices," Journal of Integer Sequences 21 (2018), Article 18.5.6. https://cs.uwaterloo.ca/journals/JIS/VOL21/Brent/brent11.tex, lines 226–238.

Formalized by `MetaMathlibExt.hadamard_zero_one_determinant_bound`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/HadamardZeroOneDeterminantBound.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/HadamardZeroOneDeterminantBound.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/index.html#hadamard-zero-one-determinant-bound).

## The van der Waerden permanent bound

For every integer $n \ge 1$ and every doubly stochastic
real $n \times n$ matrix $A$ (nonnegative entries, every row and every column summing to $1$), the
permanent of $A$ is at least $n!/n^n$.

## Sources

- G. P. Egorychev, Adv. Math. 42 (1981), 299-305, DOI 10.1016/0001-8708(81)90044-X; D. I. Falikman, Math. Notes 29 (1981), 475-479, DOI 10.1007/BF01163285.

Formalized by `MathlibExt.LinearAlgebra.Matrix.VanDerWaerdenWanted.van_der_waerden_permanent`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/VanDerWaerden.lean, line 1460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/VanDerWaerden.lean#L1460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/index.html#van-der-waerden-permanent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Special matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/special-matrices)
