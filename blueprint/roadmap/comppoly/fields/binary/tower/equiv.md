---
catalog: module
lean: ConcreteBinaryTower.towerEquiv_zero, ConcreteBinaryTower.towerRingEquiv0, ConcreteBinaryTower.towerRingEquivFromConcrete0, ConcreteBinaryTower.towerRingHomForwardMap, ConcreteBinaryTower.towerRingHomBackwardMap, ConcreteBinaryTower.towerRingHomForwardMap0_eq, ConcreteBinaryTower.towerRingHomForwardMap_zero, ConcreteBinaryTower.towerRingHomForwardMap_one, ConcreteBinaryTower.towerRingHomForwardMap_Z, ConcreteBinaryTower.towerRingHomBackwardMap_forwardMap_eq, ConcreteBinaryTower.towerRingHomForwardMap_backwardMap_eq, ConcreteBinaryTower.towerRingHomForwardMap_add_eq, ConcreteBinaryTower.split_mul_eq_mul_split, ConcreteBinaryTower.towerRingHomForwardMap_mul_eq, ConcreteBinaryTower.towerRingHomForwardMap_split_eq, ConcreteBinaryTower.towerRingHomForwardMap_join, ConcreteBinaryTower.TowerEquivResult, ConcreteBinaryTower.towerEquiv, ConcreteBinaryTower.BTField_algebraMap_succ_eq_join, ConcreteBinaryTower.ConcreteBTField_algebraMap_succ_eq_join, ConcreteBinaryTower.towerEquiv_ringEquiv_apply, ConcreteBinaryTower.towerEquiv_commutes_left_succ, ConcreteBinaryTower.towerEquiv_commutes_left_diff, ConcreteBinaryTower.towerEquiv_commutes_left, ConcreteBinaryTower.instAlgebraTowerEquiv, ConcreteBinaryTower.towerEquiv_multilinearBasis, ConcreteBinaryTower.multilinearBasis_map_towerEquiv, ConcreteBinaryTower.multilinearBasis_repr_towerEquiv
statement: formalized
proof: formalized
---

# Binary Tower Equivalence

`CompPoly.Fields.Binary.Tower.Equiv`, in [CompPoly/Fields/Binary/Tower/Equiv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean), by Chung Thai Nguyen, Quang Dao.

> Equivalences between the abstract and concrete binary tower constructions.
>
> The concrete-to-abstract equivalence commutes with the chosen tower embeddings and preserves
> the multilinear basis at each numeric index. `multilinearBasis_map_towerEquiv` identifies
> the bases after changing coefficients at the base level and transporting the ambient space.
> The coefficient actions are selected locally from the tower maps.

`ConcreteBinaryTower.towerEquiv_zero` (definition, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L33))

```lean
noncomputable def towerEquiv_zero : RingEquiv (R:=GF(2)) (S:=ConcreteBTField 0)
```

`ConcreteBinaryTower.towerRingEquiv0` (definition, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L62))

```lean
noncomputable def towerRingEquiv0 : BTField 0 ≃+* ConcreteBTField 0
```

`ConcreteBinaryTower.towerRingEquivFromConcrete0` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L67))

```lean
noncomputable def towerRingEquivFromConcrete0 : ConcreteBTField 0 ≃+* BTField 0
```

`ConcreteBinaryTower.towerRingHomForwardMap` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L70))

```lean
noncomputable def towerRingHomForwardMap (k : ℕ) : ConcreteBTField k → BTField k
```

`ConcreteBinaryTower.towerRingHomBackwardMap` (definition, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L84))

```lean
noncomputable def towerRingHomBackwardMap (k : ℕ) : BTField k → ConcreteBTField k
```

`ConcreteBinaryTower.towerRingHomForwardMap0_eq` (lemma, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L97))

```lean
lemma towerRingHomForwardMap0_eq :
    towerRingEquivFromConcrete0.toFun = towerRingHomForwardMap 0
```

`ConcreteBinaryTower.towerRingHomForwardMap_zero` (lemma, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L102))

```lean
lemma towerRingHomForwardMap_zero {k : ℕ} :
    (towerRingHomForwardMap k) 0 = 0
```

`ConcreteBinaryTower.towerRingHomForwardMap_one` (lemma, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L119))

```lean
lemma towerRingHomForwardMap_one {k : ℕ} :
    (towerRingHomForwardMap k) 1 = 1
```

`ConcreteBinaryTower.towerRingHomForwardMap_Z` (lemma, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L136))

```lean
lemma towerRingHomForwardMap_Z (k : ℕ) :
    towerRingHomForwardMap k (Z k) = BinaryTower.Z k
```

