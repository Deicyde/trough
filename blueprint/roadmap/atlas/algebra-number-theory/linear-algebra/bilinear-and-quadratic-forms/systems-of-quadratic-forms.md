---
declaration: section
origin: cited
lean: QuadraticForm.systemOrthogonalSum, QuadraticForm.systemOrthogonalSum_apply, QuadraticForm.systemOrthogonalSum_inl, QuadraticForm.systemOrthogonalSum_inr
statement: formalized
proof: formalized
---

# Systems of quadratic forms

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/systems-of-quadratic-forms/index.html).

## Orthogonal sum of systems of quadratic forms

Let $R$ be a commutative semiring, let
$M$ and $N$ be $R$-modules, and let $(Q_i)_{i \in \iota}$ and $(Q'_i)_{i \in \iota}$ be families
of quadratic forms on $M$ and on $N$ indexed by the same type $\iota$. Their pointwise
orthogonal sum is the family $(Q_i \oplus Q'_i)_{i \in \iota}$ of quadratic forms on
$M \times N$, where $Q_i \oplus Q'_i$ is the orthogonal sum given by
$(Q_i \oplus Q'_i)(x, y) = Q_i(x) + Q'_i(y)$.

Formalized by `QuadraticForm.systemOrthogonalSum`, a definition declared in [MathlibExt/LinearAlgebra/QuadraticForm/System.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/QuadraticForm/System.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/systems-of-quadratic-forms/index.html#system-orthogonal-sum).

## Evaluating an orthogonal sum of systems of quadratic forms

Let $R$ be a commutative
semiring, let $M$ and $N$ be $R$-modules, and let $(Q_i)_{i \in \iota}$ and
$(Q'_i)_{i \in \iota}$ be families of quadratic forms on $M$ and on $N$ indexed by the same
type $\iota$. For every index $i$ and every $(x, y) \in M \times N$, the $i$-th form of their
pointwise orthogonal sum takes the value $Q_i(x) + Q'_i(y)$ at $(x, y)$.

Formalized by `QuadraticForm.systemOrthogonalSum_apply`, a theorem declared in [MathlibExt/LinearAlgebra/QuadraticForm/System.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/QuadraticForm/System.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/systems-of-quadratic-forms/index.html#system-orthogonal-sum-apply).

## Orthogonal sum of systems on the left summand

Let $R$ be a commutative semiring,
let $M$ and $N$ be $R$-modules, and let $(Q_i)_{i \in \iota}$ and $(Q'_i)_{i \in \iota}$ be
families of quadratic forms on $M$ and on $N$ indexed by the same type $\iota$. For every
index $i$ and every $x \in M$, the $i$-th form of their pointwise orthogonal sum takes the
value $Q_i(x)$ at $(x, 0) \in M \times N$.

Formalized by `QuadraticForm.systemOrthogonalSum_inl`, a theorem declared in [MathlibExt/LinearAlgebra/QuadraticForm/System.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/QuadraticForm/System.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/systems-of-quadratic-forms/index.html#system-orthogonal-sum-inl).

## Orthogonal sum of systems on the right summand

Let $R$ be a commutative semiring,
let $M$ and $N$ be $R$-modules, and let $(Q_i)_{i \in \iota}$ and $(Q'_i)_{i \in \iota}$ be
families of quadratic forms on $M$ and on $N$ indexed by the same type $\iota$. For every
index $i$ and every $y \in N$, the $i$-th form of their pointwise orthogonal sum takes the
value $Q'_i(y)$ at $(0, y) \in M \times N$.

Formalized by `QuadraticForm.systemOrthogonalSum_inr`, a theorem declared in [MathlibExt/LinearAlgebra/QuadraticForm/System.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/QuadraticForm/System.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/systems-of-quadratic-forms/index.html#system-orthogonal-sum-inr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Systems of quadratic forms](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/systems-of-quadratic-forms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/systems-of-quadratic-forms)
