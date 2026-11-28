---
catalog: module
lean: CompPoly.CMlPolynomial.width, CompPoly.CMlPolynomialEval.width, CompPoly.CMlPolynomial.toBytes_eq
statement: formalized
proof: formalized
---

# Serialization of multilinear polynomials

`CompPoly.Multilinear.Bytes`, in [CompPoly/Multilinear/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Bytes.lean), by Derek Sorensen.

> `CMlPolynomial R n` and `CMlPolynomialEval R n` are `Vector R (2 ^ n)`, so they serialize
> through the vector codec with no further definitions: `2 ^ n` coefficients, or `2 ^ n`
> hypercube evaluations, in little-endian index order, `2 ^ n * width R` bytes. The two
> representations have the same bytes for different meanings; the type says which.

`CompPoly.CMlPolynomial.width` (theorem, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Bytes.lean#L26))

```lean
theorem CMlPolynomial.width [ByteCodec R] :
    ByteCodec.width (CMlPolynomial R n) = 2 ^ n * ByteCodec.width R
```

`CompPoly.CMlPolynomialEval.width` (theorem, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Bytes.lean#L29))

```lean
theorem CMlPolynomialEval.width [ByteCodec R] :
    ByteCodec.width (CMlPolynomialEval R n) = 2 ^ n * ByteCodec.width R
```

`CompPoly.CMlPolynomial.toBytes_eq` (theorem, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Bytes.lean#L32))

```lean
theorem CMlPolynomial.toBytes_eq [ByteCodec R] (p : CMlPolynomial R n) :
    ByteCodec.toBytes p = ByteCodec.toBytes (p : Vector R (2 ^ n))
```

## Depends on

- [Byte codecs of vectors](../data/bytes/vector.md)
- [Multilinear Polynomials](basic.md)

## Sources

- [CompPoly/Multilinear/Bytes.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Bytes.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multilinear.Bytes.json)
