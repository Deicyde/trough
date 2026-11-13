---
declaration: section
origin: cited
lean: MetaMathlibExt.sylvester_law_of_inertia
statement: formalized
proof: formalized
---

# Bilinear and quadratic forms: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/index.html).

Bilinear and quadratic forms on vector spaces and modules: rank, orthogonal sums, inertia and congruence, and lattices with their duals and neighbours.

## Sylvester's law of inertia

Let $A$ and $B$ be real symmetric square matrices with rows
and columns indexed by a finite set $n$, and suppose $B = P^{\mathsf T} A P$ for some invertible
real matrix $P$ indexed by $n$. Then $A$ and $B$ have the same number of positive eigenvalues, the
same number of negative eigenvalues and the same number of zero eigenvalues, each counted with
multiplicity.

Proof: By the spectral theorem, the quadratic form of each matrix is a weighted sum of squares
whose weights are its eigenvalues. Congruence gives an equivalence of quadratic forms, and
invariance of the signature fixes the positive and negative counts; the zero count follows by
trichotomy.

## Sources

- J. J. Sylvester, *A demonstration of the theorem that every homogeneous quadratic polynomial is reducible by real orthogonal substitutions to the form of a sum of positive and negative squares*, Philosophical Magazine Ser. 4, 4(23) (1852), 138-142.

Formalized by `MetaMathlibExt.sylvester_law_of_inertia`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SylvesterInertia.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/SylvesterInertia.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/index.html#sylvester-law-of-inertia).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bilinear and quadratic forms](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/bilinear-and-quadratic-forms)
