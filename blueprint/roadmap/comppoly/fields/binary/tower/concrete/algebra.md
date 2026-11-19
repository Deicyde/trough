---
catalog: module
lean: ConcreteBinaryTower.canonicalAlgMap, ConcreteBinaryTower.toNat_canonicalAlgMap, ConcreteBinaryTower.generator_is_not_lifted_to_succ, ConcreteBinaryTower.ConcreteBTField_add_eq, ConcreteBinaryTower.ConcreteBTField.RingHom_eq_of_dest_eq, ConcreteBinaryTower.ConcreteBTField.RingHom_eq_of_source_eq, ConcreteBinaryTower.ConcreteBTField.RingHom_cast_dest_apply, ConcreteBinaryTower.ConcreteBTField.RingHom_cast_source_apply, ConcreteBinaryTower.concreteTowerAlgebraMap, ConcreteBinaryTower.concreteTowerAlgebraMap_id, ConcreteBinaryTower.concreteTowerAlgebraMap_succ_1, ConcreteBinaryTower.concreteTowerAlgebraMap_succ, ConcreteBinaryTower.concreteTowerAlgebraMap_succ_last, ConcreteBinaryTower.ConcreteBTField.RingHom_comp_cast, ConcreteBinaryTower.concreteTowerAlgebraMap_assoc, ConcreteBinaryTower.toNat_concreteTowerAlgebraMap, ConcreteBinaryTower.concreteTowerAlgebraMap_eq_setWidth, ConcreteBinaryTower.concreteTowerAlgebraMap_Z_succ, ConcreteBinaryTower.instAlgebraTowerConcreteBTF, ConcreteBinaryTower.ConcreteBTFieldAlgebra, ConcreteBinaryTower.join_via_add_smul, ConcreteBinaryTower.split_algebraMap_eq_zero_x, ConcreteBinaryTower.algebraMap_succ_eq_zero_x, ConcreteBinaryTower.algebraMap_eq_zero_x, ConcreteBinaryTower.split_smul_Z_eq_zero_x, ConcreteBinaryTower.smul_Z_eq_zero_x, ConcreteBinaryTower.join_eq_join_via_add_smul, ConcreteBinaryTower.split_join_via_add_smul_eq_iff_split, ConcreteBinaryTower.ConcreteBTFieldAlgebra_def, ConcreteBinaryTower.algebraMap_ConcreteBTFieldAlgebra_def, ConcreteBinaryTower.coe_one_succ, ConcreteBinaryTower.unique_linear_decomposition_succ, ConcreteBinaryTower.ConcreteBTFieldAlgebra_id, ConcreteBinaryTower.ConcreteBTFieldAlgebra_apply_assoc, ConcreteBinaryTower.binaryTowerModule, ConcreteBinaryTower.algebra_adjacent_tower, ConcreteBinaryTower.algebraMap_adjacent_tower_def, ConcreteBinaryTower.aeval_definingPoly_at_Z_succ
statement: formalized
proof: formalized
---

# Concrete Binary Tower Algebra

`CompPoly.Fields.Binary.Tower.Concrete.Algebra`, in [CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean), by Chung Thai Nguyen, Quang Dao.

> Algebra maps and embeddings for the concrete bitvector binary tower.

`ConcreteBinaryTower.canonicalAlgMap` (definition, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L27))

```lean
def canonicalAlgMap (k : ℕ)
```

`ConcreteBinaryTower.toNat_canonicalAlgMap` (theorem, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L32))

> The embedding into the next level preserves the stored natural word.

```lean
theorem toNat_canonicalAlgMap (k : ℕ) (x : ConcreteBTField k) :
    (canonicalAlgMap k x).toNat = x.toNat
```

`ConcreteBinaryTower.generator_is_not_lifted_to_succ` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L43))

> `Z(k+1)` is the adjoined root of `poly k` to `ConcreteBTField (k+1)`, so it is not
> lifted to `ConcreteBTField (k+1)` by `canonicalAlgMap`

```lean
theorem generator_is_not_lifted_to_succ (k : ℕ) :
    ∀ x : ConcreteBTField k, canonicalAlgMap (k:=k) x ≠ Z (k + 1)
```

