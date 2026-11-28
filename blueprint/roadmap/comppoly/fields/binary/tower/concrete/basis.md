---
catalog: module
lean: ConcreteBinaryTower.Basis_cast_index_eq, ConcreteBinaryTower.Basis_cast_dest_eq, ConcreteBinaryTower.PowerBasis_cast_dest_eq, ConcreteBinaryTower.Basis_cast_index_apply, ConcreteBinaryTower.Basis_cast_dest_apply, ConcreteBinaryTower.basisSucc, ConcreteBinaryTower.powerBasisSucc, ConcreteBinaryTower.powerBasisSucc_gen, ConcreteBinaryTower.minPoly_of_powerBasisSucc_generator, ConcreteBinaryTower.powerBasisSucc_dim, ConcreteBinaryTower.hli_level_diff_0, ConcreteBinaryTower.isScalarTower_succ_right, ConcreteBinaryTower.multilinearBasis, ConcreteBinaryTower.PowerBasis.dim_of_eq_rec, ConcreteBinaryTower.PowerBasis.cast_basis_succ_of_eq_rec_apply, ConcreteBinaryTower.coe_basis_apply, ConcreteBinaryTower.algebraMap_𝕏_eq_of_index_eq, ConcreteBinaryTower.multilinearBasis_apply
statement: formalized
proof: formalized
---

# Concrete Binary Tower Basis

`CompPoly.Fields.Binary.Tower.Concrete.Basis`, in [CompPoly/Fields/Binary/Tower/Concrete/Basis.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean), by Chung Thai Nguyen, Quang Dao.

> Basis constructions for the concrete bitvector binary tower.

`ConcreteBinaryTower.Basis_cast_index_eq` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L30))

```lean
theorem Basis_cast_index_eq (i j k n : ℕ) (h_le : k ≤ n) (h_eq : i = j) :
    letI instAlgebra : Algebra (ConcreteBTField k) (ConcreteBTField n) :=
      ConcreteBTFieldAlgebra (l:=k) (r:=n) (h_le:=h_le)
    letI : Module (ConcreteBTField k) (ConcreteBTField n) := instAlgebra.toModule
    (Basis (Fin (i)) (ConcreteBTField k) (ConcreteBTField n)) =
    (Basis (Fin (j)) (ConcreteBTField k) (ConcreteBTField n))
```

`ConcreteBinaryTower.Basis_cast_dest_eq` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L39))

```lean
theorem Basis_cast_dest_eq {ι : Type*} (k n m : ℕ) (h_k_le_n : k ≤ n)
    (h_k_le_m : k ≤ m) (h_eq : m = n) :
  letI instLeftAlgebra := ConcreteBTFieldAlgebra (l:=k) (r:=m) (h_le:=h_k_le_m)
  letI instRightAlgebra := ConcreteBTFieldAlgebra (l:=k) (r:=n) (h_le:=h_k_le_n)
  @Basis ι (ConcreteBTField k) (ConcreteBTField m) _ _ instLeftAlgebra.toModule =
  @Basis ι (ConcreteBTField k) (ConcreteBTField n) _ _ instRightAlgebra.toModule
```

`ConcreteBinaryTower.PowerBasis_cast_dest_eq` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L48))

```lean
theorem PowerBasis_cast_dest_eq (k n m : ℕ) (h_k_le_n : k ≤ n)
    (h_k_le_m : k ≤ m) (h_eq : m = n) :
  letI instLeftAlgebra := ConcreteBTFieldAlgebra (l:=k) (r:=m) (h_le:=h_k_le_m)
  letI instRightAlgebra := ConcreteBTFieldAlgebra (l:=k) (r:=n) (h_le:=h_k_le_n)
  @PowerBasis (ConcreteBTField k) (ConcreteBTField m) _ _ instLeftAlgebra =
  @PowerBasis (ConcreteBTField k) (ConcreteBTField n) _ _ instRightAlgebra
```

> The following two theorems are used to cast the basis of `ConcreteBTField α`
> to `ConcreteBTField β` via changing in index type : `Fin (i)` to `Fin (j)` when `α ≤ β`.

`ConcreteBinaryTower.Basis_cast_index_apply` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L61))

```lean
theorem Basis_cast_index_apply {α β i j : ℕ} {k : Fin j}
    (h_le : α ≤ β) (h_eq : i = j)
    {b : @Basis (Fin (i)) (ConcreteBTField α) (ConcreteBTField β) _ _
      (@ConcreteBTFieldAlgebra (l := α) (r := β) (h_le := h_le)).toModule} :
  let castBasis : @Basis (Fin j) (ConcreteBTField α) (ConcreteBTField β) _ _
    (@ConcreteBTFieldAlgebra (l:=α) (r:=β) (h_le:=h_le)).toModule :=
    cast (by exact Basis_cast_index_eq i j α β h_le h_eq) b
  (castBasis k) = b (Fin.cast (h_eq.symm) k)
```

