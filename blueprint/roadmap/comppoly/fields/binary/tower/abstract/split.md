---
catalog: module
lean: BinaryTower.BTField.Basis_cast_index_eq, BinaryTower.BTField.Basis_cast_dest_eq, BinaryTower.BTField.PowerBasis_cast_dest_eq, BinaryTower.BTField.Basis_cast_index_apply, BinaryTower.BTField.Basis_cast_dest_apply, BinaryTower.powerBasisSucc, BinaryTower.powerBasisSucc_gen, BinaryTower.powerBasisSucc_dim, BinaryTower.join_via_add_smul, BinaryTower.join_via_add_smul_zero, BinaryTower.join_via_add_smul_one_zero_eq_Z, BinaryTower.join_via_add_smul_one, BinaryTower.sum_join_via_add_smul, BinaryTower.mul_join_via_add_smul, BinaryTower.unique_linear_decomposition_succ, BinaryTower.split, BinaryTower.eq_join_via_add_smul_eq_iff_split, BinaryTower.split_join_via_add_smul_eq_iff_split, BinaryTower.join_eq_join_iff, BinaryTower.split_algebraMap_eq_zero_x, BinaryTower.algebraMap_succ_eq_zero_x, BinaryTower.algebraMap_eq_zero_x, BinaryTower.minPoly_of_powerBasisSucc_generator
statement: formalized
proof: formalized
---

# Abstract Binary Tower Split

`CompPoly.Fields.Binary.Tower.Abstract.Split`, in [CompPoly/Fields/Binary/Tower/Abstract/Split.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean), by Quang Dao, Chung Thai Nguyen.

> Splitting and recombination lemmas for abstract binary tower extensions.

`BinaryTower.BTField.Basis_cast_index_eq` (theorem, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L27))

```lean
theorem BTField.Basis_cast_index_eq (i j k n : ℕ) (h_le : k ≤ n) (h_eq : i = j) :
    letI instAlgebra : Algebra (BTField k) (BTField n) :=
      binaryAlgebraTower (l:=k) (r:=n) (h_le:=h_le)
    letI : Module (BTField k) (BTField n) := instAlgebra.toModule
    (Basis (Fin (i)) (BTField k) (BTField n)) = (Basis (Fin (j)) (BTField k) (BTField n))
```

`BinaryTower.BTField.Basis_cast_dest_eq` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L35))

```lean
theorem BTField.Basis_cast_dest_eq {ι : Type*} (k n m : ℕ) (h_k_le_n : k ≤ n)
    (h_k_le_m : k ≤ m) (h_eq : m = n) :
  letI instLeftAlgebra := binaryAlgebraTower (l:=k) (r:=m) (h_le:=h_k_le_m)
  letI instRightAlgebra := binaryAlgebraTower (l:=k) (r:=n) (h_le:=h_k_le_n)
  @Basis ι (BTField k) (BTField m) _ _ instLeftAlgebra.toModule =
  @Basis ι (BTField k) (BTField n) _ _ instRightAlgebra.toModule
```

`BinaryTower.BTField.PowerBasis_cast_dest_eq` (theorem, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L44))

```lean
theorem BTField.PowerBasis_cast_dest_eq (k n m : ℕ) (h_k_le_n : k ≤ n)
    (h_k_le_m : k ≤ m) (h_eq : m = n) :
  letI instLeftAlgebra := binaryAlgebraTower (l:=k) (r:=m) (h_le:=h_k_le_m)
  letI instRightAlgebra := binaryAlgebraTower (l:=k) (r:=n) (h_le:=h_k_le_n)
  @PowerBasis (BTField k) (BTField m) _ _ instLeftAlgebra =
  @PowerBasis (BTField k) (BTField n) _ _ instRightAlgebra
```

> The following two theorems are used to cast the basis of `BTField α` to `BTField β`
> via changing in index type : `Fin (i)` to `Fin (j)` when `α ≤ β`.

`BinaryTower.BTField.Basis_cast_index_apply` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L57))

