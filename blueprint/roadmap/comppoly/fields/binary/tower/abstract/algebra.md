---
catalog: module
lean: BinaryTower.canonicalEmbedding, BinaryTower.BTField_add_eq, BinaryTower.BTField.RingHom_eq_of_dest_eq, BinaryTower.BTField.RingHom_eq_of_dest_AdjoinRoot_eq, BinaryTower.BTField.RingHom_cast_dest_apply, BinaryTower.BTField.RingHom_cast_dest_AdjoinRoot_apply, BinaryTower.towerAlgebraMap, BinaryTower.towerAlgebraMap_id, BinaryTower.towerAlgebraMap_succ_1, BinaryTower.towerAlgebraMap_succ, BinaryTower.towerAlgebraMap_succ_last, BinaryTower.BTField.RingHom_comp_cast, BinaryTower.towerAlgebraMap_assoc, BinaryTower.binaryAlgebraTower, BinaryTower.binaryTowerAlgebra_def, BinaryTower.algebraMap_binaryTowerAlgebra_def, BinaryTower.BTField.coe_one_succ, BinaryTower.binaryTowerAlgebra_id, BinaryTower.binaryTowerAlgebra_apply_assoc, BinaryTower.binaryTowerModule, BinaryTower.algebra_adjacent_tower, BinaryTower.algebraMap_adjacent_tower_def, BinaryTower.algebraMap_adjacent_tower_succ_eq_Adjoin_of, BinaryTower.algebra_adjacent_tower_def, BinaryTower.algebra_adjacent_tower_eq_AdjoinRoot_algebra, BinaryTower.BTField_succ_alg_equiv_adjoinRoot
statement: formalized
proof: formalized
---

# Abstract Binary Tower Algebra

`CompPoly.Fields.Binary.Tower.Abstract.Algebra`, in [CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean), by Quang Dao, Chung Thai Nguyen.

> Algebra maps and tower embeddings for the abstract binary tower fields.

`BinaryTower.canonicalEmbedding` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L31))

> The canonical ring homomorphism embedding `BTField k` into `BTField (k+1)`.
> This is the `AdjoinRoot.of` map.

```lean
def canonicalEmbedding (k : ℕ) : BTField k →+* BTField (k+1)
```

`BinaryTower.BTField_add_eq` (lemma, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L35))

```lean
lemma BTField_add_eq (k n m) : BTField (k + n + m) = BTField (k + (n + m))
```

`BinaryTower.BTField.RingHom_eq_of_dest_eq` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L39))

```lean
theorem BTField.RingHom_eq_of_dest_eq (k m n : ℕ) (h_eq : m = n) :
    (BTField k →+* BTField m) = (BTField k →+* BTField n)
```

`BinaryTower.BTField.RingHom_eq_of_dest_AdjoinRoot_eq` (theorem, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L45))

```lean
theorem BTField.RingHom_eq_of_dest_AdjoinRoot_eq (k m : ℕ) :
    (BTField k →+* BTField (m+1)) = (BTField k →+* (AdjoinRoot (poly m)))
```

`BinaryTower.BTField.RingHom_cast_dest_apply` (theorem, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L51))

```lean
theorem BTField.RingHom_cast_dest_apply (k m n : ℕ) (h_eq : m = n)
    (f : BTField k →+* BTField m) (x : BTField k) :
    (cast (BTField.RingHom_eq_of_dest_eq (k:=k) (m:=m) (n:=n) h_eq) f) x
    = cast (by apply cast_BTField_eq (h_eq:=h_eq)) (f x)
```

`BinaryTower.BTField.RingHom_cast_dest_AdjoinRoot_apply` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L59))

```lean
theorem BTField.RingHom_cast_dest_AdjoinRoot_apply (k m : ℕ)
    (f : BTField k →+* AdjoinRoot (poly m)) (x : BTField k) :
  (cast (BTField.RingHom_eq_of_dest_AdjoinRoot_eq (k:=k) (m:=m)).symm f) x
  = cast (BTField_succ_eq_adjoinRoot m) (f x)
```

