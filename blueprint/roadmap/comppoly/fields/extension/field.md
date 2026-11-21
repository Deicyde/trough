---
catalog: module
lean: CompPoly.Extension.Ext.instNontrivial, CompPoly.Extension.Ext.four_le_card_pow, CompPoly.Extension.Ext.toQuot_surjective, CompPoly.Extension.Ext.toQuot_bijective, CompPoly.Extension.Ext.ringEquivQuot, CompPoly.Extension.Ext.ringEquivQuot_apply, CompPoly.Extension.Ext.instFintypeQuot, CompPoly.Extension.Ext.card_quot, CompPoly.Extension.Ext.inv_zero', CompPoly.Extension.Ext.mul_inv_cancel', CompPoly.Extension.Ext.instField
statement: formalized
proof: formalized
---

# The field structure on an extension

`CompPoly.Fields.Extension.Field`, in [CompPoly/Fields/Extension/Field.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean), by Derek Sorensen.

> `toQuot` is not just injective but bijective: every class in `F[X] / f` has a unique
> representative of degree `< d`. That gives `Ext.ringEquivQuot : Ext P ≃+* AdjoinRoot P.poly`,
> and the separately certified base cardinality gives `Nat.card (Ext P) = q ^ d`. A `Field`
> structure requires `[Finite F]`, `[Fact (Nat.card F = P.q)]`, and irreducibility of the defining
> polynomial.
>
> Inversion is by Fermat's little theorem, `x⁻¹ = x ^ (q^d - 2)`, matching how
> `CompPoly/Fields/Montgomery/Native32Field.lean` inverts in the base field. Exponentiation is
> binary, so this costs `O(d · log q)` extension multiplications.
>
> The instance is assembled by hand rather than via `Function.Injective.field`, for the same
> reason as `Ext.instCommRing`: that transport takes `toQuot` as data and would make the whole
> structure `noncomputable`, which then shadows the computable `Mul` and `Pow`. The `qsmul` /
> `nnqsmul` fields use the `castRec` defaults, following `mkDivisionRingInstance` in
> `CompPoly/Fields/Binary/Tower/Concrete/Core.lean`.
>
> ## Main definitions and statements
>
> * `Ext.toQuot_surjective`, `Ext.ringEquivQuot`: `Ext P ≃+* AdjoinRoot P.poly`.
> * `Ext.inv`: Fermat inversion.
> * `Ext.instField`: the `Field` structure, given finite base field, certified `Nat.card F = P.q`,
>   and irreducibility of `P.poly`.
>
> ## Implementation notes
>
> The inverse candidate is defined in `Extension/Arithmetic.lean`; its correctness depends on
> the certificates above. `Extension/Cardinality.lean` supplies the finite-coordinate facts
> without importing the polynomial quotient bridge.

`CompPoly.Extension.Ext.instNontrivial` (instance, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L53))

```lean
instance instNontrivial : Nontrivial (Ext P)
```

`CompPoly.Extension.Ext.four_le_card_pow` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L60))

> `4 ≤ q ^ d`, since `2 ≤ q` and `2 ≤ d`. Used to justify the Fermat exponent `q ^ d - 2`.

```lean
theorem four_le_card_pow [Finite F] [Fact (Nat.card F = P.q)] : 4 ≤ P.q ^ P.d
```

> ### Surjectivity and the ring equivalence

`CompPoly.Extension.Ext.toQuot_surjective` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L69))

```lean
theorem toQuot_surjective : Function.Surjective (toQuot (P := P))
```

`CompPoly.Extension.Ext.toQuot_bijective` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L89))

```lean
theorem toQuot_bijective : Function.Bijective (toQuot (P := P))
```

`CompPoly.Extension.Ext.ringEquivQuot` (definition, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L93))

> The extension is isomorphic to its specification `F[X] / f`.

```lean
noncomputable def ringEquivQuot (P : ExtensionParams F) : Ext P ≃+* Quot[P]
```

`CompPoly.Extension.Ext.ringEquivQuot_apply` (theorem, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L96))

```lean
theorem ringEquivQuot_apply (x : Ext P) : ringEquivQuot P x = toQuot x
```

`CompPoly.Extension.Ext.instFintypeQuot` (instance, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L99))

> The quotient is finite, transported along the ring equivalence.

```lean
noncomputable instance instFintypeQuot [Fintype F] : Fintype Quot[P]
```

`CompPoly.Extension.Ext.card_quot` (theorem, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L102))

```lean
theorem card_quot [Fintype F] [Fact (Nat.card F = P.q)] : Fintype.card Quot[P] = P.q ^ P.d
```

> ### Inversion
>
> The canonical inverse candidate and its `Inv`/`Div` instances come from the raw arithmetic
> module. The following laws require certified cardinality; cancellation also requires
> irreducibility.

`CompPoly.Extension.Ext.inv_zero'` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L112))

```lean
theorem inv_zero' [Finite F] [Fact (Nat.card F = P.q)] : (0 : Ext P)⁻¹ = 0
```

> ### The field structure

`CompPoly.Extension.Ext.mul_inv_cancel'` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L122))

```lean
theorem mul_inv_cancel' {x : Ext P} (hx : x ≠ 0) : x * x⁻¹ = 1
```

`CompPoly.Extension.Ext.instField` (instance, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean#L137))

> The field structure. Every operation is computable: `inv` is Fermat exponentiation, `div` is
> `x * y⁻¹`, and the rational-scalar fields use the generic `castRec` definitions.

```lean
instance instField : Field (Ext P)
```

## Depends on

- [Bridging `Ext P` to `AdjoinRoot P.poly`](bridge.md)

## Proof depends on

- [Finiteness and cardinality of monic quotient presentations](cardinality.md)

## Sources

- [CompPoly/Fields/Extension/Field.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Field.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Extension.Field.json)
