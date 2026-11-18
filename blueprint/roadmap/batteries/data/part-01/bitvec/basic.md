---
catalog: module
lean: BitVec.ofFnLEAux, BitVec.ofFnLE, BitVec.ofFnBE
statement: formalized
proof: formalized
---

# BitVec/Basic

`Batteries.Data.BitVec.Basic`, in [Batteries/Data/BitVec/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Basic.lean), by François G. Dorais.

`BitVec.ofFnLEAux` (definition, [line 13](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Basic.lean#L13))

> `ofFnLEAux f` returns the `BitVec m` whose `i`th bit is `f i` when `i < m`, little endian.

```lean
def ofFnLEAux (m : Nat) (f : Fin n → Bool) : BitVec m
```

`BitVec.ofFnLE` (definition, [line 17](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Basic.lean#L17))

> `ofFnLE f` returns the `BitVec n` whose `i`th bit is `f i` with little endian ordering.

```lean
def ofFnLE (f : Fin n → Bool) : BitVec n
```

`BitVec.ofFnBE` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Basic.lean#L20))

> `ofFnBE f` returns the `BitVec n` whose `i`th bit is `f i` with big endian ordering.

```lean
def ofFnBE (f : Fin n → Bool) : BitVec n
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/BitVec/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Basic.lean)