`ConcreteBinaryTower.ConcreteBTField_add_eq` (lemma, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L64))

```lean
lemma ConcreteBTField_add_eq (k n m) :
    ConcreteBTField (k + n + m) = ConcreteBTField (k + (n + m))
```

`ConcreteBinaryTower.ConcreteBTField.RingHom_eq_of_dest_eq` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L69))

```lean
theorem ConcreteBTField.RingHom_eq_of_dest_eq (k m n : ℕ) (h_eq : m = n) :
    (ConcreteBTField k →+* ConcreteBTField m)
    = (ConcreteBTField k →+* ConcreteBTField n)
```

`ConcreteBinaryTower.ConcreteBTField.RingHom_eq_of_source_eq` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L76))

```lean
theorem ConcreteBTField.RingHom_eq_of_source_eq (k n m : ℕ) (h_eq : k = n) :
    (ConcreteBTField k →+* ConcreteBTField m)
    = (ConcreteBTField n →+* ConcreteBTField m)
```

`ConcreteBinaryTower.ConcreteBTField.RingHom_cast_dest_apply` (theorem, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L83))

```lean
theorem ConcreteBTField.RingHom_cast_dest_apply (k m n : ℕ) (h_eq : m = n)
    (f : ConcreteBTField k →+* ConcreteBTField m) (x : ConcreteBTField k) :
    (cast (ConcreteBTField.RingHom_eq_of_dest_eq (k:=k) (m:=m) (n:=n) h_eq) f) x
    = cast (by apply cast_ConcreteBTField_eq (h_eq:=h_eq)) (f x)
```

`ConcreteBinaryTower.ConcreteBTField.RingHom_cast_source_apply` (theorem, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L91))

```lean
theorem ConcreteBTField.RingHom_cast_source_apply (k n m : ℕ) (h_eq : k = n)
    (f : ConcreteBTField k →+* ConcreteBTField m) (x : ConcreteBTField n) :
    (cast (ConcreteBTField.RingHom_eq_of_source_eq (k:=k) (n:=n) (m:=m) h_eq) f) x
    = f (cast (by apply cast_ConcreteBTField_eq (h_eq:=h_eq.symm)) x)
```

`ConcreteBinaryTower.concreteTowerAlgebraMap` (definition, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L102))

> Auxiliary definition for `concreteTowerAlgebraMap` using structural recursion.
> This is easier to reason about in proofs than the `Nat.rec` version.

```lean
def concreteTowerAlgebraMap (l r : ℕ) (h_le : l ≤ r) :
    ConcreteBTField l →+* ConcreteBTField r
```

`ConcreteBinaryTower.concreteTowerAlgebraMap_id` (lemma, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L116))

```lean
lemma concreteTowerAlgebraMap_id (k : ℕ) :
    concreteTowerAlgebraMap (h_le:=by omega) = RingHom.id (ConcreteBTField k)
```

`ConcreteBinaryTower.concreteTowerAlgebraMap_succ_1` (lemma, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L121))

```lean
lemma concreteTowerAlgebraMap_succ_1 (k : ℕ) :
    concreteTowerAlgebraMap (l:=k) (r:=k + 1) (h_le:=by omega) = canonicalAlgMap k
```

> Right associativity of the Tower Map

`ConcreteBinaryTower.concreteTowerAlgebraMap_succ` (lemma, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L130))

```lean
lemma concreteTowerAlgebraMap_succ (l r : ℕ) (h_le : l ≤ r) :
    concreteTowerAlgebraMap (l:=l) (r:=r + 1) (h_le:=by omega) =
  (concreteTowerAlgebraMap (l:=r) (r:=r + 1) (h_le:=by omega)).comp
  (concreteTowerAlgebraMap (l:=l) (r:=r) (h_le:=by omega))
```

> Left associativity of the Tower Map

`ConcreteBinaryTower.concreteTowerAlgebraMap_succ_last` (theorem, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L142))