```lean
theorem BTField.Basis_cast_index_apply {α β i j : ℕ} {k : Fin j} (h_le : α ≤ β) (h_eq : i = j)
    {b : @Basis (Fin (i)) (BTField α) (BTField β) _ _
    (@binaryAlgebraTower (l := α) (r := β) (h_le := h_le)).toModule} :
  let castBasis : @Basis (Fin j) (BTField α) (BTField β) _ _
    (@binaryAlgebraTower (l:=α) (r:=β) (h_le:=h_le)).toModule :=
    cast (by exact BTField.Basis_cast_index_eq i j α β h_le h_eq) b
  (castBasis k) = b (Fin.cast (h_eq.symm) k)
```

`BinaryTower.BTField.Basis_cast_dest_apply` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L68))

```lean
theorem BTField.Basis_cast_dest_apply {ι : Type*} (α β γ : ℕ) (h_le1 : α ≤ β) (h_le2 : α ≤ γ)
    (h_eq : β = γ) {k : ι} (b : @Basis ι (BTField α) (BTField β) _ _
    (@binaryAlgebraTower (l := α) (r := β) (h_le := h_le1)).toModule) :
    let castBasis : @Basis ι (BTField α) (BTField γ) _ _
      (@binaryAlgebraTower (l := α) (r := γ) (h_le := h_le2)).toModule :=
      cast (by
        exact Basis_cast_dest_eq α γ β h_le2 h_le1 h_eq
      ) b
    (castBasis k) = cast (by exact BTField.cast_BTField_eq β γ h_eq) (b k)
```

> The power basis for `BTField (k+1)` over `BTField k` is {1, Z (k+1)}

`BinaryTower.powerBasisSucc` (definition, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L83))

```lean
def powerBasisSucc (k : ℕ) :
    PowerBasis (BTField k) (BTField (k+1))
```

`BinaryTower.powerBasisSucc_gen` (lemma, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L93))

```lean
lemma powerBasisSucc_gen (k : ℕ) :
    (powerBasisSucc k).gen = (Z (k+1))
```

`BinaryTower.powerBasisSucc_dim` (lemma, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L99))

```lean
lemma powerBasisSucc_dim (k : ℕ) :
    powerBasisSucc (k:=k).dim = 2
```

`BinaryTower.join_via_add_smul` (definition, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L104))

```lean
def join_via_add_smul {k : ℕ} (h_pos : k > 0) (hi_btf lo_btf : BTField (k - 1)) :
    BTField k
```

`BinaryTower.join_via_add_smul_zero` (lemma, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L111))

```lean
lemma join_via_add_smul_zero {k : ℕ} (h_pos : k > 0) :
    (⋘ 0, 0 ⋙ : BTField k) = 0
```

`BinaryTower.join_via_add_smul_one_zero_eq_Z` (lemma, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L118))

```lean
lemma join_via_add_smul_one_zero_eq_Z {k : ℕ} (h_pos : k > 0) :
    ⋘ 1, 0 ⋙ = Z k
```

`BinaryTower.join_via_add_smul_one` (lemma, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L124))

```lean
lemma join_via_add_smul_one {k : ℕ} (h_pos : k > 0) :
    (⋘ 0, 1 ⋙ : BTField k) = 1
```

`BinaryTower.sum_join_via_add_smul` (theorem, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L130))

```lean
theorem sum_join_via_add_smul (k : ℕ) (h_pos : k > 0) (a₁ a₀ b₁ b₀ : BTField (k - 1)) :
    ⋘ a₁, a₀ ⋙ + ⋘ b₁, b₀ ⋙ = ⋘ a₁ + b₁, a₀ + b₀ ⋙
```

`BinaryTower.mul_join_via_add_smul` (theorem, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L144))

> (a₁ • Z k + a₀) * (b₁ • Z k + b₀)
> = a₁ * b₁ • (Z k)^2 + (a₁ * b₀ + a₀ * b₁) • Z k + a₀ * b₀
> = a₁ * b₁ • (Z (k-1) * Z k + 1) + (a₁ * b₀ + a₀ * b₁) • Z k + a₀ * b₀
> = [a₁ * b₁ * Z (k - 1) + a₁ * b₀ + a₀ * b₁] * (Z k) + (a₀ * b₀ + a₁ * b₁)

