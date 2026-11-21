---
catalog: module
lean: Vector.induction₂_temp, Vector.nil, Vector.cons, Vector.head_cons, Vector.cons_get_eq, Vector.cons_empty_tail_eq_nil, Vector.tail_cons, Vector.cons_toList_eq_List_cons, Vector.foldl_eq_toList_foldl, Vector.foldl_succ, Vector.zipWith_cons, Vector.dotProduct, Vector.accumulateProducts, Vector.reduce_accumulateProducts, Vector.reduce_accumulateProducts_zero, Vector.accumulateProducts_mul, Vector.dotProduct_cons, Vector.Matrix, Vector.Matrix.mulVec, Vector.Matrix.ofFlatten, Vector.Matrix.toFinMatrix, Vector.Matrix.ofFinMatrix, Vector.Matrix.transpose, dotProduct_cons, Vector.dotProduct_eq_root_dotProduct, Vector.map_dotProduct
statement: formalized
proof: formalized
---

# Definitions and lemmas for `Vector`

`CompPoly.Data.Vector.Basic`, in [CompPoly/Data/Vector/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean), by Quang Dao, Chung Thai Nguyen.

> `accumulateProducts` separates product accumulation from reduction. Its reduction theorem
> recovers `dotProduct` whenever reduction preserves zero, addition, and the chosen products.

`Vector.induction₂_temp` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L32))

```lean
def induction₂_temp {α β} {motive : {n : ℕ} → Vector α n → Vector β n → Sort*}
    (v_empty : motive #v[] #v[])
  (v_insert : {n : ℕ} → (hd : α) → (tl : Vector α n) → (hd' : β) → (tl' : Vector β n) →
      motive tl tl' → motive (tl.insertIdx 0 hd) (tl'.insertIdx 0 hd')) {m : ℕ} :
    (v : Vector α m) → (v' : Vector β m) → motive v v'
```

`Vector.nil` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L45))

> The empty vector.

```lean
def nil {α} : Vector α 0
```

`Vector.cons` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L49))

> Construct a vector by prepending an element to the front of a vector,
> using `insertIdx` at `0`.

```lean
def cons {α} {n : ℕ} (hd : α) (tl : Vector α n) : Vector α (n + 1)
```

`Vector.head_cons` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L53))

```lean
theorem head_cons {α} {n : ℕ} (hd : α) (tl : Vector α n) : (cons hd tl).head = hd
```

`Vector.cons_get_eq` (lemma, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L57))

```lean
lemma cons_get_eq {α} {n : ℕ} (hd : α) (tl : Vector α n) (i : Fin (n + 1)) :
    (cons hd tl).get i =
      if hi: i.val == 0 then hd else tl.get (⟨i.val - 1, by
        simp only [beq_iff_eq, Fin.val_eq_zero_iff] at hi
        apply Nat.sub_lt_left_of_lt_add
        · by_contra hi_ne_gt_1
          simp only [not_le, Nat.lt_one_iff, Fin.val_eq_zero_iff] at hi_ne_gt_1
          contradiction
        · have hi_lt:= i.isLt; omega
      ⟩)
```

`Vector.cons_empty_tail_eq_nil` (lemma, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L80))

```lean
lemma cons_empty_tail_eq_nil {α} (hd : α) (tl : Vector α 0) :
    cons hd tl = ⟨#[hd], rfl⟩
```

`Vector.tail_cons` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L92))

```lean
theorem tail_cons {α} {n : ℕ} (hd : α) (tl : Vector α n) : (cons hd tl).tail = tl
```

`Vector.cons_toList_eq_List_cons` (theorem, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L101))

```lean
theorem cons_toList_eq_List_cons {α} {n : ℕ} (hd : α) (tl : Vector α n) :
    (cons hd tl).toList = hd :: tl.toList
```

`Vector.foldl_eq_toList_foldl` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L107))

```lean
theorem foldl_eq_toList_foldl {α β} {n : ℕ} (f : β → α → β) (init : β) (v : Vector α n) :
    v.foldl (f:=f) (b:=init) = v.toList.foldl (f:=f) (init:=init)
```

`Vector.foldl_succ` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L113))

```lean
theorem foldl_succ
    {α β} {n : ℕ} [NeZero n] (f : β → α → β) (init : β) (v : Vector α n) :
    v.foldl (f:=f) (b:=init) = v.tail.foldl (f:=f) (b:=f init v.head)
```

`Vector.zipWith_cons` (theorem, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L127))

```lean
theorem zipWith_cons {α β γ} {n : ℕ} (f : α → β → γ)
    (a : α) (b : Vector α n) (c : β) (d : Vector β n) :
  zipWith f (cons a b) (cons c d) = cons (f a c) (zipWith f b d)
```

`Vector.dotProduct` (definition, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L140))

> Inner product between two vectors of the same size. Should be faster than `_root_.dotProduct`
> due to efficient operations on `Vector`s.

```lean
def dotProduct [Zero R] [Add R] [Mul R] (a b : Vector R n) : R
```

