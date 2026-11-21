---
catalog: module
lean: Polynomial.rootsOfUnityCoset, Polynomial.rootsOfUnityCoset_injective, Polynomial.nodal_rootsOfUnityCoset, Polynomial.nodalWeight_rootsOfUnityCoset, Polynomial.eval_basis_rootsOfUnityCoset, Polynomial.interpolate_rootsOfUnityCoset_periodic
statement: formalized
proof: formalized
---

# Lagrange interpolation on a coset of the `n`-th roots of unity

`CompPoly.ToMathlib.Polynomial.CosetLagrange`, in [CompPoly/ToMathlib/Polynomial/CosetLagrange.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/CosetLagrange.lean), by Thomas Coratger.

> Let `omega` be a primitive `n`-th root of unity, and let `s != 0`.
>
> The points `x_i = s omega^i`, for `i < n`, form the coset `s mu_n`.
>
> - nodal polynomial: it is `X^n - s^n`.
> - barycentric weights: the weight of `x_i` is `x_i / (n s^n)`.
> - Lagrange basis: off the coset, `L_i(x) = (x^n - s^n) x_i / (n s^n (x - x_i))`.
> - periodic functions: with `n = p m`, a function of period `p` interpolates to `Q(X^m)`.
>
> In the last result, `Q` is the interpolant of the same values over the coset `s^m mu_p`.
>
> ```text
>     n = 8, p = 2, m = 4:   f = (a, b, a, b, a, b, a, b) on s mu_8
>                            Q interpolates (a, b) on s^4 mu_2
>                            interpolate(f) = Q(X^4)
> ```
>
> A STARK verifier uses this to evaluate a periodic column out of the domain.
>
> The cost drops from `O(n)` to `O(p)`.
>
> The weights follow Berrut and Trefethen, *Barycentric Lagrange Interpolation*.
>
> That paper appeared in SIAM Review 46(3), 2004.
>
> The folding follows the Plonky3 periodic-column evaluator.

`Polynomial.rootsOfUnityCoset` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/CosetLagrange.lean#L52))

> The points `s omega^i` of the coset `s mu_n`.

```lean
def rootsOfUnityCoset (s ω : F) (n : ℕ) : Fin n → F
```

`Polynomial.rootsOfUnityCoset_injective` (theorem, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/CosetLagrange.lean#L54))

```lean
theorem rootsOfUnityCoset_injective {s ω : F} {n : ℕ} (hω : IsPrimitiveRoot ω n) (hs : s ≠ 0) :
    Function.Injective (rootsOfUnityCoset s ω n)
```

`Polynomial.nodal_rootsOfUnityCoset` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/CosetLagrange.lean#L59))

> The nodal polynomial of `s mu_n` is `X^n - s^n`.

```lean
theorem nodal_rootsOfUnityCoset {s ω : F} {n : ℕ} (hω : IsPrimitiveRoot ω n) (hn : 0 < n) :
    nodal univ (rootsOfUnityCoset s ω n) = X ^ n - C (s ^ n)
```

`Polynomial.nodalWeight_rootsOfUnityCoset` (theorem, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/CosetLagrange.lean#L66))

> The barycentric weight of `x_i = s omega^i` is `x_i / (n s^n)`.

```lean
theorem nodalWeight_rootsOfUnityCoset {s ω : F} {n : ℕ} (hω : IsPrimitiveRoot ω n)
    (hn : (n : F) ≠ 0) (hs : s ≠ 0) (i : Fin n) :
    nodalWeight univ (rootsOfUnityCoset s ω n) i = rootsOfUnityCoset s ω n i / (n * s ^ n)
```

`Polynomial.eval_basis_rootsOfUnityCoset` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/CosetLagrange.lean#L84))

> Off the coset, `L_i(x) = (x^n - s^n) x_i / (n s^n (x - x_i))`.

```lean
theorem eval_basis_rootsOfUnityCoset {s ω x : F} {n : ℕ} (hω : IsPrimitiveRoot ω n)
    (hn : (n : F) ≠ 0) (hs : s ≠ 0) (i : Fin n) (hx : x ≠ rootsOfUnityCoset s ω n i) :
    (Lagrange.basis univ (rootsOfUnityCoset s ω n) i).eval x =
      (x ^ n - s ^ n) *
        (rootsOfUnityCoset s ω n i / (n * s ^ n) * (x - rootsOfUnityCoset s ω n i)⁻¹)
```

`Polynomial.interpolate_rootsOfUnityCoset_periodic` (theorem, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/CosetLagrange.lean#L99))

> A function of period `p` on `s mu_n`, with `n = p m`, interpolates to `Q(X^m)`.
>
> Here `Q` interpolates the same values over the coset `s^m mu_p`.

```lean
theorem interpolate_rootsOfUnityCoset_periodic {s ω : F} {p m : ℕ} [NeZero p]
    (hω : IsPrimitiveRoot ω (p * m)) (hs : s ≠ 0) (hm : 0 < m) (g : Fin p → F) :
    interpolate univ (rootsOfUnityCoset s ω (p * m)) (fun i => g (Fin.ofNat p i)) =
      (interpolate univ (rootsOfUnityCoset (s ^ m) (ω ^ m) p) g).comp (X ^ m)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/ToMathlib/Polynomial/CosetLagrange.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/CosetLagrange.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.Polynomial.CosetLagrange.json)