`ConcreteBinaryTower.Basis_cast_dest_apply` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L73))

```lean
theorem Basis_cast_dest_apply {ι : Type*} (α β γ : ℕ)
    (h_le1 : α ≤ β) (h_le2 : α ≤ γ)
    (h_eq : β = γ) {k : ι} (b : @Basis ι (ConcreteBTField α) (ConcreteBTField β) _ _
    (@ConcreteBTFieldAlgebra (l := α) (r := β) (h_le := h_le1)).toModule) :
    let castBasis : @Basis ι (ConcreteBTField α) (ConcreteBTField γ) _ _
      (@ConcreteBTFieldAlgebra (l := α) (r := γ) (h_le := h_le2)).toModule :=
      cast (by
        exact Basis_cast_dest_eq α γ β h_le2 h_le1 h_eq
      ) b
    (castBasis k) = cast (by
      exact cast_ConcreteBTField_eq β γ h_eq) (b k)
```

`ConcreteBinaryTower.basisSucc` (definition, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L87))

```lean
def basisSucc (k : ℕ) : Basis (Fin 2) (ConcreteBTField k) (ConcreteBTField (k + 1))
```

> The power basis for `ConcreteBTField (k + 1)` over `ConcreteBTField k` is {1, Z (k + 1)}

`ConcreteBinaryTower.powerBasisSucc` (definition, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L167))

```lean
def powerBasisSucc (k : ℕ) :
    PowerBasis (ConcreteBTField k) (ConcreteBTField (k + 1))
```

`ConcreteBinaryTower.powerBasisSucc_gen` (lemma, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L179))

```lean
lemma powerBasisSucc_gen (k : ℕ) :
    (powerBasisSucc k).gen = (Z (k + 1))
```

`ConcreteBinaryTower.minPoly_of_powerBasisSucc_generator` (theorem, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L183))

```lean
theorem minPoly_of_powerBasisSucc_generator (k : ℕ) :
    (minpoly (ConcreteBTField k) (powerBasisSucc k).gen) = X^2 + (Z k) • X + 1
```

`ConcreteBinaryTower.powerBasisSucc_dim` (lemma, [line 270](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L270))

```lean
lemma powerBasisSucc_dim (k : ℕ) :
    powerBasisSucc (k:=k).dim = 2
```

`ConcreteBinaryTower.hli_level_diff_0` (definition, [line 274](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L274))

```lean
def hli_level_diff_0 (l : ℕ) :
    letI instAlgebra:= ConcreteBTFieldAlgebra (l:=l) (r:=l) (h_le:=by omega)
  @Basis (Fin 1) (ConcreteBTField l) (ConcreteBTField l) _ _ instAlgebra.toModule
```

`ConcreteBinaryTower.isScalarTower_succ_right` (definition, [line 307](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L307))

> Reducible Prop-valued helper for `letI` scalar-tower instances.

```lean
def isScalarTower_succ_right (l r : ℕ) (h_le : l ≤ r)
```

`ConcreteBinaryTower.multilinearBasis` (definition, [line 315](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L315))

> The multilinear basis for `ConcreteBTField τ` over `ConcreteBTField k`
> is the set of multilinear monomials in the tower generators `Z(k + 1), ..., Z(τ)`.
> This is done via scalar tower multiplication of power basis across adjacent levels.

```lean
def multilinearBasis (l r : ℕ) (h_le : l ≤ r) :
    letI instAlgebra := ConcreteBTFieldAlgebra (h_le:=h_le)
    Basis (Fin (2 ^ (r - l))) (ConcreteBTField l) (ConcreteBTField r)
```

`ConcreteBinaryTower.PowerBasis.dim_of_eq_rec` (theorem, [line 367](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L367))

```lean
theorem PowerBasis.dim_of_eq_rec
    (r1 r : ℕ)
    (h_r : r = r1 + 1)
    (b : PowerBasis (ConcreteBTField r1) (ConcreteBTField (r1 + 1))) :
    letI instAlgebra : Algebra (ConcreteBTField r1) (ConcreteBTField r) :=
      ConcreteBTFieldAlgebra (l:=r1) (r:=r) (h_le:=by omega)
    ((Eq.rec (motive:=fun (x : ℕ) (_ : r1 + 1 = x) => by
      letI instAlgebraCur : Algebra (ConcreteBTField r1) (ConcreteBTField x) :=
        ConcreteBTFieldAlgebra (l:=r1) (r:=x) (h_le:=by omega)
      exact PowerBasis (ConcreteBTField r1) (ConcreteBTField x)) (refl:=b) (t:=h_r.symm)) :
        PowerBasis (ConcreteBTField r1) (ConcreteBTField r)).dim
    = b.dim
```

