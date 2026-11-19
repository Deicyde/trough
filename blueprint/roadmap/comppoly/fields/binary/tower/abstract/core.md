---
catalog: module
lean: BinaryTower.BinaryTowerResult, BinaryTower.BinaryTowerInductiveStepResult, BinaryTower.binary_tower_inductive_step, BinaryTower.BinaryTowerAux, BinaryTower.BTField, BinaryTower.BTField_is_BTFieldAux, BinaryTower.BTFieldIsField, BinaryTower.CommRing, BinaryTower.Nontrivial, BinaryTower.Inhabited, BinaryTower.BTFieldNeZero1, BinaryTower.BTField_Fintype, BinaryTower.BTFieldCard, BinaryTower.BTFieldIsDomain, BinaryTower.BTFieldNoZeroDiv, BinaryTower.sumZeroIffEq, BinaryTower.BTFieldChar2, BinaryTower.BTField_0_is_GF_2, BinaryTower.list, BinaryTower.Z, BinaryTower.poly, BinaryTower.poly_natDegree_eq_2, BinaryTower.BTField.cast_BTField_eq, BinaryTower.BTField.cast_mul, BinaryTower.𝕏, BinaryTower.BTField_succ_eq_adjoinRoot, BinaryTower.coe_field_adjoinRoot, BinaryTower.Z_succ_eq_adjointRoot_root, BinaryTower.list_0, BinaryTower.list_eq, BinaryTower.eval_poly_at_root, BinaryTower.poly_form, BinaryTower.eval_mapped_poly_at_root, BinaryTower.list_length, BinaryTower.list_nonempty, BinaryTower.polyIrreducible, BinaryTower.polyIrreducibleFact, BinaryTower.polyMonic, BinaryTower.poly_ne_zero
statement: formalized
proof: formalized
---

# Abstract Binary Tower Core

`CompPoly.Fields.Binary.Tower.Abstract.Core`, in [CompPoly/Fields/Binary/Tower/Abstract/Core.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean), by Quang Dao, Chung Thai Nguyen.

> Core definitions and existence data for the abstract binary tower construction.

`BinaryTower.BinaryTowerResult` (structure, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L30))

```lean
structure BinaryTowerResult (F : Type _) (k : ℕ) where
  vec : (List.Vector F (k + 1))
  instField : (Field F)
  instFintype : Fintype F
  specialElement : F
  specialElementNeZero : NeZero specialElement
  firstElementOfVecIsSpecialElement [Inhabited F] : vec.1.headI = specialElement
  instIrreduciblePoly : (Irreducible (p := (definingPoly specialElement)))
  sumZeroIffEq : ∀ (x y : F), x + y = 0 ↔ x = y
  fieldFintypeCard : Fintype.card F = 2^(2^k)
  traceMapEvalAtRootsIs1 : TraceMapProperty F specialElement k
```

`BinaryTower.BinaryTowerInductiveStepResult` (structure, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L42))

```lean
structure BinaryTowerInductiveStepResult (k : ℕ) (prevBTField : Type _)
  (prevBTResult : BinaryTowerResult prevBTField k) [instPrevBTFieldIsField : Field prevBTField]
  (prevPoly : Polynomial prevBTField) (F : Type _) where
  binaryTowerResult : BinaryTowerResult F (k+1)
  eq_adjoin : F = AdjoinRoot prevPoly
  u_is_root : Eq.mp (eq_adjoin) binaryTowerResult.specialElement = AdjoinRoot.root prevPoly
  eval_defining_poly_at_root : Eq.mp (eq_adjoin) binaryTowerResult.specialElement^2 +
    Eq.mp (eq_adjoin) binaryTowerResult.specialElement * (of prevPoly) prevBTResult.specialElement
    + 1 = 0
```

`BinaryTower.binary_tower_inductive_step` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L54))

