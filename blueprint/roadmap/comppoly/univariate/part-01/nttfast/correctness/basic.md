---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Plan.WellFormed, CompPoly.CPolynomial.NTTFast.Plan.twiddlePowers_size, CompPoly.CPolynomial.NTTFast.Plan.twiddlePowers_getD_eq_pow, CompPoly.CPolynomial.NTTFast.Plan.twiddleTable_getD_eq_twiddlePowers, CompPoly.CPolynomial.NTTFast.Plan.ofDomain_wellFormed, CompPoly.CPolynomial.NTTFast.Plan.loadNaturalArray_eq, CompPoly.CPolynomial.NTTFast.Plan.foldl_range_eq_rec, CompPoly.CPolynomial.NTTFast.Plan.foldl_range_eq_rec_fst, CompPoly.CPolynomial.NTTFast.Plan.foldl_range_congr, CompPoly.CPolynomial.NTTFast.Plan.foldl_range_preserve, CompPoly.CPolynomial.NTTFast.Plan.foldl_range_congr_inv, CompPoly.CPolynomial.NTTFast.Plan.foldl_range'_succ_shift, CompPoly.CPolynomial.NTTFast.Plan.foldl_range'_eq_range_add, CompPoly.CPolynomial.NTTFast.Plan.foldl_range'_append_split, CompPoly.CPolynomial.NTTFast.Plan.three_mul_add_eq_add_two_mul_add, CompPoly.CPolynomial.NTTFast.Plan.foldl_commute, CompPoly.CPolynomial.NTTFast.Plan.foldl_commute_foldl, CompPoly.CPolynomial.NTTFast.Plan.foldl_pair, CompPoly.CPolynomial.NTTFast.Plan.foldl_range_pair, CompPoly.CPolynomial.NTTFast.Plan.foldl_quad, CompPoly.CPolynomial.NTTFast.Plan.butterflyDITBlocks_eq_foldl, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDITInner, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDITBlocks, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyStageWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDITRadix4Inner, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDITRadix4Blocks, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyRadix4StageWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDIFInner, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDIFBlocks, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyStageDIFWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDIFRadix4Inner, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDIFRadix4Blocks, CompPoly.CPolynomial.NTTFast.Plan.size_butterflyRadix4StageDIFWithTwiddles
statement: formalized
proof: formalized
---

# Basic NTTFast correctness facts

`CompPoly.Univariate.NTTFast.Correctness.Basic`, in [CompPoly/Univariate/NTTFast/Correctness/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean), by Valerii Huhnin.

> Cached-plan well-formedness, twiddle-table facts, and shared proof helpers for
> `NTTFast` correctness.

`CompPoly.CPolynomial.NTTFast.Plan.WellFormed` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L30))

> Well-formedness condition for cached plan data.

```lean
def WellFormed (P : Plan R) : Prop
```

`CompPoly.CPolynomial.NTTFast.Plan.twiddlePowers_size` (theorem, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L77))

> The cached twiddle powers for a stage have exactly one entry per butterfly offset.

```lean
theorem twiddlePowers_size (D : NTT.Domain R) (stage : Nat) :
    (twiddlePowers D stage).size = 2 ^ stage
```

`CompPoly.CPolynomial.NTTFast.Plan.twiddlePowers_getD_eq_pow` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L86))

> Entries of the cached twiddle powers are the corresponding powers of the stage root.

```lean
theorem twiddlePowers_getD_eq_pow (D : NTT.Domain R) (stage j : Nat)
    (hj : j < 2 ^ stage) :
    (twiddlePowers D stage).getD j 0 =
      (D.omega ^ (D.n / 2 ^ (stage + 1))) ^ j
```

`CompPoly.CPolynomial.NTTFast.Plan.twiddleTable_getD_eq_twiddlePowers` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L100))

> Looking up a valid stage in the twiddle table returns that stage's twiddle powers.

```lean
theorem twiddleTable_getD_eq_twiddlePowers
    (D : NTT.Domain R) (stage : Nat) (hstage : stage < D.logN) :
    (twiddleTable D).getD stage #[] = twiddlePowers D stage
```

`CompPoly.CPolynomial.NTTFast.Plan.ofDomain_wellFormed` (theorem, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L106))

> A plan built directly from a domain has well-formed cached data.

