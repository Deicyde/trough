---
catalog: module
lean: BinaryTower.hli_level_diff_0, BinaryTower.BTField.isScalarTower_succ_right, BinaryTower.multilinearBasis, BinaryTower.BTField.PowerBasis.dim_of_eq_rec, BinaryTower.PowerBasis.cast_basis_succ_of_eq_rec_apply, BinaryTower.algebraMap_𝕏_eq_of_index_eq, BinaryTower.multilinearBasis_apply
statement: formalized
proof: formalized
---

# Abstract Binary Tower Basis

`CompPoly.Fields.Binary.Tower.Abstract.Basis`, in [CompPoly/Fields/Binary/Tower/Abstract/Basis.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Basis.lean), by Quang Dao, Chung Thai Nguyen.

> Basis constructions and index-casting lemmas for abstract binary tower extensions.

`BinaryTower.hli_level_diff_0` (definition, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Basis.lean#L27))

```lean
def hli_level_diff_0 (l : ℕ) :
    letI instAlgebra:= binaryAlgebraTower (l:=l) (r:=l) (h_le:=by omega)
  @Basis (Fin 1) (BTField l) (BTField l) _ _ instAlgebra.toModule
```

`BinaryTower.BTField.isScalarTower_succ_right` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Basis.lean#L59))

> Reducible Prop-valued helper for `letI` scalar-tower instances.

```lean
def BTField.isScalarTower_succ_right (l r : ℕ) (h_le : l ≤ r)
```

`BinaryTower.multilinearBasis` (definition, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Basis.lean#L68))

> The multilinear basis for `BTField τ` over `BTField k` is the set of multilinear monomials
> in the tower generators `Z(k+1), ..., Z(τ)`.
> This is done via scalar tower multiplication of power basis across adjacent levels.

```lean
def multilinearBasis (l r : ℕ) (h_le : l ≤ r) :
    letI instAlgebra : Algebra (BTField l) (BTField r) := binaryAlgebraTower (h_le:=h_le)
    Basis (Fin (2 ^ (r - l))) (BTField l) (BTField r)
```

`BinaryTower.BTField.PowerBasis.dim_of_eq_rec` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Basis.lean#L120))

```lean
theorem BTField.PowerBasis.dim_of_eq_rec
    (r1 r : ℕ)
    (h_r : r = r1 + 1)
    (b : PowerBasis (BTField r1) (BTField (r1 + 1))) :
    letI instAlgebra : Algebra (BTField r1) (BTField r) :=
      binaryAlgebraTower (l:=r1) (r:=r) (h_le:=by omega)
    ((Eq.rec (motive:=fun (x : ℕ) (_ : r1 + 1 = x) => by
      letI instAlgebraCur : Algebra (BTField r1) (BTField x) :=
        binaryAlgebraTower (l:=r1) (r:=x) (h_le:=by omega)
      exact PowerBasis (BTField r1) (BTField x)) (refl:=b) (t:=h_r.symm)) :
        PowerBasis (BTField r1) (BTField r)).dim
    = b.dim
```

`BinaryTower.PowerBasis.cast_basis_succ_of_eq_rec_apply` (theorem, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Basis.lean#L137))

```lean
theorem PowerBasis.cast_basis_succ_of_eq_rec_apply
    (r1 r : ℕ) (h_r : r = r1 + 1)
    (k : Fin 2) :
    letI instAlgebra : Algebra (BTField r1) (BTField r) :=
      binaryAlgebraTower (l:=r1) (r:=r) (h_le:=by omega)
    letI instAlgebraSucc : Algebra (BTField (r1 + 1)) (BTField (r)) :=
      binaryAlgebraTower (l:=r1 + 1) (r:=r) (h_le:=by omega)
    let b : PowerBasis (BTField r1) (BTField (r1 + 1)) := powerBasisSucc (k:=r1)
    let bCast : PowerBasis (BTField r1) (BTField r) := Eq.rec (motive:=
      fun (x : ℕ) (_ : r1 + 1 = x) => by
        letI instAlgebraCur : Algebra (BTField r1) (BTField x) :=
          binaryAlgebraTower (l:=r1) (r:=x) (h_le:=by omega)
        exact PowerBasis (BTField r1) (BTField x)) (refl:=b) (t:=h_r.symm)
    have h_pb_dim : b.dim = 2 := by
      exact powerBasisSucc_dim r1

    have h_pb'_dim : bCast.dim = 2 := by
      dsimp [bCast]
      erw [BTField.PowerBasis.dim_of_eq_rec (r1:=r1) (r:=r) (h_r:=h_r) (b:=b)]
      exact h_pb_dim

    have h_pb_type_eq : Basis (Fin bCast.dim) (BTField r1) (BTField r) =
      Basis (Fin 2) (BTField r1) (BTField r) := by
      congr

   -- The `cast` needs a proof that `bCast.dim = 2`. We construct it here.
    let left : Basis (Fin 2) (BTField r1) (BTField r) := cast (by exact h_pb_type_eq) bCast.basis
    let right := (algebraMap (BTField (r1 + 1)) (BTField r))
      (b.basis (Fin.cast h_pb_dim.symm k))
    left k = right
```

`BinaryTower.algebraMap_𝕏_eq_of_index_eq` (lemma, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Basis.lean#L179))

> When two indices are equal, the tower algebra maps send the respective 𝕏 to the same element.

```lean
lemma algebraMap_𝕏_eq_of_index_eq (r k m : ℕ) (h_k_le : k + 1 ≤ r) (h_m_le : m + 1 ≤ r)
    (h_eq : k = m) :
    letI := binaryAlgebraTower (l := k + 1) (r := r) (h_le := h_k_le)
    letI := binaryAlgebraTower (l := m + 1) (r := r) (h_le := h_m_le)
    (algebraMap _ _ (𝕏 k) : BTField r) = (algebraMap _ _ (𝕏 m) : BTField r)
```

> The basis element at index `j` is the product of the tower generators at
> the ON bits in binary representation of `j`.

`BinaryTower.multilinearBasis_apply` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Basis.lean#L193))

```lean
theorem multilinearBasis_apply (r : ℕ) : ∀ l : ℕ, (h_le : l ≤ r) → ∀ (j : Fin (2  ^ (r - l))),
    multilinearBasis (l:=l) (r:=r) (h_le:=h_le) j =
    (Finset.univ : Finset (Fin (r - l))).prod (fun i =>
      (binaryAlgebraTower (l:=l + i + 1) (r:=r) (h_le:=by omega)).algebraMap (
        (𝕏 (l + i)) ^ (Nat.getBit i j)))
```

## Depends on

- [Abstract Binary Tower Split](split.md)
- [Binary Tower Fin Helpers](../support/finhelpers.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Abstract/Basis.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Basis.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Abstract.Basis.json)
