---
catalog: module
lean: Serialize, Serialize.IsInjective, Deserialize, DeserializeOption, Serde
statement: formalized
proof: formalized
---

# Serialization and deserialization classes

`CompPoly.Data.Classes.Serialize`, in [CompPoly/Data/Classes/Serialize.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/Serialize.lean), by Quang Dao.

> Simple type classes for serializing a type into another type, most often `ByteArray` or a
> fixed-length `Vector` of units, and for deserializing back, with or without failure.
>
> These declarations are ported verbatim from ArkLib (`ArkLib/Data/Classes/Serde.lean`) so that
> CompPoly can supply instances for its field and polynomial types directly. The
> statistical-closeness class `Deserialize.CloseToUniform` stays in ArkLib, where the probability
> theory it needs already lives; CompPoly proves the counting facts behind it in `Nat` terms.

`Serialize` (class, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/Serialize.lean#L28))

> Type class for types that can be serialized to another type (most often `ByteArray` or
> `String`).

```lean
class Serialize (α : Type u) (β : Type v) where
  serialize : α → β
```

`Serialize.IsInjective` (class, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/Serialize.lean#L34))

> Type class for injective serialization.

```lean
class Serialize.IsInjective (α : Type u) (β : Type v) [inst : Serialize α β] : Prop where
  serialize_inj : Function.Injective inst.serialize
```

`Deserialize` (class, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/Serialize.lean#L39))

> Type class for types that can be deserialized from another type (most often `ByteArray` or
> `String`), which _never_ fails.

```lean
class Deserialize (α : Type u) (β : Type v) where
  deserialize : β → α
```

`DeserializeOption` (class, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/Serialize.lean#L44))

> Type class for types that can be deserialized from another type (most often `ByteArray` or
> `String`), returning an `Option` if the deserialization fails.

```lean
class DeserializeOption (α : Type u) (β : Type v) where
  deserialize : β → Option α
```

`Serde` (class, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/Serialize.lean#L49))

> Type class for types that can be serialized and deserialized (with potential failure) to/from
> another type (most often `ByteArray` or `String`).

```lean
class Serde (α : Type u) (β : Type v) extends Serialize α β, DeserializeOption α β
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/Classes/Serialize.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Classes/Serialize.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Classes.Serialize.json)