```lean
def binary_tower_inductive_step
    (k : Nat)
  (prevBTField : Type _) [Field prevBTField]
  (prevBTResult : BinaryTowerResult prevBTField k) :
  Σ' (F : Type _), BinaryTowerInductiveStepResult (k:=k) (prevBTField:=prevBTField)
  (prevBTResult:=prevBTResult) (prevPoly:=definingPoly (F:=prevBTField)
    (instField:=prevBTResult.instField) (s:=prevBTResult.specialElement)) (F:=F)
  (instPrevBTFieldIsField:=prevBTResult.instField)
```

`BinaryTower.BinaryTowerAux` (definition, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L241))

```lean
def BinaryTowerAux (k : ℕ) : (Σ' (F : Type 0), BinaryTowerResult F k)
```

`BinaryTower.BTField` (definition, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L382))

```lean
def BTField (k : ℕ)
```

`BinaryTower.BTField_is_BTFieldAux` (lemma, [line 384](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L384))

```lean
lemma BTField_is_BTFieldAux (k : ℕ) :
    BTField k = (BinaryTowerAux k).1
```

`BinaryTower.BTFieldIsField` (instance, [line 389](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L389))

```lean
instance BTFieldIsField (k : ℕ) : Field (BTField k)
```

`BinaryTower.CommRing` (instance, [line 391](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L391))

```lean
instance CommRing (k : ℕ) : CommRing (BTField k)
```

`BinaryTower.Nontrivial` (instance, [line 393](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L393))

```lean
instance Nontrivial (k : ℕ) : Nontrivial (BTField k)
```

`BinaryTower.Inhabited` (instance, [line 395](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L395))

```lean
instance Inhabited (k : ℕ) : Inhabited (BTField k)
```

`BinaryTower.BTFieldNeZero1` (instance, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L402))

```lean
instance BTFieldNeZero1 (k : ℕ) : NeZero (1 : BTField k)
```

`BinaryTower.BTField_Fintype` (instance, [line 406](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L406))

```lean
instance BTField_Fintype (k : ℕ) : Fintype (BTField k)
```

`BinaryTower.BTFieldCard` (theorem, [line 409](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L409))

```lean
theorem BTFieldCard (k : ℕ) : Fintype.card (BTField k) = 2^(2^k)
```

`BinaryTower.BTFieldIsDomain` (instance, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L412))

```lean
instance BTFieldIsDomain (k : ℕ) : IsDomain (BTField k)
```

`BinaryTower.BTFieldNoZeroDiv` (instance, [line 414](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L414))

```lean
instance BTFieldNoZeroDiv (k : ℕ) : NoZeroDivisors (BTField k)
```

`BinaryTower.sumZeroIffEq` (theorem, [line 419](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L419))

```lean
theorem sumZeroIffEq (k : ℕ) : ∀ (x y : BTField k),
    x + y = 0 ↔ x = y
```

`BinaryTower.BTFieldChar2` (instance, [line 422](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L422))

```lean
instance BTFieldChar2 (k : ℕ) : CharP (BTField k) 2
```

`BinaryTower.BTField_0_is_GF_2` (theorem, [line 426](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L426))

```lean
theorem BTField_0_is_GF_2 : (BTField 0) = (GF(2))
```

`BinaryTower.list` (definition, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L431))

```lean
def list (k : ℕ) : List.Vector (BTField k) (k + 1)
```

`BinaryTower.Z` (definition, [line 435](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L435))

> Z k is the generator of BTField k

```lean
def Z (k : ℕ) : BTField k
```

`BinaryTower.poly` (definition, [line 440](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L440))

```lean
def poly (k : ℕ) : Polynomial (BTField k)
```

`BinaryTower.poly_natDegree_eq_2` (lemma, [line 442](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L442))

```lean
lemma poly_natDegree_eq_2 (k : ℕ) : (poly (k:=k)).natDegree = 2
```

`BinaryTower.BTField.cast_BTField_eq` (lemma, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L445))