```lean
theorem ofDomain_wellFormed (D : NTT.Domain R) :
    WellFormed (ofDomain D)
```

`CompPoly.CPolynomial.NTTFast.Plan.loadNaturalArray_eq` (theorem, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L111))

> Loading raw coefficients into a domain-sized array is `Array.ofFn` with zero padding.

```lean
theorem loadNaturalArray_eq (D : NTT.Domain R) (a : Array R) :
    NTT.loadNaturalArray D a = Array.ofFn (fun i : D.Idx ↦ a.getD i.1 0)
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_range_eq_rec` (theorem, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L116))

> Folding over `List.range` is equivalent to the corresponding natural recursion.

```lean
theorem foldl_range_eq_rec {α : Type*} (f : Nat → α → α) (x : α) :
    ∀ n : Nat,
      List.foldl (fun acc i ↦ f i acc) x (List.range n) = Nat.rec x (fun i acc ↦ f i acc) n
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_range_eq_rec_fst` (theorem, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L124))

> First projections of pair-valued folds over `List.range` match natural recursion.

```lean
theorem foldl_range_eq_rec_fst {α β : Type*}
    (f : Nat → α × β → α × β) (x : α × β) (n : Nat) :
    (List.foldl (fun acc i ↦ f i acc) x (List.range n)).1 =
      (Nat.rec (motive := fun _ ↦ α × β) x (fun i acc ↦ f i acc) n).1
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_range_congr` (theorem, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L134))

> Two fold functions give the same range fold when they agree at every step.

```lean
theorem foldl_range_congr {α : Type*} (f g : α → Nat → α) :
    ∀ n : Nat,
      (∀ i, i < n → ∀ acc, f acc i = g acc i) →
      ∀ acc, List.foldl f acc (List.range n) = List.foldl g acc (List.range n)
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_range_preserve` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L147))

> A property preserved by every step is preserved by folding over `List.range`.

```lean
theorem foldl_range_preserve {α : Type*} (p : α → Prop) (f : α → Nat → α) :
    ∀ n : Nat,
      (∀ i, i < n → ∀ acc, p acc → p (f acc i)) →
      ∀ acc, p acc → p (List.foldl f acc (List.range n))
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_range_congr_inv` (theorem, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L161))

> Congruence for range folds under an invariant preserved by the left fold.

```lean
theorem foldl_range_congr_inv {α : Type*} (p : α → Prop) (f g : α → Nat → α) :
    ∀ n : Nat,
      (∀ i, i < n → ∀ acc, p acc → f acc i = g acc i) →
      (∀ i, i < n → ∀ acc, p acc → p (f acc i)) →
      ∀ acc, p acc → List.foldl f acc (List.range n) = List.foldl g acc (List.range n)
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_range'_succ_shift` (theorem, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L182))

> Shift a `List.range'` fold by one when the folded function shifts its index.

```lean
theorem foldl_range'_succ_shift {α : Type*} (f : Nat → α → α) :
    ∀ n offset (acc : α),
      List.foldl (fun acc t ↦ f (t + 1) acc) acc (List.range' offset n) =
        List.foldl (fun acc t ↦ f t acc) acc (List.range' (offset + 1) n)
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_range'_eq_range_add` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L193))

> Reindex a `List.range'` fold as a fold over `List.range` with an offset.

```lean
theorem foldl_range'_eq_range_add {α : Type*} (f : Nat → α → α)
    (n offset : Nat) (acc : α) :
    List.foldl (fun acc t ↦ f t acc) acc (List.range' offset n) =
      List.foldl (fun acc t ↦ f (offset + t) acc) acc (List.range n)
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_range'_append_split` (theorem, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L200))

> Split a `List.range'` fold over an appended interval into two folds.

```lean
theorem foldl_range'_append_split {α : Type*} (f : α → Nat → α)
    (acc : α) (s m n : Nat) :
    List.foldl f acc (List.range' s (m + n)) =
      List.foldl f (List.foldl f acc (List.range' s m)) (List.range' (s + m) n)
```

`CompPoly.CPolynomial.NTTFast.Plan.three_mul_add_eq_add_two_mul_add` (theorem, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L210))

> Arithmetic normal form used when rearranging adjacent radix-4 block indices.

```lean
theorem three_mul_add_eq_add_two_mul_add (q b : Nat) :
    3 * q + b = q + (2 * q + b)
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_commute` (theorem, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L215))

