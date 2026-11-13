---
declaration: section
origin: cited
lean: Algebra.ker_trace_eq_range_algEquiv_sub_id, Algebra.exists_algEquiv_sub_eq_of_trace_eq_zero
statement: formalized
proof: formalized
---

# Additive Hilbert's theorem 90

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/additive-hilbert-s-theorem-90/index.html).

## Additive Hilbert 90 for cyclic extensions

Let $L/K$ be a finite-dimensional Galois
extension and let $\sigma$ be a $K$-algebra automorphism of $L$ that generates its Galois group,
that is, every $K$-algebra automorphism of $L$ is an integer power of $\sigma$. Then the kernel
of the trace $\operatorname{Tr}_{L/K} \colon L \to K$ equals the image of the $K$-linear map
$\sigma - 1 \colon L \to L$, $y \mapsto \sigma(y) - y$.

Formalized by `Algebra.ker_trace_eq_range_algEquiv_sub_id`, a theorem declared in [MathlibExt/FieldTheory/Galois/AdditiveHilbert90.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/AdditiveHilbert90.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/additive-hilbert-s-theorem-90/index.html#ker-trace-eq-range-alg-equiv-sub-id).

## Additive Hilbert 90, pointwise form

Let $L/K$ be a finite-dimensional Galois extension
and let $\sigma$ be a $K$-algebra automorphism of $L$ that generates its Galois group, that is,
every $K$-algebra automorphism of $L$ is an integer power of $\sigma$. If $x \in L$ satisfies
$\operatorname{Tr}_{L/K}(x) = 0$, then there is $y \in L$ with $\sigma(y) - y = x$.

Formalized by `Algebra.exists_algEquiv_sub_eq_of_trace_eq_zero`, a theorem declared in [MathlibExt/FieldTheory/Galois/AdditiveHilbert90.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Galois/AdditiveHilbert90.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/additive-hilbert-s-theorem-90/index.html#exists-alg-equiv-sub-eq-of-trace-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Additive Hilbert's theorem 90](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/additive-hilbert-s-theorem-90/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/FieldTheory/galois-theory/additive-hilbert-s-theorem-90)