`Vector.accumulateProducts` (definition, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L148))

> Accumulate paired products from equal-length vectors, from left to right, starting at `init`.
> The products and accumulator lie in `W`; no reduction is performed.

```lean
def accumulateProducts {W : Type*} [Add W] (product : R → R → W) (init : W)
    (a b : Vector R n) : W
```

`Vector.reduce_accumulateProducts` (theorem, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L154))

> If reduction preserves addition and each paired product, reducing the accumulator gives
> the reduced initial value plus the dot product of the input vectors.

```lean
theorem reduce_accumulateProducts {W : Type*} [AddZero W] [AddMonoid R] [Mul R]
    (reduce : W →+ R) (product : R → R → W)
    (hproduct : ∀ x y, reduce (product x y) = x * y) (init : W) (a b : Vector R n) :
    reduce (accumulateProducts product init a b) = reduce init + dotProduct a b
```

`Vector.reduce_accumulateProducts_zero` (theorem, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L172))

> Reducing a product accumulator initialized at zero recovers the dot product.

```lean
theorem reduce_accumulateProducts_zero {W : Type*} [AddZero W] [AddMonoid R] [Mul R]
    (reduce : W →+ R) (product : R → R → W)
    (hproduct : ∀ x y, reduce (product x y) = x * y) (a b : Vector R n) :
    reduce (accumulateProducts product 0 a b) = dotProduct a b
```

`Vector.accumulateProducts_mul` (theorem, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L179))

> Ordinary multiplication is an eager product accumulator, with identity reduction.

```lean
theorem accumulateProducts_mul [AddMonoid R] [Mul R] (init : R) (a b : Vector R n) :
    accumulateProducts (· * ·) init a b = init + dotProduct a b
```

`Vector.dotProduct_cons` (lemma, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L184))

```lean
lemma dotProduct_cons [AddCommMonoid R] [Mul R] (a : R) (b : Vector R n) (c : R) (d : Vector R n) :
    dotProduct (cons a b) (cons c d) = a * c + dotProduct b d
```

`Vector.Matrix` (definition, [line 204](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L204))

> A matrix represented as iterated vectors in row-major order.
> `m` is the number of rows, and `n` is the number of columns

```lean
def Matrix (α : Type*) (m n : ℕ)
```

`Vector.Matrix.mulVec` (definition, [line 213](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L213))

> Matrix-vector multiplication over `α`.
> `M` is given as a vector of row-vectors.

```lean
def mulVec [Zero α] [Add α] [Mul α] {numRows numCols : Nat}
    (M : Vector (Vector α numCols) numRows)
  (x : Vector α numCols) : Vector α numRows
```

`Vector.Matrix.ofFlatten` (definition, [line 220](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L220))

> Convert a flat row-major vector of length `m*n` into an `m × n` row-major matrix
> represented as `Vector (Vector α n) m`.

```lean
def ofFlatten {m n : ℕ} (v : Vector α (m * n)) : Matrix α m n
```

`Vector.Matrix.toFinMatrix` (definition, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L232))

> Convert to a `Fin`-indexed matrix (the definition in Mathlib): `Fin m → Fin n → α`

```lean
def toFinMatrix {m n : ℕ} (matrix : Matrix α m n) : _root_.Matrix (Fin m) (Fin n) α
```

`Vector.Matrix.ofFinMatrix` (definition, [line 236](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L236))

> Convert from a `Fin`-indexed matrix (the definition in Mathlib): `Fin m → Fin n → α`

```lean
def ofFinMatrix {m n : ℕ} (matrix : _root_.Matrix (Fin m) (Fin n) α) : Matrix α m n
```

`Vector.Matrix.transpose` (definition, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L241))

> Transpose a matrix by swapping rows and columns.

```lean
def transpose {m n : ℕ} (matrix : Matrix α m n) : Matrix α n m
```

`dotProduct_cons` (lemma, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L255))

```lean
lemma dotProduct_cons (a : R) (b : Vector R n) (c : R) (d : Vector R n) :
    _root_.dotProduct (cons a b).get (cons c d).get = a * c + _root_.dotProduct b.get d.get
```

`Vector.dotProduct_eq_root_dotProduct` (theorem, [line 282](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L282))

```lean
theorem dotProduct_eq_root_dotProduct (a b : Vector R n) :
    dotProduct a b = _root_.dotProduct a.get b.get
```

`Vector.map_dotProduct` (theorem, [line 307](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean#L307))

> A ring homomorphism maps a dot product to the dot product of the mapped vectors.

```lean
theorem map_dotProduct {R S : Type*} [NonAssocSemiring R] [NonAssocSemiring S]
    (f : R →+* S) {n : ℕ} (a b : Vector R n) :
    f (dotProduct a b) = dotProduct (a.map f) (b.map f)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [Auxiliary lemmas for `List`](../list/lemmas.md)

## Sources

- [CompPoly/Data/Vector/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Vector/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Vector.Basic.json)