```lean
lemma BTField.cast_BTField_eq (k m : ℕ) (h_eq : k = m) :
    BTField k = BTField m
```

`BinaryTower.BTField.cast_mul` (lemma, [line 450](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L450))

```lean
lemma BTField.cast_mul (m n : ℕ) {x y : BTField m} (h_eq : m = n) :
    (cast (BTField.cast_BTField_eq m n h_eq) (x * y)) =
  (cast (BTField.cast_BTField_eq m n h_eq) x) *
  (cast (BTField.cast_BTField_eq m n h_eq) y)
```

`BinaryTower.𝕏` (definition, [line 459](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L459))

> adjoined root of poly k, generator of successor field BTField (k+1)

```lean
def 𝕏 (k : ℕ) : BTField (k+1)
```

`BinaryTower.BTField_succ_eq_adjoinRoot` (theorem, [line 462](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L462))

```lean
theorem BTField_succ_eq_adjoinRoot (k : ℕ) : AdjoinRoot (poly k) = BTField (k+1)
```

`BinaryTower.coe_field_adjoinRoot` (instance, [line 464](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L464))

```lean
instance coe_field_adjoinRoot (k : ℕ) : Coe (AdjoinRoot (poly k)) (BTField (k+1))
```

`BinaryTower.Z_succ_eq_adjointRoot_root` (theorem, [line 468](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L468))

```lean
theorem Z_succ_eq_adjointRoot_root (k : ℕ) : Z (k+1) = AdjoinRoot.root (poly k)
```

`BinaryTower.list_0` (lemma, [line 470](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L470))

```lean
lemma list_0 : list 0 = List.Vector.cons (1 : GF(2)) List.Vector.nil
```

`BinaryTower.list_eq` (lemma, [line 475](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L475))

```lean
lemma list_eq (k : ℕ) :
    list (k+1) = (Z (k+1)) ::ᵥ (list k).map (AdjoinRoot.of (poly k))
```

`BinaryTower.eval_poly_at_root` (theorem, [line 481](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L481))

```lean
theorem eval_poly_at_root (k : ℕ) : (Z (k+1))^2 + (Z (k+1)) * Z k + 1 = 0
```

`BinaryTower.poly_form` (theorem, [line 489](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L489))

```lean
theorem poly_form (k : ℕ) : poly k = X^2 + (C (Z k) * X + 1)
```

`BinaryTower.eval_mapped_poly_at_root` (theorem, [line 492](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L492))

```lean
theorem eval_mapped_poly_at_root (k : ℕ) :
    eval₂ (AdjoinRoot.of (poly k)) (Z (k+1)) (poly k) = 0
```

`BinaryTower.list_length` (lemma, [line 516](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L516))

```lean
lemma list_length (k : ℕ) : (list k).length = k + 1
```

`BinaryTower.list_nonempty` (theorem, [line 521](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L521))

```lean
theorem list_nonempty (k : ℕ) : (list k).1 ≠ []
```

`BinaryTower.polyIrreducible` (theorem, [line 531](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L531))

```lean
theorem polyIrreducible (n : ℕ) : Irreducible (poly n)
```

`BinaryTower.polyIrreducibleFact` (instance, [line 533](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L533))

```lean
instance polyIrreducibleFact (n : ℕ) : Fact (Irreducible (poly n))
```

`BinaryTower.polyMonic` (theorem, [line 535](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L535))

```lean
theorem polyMonic (n : ℕ) : Monic (poly n)
```

`BinaryTower.poly_ne_zero` (lemma, [line 537](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean#L537))

```lean
lemma poly_ne_zero (n : ℕ) : poly n ≠ 0
```

## Depends on

- [Binary Tower Defining Polynomials](../support/definingpoly.md)
- [Binary Tower Preliminaries](../support/preliminaries.md)

## Proof depends on

- [Binary Tower Irreducibility and Trace](../support/irreducibilityandtracemapproperty.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Abstract/Core.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Abstract/Core.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Abstract.Core.json)
