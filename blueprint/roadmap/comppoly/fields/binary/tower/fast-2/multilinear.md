---
catalog: module
lean: ConcreteBinaryTower.Fast.FastBT128.toConcrete_accumulateProducts, ConcreteBinaryTower.Fast.FastBT128.toConcrete_evalWithProducts
statement: formalized
proof: formalized
---

# Packed binary-tower product accumulation

`CompPoly.Fields.Binary.Tower.Fast.Multilinear`, in [CompPoly/Fields/Binary/Tower/Fast/Multilinear.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Fast/Multilinear.lean), by CompPoly Contributors.

> The eager `FastBT128` backend uses its ordinary field multiplication and addition, with
> identity reduction. Its existing ring equivalence transports arbitrary product accumulations
> and coefficient-form multilinear evaluations to the concrete tower. No unreduced product
> representation or delayed-reduction algorithm is introduced.

`ConcreteBinaryTower.Fast.FastBT128.toConcrete_accumulateProducts` (theorem, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Fast/Multilinear.lean#L28))

> Converting an eager product accumulation to the concrete tower preserves its initial
> accumulator and the dot product of its two vectors.

```lean
theorem toConcrete_accumulateProducts {n : ℕ} (init : FastBT128)
    (a b : Vector FastBT128 n) :
    toConcrete (Vector.accumulateProducts (· * ·) init a b) =
      toConcrete init + Vector.dotProduct (a.map toConcrete) (b.map toConcrete)
```

`ConcreteBinaryTower.Fast.FastBT128.toConcrete_evalWithProducts` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Fast/Multilinear.lean#L37))

> Eager packed coefficient evaluation, followed by conversion to the concrete tower,
> agrees with evaluating the converted coefficients at the converted point.

```lean
theorem toConcrete_evalWithProducts {n : ℕ} (p : CMlPolynomial FastBT128 n)
    (x : Vector FastBT128 n) :
    toConcrete (CMlPolynomial.evalWithProducts (· * ·) (AddMonoidHom.id FastBT128) p x) =
      CMlPolynomial.eval (CMlPolynomial.map ringEquiv.toRingHom p) (x.map toConcrete)
```

## Depends on

- [Fast Binary Tower Arithmetic](../fast.md)
- [Multilinear Polynomials](../../../../multilinear/basic.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Fast/Multilinear.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Fast/Multilinear.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Fast.Multilinear.json)
