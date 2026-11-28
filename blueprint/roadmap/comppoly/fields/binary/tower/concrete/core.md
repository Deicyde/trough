---
catalog: module
lean: ConcreteBinaryTower.toConcreteBTF0, ConcreteBinaryTower.fromConcreteBTF0, ConcreteBinaryTower.coeffsToBitVec, ConcreteBinaryTower.ConcreteBTFAddCommGroupProps, ConcreteBinaryTower.ConcreteBTFRingProps, ConcreteBinaryTower.ConcreteBTFDivisionRingProps, ConcreteBinaryTower.ConcreteBTFieldProps, ConcreteBinaryTower.mkRingInstance, ConcreteBinaryTower.mkDivisionRingInstance, ConcreteBinaryTower.mkFieldInstance, ConcreteBinaryTower.ConcreteBTFStepResult
statement: formalized
proof: formalized
---

# Concrete binary tower field construction interface

`CompPoly.Fields.Binary.Tower.Concrete.Core`, in [CompPoly/Fields/Binary/Tower/Concrete/Core.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean), by Chung Thai Nguyen, Quang Dao.

> Compatibility entry point for the executable arithmetic, together with the law records,
> finite-field utilities, and field-instance assembly used by the recursive construction.
> Arithmetic-only clients can import `CompPoly.Fields.Binary.Tower.Concrete.Arithmetic`;
> canonical field clients use `CompPoly.Fields.Binary.Tower.Concrete.Field`.

`ConcreteBinaryTower.toConcreteBTF0` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L44))

```lean
noncomputable def toConcreteBTF0 : GF(2) → ConcreteBTField 0
```

`ConcreteBinaryTower.fromConcreteBTF0` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L47))

```lean
noncomputable def fromConcreteBTF0 : ConcreteBTField 0 → (GF(2))
```

`ConcreteBinaryTower.coeffsToBitVec` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L51))

```lean
def coeffsToBitVec {n : ℕ} (coeffs : List (ZMod 2)) : BitVec n
```

`ConcreteBinaryTower.ConcreteBTFAddCommGroupProps` (structure, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L56))

```lean
structure ConcreteBTFAddCommGroupProps (k : ℕ) where
  add_assoc : ∀ a b c : ConcreteBTField k, (a + b) + c = a + (b + c) := add_assoc
  add_comm : ∀ a b : ConcreteBTField k, a + b = b + a := add_comm
  add_zero : ∀ a : ConcreteBTField k, a + zero = a := add_zero
  zero_add : ∀ a : ConcreteBTField k, zero + a = a := zero_add
  add_neg : ∀ a : ConcreteBTField k, a + (neg a) = zero := neg_add_cancel
```

`ConcreteBinaryTower.ConcreteBTFRingProps` (structure, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L64))

```lean
structure ConcreteBTFRingProps (k : ℕ) extends (ConcreteBTFAddCommGroupProps k) where
  -- Multiplication equations and basic properties
  mul_eq : ∀ (a b : ConcreteBTField k) (h_k : k > 0)
    {a₁ a₀ b₁ b₀ : ConcreteBTField (k - 1)}
    (_h_a : (a₁, a₀) = split h_k a) (_h_b : (b₁, b₀) = split h_k b),
    concrete_mul a b =
      《 concrete_mul a₀ b₁ + concrete_mul b₀ a₁ + concrete_mul (concrete_mul a₁ b₁) (Z (k - 1)),
      concrete_mul a₀ b₀ + concrete_mul a₁ b₁ 》

  -- Zero and one laws
  zero_mul : ∀ a : ConcreteBTField k, concrete_mul zero a = zero
  zero_mul' : ∀ a : ConcreteBTField k, concrete_mul 0 a = 0
  mul_zero : ∀ a : ConcreteBTField k, concrete_mul a zero = zero
  mul_zero' : ∀ a : ConcreteBTField k, concrete_mul a 0 = 0
  one_mul : ∀ a : ConcreteBTField k, concrete_mul one a = a
  mul_one : ∀ a : ConcreteBTField k, concrete_mul a one = a

  -- Associativity and distributivity (Ring axioms)
  mul_assoc : ∀ a b c : ConcreteBTField k, concrete_mul (concrete_mul a b) c
    = concrete_mul a (concrete_mul b c)
  mul_left_distrib : ∀ a b c : ConcreteBTField k, concrete_mul a (b + c)
    = concrete_mul a b + concrete_mul a c
  mul_right_distrib : ∀ a b c : ConcreteBTField k, concrete_mul (a + b) c
    = concrete_mul a c + concrete_mul b c
```

`ConcreteBinaryTower.ConcreteBTFDivisionRingProps` (structure, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L90))

```lean
structure ConcreteBTFDivisionRingProps (k : ℕ) extends (ConcreteBTFRingProps k) where
  -- Multiplicative inverse property
  mul_inv_cancel : ∀ a : ConcreteBTField k, a ≠ zero → concrete_mul a (concrete_inv a) = one
```

`ConcreteBinaryTower.ConcreteBTFieldProps` (structure, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L95))

```lean
structure ConcreteBTFieldProps (k : ℕ) extends (ConcreteBTFDivisionRingProps k) where
  -- Commutativity (what makes it a Field vs just a DivisionRing)
  mul_comm : ∀ a b : ConcreteBTField k, concrete_mul a b = concrete_mul b a
```

`ConcreteBinaryTower.mkRingInstance` (definition, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L99))

```lean
def mkRingInstance {k : ℕ} (props : ConcreteBTFieldProps k) :
    Ring (ConcreteBTField k)
```

`ConcreteBinaryTower.mkDivisionRingInstance` (definition, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L124))

```lean
def mkDivisionRingInstance {k : ℕ} (props : ConcreteBTFieldProps k) :
    DivisionRing (ConcreteBTField k)
```

`ConcreteBinaryTower.mkFieldInstance` (definition, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L140))

```lean
def mkFieldInstance {k : ℕ} (props : ConcreteBTFieldProps k) :
    Field (ConcreteBTField k)
```

`ConcreteBinaryTower.ConcreteBTFStepResult` (structure, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean#L145))

```lean
structure ConcreteBTFStepResult (k : ℕ) extends (ConcreteBTFieldProps k) where
  instFintype : Fintype (ConcreteBTField k)
  fieldFintypeCard : Fintype.card (ConcreteBTField k) = 2^(2^k)
  -- Additional field theory properties for irreducibility proof
  sumZeroIffEq : ∀ (x y : ConcreteBTField k), x + y = 0 ↔ x = y
  traceMapEvalAtRootsIs1 :
    letI := mkFieldInstance (k:=k) (props:=toConcreteBTFieldProps)
    TraceMapProperty (ConcreteBTField k) (u:=Z k) k
  instIrreduciblePoly :
    letI := mkFieldInstance (k:=k) (props:=toConcreteBTFieldProps)
    (Irreducible (p := (definingPoly (s:=(Z k)))))
```

## Depends on

- [Concrete binary tower arithmetic](arithmetic.md)
- [Binary Tower Defining Polynomials](../support/definingpoly.md)
- [Binary Tower Preliminaries](../support/preliminaries.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Concrete/Core.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Core.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Concrete.Core.json)