`BinaryTower.towerAlgebraMap` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L69))

> Auxiliary definition for `towerAlgebraMap` using structural recursion.
> This is easier to reason about in proofs than the `Nat.rec` version.

```lean
def towerAlgebraMap (l r : ℕ) (h_le : l ≤ r) : BTField l →+* BTField r
```

`BinaryTower.towerAlgebraMap_id` (lemma, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L80))

```lean
lemma towerAlgebraMap_id (k : ℕ) : towerAlgebraMap (h_le:=by omega) = RingHom.id (BTField k)
```

`BinaryTower.towerAlgebraMap_succ_1` (lemma, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L84))

```lean
lemma towerAlgebraMap_succ_1 (k : ℕ) :
    towerAlgebraMap (l:=k) (r:=k+1) (h_le:=by omega) = canonicalEmbedding k
```

> Right associativity of the Tower Map

`BinaryTower.towerAlgebraMap_succ` (lemma, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L92))

```lean
lemma towerAlgebraMap_succ (l r : ℕ) (h_le : l ≤ r) :
    towerAlgebraMap (l:=l) (r:=r+1) (h_le:=by omega) =
  (towerAlgebraMap (l:=r) (r:=r+1) (h_le:=by omega)).comp
  (towerAlgebraMap (l:=l) (r:=r) (h_le:=by omega))
```

> Left associativity of the Tower Map

`BinaryTower.towerAlgebraMap_succ_last` (theorem, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L104))

```lean
theorem towerAlgebraMap_succ_last (r : ℕ) : ∀ l : ℕ, (h_le : l ≤ r) →
    towerAlgebraMap (l:=l) (r:=r+1) (h_le:=by
    exact Nat.le_trans (n:=l) (m:=r) (k:=r+1) (h_le) (by omega)) =
  (towerAlgebraMap (l:=l+1) (r:=r+1) (by omega)).comp (towerAlgebraMap
    (l:=l) (r:=l+1) (by omega))
```

`BinaryTower.BTField.RingHom_comp_cast` (theorem, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L131))

> Cast of composition of BTField ring homomorphism is composition of casted BTField ring homomorphism.
> Note that this assumes the SAME underlying instances (e.g. NonAssocSemiring)
> for both the input and output ring homs.

```lean
theorem BTField.RingHom_comp_cast {α β γ δ : ℕ} (f : BTField α →+* BTField β)
    (g : BTField β →+* BTField γ) (h : γ = δ) :
    ((cast (BTField.RingHom_eq_of_dest_eq (k:=β) (m:=γ) (n:=δ) h) g).comp f)
    = cast (BTField.RingHom_eq_of_dest_eq (k:=α) (m:=γ) (n:=δ) h) (g.comp f)
```

`BinaryTower.towerAlgebraMap_assoc` (theorem, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L144))

```lean
theorem towerAlgebraMap_assoc : ∀ r mid l : ℕ, (h_l_le_mid : l ≤ mid) → (h_mid_le_r : mid ≤ r) →
    towerAlgebraMap (l:=l) (r:=r) (h_le:=by exact Nat.le_trans h_l_le_mid h_mid_le_r) =
    (towerAlgebraMap (l:=mid) (r:=r) (h_le:=h_mid_le_r)).comp
    (towerAlgebraMap (l:=l) (r:=mid) (h_le:=h_l_le_mid))
```

`BinaryTower.binaryAlgebraTower` (definition, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L183))

```lean
def binaryAlgebraTower {l r : ℕ} (h_le : l ≤ r) : Algebra (BTField l) (BTField r)
```

`BinaryTower.binaryTowerAlgebra_def` (lemma, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L186))

```lean
lemma binaryTowerAlgebra_def (l r : ℕ) (h_le : l ≤ r) :
    @binaryAlgebraTower (l:=l) (r:=r) (h_le:=h_le)
    = (towerAlgebraMap l r h_le).toAlgebra
```

