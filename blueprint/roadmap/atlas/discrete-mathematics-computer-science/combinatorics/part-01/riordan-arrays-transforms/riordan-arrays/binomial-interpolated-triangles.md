---
declaration: section
origin: cited
lean: MetaMathlibExt.IsBinaryBinomialInterpolatedTriangle, MetaMathlibExt.risingDiagonal, MetaMathlibExt.risingDiagonal_const
statement: formalized
proof: formalized
---

# Binomial interpolated triangles

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/binomial-interpolated-triangles/index.html).

## Binary binomial interpolated triangle

For real numbers $a_0, a_1, \alpha, \beta$, a real
array $(a_{n,k})_{n,k \ge 0}$ is the binary binomial interpolated triangle
$BT(a_0, a_1, \alpha, \beta; \alpha, \beta)$ when $\alpha\beta \ne 0$, $|a_0| + |a_1| \ne 0$,
$a_{0,0} = a_0$, $a_{1,0} = a_1$, $a_{n,0} = \alpha\, a_{n-1,0} + \beta\, a_{n-2,0}$ for every
$n \ge 2$, and $a_{n,k} = \alpha\, a_{n,k-1} + \beta\, a_{n-1,k-1}$ for all $1 \le k \le n$.
Entries $a_{n,k}$ with $k > n$ are not constrained.

Formalized by `MetaMathlibExt.IsBinaryBinomialInterpolatedTriangle`, a definition declared in [MathlibExt/Combinatorics/Enumerative/RisingDiagonalSequence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RisingDiagonalSequence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/binomial-interpolated-triangles/index.html#is-binary-binomial-interpolated-triangle).

## Rising diagonal

For a real array $a = (a_{n,k})_{n,k \ge 0}$ and $n \ge 0$, the rising
diagonal of $a$ at level $n$ is the finite sequence $k \mapsto a_{n-k,k}$ indexed by
$0 \le k \le \lfloor n/2 \rfloor$.

Formalized by `MetaMathlibExt.risingDiagonal`, a definition declared in [MathlibExt/Combinatorics/Enumerative/RisingDiagonalSequence.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RisingDiagonalSequence.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/binomial-interpolated-triangles/index.html#rising-diagonal).

## Rising diagonals of a binary binomial interpolated triangle are constant

Let
$a_0, a_1, \alpha, \beta$ be real numbers and let $a = (a_{n,k})_{n,k \ge 0}$ be a real array that
is the binary binomial interpolated triangle $BT(a_0, a_1, \alpha, \beta; \alpha, \beta)$. Then
for every $n \ge 0$ the rising diagonal of $a$ at level $n$ is constant: $a_{n-i,i} = a_{n-j,j}$
for all $0 \le i, j \le \lfloor n/2 \rfloor$.

Formalized by `MetaMathlibExt.risingDiagonal_const`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RisingDiagonalSequence.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RisingDiagonalSequence.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/binomial-interpolated-triangles/index.html#rising-diagonal-const).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial interpolated triangles](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/binomial-interpolated-triangles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/binomial-interpolated-triangles)