```lean
theorem concreteTowerAlgebraMap_succ_last (r : ℕ) : ∀ l : ℕ, (h_le : l ≤ r) →
    concreteTowerAlgebraMap (l:=l) (r:=r + 1) (h_le:=by
    exact Nat.le_trans (n:=l) (m:=r) (k:=r + 1) (h_le) (by omega)) =
  (concreteTowerAlgebraMap (l:=l + 1) (r:=r + 1) (by omega)).comp (concreteTowerAlgebraMap
    (l:=l) (r:=l + 1) (by omega))
```

`ConcreteBinaryTower.ConcreteBTField.RingHom_comp_cast` (theorem, [line 170](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L170))

> Cast of composition of ConcreteBTField ring homomorphism is composition of
> casted ConcreteBTField ring homomorphism.
> Note that this assumes the SAME underlying instances (e.g. NonAssocSemiring)
> for both the input and output ring homs.

```lean
theorem ConcreteBTField.RingHom_comp_cast {α β γ δ : ℕ}
    (f : ConcreteBTField α →+* ConcreteBTField β)
    (g : ConcreteBTField β →+* ConcreteBTField γ) (h : γ = δ) :
    ((cast (ConcreteBTField.RingHom_eq_of_dest_eq (k:=β) (m:=γ) (n:=δ) h) g).comp f)
    = cast (ConcreteBTField.RingHom_eq_of_dest_eq (k:=α) (m:=γ) (n:=δ) h) (g.comp f)
```

`ConcreteBinaryTower.concreteTowerAlgebraMap_assoc` (theorem, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L183))

```lean
theorem concreteTowerAlgebraMap_assoc :
    ∀ r mid l : ℕ, (h_l_le_mid : l ≤ mid) → (h_mid_le_r : mid ≤ r) →
    concreteTowerAlgebraMap (l:=l) (r:=r) (h_le:=by exact Nat.le_trans h_l_le_mid h_mid_le_r) =
    (concreteTowerAlgebraMap (l:=mid) (r:=r) (h_le:=h_mid_le_r)).comp
    (concreteTowerAlgebraMap (l:=l) (r:=mid) (h_le:=h_l_le_mid))
```

`ConcreteBinaryTower.toNat_concreteTowerAlgebraMap` (theorem, [line 213](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L213))

> An embedding between any ordered levels preserves the stored natural word.

```lean
theorem toNat_concreteTowerAlgebraMap {i j : ℕ} (h : i ≤ j) (x : ConcreteBTField i) :
    (concreteTowerAlgebraMap i j h x).toNat = x.toNat
```

`ConcreteBinaryTower.concreteTowerAlgebraMap_eq_setWidth` (theorem, [line 222](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L222))

> An embedding between ordered levels zero-extends the original bitvector.

```lean
theorem concreteTowerAlgebraMap_eq_setWidth {i j : ℕ} (h : i ≤ j)
    (x : ConcreteBTField i) :
    (concreteTowerAlgebraMap i j h x).toBitVec = x.toBitVec.setWidth (2 ^ j)
```

`ConcreteBinaryTower.concreteTowerAlgebraMap_Z_succ` (theorem, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L231))

> The image of the level-`k + 1` generator keeps its set bit at position `2 ^ k`.

```lean
theorem concreteTowerAlgebraMap_Z_succ {k j : ℕ} (h : k + 1 ≤ j) :
    (concreteTowerAlgebraMap (k + 1) j h (Z (k + 1))).toBitVec =
      BitVec.ofNat (2 ^ j) (2 ^ (2 ^ k))
```

`ConcreteBinaryTower.instAlgebraTowerConcreteBTF` (instance, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L241))

> **Formalization of Cross - Level Algebra** : For any `k ≤ τ`, `ConcreteBTField τ` is an
> algebra over `ConcreteBTField k`.

```lean
instance instAlgebraTowerConcreteBTF : AlgebraTower (ConcreteBTField)
```

`ConcreteBinaryTower.ConcreteBTFieldAlgebra` (abbreviation, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L251))

```lean
abbrev ConcreteBTFieldAlgebra {l r : ℕ} (h_le : l ≤ r) :
    Algebra (ConcreteBTField l) (ConcreteBTField r)
```

`ConcreteBinaryTower.join_via_add_smul` (definition, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L255))