`ConcreteBinaryTower.PowerBasis.cast_basis_succ_of_eq_rec_apply` (theorem, [line 383](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L383))

```lean
theorem PowerBasis.cast_basis_succ_of_eq_rec_apply
    (r1 r : ℕ) (h_r : r = r1 + 1)
    (k : Fin 2) :
    letI instAlgebra : Algebra (ConcreteBTField r1) (ConcreteBTField r) :=
      ConcreteBTFieldAlgebra (l:=r1) (r:=r) (h_le:=by omega)
    letI instAlgebraSucc : Algebra (ConcreteBTField (r1 + 1)) (ConcreteBTField (r)) :=
      ConcreteBTFieldAlgebra (l:=r1 + 1) (r:=r) (h_le:=by omega)
    let b : PowerBasis (ConcreteBTField r1) (ConcreteBTField (r1 + 1)) :=
      powerBasisSucc (k:=r1)
    let bCast : PowerBasis (ConcreteBTField r1) (ConcreteBTField r) := Eq.rec (motive:=
      fun (x : ℕ) (_ : r1 + 1 = x) => by
        letI instAlgebraCur : Algebra (ConcreteBTField r1) (ConcreteBTField x) :=
          ConcreteBTFieldAlgebra (l:=r1) (r:=x) (h_le:=by omega)
        exact PowerBasis (ConcreteBTField r1) (ConcreteBTField x)) (refl:=b) (t:=h_r.symm)
    have h_pb_dim : b.dim = 2 := by
      exact powerBasisSucc_dim r1

    have h_pb'_dim : bCast.dim = 2 := by
      dsimp [bCast]
      rw [PowerBasis.dim_of_eq_rec (r1:=r1) (r:=r) (h_r:=h_r) (b:=b)]
      exact h_pb_dim

    have h_pb_type_eq : Basis (Fin bCast.dim) (ConcreteBTField r1) (ConcreteBTField r) =
      Basis (Fin 2) (ConcreteBTField r1) (ConcreteBTField r) := by
      congr

   -- The `cast` needs a proof that `bCast.dim = 2`. We construct it here.
    let left : Basis (Fin 2) (ConcreteBTField r1) (ConcreteBTField r) :=
      cast (by exact h_pb_type_eq) bCast.basis
    let right := (algebraMap (ConcreteBTField (r1 + 1)) (ConcreteBTField r))
      (b.basis (Fin.cast h_pb_dim.symm k))
    left k = right
```

`ConcreteBinaryTower.coe_basis_apply` (theorem, [line 421](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L421))

```lean
theorem coe_basis_apply {R S : Type*} [CommRing R] [Ring S] [Algebra R S]
    (pb : PowerBasis R S) (i : Fin pb.dim) : ⇑pb.basis i = pb.gen ^ (i : ℕ)
```

`ConcreteBinaryTower.algebraMap_𝕏_eq_of_index_eq` (lemma, [line 426](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L426))

> When two indices are equal, the tower algebra maps send the respective 𝕏 to the same element.

```lean
lemma algebraMap_𝕏_eq_of_index_eq (r k m : ℕ) (h_k_le : k + 1 ≤ r) (h_m_le : m + 1 ≤ r)
    (h_eq : k = m) :
    letI := ConcreteBTFieldAlgebra (l := k + 1) (r := r) (h_le := h_k_le)
    letI := ConcreteBTFieldAlgebra (l := m + 1) (r := r) (h_le := h_m_le)
    (algebraMap _ _ (𝕏 k) : ConcreteBTField r) =
      (algebraMap _ _ (𝕏 m) : ConcreteBTField r)
```

> The basis element at index `j` is the product of the tower generators at
> the ON bits in binary representation of `j`.

`ConcreteBinaryTower.multilinearBasis_apply` (theorem, [line 439](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean#L439))

```lean
theorem multilinearBasis_apply (r : ℕ) : ∀ l : ℕ, (h_le : l ≤ r) → ∀ (j : Fin (2 ^ (r - l))),
    multilinearBasis (l:=l) (r:=r) (h_le:=h_le) j =
    (Finset.univ : Finset (Fin (r - l))).prod (fun i =>
      (ConcreteBTFieldAlgebra (l:=l + i + 1) (r:=r) (h_le:=by omega)).algebraMap (
        (𝕏 (l + i)) ^ (Nat.getBit i j)))
```

## Depends on

- [Concrete Binary Tower Algebra](algebra.md)
- [Binary Tower Fin Helpers](../support/finhelpers.md)

## Proof depends on

- [Binary Tower `Fin 2` Linear Independence](../support/linearindependentfin2.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Concrete/Basis.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Concrete/Basis.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Concrete.Basis.json)
