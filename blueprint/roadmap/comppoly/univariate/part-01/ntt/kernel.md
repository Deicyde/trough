---
catalog: module
lean: CompPoly.CPolynomial.NTT.omegaInv_pow_mul_eq, CompPoly.CPolynomial.NTT.kernel_term_eq, CompPoly.CPolynomial.NTT.omega_sum_pow_mul_eq_if_dvd, CompPoly.CPolynomial.NTT.dvd_add_sub_iff_fin_eq, CompPoly.CPolynomial.NTT.kernel_sum_eq_if, CompPoly.CPolynomial.NTT.kernel_sum_forward_inverse_eq_if
statement: formalized
proof: formalized
---

# NTT Kernel Identities

`CompPoly.Univariate.NTT.Kernel`, in [CompPoly/Univariate/NTT/Kernel.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Kernel.lean), by Salih Erdem Koçak, Doran Pamukçu, Valerii Huhnin.

> Shared root-of-unity orthogonality lemmas used by NTT evaluation,
> interpolation, and multiplication proofs.

`CompPoly.CPolynomial.NTT.omegaInv_pow_mul_eq` (theorem, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Kernel.lean#L29))

> Rewrite powers of the inverse root as powers of the forward root.

```lean
theorem omegaInv_pow_mul_eq (D : Domain R) {i : Nat} (hi : i < D.n) (k : Nat) :
    D.omegaInv ^ (i * k) = D.omega ^ ((D.n - i) * k)
```

`CompPoly.CPolynomial.NTT.kernel_term_eq` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Kernel.lean#L43))

> Combine a forward-kernel term with an inverse-kernel term.

```lean
theorem kernel_term_eq (D : Domain R) {i : Nat} (hi : i < D.n) (j k : Nat) :
    D.omega ^ (k * j) * D.omegaInv ^ (i * k) =
      D.omega ^ ((j + (D.n - i)) * k)
```

`CompPoly.CPolynomial.NTT.omega_sum_pow_mul_eq_if_dvd` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Kernel.lean#L52))

> Sum of powers over the NTT domain, expressed by divisibility of the exponent.

```lean
theorem omega_sum_pow_mul_eq_if_dvd (D : Domain R) (m : Nat) :
    (∑ k : D.Idx, D.omega ^ (m * (k : Nat))) = if D.n ∣ m then (D.n : R) else 0
```

`CompPoly.CPolynomial.NTT.dvd_add_sub_iff_fin_eq` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Kernel.lean#L87))

> The kernel divisibility condition is equivalent to equality of domain indices.

```lean
theorem dvd_add_sub_iff_fin_eq (D : Domain R) (i j : D.Idx) :
    D.n ∣ (j.1 + (D.n - i.1)) ↔ j = i
```

`CompPoly.CPolynomial.NTT.kernel_sum_eq_if` (theorem, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Kernel.lean#L111))

> Orthogonality of the forward/inverse NTT kernels over the domain.

```lean
theorem kernel_sum_eq_if (D : Domain R) (i j : D.Idx) :
    (∑ k : D.Idx, D.omega ^ ((k : Nat) * (j : Nat)) *
        D.omegaInv ^ ((i : Nat) * (k : Nat))) =
      if j = i then (D.n : R) else 0
```

`CompPoly.CPolynomial.NTT.kernel_sum_forward_inverse_eq_if` (theorem, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Kernel.lean#L130))

> Orthogonality of the inverse/forward NTT kernels over the domain.

```lean
theorem kernel_sum_forward_inverse_eq_if (D : Domain R) (i j : D.Idx) :
    (∑ k : D.Idx, D.omegaInv ^ ((k : Nat) * (j : Nat)) *
        D.omega ^ ((i : Nat) * (k : Nat))) =
      if j = i then (D.n : R) else 0
```

## Depends on

- [NTT Domain](domain.md)

## Sources

- [CompPoly/Univariate/NTT/Kernel.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Kernel.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.Kernel.json)
