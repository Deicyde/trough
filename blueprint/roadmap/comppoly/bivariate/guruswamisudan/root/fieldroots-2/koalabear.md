---
catalog: module
lean: CompPoly.GuruswamiSudan.koalaBearFiniteFieldContext, CompPoly.GuruswamiSudan.koalaBearSmoothCyclicRootContext, CompPoly.GuruswamiSudan.koalaBearFieldRootContext, CompPoly.GuruswamiSudan.koalaBearNttFieldRootContext, CompPoly.GuruswamiSudan.koalaBearNttFastFieldRootContext, CompPoly.GuruswamiSudan.fastKoalaBearFiniteFieldContext, CompPoly.GuruswamiSudan.fastKoalaBearPrimitiveRoot, CompPoly.GuruswamiSudan.fastKoalaBearPrimitiveRoot_order, CompPoly.GuruswamiSudan.fastKoalaBearSmoothCyclicRootContext, CompPoly.GuruswamiSudan.fastKoalaBearFieldRootContext, CompPoly.GuruswamiSudan.fastKoalaBearNttFieldRootContext, CompPoly.GuruswamiSudan.fastKoalaBearNttFastFieldRootContext
statement: formalized
proof: formalized
---

# KoalaBear Guruswami-Sudan Field-Root Backends

`CompPoly.Bivariate.GuruswamiSudan.Root.FieldRoots.KoalaBear`, in [CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean), by Valerii Huhnin.

> Concrete finite-field root backends for canonical KoalaBear and native-word fast
> KoalaBear. Both use the generic finite-field algorithm directly over their field
> carriers.

`CompPoly.GuruswamiSudan.koalaBearFiniteFieldContext` (definition, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L28))

> Finite-field context for canonical KoalaBear.

```lean
def koalaBearFiniteFieldContext :
    CPolynomial.Roots.FiniteField.FiniteFieldContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearSmoothCyclicRootContext` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L39))

> Smooth cyclic splitter context for canonical KoalaBear.

```lean
def koalaBearSmoothCyclicRootContext :
    CPolynomial.Roots.FiniteField.SmoothCyclicRootContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearFieldRootContext` (definition, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L86))

> Complete GS-facing finite-field root backend for canonical KoalaBear.

```lean
def koalaBearFieldRootContext : FieldRootContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearNttFieldRootContext` (definition, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L95))

> Complete GS-facing finite-field root backend for canonical KoalaBear with NTT arithmetic.

```lean
def koalaBearNttFieldRootContext : FieldRootContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.koalaBearNttFastFieldRootContext` (definition, [line 108](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L108))

> Complete GS-facing finite-field root backend for canonical KoalaBear with NTTFast arithmetic.

```lean
def koalaBearNttFastFieldRootContext : FieldRootContext KoalaBear.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearFiniteFieldContext` (definition, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L121))

> Finite-field context for native-word fast KoalaBear.

```lean
def fastKoalaBearFiniteFieldContext :
    CPolynomial.Roots.FiniteField.FiniteFieldContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearPrimitiveRoot` (definition, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L138))

> Primitive generator transported to native-word fast KoalaBear.

```lean
def fastKoalaBearPrimitiveRoot : KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearPrimitiveRoot_order` (lemma, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L142))

> The transported fast KoalaBear generator has full multiplicative order.

```lean
lemma fastKoalaBearPrimitiveRoot_order :
    orderOf fastKoalaBearPrimitiveRoot = KoalaBear.fieldSize - 1
```

`CompPoly.GuruswamiSudan.fastKoalaBearSmoothCyclicRootContext` (definition, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L152))

> Smooth cyclic splitter context for native-word fast KoalaBear.

```lean
def fastKoalaBearSmoothCyclicRootContext :
    CPolynomial.Roots.FiniteField.SmoothCyclicRootContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearFieldRootContext` (definition, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L208))

> Complete GS-facing finite-field root backend for native-word fast KoalaBear.

```lean
def fastKoalaBearFieldRootContext : FieldRootContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearNttFieldRootContext` (definition, [line 220](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L220))

> Complete GS-facing finite-field root backend for native-word fast KoalaBear with
> NTT arithmetic.

```lean
def fastKoalaBearNttFieldRootContext : FieldRootContext KoalaBear.Fast.Field
```

`CompPoly.GuruswamiSudan.fastKoalaBearNttFastFieldRootContext` (definition, [line 236](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean#L236))

> Complete GS-facing finite-field root backend for native-word fast KoalaBear with
> NTTFast arithmetic.

```lean
def fastKoalaBearNttFastFieldRootContext : FieldRootContext KoalaBear.Fast.Field
```

## Depends on

- [Guruswami-Sudan Finite-Field Root Adapter](finitefield.md)
- [KoalaBear NTT Domains](../../../../univariate/part-01/ntt/koalabear.md)

## Proof depends on

- [Smooth Multiplicative-Subgroup Splitter Correctness](../../../../univariate/part-02/roots/smoothsubgroup/correctness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/FieldRoots/KoalaBear.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.FieldRoots.KoalaBear.json)