`ConcreteBinaryTower.towerRingHomBackwardMap_forwardMap_eq` (lemma, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L153))

```lean
lemma towerRingHomBackwardMap_forwardMap_eq (k : ℕ) (x : ConcreteBTField k) :
    towerRingHomBackwardMap (k:=k) (towerRingHomForwardMap (k:=k) x) = x
```

`ConcreteBinaryTower.towerRingHomForwardMap_backwardMap_eq` (lemma, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L181))

```lean
lemma towerRingHomForwardMap_backwardMap_eq (k : ℕ) (x : BTField k) :
    towerRingHomForwardMap (k:=k) (towerRingHomBackwardMap (k:=k) x) = x
```

`ConcreteBinaryTower.towerRingHomForwardMap_add_eq` (lemma, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L208))

```lean
lemma towerRingHomForwardMap_add_eq (k : ℕ) (x y : ConcreteBTField k) :
    towerRingHomForwardMap (k:=k) (x + y)
    = towerRingHomForwardMap (k:=k) x + towerRingHomForwardMap (k:=k) y
```

`ConcreteBinaryTower.split_mul_eq_mul_split` (theorem, [line 250](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L250))

```lean
theorem split_mul_eq_mul_split {k : ℕ} (h_pos : k > 0) (x₀ x₁ : ConcreteBTField k)
    (hi₀ lo₀ hi₁ lo₁ : ConcreteBTField (k - 1))
  (h_split_x₀ : split h_pos x₀ = (hi₀, lo₀))
  (h_split_x₁ : split h_pos x₁ = (hi₁, lo₁)) :
  split h_pos (x₀ * x₁) =
    (lo₀ * hi₁ + lo₁ * hi₀ + hi₀ * hi₁ * Z (k - 1), lo₀ * lo₁ + hi₀ * hi₁)
```

`ConcreteBinaryTower.towerRingHomForwardMap_mul_eq` (lemma, [line 263](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L263))

```lean
lemma towerRingHomForwardMap_mul_eq (k : ℕ) (x y : ConcreteBTField k) :
    towerRingHomForwardMap (k:=k) (x * y)
    = towerRingHomForwardMap (k:=k) x * towerRingHomForwardMap (k:=k) y
```

`ConcreteBinaryTower.towerRingHomForwardMap_split_eq` (lemma, [line 304](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L304))

```lean
lemma towerRingHomForwardMap_split_eq (k : ℕ) (h_pos : k > 0) (x : ConcreteBTField k) :
    let p := split (k:=k) (h:=h_pos) x
  towerRingHomForwardMap (k:=k) (x) =
    BinaryTower.join_via_add_smul (k:=k) (h_pos:=h_pos)
      (hi_btf := towerRingHomForwardMap (k:=k-1) (p.1))
      (lo_btf := towerRingHomForwardMap (k:=k-1) (p.2))
```

`ConcreteBinaryTower.towerRingHomForwardMap_join` (lemma, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L320))

```lean
lemma towerRingHomForwardMap_join {k : ℕ} (h_pos : k > 0) (hi lo : ConcreteBTField (k - 1)) :
    towerRingHomForwardMap (k:=k) (《 hi, lo 》) =
    BinaryTower.join_via_add_smul (k:=k) (h_pos:=by omega)
      (hi_btf := towerRingHomForwardMap (k:=k-1) hi)
      (lo_btf := towerRingHomForwardMap (k:=k-1) lo)
```

`ConcreteBinaryTower.TowerEquivResult` (structure, [line 336](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L336))

```lean
structure TowerEquivResult (k : ℕ) where
  ringEquiv : ConcreteBTField k ≃+* BTField k
  ringEquivForwardMapEq : ringEquiv = towerRingHomForwardMap k
```

`ConcreteBinaryTower.towerEquiv` (definition, [line 340](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L340))

```lean
noncomputable def towerEquiv (n : ℕ) : TowerEquivResult n
```

`ConcreteBinaryTower.BTField_algebraMap_succ_eq_join` (theorem, [line 376](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L376))

```lean
theorem BTField_algebraMap_succ_eq_join (k : ℕ) (x : BTField k) :
    algebraMap (BTField k) (BTField (k+1)) x =
      BinaryTower.join_via_add_smul (k:=k+1) (h_pos:=by omega) 0 x
```

`ConcreteBinaryTower.ConcreteBTField_algebraMap_succ_eq_join` (theorem, [line 381](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L381))

```lean
theorem ConcreteBTField_algebraMap_succ_eq_join (k : ℕ) (r : ConcreteBTField k) :
    algebraMap (ConcreteBTField k) (ConcreteBTField (k+1)) r =
      join (k:=k+1) (h_pos:=by omega) 0 r
```