> Move an operation through a range fold when it commutes with every step.

```lean
theorem foldl_commute {α : Type*} (op : α → α) (f : Nat → α → α) :
    ∀ n : Nat,
      (∀ i, i < n → ∀ x, op (f i x) = f i (op x)) →
      ∀ x, op (List.foldl (fun x i ↦ f i x) x (List.range n)) =
        List.foldl (fun x i ↦ f i x) (op x) (List.range n)
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_commute_foldl` (theorem, [line 229](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L229))

> Swap two range folds when every step of one commutes with every step of the other.

```lean
theorem foldl_commute_foldl {α : Type*} (f g : Nat → α → α) (m n : Nat)
    (hcomm : ∀ i j, i < m → j < n → ∀ x, g j (f i x) = f i (g j x)) :
    ∀ x,
      List.foldl (fun x i ↦ f i x) (List.foldl (fun x j ↦ g j x) x (List.range n))
          (List.range m) =
        List.foldl (fun x j ↦ g j x) (List.foldl (fun x i ↦ f i x) x (List.range m))
          (List.range n)
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_pair` (theorem, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L246))

> Split a fold of paired same-index operations into two separate range folds.

```lean
theorem foldl_pair {α : Type*} (f g : Nat → α → α) :
    ∀ n : Nat,
      (∀ i j, i < j → j < n → ∀ x, f j (g i x) = g i (f j x)) →
      ∀ x,
        List.foldl (fun x i ↦ g i (f i x)) x (List.range n) =
          List.foldl (fun x i ↦ g i x)
            (List.foldl (fun x i ↦ f i x) x (List.range n)) (List.range n)
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_range_pair` (theorem, [line 265](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L265))

> Fold a pair of consecutive indexed operations as one fold over twice the range.

```lean
theorem foldl_range_pair {α : Type*} (f : Nat → α → α) :
    ∀ n (acc : α),
      List.foldl (fun acc b ↦ f (2 * b + 1) (f (2 * b) acc)) acc (List.range n) =
        List.foldl (fun acc k ↦ f k acc) acc (List.range (2 * n))
```

`CompPoly.CPolynomial.NTTFast.Plan.foldl_quad` (theorem, [line 282](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L282))

> Split a fold of four same-index operations into four separate range folds.

```lean
theorem foldl_quad {α : Type*} (l₁ l₂ h₁ h₂ : Nat → α → α) :
    ∀ n : Nat,
      (∀ i j, i < j → j < n → ∀ x, l₁ j (l₂ i x) = l₂ i (l₁ j x)) →
      (∀ i j, i < j → j < n → ∀ x, l₁ j (h₁ i x) = h₁ i (l₁ j x)) →
      (∀ i j, i < j → j < n → ∀ x, l₁ j (h₂ i x) = h₂ i (l₁ j x)) →
      (∀ i j, i < j → j < n → ∀ x, l₂ j (h₁ i x) = h₁ i (l₂ j x)) →
      (∀ i j, i < j → j < n → ∀ x, l₂ j (h₂ i x) = h₂ i (l₂ j x)) →
      (∀ i j, i < j → j < n → ∀ x, h₁ j (h₂ i x) = h₂ i (h₁ j x)) →
      ∀ x,
        List.foldl (fun x i ↦ h₂ i (h₁ i (l₂ i (l₁ i x)))) x (List.range n) =
          List.foldl (fun x i ↦ h₂ i x)
            (List.foldl (fun x i ↦ h₁ i x)
              (List.foldl (fun x i ↦ l₂ i x)
                (List.foldl (fun x i ↦ l₁ i x) x (List.range n)) (List.range n))
              (List.range n))
            (List.range n)
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDITBlocks_eq_foldl` (theorem, [line 385](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L385))

> Express the recursive DIT block loop as a fold over baseline NTT block steps.

```lean
theorem butterflyDITBlocks_eq_foldl
    (twiddles : Array R) (blockSize half : Nat) (wm : R)
    (htwiddles : ∀ j, j < half → twiddles.getD j 0 = wm ^ j) :
    ∀ n blocks block (acc : Array R),
      blocks = block + n →
      butterflyDITBlocks twiddles blockSize half blocks block acc =
        List.foldl (fun acc block ↦ NTT.Transform.butterflyBlockStep blockSize half wm block acc)
          acc (List.range' block n)
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDITInner` (theorem, [line 408](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L408))

