---
declaration: module
origin: cited
lean: Projection.compress, Projection.compress_apply, Projection.compress_zero, Projection.zero_compress_apply, Projection.zero_compress, Projection.compress_add, IsIdempotentElem.mul_compress, IsIdempotentElem.compress_mul
statement: formalized
proof: formalized
---

# Compression by a projection

The module `Physlib.Mathematics.Projection.Compress`, [Physlib/Mathematics/Projection/Compress.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean): 13 declarations, 8 with a docstring.

## i. Overview

> The compression of `a` by `p` is the product `p * a * p`. If `p` is idempotent, then
> compression by `p` is an idempotent map. If `p` is self-adjoint, compression commutes
> with the star operation. A star projection has both properties.

## ii. Key results

> - `Projection.compress` defines compression using only multiplication.
> - `IsIdempotentElem.compress_comp_compress` gives idempotence of the compression map.
> - `IsSelfAdjoint.star_compress` relates compression and the star operation.

## iv. References

> * None.

## A. Compression

**`Projection.compress`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L47).

> The compression of `a` by an idempotent element `p`, given by `p * a * p`.

```lean
def compress [Mul A] (p a : A) : A
```

**`Projection.compress_apply`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L49).

```lean
lemma compress_apply [Mul A] (p a : A) : compress p a = p * a * p
```

**`Projection.compress_zero`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L51).

```lean
lemma compress_zero [MulZeroClass A] (p : A) : compress p 0 = 0
```

**`Projection.zero_compress_apply`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L54).

```lean
lemma zero_compress_apply [MulZeroClass A] (a : A) : compress 0 a = 0
```

**`Projection.zero_compress`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L57).

```lean
lemma zero_compress [MulZeroClass A] : compress (0 : A) = 0
```

**`Projection.compress_add`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L60).

```lean
lemma compress_add [Distrib A] (p a b : A) :
    compress p (a + b) = compress p a + compress p b
```

## B. Compression by an idempotent

**`IsIdempotentElem.mul_compress`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L79).

> Multiplying a compression by its idempotent on the left leaves it unchanged.

```lean
lemma mul_compress (a : A) : p * compress p a = compress p a
```

**`IsIdempotentElem.compress_mul`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L83).

> Multiplying a compression by its idempotent on the right leaves it unchanged.

```lean
lemma compress_mul (a : A) : compress p a * p = compress p a
```

**`IsIdempotentElem.compress_compress`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L87).

> Compression by the same idempotent twice gives the original compression.

```lean
lemma compress_compress (a : A) : compress p (compress p a) = compress p a
```

**`IsIdempotentElem.compress_comp_compress`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L91).

> Compression by an idempotent is idempotent under function composition.

```lean
lemma compress_comp_compress : compress p ∘ compress p = compress p
```

**`IsIdempotentElem.compress_mul_compress`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L95).

> The product of two compressions is a compression with an intermediate idempotent.

```lean
lemma compress_mul_compress (a b : A) : compress p a * compress p b = compress p (a * p * b)
```

## C. Compression by a self-adjoint element

**`IsSelfAdjoint.star_compress`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L111).

> Compression by a self-adjoint element commutes with taking the star.

```lean
lemma star_compress (a : A) : star (compress p a) = compress p (star a)
```

**`IsSelfAdjoint.isSelfAdjoint_compress`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean#L115).

> Compression by a self-adjoint element preserves self-adjointness.

```lean
lemma isSelfAdjoint_compress {a : A} (ha : IsSelfAdjoint a) : IsSelfAdjoint (compress p a)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Projection/Compress.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/Projection/Compress.lean)