```lean
def join_via_add_smul (k : ℕ) (h_pos : k > 0) (hi_btf lo_btf : ConcreteBTField (k - 1)) :
    ConcreteBTField k
```

`ConcreteBinaryTower.split_algebraMap_eq_zero_x` (lemma, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L264))

> An element `x` lifted from the base field `ConcreteBTField (k-1)` has `(0, x)` as its
> split representation in `ConcreteBTField k`.

```lean
lemma split_algebraMap_eq_zero_x {k : ℕ} (h_pos : k > 0) (x : ConcreteBTField (k - 1)) :
    letI instAlgebra := ConcreteBTFieldAlgebra (l:=k-1) (r:=k) (h_le:=by omega)
  split h_pos (algebraMap (ConcreteBTField (k - 1)) (ConcreteBTField k) x) = (0, x)
```

`ConcreteBinaryTower.algebraMap_succ_eq_zero_x` (lemma, [line 298](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L298))

```lean
lemma algebraMap_succ_eq_zero_x {k : ℕ} (h_pos : k > 0) (x : ConcreteBTField (k - 1)) :
    letI instAlgebra := ConcreteBTFieldAlgebra (l:=k-1) (r:=k) (h_le:=by omega)
  algebraMap (ConcreteBTField (k - 1)) (ConcreteBTField k) x = 《 0, x 》
```

`ConcreteBinaryTower.algebraMap_eq_zero_x` (lemma, [line 304](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L304))

```lean
lemma algebraMap_eq_zero_x {i j : ℕ} (h_le : i < j) (x : ConcreteBTField i) :
    letI instAlgebra := ConcreteBTFieldAlgebra (l:=i) (r:=j) (h_le:=by omega)
    letI instAlgebraPred := ConcreteBTFieldAlgebra (l:=i) (r:=j-1) (h_le:=by omega)
    algebraMap (ConcreteBTField i) (ConcreteBTField j) x
      = 《 0, algebraMap (ConcreteBTField i) (ConcreteBTField (j-1)) x 》
```

`ConcreteBinaryTower.split_smul_Z_eq_zero_x` (lemma, [line 328](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L328))

```lean
lemma split_smul_Z_eq_zero_x {k : ℕ} (h_pos : k > 0) (x : ConcreteBTField (k - 1)) :
    letI instAlgebra := ConcreteBTFieldAlgebra (l:=k-1) (r:=k) (h_le:=by omega)
  split h_pos (x • Z k) = (x, 0)
```

`ConcreteBinaryTower.smul_Z_eq_zero_x` (lemma, [line 352](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L352))

```lean
lemma smul_Z_eq_zero_x {k : ℕ} (h_pos : k > 0) (x : ConcreteBTField (k - 1)) :
    letI instAlgebra := ConcreteBTFieldAlgebra (l:=k-1) (r:=k) (h_le:=by omega)
  x • Z k = 《 x, 0 》
```

`ConcreteBinaryTower.join_eq_join_via_add_smul` (theorem, [line 359](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L359))

```lean
theorem join_eq_join_via_add_smul {k : ℕ} (h_pos : k > 0)
    (hi_btf lo_btf : ConcreteBTField (k - 1)) :
    《 hi_btf, lo_btf 》 = join_via_add_smul k h_pos hi_btf lo_btf
```

`ConcreteBinaryTower.split_join_via_add_smul_eq_iff_split` (lemma, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L382))

```lean
lemma split_join_via_add_smul_eq_iff_split {k : ℕ} (h_pos : k > 0)
    (hi_btf lo_btf : ConcreteBTField (k - 1)) :
    split (k:=k) (h:=by omega) (x:=join_via_add_smul (k:=k) (h_pos:=h_pos) hi_btf lo_btf) =
      (hi_btf, lo_btf)
```

`ConcreteBinaryTower.ConcreteBTFieldAlgebra_def` (lemma, [line 390](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L390))

```lean
lemma ConcreteBTFieldAlgebra_def (l r : ℕ) (h_le : l ≤ r) :
    @ConcreteBTFieldAlgebra (l:=l) (r:=r) (h_le:=h_le)
    = (concreteTowerAlgebraMap l r h_le).toAlgebra
```

