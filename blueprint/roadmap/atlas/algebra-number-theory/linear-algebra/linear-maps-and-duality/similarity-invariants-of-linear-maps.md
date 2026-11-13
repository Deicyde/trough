---
declaration: section
origin: cited
lean: LinearMap.charpoly_of_finrank_eq_two, LinearMap.trace_eq_and_det_eq_of_semiconj, LinearMap.finrank_ker_dualMap_eq_finrank_ker
statement: formalized
proof: formalized
---

# Similarity invariants of linear maps

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/similarity-invariants-of-linear-maps/index.html).

## Characteristic polynomial of a rank-two endomorphism

The characteristic polynomial of an endomorphism of a free rank-two
module is `X² - tr f · X + det f`, the familiar quadratic formula.

Formalized by `LinearMap.charpoly_of_finrank_eq_two`, a theorem declared in [MathlibExt/LinearAlgebra/LinearMapInvariants.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/LinearMapInvariants.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/similarity-invariants-of-linear-maps/index.html#charpoly-of-finrank-eq-two).

## Trace and determinant are invariant under semiconjugacy

Trace and determinant are preserved under semiconjugacy: if `e` intertwines
`f` and `g`, then `g` is the conjugate of `f` by `e`, so both invariants agree.

Formalized by `LinearMap.trace_eq_and_det_eq_of_semiconj`, a theorem declared in [MathlibExt/LinearAlgebra/LinearMapInvariants.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/LinearMapInvariants.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/similarity-invariants-of-linear-maps/index.html#trace-eq-and-det-eq-of-semiconj).

## Kernel of the dual map has the same dimension as the kernel

The kernel of the dual map has the same finite dimension as the kernel:
both are complementary to the range, by rank-nullity and the
dual-annihilator dimension formula.

Formalized by `LinearMap.finrank_ker_dualMap_eq_finrank_ker`, a theorem declared in [MathlibExt/LinearAlgebra/LinearMapInvariants.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/LinearMapInvariants.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/similarity-invariants-of-linear-maps/index.html#finrank-ker-dual-map-eq-finrank-ker).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Similarity invariants of linear maps](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/similarity-invariants-of-linear-maps/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/linear-maps-and-duality/similarity-invariants-of-linear-maps)