```lean
theorem size_butterflyDITInner
    (twiddles : Array R) (limit j i0 i1 : Nat) :
    ∀ acc : Array R, (butterflyDITInner twiddles limit j i0 i1 acc).size = acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDITBlocks` (theorem, [line 425](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L425))

```lean
theorem size_butterflyDITBlocks
    (twiddles : Array R) (blockSize half blocks block : Nat) :
    ∀ acc : Array R,
      (butterflyDITBlocks twiddles blockSize half blocks block acc).size = acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyStageWithTwiddles` (theorem, [line 443](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L443))

```lean
theorem size_butterflyStageWithTwiddles
    (D : NTT.Domain R) (stage : Nat) (twiddles a : Array R) :
    (butterflyStageWithTwiddles D stage twiddles a).size = a.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDITRadix4Inner` (theorem, [line 448](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L448))

```lean
theorem size_butterflyDITRadix4Inner
    (twiddlesLow twiddlesHigh : Array R) (limit j i0 i1 i2 i3 : Nat) :
    ∀ acc : Array R,
      (butterflyDITRadix4Inner twiddlesLow twiddlesHigh limit j i0 i1 i2 i3 acc).size =
        acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDITRadix4Blocks` (theorem, [line 467](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L467))

```lean
theorem size_butterflyDITRadix4Blocks
    (twiddlesLow twiddlesHigh : Array R) (blockSize quarter blocks block : Nat) :
    ∀ acc : Array R,
      (butterflyDITRadix4Blocks twiddlesLow twiddlesHigh blockSize quarter blocks block acc).size =
        acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyRadix4StageWithTwiddles` (theorem, [line 486](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L486))

```lean
theorem size_butterflyRadix4StageWithTwiddles
    (D : NTT.Domain R) (lowStage : Nat) (twiddlesLow twiddlesHigh a : Array R) :
    (butterflyRadix4StageWithTwiddles D lowStage twiddlesLow twiddlesHigh a).size =
      a.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDIFInner` (theorem, [line 492](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L492))

```lean
theorem size_butterflyDIFInner
    (twiddles : Array R) (limit j i0 i1 : Nat) :
    ∀ acc : Array R, (butterflyDIFInner twiddles limit j i0 i1 acc).size = acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDIFBlocks` (theorem, [line 509](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L509))

```lean
theorem size_butterflyDIFBlocks
    (twiddles : Array R) (blockSize half blocks block : Nat) :
    ∀ acc : Array R,
      (butterflyDIFBlocks twiddles blockSize half blocks block acc).size = acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyStageDIFWithTwiddles` (theorem, [line 527](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L527))

```lean
theorem size_butterflyStageDIFWithTwiddles
    (D : NTT.Domain R) (stage : Nat) (twiddles a : Array R) :
    (butterflyStageDIFWithTwiddles D stage twiddles a).size = a.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDIFRadix4Inner` (theorem, [line 532](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L532))

```lean
theorem size_butterflyDIFRadix4Inner
    (twiddlesHigh twiddlesLow : Array R) (limit j i0 i1 i2 i3 : Nat) :
    ∀ acc : Array R,
      (butterflyDIFRadix4Inner twiddlesHigh twiddlesLow limit j i0 i1 i2 i3 acc).size =
        acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyDIFRadix4Blocks` (theorem, [line 551](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L551))

```lean
theorem size_butterflyDIFRadix4Blocks
    (twiddlesHigh twiddlesLow : Array R) (blockSize quarter blocks block : Nat) :
    ∀ acc : Array R,
      (butterflyDIFRadix4Blocks twiddlesHigh twiddlesLow blockSize quarter blocks block acc).size =
        acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.size_butterflyRadix4StageDIFWithTwiddles` (theorem, [line 570](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean#L570))

```lean
theorem size_butterflyRadix4StageDIFWithTwiddles
    (D : NTT.Domain R) (lowStage : Nat) (twiddlesHigh twiddlesLow a : Array R) :
    (butterflyRadix4StageDIFWithTwiddles D lowStage twiddlesHigh twiddlesLow a).size =
      a.size
```

## Depends on

- [Planned NTTFast multiplication](../plan.md)

## Sources

- [CompPoly/Univariate/NTTFast/Correctness/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Basic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Correctness.Basic.json)