```lean
theorem mul_join_via_add_smul (k : ℕ) (h_pos : k > 0) (a₁ a₀ b₁ b₀ : BTField (k - 1)) :
    ⋘ a₁, a₀ ⋙ * ⋘ b₁, b₀ ⋙ = ⋘ a₁ * b₁ * Z (k - 1) + a₁ * b₀ + a₀ * b₁, a₀ * b₀ + a₁ * b₁ ⋙
```

`BinaryTower.unique_linear_decomposition_succ` (theorem, [line 194](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L194))

```lean
theorem unique_linear_decomposition_succ (k : ℕ) :
    ∀ (x : BTField (k+1)), ∃! (p : BTField k × BTField k),
    x = ⋘ p.1, p.2 ⋙
```

`BinaryTower.split` (definition, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L227))

```lean
def split (k : ℕ) (h_k : k > 0) (x : BTField k) : BTField (k-1) × BTField (k-1)
```

> Proofs that `split` is the inverse of `join_via_add_smul`

`BinaryTower.eq_join_via_add_smul_eq_iff_split` (theorem, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L237))

```lean
theorem eq_join_via_add_smul_eq_iff_split (k : ℕ) (h_pos : k > 0)
    (x : BTField k) (hi_btf lo_btf : BTField (k - 1)) :
    x = ⋘ hi_btf, lo_btf ⋙ ↔
  split (k:=k) (h_k:=h_pos) x = (hi_btf, lo_btf)
```

`BinaryTower.split_join_via_add_smul_eq_iff_split` (lemma, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L276))

```lean
lemma split_join_via_add_smul_eq_iff_split (k : ℕ) (h_pos : k > 0)
    (hi_btf lo_btf : BTField (k - 1)) :
    split (k:=k) (h_k:=h_pos) (⋘ hi_btf, lo_btf ⋙) = (hi_btf, lo_btf)
```

`BinaryTower.join_eq_join_iff` (lemma, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L281))

```lean
lemma join_eq_join_iff (k : ℕ) (h_pos : k > 0) (hi₁ hi₀ lo₁ lo₀ : BTField (k - 1)) :
    ⋘ hi₁, lo₁ ⋙ = ⋘ hi₀, lo₀ ⋙ ↔
  hi₁ = hi₀ ∧ lo₁ = lo₀
```

`BinaryTower.split_algebraMap_eq_zero_x` (lemma, [line 297](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L297))

> An element `x` lifted from the base field `BTField (k-1)` has `(0, x)` as its
> split representation in `BTField k`.

```lean
lemma split_algebraMap_eq_zero_x {k : ℕ} (h_pos : k > 0) (x : BTField (k - 1)) :
    letI instAlgebra := binaryAlgebraTower (l:=k-1) (r:=k) (h_le:=by omega)
  split (k:=k) (h_k:=h_pos) (algebraMap (BTField (k - 1)) (BTField k) x) = (0, x)
```

`BinaryTower.algebraMap_succ_eq_zero_x` (lemma, [line 338](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L338))

```lean
lemma algebraMap_succ_eq_zero_x {k : ℕ} (h_pos : k > 0) (x : BTField (k - 1)) :
    letI instAlgebra := binaryAlgebraTower (l:=k-1) (r:=k) (h_le:=by omega)
  algebraMap (BTField (k - 1)) (BTField k) x = ⋘ 0, x ⋙
```

`BinaryTower.algebraMap_eq_zero_x` (lemma, [line 347](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L347))

```lean
lemma algebraMap_eq_zero_x {i j : ℕ} (h_le : i < j) (x : BTField i) :
    letI instAlgebra := binaryAlgebraTower (l:=i) (r:=j) (h_le:=by omega)
    letI instAlgebraPred := binaryAlgebraTower (l:=i) (r:=j-1) (h_le:=by omega)
    algebraMap (BTField i) (BTField j) x
      = ⋘ 0, algebraMap (BTField i) (BTField (j-1)) x ⋙
```

`BinaryTower.minPoly_of_powerBasisSucc_generator` (theorem, [line 372](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean#L372))

```lean
theorem minPoly_of_powerBasisSucc_generator (k : ℕ) :
    (minpoly (BTField k) (powerBasisSucc k).gen) = X^2 + (Z k) • X + 1
```

## Depends on

- [Abstract Binary Tower Algebra](algebra.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Abstract/Split.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Abstract/Split.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Abstract.Split.json)
