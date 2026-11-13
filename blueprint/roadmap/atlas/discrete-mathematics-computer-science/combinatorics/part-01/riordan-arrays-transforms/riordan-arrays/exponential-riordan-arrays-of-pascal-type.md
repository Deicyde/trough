---
declaration: section
origin: cited
lean: MetaMathlibExt.exponentialPascalTypeSeries, MetaMathlibExt.exponentialPascalTypePair, MetaMathlibExt.exponentialPascalTypeMatrix
statement: formalized
proof: formalized
---

# Exponential Riordan arrays of Pascal type

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/exponential-riordan-arrays-of-pascal-type/index.html).

## Second series of the exponential Pascal-type pair

Let $R$ be a commutative ring
that is a $\mathbb{Q}$-algebra and let $r \in \mathbb{Q}$. This is the formal power series
$t + \frac{r}{2} t^2$ over $R$, the second component of the generating pair
$[e^t, t + r t^2/2]$ of the exponential Pascal-type matrix.

Formalized by `MetaMathlibExt.exponentialPascalTypeSeries`, a definition declared in [MathlibExt/NumberTheory/ExponentialPascalMatrix.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ExponentialPascalMatrix.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/exponential-riordan-arrays-of-pascal-type/index.html#exponential-pascal-type-series).

## Generating pair of the exponential Pascal-type matrix

Let $R$ be a commutative ring
that is a $\mathbb{Q}$-algebra and let $r \in \mathbb{Q}$. This is the pair of formal power
series $\left(e^t, t + \frac{r}{2} t^2\right)$ over $R$, written $[e^t, t + r t^2/2]$ in
exponential Riordan array notation.

Formalized by `MetaMathlibExt.exponentialPascalTypePair`, a definition declared in [MathlibExt/NumberTheory/ExponentialPascalMatrix.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ExponentialPascalMatrix.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/exponential-riordan-arrays-of-pascal-type/index.html#exponential-pascal-type-pair).

## Exponential Pascal-type matrix

Let $R$ be a commutative ring that is a
$\mathbb{Q}$-algebra and let $r \in \mathbb{Q}$. The exponential Pascal-type matrix with
parameter $r$ is the exponential Riordan array $[e^t, t + r t^2/2]$ over $R$: the matrix with
rows and columns indexed by the natural numbers whose $(n, k)$ entry is

$$\frac{n!}{k!} \, [t^n] \, e^t \left(t + \frac{r}{2} t^2\right)^k,$$

where $[t^n]$ takes the coefficient of $t^n$ in a formal power series over $R$ and the
rational number $n!/k!$ acts on $R$ through its $\mathbb{Q}$-algebra structure.

Formalized by `MetaMathlibExt.exponentialPascalTypeMatrix`, a definition declared in [MathlibExt/NumberTheory/ExponentialPascalMatrix.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ExponentialPascalMatrix.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/exponential-riordan-arrays-of-pascal-type/index.html#exponential-pascal-type-matrix).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential Riordan arrays of Pascal type](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/exponential-riordan-arrays-of-pascal-type/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/exponential-riordan-arrays-of-pascal-type)
