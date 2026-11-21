---
catalog: module
lean: bit_finProdFinEquiv_symm_2_pow_succ, leftDivNat, leftModNat, revFinProdFinEquiv, bit_revFinProdFinEquiv_symm_2_pow_succ
statement: formalized
proof: formalized
---

# Binary Tower Fin Helpers

`CompPoly.Fields.Binary.Tower.Support.FinHelpers`, in [CompPoly/Fields/Binary/Tower/Support/FinHelpers.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/FinHelpers.lean), by Quang Dao, Chung Thai Nguyen.

> Finite-index helper lemmas for bit manipulations used in binary tower proofs.

`bit_finProdFinEquiv_symm_2_pow_succ` (theorem, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/FinHelpers.lean#L25))

```lean
theorem bit_finProdFinEquiv_symm_2_pow_succ {n : ℕ} (j : Fin (2 ^ (n + 1))) (i : Fin (n + 1)) :
    let e := (finProdFinEquiv (m := 2 ^ n) (n := 2)).symm
    let j' : Fin (2 ^ n * 2) := Fin.cast (Nat.pow_succ 2 n) j
    Nat.getBit (i) j = if i.val > 0 then Nat.getBit (i.val-1) (e j').1 else (e j').2
```

`leftDivNat` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/FinHelpers.lean#L49))

> Equivalence between `Fin m × Fin n` and `Fin (m * n)`
> which splits quotient part into Fin (n) and the remainder into Fin (m).
> If m and n are powers of 2, the Fin (n) holds MSBs and Fin (m) holds LSBs.
> This is a reversed version of `finProdFinEquiv`.
> We put `m` before `n` for integration with `Basis.smulTower` in `multilinearBasis`
> though it's a bit counter-intuitive.

```lean
def leftDivNat {m n : ℕ} (i : Fin (m * n)) : Fin n
```

`leftModNat` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/FinHelpers.lean#L54))

```lean
def leftModNat {m n : ℕ} (h_m : m > 0) (i : Fin (m * n)) : Fin m
```

`revFinProdFinEquiv` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/FinHelpers.lean#L60))

```lean
def revFinProdFinEquiv {m n : ℕ} (h_m : m > 0) : Fin m × Fin n ≃ Fin (m * n)
```

`bit_revFinProdFinEquiv_symm_2_pow_succ` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/FinHelpers.lean#L89))

```lean
theorem bit_revFinProdFinEquiv_symm_2_pow_succ {n : ℕ} (j : Fin (2 ^ (n + 1))) (i : Fin (n + 1)) :
    let e : Fin (2 ^ n * 2) ≃ Fin (2 ^ n) × Fin 2 :=
      (revFinProdFinEquiv (m := 2 ^ n) (n := 2) (h_m := Nat.two_pow_pos n)).symm
    let j' : Fin (2 ^ n * 2) := Fin.cast (Nat.pow_succ 2 n) j
    let msb : Fin 2 := (e j').2
    let lsbs : Fin (2 ^ n) := (e j').1
    Nat.getBit (i) j = if i.val < n then Nat.getBit (i.val) lsbs else msb
```

## Depends on

- [Bit operations on natural numbers](../../../../data/nat/bitwise.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Support/FinHelpers.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/FinHelpers.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Support.FinHelpers.json)
