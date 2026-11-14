---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.PrimitiveBinaryComponent.exists_mul_eq, MIPRE.LowDegree.splitAllComponents_primitive, MIPRE.LowDegree.ComponentFamily.length_le_finrank, MIPRE.LowDegree.BinaryLinear.groupFixedGeneratorsProg_correct, MIPRE.LowDegree.BinaryLinear.groupComponents_primitive, MIPRE.LowDegree.BinaryLinear.groupComponents_length_le, MIPRE.LowDegree.BinaryLinear.groupComponentsProg, MIPRE.LowDegree.BinaryLinear.groupComponentsProg_correct, MIPRE.SAT.shoupFrobeniusAction_injective, MIPRE.SAT.shoupProjectedVector_ne_zero, MIPRE.SAT.shoupNormalElement_projection, MIPRE.SAT.shoupNormalOrbitMap_injective, MIPRE.SAT.shoupNormalBasis_normal, MIPRE.SAT.shoupOrbitProg_correct, MIPRE.SAT.shoupActionProg_correct, MIPRE.SAT.shoupNormalElementProg_correct, MIPRE.SAT.shoupNormalBasisProg, MIPRE.SAT.shoupNormalBasisProg_correct
statement: formalized
proof: formalized
---

# Effective normal element by fixed-space projections

For odd $k>0$, a deterministic ambient program, with unary degree as its only input, outputs the polynomial-basis encodings of a normal basis of the Shoup field. Its runtime is polynomial in $k$.

## Depends on

- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)
- [Self-dual and normal bases](../part-04/def-self-dual-basis.md)
- [Effective indexing and padding arithmetic](../../structure-of-the-proof/part-07/lem-pcp-padding-programs.md)

## Proof depends on

- [Self-dualization in the group algebra](../part-04/lem-group-algebra-selfdualization.md)

## Proof

In $\mathbb{F}_2[C_k]$, compute generators of the fixed space of squaring by binary elimination. Starting from $1$, split each component by a fixed generator $b$ into $eb$ and $e(1-b)$, omitting zeros. The remaining components are nonzero orthogonal idempotents summing to $1$, so there are at most $k$. Spanning the fixed space makes them primitive. Odd $k$ makes squaring bijective, and every nonzero element supported on a primitive component has an inverse there.

Let the cyclic algebra act on the quotient field by Frobenius. Independence of distinct field automorphisms makes this action faithful. For each component, scan the polynomial basis and select its first nonzero projected vector. Their sum has trivial annihilator: applying a component and its inverse would otherwise kill its selected nonzero vector. Its Frobenius orbit is therefore a basis. All scans, kernel computations, cyclic products and orbit computations are implemented by polynomial-time programs. A dimension cap bounds component lists also on malformed inputs and is proved inert on valid component families.

## Lean

Formalized as [`MIPRE.LowDegree.PrimitiveBinaryComponent.exists_mul_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.PrimitiveBinaryComponent.exists_mul_eq), [`MIPRE.LowDegree.splitAllComponents_primitive`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.splitAllComponents_primitive), [`MIPRE.LowDegree.ComponentFamily.length_le_finrank`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.ComponentFamily.length_le_finrank), [`MIPRE.LowDegree.BinaryLinear.groupFixedGeneratorsProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.groupFixedGeneratorsProg_correct), [`MIPRE.LowDegree.BinaryLinear.groupComponents_primitive`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.groupComponents_primitive), [`MIPRE.LowDegree.BinaryLinear.groupComponents_length_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.groupComponents_length_le), [`MIPRE.LowDegree.BinaryLinear.groupComponentsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.groupComponentsProg), [`MIPRE.LowDegree.BinaryLinear.groupComponentsProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.groupComponentsProg_correct), [`MIPRE.SAT.shoupFrobeniusAction_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupFrobeniusAction_injective), [`MIPRE.SAT.shoupProjectedVector_ne_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupProjectedVector_ne_zero), [`MIPRE.SAT.shoupNormalElement_projection`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupNormalElement_projection), [`MIPRE.SAT.shoupNormalOrbitMap_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupNormalOrbitMap_injective), [`MIPRE.SAT.shoupNormalBasis_normal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupNormalBasis_normal), [`MIPRE.SAT.shoupOrbitProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupOrbitProg_correct), [`MIPRE.SAT.shoupActionProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupActionProg_correct), [`MIPRE.SAT.shoupNormalElementProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupNormalElementProg_correct), [`MIPRE.SAT.shoupNormalBasisProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupNormalBasisProg), [`MIPRE.SAT.shoupNormalBasisProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupNormalBasisProg_correct).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 7109](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L7109)
