---
catalog: module
lean: BitVec.ofNat_pow, BitVec.toNat_ofFnLEAux, BitVec.toFin_ofFnLEAux, BitVec.toNat_ofFnLE, BitVec.toFin_ofFnLE, BitVec.toInt_ofFnLE, BitVec.getElem_ofFnLEAux, BitVec.getElem_ofFnLE, BitVec.getLsb_ofFnLE, BitVec.getLsbD_ofFnLE, BitVec.getMsb_ofFnLE, BitVec.getMsbD_ofFnLE, BitVec.msb_ofFnLE, BitVec.toNat_ofFnBE, BitVec.toFin_ofFnBE, BitVec.toInt_ofFnBE, BitVec.getElem_ofFnBE, BitVec.getLsb_ofFnBE, BitVec.getLsbD_ofFnBE, BitVec.getMsb_ofFnBE, BitVec.getMsbD_ofFnBE, BitVec.msb_ofFnBE
statement: formalized
proof: formalized
---

# BitVec/Lemmas

`Batteries.Data.BitVec.Lemmas`, in [Batteries/Data/BitVec/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean), by François G. Dorais.

`BitVec.ofNat_pow` (theorem, [line 17](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L17))

```lean
theorem ofNat_pow (w x n : Nat) : BitVec.ofNat w (x ^ n) = BitVec.ofNat w x ^ n
```

`BitVec.toNat_ofFnLEAux` (theorem, [line 20](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L20))

```lean
theorem toNat_ofFnLEAux (m : Nat) (f : Fin n → Bool) :
    (ofFnLEAux m f).toNat = Nat.ofBits f % 2 ^ m
```

`BitVec.toFin_ofFnLEAux` (theorem, [line 31](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L31))

```lean
theorem toFin_ofFnLEAux (m : Nat) (f : Fin n → Bool) :
    (ofFnLEAux m f).toFin = Fin.ofNat (2 ^ m) (Nat.ofBits f)
```

`BitVec.toNat_ofFnLE` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L35))

```lean
theorem toNat_ofFnLE (f : Fin n → Bool) : (ofFnLE f).toNat = Nat.ofBits f
```

`BitVec.toFin_ofFnLE` (theorem, [line 38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L38))

```lean
theorem toFin_ofFnLE (f : Fin n → Bool) : (ofFnLE f).toFin = Fin.ofBits f
```

`BitVec.toInt_ofFnLE` (theorem, [line 41](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L41))

```lean
theorem toInt_ofFnLE (f : Fin n → Bool) : (ofFnLE f).toInt = Int.ofBits f
```

`BitVec.getElem_ofFnLEAux` (theorem, [line 47](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L47))

```lean
theorem getElem_ofFnLEAux (f : Fin n → Bool) (i) (h : i < n) (h' : i < m) :
    (ofFnLEAux m f)[i] = f ⟨i, h⟩
```

`BitVec.getElem_ofFnLE` (theorem, [line 58](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L58))

```lean
theorem getElem_ofFnLE (f : Fin n → Bool) (i) (h : i < n) :
    (ofFnLE f)[i] = f ⟨i, h⟩
```

`BitVec.getLsb_ofFnLE` (theorem, [line 63](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L63))

```lean
theorem getLsb_ofFnLE (f : Fin n → Bool) (i) : (ofFnLE f).getLsb i = f i
```

`BitVec.getLsbD_ofFnLE` (theorem, [line 65](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L65))

```lean
theorem getLsbD_ofFnLE (f : Fin n → Bool) (i) :
    (ofFnLE f).getLsbD i = if h : i < n then f ⟨i, h⟩ else false
```

`BitVec.getMsb_ofFnLE` (theorem, [line 69](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L69))

```lean
theorem getMsb_ofFnLE (f : Fin n → Bool) (i) : (ofFnLE f).getMsb i = f i.rev
```

`BitVec.getMsbD_ofFnLE` (theorem, [line 73](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L73))

```lean
theorem getMsbD_ofFnLE (f : Fin n → Bool) (i) :
    (ofFnLE f).getMsbD i = if h : i < n then f (Fin.rev ⟨i, h⟩) else false
```

`BitVec.msb_ofFnLE` (theorem, [line 77](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L77))

```lean
theorem msb_ofFnLE (f : Fin n → Bool) :
    (ofFnLE f).msb = if h : n ≠ 0 then f ⟨n-1, Nat.sub_one_lt h⟩ else false
```

`BitVec.toNat_ofFnBE` (theorem, [line 81](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L81))

```lean
theorem toNat_ofFnBE (f : Fin n → Bool) :
    (ofFnBE f).toNat = Nat.ofBits (f ∘ Fin.rev)
```

`BitVec.toFin_ofFnBE` (theorem, [line 85](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L85))

```lean
theorem toFin_ofFnBE (f : Fin n → Bool) :
    (ofFnBE f).toFin = Fin.ofBits (f ∘ Fin.rev)
```

`BitVec.toInt_ofFnBE` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L89))

```lean
theorem toInt_ofFnBE (f : Fin n → Bool) :
    (ofFnBE f).toInt = Int.ofBits (f ∘ Fin.rev)
```

`BitVec.getElem_ofFnBE` (theorem, [line 93](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L93))

```lean
theorem getElem_ofFnBE (f : Fin n → Bool) (i) (h : i < n) :
    (ofFnBE f)[i] = f (Fin.rev ⟨i, h⟩)
```

`BitVec.getLsb_ofFnBE` (theorem, [line 97](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L97))

```lean
theorem getLsb_ofFnBE (f : Fin n → Bool) (i) : (ofFnBE f).getLsb i = f i.rev
```

`BitVec.getLsbD_ofFnBE` (theorem, [line 100](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L100))

```lean
theorem getLsbD_ofFnBE (f : Fin n → Bool) (i) :
    (ofFnBE f).getLsbD i = if h : i < n then f (Fin.rev ⟨i, h⟩) else false
```

`BitVec.getMsb_ofFnBE` (theorem, [line 104](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L104))

```lean
theorem getMsb_ofFnBE (f : Fin n → Bool) (i) : (ofFnBE f).getMsb i = f i
```

`BitVec.getMsbD_ofFnBE` (theorem, [line 108](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L108))

```lean
theorem getMsbD_ofFnBE (f : Fin n → Bool) (i) :
    (ofFnBE f).getMsbD i = if h : i < n then f ⟨i, h⟩ else false
```

`BitVec.msb_ofFnBE` (theorem, [line 113](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean#L113))

```lean
theorem msb_ofFnBE (f : Fin n → Bool) :
    (ofFnBE f).msb = if h : n ≠ 0 then f ⟨0, Nat.zero_lt_of_ne_zero h⟩ else false
```

## Depends on

- [BitVec/Basic](basic.md)
- [OfBits](../fin/ofbits.md)
- [Int](../int.md)

## Proof depends on

- [WF](../binaryheap/wf.md)

## Sources

- [Batteries/Data/BitVec/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/BitVec/Lemmas.lean)