`ConcreteBinaryTower.algebraMap_ConcreteBTFieldAlgebra_def` (lemma, [line 394](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L394))

```lean
lemma algebraMap_ConcreteBTFieldAlgebra_def (l r : ℕ) (h_le : l ≤ r) :
    (@ConcreteBTFieldAlgebra (l:=l) (r:=r) (h_le:=h_le)).algebraMap
    = concreteTowerAlgebraMap l r h_le
```

`ConcreteBinaryTower.coe_one_succ` (lemma, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L398))

```lean
lemma coe_one_succ (l : ℕ) :
    (@ConcreteBTFieldAlgebra (l:=l) (r:=l + 1) (h_le:=by omega)).algebraMap
    (1 : ConcreteBTField l) = (1 : ConcreteBTField (l + 1))
```

`ConcreteBinaryTower.unique_linear_decomposition_succ` (theorem, [line 403](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L403))

```lean
theorem unique_linear_decomposition_succ (k : ℕ) :
    letI : Algebra (ConcreteBTField k) (ConcreteBTField (k+1)) :=
    ConcreteBTFieldAlgebra (l:=k) (r:=k+1) (h_le:=by omega)
  ∀ (x : ConcreteBTField (k+1)), ∃! (p : ConcreteBTField k × ConcreteBTField k),
    x = join_via_add_smul (k+1) (by omega) p.1 p.2
```

`ConcreteBinaryTower.ConcreteBTFieldAlgebra_id` (theorem, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L431))

```lean
theorem ConcreteBTFieldAlgebra_id {l r : ℕ} (h_eq : l = r) :
    @ConcreteBTFieldAlgebra l r (h_le:=by omega) =
    (h_eq ▸ (Algebra.id (ConcreteBTField l)) :
      Algebra (ConcreteBTField l) (ConcreteBTField r))
```

`ConcreteBinaryTower.ConcreteBTFieldAlgebra_apply_assoc` (theorem, [line 439](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L439))

```lean
theorem ConcreteBTFieldAlgebra_apply_assoc (l mid r : ℕ)
    (h_l_le_mid : l ≤ mid) (h_mid_le_r : mid ≤ r) :
    ∀ x : ConcreteBTField l,
    (@ConcreteBTFieldAlgebra (l:=l) (r:=r) (h_le:=by
      exact Nat.le_trans h_l_le_mid h_mid_le_r)).algebraMap x =
    (@ConcreteBTFieldAlgebra (l:=mid) (r:=r) (h_le:=h_mid_le_r)).algebraMap
      ((@ConcreteBTFieldAlgebra (l:=l) (r:=mid) (h_le:=h_l_le_mid)).algebraMap x)
```

`ConcreteBinaryTower.binaryTowerModule` (abbreviation, [line 453](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L453))

> This also provides the corresponding Module instance.

```lean
abbrev binaryTowerModule {l r : ℕ} (h_le : l ≤ r) :
    Module (ConcreteBTField l) (ConcreteBTField r)
```

`ConcreteBinaryTower.algebra_adjacent_tower` (instance, [line 457](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L457))

```lean
instance (priority := 1000) algebra_adjacent_tower (l : ℕ) :
  Algebra (ConcreteBTField l) (ConcreteBTField (l + 1))
```

`ConcreteBinaryTower.algebraMap_adjacent_tower_def` (lemma, [line 461](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L461))

```lean
lemma algebraMap_adjacent_tower_def (l : ℕ) :
    (algebraMap (ConcreteBTField l) (ConcreteBTField (l + 1))) =
    canonicalAlgMap l
```

`ConcreteBinaryTower.aeval_definingPoly_at_Z_succ` (lemma, [line 468](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean#L468))

```lean
lemma aeval_definingPoly_at_Z_succ (k : ℕ) :
    (aeval (Z (k + 1))) (definingPoly (s:=Z (k))) = 0
```

## Depends on

- [Towers of algebras and their equivalences](../../../../data/ringtheory/algebratower.md)
- [Concrete Binary Tower Field](field.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Concrete/Algebra.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Concrete.Algebra.json)