`ConcreteBinaryTower.towerEquiv_ringEquiv_apply` (theorem, [line 387](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L387))

```lean
theorem towerEquiv_ringEquiv_apply (k : ℕ) (r : ConcreteBTField k) :
    (towerEquiv k).ringEquiv r = towerRingHomForwardMap k r
```

`ConcreteBinaryTower.towerEquiv_commutes_left_succ` (theorem, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L392))

```lean
theorem towerEquiv_commutes_left_succ (k : ℕ) : ∀ r : ConcreteBTField k,
    (AlgebraTower.algebraMap k (k+1) (by omega)) ((towerEquiv k).ringEquiv r) =
  (towerEquiv (k+1)).ringEquiv ((AlgebraTower.algebraMap k (k+1) (by omega)) r)
```

`ConcreteBinaryTower.towerEquiv_commutes_left_diff` (theorem, [line 414](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L414))

```lean
theorem towerEquiv_commutes_left_diff (i d : ℕ) : ∀ r : ConcreteBTField i,
    (AlgebraTower.algebraMap i (i+d) (by omega)) ((towerEquiv i).ringEquiv r) =
  (towerEquiv (i+d)).ringEquiv ((AlgebraTower.algebraMap i (i+d) (by omega)) r)
```

`ConcreteBinaryTower.towerEquiv_commutes_left` (theorem, [line 477](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L477))

```lean
theorem towerEquiv_commutes_left (i j : ℕ) (h : i ≤ j) : ∀ r : ConcreteBTField i,
    (AlgebraTower.algebraMap i j h) ((towerEquiv i).ringEquiv r) =
  (towerEquiv j).ringEquiv ((AlgebraTower.algebraMap i j h) r)
```

`ConcreteBinaryTower.instAlgebraTowerEquiv` (definition, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L485))

```lean
noncomputable def instAlgebraTowerEquiv : AlgebraTowerEquiv
  (ConcreteBTField) (BTField)
```

`ConcreteBinaryTower.towerEquiv_multilinearBasis` (theorem, [line 493](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L493))

> The tower equivalence sends each concrete multilinear basis vector to the abstract
> basis vector at the same numeric index.

```lean
theorem towerEquiv_multilinearBasis {i j : ℕ} (h : i ≤ j) (q : Fin (2 ^ (j - i))) :
    (towerEquiv j).ringEquiv (multilinearBasis i j h q) =
      BinaryTower.multilinearBasis i j h q
```

`ConcreteBinaryTower.multilinearBasis_map_towerEquiv` (theorem, [line 510](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L510))

> Transporting the concrete multilinear basis along the tower equivalence gives the
> abstract basis with coefficients changed by the inverse equivalence at the base level.
> Both coefficient actions are the chosen tower actions.

```lean
theorem multilinearBasis_map_towerEquiv {i j : ℕ} (h : i ≤ j) :
    let := ConcreteBTFieldAlgebra h
    let := binaryAlgebraTower h
    let := instAlgebraTowerEquiv.toAlgebraOverLeft i j h
    (multilinearBasis i j h).map
        (instAlgebraTowerEquiv.toAlgEquivOverLeft i j h).toLinearEquiv =
      (BinaryTower.multilinearBasis i j h).mapCoeffs (towerEquiv i).ringEquiv.symm
        (by
          intro a x
          change towerAlgebraMap i j h
              ((towerEquiv i).ringEquiv ((towerEquiv i).ringEquiv.symm a)) * x =
            towerAlgebraMap i j h a * x
          rw [RingEquiv.apply_symm_apply])
```

`ConcreteBinaryTower.multilinearBasis_repr_towerEquiv` (theorem, [line 534](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean#L534))

> The abstract basis coordinates of a mapped element are its concrete basis coordinates
> mapped by the equivalence at the base level, at the same numeric indices.
> Both representations use their chosen tower coefficient actions.

```lean
theorem multilinearBasis_repr_towerEquiv {i j : ℕ} (h : i ≤ j) (x : ConcreteBTField j)
    (q : Fin (2 ^ (j - i))) :
    let := ConcreteBTFieldAlgebra h
    let := binaryAlgebraTower h
    (BinaryTower.multilinearBasis i j h).repr ((towerEquiv j).ringEquiv x) q =
      (towerEquiv i).ringEquiv ((ConcreteBinaryTower.multilinearBasis i j h).repr x q)
```

## Depends on

- [Abstract Binary Tower Basis](abstract/basis.md)
- [Concrete Binary Tower Basis](concrete/basis.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Equiv.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Equiv.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Equiv.json)