`BinaryTower.algebraMap_binaryTowerAlgebra_def` (lemma, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L190))

```lean
lemma algebraMap_binaryTowerAlgebra_def (l r : ℕ) (h_le : l ≤ r) :
    (@binaryAlgebraTower (l:=l) (r:=r) (h_le:=h_le)).algebraMap = towerAlgebraMap l r h_le
```

`BinaryTower.BTField.coe_one_succ` (lemma, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L193))

```lean
lemma BTField.coe_one_succ (l : ℕ) :
    (@binaryAlgebraTower (l:=l) (r:=l+1) (h_le:=by omega)).algebraMap (1 : BTField l) =
    (1 : BTField (l+1))
```

`BinaryTower.binaryTowerAlgebra_id` (theorem, [line 199](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L199))

```lean
theorem binaryTowerAlgebra_id {l r : ℕ} (h_eq : l = r) :
    @binaryAlgebraTower l r (h_le:=by omega) =
    (h_eq ▸ (Algebra.id (BTField l)) : Algebra (BTField l) (BTField r))
```

`BinaryTower.binaryTowerAlgebra_apply_assoc` (theorem, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L206))

```lean
theorem binaryTowerAlgebra_apply_assoc (l mid r : ℕ) (h_l_le_mid : l ≤ mid) (h_mid_le_r : mid ≤ r) :
    ∀ x : BTField l,
    (@binaryAlgebraTower (l:=l) (r:=r) (h_le:=by
      exact Nat.le_trans h_l_le_mid h_mid_le_r)).algebraMap x =
    (@binaryAlgebraTower (l:=mid) (r:=r) (h_le:=h_mid_le_r)).algebraMap
      (    (@binaryAlgebraTower (l:=l) (r:=mid) (h_le:=h_l_le_mid)).algebraMap x)
```

`BinaryTower.binaryTowerModule` (definition, [line 219](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L219))

> This also provides the corresponding Module instance.

```lean
def binaryTowerModule {l r : ℕ} (h_le : l ≤ r) : Module (BTField l) (BTField r)
```

`BinaryTower.algebra_adjacent_tower` (instance, [line 222](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L222))

```lean
instance (priority := 1000) algebra_adjacent_tower (l : ℕ) :
  Algebra (BTField l) (BTField (l+1))
```

`BinaryTower.algebraMap_adjacent_tower_def` (lemma, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L226))

```lean
lemma algebraMap_adjacent_tower_def (l : ℕ) :
    (algebraMap (BTField l) (BTField (l + 1))) = canonicalEmbedding l
```

`BinaryTower.algebraMap_adjacent_tower_succ_eq_Adjoin_of` (lemma, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L232))

```lean
lemma algebraMap_adjacent_tower_succ_eq_Adjoin_of (k : ℕ) :
    (algebraMap (BTField k) (BTField (k + 1))) = of (poly k)
```

`BinaryTower.algebra_adjacent_tower_def` (lemma, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L237))

```lean
lemma algebra_adjacent_tower_def (l : ℕ) :
    (algebra_adjacent_tower l) = (canonicalEmbedding l).toAlgebra
```

`BinaryTower.algebra_adjacent_tower_eq_AdjoinRoot_algebra` (lemma, [line 243](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L243))

```lean
lemma algebra_adjacent_tower_eq_AdjoinRoot_algebra (k : ℕ) :
    (algebra_adjacent_tower k) = (AdjoinRoot.instAlgebra (poly k))
```

`BinaryTower.BTField_succ_alg_equiv_adjoinRoot` (definition, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean#L252))

```lean
def BTField_succ_alg_equiv_adjoinRoot (k : ℕ) :
    AdjoinRoot (poly k) ≃ₐ[BTField k] BTField (k + 1)
```

## Depends on

- [Towers of algebras and their equivalences](../../../../data/ringtheory/algebratower.md)
- [Abstract Binary Tower Core](core.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Abstract/Algebra.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Abstract.Algebra.json)
